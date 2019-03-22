print(" **********  ")
mashaApples = int(input("Сколько яблок у Маши?"))
mishaApples = int(input("Сколько яблок у Миши?"))

totalApples = mashaApples + mishaApples
print("У детей " + str(totalApples) + " яблок")

print("Сейчас дети поделятся по честному. ")
if mashaApples > mishaApples:
    while mashaApples > mishaApples:
        mashaApples = mashaApples - 1
        mishaApples = mishaApples + 1
        print("Миша: " + str(mishaApples) + " и Маша: " + str(mashaApples))
else:
    while mashaApples < mishaApples:
        mashaApples = mashaApples + 1
        mishaApples = mishaApples - 1
        print("Миша: " + str(mishaApples) + " и Маша: " + str(mashaApples))



