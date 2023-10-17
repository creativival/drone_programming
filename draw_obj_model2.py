import pywavefront
import random
import numpy as np
import csv

# FILE_NAME = '10054_Whale_v2_L3'  # https://free3d.com/3d-model/whale-v4--501429.html
# FILE_NAME = '12140_Skull_v3_L2'  # https://free3d.com/3d-model/skull-v3--785914.html
# FILE_NAME = '10050_RattleSnake_v4_L3'  # https://free3d.com/3d-model/rattlesnake-v04--784635.html
# FILE_NAME = '12328_Statue_v1_L2'  # https://free3d.com/3d-model/statue-v1--541832.html
# FILE_NAME = '10042_Sea_Turtle_V2_iterations-2'  # https://free3d.com/3d-model/-sea-turtle-v1--427786.html
# FILE_NAME = '12222_Cat_v1_l3'  # https://free3d.com/3d-model/cat-v1--326682.html
# FILE_NAME = '3854523_WhaleOBJ'  # https://www.cgtrader.com/3d-models/animals/mammal/humpback-whale-animated-19a45729-340b-4420-8da2-ac557ff4fab6
FILE_NAME = 'whale_animation10'

# Set the log level to suppress warnings
pywavefront.configure_logging(level="ERROR")

def random_point_on_triangle(v1, v2, v3):
    """Return a random point on a triangle defined by vertices v1, v2, and v3."""
    s, t = sorted([random.random(), random.random()])
    return (s * v1[0] + (t - s) * v2[0] + (1 - t) * v3[0],
            s * v1[1] + (t - s) * v2[1] + (1 - t) * v3[1],
            s * v1[2] + (t - s) * v2[2] + (1 - t) * v3[2])

def triangle_area(v1, v2, v3):
    """Return the area of a triangle defined by vertices v1, v2, and v3."""
    return 0.5 * np.linalg.norm(np.cross(np.array(v2) - np.array(v1), np.array(v3) - np.array(v1)))

def sample_points_from_mesh(mesh, num_points):
    """Sample num_points from the surface of the given mesh."""
    points = []

    # Calculate areas for all triangles
    areas = [triangle_area(*[mesh.vertices[face[i]] for i in range(3)]) for face in mesh.mesh_list[0].faces]
    total_area = sum(areas)
    probabilities = [area / total_area for area in areas]

    while len(points) < num_points:
        # Select a triangle based on its area
        face_index = np.random.choice(len(mesh.mesh_list[0].faces), p=probabilities)
        face = mesh.mesh_list[0].faces[face_index]
        vertices = [mesh.vertices[face[i]] for i in range(3)]
        point = random_point_on_triangle(*vertices)
        points.append(point)

    return points

# Load the 3D model
print(FILE_NAME)
mesh = pywavefront.Wavefront(f'model/{FILE_NAME}.obj', collect_faces=True)

# Sample 200 points from the surface of the model
sampled_points = sample_points_from_mesh(mesh, 800)

# Save the sampled points to a CSV file
with open(f'csv/{FILE_NAME}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["X", "Y", "Z"])  # Header row
    for point in sampled_points:
        writer.writerow(point)
