# 함수 

# def print_name(name): # 파라미터 name을 받아서 출력하는 함수 
#     print(f'이름은 {name}입니다') # f-string을 사용하여 name을 출력하는 함수
    
# print_name("홍길동") # 함수 호출, 인자로 "홍길동"을 전달하여 함수 실행  
# print_name("김철수") # 함수 호출, 인자로 "김철수"를 전달하여 함수 실행

# def print_string():
#     print('문자열입니다') # 문자열을 출력하는 함수
    
# print_string() # 함수 호출, 문자열을 출력하는 함수 실행

## 용어정리
# 파라미터 , 인자 , 매개변수 , 아규먼트
# - 함수 정의 시에 사용되는 변수 : 파라미터 (parameter) , 매개변수 (parameter)
    # name : 파라미터, 매개변수
# - 함수 호출 시에 전달되는 값 : 인자 (argument) , 아규먼트 (argument)  
    # 홍길동, 김철수 : 인자, 아규먼트

# def print_name_age(name, age): # 파라미터 name과 age를 받아서 출력하는 함수
#     print(f'이름은 {name}이고, 나이는 {age}입니다') # f-string을 사용하여 name과 age를 출력하는 함수

# print(print_name_age("홍길동", 20)) # 함수 호출, 인자로 "홍길동"과 20을 전달하여 함수 실행
# print(print_name_age("김철수", 25)) # 함수 호출, 인자로 "김철수"와 25를 전달하여 함수 실행
# print_nama_age() # TypeError: print_nama_age() missing 2 required positional arguments: 'name' and 'age'
# 함수 호출 시에 필요한 인자가 전달되지 않으면 TypeError가 발생

# -------------------------------------------------------------------