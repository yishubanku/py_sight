from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# 创建一个D6骰子
die = Die()

# 掷几次骰子并把结果存在一个列表里
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout},
             filename='d6.html')