rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i+1):
        print('*', end = ' ')
    print("")

    total_sum = 0

for i in range(1, 5):
    total_sum = total_sum + i

print(total_sum)

