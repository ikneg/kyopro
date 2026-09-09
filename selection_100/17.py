def dfs(cnt):
    if cnt == 8:
        for i in board:
            print("".join(i))

        return True
    for r in range(8):
        if "Q" not in board[r]:
            for c in range(8):
                if canPut(r, c):
                    board[r][c] = "Q"
                    if dfs(cnt+1):
                        return True

                    board[r][c] = "."

def canPut(row, col):
    for r in range(8):
        for c in range(8):
            if board[r][c] == "Q":
                if col == c:
                    return False

                if abs(row - r) == abs(col - c):
                    return False

    return True

k = int(input())
board = [["."] * 8 for _ in range(8)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = "Q"

dfs(k)
