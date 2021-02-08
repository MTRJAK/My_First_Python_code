x = 1
y = 2
z = 1.2

print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x%y)

a = "Hello"
b = 'bye'
c ="""
안녕하세요
김태호입니다
"""

print(a)
print(b)
print(c)

print("안녕" + "잘 지내니?")

#str을 사용하여 형변환 캐스팅을 해주어야함.
print("너 몇 살 이니?" + str(x) + "살")

x = 4 # 숫자타입
y = "4" #문자열 타입

#print(x + y) << 캐스팅이 없기에 출력 에러

print(str(x) + y)
print(x + int(y))

#boolean : 참 거짓 증명
x = True
y = False
print(x)
print(y)