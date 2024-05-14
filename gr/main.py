import time_check

def get_shift():
    print('What shift do you want to see?\nType:\n')
    print('1 - for first\n2 - for second\n3 - for third\n')
    return input()

def main():
    print()
    time_check.do_time_check(shift)

if __name__ == "__main__":
    shift = get_shift()
    main()