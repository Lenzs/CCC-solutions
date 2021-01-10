in_str = input()
index = list(in_str)

grid = [[1, 2], [3, 4]]

for i in range(len(index)):
    if index[i] == "H":
        grid[0], grid[1] = grid[1], grid[0]
    else:
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]


print(str(grid[0][0]) + " " + str(grid[0][1]) + "\n" + str(grid[1][0]) + " " + str(grid[1][1]))



