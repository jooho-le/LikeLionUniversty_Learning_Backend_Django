# # 딧셔너리

# student = {
#     "name": "홍길동",
#     "age": 20,
#     "major": "컴퓨터공학"
# } # 딧셔너리는 키와 값의 쌍으로 이루어진 자료형
# print(student["name"]) # 딧셔너리에서 키를 사용하여 값을 조회

# student["age"] = 21 # 딧셔너리에서 키를 사용하여 값을 변경
# print(student)

# # 키와 속성들을 어떻게 관리할지 설계를 잘 해야함 

# # -----------------------------------------------------------------

# student = {
#     "name": "홍길동",
#     "age": 20,
#     "major": "컴퓨터공학"
# }

# # 추가
# student["gpa"] = "4.5" # 딧셔너리에 새로운 키와 값을 추가
# print(student)
# # 끝에말고 중간에 추가할려면 새 딕셔너리로 재구성하여 달성 
# # student = {
# #     "name": "홍길동",
# #     "age": 20,
# #     "gpa": "4.5", # 새로운 키와 값 추가
# #     "major": "컴퓨터공학"
# # }
# # print(student)

# # 수정
# student["gpa"] = 4.3 # 딧셔너리에 이미 존재하는 키에 새로운 값을 할당하여 수정
# print(student)

# # 삭제
# del student["age"] # 딧셔너리에서 특정 키와 그에 해당하는 값을 삭제
# print(student) 

# # -----------------------------------------------------------------

# student = {
#     "name": "홍길동",
#     "age": 20,
#     "major": "컴퓨터공학"
# }   

# # 데이터 접근
# print(student.get("name")) # get 메서드는 키가 존재하지 않을 때 None을 반환하여 오류를 방지할 수 있음
# print(student.get("gpa", "키가 존재하지 않습니다.")) # 키가 없을 때 사용자가 지정한 기본값을 반환할 수 있음

# # 딕셔너리의 키를 반환 
# print(student.keys()) # 딕셔너리의 키를 반환하는 메서드, 반환된 객체는 dict_keys 타입이며, 리스트처럼 순회할 수 있지만 인덱싱은 지원하지 않음

# print(list(student.keys())) # dict_keys 객체를 리스트로 변환하여 키를 반환

# # 딕셔너리의 값을 반환 
# print(student.values()) # 딕셔너리의 값을 반환하는 메서드, 반환된 객체는 dict_values 타입이며, 리스트처럼 순회할 수 있지만 인덱싱은 지원하지 않음   

# print(list(student.values())) # dict_values 객체를 리스트로 변환하여 값을 반환  

# # -----------------------------------------------------------------

# tech = {
#     "python": "파이썬",
#     "java": "자바",
#     "javascript": "자바스크립트"
# }

# for key, value in tech.items(): # 딕셔너리의 키와 값을 순회하는 메서드, 반환된 객체는 dict_items 타입이며, 각 요소는 (키, 값) 튜플로 이루어져 있음
#     print(f'{key} - {value}')
    
# for i in tech: # 딕셔너리를 순회할 때 기본적으로 키를 순회함
#     print(i) # 키만 출력됨  

# for key, value in tech:
#     print(f'{key} - {value}') # 키와 값을 출력하려면 items() 메서드를 사용하여 키와 값을 함께 순회해야 함
    
# for key in tech.keys(): # 딕셔너리의 키를 순회하는 메서드
#     print(key) # 키만 출력됨
    
# for value in tech.values(): # 딕셔너리의 값을 순회하는 메서드
#     print(value) # 값만 출력됨
    
# # -----------------------------------------------------------------

# # 중첩

# student_1 = {
#     "student_id": 1,
#     "gpa": 4.5,
# }
# student_2 = {
#     "student_id": 2,
#     "gpa": 3.3,
# }

# studnts = [student_1, student_2] # 딕셔너리를 요소로 가지는 리스트

# for student in studnts:
#     print(student)
    
# for student in studnts:
#     print(student["student_id"], student["gpa"]) # 딕셔너리의 키를 사용하여 각 학생의 ID와 GPA를 출력
    
# for student in studnts:
#     student["graduated"] = False # 딕셔너리에 새로운 키와 값을 추가하여 졸업 여부를 나타냄
#     print(student)

# student = {
#     "subjects": ["Python", "Java", "JavaScript"], # 딕셔너리의 값으로 리스트를 사용하여 여러 과목을 나타냄
# }

# print(student["subjects"]) # 딕셔너리에서 키를 사용하여 리스트를 조회

# subjects_list = student["subjects"] # 딕셔너리에서 키를 사용하여 리스트를 조회하여 변수에 저장

# for subject in subjects_list:
#     print(subject) # 리스트의 각 요소를 순회하며 출력   

# student = {
#     "scholarship" : {
#         "name": "장학금",
#         "amount": 1000000
#     }
# } # 딕셔너리의 값으로 또 다른 딕셔너리를 사용하여 장학금 정보를 나타냄

# print(student)

# for key in student.keys():
#     print(key)
    
# for value in student.values():
#     print(value) # 딕셔너리의 값은 또 다른 딕셔너리이므로, 값 자체가 딕셔너리로 출력됨
    
# for valeu in student.values():
#     for value_2 in valeu.values():
#         print(value_2)

# # -----------------------------------------------------------------