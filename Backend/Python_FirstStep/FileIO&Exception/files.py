# 파일 읽기 쓰기

# f = open('Backend/Python_FirstStep/FileIO&Exception/literaure/ex.txt', 'r', encoding='utf-8') # r: read, w: write, a: append

# print(f) # 객체 정보를 출력 
# print(f.read()) # 파일 전체 읽기   
# print('-------') 
# print(f.readline()) # 파일에서 한 줄 읽기
# print(f.readlines()) # 파일에서 모든 줄을 읽어서 리스트로 반환

# f.close() # 파일 닫기 , 파일을 열었으면 꼭 닫아줘야 함, 안 그러면 메모리 누수 발생할 수 있음

# -------------------------------------------------------------------
 
# with open('Backend/Python_FirstStep/FileIO&Exception/literaure/ex.txt', 'r', encoding='utf-8') as f: # with 구문을 사용하면 파일을 자동으로 닫아줌
#     print(f.read())
    
# -------------------------------------------------------------------

# 파일 쓰기 

# f = open('Backend/Python_FirstStep/FileIO&Exception/literaure/ex.txt', 'w', encoding='utf-8') # w: write, a: append
# # w : 파일이 존재하지 않으면 새로 생성, 존재하면 기존 내용 삭제 후 새로 작성
# # a : 파일이 존재하지 않으면 새로 생성, 존재하면 기존 내용 유지 후 새로 작성

# f.write('새로운 글 작성')
# f.close()

f = open('Backend/Python_FirstStep/FileIO&Exception/literature/ex.txt', 'a', encoding='utf-8') # a: append
f.write('\n새로운 글 추가')
f.close()