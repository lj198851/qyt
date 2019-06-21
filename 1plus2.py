# #  高级版作业
# try:
#     num1 = int(input("请输入第一个数字: "))
# except Exception as e:
#     print("请重新输入一个整数：")
#     raise e
#
# try:
#     num2 = int(input("请输入第二个数字: "))
# except Exception as e:
#     print("请重新输入一个整数：")
#     raise e
#
# result = num1 + num2
#
# print("您输入的数字有误，请重新运行")
# print("计算%d+%d的结果" %(num1, num2))
# print("计算结果是: %d" %(result))


while True:
    try:
        num1 = int(input("第一个数字："))

        break
    except:
        print("输入错误,请重新输入一个整数\r\n")

while True:
    try:
        num2 = int(input("第二个数字:"))
        break
    except:
        print("输入错误,请重新输入一个整数")
result = num1 + num2
print("计算%d+%d的结果" %(num1, num2))
print("计算结果是: %d" %(result))


