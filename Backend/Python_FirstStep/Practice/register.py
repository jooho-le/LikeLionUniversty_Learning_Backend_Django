print("-------------------------------")
print("회원가입!")
print("-------------------------------")

register = False # 회원가입 여부를 나타내는 변수, 초기값은 False로 설정하여 회원가입이 완료되지 않았음을 나타냄

while not register: # register가 False인 동안 반복하는 while 루프, 회원가입이 완료될 때까지 계속해서 사용자 입력을 받음
    print("회원가입을 진행하시겠습니까? \b(Y/N)") 
    register_input = input('>>') # 사용자로부터 입력을 받는 함수, 회원가입 여부에 대한 입력을 받음, >>는 입력 프롬프트로 사용자가 입력할 위치를 나타냄
    register_input = register_input.lower() # 입력된 문자열을 소문자로 변환하여 대소문자 구분 없이 처리할 수 있도록 함
    
    if register_input == 'y': # 사용자가 'y'를 입력한 경우, 회원가입을 진행하는 조건문
        print("회원가입이 완료되었습니다!") 
        register = True # 회원가입이 완료되었음을 나타내는 변수, True로 설정하여 while 루프를 종료할 수 있도록 함
    elif register_input == 'n': # 사용자가 'n'를 입력한 경우, 회원가입을 진행하지 않는 조건문
        print("회원가입이 취소되었습니다.")
        exit() # 프로그램을 종료하는 함수, 회원가입이 취소된 경우 프로그램을 종료하여 더 이상 사용자 입력을 받지 않도록 함
    else: # 사용자가 'y'나 'n'이 아닌 다른 입력을 한 경우, 올바른 입력을 요구하는 조건문
        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
  
users = [] # 사용자 정보를 저장하는 리스트, 회원가입이 완료된 사용자들의 정보를 저장하기 위해 빈 리스트로 초기화

while True: # 무한 루프, 사용자 정보를 계속해서 입력받기 위해 사용
    
    user = {} # 사용자 정보를 저장하는 딕셔너리, 각 사용자의 정보를 키-값 쌍으로 저장하기 위해 빈 딕셔너리로 초기화
    
    username = input("ID: ") # 사용자로부터 ID를 입력받는 함수, 입력된 ID를 username 변수에 저장
    while True:
        password = input("Password: ") # 사용자로부터 비밀번호를 입력받는 함수, 입력된 비밀번호를 password 변수에 저장
        password_confirm = input("Password 확인: ") # 사용자로부터 비밀번호 확인을 입력받는 함수, 입력된 비밀번호 확인을 password_confirm 변수에 저장
        if password == password_confirm:
            break
        else:
            print("비밀번호가 일치하지 않습니다. 다시 입력해주세요.")
    name = input("Name: ") # 사용자로부터 이름을 입력받는 함수, 입력된 이름을 name 변수에 저장
    while True:
        birth_date = input("생년월일(6자리): ")
        if len(birth_date) == 6 and birth_date.isdigit(): # 생년월일이 6자 이면서 숫자로만 
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다")
    email = input("email: ")
    
    user['username'] = username
    user['name'] = username
    user['name'] = username
    user['birth_date'] = username
    user['email'] = username
    
    users.append(user)
    print(users)
    
    print("-------------------------------")
    print(f"{user['name']}님 회원가입 축하합니다")
    print("-------------------------------")
    
    print("회원가입을 추가로 진행하시겠습니다? \b(Y/N)")
    register_another_input = input(">>")
    register_another_input = register_another_input.lower()
    
    if register_another_input == 'y':
        pass
    elif register_another_input == 'n':
        exit()
    