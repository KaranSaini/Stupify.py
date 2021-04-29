print("Input to be stupified...")
toStupify = str(input())

# takes a string and returns stupified string
def stupify(inputString):
    toBeStupified = inputString.lower()
    stupified = ""
    for index in range(len(toBeStupified)):
        if(index % 2 != 0 and index != 0):
            toAdd = toBeStupified[index].upper()
            stupified += toAdd
        else:
            stupified += toBeStupified[index]
    return stupified

print(stupify(toStupify))