def fizzbuzz(input: int)-> str:
    returnValue = ""
    if(input % 3 == 0):
        returnValue += "Fizz"
    if(input % 5 == 0):
        returnValue += "Buzz"
    if(len(returnValue) == 0):
        return str(input)
    else:
        return returnValue
    