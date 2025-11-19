def hanoi(n):
    def move(size, start, end, temp):
        nonlocal moves
        if size == 1:
            print(f"Move disc 1 from pole {start} to pole {end}.")
            moves += 1
        else:
            move(size - 1, start, temp, end)
            print(f"Move disc {size} from pole {start} to pole {end}.")
            moves += 1
            move(size - 1, temp, end, start)

    moves = 0
    move(n, 'A', 'C', 'B')
    print(f"{moves} moves needed")