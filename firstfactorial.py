def FirstFactorial(num): 
    if num == 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)

str = input()
print(FirstFactorial(str))
