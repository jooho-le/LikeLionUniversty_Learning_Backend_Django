## 함수 

def print_name(name): # 파라미터 name을 받아서 출력하는 함수 
    print(f'이름은 {name}입니다') # f-string을 사용하여 name을 출력하는 함수
    
print_name("홍길동") # 함수 호출, 인자로 "홍길동"을 전달하여 함수 실행  
print_name("김철수") # 함수 호출, 인자로 "김철수"를 전달하여 함수 실행

def print_string():
    print('문자열입니다') # 문자열을 출력하는 함수
    
print_string() # 함수 호출, 문자열을 출력하는 함수 실행

# 용어정리
# 파라미터 , 인자 , 매개변수 , 아규먼트
# - 함수 정의 시에 사용되는 변수 : 파라미터 (parameter) , 매개변수 (parameter)
#     name : 파라미터, 매개변수
# - 함수 호출 시에 전달되는 값 : 인자 (argument) , 아규먼트 (argument)  
#     홍길동, 김철수 : 인자, 아규먼트

def print_name_age(name, age): # 파라미터 name과 age를 받아서 출력하는 함수
    print(f'이름은 {name}이고, 나이는 {age}입니다') # f-string을 사용하여 name과 age를 출력하는 함수

print(print_name_age("홍길동", 20)) # 함수 호출, 인자로 "홍길동"과 20을 전달하여 함수 실행
print(print_name_age("김철수", 25)) # 함수 호출, 인자로 "김철수"와 25를 전달하여 함수 실행
# print_nama_age() # TypeError: print_nama_age() missing 2 required positional arguments: 'name' and 'age'
# 함수 호출 시에 필요한 인자가 전달되지 않으면 TypeError가 발생

# -------------------------------------------------------------------

def order_coffee(qty, option='hot'): # 파라미터 qty와 option을 받아서 주문한 커피의 수량과 옵션을 출력하는 함수, option은 기본값이 'hot'으로 설정되어 있음
    # 디폴트로 지정된 파라미터가 뒤에 위치해야 함 
    print(f'{qty}잔 / 옵션: {option}') # 주문한 커피의 수량과 옵션을 출력하는 함수

order_coffee(2, '아이스') # 함수 호출, 인자로 2와 '아이스'를 전달하여 함수 실행
order_coffee(3) # 함수 호출, 인자로 3만 전달하여 함수 실행 (option은 기본값 'hot' 사용)
order_coffee(qty=4, option='아이스') # 함수 호출, 인자로 qty=4와 option='아이스'를 전달하여 함수 실행 (키워드 인자 사용)
order_coffee(option='아이스', qty=5) # 함수 호출, 인자로 option='아이스'와 qty=5를 전달하여 함수 실행 (키워드 인자 사용, 순서 변경)

# -------------------------------------------------------------------

def get_id(email):
    email_id = email.removesuffix('@example.com') # 문자열에서 특정 접미사를 제거하는 메서드, email에서 '@example.com'을 제거하여 아이디를 반환
    print(email_id)
    return email_id # 함수의 반환값, email_id를 반환하여 함수 실행 결과로 사용할 수 있도록 함

#    print("이 코드는 실행되지 않습니다") # return 이후의 코드는 실행되지 않음

get_id('user@example.com') # 함수 호출, 인자로 
user_id = get_id("user@example.com") # return된 값을 변수에 저장하여 이후에 사용할 수 있도록 함
print(user_id) # 변수에 저장된 값을 출력하여 함수의 반환값을 확인할

def get_id(email):
    
    if email.endswith('@example.com'): # 문자열이 특정 접미사로 끝나는지 확인하는 메서드, email이 '@example.com'으로 끝나는지 확인하여 조건문 실행
        email_id = email.removesuffix('@example.com') # 문자열에서 특정 접미사를 제거하는 메서드, email에서 '@example.com'을 제거하여 아이디를 반환
        return email_id # 함수의 반환값, email_id를 반환하여 함수 실행 결과로 사용할 수 있도록 함
    else:
        return None # email이 '@example.com'으로 끝나지 않는 경우, None을 반환하여 함수 실행 결과로 사용할 수 있도록 함
    
user_id = get_id("user@example.com")
print(user_id) 

# -------------------------------------------------------------------