import turtle as t
import random as r

t.bgcolor('midnightblue') # 밤하늘 색상 설정
t.speed(0) # 최고속도 설정
t.setup(1000,1000) # 스크린 크기 설정

for i in range(20): # 20번 반복
    where = (r.randint(-500, 500), r.randint(-500, 500)) # 좌표 랜덤 설정
    size = r.randrange(20,50,10) # 크기 랜덤 설정
    for star in range(18): # 별의 꼭짓점 수
        t.penup() # 펜 비활성화
        t.goto(where) # 좌표로 이동
        t.right(20) # 오른쪽으로 20도 돌기
        t.pendown() # 펜 활성화
        t.pencolor('navajowhite') # 펜 색상 설정
        t.pensize(2) # 펜 크기 설정
        t.circle(size,120) # 반지름이 size인 원을 120도 만큼 그리기
    
t.exitonclick()



# import turtle as t

# gap = 15 # gap 생성
# t.bgcolor('midnightblue') # 밤하늘 색상 설정
# t.tracer(gap, 1) # *화면에 당장 표시하지 않기

# lst = []
# for cnt in range(gap): # gap 수 만큼 반복
#   turtle = t.Turtle() # 터틀 생성
#   turtle.setheading(360 / gap * cnt) # 터틀이 향할 방향 설정
#   lst.append(turtle) # 리스트에 각 turtle 넣기

# for r in range(360):
#   for turtle_each in lst: # 리스트에서 turtle 꺼내기
#     turtle_each.pencolor('navajowhite') # 색상 설정
#     turtle_each.circle(r * r, 30) # 반지름이 r * r만큼 증가하는 원을 30도만 그리기

# t.update() # *화면에 표시하기
# t.exitonclick()

