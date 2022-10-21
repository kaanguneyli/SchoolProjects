
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# we are taking the nested list form of the ppm and the max value
img_lst = read_ppm_file(filename)[0]
max_1 = read_ppm_file(filename)[1]
# in this operation we are doing the necessary calculation for every channel value in every pixel with for loops and...
# rounding it to 4
if operation == 1:
    minimum = int(input())
    maximum = int(input())
    for i in range(len(img_lst)):
        for j in range(len(img_lst[i])):
            for k in range(len(img_lst[i][j])):
                img_lst[i][j][k] = round(((img_lst[i][j][k] - 0)*(maximum - minimum)) / (max_1 - 0) + minimum, 4)
    img_printer(img_lst)


def channel_mean(num, lst=img_lst, pixel=0, channel_sum=0):
    # in this function we are finding channelwise means by summing all the values and dividing it to the amount of...
    # pixels, which is also found by the for loop
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            channel_sum += img_lst[i][j][num]
            pixel += 1
    return channel_sum / pixel


def channel_standard_deviation(num, lst=img_lst, pixel=0, difference_sum=0):
    # this function helps us to find the standard deviation of a channel. It uses values for mean from the previous...
    # function. It also finds the number of pixels the same way. Then it does the necessary calculation using the ...
    # mean value for given channel
    global red_mean
    global green_mean
    global blue_mean
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            pixel += 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if num == 0:
                difference_sum += (img_lst[i][j][0] - red_mean)**2
            if num == 1:
                difference_sum += (img_lst[i][j][1] - green_mean)**2
            if num == 2:
                difference_sum += (img_lst[i][j][2] - blue_mean)**2
    return (difference_sum / pixel) ** 0.5


if operation == 2:
    # here we find the means and standard deviations of each channel, with the functions given above
    red_mean = channel_mean(0)
    green_mean = channel_mean(1)
    blue_mean = channel_mean(2)
    sd_red = channel_standard_deviation(0) + 10**(-6)
    sd_green = channel_standard_deviation(1) + 10**(-6)
    sd_blue = channel_standard_deviation(2) + 10**(-6)
    # with this for loop we make the calculations for every pixel and then we round it to 4
    for i in range(len(img_lst)):
        for j in range(len(img_lst[i])):
            img_lst[i][j][0] = round((img_lst[i][j][0] - red_mean) / sd_red, 4)
            img_lst[i][j][1] = round((img_lst[i][j][1] - green_mean) / sd_green, 4)
            img_lst[i][j][2] = round((img_lst[i][j][2] - blue_mean) / sd_blue, 4)
    img_printer(img_lst)

if operation == 3:
    # with these loops we reach the pixels
    for i in range(len(img_lst)):
        for j in range(len(img_lst[i])):
            # here we take the average of values in one pixel, turn it to an integer and assign it back to the channels.
            value = int(sum(img_lst[i][j]) / 3)
            img_lst[i][j] = [value, value, value]
    img_printer(img_lst)

# this doesn't work. I couldn't do it
if operation == 4:
    fname = input()
    stride = int(input())
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    new_img = []
    for i in range(32):
        new_img.append([])
        for j in range(32):
            new_img[i].append([])
            for k in range(3):
                new_img[i][j].append('*')
    filter = []
    for line in lines:
        line = line.split()
        filter.append(line)
    for i in range(len(img_lst)):
        for j in range(len(img_lst[i])):
            for k in range(len(img_lst[i][j])):
                print(k)
    img_printer(new_img)


def quantization(i, j, k, lst=img_lst):
    # i is the variable that increases vertically, j is the vertical one
    if i+1 == len(lst):
        # this is our base condition which works when we reach the end
        if j+1 == len(lst):
            return img_lst
        # if we reach the end of a column this part works and does horizontal check and then sends the recursion to...
        # the next vertical column. We use i-1 to prevent the base function to work
        else:
            if -1 * rang < lst[i][j][0] - lst[i][j+1][0] < rang:
                if -1*rang < lst[i][j][1] - lst[i][j+1][1] < rang:
                    if -1*rang < lst[i][j][2] - lst[i][j+1][2] < rang:
                        lst[i][j+1] = lst[i][j]
            return quantization(i-1, j+1, k, lst)
    # here we take i == -1 to base condition to compensate the i-1 thing above (this one works the we climb up a cloumn)
    # and the reason for adding j!=0 is making the code able to take the first line of image into account
    if i == -1 and j != 0:
        # this is the same base condition as above
        if j+1 == len(lst):
            return img_lst
        # this does the same thing as the one above, just in the opposite direction
        else:
            if -1 * rang < lst[i+1][j][0] - lst[i+1][j+1][0] < rang:
                if -1 * rang < lst[i+1][j][1] - lst[i+1][j+1][1] < rang:
                    if -1 * rang < lst[i+1][j][2] - lst[i+1][j+1][2] < rang:
                        lst[i+1][j+1] = lst[i+1][j]
            return quantization(i+1, j+1, k, lst)
    # this part when we are going up a column
    if j % 2 == 0:
        # this statement does the range check for the difference numbers, and assigns the numbers to the new values...
        # if it is okey to do so
        if -1*rang < lst[i][j][0] - lst[i+1][j][0] < rang:
            if -1*rang < lst[i][j][1] - lst[i+1][j][1] < rang:
                if -1*rang < lst[i][j][2] - lst[i+1][j][2] < rang:
                    lst[i+1][j] = lst[i][j]
        # this recursive call sends the function to the upper pixel
        return quantization(i+1, j, k, lst)
    # this part is the same as above but in the opposite direction
    elif j % 2 == 1:
        if -1*rang < lst[i][j][0] - lst[i+1][j][0] < rang:
            if -1*rang < lst[i+1][j][1] - lst[i][j][1] < rang:
                if -1*rang < lst[i+1][j][2] - lst[i][j][2] < rang:
                    lst[i][j] = lst[i+1][j]
        return quantization(i-1, j, k, lst)


if operation == 6:
    rang = int(input())
    img_lst = quantization(0, 0, 0)
    img_printer(img_lst)


# this is almost the same as previous one
def quantization_2(i, j, k, lst=img_lst):
    # this one works the same way when k is not 1, the only difference is it works channelwise
    if k != 1 and i+1 == len(lst):
        if j+1 == len(lst):
            return img_lst
        else:
            if -1 * rang < lst[i][j][k] - lst[i][j+1][k] < rang:
                lst[i][j+1][k] = lst[i][j][k]
            return quantization_2(i-1, j+1, k, lst)

    if k != 1 and i == -1 and j != 0:
        if k == 2 and j+1 == len(lst):
            return img_lst
        # this part makes channel change possible
        elif k == 0 and j+1 == len(lst):
            if -1*rang < lst[i][j][k] - lst[i][j][k+1] < rang:
                lst[i+1][j][k+1] = lst[i+1][j][k]
            return quantization_2(i+1, j, k+1, lst)
        else:
            if -1 * rang < lst[i+1][j][k] - lst[i+1][j+1][k] < rang:
                lst[i+1][j+1][k] = lst[i+1][j][k]
            return quantization_2(i+1, j+1, k, lst)
    # these if statements are the same as above but they work in the opposite way
    if k == 1 and i == -1:
        if j == 0:
            if -1 * rang < lst[i+1][j][k] - lst[i+1][j][k+1] < rang:
                lst[i+1][j][k+1] = lst[i+1][j][k]
            return quantization_2(i, j, k+1, lst)
        else:
            if -1 * rang < lst[i+1][j][k] - lst[i+1][j-1][k] < rang:
                lst[i+1][j-1][k] = lst[i+1][j][k]
            return quantization_2(i+1, j-1, k, lst)

    if k == 1 and i+1 == len(lst):
        if j == 0:
            if -1*rang < lst[i][j][k] - lst[i][j][k+1] < rang:
                lst[i][j][k+1] = lst[i][j][k]
            return quantization_2(i, j, k+1)
        else:
            if -1 * rang < lst[i][j][k] - lst[i][j-1][k] < rang:
                lst[i][j-1][k] = lst[i][j][k]
            return quantization_2(i-1, j-1, k, lst)


    if j % 2 == 0 and k != 1:
        if i == 0 and j == 0 and k != 0:
            if -1*rang < lst[i][j][k-1]-lst[i][j][k] < rang:
                lst[i][j][k] = lst[i][j][k-1]
            return quantization_2(i+1, j, k)
        else:
            if -1 * rang < lst[i+1][j][k] - lst[i][j][k] < rang:
                lst[i+1][j][k] = lst[i][j][k]
        return quantization_2(i+1, j, k, lst)

    elif j % 2 == 1 and k != 1:
        if -1 * rang < lst[i][j][k] - lst[i+1][j][k] < rang:
            lst[i][j][k] = lst[i+1][j][k]
        return quantization_2(i-1, j, k, lst)

    elif j % 2 == 0 and k == 1:
        if -1 * rang < lst[i][j][k] - lst[i + 1][j][k] < rang:
            lst[i][j][k] = lst[i+1][j][k]
        return quantization_2(i-1, j, k, lst)

    elif j % 2 == 1 and k == 1:
        if -1 * rang < lst[i][j][k] - lst[i+1][j][k] < rang:
            lst[i+1][j][k] = lst[i][j][k]
        return quantization_2(i+1, j, k, lst)


if operation == 7:
    rang = int(input())
    img_lst = quantization_2(0, 0, 0)
    img_printer(img_lst)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

