# 1: factorial


def main():
    t = int(input())
    i = 1
    while i <= t:
        n = int(input())
        print(factorial(n))
        i += 1

# Return the factorial for a specified number 
def factorial(n):
    if n <= 13:
        return factorialHelper(n, 1) # Call auxiliary function    
    return 'input too large'
  
# Auxiliary tail-recursive function for factorial 
def factorialHelper(n, result):
    if n == 0:
        return result
    else:
        return factorialHelper(n - 1, n * result) # Recursive call

# main() # Call the main function

# 2:  Fibonacci numbers

def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number - 1) + fib(number - 2) 

# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(10))

# 3:  Towers of Hanoi
def hanoi(n):
    nr_moves = 0
    
    total_moves, pos_disc_1 = move_disc(n, "A")
    
    print(str(total_moves) + " moves needed")
    
    
def move_disc(n, pos_disc_1):
    nr_moves = 0
    if n > 1:
        extra_moves, pos_disc_1 = move_disc(n-1, pos_disc_1)
        if n % 2 == 0 and pos_disc_1 == "A":
            print("Disc " + str(n) + " from C to B")
        elif n % 2 == 0 and pos_disc_1 == "B":
            print("Disc " + str(n) + " from A to C")
        elif n % 2 == 0 and pos_disc_1 == "C":
            print("Disc " + str(n) + " from B to A")
        elif n % 2 == 1 and pos_disc_1 == "A":
            print("Disc " + str(n) + " from B to C")
        elif n % 2 == 1 and pos_disc_1 == "B":
            print("Disc " + str(n) + " from C to A")
        elif n % 2 == 1 and pos_disc_1 == "C":
            print("Disc " + str(n) + " from A to B")

        # print(n)
        extra_moves, pos_disc_1 = move_disc(n-1, pos_disc_1)
        nr_moves += 2 * extra_moves + 1 
        return nr_moves, pos_disc_1
    elif n == 1:
        if pos_disc_1 == "A":
            print("Disc 1 from A to B")
            pos_disc_1 = "B"
        elif pos_disc_1 == "B":
            print("Disc 1 from B to C")
            pos_disc_1 = "C"
        elif pos_disc_1 == "C":
            print("Disc 1 from C to A")
            pos_disc_1 = "A"
        nr_moves += 1
        return nr_moves, pos_disc_1
    else:
        return 

    
    # print("Move disc" + discnumber + "from pole"  + source + " to pole " + destination + ".")
    # current_nr_moves += 1
    # move_disc(target_disc - 1, source, current_nr_moves)

hanoi(4)


# 4: Palindrome
def isPalindroom(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return isPalindroom(string[1:-1])
    else:
        return False
