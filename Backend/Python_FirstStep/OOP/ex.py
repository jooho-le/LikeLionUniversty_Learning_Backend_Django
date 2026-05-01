from classes import Student, ForeignStudent
# from class import * # 모든 클래스 가져오기

stud_1 = Student('이주호', '기설')
foreign_stud_1 = ForeignStudent('david', '국문학과', '미국')

stud_1.study()
foreign_stud_1.study()