import time

nemo = ['nemo'] #O(1)
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla'] #O(1)
large = ['nemo' for i in range(100)] #O(1)
def find_nemo(array): #O(1)
    t0 = time.time() #O(1)
    for i in range(0,len(array)): #O(N)
        if array[i] == 'nemo': #O(N)
            print("Found Nemo!!") #O(N)
    t1 = time.time() #O(1)
    print(f'The search took {t1-t0} seconds.') #O(1)

find_nemo(nemo)  #O(1)
find_nemo(everyone) #O(1)
find_nemo(large) #O(1)


def funchallenge(input):
    temp = 10 #O(1)
    temp = temp +50 #O(1)
    for i in range(len(input)): #O(n)
        var = True #O(N)
        a += 1 #O(N)
    return a #O(1)

funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)

#Total running time of the funchallenge function =
#O(1 + 1 + n + n*1 + n*1 + n*1 + 1) = O(3n +3) = O(3(n+1))
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3(n+1)) becomes O(n+1)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.