import numpy as np
import matplotlib.pyplot as plt

# --- 数据生成部分 (与之前相同) ---
n = 20  # 定义网格大小
x_vals = np.linspace(-10, 10, n)
y_vals = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x_vals, y_vals)
Z = 0.5 * X + 0.3 * Y + 5 * np.exp(-(X**2 + Y**2) / 5)

# --- 美化和细腻化绘图部分 ---

# 1. 创建图形和3D坐标轴
fig = plt.figure(figsize=(10, 8)) # 调整图形窗口大小，提供更多空间
ax = fig.add_subplot(111, projection='3d') # 等同于 plt.subplots(1, 1, subplot_kw={'projection': '3d'})

# 2. 绘制表面图并进行美化
#    cmap: 选择更细腻或具有对比度的颜色映射，如 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
#    linewidth: 控制边缘线的宽度
#    antialiased: 设置为 True 可以使边缘和表面更平滑 (抗锯齿)
#    rstride, cstride: 控制行步长和列步长，用于采样表面网格，较小的步长会显示更多网格线，但可能显得杂乱。
#                       通常保持默认或设置为 1。
#    shade: 控制表面光照。通常为 True 或 False。如果为 True，会根据灯光和表面法线计算阴影。
#    alpha: 控制表面的透明度 (0.0 到 1.0)
surf = ax.plot_surface(X, Y, Z,cmap='viridis',        # 颜色映射，这里用 viridis，你可以尝试 'plasma', 'inferno' 等
                    linewidth=0.5,antialiased=True,   # 边缘线宽度,抗锯齿处理，使边缘和表面更平滑
                    shade=True,alpha=0.8)             # 显示表面阴影，增强立体感,设置表面透明度为 80%

# 3. 调整坐标轴外观
ax.set_title('Refined 3D Surface Plot with Custom Styling', fontsize=16, fontweight='bold')
ax.set_xlabel('X-axis', fontsize=12, labelpad=10) # labelpad 增加标签与轴的距离
ax.set_ylabel('Y-axis', fontsize=12, labelpad=10)
ax.set_zlabel('Z-axis', fontsize=12, labelpad=10)

# 可以调整刻度标签的字体大小
# ax.tick_params(axis='both', which='major', labelsize=10)

# 4. 设置相机视角 (俯仰角 elevation, 方位角 azimuth)
#    从不同角度观察，可以更好地展示曲面的形状
#    例如：ax.view_init(elev=30., azim=-60.) # 示例视角
#    我们先用默认视角，你也可以尝试调整
# ax.view_init(elev=20., azim=30.) # 尝试一个比较常见的视角

# 5. 添加和美化颜色条
#    shrink 和 aspect 用于控制颜色条的大小和长宽比
#    orientation 可以设置为 'horizontal'
cbar = fig.colorbar(surf, shrink=0.6, aspect=10, pad=0.1) # pad 调整颜色条与绘图区域的距离
cbar.set_label('Z Value', fontsize=12) # 设置颜色条的标签

# 6. 移除默认的坐标轴网格线 (可选，因为 surf 本身有网格)
# ax.grid(False) # 如果想彻底移除 Matplotlib 的轴网格线

# 7. 调整布局以防止标签重叠
plt.tight_layout()

# 显示图形
plt.show()