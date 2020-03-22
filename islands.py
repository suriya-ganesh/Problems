def B(grid, row, column) :


    if grid[row][column] != '0':

        grid[row][column] = "visited"

        # checking up
        if row >= 1:
            # print("<<<==== checking up ===>>>>")
            if grid[row-1][column] != "visited":
                grid = B(grid, row-1,column)


        # checking down
        if row < len(grid)-1:
            # print("<<<==== checking down ===>>>>")
            if grid[row+1][column] != "visited":
                grid = B(grid, row+1,column)


        # Checking left
        if column >= 1:
            # print("<<<==== checking left =====>>>")
            if grid[row][column-1] != "visited" :
                grid = B(grid, row, column-1)


        # checking right
        if row < len(grid[0])-1:
            # print("<<<==== Checking right ====>>>")
            if grid[row][column+1] != "visited":
                grid = B(grid, row, column+1)

    return grid


def numIslands(grid) :
    islands = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] != '0' and grid[row][column] != "visited":
                # print("i")
                grid = B(grid, row, column)
                islands += 1
                # print(grid)
    return islands


if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    print(n)
    m = int(row[1])
    grid = []
    for _ in range(n):
        r = input().split()
        grid.append(r)
        print(grid)
    result = numIslands(grid)
    print(result)


