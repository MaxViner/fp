
print("размерность массива?")
N = int(input())
print(N)
def one_dimensional_array():
    Wide = input("длинна массива?:")
    A = [0] * Wide
    for i in range(Wide):
        A[i] =str(input(" введите элемент массива"))
    for i in range(N):
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
                    print(A[i], end=" ")

def 3_dim_array():

    Wide = input("длинна массива?:")
    Up = input("число строк?:")
    A = [0] * Wide * Up * Deep

