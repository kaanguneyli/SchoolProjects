
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# we are printing the part of the straw that is outside the glass
# the equation in range gives the number of outputs that we need
for times in range(int((2*glass_size-straw_pos)/2) + 2):
    for x in range(straw_pos):
        for z in range(x):
            print(' ', end='')
        print('o')
# we are staring to print the glass
    for line in range(glass_size):
        for e in range(line):
            print(' ', end='')
        print('\\', end='')
# with this if else construction the program finds out that should it draw the straw or water
# because the value of 'times' gets bigger the lines that contain straw increase every time
        if line < times:
            for k in range(straw_pos-1):
                print(' ', end='')
            print('o', end='')
            # the equation comes the gap between the point where the straw is and total lenght of the line
            for m in range(2 * glass_size - straw_pos - 2 * line):
                print(' ', end='')
        else:
            for b in range(2 * (glass_size - line)):
                print('*', end='')
        print('/')
# in this part we are drawing the bottom of glass
    for y in range(glass_size):
        print(' ', end='')
    for j in range(2):
        print('-', end='')
    print()
# this part is the stem of the glass
    for g in range(glass_size):
        for h in range(glass_size):
            print(' ', end='')
        for f in range(2):
            print('|', end='')
        print()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


