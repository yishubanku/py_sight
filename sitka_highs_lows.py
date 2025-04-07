import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 指定中文字体，否则会出现显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']

# 根据最高温度绘制图形
# plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title("2018年每日最高和最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('温度 (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()