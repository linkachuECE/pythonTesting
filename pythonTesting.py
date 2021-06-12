def midSquareHash(num):
    numSquare = str(num ** 2)
    if len(numSquare)%2 == 0:
        lowMid = int(numSquare[len(numSquare)//2 - 1])
        highMid = int(numSquare[(len(numSquare)//2)])
        midNumber = int("{}{}".format(lowMid,highMid))
        remainder = midNumber%11
        return remainder
    else:
        return int(numSquare[(len(numSquare)//2)])
 

print(midSquareHash(31))