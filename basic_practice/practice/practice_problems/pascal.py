#pacal triangle
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def pascal_triangle(rows):
    for i in range(rows):
        for j in range(i+1):
           
            value = factorial(i) // (factorial(j) * factorial(i-j))
            print(value,end=" ")
        print()


n = 5  
pascal_triangle(n)

