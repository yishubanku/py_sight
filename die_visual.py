from die import Die


# 创建一个D6骰子
die = Die()

# 掷几次骰子并把结果存在一个列表里
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)