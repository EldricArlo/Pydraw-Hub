import matplotlib.pyplot as plt
import numpy as np
import random

def load_style():
    """加载样式"""
    try:
        plt.style.use("chartlib.mplstyle")
    except:
        pass
    # 设置中文字体，以正常显示中文
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["grid.color"] = "#fed2d2"

def create_data(x, size, n, max_value):
    """通过高斯函数生成一组平滑数据"""
    sigma = size / 25 # 控制平滑度
    values = max_value * np.exp(-0.5 * ((x - n) / sigma) ** 2)
    return values

def create_polar_stacked_area_chart(ax):
    """创建极坐标堆叠面积图"""

    ## 1. 生成随机数据
    random.seed(1)
    categories = [] # 数据标签
    size = 300
    x_max = 2 * np.pi
    theta = np.linspace(0, 2 * np.pi, size) # 使用 theta 作为角度
    peaks = np.array([0, 10, 23, 30, 40, 55, 73, 80]) / 80 * 2 * np.pi
    means = [0, 2.2, 3.0, 2.5, 2.5, 2.5, 2.0, 0]

    y_list = []
    r_circle = 5
    for i in range(8):
        temp_y = 0
        categories.append(f"类别{i+1}")
        for j in range(len(peaks)):
            temp_y += create_data(
                theta, x_max, peaks[j], means[j] * random.random() * 0.5
            )
        if i == 0:
            temp_y += r_circle # 使得第一层从 r_circle 处开始
        y_list.append(temp_y)

    colors = [
        "#214e81",
        "#456991",
        "#6983a2",
        "#8d9eb2",
        "#b59fb1",
        "#dc9fb0",
        "#cf8d9e",
        "#c2768b",
    ]

    ## 2. 绘制极坐标堆叠面积图
    polys = ax.stackplot(theta, y_list, colors=colors, labels=categories, zorder=10)

    # 提取边界线
    for poly in polys:
        verts = poly.get_paths()[0].vertices
        ax.plot(verts[:, 0], verts[:, 1], color="#ffffff", zorder=20, linewidth=1)

    # 在中间添加一个白色的圆环区域
    theta_circle = np.linspace(0, 2 * np.pi, 100)
    ax.fill(theta_circle, np.full(100, r_circle - 0.2), color="white", zorder=10)

    # 设置图例
    legend = ax.legend(
        loc="center",
        ncols=1,
        prop={"weight": "bold"},
        bbox_to_anchor=(1.2, 0.5),
        handlelength=1,
        handleheight=1,
        # Removed invalid parameters: color="#ffffff", zorder=10
    )
    # Correct way to set legend frame edge color
    legend.get_frame().set_edgecolor("#ffffff")

    # 设置网格和标签
    ax.text(
        0,
        0,
        "极坐标堆叠面积图",
        zorder=20,
        ha="center",
        va="center",
        fontweight="bold",
        fontsize=12,
    )
    ax.set_yticklabels([]) # 隐藏径向向标签

    plt.tight_layout()

if __name__ == "__main__":
    load_style()
    # Corrected: plt.subplots returns a tuple (fig, ax) which should be unpacked
    fig, ax = plt.subplots(figsize=(8, 5), subplot_kw={"projection": "polar"}, dpi=150)
    # Removed the incorrect line: ax = fig
    create_polar_stacked_area_chart(ax)
    plt.show()