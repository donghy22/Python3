#gotcha
def gotcha():
    print("잡았다!")

gotcha()

#add함수
def add(num1, num2): #num1,num2는 매개변수
    return num1 + num2

print(add(1, 3)) #1,3은 인자

#add_mul 함수
def add_mul(num1, num2):
    return num1+num2, num1*num2

print(add_mul(2, 4))

#attack함수
def attack(name):
    print(name, "100만볼트")

attack("피카츄")