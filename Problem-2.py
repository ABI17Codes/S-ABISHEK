def OddNumber(a):
    result = []
    for i in range(1, a+1):   
        result.append(2*i - 1) 
    return result

a = int(input("Enter the valid number: "))
print("Result:", OddNumber(a))
