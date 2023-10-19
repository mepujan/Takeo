with open("pujan.txt", 'r') as file:
    # reading each line of file
    for each_line in file:
        # looping each word of file and seperating them with white space using split() method
        for word in each_line.split():
            print(word)
