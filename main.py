def two_odd_occuring(arr, size):
    Xoroftwo = arr[0]
    x = 0
    y = 0
    #this will hold the right most set bit
    setbit = 0 
    for i in range(1, size):
        Xoroftwo = Xoroftwo ^ arr[i]
    setbit = Xoroftwo &~ (Xoroftwo - 1)
    for i in range(size):
        if (arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("THE TWO ODD ELEMENT ARE>>>", x, "&", y)
arr = []
arr_size = int(input("ENTER SIZE OF THE ARRAY"))
for i in range(0, arr_size):
    z = int(input("ENTER ELEMENT"))
    arr.append(z)
two_odd_occuring(arr, arr_size)