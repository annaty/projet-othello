
for row in range(0,9):
    if row == 0:
        print("  ", end="")
        for index in range(1,9):                
                print(index, end=" ")
        print()
    else :
        print(row, end=" ")
        for dot in range(0,8):
            print(".", end=" ")
        print()
