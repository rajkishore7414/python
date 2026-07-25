

#! phase 1


# def hello5(n):
#     if n == 0:
#         return

#     hello5(n-1)
#     # print("hello")
#     print(f"{n} hello")




# hello5(5) #fn call 



#====================================

i = 1
def printOneToFive():
    # global i
    if i <=5:
        return
    print(i)

    i = i +1

    printOneToFive()

printOneToFive()




#_____________________________________

