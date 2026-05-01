# 클래스 (classes) - 설계

class Student:
    def __init__(self, name, major, is_graduated): # init: 클래스의 생성자 메서드, 객체가 생성될 때 자동으로 호출되는 메서드, name과 age 매개변수를 받아서 객체의 속성으로 저장
        self.name = name
        self.major = major
        self.is_graduated = is_graduated
        # self는 객체 자신을 가리키는 참조 변수, 객체의 속성에 접근하기 위해 사용됨
        
    def study(self):
        print(f'{self.name} 학생은 공부 중이니다.')
        
        
# 인스턴스 - 실체화된 사물 

student_1 = Student('이주호', '기설', False)
print(student_1) # 주소 값이 출력됨, student_1 객체의 메모리 주소를 나타냄

# student_1 = student_1.name # student_1 객체의 name 속성에 접근하여 출력, '이주호'가 출력됨
# print(student_1) # init 메서드에서 name 속성에 '이주호'가 저장되었기 때문에 student_1을 출력하면 '이주호'가 출력됨

student_1.study()
