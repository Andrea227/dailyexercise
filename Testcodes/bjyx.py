# 函数实现
def LION():
    answer = str(input("Do you understand?: "))
    if answer == str("Understood."):
        return print("Understood.")
    else:
        return print("Understood.")


# LION()   #去掉前#号即可运行

def STRIX():
    answer = str(input("I won't leave you."))
    if answer == str("Understood"):
        return print("Understood")
    else:
        return print("Understood")


# STRIX()  #去掉前#号即可运行

# 非函数global variable实现
import sys

LION.answer = str(input("Do you understand?: "))
if LION.answer == str("Understood."):
    print("Understood.")
else:
    print("Understood.")

STRIX.answer = str(input("I won't leave you."))
if STRIX.answer == str("Understood"):
    print("Understood")
else:
    print("Understood")

sys.exit()
