import turtle
t = turtle
t.bgcolor("#c842d9")
t.color("#FFFFFF")

t.penup()
t.setx(-5)
t.sety(100)
t.write("K", font=("Times New Roman", 50,"bold"))

t.penup()
t.setx(-10)
t.sety(-100)
t.write("J", font=("Times New Roman", 50,"bold"))

t.penup()
t.setx(-100)
t.sety(0)
t.write("7", font=("Times New Roman", 50,"bold"))

t.penup()
t.setx(0)
t.sety(0)
t.write("9", font=("Times New Roman", 50,"bold"))

t.penup()
t.setx(100)
t.sety(0)
t.write("6", font=("Times New Roman", 50,"bold"))

t.exitonclick()