# ===========================================================
#  文件名：marginal_histograms.py
#  描  述：二维正态样本 + 边缘直方图（代码与注释分离版）
#  依  赖：matplotlib ≥ 3.6，numpy
# ===========================================================

# region 1. 基础库导入 --------------------------------------
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
# endregion

# region 2. 随机数生成 --------------------------------------
np.random.seed(24)
mean = [0, 0]
cov  = [[2, -1], [-1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 1000).T
# endregion

# region 3. 画布与布局 --------------------------------------
fig  = plt.figure(figsize=(8, 5))
grid = plt.GridSpec(4, 6)
ax_main = fig.add_subplot(grid[1:4, 0:5])  # 主散点图
ax_x    = fig.add_subplot(grid[0,   0:5])  # x 轴上方直方图
ax_y    = fig.add_subplot(grid[1:4, 5])    # y 轴右侧直方图
# endregion

# region 4. 绘制图形 ----------------------------------------
# 4-a 散点图
ax_main.plot(x, y, "o", color="#c0627a", markersize=3, alpha=0.5)

# 4-b x 轴直方图
ax_x.hist(x, 50, color="#c0627a", edgecolor="#f5d9dd")
ax_x.set_xticks([])
ax_x.yaxis.set_major_locator(MultipleLocator(25))
ax_x.grid()

# 4-c y 轴直方图
ax_y.hist(y, 25, orientation="horizontal",
          color="#c0627a", edgecolor="#f5d9dd")
ax_y.xaxis.set_major_locator(MultipleLocator(25))
ax_y.set_yticks([])
ax_y.grid()
# endregion

# region 5. 坐标同步与输出 ----------------------------------
ax_x.set_xlim(ax_main.get_xlim())
ax_y.set_ylim(ax_main.get_ylim())
fig.set_layout_engine('tight')
plt.show()
# endregion

# ===========================================================
#  逐行中文解释（与代码分离，方便折叠或文档化）
# ===========================================================
# 行  7- 9：导入绘图与数值计算库；MultipleLocator 用于设置刻度间隔
# 行 12   ：固定随机种子，保证结果可复现
# 行 13-15：定义二维正态分布参数，并抽取 1000 个样本
# 行 18-23：创建 8×5 英寸画布；GridSpec 4×6 网格，
#           分别放置主图、x 轴直方图、y 轴直方图
# 行 26-27：主图绘制散点，圆形标记、玫红色、半透明
# 行 30-34：x 轴上方直方图：50 个 bin、隐藏 x 刻度、y 轴刻度间隔 25、开网格
# 行 37-42：y 轴右侧直方图：水平方向、25 个 bin、隐藏 y 刻度、x 轴刻度间隔 25、开网格
# 行 45-46：将直方图坐标范围与主图同步，使视觉对齐

# 行 47-48：tight_layout 自动调整子图间距，最后显示图形