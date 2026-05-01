# 예외 

# a = 10
# b = 0
# a / b  # ZeroDivisionError: division by zero

fruits = ['apple', 'banana', 'strawberry']
# print(fruits[3])  # IndexError: list index out of range']

try: # 예외가 발생할 수 있는 코드
    fruits[3]
except: # 예외가 발생했을 때 실행할 코드
    print('인덱스 범위를 벗어났습니다.')
else: # 예외가 발생하지 않았을 때 실행할 코드
    print('인덱스 범위 내입니다.')
finally: # 예외 발생 여부와 상관없이 항상 실행할 코드
    print('프로그램 종료')

print(fruits)