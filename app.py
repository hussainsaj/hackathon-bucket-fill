import sys

def strokesRequired(picture):
    # Write your code here
    strokes = 0
    
    #holds all the cells which I've already visited
    checked = []

    for i in range(len(picture)):
        checked.append([False] * len(picture[i]))

    def fill(i, a):
        #mark the current pixel as checked
        checked[i][a] = True

        #fill all the pixels around the current pixel which haven't been checked already
        if (i > 0 and checked[i - 1][a] != True):
            if (picture[i - 1][a] == picture[i][a]):
                fill(i - 1, a)
        
        if (i < len(picture) - 1 and checked[i + 1][a] != True):
            if (picture[i + 1][a] == picture[i][a]):
                fill(i + 1, a)

        if (a > 0 and checked[i][a - 1] != True):
            if (picture[i][a - 1] == picture[i][a]):
                fill(i, a - 1)

        if (a < len(picture[i]) - 1 and checked[i][a + 1] != True):
            if (picture[i][a + 1] == picture[i][a]):
                fill(i, a + 1)

    #go through each pixel of the picture
    for i in range(0, len(picture)):
        for a in range(0, len(picture[i])):
            #increase the strokes and fill the currect pixel if it hasn't been checked already
            if checked[i][a] == False:
                strokes += 1
                fill(i, a)
    
    return strokes

if __name__ == '__main__':
    fptr = sys.stdout

    picture_count = int(input().strip())

    picture = []

    for _ in range(picture_count):
        picture_item = input()
        picture.append(picture_item)

    result = strokesRequired(picture)

    fptr.write(str(result) + '\n')

    fptr.close()