# minesweeper game played in the terminal
# do layout first
# Printing the Minesweeper Layout
import random

def print_mines_layout():
    global mine_values
    global n
 
    print()
    print("\t\t\tMINESWEEPER\n")
 
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
 
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
         
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()
    
def set_mines():
    global numbers
    count = 0
    # get random number tied to number of tiles possible, add to appropriate col/row, and continue until correct number of mines has been placed
    
    while count < mines_no:
        mine_pos = random.randint(0, n*n - 1)
        
        row = mine_pos//n
        col = mine_pos%n
        
        if numbers[row][col] != -1:
            numbers[row][col] = -1
            count += 1
    
    
def main():
    set_mines()
    print_mines_layout()

if __name__ == "__main__":
    
    mines_no = 8;
    
    n = 8;
    
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    
    numbers = [[0 for y in range(n)] for x in range(n)]
    
    main()