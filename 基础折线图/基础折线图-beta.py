import matplotlib.pyplot as plt

# 设置中文字体与负号
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 数据
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
avg_temps = [15.2, 14.8, 15.5, 15.0, 15.6, 15.8, 16.0, 15.9, 16.2, 16.1, 16.3]
max_temps = [38, 37, 39, 38, 40, 39, 41, 40, 42, 40, 41]
min_temps = [-6, -8, -5, -7, -4, -5, -3, -6, -4, -5, -3]

plt.figure(figsize=(12, 7))

# 绘制三条折线
plt.plot(year, avg_temps, color="blue", linestyle="-", marker="o",
         linewidth=2.5, markersize=7, label="平均气温（℃）")
plt.plot(year, max_temps, color="red", linestyle="--", marker="o",
         linewidth=2.5, markersize=7, label="最高气温（℃）")
plt.plot(year, min_temps, color="green", linestyle="-.", marker="o",
         linewidth=2.5, markersize=7, label="最低气温（℃）")

# 标题与坐标轴
plt.title("滨海市2010-2020年气温变化趋势", fontweight="bold", fontsize=16)
plt.xlabel("年份", fontsize=14)
plt.ylabel("气温（℃）", fontsize=14)

# 网格
plt.grid(True, linestyle="--", alpha=0.3)

# 图例
plt.legend(fontsize=12, loc="upper left", framealpha=0.8)

# 坐标轴刻度
plt.xticks(year, rotation=45)
plt.yticks(fontsize=11)

# 设置 y 轴范围，确保所有标签可见
plt.ylim(-12, 47)

# 为每条曲线添加数据标签，位置根据曲线范围微调
for x, y in zip(year, avg_temps):
    plt.text(x, y + 0.5, f"{y}", ha="center", va="bottom", fontsize=9, color="blue")

for x, y in zip(year, max_temps):
    plt.text(x, y + 0.8, f"{y}", ha="center", va="bottom", fontsize=9, color="red")

for x, y in zip(year, min_temps):
    plt.text(x, y - 1.2, f"{y}", ha="center", va="top", fontsize=9, color="green")

plt.tight_layout()
plt.show()