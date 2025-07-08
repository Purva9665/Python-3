def factorial(y):
    count=1
    for i in range(1,y+1):
        count=i*count
    print(f"Factorial of {y} is {count}!")
    return count
sample_number=int(input("Enter a number:"))
count=factorial(sample_number)







