
while True:

    import random
    import string


    letter1 = random.choice(string.ascii_uppercase)
    letter2 = random.choice(string.ascii_uppercase)
    letter3 = random.choice(string.ascii_uppercase)

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    num4 = random.randint(0,9)
    num5 = random.randint(0,9)
    num6 = random.randint(0,9)

    dictionary = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'G': 16,
        'H': 17,
        'I': 18,
        'J': 19,
        'K': 20,
        'L': 21,
        'M': 22,
        'N': 23,
        'O': 24,
        'P': 25,
        'Q': 26,
        'R': 27,
        'S': 28,
        'T': 29,
        'U': 30,
        'V': 31,
        'W': 32,
        'X': 33,
        'Y': 34,
        'Z': 35
    }

    wlttr1 = dictionary[letter1]
    wlttr2 = dictionary[letter2]
    wlttr3 = dictionary[letter3]

    seriesNumber = [wlttr1 * 7, wlttr2 * 3, wlttr3 * 1, num1 * 9, num2 * 7, num3 * 3, num4 * 1, num5 * 7, num6 * 3]

    checkSum = 0
    i = 0
    while i < len(seriesNumber):
      checkSum += seriesNumber[i]
      i += 1


    if(checkSum%10==0):
        #print(checkSum%10)
        print(letter1+letter2+letter3+str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6))
        break