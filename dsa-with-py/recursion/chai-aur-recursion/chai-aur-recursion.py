# def printNumbers(Lrange, Urange):
#     # base case
#     if Lrange > Urange:
#         return

#     print(Lrange)
#     printNumbers(Lrange + 1, Urange)


# printNumbers(1, 5)




# def printNumbers(Lrange, Urange):
#     # base case
#     if Lrange > Urange:
#         return

#     printNumbers(Lrange + 1, Urange)
#     print(Lrange)


# printNumbers(1, 5)


#! THREE FOUNDATIONIONAL PROBLEMS ON RECUSRION

#! 1. Sum of Array Element

# [1, 2, 3, 4, 5]

#? Iterative approach

arr = [1, 2, 3, 4, 5, 6]

def sumArr(arr):
    total = 0

    for i in arr:
        total = total + i

    return total



ans = sumArr(arr)
print(ans)