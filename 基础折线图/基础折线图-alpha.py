import matplotlib.pyplot as plt

# 设置中文显示，确保标题和标签能正常显示中文
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False # 解决负号显示问题

# 准备数据 - 滨海市2010-2020年气温数据
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
avg_temps = [15.2, 14.8, 15.5, 15.0, 15.6, 15.8, 16.0, 15.9, 16.2, 16.1, 16.3]
max_temps = [38, 37, 39, 38, 40, 39, 41, 40, 42, 40, 41]
min_temps = [-6, -8, -5, -7, -4, -5, -3, -6, -4, -5, -3]

# 创建图形对象，设置画布大小为12*7英寸
plt.figure(figsize = (12, 7))

# 绘制平均气温折线图
# color = "bule" 蓝色线条
# linestyle = '-' 实线样式
# marker = 'o' 圆形数据标记
# linewidth = 2.5 线条宽度设置为2.5
# markersize = 7 标记大小为7
# label 图例文本
plt.plot(year, avg_temps, color = "blue", linestyle = '-', marker = 'o',
        linewidth = 2.5, markersize = 7, label = '平均气温（摄氏度）')

# 绘制最高气温折线图
# color = 'red' 红色线条
# linestyle = '--' 虚线样式
plt.plot(year, max_temps, color = 'red' , linestyle = '--',
         marker = 'o', linewidth = 2.5, markersize = 7, label = '最高气温（摄氏度）')

# 绘制最低气温折线图
# color = 'green' 绿色线条
# linestyle = '-.'
plt.plot(year, min_temps, color = 'green', linestyle = '-.',
         marker = 'o', linewidth = 2.5, markersize = 7, label = '最低气温（摄氏度）')

# 添加标题，设置为黑体加粗，字号为16
plt.title('滨海市2010-2020年气温变换趋势', fontweight = 'bold', fontsize = 16)

# 添加坐标轴标签，字号设置为14
plt.xlabel('年份', fontsize = 14)
plt.ylabel('气温（摄氏度）', fontsize = 14)

# 添加网格线，使用虚线样式，透明度0.7使图标更清晰
plt.grid(True, linestyle = '--', alpha = 0.7)

# 添加图例，字体大小12，位置自动选择最佳位置
plt.legend(fontsize = 12, loc = 'best')

# 设置坐标轴刻度，x轴标签旋转45度以便更好显示年份
plt.xticks(year, rotation = 45)
plt.yticks(fontsize = 11) # 调整y轴刻度字体大小

# 为平均气温添加数据标签，显示具体数据
# x, y + 0.3 标签位置在数据点上方0.3单位处
# ha = 'center' 水平居中对齐
for x, y in zip(year, avg_temps):
    plt.text(x, y + 1, f"{y}", ha = 'center', fontsize = 10, color = 'red')

# 为最高气温添加数据标签
for x, y in  zip(year, max_temps):
    plt.text(x, y + 1, f'{y}', ha = 'center', fontsize = 10, color = 'red')

# 为最低气温添加数据标签
for x, y in zip(year, min_temps):
    plt.text(x, y + 1, f'{y}', ha = 'center', fontsize = 10, color = 'green')

# 显示图形
plt.show()