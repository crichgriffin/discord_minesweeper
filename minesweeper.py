import random

num2words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: '9ine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}



def place_mines(n,k):
    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        arr[y][x] = 'X'
    return arr

def count_mines(arr):
    # -1 because of zero indexing
    n_y = len(arr[0]) -1 # length of row one
    n_x = len(arr) -1 # how many rows
    # +1 because how range works
    for x in range(n_x + 1):
        for y in range(n_y +1):
            if arr[x][y] == 'X':
                if x != 0 and arr[x-1][y] !='X':
                    arr[x-1][y] += 1 # top centre
                if x != n_x and arr[x+1][y] !='X':
                    arr[x+1][y] += 1 # bottom centre

                if y !=0 and x!=0 and arr[x-1][y-1] !='X':
                    arr[x - 1][y-1] += 1 # top left
                if y!= 0 and arr[x][y-1] !='X':
                    arr[x][y - 1] += 1 #  centre left
                if y != 0 and x != n_x and arr[x+1][y-1] !='X':
                    arr[x + 1][y - 1] += 1  # bottom left

                if y != n_y and x != 0:
                    if arr[x-1][y+1] !='X':
                        arr[x - 1][y+1] += 1 # top right
                if y != n_y:
                    if arr[x][y+1] !='X':
                        arr[x][y + 1] += 1 # centre right
                if y != n_y and x != n_x:
                    if arr[x+1][y+1] !='X':
                        arr[x + 1][y + 1] += 1  # bottom right
    return arr



def convert_val_to_discord(x, boom_string):
    if isinstance(x, int):
        if x is 0:
            y = ":" + num2words[x] + ":"
        else:
            y = "||:" + num2words[x] + ":||"
    elif x is 'X':
        y = "||:" + boom_string + ":||"
    return y


def discord_minesweeper(x, y):
    grid = place_mines(x, y)
    grid = count_mines(grid)
    for row in grid:
        print("\t".join(convert_val_to_discord(cell, "rainbow_heart") for cell in row))


if __name__ == "__main__":
    # beginner
    discord_minesweeper(6, 12)  # intermediate
    # minesweeper(8, 20)  # advanced
