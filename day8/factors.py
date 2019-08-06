
def CountToN(num):
    #num will be assigned
    #the absolute value of 
    #itself
    num = abs(num)
    for i in range(1,num+1):
        print i
    i += 1
n = raw_input("Enter an integer:\n")
n = int(n)


def Factors(num):
    num = abs(num)
    l = [] #list()

    for i in range(1,num+1):
        if num % i == 0:
            l.append(i)
    return l 

CountToN(n)
print Factors(n)    


