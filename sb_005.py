print("астероиды летят навстречу друг к другу.")
speed1 = int(input("введите скорость первого астероида (км/час): "))
speed2 = int(input("введите скорость второго астероида (км/час): "))
distance = int(input("введите расстояние между астероидами (км): "))

meetTime = distance / (speed1 + speed2)

print("астероиды столкнутся через " + str(meetTime) + " часов")

distance1 = speed1 * meetTime
distance2 = speed2 * meetTime

print("астероид1 пролетел " + str(distance1) + "км")
print("астероид2 пролетел " + str(distance2) + "км")


