def OddNumber(a):
    result = []
    limit = a if a % 2 != 0 else a - 1

    for i in range(1, limit + 1):   
        result.append(2 * i - 1)  
    
    return result

a = int(input("Enter the valid number: "))
print("Result:", OddNumber(a))
