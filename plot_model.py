import csv
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def read_coords_from_csv(file_name):
    coords = []
    with open(f'csv/{file_name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            coords.append(tuple(map(float, row)))  # Convert each entry to float and append
    return coords


# FILE_NAME = '10054_Whale_v2_L3'
# FILE_NAME = '12140_Skull_v3_L2'
# FILE_NAME = '10050_RattleSnake_v4_L3'
# FILE_NAME = '12328_Statue_v1_L2'
# FILE_NAME = '10042_Sea_Turtle_V2_iterations-2'
FILE_NAME = '12222_Cat_v1_l3'

# CSVファイルから座標を読み込む
coords = read_coords_from_csv(FILE_NAME)

# 座標をx, y, zのリストに分解
x = [coord[0] for coord in coords]
y = [coord[1] for coord in coords]
z = [coord[2] for coord in coords]

# プロットの準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 散布図を作成
ax.scatter(x, y, z)

# 軸ラベルの追加
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 表示
plt.show()
