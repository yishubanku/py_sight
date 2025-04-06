import matplotlib.pyplot as plt


# 指定中文字体，否则会出现显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax = plt.subplots()

# 自定义颜色，方法一，形参c
# ax.scatter(x_values, y_values, c='green', s=10)
# 自定义颜色，方法二，形参c
# ax.scatter(x_values, y_values, c=[(0, 0.8, 0)], s=10)
# 自定义颜色，方法一，形参color
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()