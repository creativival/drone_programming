import numpy as np

def generate_sphere_coordinates(num_points, radius):
    indices = np.arange(0, num_points, dtype=float) + 0.5

    phi = np.arccos(1 - 2 * indices / num_points)
    theta = np.pi * (1 + 5**0.5) * indices

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return list(zip(x, y, z))

# 200のドローンと半径10の球を使用
drones_positions = generate_sphere_coordinates(200, 10)

# 結果を表示
for position in drones_positions:
    print(position)
