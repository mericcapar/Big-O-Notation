import time

array1 = ['a','b','c','d','e']
array2 = [1,2,3,4,5]

def pairs(m, n):

    # Here there are two different variables array1 and array2.
    # They have to be represented by 2 different variables in the Big-O representation as well.
    # Let array1 correspond to m and array2 correspond to n

    for i in range(len(m)): #n*O(m)
        for j in range(len(n)): #m*O(n)
            print(m[i],n[j]) #n*m*O(1)
        print("-----------")


pairs(array1,array2)

#Total time complexity would be O(3*m*n)
#After we ignore the constants it would be O(m*n)
