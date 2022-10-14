
def one_dimensional_array():
    Wide = int(input("длинна массива?:"))
    A = [0] * Wide
    for i in range(Wide):
        A[i] =str(input(" введите элемент массива"))
    for i in range(Wide):
        if len(A[i])<=3:
            print(A[i], end=" ")
def tw0_dimensional_array():
    Wide = input("длинна массива?:")
    Up= input("число строк?:")
    A = [0] * Wide * Up
    for i in range(Up):
        for j in range(Wide):
            A[i,j] = str(input(" введите элемент массива"))
        for i in range(Up):
            for j in range(Wide):
                if len(A[i,j]) <= 3:
                    print(A[i,j], end=" ")

def fre_dim_array():
    Wide = input("длинна массива?:")
    Up = input("число строк?:")
    Deep = input("глубина массива?:")
    A = [0] * Wide * Up * Deep
    for i in range(Up):
        for j in range(Wide):
            for k in range(Deep):
                A[i, j, k] = str(input(" введите элемент массива"))
    for i in range(Up):
        for j in range(Wide):
            for k in range(Deep):
                if len(A[i, j, k]) <= 3:
                    print(A[i,j,k], end=" ")

def array_selector(N):

    if N==1:
        one_dimensional_array()
    elif N==2:
        tw0_dimensional_array()
    elif N==3:
        fre_dim_array()
    else:print("oh...something wrong")

print("размерность массива?")
N = int(input())
print(N)
array_selector(N)