#  随机打印IP地址
import random
a = str(random.randint(1, 255))
b = str(random.randint(1, 255))
c = str(random.randint(1, 255))
d = str(random.randint(1, 255))

ip = a + '.' + b + '.' + c + '.' +d

print("IP_address：" + ip)
