# 파일 읽기 쓰기

# f = open('Backend/Python_FirstStep/FileIO&Exception/literaure/ex.txt', 'r', encoding='utf-8') # r: read, w: write, a: append

# print(f) # 객체 정보를 출력 
# print(f.read()) # 파일 전체 읽기   
# print('-------') 
# print(f.readline()) # 파일에서 한 줄 읽기
# print(f.readlines()) # 파일에서 모든 줄을 읽어서 리스트로 반환

# f.close() # 파일 닫기 , 파일을 열었으면 꼭 닫아줘야 함, 안 그러면 메모리 누수 발생할 수 있음

# -------------------------------------------------------------------
 
with open('Backend/Python_FirstStep/FileIO&Exception/literaure/ex.txt', 'r', encoding='utf-8') as f: # with 구문을 사용하면 파일을 자동으로 닫아줌
    print(f.read())