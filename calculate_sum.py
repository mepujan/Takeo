sum = 0

# calculating sum of even number ranges from 1 to 100
for num in range(1, 101):
    if num % 2 == 0:
        sum += num
print("The sum is : ", sum)
