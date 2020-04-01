print("Hello World!")
print(3)
print(-11)

a="Hellp World!"
b=3
c=-11

print(a)
print(b)
print(c)

#숫자의 연산
a=1
b=5
print(a+b)

#+,-,%,/,//(실수나누기)

c=a/b
print(c)

#문자의 연산: +,*만 가능
a="Hello"
b="World"
print(a+b)
c=a*3
print(c)

#숫자+문자
a=1000
a=str(a)

b="원"
print(a+b)

#Types: 정수 int 실수 float 문자 str 참/거짓 bool 리스트 list 딕셔너리 dict
#실수 a=0.3, 문자 a="Hi"  참/거짓 a=True 리스트 a=[1,3,4]

#형변환
a=1000
print(type(a))
b="원"
print(type(b))
c=True
print(type(c))
d=[1,2,3]
print(type(d))

print(str(a)+b)   #형변환

#input 입력 함수
#name=input("이름을 입력해주세요: ")
#age=input("나이를 입력해주세요: ")

#print("이름은", name)
#print("나이는", age)

#g_age=int(age)-1
#print("만 나이는", g_age)

#BMI 계산기
#height=input("신장: ")
#weight=input("몸무게: ")
#height=float(height)
#weight=float(weight)

#bmi=weight/(height*height)*10000
#print("BMI: ",bmi)

#string variables
string1="브이넥 라이트 다운 베스트"
string2="     25,900            "

print(string1)
print(string2)
print(string1[0])
print(string1[1])   #앞에서부터
print(string1[2])

print(string1[-1])  #뒤에서부터
print(string1[-2])
print(string1[-3])

print(string2[4])
print(string2[5])

#문자열 슬라이싱
print(string1[0:4])
print(string1[-6:-4])
print(string2[4:10])

print(string1[11:])
print(string1[:7])

#문자열 바꾸기: replace
print(string1.replace("라이트","헤비"))
print(string1)

string1=string1.replace("라이트","헤비")
print(string1)

#문자열 앞뒤 공백 없애기: strip
print(string2.strip())
print(string2)

string2=string2.strip().replace(",","")
print(string2)

#list
players=["황의조","황희찬","구자철","이재성","기성용"]

print(players)
print(players[0])
print(players[3])

print(players[-1])
print(players[-5])

#리스트 관련 함수: append(), del
players.append("이승우")  #오른쪽
print(players)
players.insert(0, "김민재")   #왼쪽
print(players)
players.pop(2)  #delete와 같은 효과
print(players)
del players[1]

print(players)
print(len(players))

#반복문
a=range(1, 10)
print(a)


for i in range(1,9):
    print(i)
    print("반복문을 배워 봅시다.")

print("2019년 아시안컵 출전명단:")

for i in range(4):
    print(players[i])


#리스트 기준 반복
for player in players:
    print(player)


#수집한 데이터 후처리하기
data=["조회수: 1,500",
      "조회수: 1,002",
      "조회수: 300",
      "조회수: 251",
      "조회수: 13,432",
      "조회수: 998"]
sum=0

for click in data:
    print(click.replace("조회수:","").strip().replace(",",""))
    click=click.replace("조회수:","").strip().replace(",","")
    click=int(click)
    sum=sum+click
    print(sum)

print("summary: "+str(sum))

for i in range(0, len(data)):
    print(range)
