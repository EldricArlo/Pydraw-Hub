import plotly.graph_objects as go
import numpy as np

# 构造网格及高度数据
rows, cols = 32, 22
x = np.linspace(-1, 1, cols)
y = np.linspace(-1.7, 1.3, rows)
X, Y = np.meshgrid(x, y)
Z = np.exp(-((X+0.5)**2 + (Y+0.5)**2) / 0.7) * 1.5 + np.exp(-((X-0.5)**2 + (Y-0.5)**2) / 0.3)

# 定义自定义颜色色系
# 原图的定义方式会创建一个额外的嵌套列表，Plotly期望的是直接的 [值, 颜色] 对列表
colorscale_custom = [
    [0.0, "#2f648e"],
    [0.5, "#e9d1ab"],
    [1.0, "#c3476a"]
]

# 设置网格线密度: 通过调整 start、end 和 size 控制网格的间隔
fig = go.Figure(data=[go.Surface(
    x=X, y=Y, z=Z,
    colorscale=colorscale_custom,
    contours={
        "x": {"show": True, "color": "white", "width": 1,
        "start": x.min(), "end": x.max(), "size": 0.1},
        "y": {"show": True, "color": "white", "width": 1,
        "start": y.min(), "end": y.max(), "size": 0.1}
    }
)])

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

fig.show()