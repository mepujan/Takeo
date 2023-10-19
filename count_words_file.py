with open("pujan.txt", 'r') as file:
    # reading each line of file
    count = 0
    for each_line in file:
        # looping each word of file and seperating them with white space using split() method
        # and incrementing the count
        for word in each_line.split():
            count += 1
print("Number of words = ", count)
