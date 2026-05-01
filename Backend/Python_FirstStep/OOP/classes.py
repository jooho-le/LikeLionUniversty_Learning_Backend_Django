# # 클래스 (classes) - 설계

# class Student:
#     def __init__(self, name, major, is_graduated): # init: 클래스의 생성자 메서드, 객체가 생성될 때 자동으로 호출되는 메서드, name과 age 매개변수를 받아서 객체의 속성으로 저장
#         self.name = name
#         self.major = major
#         self.is_graduated = is_graduated
#         # self는 객체 자신을 가리키는 참조 변수, 객체의 속성에 접근하기 위해 사용됨
        
#     def study(self):
#         print(f'{self.name} 학생은 공부 중이니다.')
        
        
# # 인스턴스 - 실체화된 사물 

# student_1 = Student('이주호', '기설', False)
# print(student_1) # 주소 값이 출력됨, student_1 객체의 메모리 주소를 나타냄

# # student_1 = student_1.name # student_1 객체의 name 속성에 접근하여 출력, '이주호'가 출력됨
# # print(student_1) # init 메서드에서 name 속성에 '이주호'가 저장되었기 때문에 student_1을 출력하면 '이주호'가 출력됨

# student_1.study()

# -------------------------------------------------------------------

# class Student:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major
#         self.is_graduated = False

#     def study(self):
#         print(f'{self.name} 학생은 공부 중입니다.')

# student_1 = Student('이주호', '기설')

# student_1_name = student_1.name
# print(student_1.name)
# student_1_major = student_1.major
# print(student_1.major)
# student_1_graduated = student_1.is_graduated
# print(student_1.is_graduated)

# student_1.study()


# ## 인스턴스 값 변경 

# class Student:
#     def __init__(self, name, major):
#         self.name = name
#         self.major = major
#         self.is_graduated = False

#     def study(self):
#         print(f'{self.name} 학생은 공부 중입니다.')
        
#     ## 변경함수 
#     def edit_major(self, new_major):
#         self.major = new_major
#         print(f'{student_1.major}로 전경 변경')

# student_1 = Student('이주호', '기설')

# ## 직접변경 - 바람직하지는 않음 
# # student_1.major = '컴공'
# # print(student_1.major)

# student_1.edit_major('컴공')
# print(student_1.major)

# -------------------------------------------------------------------

# 상속 (inheritance)

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

class ForeignStudent(Student): # ForeignStudent 클래스는 Student 클래스를 상속받음, ForeignStudent 클래스는 Student 클래스의 모든 속성과 메서드를 사용할 수 있음
    def __init__(self, name, major, country): # ForeignStudent 클래스의 생성자 메서드, name과 major 매개변수는 부모 클래스인 Student의 생성자 메서드에서 처리되고, country 매개변수는 ForeignStudent 클래스에서 처리됨
        super().__init__(name, major) # 부모 클래스인 Student의 생성자 메서드를 호출하여 name과 major 속성을 초기화함
        self.country = country # self로 새롭게 할당 받을수 있게 
        
    # 오버라이딩 : 부모 클래스의 메서드를 자식 클래스에서 재정의하여 사용하는 것, ForeignStudent 클래스에서 study 메서드를 재정의하여 부모 클래스인 Student의 study 메서드와 다른 동작을 하도록 함 
    def study(self):
        print(f'{self.name} is studying now.')

foreign_stud_1 = ForeignStudent('david', '국문학과', '미국')
# print(foreign_stud_1.name) # ForeignStudent 클래스는 Student 클래스를 상속받았기 때문에 name 속성에 접근할 수 있음, 'david'가 출력
# print(foreign_stud_1.major) # ForeignStudent 클래스는 Student 클래스를 상속받았기 때문에 major 속성에 접근할 수 있음, '국문학과'가 출력
# print(foreign_stud_1.is_graduated) # ForeignStudent 클래스는 Student 클래스를 상속받았기 때문에 is_graduated 속성에 접근할 수 있음, False가 출력
# print(foreign_stud_1.country) # ForeignStudent 클래스는 Student 클래스를 상속받았기 때문에 country 속성에 접근할 수 있음, '미국'이 출력

# 오버라이딩한거 출력 
foreign_stud_1.study()