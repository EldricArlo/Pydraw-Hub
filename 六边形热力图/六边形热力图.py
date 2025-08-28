import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def load_style():
    """加载样式"""
    try:
        plt.style.use("chartlib.mplstyle")
    except:
        pass
    # 设置中文字体，以正常显示中文
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["axes.edgecolor"] = "#ffffff"
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 0

def create_gaussian_points(center, amplitude, sigma_x, sigma_y, num_points):
    """生成二维高斯分布的散点数据"""
    x = np.random.normal(center[0], sigma_x, num_points)
    y = np.random.normal(center[1], sigma_y, num_points)
    z = amplitude * np.exp(
        - (
            (x - center[0]) ** 2 / (2 * sigma_x**2)
            + (y - center[1]) ** 2 / (2 * sigma_y**2)
        )
    )
    return x, y, z

def create_hexbin_chart(ax):
    """生成两个高斯分布的散点数据"""
    np.random.seed(2) # 设置随机种子以保证结果可复现
    num_points = 5000

    # 生成第一个高斯分布数据
    x1, y1, z1 = create_gaussian_points(
        center=(10, 7), amplitude=-50, sigma_x=28,
        sigma_y=25, num_points=num_points
    )

    # 生成第二个高斯分布数据
    x2, y2, z2 = create_gaussian_points(
        center=(25, 12), amplitude=50, sigma_x=27,
        sigma_y=26, num_points=num_points
    )

    # 合并数据
    x = np.concatenate([x1, x2])
    y = np.concatenate([y1, y2])
    z = np.concatenate([z1, z2])
    # 加入随机噪声
    z += np.random.uniform(-25, 25, 2 * num_points) 

    # 自定义颜色映射
    colors = ["#747b9d", "#87b4b9", "#ffffff", "#e9d1ab", "#cd8195"]
    cmap_name = "custom_cmap"
    # 创建颜色映射，N 参数指定颜色分段数量
    cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=256)

    # 使用 hexbin 绘制六边形热力图
    # C=z 用于指定每个点的颜色值，reduce_C_function=np.mean 表示计算每个六边形内的 C 值的平均值
    hb = ax.hexbin(
        x, y, C=z, gridsize=50, cmap=cmap,
        reduce_C_function=np.mean, edgecolors="white", linewidths=0.5
    )

    # 添加颜色条
    # hb 是 mappable 对象，ax 是 colorbar 依附的轴
    fig = ax.get_figure() # 获取当前的 Figure 对象
    cb = fig.colorbar(hb, ax=ax, orientation="vertical", pad=0.01, fraction=0.05)

    # 设置图表标题和轴标签
    ax.set_title("六边形热力图")
    ax.set_xlabel("X 轴")
    ax.set_ylabel("Y 轴")
    
    plt.tight_layout() # 自动调整子图参数，使之更紧凑

if __name__ == "__main__":
    load_style() # 加载自定义样式
    # 创建图形和子图，并指定大小和DPI
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    create_hexbin_chart(ax) # 调用绘制六边形热力图的函数
    plt.show() # 显示图表