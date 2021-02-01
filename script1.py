n = int(input('До числа:'))
count = 0

for i in range(1, n + 1):
    # b = []
    # while i > 0:
    #     b.append(i % 10)
    #     i = i // 10
    # b = b[::-1]
    b = [*str(i)]
    if len(b) == len(set(b)):
        count += 1
print(count)
