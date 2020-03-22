def B(grid, row, column) :

    # print(row,column)
    if grid[row][column] != '0':

        grid[row][column] = "v"

        # checking up
        if row >= 1:
            # print("<<<==== checking up ===>>>>")
            if grid[row-1][column] != "v":
                grid = B(grid, row-1,column)


        # checking down
        if row < len(grid)-1:
            # print("<<<==== checking down ===>>>>")
            if grid[row+1][column] != "v":
                grid = B(grid, row+1,column)


        # Checking left
        if column >= 1:
            # print("<<<==== checking left =====>>>")
            if grid[row][column-1] != "v" :
                grid = B(grid, row, column-1)


        # checking right
        if column < len(grid[0])-1:
            # print("<<<==== Checking right ====>>>")
            if grid[row][column+1] != "v":
                grid = B(grid, row, column+1)

    return grid


def numIslands(grid) :
    islands = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == '0' or grid[row][column] == 'v' or grid[row][column] == '1':

                if grid[row][column] != '0' and grid[row][column] != "v":

                    # exit()
                    grid = B(grid, row, column)
                    islands += 1
            else:
                return 0

    print("\n\n")

    for i in grid:
        for j in i:
            print(j,end=" ")
        print("\n",end="")
    return islands


if __name__ == '__main__':
    [n,m] = map(int,input().split())
    grid = []
    for _ in range(n):
        r = input().split()
        grid.append(r)
    result = numIslands(grid)

    print(result)


