
def one_dimensional_array():
    Wide = int(input("длинна массива?:"))
    A = [0] * Wide
    for i in range(Wide):
        A[i] =str(input(" введите элемент массива"))
    for i in range(Wide):
        if len(A[i])<=3:
            print(A[i], end=" ")


def tw0_dimensional_array():
    Wide = int(input("длинна массива?:"))
    Up = int(input("число строк?:"))
    A = [[0] * Wide for i in range(Up)]
    for i in range(0, Up):
        for i2 in range(0, Wide)
            if len(A[i][i2]) <= 3:
                A[i][i2]= str(input())

    for i in range(0, len(A)):
        for i2 in range(0, len(A[i])):
            print(A[i][i2], end=' ')
        print()

def fre_dim_array():
    Wide = int(input("длинна массива?:"))
    Up = int(input("число строк?:"))
    Deep = int(input("глубина массива?:"))
    A = [[[0] * Wide for i in range(Up)] for k in range(Deep)]
    for i in range(Up):
        for j in range(Wide):
            for k in range(Deep):
                A[i][ j][ k] = str(input(" введите элемент массива"))
    for i in range(Up):
        for j in range(Wide):
            for k in range(Deep):
                if len(A[i][j][k]) <= 3:
                    print( A[i][j][k], end=" ")

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