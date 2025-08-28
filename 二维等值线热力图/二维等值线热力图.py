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
    # 自定义样式
    plt.rcParams["axes.edgecolor"] = "#ffffff"
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 0

def create_gaussian_data(center_x, center_y, value):
    # 注意: 这里的 x, y 是在函数内部定义的，并用于生成 X, Y 配合当前高斯函数
    # 它们是局部变量，与 create_chart 中定义的 X, Y 网格范围是匹配的。
    x = np.linspace(-4.0, 4.0, 100)
    y = np.linspace(-4.0, 4.0, 100)
    X, Y = np.meshgrid(x, y)
    return value * np.exp(-((X - center_x) ** 2 + (Y - center_y) ** 2))

def create_chart(ax):
    """创建等值线热力图"""
    # 定义绘图的网格尺寸
    x = np.linspace(-4.0, 4.0, 100)
    y = np.linspace(-4.0, 4.0, 100)
    X, Y = np.meshgrid(x, y)

    # 初始化 Z 并叠加多个高斯分布
    # 第一次调用 create_gaussian_data 会基于上面定义的 X, Y 生成第一个高斯分布
    Z = create_gaussian_data(-2, 3, -5)
    Z += create_gaussian_data(-3, 1.5, -2)
    Z += create_gaussian_data(-1, -2, 1)
    Z += create_gaussian_data(1, -2, 2)
    Z += create_gaussian_data(-3, -3, -3)
    Z += create_gaussian_data(1, 1, 2)
    Z += create_gaussian_data(1, 3.5, 1)
    Z += create_gaussian_data(3, -2.5, 2)
    Z += create_gaussian_data(3, 2, 2)

    # 创建主要的等高线填充 (热力图区域)
    # 自定义颜色映射
    colors = ["#515a85", "#69a1a7", "#e4c696", "#c0627a"] # 定义颜色列表
    n_bins = 300 # 使用多少个颜色分段
    cmap_name = "my_custom_cmap"

    # 创建颜色映射
    # 修正: 将 N_n_bins 改为 N=n_bins
    cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

    # 绘制填充等高线
    contour = ax.contourf(X, Y, Z, levels=50, cmap=cmap)
    # 绘制等高线，并设置线条颜色和宽度
    contour_lines = ax.contour(X, Y, Z, levels=15, colors="#ffffff", linewidths=0.8)
    # 在等高线上添加标签
    ax.clabel(contour_lines, inline=True, fontsize=8, fmt="%.2f")

    # 添加 colorbar (颜色条)
    # 需要传入 fig 对象，因为 colorbar 是 Figure 级别的对象，但这里直接 ax=ax 也可以在当前 Axes 附近绘制
    # (注意：通常 fig.colorbar 的第一个参数是 mappable，即 contourf 返回的对象)
    fig = ax.get_figure() # 获取当前的 figure 对象
    fig.colorbar(contour, ax=ax, pad=0.01, fraction=0.05)

    # 设置图表标题和轴标签
    ax.set_title("等值线热力图")
    ax.set_xlabel("X 轴")
    ax.set_ylabel("Y 轴")
    
    plt.tight_layout() # 自动调整子图参数，使之更紧凑

if __name__ == "__main__":
    load_style() # 加载自定义样式
    # 创建图形和子图，这里的 fig, ax = plt.subplots(...) 是正确的解包方式
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    create_chart(ax) # 调用绘图函数
    plt.show() # 显示图表