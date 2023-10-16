import pywavefront
import random
import numpy as np


def random_point_on_triangle(v1, v2, v3):
    """Return a random point on a triangle defined by vertices v1, v2, and v3."""
    s, t = sorted([random.random(), random.random()])
    return (s * v1[0] + (t - s) * v2[0] + (1 - t) * v3[0],
            s * v1[1] + (t - s) * v2[1] + (1 - t) * v3[1],
            s * v1[2] + (t - s) * v2[2] + (1 - t) * v3[2])


def sample_points_from_mesh(mesh, num_points):
    """Sample num_points from the surface of the given mesh."""
    points = []
    while len(points) < num_points:
        # Select a random face
        face = random.choice(mesh.mesh_list[0].faces)

        vertices = [mesh.vertices[face[i]] for i in range(3)]
        point = random_point_on_triangle(*vertices)
        points.append(point)

    return points


# Load the 3D model
mesh = pywavefront.Wavefront('model/10054_Whale_v2_L3.obj', collect_faces=True)

# Sample 200 points from the surface of the model
sampled_points = sample_points_from_mesh(mesh, 800)

# Print the sampled points
for point in sampled_points:
    print(point)
