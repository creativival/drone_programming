import numpy as np

def generate_ellipsoid_coordinates(num_points, a, b, c):
    indices = np.arange(0, num_points, dtype=float) + 0.5

    phi = np.arccos(1 - 2 * indices / num_points)
    theta = np.pi * (1 + 5**0.5) * indices

    x = a * np.sin(phi) * np.cos(theta)
    y = b * np.sin(phi) * np.sin(theta)
    z = c * np.cos(phi)

    return list(zip(x, y, z))

# 金魚の形を簡略化して、主軸が10、10、5の楕円体として近似
drones_positions = generate_ellipsoid_coordinates(200, 10, 10, 5)

# 結果を表示
for position in drones_positions:
    print(position)
