import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np
import random
from scipy.interpolate import make_interp_spline

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
    sigma = size / 30 # 控制平滑度
    values = max_value * np.exp(-0.5 * ((x - n) / sigma) ** 2)
    return values

def create_3d_ridgeline_plot(ax):
    """创建三维分层面积图"""
    ## 1. 生成随机数据
    random.seed(4)
    categories = [] # 数据标签
    size = 300
    x_max = 80
    x = np.linspace(0, x_max, size)
    peaks = [8, 15, 23, 30, 35, 40, 53, 60]
    means = [2.5, 1.2, 3.0, 2.5, 1.0, 1.5, 2.0, 2.2]
    y_list = []
    for i in range(8):
        temp_y = 0
        categories.append(f"类别{i+1}")
        for j in range(len(peaks)):
            temp_y += create_data(
                x, x_max, peaks[j], means[j] * random.uniform(0.2, 0.7)
            )
        y_list.append(temp_y)

    # 配色表
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

    ## 2. 绘制三维分层面积图
    def polygon_under_graph(x, y):
        """创建包围数据区域的多边形"""
        return [[x[0], 0], *zip(x, y), [x[-1], 0]]

    verts = []
    zs = np.arange(len(y_list))
    for i, y in enumerate(y_list):
        y_spline = make_interp_spline(x, y) # 使用样条插值
        x_smooth = np.linspace(x.min(), x.max(), 500)
        y_smooth = y_spline(x_smooth)
        verts.append(polygon_under_graph(x_smooth, y_smooth))

    poly = PolyCollection(
        verts, facecolors=colors, alpha=0.5,
        edgecolor="#ffffff", linewidths=1
    )
    ax.add_collection3d(poly, zs=zs, zdir="y")

    # 设置图表标题和标签
    ax.set_title("三维分层面积图") # 图像标题
    ax.set_xlabel("X 轴") # X 轴标签
    ax.set_ylabel("类别") # Y 轴标签
    ax.set_zlabel("数值") # Z 轴标签
    ax.set_xlim(0, 70) # X 轴范围
    ax.set_ylim(0, 8) # Y 轴 (类别) 范围
    ax.set_zlim(0, 3) # Z 轴 (数值) 范围

    # 设置观察角度
    ax.view_init(elev=30, azim=-60)

    # 拉伸方向
    ax.set_box_aspect([3, 2, 1]) # X:Y:Z 的比例

    plt.tight_layout()

if __name__ == "__main__":
    load_style()
    fig = plt.figure(figsize=(8, 5), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    create_3d_ridgeline_plot(ax)
    plt.show()