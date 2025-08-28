import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 确保中文正常显示
np.random.seed(24)


# 生成模拟数据
def generate_ore_data(n_samples=100):
    """生成模拟的矿石样本数据"""
    sample_ids = [f"ORE-{i+1:03d}" for i in range(n_samples)]

    # 先全部随机生成
    ore_types = np.random.choice(
        ["磁铁矿", "赤铁矿", "混合矿"], size=n_samples, p=[0.3, 0.4, 0.3]
    )

    fe_contents, si_contents, al_contents = [], [], []
    for ot in ore_types:
        if ot == "磁铁矿":
            fe = np.random.uniform(55, 65)
            si = np.random.uniform(3, 10)
            al = np.random.uniform(1, 3)
        elif ot == "赤铁矿":
            fe = np.random.uniform(40, 55)
            si = np.random.uniform(8, 15)
            al = np.random.uniform(2, 5)
        else:  # 混合矿
            fe = np.random.uniform(25, 40)
            si = np.random.uniform(15, 25)
            al = np.random.uniform(5, 10)
        fe_contents.append(round(fe, 1))
        si_contents.append(round(si, 1))
        al_contents.append(round(al, 1))

    df = pd.DataFrame(
        {
            "样本编号": sample_ids,
            "铁含量": fe_contents,
            "硅含量": si_contents,
            "铝含量": al_contents,
            "矿石类型": ore_types,
        }
    )

    # 把前 10 条替换成固定演示数据
    if n_samples >= 10:
        demo = pd.DataFrame(
            [
                ("ORE-001", 62.3, 4.5, 1.2, "磁铁矿"),
                ("ORE-002", 58.9, 6.8, 2.1, "磁铁矿"),
                ("ORE-003", 45.6, 12.3, 3.5, "赤铁矿"),
                ("ORE-004", 32.1, 20.5, 8.7, "混合矿"),
                ("ORE-005", 59.8, 5.2, 1.8, "磁铁矿"),
                ("ORE-006", 48.3, 10.1, 2.9, "赤铁矿"),
                ("ORE-007", 28.7, 22.4, 9.3, "混合矿"),
                ("ORE-008", 42.9, 14.7, 4.2, "赤铁矿"),
                ("ORE-009", 35.5, 18.9, 7.6, "混合矿"),
                ("ORE-010", 51.2, 8.9, 2.5, "赤铁矿"),
            ],
            columns=["样本编号", "铁含量", "硅含量", "铝含量", "矿石类型"],
        )
        df.iloc[:10] = demo.values
    return df


df = generate_ore_data(100)

# 配色
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

# 创建 3D 散点图
fig = go.Figure()

for i, ore_type in enumerate(df["矿石类型"].unique()):
    subset = df[df["矿石类型"] == ore_type]
    main_color = colors[i % len(colors)]

    fig.add_trace(
        go.Scatter3d(
            x=subset["铁含量"],
            y=subset["硅含量"],
            z=subset["铝含量"],
            mode="markers",
            marker=dict(
                size=5,
                color=main_color,
                opacity=0.8,
                line=dict(width=0.5, color="white"),
            ),
            name=ore_type,
            hovertemplate=(
                "样本编号: %{text}<br>"
                "铁含量: %{x}%<br>"
                "硅含量: %{y}%<br>"
                "铝含量: %{z}%<br>"
                "矿石类型: " + ore_type + "<extra></extra>"
            ),
            text=subset["样本编号"],
        )
    )

# 统一布局
fig.update_layout(
    title={
        "text": "矿石样本成分三维散点图",
        "x": 0.5,
        "y": 0.95,
        "xanchor": "center",
        "yanchor": "top",
        "font": {"size": 20, "color": colors[3]},
    },
    scene=dict(
        xaxis_title="铁含量 (%)",
        yaxis_title="硅含量 (%)",
        zaxis_title="铝含量 (%)",
        xaxis=dict(gridcolor=colors[4], backgroundcolor="rgba(255,255,255,0.7)"),
        yaxis=dict(gridcolor=colors[4], backgroundcolor="rgba(255,255,255,0.7)"),
        zaxis=dict(gridcolor=colors[4], backgroundcolor="rgba(255,255,255,0.7)"),
        camera=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=1.25, y=1.25, z=0.5),
        ),
    ),
    legend=dict(title="矿石类型", font=dict(size=12, color=colors[3]), x=0.05, y=0.95),
    margin=dict(l=0, r=0, b=0, t=50),
    paper_bgcolor="rgba(245,245,245,0.8)",
)

# 输出
fig.write_html("ore_3d_scatter.html")
print("图形已保存为 ore_3d_scatter.html，请手动打开查看")
