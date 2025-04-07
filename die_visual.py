from die import Die


# 创建一个D6骰子
die = Die()

# 掷几次骰子并把结果存在一个列表里
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)