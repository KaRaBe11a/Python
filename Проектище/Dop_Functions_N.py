def ROFLAN():
    with open("add.txt", "w", encoding="utf-8") as file:
        for i in range(-1, 20):
            for j in range(0, 20):
                file.write(f"if number1 == \"{i}\" and number2 == \"{j}\":\n"
                        f"   return \"{(i+j)}\"\n\n")


def ADD_N_N(number1: str, number2: str):  # Сложение двух натуральных чисел <10
    number1 = str(number1)
    number2 = str(number2)

    if number1 == "0" and number2 == "0":
        return "0", "0"

    if number1 == "0" and number2 == "1":
        return "1", "0"

    if number1 == "0" and number2 == "2":
        return "2", "0"

    if number1 == "0" and number2 == "3":
        return "3", "0"

    if number1 == "0" and number2 == "4":
        return "4", "0"

    if number1 == "0" and number2 == "5":
        return "5", "0"

    if number1 == "0" and number2 == "6":
        return "6", "0"

    if number1 == "0" and number2 == "7":
        return "7", "0"

    if number1 == "0" and number2 == "8":
        return "8", "0"

    if number1 == "0" and number2 == "9":
        return "9", "0"

    if number1 == "1" and number2 == "0":
        return "1", "0"

    if number1 == "1" and number2 == "1":
        return "2", "0"

    if number1 == "1" and number2 == "2":
        return "3", "0"

    if number1 == "1" and number2 == "3":
        return "4", "0"

    if number1 == "1" and number2 == "4":
        return "5", "0"

    if number1 == "1" and number2 == "5":
        return "6", "0"

    if number1 == "1" and number2 == "6":
        return "7", "0"

    if number1 == "1" and number2 == "7":
        return "8", "0"

    if number1 == "1" and number2 == "8":
        return "9", "0"

    if number1 == "1" and number2 == "9":
        return "0", "1"

    if number1 == "2" and number2 == "0":
        return "2", "0"

    if number1 == "2" and number2 == "1":
        return "3", "0"

    if number1 == "2" and number2 == "2":
        return "4", "0"

    if number1 == "2" and number2 == "3":
        return "5", "0"

    if number1 == "2" and number2 == "4":
        return "6", "0"

    if number1 == "2" and number2 == "5":
        return "7", "0"

    if number1 == "2" and number2 == "6":
        return "8", "0"

    if number1 == "2" and number2 == "7":
        return "9", "0"

    if number1 == "2" and number2 == "8":
        return "0", "1"

    if number1 == "2" and number2 == "9":
        return "1", "1"

    if number1 == "3" and number2 == "0":
        return "3", "0"

    if number1 == "3" and number2 == "1":
        return "4", "0"

    if number1 == "3" and number2 == "2":
        return "5", "0"

    if number1 == "3" and number2 == "3":
        return "6", "0"

    if number1 == "3" and number2 == "4":
        return "7", "0"

    if number1 == "3" and number2 == "5":
        return "8", "0"

    if number1 == "3" and number2 == "6":
        return "9", "0"

    if number1 == "3" and number2 == "7":
        return "0", "1"

    if number1 == "3" and number2 == "8":
        return "1", "1"

    if number1 == "3" and number2 == "9":
        return "2", "1"

    if number1 == "4" and number2 == "0":
        return "4", "0"

    if number1 == "4" and number2 == "1":
        return "5", "0"

    if number1 == "4" and number2 == "2":
        return "6", "0"

    if number1 == "4" and number2 == "3":
        return "7", "0"

    if number1 == "4" and number2 == "4":
        return "8", "0"

    if number1 == "4" and number2 == "5":
        return "9", "0"

    if number1 == "4" and number2 == "6":
        return "0", "1"

    if number1 == "4" and number2 == "7":
        return "1", "1"

    if number1 == "4" and number2 == "8":
        return "2", "1"

    if number1 == "4" and number2 == "9":
        return "3", "1"

    if number1 == "5" and number2 == "0":
        return "5", "0"

    if number1 == "5" and number2 == "1":
        return "6", "0"

    if number1 == "5" and number2 == "2":
        return "7", "0"

    if number1 == "5" and number2 == "3":
        return "8", "0"

    if number1 == "5" and number2 == "4":
        return "9", "0"

    if number1 == "5" and number2 == "5":
        return "0", "1"

    if number1 == "5" and number2 == "6":
        return "1", "1"

    if number1 == "5" and number2 == "7":
        return "2", "1"

    if number1 == "5" and number2 == "8":
        return "3", "1"

    if number1 == "5" and number2 == "9":
        return "4", "1"

    if number1 == "6" and number2 == "0":
        return "6", "0"

    if number1 == "6" and number2 == "1":
        return "7", "0"

    if number1 == "6" and number2 == "2":
        return "8", "0"

    if number1 == "6" and number2 == "3":
        return "9", "0"

    if number1 == "6" and number2 == "4":
        return "0", "1"

    if number1 == "6" and number2 == "5":
        return "1", "1"

    if number1 == "6" and number2 == "6":
        return "2", "1"

    if number1 == "6" and number2 == "7":
        return "3", "1"

    if number1 == "6" and number2 == "8":
        return "4", "1"

    if number1 == "6" and number2 == "9":
        return "5", "1"

    if number1 == "7" and number2 == "0":
        return "7", "0"

    if number1 == "7" and number2 == "1":
        return "8", "0"

    if number1 == "7" and number2 == "2":
        return "9", "0"

    if number1 == "7" and number2 == "3":
        return "0", "1"

    if number1 == "7" and number2 == "4":
        return "1", "1"

    if number1 == "7" and number2 == "5":
        return "2", "1"

    if number1 == "7" and number2 == "6":
        return "3", "1"

    if number1 == "7" and number2 == "7":
        return "4", "1"

    if number1 == "7" and number2 == "8":
        return "5", "1"

    if number1 == "7" and number2 == "9":
        return "6", "1"

    if number1 == "8" and number2 == "0":
        return "8", "0"

    if number1 == "8" and number2 == "1":
        return "9", "0"

    if number1 == "8" and number2 == "2":
        return "0", "1"

    if number1 == "8" and number2 == "3":
        return "1", "1"

    if number1 == "8" and number2 == "4":
        return "2", "1"

    if number1 == "8" and number2 == "5":
        return "3", "1"

    if number1 == "8" and number2 == "6":
        return "4", "1"

    if number1 == "8" and number2 == "7":
        return "5", "1"

    if number1 == "8" and number2 == "8":
        return "6", "1"

    if number1 == "8" and number2 == "9":
        return "7", "1"

    if number1 == "9" and number2 == "0":
        return "9", "0"

    if number1 == "9" and number2 == "1":
        return "0", "1"

    if number1 == "9" and number2 == "2":
        return "1", "1"

    if number1 == "9" and number2 == "3":
        return "2", "1"

    if number1 == "9" and number2 == "4":
        return "3", "1"

    if number1 == "9" and number2 == "5":
        return "4", "1"

    if number1 == "9" and number2 == "6":
        return "5", "1"

    if number1 == "9" and number2 == "7":
        return "6", "1"

    if number1 == "9" and number2 == "8":
        return "7", "1"

    if number1 == "9" and number2 == "9":
        return "8", "1"


def ADD_N_N_N(number1: str, number2: str, number3: str):
    number1 = str(number1)
    number2 = str(number2)
    number3 = str(number3)

    if number1 == "0" and number2 == "0" and number3 == "0":
        return "0", "0"

    if number1 == "0" and number2 == "0" and number3 == "1":
        return "1", "0"

    if number1 == "0" and number2 == "0" and number3 == "2":
        return "2", "0"

    if number1 == "0" and number2 == "0" and number3 == "3":
        return "3", "0"

    if number1 == "0" and number2 == "0" and number3 == "4":
        return "4", "0"

    if number1 == "0" and number2 == "0" and number3 == "5":
        return "5", "0"

    if number1 == "0" and number2 == "0" and number3 == "6":
        return "6", "0"

    if number1 == "0" and number2 == "0" and number3 == "7":
        return "7", "0"

    if number1 == "0" and number2 == "0" and number3 == "8":
        return "8", "0"

    if number1 == "0" and number2 == "0" and number3 == "9":
        return "9", "0"

    if number1 == "0" and number2 == "1" and number3 == "0":
        return "1", "0"

    if number1 == "0" and number2 == "1" and number3 == "1":
        return "2", "0"

    if number1 == "0" and number2 == "1" and number3 == "2":
        return "3", "0"

    if number1 == "0" and number2 == "1" and number3 == "3":
        return "4", "0"

    if number1 == "0" and number2 == "1" and number3 == "4":
        return "5", "0"

    if number1 == "0" and number2 == "1" and number3 == "5":
        return "6", "0"

    if number1 == "0" and number2 == "1" and number3 == "6":
        return "7", "0"

    if number1 == "0" and number2 == "1" and number3 == "7":
        return "8", "0"

    if number1 == "0" and number2 == "1" and number3 == "8":
        return "9", "0"

    if number1 == "0" and number2 == "1" and number3 == "9":
        return "0", "1"

    if number1 == "0" and number2 == "2" and number3 == "0":
        return "2", "0"

    if number1 == "0" and number2 == "2" and number3 == "1":
        return "3", "0"

    if number1 == "0" and number2 == "2" and number3 == "2":
        return "4", "0"

    if number1 == "0" and number2 == "2" and number3 == "3":
        return "5", "0"

    if number1 == "0" and number2 == "2" and number3 == "4":
        return "6", "0"

    if number1 == "0" and number2 == "2" and number3 == "5":
        return "7", "0"

    if number1 == "0" and number2 == "2" and number3 == "6":
        return "8", "0"

    if number1 == "0" and number2 == "2" and number3 == "7":
        return "9", "0"

    if number1 == "0" and number2 == "2" and number3 == "8":
        return "0", "1"

    if number1 == "0" and number2 == "2" and number3 == "9":
        return "1", "1"

    if number1 == "0" and number2 == "3" and number3 == "0":
        return "3", "0"

    if number1 == "0" and number2 == "3" and number3 == "1":
        return "4", "0"

    if number1 == "0" and number2 == "3" and number3 == "2":
        return "5", "0"

    if number1 == "0" and number2 == "3" and number3 == "3":
        return "6", "0"

    if number1 == "0" and number2 == "3" and number3 == "4":
        return "7", "0"

    if number1 == "0" and number2 == "3" and number3 == "5":
        return "8", "0"

    if number1 == "0" and number2 == "3" and number3 == "6":
        return "9", "0"

    if number1 == "0" and number2 == "3" and number3 == "7":
        return "0", "1"

    if number1 == "0" and number2 == "3" and number3 == "8":
        return "1", "1"

    if number1 == "0" and number2 == "3" and number3 == "9":
        return "2", "1"

    if number1 == "0" and number2 == "4" and number3 == "0":
        return "4", "0"

    if number1 == "0" and number2 == "4" and number3 == "1":
        return "5", "0"

    if number1 == "0" and number2 == "4" and number3 == "2":
        return "6", "0"

    if number1 == "0" and number2 == "4" and number3 == "3":
        return "7", "0"

    if number1 == "0" and number2 == "4" and number3 == "4":
        return "8", "0"

    if number1 == "0" and number2 == "4" and number3 == "5":
        return "9", "0"

    if number1 == "0" and number2 == "4" and number3 == "6":
        return "0", "1"

    if number1 == "0" and number2 == "4" and number3 == "7":
        return "1", "1"

    if number1 == "0" and number2 == "4" and number3 == "8":
        return "2", "1"

    if number1 == "0" and number2 == "4" and number3 == "9":
        return "3", "1"

    if number1 == "0" and number2 == "5" and number3 == "0":
        return "5", "0"

    if number1 == "0" and number2 == "5" and number3 == "1":
        return "6", "0"

    if number1 == "0" and number2 == "5" and number3 == "2":
        return "7", "0"

    if number1 == "0" and number2 == "5" and number3 == "3":
        return "8", "0"

    if number1 == "0" and number2 == "5" and number3 == "4":
        return "9", "0"

    if number1 == "0" and number2 == "5" and number3 == "5":
        return "0", "1"

    if number1 == "0" and number2 == "5" and number3 == "6":
        return "1", "1"

    if number1 == "0" and number2 == "5" and number3 == "7":
        return "2", "1"

    if number1 == "0" and number2 == "5" and number3 == "8":
        return "3", "1"

    if number1 == "0" and number2 == "5" and number3 == "9":
        return "4", "1"

    if number1 == "0" and number2 == "6" and number3 == "0":
        return "6", "0"

    if number1 == "0" and number2 == "6" and number3 == "1":
        return "7", "0"

    if number1 == "0" and number2 == "6" and number3 == "2":
        return "8", "0"

    if number1 == "0" and number2 == "6" and number3 == "3":
        return "9", "0"

    if number1 == "0" and number2 == "6" and number3 == "4":
        return "0", "1"

    if number1 == "0" and number2 == "6" and number3 == "5":
        return "1", "1"

    if number1 == "0" and number2 == "6" and number3 == "6":
        return "2", "1"

    if number1 == "0" and number2 == "6" and number3 == "7":
        return "3", "1"

    if number1 == "0" and number2 == "6" and number3 == "8":
        return "4", "1"

    if number1 == "0" and number2 == "6" and number3 == "9":
        return "5", "1"

    if number1 == "0" and number2 == "7" and number3 == "0":
        return "7", "0"

    if number1 == "0" and number2 == "7" and number3 == "1":
        return "8", "0"

    if number1 == "0" and number2 == "7" and number3 == "2":
        return "9", "0"

    if number1 == "0" and number2 == "7" and number3 == "3":
        return "0", "1"

    if number1 == "0" and number2 == "7" and number3 == "4":
        return "1", "1"

    if number1 == "0" and number2 == "7" and number3 == "5":
        return "2", "1"

    if number1 == "0" and number2 == "7" and number3 == "6":
        return "3", "1"

    if number1 == "0" and number2 == "7" and number3 == "7":
        return "4", "1"

    if number1 == "0" and number2 == "7" and number3 == "8":
        return "5", "1"

    if number1 == "0" and number2 == "7" and number3 == "9":
        return "6", "1"

    if number1 == "0" and number2 == "8" and number3 == "0":
        return "8", "0"

    if number1 == "0" and number2 == "8" and number3 == "1":
        return "9", "0"

    if number1 == "0" and number2 == "8" and number3 == "2":
        return "0", "1"

    if number1 == "0" and number2 == "8" and number3 == "3":
        return "1", "1"

    if number1 == "0" and number2 == "8" and number3 == "4":
        return "2", "1"

    if number1 == "0" and number2 == "8" and number3 == "5":
        return "3", "1"

    if number1 == "0" and number2 == "8" and number3 == "6":
        return "4", "1"

    if number1 == "0" and number2 == "8" and number3 == "7":
        return "5", "1"

    if number1 == "0" and number2 == "8" and number3 == "8":
        return "6", "1"

    if number1 == "0" and number2 == "8" and number3 == "9":
        return "7", "1"

    if number1 == "0" and number2 == "9" and number3 == "0":
        return "9", "0"

    if number1 == "0" and number2 == "9" and number3 == "1":
        return "0", "1"

    if number1 == "0" and number2 == "9" and number3 == "2":
        return "1", "1"

    if number1 == "0" and number2 == "9" and number3 == "3":
        return "2", "1"

    if number1 == "0" and number2 == "9" and number3 == "4":
        return "3", "1"

    if number1 == "0" and number2 == "9" and number3 == "5":
        return "4", "1"

    if number1 == "0" and number2 == "9" and number3 == "6":
        return "5", "1"

    if number1 == "0" and number2 == "9" and number3 == "7":
        return "6", "1"

    if number1 == "0" and number2 == "9" and number3 == "8":
        return "7", "1"

    if number1 == "0" and number2 == "9" and number3 == "9":
        return "8", "1"

    if number1 == "1" and number2 == "0" and number3 == "0":
        return "1", "0"

    if number1 == "1" and number2 == "0" and number3 == "1":
        return "2", "0"

    if number1 == "1" and number2 == "0" and number3 == "2":
        return "3", "0"

    if number1 == "1" and number2 == "0" and number3 == "3":
        return "4", "0"

    if number1 == "1" and number2 == "0" and number3 == "4":
        return "5", "0"

    if number1 == "1" and number2 == "0" and number3 == "5":
        return "6", "0"

    if number1 == "1" and number2 == "0" and number3 == "6":
        return "7", "0"

    if number1 == "1" and number2 == "0" and number3 == "7":
        return "8", "0"

    if number1 == "1" and number2 == "0" and number3 == "8":
        return "9", "0"

    if number1 == "1" and number2 == "0" and number3 == "9":
        return "0", "1"

    if number1 == "1" and number2 == "1" and number3 == "0":
        return "2", "0"

    if number1 == "1" and number2 == "1" and number3 == "1":
        return "3", "0"

    if number1 == "1" and number2 == "1" and number3 == "2":
        return "4", "0"

    if number1 == "1" and number2 == "1" and number3 == "3":
        return "5", "0"

    if number1 == "1" and number2 == "1" and number3 == "4":
        return "6", "0"

    if number1 == "1" and number2 == "1" and number3 == "5":
        return "7", "0"

    if number1 == "1" and number2 == "1" and number3 == "6":
        return "8", "0"

    if number1 == "1" and number2 == "1" and number3 == "7":
        return "9", "0"

    if number1 == "1" and number2 == "1" and number3 == "8":
        return "0", "1"

    if number1 == "1" and number2 == "1" and number3 == "9":
        return "1", "1"

    if number1 == "1" and number2 == "2" and number3 == "0":
        return "3", "0"

    if number1 == "1" and number2 == "2" and number3 == "1":
        return "4", "0"

    if number1 == "1" and number2 == "2" and number3 == "2":
        return "5", "0"

    if number1 == "1" and number2 == "2" and number3 == "3":
        return "6", "0"

    if number1 == "1" and number2 == "2" and number3 == "4":
        return "7", "0"

    if number1 == "1" and number2 == "2" and number3 == "5":
        return "8", "0"

    if number1 == "1" and number2 == "2" and number3 == "6":
        return "9", "0"

    if number1 == "1" and number2 == "2" and number3 == "7":
        return "0", "1"

    if number1 == "1" and number2 == "2" and number3 == "8":
        return "1", "1"

    if number1 == "1" and number2 == "2" and number3 == "9":
        return "2", "1"

    if number1 == "1" and number2 == "3" and number3 == "0":
        return "4", "0"

    if number1 == "1" and number2 == "3" and number3 == "1":
        return "5", "0"

    if number1 == "1" and number2 == "3" and number3 == "2":
        return "6", "0"

    if number1 == "1" and number2 == "3" and number3 == "3":
        return "7", "0"

    if number1 == "1" and number2 == "3" and number3 == "4":
        return "8", "0"

    if number1 == "1" and number2 == "3" and number3 == "5":
        return "9", "0"

    if number1 == "1" and number2 == "3" and number3 == "6":
        return "0", "1"

    if number1 == "1" and number2 == "3" and number3 == "7":
        return "1", "1"

    if number1 == "1" and number2 == "3" and number3 == "8":
        return "2", "1"

    if number1 == "1" and number2 == "3" and number3 == "9":
        return "3", "1"

    if number1 == "1" and number2 == "4" and number3 == "0":
        return "5", "0"

    if number1 == "1" and number2 == "4" and number3 == "1":
        return "6", "0"

    if number1 == "1" and number2 == "4" and number3 == "2":
        return "7", "0"

    if number1 == "1" and number2 == "4" and number3 == "3":
        return "8", "0"

    if number1 == "1" and number2 == "4" and number3 == "4":
        return "9", "0"

    if number1 == "1" and number2 == "4" and number3 == "5":
        return "0", "1"

    if number1 == "1" and number2 == "4" and number3 == "6":
        return "1", "1"

    if number1 == "1" and number2 == "4" and number3 == "7":
        return "2", "1"

    if number1 == "1" and number2 == "4" and number3 == "8":
        return "3", "1"

    if number1 == "1" and number2 == "4" and number3 == "9":
        return "4", "1"

    if number1 == "1" and number2 == "5" and number3 == "0":
        return "6", "0"

    if number1 == "1" and number2 == "5" and number3 == "1":
        return "7", "0"

    if number1 == "1" and number2 == "5" and number3 == "2":
        return "8", "0"

    if number1 == "1" and number2 == "5" and number3 == "3":
        return "9", "0"

    if number1 == "1" and number2 == "5" and number3 == "4":
        return "0", "1"

    if number1 == "1" and number2 == "5" and number3 == "5":
        return "1", "1"

    if number1 == "1" and number2 == "5" and number3 == "6":
        return "2", "1"

    if number1 == "1" and number2 == "5" and number3 == "7":
        return "3", "1"

    if number1 == "1" and number2 == "5" and number3 == "8":
        return "4", "1"

    if number1 == "1" and number2 == "5" and number3 == "9":
        return "5", "1"

    if number1 == "1" and number2 == "6" and number3 == "0":
        return "7", "0"

    if number1 == "1" and number2 == "6" and number3 == "1":
        return "8", "0"

    if number1 == "1" and number2 == "6" and number3 == "2":
        return "9", "0"

    if number1 == "1" and number2 == "6" and number3 == "3":
        return "0", "1"

    if number1 == "1" and number2 == "6" and number3 == "4":
        return "1", "1"

    if number1 == "1" and number2 == "6" and number3 == "5":
        return "2", "1"

    if number1 == "1" and number2 == "6" and number3 == "6":
        return "3", "1"

    if number1 == "1" and number2 == "6" and number3 == "7":
        return "4", "1"

    if number1 == "1" and number2 == "6" and number3 == "8":
        return "5", "1"

    if number1 == "1" and number2 == "6" and number3 == "9":
        return "6", "1"

    if number1 == "1" and number2 == "7" and number3 == "0":
        return "8", "0"

    if number1 == "1" and number2 == "7" and number3 == "1":
        return "9", "0"

    if number1 == "1" and number2 == "7" and number3 == "2":
        return "0", "1"

    if number1 == "1" and number2 == "7" and number3 == "3":
        return "1", "1"

    if number1 == "1" and number2 == "7" and number3 == "4":
        return "2", "1"

    if number1 == "1" and number2 == "7" and number3 == "5":
        return "3", "1"

    if number1 == "1" and number2 == "7" and number3 == "6":
        return "4", "1"

    if number1 == "1" and number2 == "7" and number3 == "7":
        return "5", "1"

    if number1 == "1" and number2 == "7" and number3 == "8":
        return "6", "1"

    if number1 == "1" and number2 == "7" and number3 == "9":
        return "7", "1"

    if number1 == "1" and number2 == "8" and number3 == "0":
        return "9", "0"

    if number1 == "1" and number2 == "8" and number3 == "1":
        return "0", "1"

    if number1 == "1" and number2 == "8" and number3 == "2":
        return "1", "1"

    if number1 == "1" and number2 == "8" and number3 == "3":
        return "2", "1"

    if number1 == "1" and number2 == "8" and number3 == "4":
        return "3", "1"

    if number1 == "1" and number2 == "8" and number3 == "5":
        return "4", "1"

    if number1 == "1" and number2 == "8" and number3 == "6":
        return "5", "1"

    if number1 == "1" and number2 == "8" and number3 == "7":
        return "6", "1"

    if number1 == "1" and number2 == "8" and number3 == "8":
        return "7", "1"

    if number1 == "1" and number2 == "8" and number3 == "9":
        return "8", "1"

    if number1 == "1" and number2 == "9" and number3 == "0":
        return "0", "1"

    if number1 == "1" and number2 == "9" and number3 == "1":
        return "1", "1"

    if number1 == "1" and number2 == "9" and number3 == "2":
        return "2", "1"

    if number1 == "1" and number2 == "9" and number3 == "3":
        return "3", "1"

    if number1 == "1" and number2 == "9" and number3 == "4":
        return "4", "1"

    if number1 == "1" and number2 == "9" and number3 == "5":
        return "5", "1"

    if number1 == "1" and number2 == "9" and number3 == "6":
        return "6", "1"

    if number1 == "1" and number2 == "9" and number3 == "7":
        return "7", "1"

    if number1 == "1" and number2 == "9" and number3 == "8":
        return "8", "1"

    if number1 == "1" and number2 == "9" and number3 == "9":
        return "9", "1"

    if number1 == "2" and number2 == "0" and number3 == "0":
        return "2", "0"

    if number1 == "2" and number2 == "0" and number3 == "1":
        return "3", "0"

    if number1 == "2" and number2 == "0" and number3 == "2":
        return "4", "0"

    if number1 == "2" and number2 == "0" and number3 == "3":
        return "5", "0"

    if number1 == "2" and number2 == "0" and number3 == "4":
        return "6", "0"

    if number1 == "2" and number2 == "0" and number3 == "5":
        return "7", "0"

    if number1 == "2" and number2 == "0" and number3 == "6":
        return "8", "0"

    if number1 == "2" and number2 == "0" and number3 == "7":
        return "9", "0"

    if number1 == "2" and number2 == "0" and number3 == "8":
        return "0", "1"

    if number1 == "2" and number2 == "0" and number3 == "9":
        return "1", "1"

    if number1 == "2" and number2 == "1" and number3 == "0":
        return "3", "0"

    if number1 == "2" and number2 == "1" and number3 == "1":
        return "4", "0"

    if number1 == "2" and number2 == "1" and number3 == "2":
        return "5", "0"

    if number1 == "2" and number2 == "1" and number3 == "3":
        return "6", "0"

    if number1 == "2" and number2 == "1" and number3 == "4":
        return "7", "0"

    if number1 == "2" and number2 == "1" and number3 == "5":
        return "8", "0"

    if number1 == "2" and number2 == "1" and number3 == "6":
        return "9", "0"

    if number1 == "2" and number2 == "1" and number3 == "7":
        return "0", "1"

    if number1 == "2" and number2 == "1" and number3 == "8":
        return "1", "1"

    if number1 == "2" and number2 == "1" and number3 == "9":
        return "2", "1"

    if number1 == "2" and number2 == "2" and number3 == "0":
        return "4", "0"

    if number1 == "2" and number2 == "2" and number3 == "1":
        return "5", "0"

    if number1 == "2" and number2 == "2" and number3 == "2":
        return "6", "0"

    if number1 == "2" and number2 == "2" and number3 == "3":
        return "7", "0"

    if number1 == "2" and number2 == "2" and number3 == "4":
        return "8", "0"

    if number1 == "2" and number2 == "2" and number3 == "5":
        return "9", "0"

    if number1 == "2" and number2 == "2" and number3 == "6":
        return "0", "1"

    if number1 == "2" and number2 == "2" and number3 == "7":
        return "1", "1"

    if number1 == "2" and number2 == "2" and number3 == "8":
        return "2", "1"

    if number1 == "2" and number2 == "2" and number3 == "9":
        return "3", "1"

    if number1 == "2" and number2 == "3" and number3 == "0":
        return "5", "0"

    if number1 == "2" and number2 == "3" and number3 == "1":
        return "6", "0"

    if number1 == "2" and number2 == "3" and number3 == "2":
        return "7", "0"

    if number1 == "2" and number2 == "3" and number3 == "3":
        return "8", "0"

    if number1 == "2" and number2 == "3" and number3 == "4":
        return "9", "0"

    if number1 == "2" and number2 == "3" and number3 == "5":
        return "0", "1"

    if number1 == "2" and number2 == "3" and number3 == "6":
        return "1", "1"

    if number1 == "2" and number2 == "3" and number3 == "7":
        return "2", "1"

    if number1 == "2" and number2 == "3" and number3 == "8":
        return "3", "1"

    if number1 == "2" and number2 == "3" and number3 == "9":
        return "4", "1"

    if number1 == "2" and number2 == "4" and number3 == "0":
        return "6", "0"

    if number1 == "2" and number2 == "4" and number3 == "1":
        return "7", "0"

    if number1 == "2" and number2 == "4" and number3 == "2":
        return "8", "0"

    if number1 == "2" and number2 == "4" and number3 == "3":
        return "9", "0"

    if number1 == "2" and number2 == "4" and number3 == "4":
        return "0", "1"

    if number1 == "2" and number2 == "4" and number3 == "5":
        return "1", "1"

    if number1 == "2" and number2 == "4" and number3 == "6":
        return "2", "1"

    if number1 == "2" and number2 == "4" and number3 == "7":
        return "3", "1"

    if number1 == "2" and number2 == "4" and number3 == "8":
        return "4", "1"

    if number1 == "2" and number2 == "4" and number3 == "9":
        return "5", "1"

    if number1 == "2" and number2 == "5" and number3 == "0":
        return "7", "0"

    if number1 == "2" and number2 == "5" and number3 == "1":
        return "8", "0"

    if number1 == "2" and number2 == "5" and number3 == "2":
        return "9", "0"

    if number1 == "2" and number2 == "5" and number3 == "3":
        return "0", "1"

    if number1 == "2" and number2 == "5" and number3 == "4":
        return "1", "1"

    if number1 == "2" and number2 == "5" and number3 == "5":
        return "2", "1"

    if number1 == "2" and number2 == "5" and number3 == "6":
        return "3", "1"

    if number1 == "2" and number2 == "5" and number3 == "7":
        return "4", "1"

    if number1 == "2" and number2 == "5" and number3 == "8":
        return "5", "1"

    if number1 == "2" and number2 == "5" and number3 == "9":
        return "6", "1"

    if number1 == "2" and number2 == "6" and number3 == "0":
        return "8", "0"

    if number1 == "2" and number2 == "6" and number3 == "1":
        return "9", "0"

    if number1 == "2" and number2 == "6" and number3 == "2":
        return "0", "1"

    if number1 == "2" and number2 == "6" and number3 == "3":
        return "1", "1"

    if number1 == "2" and number2 == "6" and number3 == "4":
        return "2", "1"

    if number1 == "2" and number2 == "6" and number3 == "5":
        return "3", "1"

    if number1 == "2" and number2 == "6" and number3 == "6":
        return "4", "1"

    if number1 == "2" and number2 == "6" and number3 == "7":
        return "5", "1"

    if number1 == "2" and number2 == "6" and number3 == "8":
        return "6", "1"

    if number1 == "2" and number2 == "6" and number3 == "9":
        return "7", "1"

    if number1 == "2" and number2 == "7" and number3 == "0":
        return "9", "0"

    if number1 == "2" and number2 == "7" and number3 == "1":
        return "0", "1"

    if number1 == "2" and number2 == "7" and number3 == "2":
        return "1", "1"

    if number1 == "2" and number2 == "7" and number3 == "3":
        return "2", "1"

    if number1 == "2" and number2 == "7" and number3 == "4":
        return "3", "1"

    if number1 == "2" and number2 == "7" and number3 == "5":
        return "4", "1"

    if number1 == "2" and number2 == "7" and number3 == "6":
        return "5", "1"

    if number1 == "2" and number2 == "7" and number3 == "7":
        return "6", "1"

    if number1 == "2" and number2 == "7" and number3 == "8":
        return "7", "1"

    if number1 == "2" and number2 == "7" and number3 == "9":
        return "8", "1"

    if number1 == "2" and number2 == "8" and number3 == "0":
        return "0", "1"

    if number1 == "2" and number2 == "8" and number3 == "1":
        return "1", "1"

    if number1 == "2" and number2 == "8" and number3 == "2":
        return "2", "1"

    if number1 == "2" and number2 == "8" and number3 == "3":
        return "3", "1"

    if number1 == "2" and number2 == "8" and number3 == "4":
        return "4", "1"

    if number1 == "2" and number2 == "8" and number3 == "5":
        return "5", "1"

    if number1 == "2" and number2 == "8" and number3 == "6":
        return "6", "1"

    if number1 == "2" and number2 == "8" and number3 == "7":
        return "7", "1"

    if number1 == "2" and number2 == "8" and number3 == "8":
        return "8", "1"

    if number1 == "2" and number2 == "8" and number3 == "9":
        return "9", "1"

    if number1 == "2" and number2 == "9" and number3 == "0":
        return "1", "1"

    if number1 == "2" and number2 == "9" and number3 == "1":
        return "2", "1"

    if number1 == "2" and number2 == "9" and number3 == "2":
        return "3", "1"

    if number1 == "2" and number2 == "9" and number3 == "3":
        return "4", "1"

    if number1 == "2" and number2 == "9" and number3 == "4":
        return "5", "1"

    if number1 == "2" and number2 == "9" and number3 == "5":
        return "6", "1"

    if number1 == "2" and number2 == "9" and number3 == "6":
        return "7", "1"

    if number1 == "2" and number2 == "9" and number3 == "7":
        return "8", "1"

    if number1 == "2" and number2 == "9" and number3 == "8":
        return "9", "1"

    if number1 == "2" and number2 == "9" and number3 == "9":
        return "0", "2"

    if number1 == "3" and number2 == "0" and number3 == "0":
        return "3", "0"

    if number1 == "3" and number2 == "0" and number3 == "1":
        return "4", "0"

    if number1 == "3" and number2 == "0" and number3 == "2":
        return "5", "0"

    if number1 == "3" and number2 == "0" and number3 == "3":
        return "6", "0"

    if number1 == "3" and number2 == "0" and number3 == "4":
        return "7", "0"

    if number1 == "3" and number2 == "0" and number3 == "5":
        return "8", "0"

    if number1 == "3" and number2 == "0" and number3 == "6":
        return "9", "0"

    if number1 == "3" and number2 == "0" and number3 == "7":
        return "0", "1"

    if number1 == "3" and number2 == "0" and number3 == "8":
        return "1", "1"

    if number1 == "3" and number2 == "0" and number3 == "9":
        return "2", "1"

    if number1 == "3" and number2 == "1" and number3 == "0":
        return "4", "0"

    if number1 == "3" and number2 == "1" and number3 == "1":
        return "5", "0"

    if number1 == "3" and number2 == "1" and number3 == "2":
        return "6", "0"

    if number1 == "3" and number2 == "1" and number3 == "3":
        return "7", "0"

    if number1 == "3" and number2 == "1" and number3 == "4":
        return "8", "0"

    if number1 == "3" and number2 == "1" and number3 == "5":
        return "9", "0"

    if number1 == "3" and number2 == "1" and number3 == "6":
        return "0", "1"

    if number1 == "3" and number2 == "1" and number3 == "7":
        return "1", "1"

    if number1 == "3" and number2 == "1" and number3 == "8":
        return "2", "1"

    if number1 == "3" and number2 == "1" and number3 == "9":
        return "3", "1"

    if number1 == "3" and number2 == "2" and number3 == "0":
        return "5", "0"

    if number1 == "3" and number2 == "2" and number3 == "1":
        return "6", "0"

    if number1 == "3" and number2 == "2" and number3 == "2":
        return "7", "0"

    if number1 == "3" and number2 == "2" and number3 == "3":
        return "8", "0"

    if number1 == "3" and number2 == "2" and number3 == "4":
        return "9", "0"

    if number1 == "3" and number2 == "2" and number3 == "5":
        return "0", "1"

    if number1 == "3" and number2 == "2" and number3 == "6":
        return "1", "1"

    if number1 == "3" and number2 == "2" and number3 == "7":
        return "2", "1"

    if number1 == "3" and number2 == "2" and number3 == "8":
        return "3", "1"

    if number1 == "3" and number2 == "2" and number3 == "9":
        return "4", "1"

    if number1 == "3" and number2 == "3" and number3 == "0":
        return "6", "0"

    if number1 == "3" and number2 == "3" and number3 == "1":
        return "7", "0"

    if number1 == "3" and number2 == "3" and number3 == "2":
        return "8", "0"

    if number1 == "3" and number2 == "3" and number3 == "3":
        return "9", "0"

    if number1 == "3" and number2 == "3" and number3 == "4":
        return "0", "1"

    if number1 == "3" and number2 == "3" and number3 == "5":
        return "1", "1"

    if number1 == "3" and number2 == "3" and number3 == "6":
        return "2", "1"

    if number1 == "3" and number2 == "3" and number3 == "7":
        return "3", "1"

    if number1 == "3" and number2 == "3" and number3 == "8":
        return "4", "1"

    if number1 == "3" and number2 == "3" and number3 == "9":
        return "5", "1"

    if number1 == "3" and number2 == "4" and number3 == "0":
        return "7", "0"

    if number1 == "3" and number2 == "4" and number3 == "1":
        return "8", "0"

    if number1 == "3" and number2 == "4" and number3 == "2":
        return "9", "0"

    if number1 == "3" and number2 == "4" and number3 == "3":
        return "0", "1"

    if number1 == "3" and number2 == "4" and number3 == "4":
        return "1", "1"

    if number1 == "3" and number2 == "4" and number3 == "5":
        return "2", "1"

    if number1 == "3" and number2 == "4" and number3 == "6":
        return "3", "1"

    if number1 == "3" and number2 == "4" and number3 == "7":
        return "4", "1"

    if number1 == "3" and number2 == "4" and number3 == "8":
        return "5", "1"

    if number1 == "3" and number2 == "4" and number3 == "9":
        return "6", "1"

    if number1 == "3" and number2 == "5" and number3 == "0":
        return "8", "0"

    if number1 == "3" and number2 == "5" and number3 == "1":
        return "9", "0"

    if number1 == "3" and number2 == "5" and number3 == "2":
        return "0", "1"

    if number1 == "3" and number2 == "5" and number3 == "3":
        return "1", "1"

    if number1 == "3" and number2 == "5" and number3 == "4":
        return "2", "1"

    if number1 == "3" and number2 == "5" and number3 == "5":
        return "3", "1"

    if number1 == "3" and number2 == "5" and number3 == "6":
        return "4", "1"

    if number1 == "3" and number2 == "5" and number3 == "7":
        return "5", "1"

    if number1 == "3" and number2 == "5" and number3 == "8":
        return "6", "1"

    if number1 == "3" and number2 == "5" and number3 == "9":
        return "7", "1"

    if number1 == "3" and number2 == "6" and number3 == "0":
        return "9", "0"

    if number1 == "3" and number2 == "6" and number3 == "1":
        return "0", "1"

    if number1 == "3" and number2 == "6" and number3 == "2":
        return "1", "1"

    if number1 == "3" and number2 == "6" and number3 == "3":
        return "2", "1"

    if number1 == "3" and number2 == "6" and number3 == "4":
        return "3", "1"

    if number1 == "3" and number2 == "6" and number3 == "5":
        return "4", "1"

    if number1 == "3" and number2 == "6" and number3 == "6":
        return "5", "1"

    if number1 == "3" and number2 == "6" and number3 == "7":
        return "6", "1"

    if number1 == "3" and number2 == "6" and number3 == "8":
        return "7", "1"

    if number1 == "3" and number2 == "6" and number3 == "9":
        return "8", "1"

    if number1 == "3" and number2 == "7" and number3 == "0":
        return "0", "1"

    if number1 == "3" and number2 == "7" and number3 == "1":
        return "1", "1"

    if number1 == "3" and number2 == "7" and number3 == "2":
        return "2", "1"

    if number1 == "3" and number2 == "7" and number3 == "3":
        return "3", "1"

    if number1 == "3" and number2 == "7" and number3 == "4":
        return "4", "1"

    if number1 == "3" and number2 == "7" and number3 == "5":
        return "5", "1"

    if number1 == "3" and number2 == "7" and number3 == "6":
        return "6", "1"

    if number1 == "3" and number2 == "7" and number3 == "7":
        return "7", "1"

    if number1 == "3" and number2 == "7" and number3 == "8":
        return "8", "1"

    if number1 == "3" and number2 == "7" and number3 == "9":
        return "9", "1"

    if number1 == "3" and number2 == "8" and number3 == "0":
        return "1", "1"

    if number1 == "3" and number2 == "8" and number3 == "1":
        return "2", "1"

    if number1 == "3" and number2 == "8" and number3 == "2":
        return "3", "1"

    if number1 == "3" and number2 == "8" and number3 == "3":
        return "4", "1"

    if number1 == "3" and number2 == "8" and number3 == "4":
        return "5", "1"

    if number1 == "3" and number2 == "8" and number3 == "5":
        return "6", "1"

    if number1 == "3" and number2 == "8" and number3 == "6":
        return "7", "1"

    if number1 == "3" and number2 == "8" and number3 == "7":
        return "8", "1"

    if number1 == "3" and number2 == "8" and number3 == "8":
        return "9", "1"

    if number1 == "3" and number2 == "8" and number3 == "9":
        return "0", "2"

    if number1 == "3" and number2 == "9" and number3 == "0":
        return "2", "1"

    if number1 == "3" and number2 == "9" and number3 == "1":
        return "3", "1"

    if number1 == "3" and number2 == "9" and number3 == "2":
        return "4", "1"

    if number1 == "3" and number2 == "9" and number3 == "3":
        return "5", "1"

    if number1 == "3" and number2 == "9" and number3 == "4":
        return "6", "1"

    if number1 == "3" and number2 == "9" and number3 == "5":
        return "7", "1"

    if number1 == "3" and number2 == "9" and number3 == "6":
        return "8", "1"

    if number1 == "3" and number2 == "9" and number3 == "7":
        return "9", "1"

    if number1 == "3" and number2 == "9" and number3 == "8":
        return "0", "2"

    if number1 == "3" and number2 == "9" and number3 == "9":
        return "1", "2"

    if number1 == "4" and number2 == "0" and number3 == "0":
        return "4", "0"

    if number1 == "4" and number2 == "0" and number3 == "1":
        return "5", "0"

    if number1 == "4" and number2 == "0" and number3 == "2":
        return "6", "0"

    if number1 == "4" and number2 == "0" and number3 == "3":
        return "7", "0"

    if number1 == "4" and number2 == "0" and number3 == "4":
        return "8", "0"

    if number1 == "4" and number2 == "0" and number3 == "5":
        return "9", "0"

    if number1 == "4" and number2 == "0" and number3 == "6":
        return "0", "1"

    if number1 == "4" and number2 == "0" and number3 == "7":
        return "1", "1"

    if number1 == "4" and number2 == "0" and number3 == "8":
        return "2", "1"

    if number1 == "4" and number2 == "0" and number3 == "9":
        return "3", "1"

    if number1 == "4" and number2 == "1" and number3 == "0":
        return "5", "0"

    if number1 == "4" and number2 == "1" and number3 == "1":
        return "6", "0"

    if number1 == "4" and number2 == "1" and number3 == "2":
        return "7", "0"

    if number1 == "4" and number2 == "1" and number3 == "3":
        return "8", "0"

    if number1 == "4" and number2 == "1" and number3 == "4":
        return "9", "0"

    if number1 == "4" and number2 == "1" and number3 == "5":
        return "0", "1"

    if number1 == "4" and number2 == "1" and number3 == "6":
        return "1", "1"

    if number1 == "4" and number2 == "1" and number3 == "7":
        return "2", "1"

    if number1 == "4" and number2 == "1" and number3 == "8":
        return "3", "1"

    if number1 == "4" and number2 == "1" and number3 == "9":
        return "4", "1"

    if number1 == "4" and number2 == "2" and number3 == "0":
        return "6", "0"

    if number1 == "4" and number2 == "2" and number3 == "1":
        return "7", "0"

    if number1 == "4" and number2 == "2" and number3 == "2":
        return "8", "0"

    if number1 == "4" and number2 == "2" and number3 == "3":
        return "9", "0"

    if number1 == "4" and number2 == "2" and number3 == "4":
        return "0", "1"

    if number1 == "4" and number2 == "2" and number3 == "5":
        return "1", "1"

    if number1 == "4" and number2 == "2" and number3 == "6":
        return "2", "1"

    if number1 == "4" and number2 == "2" and number3 == "7":
        return "3", "1"

    if number1 == "4" and number2 == "2" and number3 == "8":
        return "4", "1"

    if number1 == "4" and number2 == "2" and number3 == "9":
        return "5", "1"

    if number1 == "4" and number2 == "3" and number3 == "0":
        return "7", "0"

    if number1 == "4" and number2 == "3" and number3 == "1":
        return "8", "0"

    if number1 == "4" and number2 == "3" and number3 == "2":
        return "9", "0"

    if number1 == "4" and number2 == "3" and number3 == "3":
        return "0", "1"

    if number1 == "4" and number2 == "3" and number3 == "4":
        return "1", "1"

    if number1 == "4" and number2 == "3" and number3 == "5":
        return "2", "1"

    if number1 == "4" and number2 == "3" and number3 == "6":
        return "3", "1"

    if number1 == "4" and number2 == "3" and number3 == "7":
        return "4", "1"

    if number1 == "4" and number2 == "3" and number3 == "8":
        return "5", "1"

    if number1 == "4" and number2 == "3" and number3 == "9":
        return "6", "1"

    if number1 == "4" and number2 == "4" and number3 == "0":
        return "8", "0"

    if number1 == "4" and number2 == "4" and number3 == "1":
        return "9", "0"

    if number1 == "4" and number2 == "4" and number3 == "2":
        return "0", "1"

    if number1 == "4" and number2 == "4" and number3 == "3":
        return "1", "1"

    if number1 == "4" and number2 == "4" and number3 == "4":
        return "2", "1"

    if number1 == "4" and number2 == "4" and number3 == "5":
        return "3", "1"

    if number1 == "4" and number2 == "4" and number3 == "6":
        return "4", "1"

    if number1 == "4" and number2 == "4" and number3 == "7":
        return "5", "1"

    if number1 == "4" and number2 == "4" and number3 == "8":
        return "6", "1"

    if number1 == "4" and number2 == "4" and number3 == "9":
        return "7", "1"

    if number1 == "4" and number2 == "5" and number3 == "0":
        return "9", "0"

    if number1 == "4" and number2 == "5" and number3 == "1":
        return "0", "1"

    if number1 == "4" and number2 == "5" and number3 == "2":
        return "1", "1"

    if number1 == "4" and number2 == "5" and number3 == "3":
        return "2", "1"

    if number1 == "4" and number2 == "5" and number3 == "4":
        return "3", "1"

    if number1 == "4" and number2 == "5" and number3 == "5":
        return "4", "1"

    if number1 == "4" and number2 == "5" and number3 == "6":
        return "5", "1"

    if number1 == "4" and number2 == "5" and number3 == "7":
        return "6", "1"

    if number1 == "4" and number2 == "5" and number3 == "8":
        return "7", "1"

    if number1 == "4" and number2 == "5" and number3 == "9":
        return "8", "1"

    if number1 == "4" and number2 == "6" and number3 == "0":
        return "0", "1"

    if number1 == "4" and number2 == "6" and number3 == "1":
        return "1", "1"

    if number1 == "4" and number2 == "6" and number3 == "2":
        return "2", "1"

    if number1 == "4" and number2 == "6" and number3 == "3":
        return "3", "1"

    if number1 == "4" and number2 == "6" and number3 == "4":
        return "4", "1"

    if number1 == "4" and number2 == "6" and number3 == "5":
        return "5", "1"

    if number1 == "4" and number2 == "6" and number3 == "6":
        return "6", "1"

    if number1 == "4" and number2 == "6" and number3 == "7":
        return "7", "1"

    if number1 == "4" and number2 == "6" and number3 == "8":
        return "8", "1"

    if number1 == "4" and number2 == "6" and number3 == "9":
        return "9", "1"

    if number1 == "4" and number2 == "7" and number3 == "0":
        return "1", "1"

    if number1 == "4" and number2 == "7" and number3 == "1":
        return "2", "1"

    if number1 == "4" and number2 == "7" and number3 == "2":
        return "3", "1"

    if number1 == "4" and number2 == "7" and number3 == "3":
        return "4", "1"

    if number1 == "4" and number2 == "7" and number3 == "4":
        return "5", "1"

    if number1 == "4" and number2 == "7" and number3 == "5":
        return "6", "1"

    if number1 == "4" and number2 == "7" and number3 == "6":
        return "7", "1"

    if number1 == "4" and number2 == "7" and number3 == "7":
        return "8", "1"

    if number1 == "4" and number2 == "7" and number3 == "8":
        return "9", "1"

    if number1 == "4" and number2 == "7" and number3 == "9":
        return "0", "2"

    if number1 == "4" and number2 == "8" and number3 == "0":
        return "2", "1"

    if number1 == "4" and number2 == "8" and number3 == "1":
        return "3", "1"

    if number1 == "4" and number2 == "8" and number3 == "2":
        return "4", "1"

    if number1 == "4" and number2 == "8" and number3 == "3":
        return "5", "1"

    if number1 == "4" and number2 == "8" and number3 == "4":
        return "6", "1"

    if number1 == "4" and number2 == "8" and number3 == "5":
        return "7", "1"

    if number1 == "4" and number2 == "8" and number3 == "6":
        return "8", "1"

    if number1 == "4" and number2 == "8" and number3 == "7":
        return "9", "1"

    if number1 == "4" and number2 == "8" and number3 == "8":
        return "0", "2"

    if number1 == "4" and number2 == "8" and number3 == "9":
        return "1", "2"

    if number1 == "4" and number2 == "9" and number3 == "0":
        return "3", "1"

    if number1 == "4" and number2 == "9" and number3 == "1":
        return "4", "1"

    if number1 == "4" and number2 == "9" and number3 == "2":
        return "5", "1"

    if number1 == "4" and number2 == "9" and number3 == "3":
        return "6", "1"

    if number1 == "4" and number2 == "9" and number3 == "4":
        return "7", "1"

    if number1 == "4" and number2 == "9" and number3 == "5":
        return "8", "1"

    if number1 == "4" and number2 == "9" and number3 == "6":
        return "9", "1"

    if number1 == "4" and number2 == "9" and number3 == "7":
        return "0", "2"

    if number1 == "4" and number2 == "9" and number3 == "8":
        return "1", "2"

    if number1 == "4" and number2 == "9" and number3 == "9":
        return "2", "2"

    if number1 == "5" and number2 == "0" and number3 == "0":
        return "5", "0"

    if number1 == "5" and number2 == "0" and number3 == "1":
        return "6", "0"

    if number1 == "5" and number2 == "0" and number3 == "2":
        return "7", "0"

    if number1 == "5" and number2 == "0" and number3 == "3":
        return "8", "0"

    if number1 == "5" and number2 == "0" and number3 == "4":
        return "9", "0"

    if number1 == "5" and number2 == "0" and number3 == "5":
        return "0", "1"

    if number1 == "5" and number2 == "0" and number3 == "6":
        return "1", "1"

    if number1 == "5" and number2 == "0" and number3 == "7":
        return "2", "1"

    if number1 == "5" and number2 == "0" and number3 == "8":
        return "3", "1"

    if number1 == "5" and number2 == "0" and number3 == "9":
        return "4", "1"

    if number1 == "5" and number2 == "1" and number3 == "0":
        return "6", "0"

    if number1 == "5" and number2 == "1" and number3 == "1":
        return "7", "0"

    if number1 == "5" and number2 == "1" and number3 == "2":
        return "8", "0"

    if number1 == "5" and number2 == "1" and number3 == "3":
        return "9", "0"

    if number1 == "5" and number2 == "1" and number3 == "4":
        return "0", "1"

    if number1 == "5" and number2 == "1" and number3 == "5":
        return "1", "1"

    if number1 == "5" and number2 == "1" and number3 == "6":
        return "2", "1"

    if number1 == "5" and number2 == "1" and number3 == "7":
        return "3", "1"

    if number1 == "5" and number2 == "1" and number3 == "8":
        return "4", "1"

    if number1 == "5" and number2 == "1" and number3 == "9":
        return "5", "1"

    if number1 == "5" and number2 == "2" and number3 == "0":
        return "7", "0"

    if number1 == "5" and number2 == "2" and number3 == "1":
        return "8", "0"

    if number1 == "5" and number2 == "2" and number3 == "2":
        return "9", "0"

    if number1 == "5" and number2 == "2" and number3 == "3":
        return "0", "1"

    if number1 == "5" and number2 == "2" and number3 == "4":
        return "1", "1"

    if number1 == "5" and number2 == "2" and number3 == "5":
        return "2", "1"

    if number1 == "5" and number2 == "2" and number3 == "6":
        return "3", "1"

    if number1 == "5" and number2 == "2" and number3 == "7":
        return "4", "1"

    if number1 == "5" and number2 == "2" and number3 == "8":
        return "5", "1"

    if number1 == "5" and number2 == "2" and number3 == "9":
        return "6", "1"

    if number1 == "5" and number2 == "3" and number3 == "0":
        return "8", "0"

    if number1 == "5" and number2 == "3" and number3 == "1":
        return "9", "0"

    if number1 == "5" and number2 == "3" and number3 == "2":
        return "0", "1"

    if number1 == "5" and number2 == "3" and number3 == "3":
        return "1", "1"

    if number1 == "5" and number2 == "3" and number3 == "4":
        return "2", "1"

    if number1 == "5" and number2 == "3" and number3 == "5":
        return "3", "1"

    if number1 == "5" and number2 == "3" and number3 == "6":
        return "4", "1"

    if number1 == "5" and number2 == "3" and number3 == "7":
        return "5", "1"

    if number1 == "5" and number2 == "3" and number3 == "8":
        return "6", "1"

    if number1 == "5" and number2 == "3" and number3 == "9":
        return "7", "1"

    if number1 == "5" and number2 == "4" and number3 == "0":
        return "9", "0"

    if number1 == "5" and number2 == "4" and number3 == "1":
        return "0", "1"

    if number1 == "5" and number2 == "4" and number3 == "2":
        return "1", "1"

    if number1 == "5" and number2 == "4" and number3 == "3":
        return "2", "1"

    if number1 == "5" and number2 == "4" and number3 == "4":
        return "3", "1"

    if number1 == "5" and number2 == "4" and number3 == "5":
        return "4", "1"

    if number1 == "5" and number2 == "4" and number3 == "6":
        return "5", "1"

    if number1 == "5" and number2 == "4" and number3 == "7":
        return "6", "1"

    if number1 == "5" and number2 == "4" and number3 == "8":
        return "7", "1"

    if number1 == "5" and number2 == "4" and number3 == "9":
        return "8", "1"

    if number1 == "5" and number2 == "5" and number3 == "0":
        return "0", "1"

    if number1 == "5" and number2 == "5" and number3 == "1":
        return "1", "1"

    if number1 == "5" and number2 == "5" and number3 == "2":
        return "2", "1"

    if number1 == "5" and number2 == "5" and number3 == "3":
        return "3", "1"

    if number1 == "5" and number2 == "5" and number3 == "4":
        return "4", "1"

    if number1 == "5" and number2 == "5" and number3 == "5":
        return "5", "1"

    if number1 == "5" and number2 == "5" and number3 == "6":
        return "6", "1"

    if number1 == "5" and number2 == "5" and number3 == "7":
        return "7", "1"

    if number1 == "5" and number2 == "5" and number3 == "8":
        return "8", "1"

    if number1 == "5" and number2 == "5" and number3 == "9":
        return "9", "1"

    if number1 == "5" and number2 == "6" and number3 == "0":
        return "1", "1"

    if number1 == "5" and number2 == "6" and number3 == "1":
        return "2", "1"

    if number1 == "5" and number2 == "6" and number3 == "2":
        return "3", "1"

    if number1 == "5" and number2 == "6" and number3 == "3":
        return "4", "1"

    if number1 == "5" and number2 == "6" and number3 == "4":
        return "5", "1"

    if number1 == "5" and number2 == "6" and number3 == "5":
        return "6", "1"

    if number1 == "5" and number2 == "6" and number3 == "6":
        return "7", "1"

    if number1 == "5" and number2 == "6" and number3 == "7":
        return "8", "1"

    if number1 == "5" and number2 == "6" and number3 == "8":
        return "9", "1"

    if number1 == "5" and number2 == "6" and number3 == "9":
        return "0", "2"

    if number1 == "5" and number2 == "7" and number3 == "0":
        return "2", "1"

    if number1 == "5" and number2 == "7" and number3 == "1":
        return "3", "1"

    if number1 == "5" and number2 == "7" and number3 == "2":
        return "4", "1"

    if number1 == "5" and number2 == "7" and number3 == "3":
        return "5", "1"

    if number1 == "5" and number2 == "7" and number3 == "4":
        return "6", "1"

    if number1 == "5" and number2 == "7" and number3 == "5":
        return "7", "1"

    if number1 == "5" and number2 == "7" and number3 == "6":
        return "8", "1"

    if number1 == "5" and number2 == "7" and number3 == "7":
        return "9", "1"

    if number1 == "5" and number2 == "7" and number3 == "8":
        return "0", "2"

    if number1 == "5" and number2 == "7" and number3 == "9":
        return "1", "2"

    if number1 == "5" and number2 == "8" and number3 == "0":
        return "3", "1"

    if number1 == "5" and number2 == "8" and number3 == "1":
        return "4", "1"

    if number1 == "5" and number2 == "8" and number3 == "2":
        return "5", "1"

    if number1 == "5" and number2 == "8" and number3 == "3":
        return "6", "1"

    if number1 == "5" and number2 == "8" and number3 == "4":
        return "7", "1"

    if number1 == "5" and number2 == "8" and number3 == "5":
        return "8", "1"

    if number1 == "5" and number2 == "8" and number3 == "6":
        return "9", "1"

    if number1 == "5" and number2 == "8" and number3 == "7":
        return "0", "2"

    if number1 == "5" and number2 == "8" and number3 == "8":
        return "1", "2"

    if number1 == "5" and number2 == "8" and number3 == "9":
        return "2", "2"

    if number1 == "5" and number2 == "9" and number3 == "0":
        return "4", "1"

    if number1 == "5" and number2 == "9" and number3 == "1":
        return "5", "1"

    if number1 == "5" and number2 == "9" and number3 == "2":
        return "6", "1"

    if number1 == "5" and number2 == "9" and number3 == "3":
        return "7", "1"

    if number1 == "5" and number2 == "9" and number3 == "4":
        return "8", "1"

    if number1 == "5" and number2 == "9" and number3 == "5":
        return "9", "1"

    if number1 == "5" and number2 == "9" and number3 == "6":
        return "0", "2"

    if number1 == "5" and number2 == "9" and number3 == "7":
        return "1", "2"

    if number1 == "5" and number2 == "9" and number3 == "8":
        return "2", "2"

    if number1 == "5" and number2 == "9" and number3 == "9":
        return "3", "2"

    if number1 == "6" and number2 == "0" and number3 == "0":
        return "6", "0"

    if number1 == "6" and number2 == "0" and number3 == "1":
        return "7", "0"

    if number1 == "6" and number2 == "0" and number3 == "2":
        return "8", "0"

    if number1 == "6" and number2 == "0" and number3 == "3":
        return "9", "0"

    if number1 == "6" and number2 == "0" and number3 == "4":
        return "0", "1"

    if number1 == "6" and number2 == "0" and number3 == "5":
        return "1", "1"

    if number1 == "6" and number2 == "0" and number3 == "6":
        return "2", "1"

    if number1 == "6" and number2 == "0" and number3 == "7":
        return "3", "1"

    if number1 == "6" and number2 == "0" and number3 == "8":
        return "4", "1"

    if number1 == "6" and number2 == "0" and number3 == "9":
        return "5", "1"

    if number1 == "6" and number2 == "1" and number3 == "0":
        return "7", "0"

    if number1 == "6" and number2 == "1" and number3 == "1":
        return "8", "0"

    if number1 == "6" and number2 == "1" and number3 == "2":
        return "9", "0"

    if number1 == "6" and number2 == "1" and number3 == "3":
        return "0", "1"

    if number1 == "6" and number2 == "1" and number3 == "4":
        return "1", "1"

    if number1 == "6" and number2 == "1" and number3 == "5":
        return "2", "1"

    if number1 == "6" and number2 == "1" and number3 == "6":
        return "3", "1"

    if number1 == "6" and number2 == "1" and number3 == "7":
        return "4", "1"

    if number1 == "6" and number2 == "1" and number3 == "8":
        return "5", "1"

    if number1 == "6" and number2 == "1" and number3 == "9":
        return "6", "1"

    if number1 == "6" and number2 == "2" and number3 == "0":
        return "8", "0"

    if number1 == "6" and number2 == "2" and number3 == "1":
        return "9", "0"

    if number1 == "6" and number2 == "2" and number3 == "2":
        return "0", "1"

    if number1 == "6" and number2 == "2" and number3 == "3":
        return "1", "1"

    if number1 == "6" and number2 == "2" and number3 == "4":
        return "2", "1"

    if number1 == "6" and number2 == "2" and number3 == "5":
        return "3", "1"

    if number1 == "6" and number2 == "2" and number3 == "6":
        return "4", "1"

    if number1 == "6" and number2 == "2" and number3 == "7":
        return "5", "1"

    if number1 == "6" and number2 == "2" and number3 == "8":
        return "6", "1"

    if number1 == "6" and number2 == "2" and number3 == "9":
        return "7", "1"

    if number1 == "6" and number2 == "3" and number3 == "0":
        return "9", "0"

    if number1 == "6" and number2 == "3" and number3 == "1":
        return "0", "1"

    if number1 == "6" and number2 == "3" and number3 == "2":
        return "1", "1"

    if number1 == "6" and number2 == "3" and number3 == "3":
        return "2", "1"

    if number1 == "6" and number2 == "3" and number3 == "4":
        return "3", "1"

    if number1 == "6" and number2 == "3" and number3 == "5":
        return "4", "1"

    if number1 == "6" and number2 == "3" and number3 == "6":
        return "5", "1"

    if number1 == "6" and number2 == "3" and number3 == "7":
        return "6", "1"

    if number1 == "6" and number2 == "3" and number3 == "8":
        return "7", "1"

    if number1 == "6" and number2 == "3" and number3 == "9":
        return "8", "1"

    if number1 == "6" and number2 == "4" and number3 == "0":
        return "0", "1"

    if number1 == "6" and number2 == "4" and number3 == "1":
        return "1", "1"

    if number1 == "6" and number2 == "4" and number3 == "2":
        return "2", "1"

    if number1 == "6" and number2 == "4" and number3 == "3":
        return "3", "1"

    if number1 == "6" and number2 == "4" and number3 == "4":
        return "4", "1"

    if number1 == "6" and number2 == "4" and number3 == "5":
        return "5", "1"

    if number1 == "6" and number2 == "4" and number3 == "6":
        return "6", "1"

    if number1 == "6" and number2 == "4" and number3 == "7":
        return "7", "1"

    if number1 == "6" and number2 == "4" and number3 == "8":
        return "8", "1"

    if number1 == "6" and number2 == "4" and number3 == "9":
        return "9", "1"

    if number1 == "6" and number2 == "5" and number3 == "0":
        return "1", "1"

    if number1 == "6" and number2 == "5" and number3 == "1":
        return "2", "1"

    if number1 == "6" and number2 == "5" and number3 == "2":
        return "3", "1"

    if number1 == "6" and number2 == "5" and number3 == "3":
        return "4", "1"

    if number1 == "6" and number2 == "5" and number3 == "4":
        return "5", "1"

    if number1 == "6" and number2 == "5" and number3 == "5":
        return "6", "1"

    if number1 == "6" and number2 == "5" and number3 == "6":
        return "7", "1"

    if number1 == "6" and number2 == "5" and number3 == "7":
        return "8", "1"

    if number1 == "6" and number2 == "5" and number3 == "8":
        return "9", "1"

    if number1 == "6" and number2 == "5" and number3 == "9":
        return "0", "2"

    if number1 == "6" and number2 == "6" and number3 == "0":
        return "2", "1"

    if number1 == "6" and number2 == "6" and number3 == "1":
        return "3", "1"

    if number1 == "6" and number2 == "6" and number3 == "2":
        return "4", "1"

    if number1 == "6" and number2 == "6" and number3 == "3":
        return "5", "1"

    if number1 == "6" and number2 == "6" and number3 == "4":
        return "6", "1"

    if number1 == "6" and number2 == "6" and number3 == "5":
        return "7", "1"

    if number1 == "6" and number2 == "6" and number3 == "6":
        return "8", "1"

    if number1 == "6" and number2 == "6" and number3 == "7":
        return "9", "1"

    if number1 == "6" and number2 == "6" and number3 == "8":
        return "0", "2"

    if number1 == "6" and number2 == "6" and number3 == "9":
        return "1", "2"

    if number1 == "6" and number2 == "7" and number3 == "0":
        return "3", "1"

    if number1 == "6" and number2 == "7" and number3 == "1":
        return "4", "1"

    if number1 == "6" and number2 == "7" and number3 == "2":
        return "5", "1"

    if number1 == "6" and number2 == "7" and number3 == "3":
        return "6", "1"

    if number1 == "6" and number2 == "7" and number3 == "4":
        return "7", "1"

    if number1 == "6" and number2 == "7" and number3 == "5":
        return "8", "1"

    if number1 == "6" and number2 == "7" and number3 == "6":
        return "9", "1"

    if number1 == "6" and number2 == "7" and number3 == "7":
        return "0", "2"

    if number1 == "6" and number2 == "7" and number3 == "8":
        return "1", "2"

    if number1 == "6" and number2 == "7" and number3 == "9":
        return "2", "2"

    if number1 == "6" and number2 == "8" and number3 == "0":
        return "4", "1"

    if number1 == "6" and number2 == "8" and number3 == "1":
        return "5", "1"

    if number1 == "6" and number2 == "8" and number3 == "2":
        return "6", "1"

    if number1 == "6" and number2 == "8" and number3 == "3":
        return "7", "1"

    if number1 == "6" and number2 == "8" and number3 == "4":
        return "8", "1"

    if number1 == "6" and number2 == "8" and number3 == "5":
        return "9", "1"

    if number1 == "6" and number2 == "8" and number3 == "6":
        return "0", "2"

    if number1 == "6" and number2 == "8" and number3 == "7":
        return "1", "2"

    if number1 == "6" and number2 == "8" and number3 == "8":
        return "2", "2"

    if number1 == "6" and number2 == "8" and number3 == "9":
        return "3", "2"

    if number1 == "6" and number2 == "9" and number3 == "0":
        return "5", "1"

    if number1 == "6" and number2 == "9" and number3 == "1":
        return "6", "1"

    if number1 == "6" and number2 == "9" and number3 == "2":
        return "7", "1"

    if number1 == "6" and number2 == "9" and number3 == "3":
        return "8", "1"

    if number1 == "6" and number2 == "9" and number3 == "4":
        return "9", "1"

    if number1 == "6" and number2 == "9" and number3 == "5":
        return "0", "2"

    if number1 == "6" and number2 == "9" and number3 == "6":
        return "1", "2"

    if number1 == "6" and number2 == "9" and number3 == "7":
        return "2", "2"

    if number1 == "6" and number2 == "9" and number3 == "8":
        return "3", "2"

    if number1 == "6" and number2 == "9" and number3 == "9":
        return "4", "2"

    if number1 == "7" and number2 == "0" and number3 == "0":
        return "7", "0"

    if number1 == "7" and number2 == "0" and number3 == "1":
        return "8", "0"

    if number1 == "7" and number2 == "0" and number3 == "2":
        return "9", "0"

    if number1 == "7" and number2 == "0" and number3 == "3":
        return "0", "1"

    if number1 == "7" and number2 == "0" and number3 == "4":
        return "1", "1"

    if number1 == "7" and number2 == "0" and number3 == "5":
        return "2", "1"

    if number1 == "7" and number2 == "0" and number3 == "6":
        return "3", "1"

    if number1 == "7" and number2 == "0" and number3 == "7":
        return "4", "1"

    if number1 == "7" and number2 == "0" and number3 == "8":
        return "5", "1"

    if number1 == "7" and number2 == "0" and number3 == "9":
        return "6", "1"

    if number1 == "7" and number2 == "1" and number3 == "0":
        return "8", "0"

    if number1 == "7" and number2 == "1" and number3 == "1":
        return "9", "0"

    if number1 == "7" and number2 == "1" and number3 == "2":
        return "0", "1"

    if number1 == "7" and number2 == "1" and number3 == "3":
        return "1", "1"

    if number1 == "7" and number2 == "1" and number3 == "4":
        return "2", "1"

    if number1 == "7" and number2 == "1" and number3 == "5":
        return "3", "1"

    if number1 == "7" and number2 == "1" and number3 == "6":
        return "4", "1"

    if number1 == "7" and number2 == "1" and number3 == "7":
        return "5", "1"

    if number1 == "7" and number2 == "1" and number3 == "8":
        return "6", "1"

    if number1 == "7" and number2 == "1" and number3 == "9":
        return "7", "1"

    if number1 == "7" and number2 == "2" and number3 == "0":
        return "9", "0"

    if number1 == "7" and number2 == "2" and number3 == "1":
        return "0", "1"

    if number1 == "7" and number2 == "2" and number3 == "2":
        return "1", "1"

    if number1 == "7" and number2 == "2" and number3 == "3":
        return "2", "1"

    if number1 == "7" and number2 == "2" and number3 == "4":
        return "3", "1"

    if number1 == "7" and number2 == "2" and number3 == "5":
        return "4", "1"

    if number1 == "7" and number2 == "2" and number3 == "6":
        return "5", "1"

    if number1 == "7" and number2 == "2" and number3 == "7":
        return "6", "1"

    if number1 == "7" and number2 == "2" and number3 == "8":
        return "7", "1"

    if number1 == "7" and number2 == "2" and number3 == "9":
        return "8", "1"

    if number1 == "7" and number2 == "3" and number3 == "0":
        return "0", "1"

    if number1 == "7" and number2 == "3" and number3 == "1":
        return "1", "1"

    if number1 == "7" and number2 == "3" and number3 == "2":
        return "2", "1"

    if number1 == "7" and number2 == "3" and number3 == "3":
        return "3", "1"

    if number1 == "7" and number2 == "3" and number3 == "4":
        return "4", "1"

    if number1 == "7" and number2 == "3" and number3 == "5":
        return "5", "1"

    if number1 == "7" and number2 == "3" and number3 == "6":
        return "6", "1"

    if number1 == "7" and number2 == "3" and number3 == "7":
        return "7", "1"

    if number1 == "7" and number2 == "3" and number3 == "8":
        return "8", "1"

    if number1 == "7" and number2 == "3" and number3 == "9":
        return "9", "1"

    if number1 == "7" and number2 == "4" and number3 == "0":
        return "1", "1"

    if number1 == "7" and number2 == "4" and number3 == "1":
        return "2", "1"

    if number1 == "7" and number2 == "4" and number3 == "2":
        return "3", "1"

    if number1 == "7" and number2 == "4" and number3 == "3":
        return "4", "1"

    if number1 == "7" and number2 == "4" and number3 == "4":
        return "5", "1"

    if number1 == "7" and number2 == "4" and number3 == "5":
        return "6", "1"

    if number1 == "7" and number2 == "4" and number3 == "6":
        return "7", "1"

    if number1 == "7" and number2 == "4" and number3 == "7":
        return "8", "1"

    if number1 == "7" and number2 == "4" and number3 == "8":
        return "9", "1"

    if number1 == "7" and number2 == "4" and number3 == "9":
        return "0", "2"

    if number1 == "7" and number2 == "5" and number3 == "0":
        return "2", "1"

    if number1 == "7" and number2 == "5" and number3 == "1":
        return "3", "1"

    if number1 == "7" and number2 == "5" and number3 == "2":
        return "4", "1"

    if number1 == "7" and number2 == "5" and number3 == "3":
        return "5", "1"

    if number1 == "7" and number2 == "5" and number3 == "4":
        return "6", "1"

    if number1 == "7" and number2 == "5" and number3 == "5":
        return "7", "1"

    if number1 == "7" and number2 == "5" and number3 == "6":
        return "8", "1"

    if number1 == "7" and number2 == "5" and number3 == "7":
        return "9", "1"

    if number1 == "7" and number2 == "5" and number3 == "8":
        return "0", "2"

    if number1 == "7" and number2 == "5" and number3 == "9":
        return "1", "2"

    if number1 == "7" and number2 == "6" and number3 == "0":
        return "3", "1"

    if number1 == "7" and number2 == "6" and number3 == "1":
        return "4", "1"

    if number1 == "7" and number2 == "6" and number3 == "2":
        return "5", "1"

    if number1 == "7" and number2 == "6" and number3 == "3":
        return "6", "1"

    if number1 == "7" and number2 == "6" and number3 == "4":
        return "7", "1"

    if number1 == "7" and number2 == "6" and number3 == "5":
        return "8", "1"

    if number1 == "7" and number2 == "6" and number3 == "6":
        return "9", "1"

    if number1 == "7" and number2 == "6" and number3 == "7":
        return "0", "2"

    if number1 == "7" and number2 == "6" and number3 == "8":
        return "1", "2"

    if number1 == "7" and number2 == "6" and number3 == "9":
        return "2", "2"

    if number1 == "7" and number2 == "7" and number3 == "0":
        return "4", "1"

    if number1 == "7" and number2 == "7" and number3 == "1":
        return "5", "1"

    if number1 == "7" and number2 == "7" and number3 == "2":
        return "6", "1"

    if number1 == "7" and number2 == "7" and number3 == "3":
        return "7", "1"

    if number1 == "7" and number2 == "7" and number3 == "4":
        return "8", "1"

    if number1 == "7" and number2 == "7" and number3 == "5":
        return "9", "1"

    if number1 == "7" and number2 == "7" and number3 == "6":
        return "0", "2"

    if number1 == "7" and number2 == "7" and number3 == "7":
        return "1", "2"

    if number1 == "7" and number2 == "7" and number3 == "8":
        return "2", "2"

    if number1 == "7" and number2 == "7" and number3 == "9":
        return "3", "2"

    if number1 == "7" and number2 == "8" and number3 == "0":
        return "5", "1"

    if number1 == "7" and number2 == "8" and number3 == "1":
        return "6", "1"

    if number1 == "7" and number2 == "8" and number3 == "2":
        return "7", "1"

    if number1 == "7" and number2 == "8" and number3 == "3":
        return "8", "1"

    if number1 == "7" and number2 == "8" and number3 == "4":
        return "9", "1"

    if number1 == "7" and number2 == "8" and number3 == "5":
        return "0", "2"

    if number1 == "7" and number2 == "8" and number3 == "6":
        return "1", "2"

    if number1 == "7" and number2 == "8" and number3 == "7":
        return "2", "2"

    if number1 == "7" and number2 == "8" and number3 == "8":
        return "3", "2"

    if number1 == "7" and number2 == "8" and number3 == "9":
        return "4", "2"

    if number1 == "7" and number2 == "9" and number3 == "0":
        return "6", "1"

    if number1 == "7" and number2 == "9" and number3 == "1":
        return "7", "1"

    if number1 == "7" and number2 == "9" and number3 == "2":
        return "8", "1"

    if number1 == "7" and number2 == "9" and number3 == "3":
        return "9", "1"

    if number1 == "7" and number2 == "9" and number3 == "4":
        return "0", "2"

    if number1 == "7" and number2 == "9" and number3 == "5":
        return "1", "2"

    if number1 == "7" and number2 == "9" and number3 == "6":
        return "2", "2"

    if number1 == "7" and number2 == "9" and number3 == "7":
        return "3", "2"

    if number1 == "7" and number2 == "9" and number3 == "8":
        return "4", "2"

    if number1 == "7" and number2 == "9" and number3 == "9":
        return "5", "2"

    if number1 == "8" and number2 == "0" and number3 == "0":
        return "8", "0"

    if number1 == "8" and number2 == "0" and number3 == "1":
        return "9", "0"

    if number1 == "8" and number2 == "0" and number3 == "2":
        return "0", "1"

    if number1 == "8" and number2 == "0" and number3 == "3":
        return "1", "1"

    if number1 == "8" and number2 == "0" and number3 == "4":
        return "2", "1"

    if number1 == "8" and number2 == "0" and number3 == "5":
        return "3", "1"

    if number1 == "8" and number2 == "0" and number3 == "6":
        return "4", "1"

    if number1 == "8" and number2 == "0" and number3 == "7":
        return "5", "1"

    if number1 == "8" and number2 == "0" and number3 == "8":
        return "6", "1"

    if number1 == "8" and number2 == "0" and number3 == "9":
        return "7", "1"

    if number1 == "8" and number2 == "1" and number3 == "0":
        return "9", "0"

    if number1 == "8" and number2 == "1" and number3 == "1":
        return "0", "1"

    if number1 == "8" and number2 == "1" and number3 == "2":
        return "1", "1"

    if number1 == "8" and number2 == "1" and number3 == "3":
        return "2", "1"

    if number1 == "8" and number2 == "1" and number3 == "4":
        return "3", "1"

    if number1 == "8" and number2 == "1" and number3 == "5":
        return "4", "1"

    if number1 == "8" and number2 == "1" and number3 == "6":
        return "5", "1"

    if number1 == "8" and number2 == "1" and number3 == "7":
        return "6", "1"

    if number1 == "8" and number2 == "1" and number3 == "8":
        return "7", "1"

    if number1 == "8" and number2 == "1" and number3 == "9":
        return "8", "1"

    if number1 == "8" and number2 == "2" and number3 == "0":
        return "0", "1"

    if number1 == "8" and number2 == "2" and number3 == "1":
        return "1", "1"

    if number1 == "8" and number2 == "2" and number3 == "2":
        return "2", "1"

    if number1 == "8" and number2 == "2" and number3 == "3":
        return "3", "1"

    if number1 == "8" and number2 == "2" and number3 == "4":
        return "4", "1"

    if number1 == "8" and number2 == "2" and number3 == "5":
        return "5", "1"

    if number1 == "8" and number2 == "2" and number3 == "6":
        return "6", "1"

    if number1 == "8" and number2 == "2" and number3 == "7":
        return "7", "1"

    if number1 == "8" and number2 == "2" and number3 == "8":
        return "8", "1"

    if number1 == "8" and number2 == "2" and number3 == "9":
        return "9", "1"

    if number1 == "8" and number2 == "3" and number3 == "0":
        return "1", "1"

    if number1 == "8" and number2 == "3" and number3 == "1":
        return "2", "1"

    if number1 == "8" and number2 == "3" and number3 == "2":
        return "3", "1"

    if number1 == "8" and number2 == "3" and number3 == "3":
        return "4", "1"

    if number1 == "8" and number2 == "3" and number3 == "4":
        return "5", "1"

    if number1 == "8" and number2 == "3" and number3 == "5":
        return "6", "1"

    if number1 == "8" and number2 == "3" and number3 == "6":
        return "7", "1"

    if number1 == "8" and number2 == "3" and number3 == "7":
        return "8", "1"

    if number1 == "8" and number2 == "3" and number3 == "8":
        return "9", "1"

    if number1 == "8" and number2 == "3" and number3 == "9":
        return "0", "2"

    if number1 == "8" and number2 == "4" and number3 == "0":
        return "2", "1"

    if number1 == "8" and number2 == "4" and number3 == "1":
        return "3", "1"

    if number1 == "8" and number2 == "4" and number3 == "2":
        return "4", "1"

    if number1 == "8" and number2 == "4" and number3 == "3":
        return "5", "1"

    if number1 == "8" and number2 == "4" and number3 == "4":
        return "6", "1"

    if number1 == "8" and number2 == "4" and number3 == "5":
        return "7", "1"

    if number1 == "8" and number2 == "4" and number3 == "6":
        return "8", "1"

    if number1 == "8" and number2 == "4" and number3 == "7":
        return "9", "1"

    if number1 == "8" and number2 == "4" and number3 == "8":
        return "0", "2"

    if number1 == "8" and number2 == "4" and number3 == "9":
        return "1", "2"

    if number1 == "8" and number2 == "5" and number3 == "0":
        return "3", "1"

    if number1 == "8" and number2 == "5" and number3 == "1":
        return "4", "1"

    if number1 == "8" and number2 == "5" and number3 == "2":
        return "5", "1"

    if number1 == "8" and number2 == "5" and number3 == "3":
        return "6", "1"

    if number1 == "8" and number2 == "5" and number3 == "4":
        return "7", "1"

    if number1 == "8" and number2 == "5" and number3 == "5":
        return "8", "1"

    if number1 == "8" and number2 == "5" and number3 == "6":
        return "9", "1"

    if number1 == "8" and number2 == "5" and number3 == "7":
        return "0", "2"

    if number1 == "8" and number2 == "5" and number3 == "8":
        return "1", "2"

    if number1 == "8" and number2 == "5" and number3 == "9":
        return "2", "2"

    if number1 == "8" and number2 == "6" and number3 == "0":
        return "4", "1"

    if number1 == "8" and number2 == "6" and number3 == "1":
        return "5", "1"

    if number1 == "8" and number2 == "6" and number3 == "2":
        return "6", "1"

    if number1 == "8" and number2 == "6" and number3 == "3":
        return "7", "1"

    if number1 == "8" and number2 == "6" and number3 == "4":
        return "8", "1"

    if number1 == "8" and number2 == "6" and number3 == "5":
        return "9", "1"

    if number1 == "8" and number2 == "6" and number3 == "6":
        return "0", "2"

    if number1 == "8" and number2 == "6" and number3 == "7":
        return "1", "2"

    if number1 == "8" and number2 == "6" and number3 == "8":
        return "2", "2"

    if number1 == "8" and number2 == "6" and number3 == "9":
        return "3", "2"

    if number1 == "8" and number2 == "7" and number3 == "0":
        return "5", "1"

    if number1 == "8" and number2 == "7" and number3 == "1":
        return "6", "1"

    if number1 == "8" and number2 == "7" and number3 == "2":
        return "7", "1"

    if number1 == "8" and number2 == "7" and number3 == "3":
        return "8", "1"

    if number1 == "8" and number2 == "7" and number3 == "4":
        return "9", "1"

    if number1 == "8" and number2 == "7" and number3 == "5":
        return "0", "2"

    if number1 == "8" and number2 == "7" and number3 == "6":
        return "1", "2"

    if number1 == "8" and number2 == "7" and number3 == "7":
        return "2", "2"

    if number1 == "8" and number2 == "7" and number3 == "8":
        return "3", "2"

    if number1 == "8" and number2 == "7" and number3 == "9":
        return "4", "2"

    if number1 == "8" and number2 == "8" and number3 == "0":
        return "6", "1"

    if number1 == "8" and number2 == "8" and number3 == "1":
        return "7", "1"

    if number1 == "8" and number2 == "8" and number3 == "2":
        return "8", "1"

    if number1 == "8" and number2 == "8" and number3 == "3":
        return "9", "1"

    if number1 == "8" and number2 == "8" and number3 == "4":
        return "0", "2"

    if number1 == "8" and number2 == "8" and number3 == "5":
        return "1", "2"

    if number1 == "8" and number2 == "8" and number3 == "6":
        return "2", "2"

    if number1 == "8" and number2 == "8" and number3 == "7":
        return "3", "2"

    if number1 == "8" and number2 == "8" and number3 == "8":
        return "4", "2"

    if number1 == "8" and number2 == "8" and number3 == "9":
        return "5", "2"

    if number1 == "8" and number2 == "9" and number3 == "0":
        return "7", "1"

    if number1 == "8" and number2 == "9" and number3 == "1":
        return "8", "1"

    if number1 == "8" and number2 == "9" and number3 == "2":
        return "9", "1"

    if number1 == "8" and number2 == "9" and number3 == "3":
        return "0", "2"

    if number1 == "8" and number2 == "9" and number3 == "4":
        return "1", "2"

    if number1 == "8" and number2 == "9" and number3 == "5":
        return "2", "2"

    if number1 == "8" and number2 == "9" and number3 == "6":
        return "3", "2"

    if number1 == "8" and number2 == "9" and number3 == "7":
        return "4", "2"

    if number1 == "8" and number2 == "9" and number3 == "8":
        return "5", "2"

    if number1 == "8" and number2 == "9" and number3 == "9":
        return "6", "2"

    if number1 == "9" and number2 == "0" and number3 == "0":
        return "9", "0"

    if number1 == "9" and number2 == "0" and number3 == "1":
        return "0", "1"

    if number1 == "9" and number2 == "0" and number3 == "2":
        return "1", "1"

    if number1 == "9" and number2 == "0" and number3 == "3":
        return "2", "1"

    if number1 == "9" and number2 == "0" and number3 == "4":
        return "3", "1"

    if number1 == "9" and number2 == "0" and number3 == "5":
        return "4", "1"

    if number1 == "9" and number2 == "0" and number3 == "6":
        return "5", "1"

    if number1 == "9" and number2 == "0" and number3 == "7":
        return "6", "1"

    if number1 == "9" and number2 == "0" and number3 == "8":
        return "7", "1"

    if number1 == "9" and number2 == "0" and number3 == "9":
        return "8", "1"

    if number1 == "9" and number2 == "1" and number3 == "0":
        return "0", "1"

    if number1 == "9" and number2 == "1" and number3 == "1":
        return "1", "1"

    if number1 == "9" and number2 == "1" and number3 == "2":
        return "2", "1"

    if number1 == "9" and number2 == "1" and number3 == "3":
        return "3", "1"

    if number1 == "9" and number2 == "1" and number3 == "4":
        return "4", "1"

    if number1 == "9" and number2 == "1" and number3 == "5":
        return "5", "1"

    if number1 == "9" and number2 == "1" and number3 == "6":
        return "6", "1"

    if number1 == "9" and number2 == "1" and number3 == "7":
        return "7", "1"

    if number1 == "9" and number2 == "1" and number3 == "8":
        return "8", "1"

    if number1 == "9" and number2 == "1" and number3 == "9":
        return "9", "1"

    if number1 == "9" and number2 == "2" and number3 == "0":
        return "1", "1"

    if number1 == "9" and number2 == "2" and number3 == "1":
        return "2", "1"

    if number1 == "9" and number2 == "2" and number3 == "2":
        return "3", "1"

    if number1 == "9" and number2 == "2" and number3 == "3":
        return "4", "1"

    if number1 == "9" and number2 == "2" and number3 == "4":
        return "5", "1"

    if number1 == "9" and number2 == "2" and number3 == "5":
        return "6", "1"

    if number1 == "9" and number2 == "2" and number3 == "6":
        return "7", "1"

    if number1 == "9" and number2 == "2" and number3 == "7":
        return "8", "1"

    if number1 == "9" and number2 == "2" and number3 == "8":
        return "9", "1"

    if number1 == "9" and number2 == "2" and number3 == "9":
        return "0", "2"

    if number1 == "9" and number2 == "3" and number3 == "0":
        return "2", "1"

    if number1 == "9" and number2 == "3" and number3 == "1":
        return "3", "1"

    if number1 == "9" and number2 == "3" and number3 == "2":
        return "4", "1"

    if number1 == "9" and number2 == "3" and number3 == "3":
        return "5", "1"

    if number1 == "9" and number2 == "3" and number3 == "4":
        return "6", "1"

    if number1 == "9" and number2 == "3" and number3 == "5":
        return "7", "1"

    if number1 == "9" and number2 == "3" and number3 == "6":
        return "8", "1"

    if number1 == "9" and number2 == "3" and number3 == "7":
        return "9", "1"

    if number1 == "9" and number2 == "3" and number3 == "8":
        return "0", "2"

    if number1 == "9" and number2 == "3" and number3 == "9":
        return "1", "2"

    if number1 == "9" and number2 == "4" and number3 == "0":
        return "3", "1"

    if number1 == "9" and number2 == "4" and number3 == "1":
        return "4", "1"

    if number1 == "9" and number2 == "4" and number3 == "2":
        return "5", "1"

    if number1 == "9" and number2 == "4" and number3 == "3":
        return "6", "1"

    if number1 == "9" and number2 == "4" and number3 == "4":
        return "7", "1"

    if number1 == "9" and number2 == "4" and number3 == "5":
        return "8", "1"

    if number1 == "9" and number2 == "4" and number3 == "6":
        return "9", "1"

    if number1 == "9" and number2 == "4" and number3 == "7":
        return "0", "2"

    if number1 == "9" and number2 == "4" and number3 == "8":
        return "1", "2"

    if number1 == "9" and number2 == "4" and number3 == "9":
        return "2", "2"

    if number1 == "9" and number2 == "5" and number3 == "0":
        return "4", "1"

    if number1 == "9" and number2 == "5" and number3 == "1":
        return "5", "1"

    if number1 == "9" and number2 == "5" and number3 == "2":
        return "6", "1"

    if number1 == "9" and number2 == "5" and number3 == "3":
        return "7", "1"

    if number1 == "9" and number2 == "5" and number3 == "4":
        return "8", "1"

    if number1 == "9" and number2 == "5" and number3 == "5":
        return "9", "1"

    if number1 == "9" and number2 == "5" and number3 == "6":
        return "0", "2"

    if number1 == "9" and number2 == "5" and number3 == "7":
        return "1", "2"

    if number1 == "9" and number2 == "5" and number3 == "8":
        return "2", "2"

    if number1 == "9" and number2 == "5" and number3 == "9":
        return "3", "2"

    if number1 == "9" and number2 == "6" and number3 == "0":
        return "5", "1"

    if number1 == "9" and number2 == "6" and number3 == "1":
        return "6", "1"

    if number1 == "9" and number2 == "6" and number3 == "2":
        return "7", "1"

    if number1 == "9" and number2 == "6" and number3 == "3":
        return "8", "1"

    if number1 == "9" and number2 == "6" and number3 == "4":
        return "9", "1"

    if number1 == "9" and number2 == "6" and number3 == "5":
        return "0", "2"

    if number1 == "9" and number2 == "6" and number3 == "6":
        return "1", "2"

    if number1 == "9" and number2 == "6" and number3 == "7":
        return "2", "2"

    if number1 == "9" and number2 == "6" and number3 == "8":
        return "3", "2"

    if number1 == "9" and number2 == "6" and number3 == "9":
        return "4", "2"

    if number1 == "9" and number2 == "7" and number3 == "0":
        return "6", "1"

    if number1 == "9" and number2 == "7" and number3 == "1":
        return "7", "1"

    if number1 == "9" and number2 == "7" and number3 == "2":
        return "8", "1"

    if number1 == "9" and number2 == "7" and number3 == "3":
        return "9", "1"

    if number1 == "9" and number2 == "7" and number3 == "4":
        return "0", "2"

    if number1 == "9" and number2 == "7" and number3 == "5":
        return "1", "2"

    if number1 == "9" and number2 == "7" and number3 == "6":
        return "2", "2"

    if number1 == "9" and number2 == "7" and number3 == "7":
        return "3", "2"

    if number1 == "9" and number2 == "7" and number3 == "8":
        return "4", "2"

    if number1 == "9" and number2 == "7" and number3 == "9":
        return "5", "2"

    if number1 == "9" and number2 == "8" and number3 == "0":
        return "7", "1"

    if number1 == "9" and number2 == "8" and number3 == "1":
        return "8", "1"

    if number1 == "9" and number2 == "8" and number3 == "2":
        return "9", "1"

    if number1 == "9" and number2 == "8" and number3 == "3":
        return "0", "2"

    if number1 == "9" and number2 == "8" and number3 == "4":
        return "1", "2"

    if number1 == "9" and number2 == "8" and number3 == "5":
        return "2", "2"

    if number1 == "9" and number2 == "8" and number3 == "6":
        return "3", "2"

    if number1 == "9" and number2 == "8" and number3 == "7":
        return "4", "2"

    if number1 == "9" and number2 == "8" and number3 == "8":
        return "5", "2"

    if number1 == "9" and number2 == "8" and number3 == "9":
        return "6", "2"

    if number1 == "9" and number2 == "9" and number3 == "0":
        return "8", "1"

    if number1 == "9" and number2 == "9" and number3 == "1":
        return "9", "1"

    if number1 == "9" and number2 == "9" and number3 == "2":
        return "0", "2"

    if number1 == "9" and number2 == "9" and number3 == "3":
        return "1", "2"

    if number1 == "9" and number2 == "9" and number3 == "4":
        return "2", "2"

    if number1 == "9" and number2 == "9" and number3 == "5":
        return "3", "2"

    if number1 == "9" and number2 == "9" and number3 == "6":
        return "4", "2"

    if number1 == "9" and number2 == "9" and number3 == "7":
        return "5", "2"

    if number1 == "9" and number2 == "9" and number3 == "8":
        return "6", "2"

    if number1 == "9" and number2 == "9" and number3 == "9":
        return "7", "2"


def SUB_N_N(number1: str, number2: str):

    number1 = str(number1)
    number2 = str(number2)

    if number1 == "0" and number2 == "0":
        return "0"

    if number1 == "0" and number2 == "1":
        return "-1"

    if number1 == "0" and number2 == "2":
        return "-2"

    if number1 == "0" and number2 == "3":
        return "-3"

    if number1 == "0" and number2 == "4":
        return "-4"

    if number1 == "0" and number2 == "5":
        return "-5"

    if number1 == "0" and number2 == "6":
        return "-6"

    if number1 == "0" and number2 == "7":
        return "-7"

    if number1 == "0" and number2 == "8":
        return "-8"

    if number1 == "0" and number2 == "9":
        return "-9"

    if number1 == "1" and number2 == "0":
        return "1"

    if number1 == "1" and number2 == "1":
        return "0"

    if number1 == "1" and number2 == "2":
        return "-1"

    if number1 == "1" and number2 == "3":
        return "-2"

    if number1 == "1" and number2 == "4":
        return "-3"

    if number1 == "1" and number2 == "5":
        return "-4"

    if number1 == "1" and number2 == "6":
        return "-5"

    if number1 == "1" and number2 == "7":
        return "-6"

    if number1 == "1" and number2 == "8":
        return "-7"

    if number1 == "1" and number2 == "9":
        return "-8"

    if number1 == "2" and number2 == "0":
        return "2"

    if number1 == "2" and number2 == "1":
        return "1"

    if number1 == "2" and number2 == "2":
        return "0"

    if number1 == "2" and number2 == "3":
        return "-1"

    if number1 == "2" and number2 == "4":
        return "-2"

    if number1 == "2" and number2 == "5":
        return "-3"

    if number1 == "2" and number2 == "6":
        return "-4"

    if number1 == "2" and number2 == "7":
        return "-5"

    if number1 == "2" and number2 == "8":
        return "-6"

    if number1 == "2" and number2 == "9":
        return "-7"

    if number1 == "3" and number2 == "0":
        return "3"

    if number1 == "3" and number2 == "1":
        return "2"

    if number1 == "3" and number2 == "2":
        return "1"

    if number1 == "3" and number2 == "3":
        return "0"

    if number1 == "3" and number2 == "4":
        return "-1"

    if number1 == "3" and number2 == "5":
        return "-2"

    if number1 == "3" and number2 == "6":
        return "-3"

    if number1 == "3" and number2 == "7":
        return "-4"

    if number1 == "3" and number2 == "8":
        return "-5"

    if number1 == "3" and number2 == "9":
        return "-6"

    if number1 == "4" and number2 == "0":
        return "4"

    if number1 == "4" and number2 == "1":
        return "3"

    if number1 == "4" and number2 == "2":
        return "2"

    if number1 == "4" and number2 == "3":
        return "1"

    if number1 == "4" and number2 == "4":
        return "0"

    if number1 == "4" and number2 == "5":
        return "-1"

    if number1 == "4" and number2 == "6":
        return "-2"

    if number1 == "4" and number2 == "7":
        return "-3"

    if number1 == "4" and number2 == "8":
        return "-4"

    if number1 == "4" and number2 == "9":
        return "-5"

    if number1 == "5" and number2 == "0":
        return "5"

    if number1 == "5" and number2 == "1":
        return "4"

    if number1 == "5" and number2 == "2":
        return "3"

    if number1 == "5" and number2 == "3":
        return "2"

    if number1 == "5" and number2 == "4":
        return "1"

    if number1 == "5" and number2 == "5":
        return "0"

    if number1 == "5" and number2 == "6":
        return "-1"

    if number1 == "5" and number2 == "7":
        return "-2"

    if number1 == "5" and number2 == "8":
        return "-3"

    if number1 == "5" and number2 == "9":
        return "-4"

    if number1 == "6" and number2 == "0":
        return "6"

    if number1 == "6" and number2 == "1":
        return "5"

    if number1 == "6" and number2 == "2":
        return "4"

    if number1 == "6" and number2 == "3":
        return "3"

    if number1 == "6" and number2 == "4":
        return "2"

    if number1 == "6" and number2 == "5":
        return "1"

    if number1 == "6" and number2 == "6":
        return "0"

    if number1 == "6" and number2 == "7":
        return "-1"

    if number1 == "6" and number2 == "8":
        return "-2"

    if number1 == "6" and number2 == "9":
        return "-3"

    if number1 == "7" and number2 == "0":
        return "7"

    if number1 == "7" and number2 == "1":
        return "6"

    if number1 == "7" and number2 == "2":
        return "5"

    if number1 == "7" and number2 == "3":
        return "4"

    if number1 == "7" and number2 == "4":
        return "3"

    if number1 == "7" and number2 == "5":
        return "2"

    if number1 == "7" and number2 == "6":
        return "1"

    if number1 == "7" and number2 == "7":
        return "0"

    if number1 == "7" and number2 == "8":
        return "-1"

    if number1 == "7" and number2 == "9":
        return "-2"

    if number1 == "8" and number2 == "0":
        return "8"

    if number1 == "8" and number2 == "1":
        return "7"

    if number1 == "8" and number2 == "2":
        return "6"

    if number1 == "8" and number2 == "3":
        return "5"

    if number1 == "8" and number2 == "4":
        return "4"

    if number1 == "8" and number2 == "5":
        return "3"

    if number1 == "8" and number2 == "6":
        return "2"

    if number1 == "8" and number2 == "7":
        return "1"

    if number1 == "8" and number2 == "8":
        return "0"

    if number1 == "8" and number2 == "9":
        return "-1"

    if number1 == "9" and number2 == "0":
        return "9"

    if number1 == "9" and number2 == "1":
        return "8"

    if number1 == "9" and number2 == "2":
        return "7"

    if number1 == "9" and number2 == "3":
        return "6"

    if number1 == "9" and number2 == "4":
        return "5"

    if number1 == "9" and number2 == "5":
        return "4"

    if number1 == "9" and number2 == "6":
        return "3"

    if number1 == "9" and number2 == "7":
        return "2"

    if number1 == "9" and number2 == "8":
        return "1"

    if number1 == "9" and number2 == "9":
        return "0"

    if number1 == "10" and number2 == "0":
        return "10"

    if number1 == "10" and number2 == "1":
        return "9"

    if number1 == "10" and number2 == "2":
        return "8"

    if number1 == "10" and number2 == "3":
        return "7"

    if number1 == "10" and number2 == "4":
        return "6"

    if number1 == "10" and number2 == "5":
        return "5"

    if number1 == "10" and number2 == "6":
        return "4"

    if number1 == "10" and number2 == "7":
        return "3"

    if number1 == "10" and number2 == "8":
        return "2"

    if number1 == "10" and number2 == "9":
        return "1"

    if number1 == "11" and number2 == "0":
        return "11"

    if number1 == "11" and number2 == "1":
        return "10"

    if number1 == "11" and number2 == "2":
        return "9"

    if number1 == "11" and number2 == "3":
        return "8"

    if number1 == "11" and number2 == "4":
        return "7"

    if number1 == "11" and number2 == "5":
        return "6"

    if number1 == "11" and number2 == "6":
        return "5"

    if number1 == "11" and number2 == "7":
        return "4"

    if number1 == "11" and number2 == "8":
        return "3"

    if number1 == "11" and number2 == "9":
        return "2"

    if number1 == "12" and number2 == "0":
        return "12"

    if number1 == "12" and number2 == "1":
        return "11"

    if number1 == "12" and number2 == "2":
        return "10"

    if number1 == "12" and number2 == "3":
        return "9"

    if number1 == "12" and number2 == "4":
        return "8"

    if number1 == "12" and number2 == "5":
        return "7"

    if number1 == "12" and number2 == "6":
        return "6"

    if number1 == "12" and number2 == "7":
        return "5"

    if number1 == "12" and number2 == "8":
        return "4"

    if number1 == "12" and number2 == "9":
        return "3"

    if number1 == "13" and number2 == "0":
        return "13"

    if number1 == "13" and number2 == "1":
        return "12"

    if number1 == "13" and number2 == "2":
        return "11"

    if number1 == "13" and number2 == "3":
        return "10"

    if number1 == "13" and number2 == "4":
        return "9"

    if number1 == "13" and number2 == "5":
        return "8"

    if number1 == "13" and number2 == "6":
        return "7"

    if number1 == "13" and number2 == "7":
        return "6"

    if number1 == "13" and number2 == "8":
        return "5"

    if number1 == "13" and number2 == "9":
        return "4"

    if number1 == "14" and number2 == "0":
        return "14"

    if number1 == "14" and number2 == "1":
        return "13"

    if number1 == "14" and number2 == "2":
        return "12"

    if number1 == "14" and number2 == "3":
        return "11"

    if number1 == "14" and number2 == "4":
        return "10"

    if number1 == "14" and number2 == "5":
        return "9"

    if number1 == "14" and number2 == "6":
        return "8"

    if number1 == "14" and number2 == "7":
        return "7"

    if number1 == "14" and number2 == "8":
        return "6"

    if number1 == "14" and number2 == "9":
        return "5"

    if number1 == "15" and number2 == "0":
        return "15"

    if number1 == "15" and number2 == "1":
        return "14"

    if number1 == "15" and number2 == "2":
        return "13"

    if number1 == "15" and number2 == "3":
        return "12"

    if number1 == "15" and number2 == "4":
        return "11"

    if number1 == "15" and number2 == "5":
        return "10"

    if number1 == "15" and number2 == "6":
        return "9"

    if number1 == "15" and number2 == "7":
        return "8"

    if number1 == "15" and number2 == "8":
        return "7"

    if number1 == "15" and number2 == "9":
        return "6"

    if number1 == "16" and number2 == "0":
        return "16"

    if number1 == "16" and number2 == "1":
        return "15"

    if number1 == "16" and number2 == "2":
        return "14"

    if number1 == "16" and number2 == "3":
        return "13"

    if number1 == "16" and number2 == "4":
        return "12"

    if number1 == "16" and number2 == "5":
        return "11"

    if number1 == "16" and number2 == "6":
        return "10"

    if number1 == "16" and number2 == "7":
        return "9"

    if number1 == "16" and number2 == "8":
        return "8"

    if number1 == "16" and number2 == "9":
        return "7"

    if number1 == "17" and number2 == "0":
        return "17"

    if number1 == "17" and number2 == "1":
        return "16"

    if number1 == "17" and number2 == "2":
        return "15"

    if number1 == "17" and number2 == "3":
        return "14"

    if number1 == "17" and number2 == "4":
        return "13"

    if number1 == "17" and number2 == "5":
        return "12"

    if number1 == "17" and number2 == "6":
        return "11"

    if number1 == "17" and number2 == "7":
        return "10"

    if number1 == "17" and number2 == "8":
        return "9"

    if number1 == "17" and number2 == "9":
        return "8"

    if number1 == "18" and number2 == "0":
        return "18"

    if number1 == "18" and number2 == "1":
        return "17"

    if number1 == "18" and number2 == "2":
        return "16"

    if number1 == "18" and number2 == "3":
        return "15"

    if number1 == "18" and number2 == "4":
        return "14"

    if number1 == "18" and number2 == "5":
        return "13"

    if number1 == "18" and number2 == "6":
        return "12"

    if number1 == "18" and number2 == "7":
        return "11"

    if number1 == "18" and number2 == "8":
        return "10"

    if number1 == "18" and number2 == "9":
        return "9"


def ADD_N_N_bez_ost(number1: str, number2: str):
    number1 = str(number1)
    number2 = str(number2)

    if number1 == "-1" and number2 == "0":
        return "-1"

    if number1 == "-1" and number2 == "1":
        return "0"

    if number1 == "-1" and number2 == "2":
        return "1"

    if number1 == "-1" and number2 == "3":
        return "2"

    if number1 == "-1" and number2 == "4":
        return "3"

    if number1 == "-1" and number2 == "5":
        return "4"

    if number1 == "-1" and number2 == "6":
        return "5"

    if number1 == "-1" and number2 == "7":
        return "6"

    if number1 == "-1" and number2 == "8":
        return "7"

    if number1 == "-1" and number2 == "9":
        return "8"

    if number1 == "-1" and number2 == "10":
        return "9"

    if number1 == "-1" and number2 == "11":
        return "10"

    if number1 == "-1" and number2 == "12":
        return "11"

    if number1 == "-1" and number2 == "13":
        return "12"

    if number1 == "-1" and number2 == "14":
        return "13"

    if number1 == "-1" and number2 == "15":
        return "14"

    if number1 == "-1" and number2 == "16":
        return "15"

    if number1 == "-1" and number2 == "17":
        return "16"

    if number1 == "-1" and number2 == "18":
        return "17"

    if number1 == "-1" and number2 == "19":
        return "18"

    if number1 == "0" and number2 == "0":
        return "0"

    if number1 == "0" and number2 == "1":
        return "1"

    if number1 == "0" and number2 == "2":
        return "2"

    if number1 == "0" and number2 == "3":
        return "3"

    if number1 == "0" and number2 == "4":
        return "4"

    if number1 == "0" and number2 == "5":
        return "5"

    if number1 == "0" and number2 == "6":
        return "6"

    if number1 == "0" and number2 == "7":
        return "7"

    if number1 == "0" and number2 == "8":
        return "8"

    if number1 == "0" and number2 == "9":
        return "9"

    if number1 == "0" and number2 == "10":
        return "10"

    if number1 == "0" and number2 == "11":
        return "11"

    if number1 == "0" and number2 == "12":
        return "12"

    if number1 == "0" and number2 == "13":
        return "13"

    if number1 == "0" and number2 == "14":
        return "14"

    if number1 == "0" and number2 == "15":
        return "15"

    if number1 == "0" and number2 == "16":
        return "16"

    if number1 == "0" and number2 == "17":
        return "17"

    if number1 == "0" and number2 == "18":
        return "18"

    if number1 == "0" and number2 == "19":
        return "19"

    if number1 == "1" and number2 == "0":
        return "1"

    if number1 == "1" and number2 == "1":
        return "2"

    if number1 == "1" and number2 == "2":
        return "3"

    if number1 == "1" and number2 == "3":
        return "4"

    if number1 == "1" and number2 == "4":
        return "5"

    if number1 == "1" and number2 == "5":
        return "6"

    if number1 == "1" and number2 == "6":
        return "7"

    if number1 == "1" and number2 == "7":
        return "8"

    if number1 == "1" and number2 == "8":
        return "9"

    if number1 == "1" and number2 == "9":
        return "10"

    if number1 == "1" and number2 == "10":
        return "11"

    if number1 == "1" and number2 == "11":
        return "12"

    if number1 == "1" and number2 == "12":
        return "13"

    if number1 == "1" and number2 == "13":
        return "14"

    if number1 == "1" and number2 == "14":
        return "15"

    if number1 == "1" and number2 == "15":
        return "16"

    if number1 == "1" and number2 == "16":
        return "17"

    if number1 == "1" and number2 == "17":
        return "18"

    if number1 == "1" and number2 == "18":
        return "19"

    if number1 == "1" and number2 == "19":
        return "20"

    if number1 == "2" and number2 == "0":
        return "2"

    if number1 == "2" and number2 == "1":
        return "3"

    if number1 == "2" and number2 == "2":
        return "4"

    if number1 == "2" and number2 == "3":
        return "5"

    if number1 == "2" and number2 == "4":
        return "6"

    if number1 == "2" and number2 == "5":
        return "7"

    if number1 == "2" and number2 == "6":
        return "8"

    if number1 == "2" and number2 == "7":
        return "9"

    if number1 == "2" and number2 == "8":
        return "10"

    if number1 == "2" and number2 == "9":
        return "11"

    if number1 == "2" and number2 == "10":
        return "12"

    if number1 == "2" and number2 == "11":
        return "13"

    if number1 == "2" and number2 == "12":
        return "14"

    if number1 == "2" and number2 == "13":
        return "15"

    if number1 == "2" and number2 == "14":
        return "16"

    if number1 == "2" and number2 == "15":
        return "17"

    if number1 == "2" and number2 == "16":
        return "18"

    if number1 == "2" and number2 == "17":
        return "19"

    if number1 == "2" and number2 == "18":
        return "20"

    if number1 == "2" and number2 == "19":
        return "21"

    if number1 == "3" and number2 == "0":
        return "3"

    if number1 == "3" and number2 == "1":
        return "4"

    if number1 == "3" and number2 == "2":
        return "5"

    if number1 == "3" and number2 == "3":
        return "6"

    if number1 == "3" and number2 == "4":
        return "7"

    if number1 == "3" and number2 == "5":
        return "8"

    if number1 == "3" and number2 == "6":
        return "9"

    if number1 == "3" and number2 == "7":
        return "10"

    if number1 == "3" and number2 == "8":
        return "11"

    if number1 == "3" and number2 == "9":
        return "12"

    if number1 == "3" and number2 == "10":
        return "13"

    if number1 == "3" and number2 == "11":
        return "14"

    if number1 == "3" and number2 == "12":
        return "15"

    if number1 == "3" and number2 == "13":
        return "16"

    if number1 == "3" and number2 == "14":
        return "17"

    if number1 == "3" and number2 == "15":
        return "18"

    if number1 == "3" and number2 == "16":
        return "19"

    if number1 == "3" and number2 == "17":
        return "20"

    if number1 == "3" and number2 == "18":
        return "21"

    if number1 == "3" and number2 == "19":
        return "22"

    if number1 == "4" and number2 == "0":
        return "4"

    if number1 == "4" and number2 == "1":
        return "5"

    if number1 == "4" and number2 == "2":
        return "6"

    if number1 == "4" and number2 == "3":
        return "7"

    if number1 == "4" and number2 == "4":
        return "8"

    if number1 == "4" and number2 == "5":
        return "9"

    if number1 == "4" and number2 == "6":
        return "10"

    if number1 == "4" and number2 == "7":
        return "11"

    if number1 == "4" and number2 == "8":
        return "12"

    if number1 == "4" and number2 == "9":
        return "13"

    if number1 == "4" and number2 == "10":
        return "14"

    if number1 == "4" and number2 == "11":
        return "15"

    if number1 == "4" and number2 == "12":
        return "16"

    if number1 == "4" and number2 == "13":
        return "17"

    if number1 == "4" and number2 == "14":
        return "18"

    if number1 == "4" and number2 == "15":
        return "19"

    if number1 == "4" and number2 == "16":
        return "20"

    if number1 == "4" and number2 == "17":
        return "21"

    if number1 == "4" and number2 == "18":
        return "22"

    if number1 == "4" and number2 == "19":
        return "23"

    if number1 == "5" and number2 == "0":
        return "5"

    if number1 == "5" and number2 == "1":
        return "6"

    if number1 == "5" and number2 == "2":
        return "7"

    if number1 == "5" and number2 == "3":
        return "8"

    if number1 == "5" and number2 == "4":
        return "9"

    if number1 == "5" and number2 == "5":
        return "10"

    if number1 == "5" and number2 == "6":
        return "11"

    if number1 == "5" and number2 == "7":
        return "12"

    if number1 == "5" and number2 == "8":
        return "13"

    if number1 == "5" and number2 == "9":
        return "14"

    if number1 == "5" and number2 == "10":
        return "15"

    if number1 == "5" and number2 == "11":
        return "16"

    if number1 == "5" and number2 == "12":
        return "17"

    if number1 == "5" and number2 == "13":
        return "18"

    if number1 == "5" and number2 == "14":
        return "19"

    if number1 == "5" and number2 == "15":
        return "20"

    if number1 == "5" and number2 == "16":
        return "21"

    if number1 == "5" and number2 == "17":
        return "22"

    if number1 == "5" and number2 == "18":
        return "23"

    if number1 == "5" and number2 == "19":
        return "24"

    if number1 == "6" and number2 == "0":
        return "6"

    if number1 == "6" and number2 == "1":
        return "7"

    if number1 == "6" and number2 == "2":
        return "8"

    if number1 == "6" and number2 == "3":
        return "9"

    if number1 == "6" and number2 == "4":
        return "10"

    if number1 == "6" and number2 == "5":
        return "11"

    if number1 == "6" and number2 == "6":
        return "12"

    if number1 == "6" and number2 == "7":
        return "13"

    if number1 == "6" and number2 == "8":
        return "14"

    if number1 == "6" and number2 == "9":
        return "15"

    if number1 == "6" and number2 == "10":
        return "16"

    if number1 == "6" and number2 == "11":
        return "17"

    if number1 == "6" and number2 == "12":
        return "18"

    if number1 == "6" and number2 == "13":
        return "19"

    if number1 == "6" and number2 == "14":
        return "20"

    if number1 == "6" and number2 == "15":
        return "21"

    if number1 == "6" and number2 == "16":
        return "22"

    if number1 == "6" and number2 == "17":
        return "23"

    if number1 == "6" and number2 == "18":
        return "24"

    if number1 == "6" and number2 == "19":
        return "25"

    if number1 == "7" and number2 == "0":
        return "7"

    if number1 == "7" and number2 == "1":
        return "8"

    if number1 == "7" and number2 == "2":
        return "9"

    if number1 == "7" and number2 == "3":
        return "10"

    if number1 == "7" and number2 == "4":
        return "11"

    if number1 == "7" and number2 == "5":
        return "12"

    if number1 == "7" and number2 == "6":
        return "13"

    if number1 == "7" and number2 == "7":
        return "14"

    if number1 == "7" and number2 == "8":
        return "15"

    if number1 == "7" and number2 == "9":
        return "16"

    if number1 == "7" and number2 == "10":
        return "17"

    if number1 == "7" and number2 == "11":
        return "18"

    if number1 == "7" and number2 == "12":
        return "19"

    if number1 == "7" and number2 == "13":
        return "20"

    if number1 == "7" and number2 == "14":
        return "21"

    if number1 == "7" and number2 == "15":
        return "22"

    if number1 == "7" and number2 == "16":
        return "23"

    if number1 == "7" and number2 == "17":
        return "24"

    if number1 == "7" and number2 == "18":
        return "25"

    if number1 == "7" and number2 == "19":
        return "26"

    if number1 == "8" and number2 == "0":
        return "8"

    if number1 == "8" and number2 == "1":
        return "9"

    if number1 == "8" and number2 == "2":
        return "10"

    if number1 == "8" and number2 == "3":
        return "11"

    if number1 == "8" and number2 == "4":
        return "12"

    if number1 == "8" and number2 == "5":
        return "13"

    if number1 == "8" and number2 == "6":
        return "14"

    if number1 == "8" and number2 == "7":
        return "15"

    if number1 == "8" and number2 == "8":
        return "16"

    if number1 == "8" and number2 == "9":
        return "17"

    if number1 == "8" and number2 == "10":
        return "18"

    if number1 == "8" and number2 == "11":
        return "19"

    if number1 == "8" and number2 == "12":
        return "20"

    if number1 == "8" and number2 == "13":
        return "21"

    if number1 == "8" and number2 == "14":
        return "22"

    if number1 == "8" and number2 == "15":
        return "23"

    if number1 == "8" and number2 == "16":
        return "24"

    if number1 == "8" and number2 == "17":
        return "25"

    if number1 == "8" and number2 == "18":
        return "26"

    if number1 == "8" and number2 == "19":
        return "27"

    if number1 == "9" and number2 == "0":
        return "9"

    if number1 == "9" and number2 == "1":
        return "10"

    if number1 == "9" and number2 == "2":
        return "11"

    if number1 == "9" and number2 == "3":
        return "12"

    if number1 == "9" and number2 == "4":
        return "13"

    if number1 == "9" and number2 == "5":
        return "14"

    if number1 == "9" and number2 == "6":
        return "15"

    if number1 == "9" and number2 == "7":
        return "16"

    if number1 == "9" and number2 == "8":
        return "17"

    if number1 == "9" and number2 == "9":
        return "18"

    if number1 == "9" and number2 == "10":
        return "19"

    if number1 == "9" and number2 == "11":
        return "20"

    if number1 == "9" and number2 == "12":
        return "21"

    if number1 == "9" and number2 == "13":
        return "22"

    if number1 == "9" and number2 == "14":
        return "23"

    if number1 == "9" and number2 == "15":
        return "24"

    if number1 == "9" and number2 == "16":
        return "25"

    if number1 == "9" and number2 == "17":
        return "26"

    if number1 == "9" and number2 == "18":
        return "27"

    if number1 == "9" and number2 == "19":
        return "28"

    if number1 == "10" and number2 == "0":
        return "10"

    if number1 == "10" and number2 == "1":
        return "11"

    if number1 == "10" and number2 == "2":
        return "12"

    if number1 == "10" and number2 == "3":
        return "13"

    if number1 == "10" and number2 == "4":
        return "14"

    if number1 == "10" and number2 == "5":
        return "15"

    if number1 == "10" and number2 == "6":
        return "16"

    if number1 == "10" and number2 == "7":
        return "17"

    if number1 == "10" and number2 == "8":
        return "18"

    if number1 == "10" and number2 == "9":
        return "19"

    if number1 == "10" and number2 == "10":
        return "20"

    if number1 == "10" and number2 == "11":
        return "21"

    if number1 == "10" and number2 == "12":
        return "22"

    if number1 == "10" and number2 == "13":
        return "23"

    if number1 == "10" and number2 == "14":
        return "24"

    if number1 == "10" and number2 == "15":
        return "25"

    if number1 == "10" and number2 == "16":
        return "26"

    if number1 == "10" and number2 == "17":
        return "27"

    if number1 == "10" and number2 == "18":
        return "28"

    if number1 == "10" and number2 == "19":
        return "29"

    if number1 == "11" and number2 == "0":
        return "11"

    if number1 == "11" and number2 == "1":
        return "12"

    if number1 == "11" and number2 == "2":
        return "13"

    if number1 == "11" and number2 == "3":
        return "14"

    if number1 == "11" and number2 == "4":
        return "15"

    if number1 == "11" and number2 == "5":
        return "16"

    if number1 == "11" and number2 == "6":
        return "17"

    if number1 == "11" and number2 == "7":
        return "18"

    if number1 == "11" and number2 == "8":
        return "19"

    if number1 == "11" and number2 == "9":
        return "20"

    if number1 == "11" and number2 == "10":
        return "21"

    if number1 == "11" and number2 == "11":
        return "22"

    if number1 == "11" and number2 == "12":
        return "23"

    if number1 == "11" and number2 == "13":
        return "24"

    if number1 == "11" and number2 == "14":
        return "25"

    if number1 == "11" and number2 == "15":
        return "26"

    if number1 == "11" and number2 == "16":
        return "27"

    if number1 == "11" and number2 == "17":
        return "28"

    if number1 == "11" and number2 == "18":
        return "29"

    if number1 == "11" and number2 == "19":
        return "30"

    if number1 == "12" and number2 == "0":
        return "12"

    if number1 == "12" and number2 == "1":
        return "13"

    if number1 == "12" and number2 == "2":
        return "14"

    if number1 == "12" and number2 == "3":
        return "15"

    if number1 == "12" and number2 == "4":
        return "16"

    if number1 == "12" and number2 == "5":
        return "17"

    if number1 == "12" and number2 == "6":
        return "18"

    if number1 == "12" and number2 == "7":
        return "19"

    if number1 == "12" and number2 == "8":
        return "20"

    if number1 == "12" and number2 == "9":
        return "21"

    if number1 == "12" and number2 == "10":
        return "22"

    if number1 == "12" and number2 == "11":
        return "23"

    if number1 == "12" and number2 == "12":
        return "24"

    if number1 == "12" and number2 == "13":
        return "25"

    if number1 == "12" and number2 == "14":
        return "26"

    if number1 == "12" and number2 == "15":
        return "27"

    if number1 == "12" and number2 == "16":
        return "28"

    if number1 == "12" and number2 == "17":
        return "29"

    if number1 == "12" and number2 == "18":
        return "30"

    if number1 == "12" and number2 == "19":
        return "31"

    if number1 == "13" and number2 == "0":
        return "13"

    if number1 == "13" and number2 == "1":
        return "14"

    if number1 == "13" and number2 == "2":
        return "15"

    if number1 == "13" and number2 == "3":
        return "16"

    if number1 == "13" and number2 == "4":
        return "17"

    if number1 == "13" and number2 == "5":
        return "18"

    if number1 == "13" and number2 == "6":
        return "19"

    if number1 == "13" and number2 == "7":
        return "20"

    if number1 == "13" and number2 == "8":
        return "21"

    if number1 == "13" and number2 == "9":
        return "22"

    if number1 == "13" and number2 == "10":
        return "23"

    if number1 == "13" and number2 == "11":
        return "24"

    if number1 == "13" and number2 == "12":
        return "25"

    if number1 == "13" and number2 == "13":
        return "26"

    if number1 == "13" and number2 == "14":
        return "27"

    if number1 == "13" and number2 == "15":
        return "28"

    if number1 == "13" and number2 == "16":
        return "29"

    if number1 == "13" and number2 == "17":
        return "30"

    if number1 == "13" and number2 == "18":
        return "31"

    if number1 == "13" and number2 == "19":
        return "32"

    if number1 == "14" and number2 == "0":
        return "14"

    if number1 == "14" and number2 == "1":
        return "15"

    if number1 == "14" and number2 == "2":
        return "16"

    if number1 == "14" and number2 == "3":
        return "17"

    if number1 == "14" and number2 == "4":
        return "18"

    if number1 == "14" and number2 == "5":
        return "19"

    if number1 == "14" and number2 == "6":
        return "20"

    if number1 == "14" and number2 == "7":
        return "21"

    if number1 == "14" and number2 == "8":
        return "22"

    if number1 == "14" and number2 == "9":
        return "23"

    if number1 == "14" and number2 == "10":
        return "24"

    if number1 == "14" and number2 == "11":
        return "25"

    if number1 == "14" and number2 == "12":
        return "26"

    if number1 == "14" and number2 == "13":
        return "27"

    if number1 == "14" and number2 == "14":
        return "28"

    if number1 == "14" and number2 == "15":
        return "29"

    if number1 == "14" and number2 == "16":
        return "30"

    if number1 == "14" and number2 == "17":
        return "31"

    if number1 == "14" and number2 == "18":
        return "32"

    if number1 == "14" and number2 == "19":
        return "33"

    if number1 == "15" and number2 == "0":
        return "15"

    if number1 == "15" and number2 == "1":
        return "16"

    if number1 == "15" and number2 == "2":
        return "17"

    if number1 == "15" and number2 == "3":
        return "18"

    if number1 == "15" and number2 == "4":
        return "19"

    if number1 == "15" and number2 == "5":
        return "20"

    if number1 == "15" and number2 == "6":
        return "21"

    if number1 == "15" and number2 == "7":
        return "22"

    if number1 == "15" and number2 == "8":
        return "23"

    if number1 == "15" and number2 == "9":
        return "24"

    if number1 == "15" and number2 == "10":
        return "25"

    if number1 == "15" and number2 == "11":
        return "26"

    if number1 == "15" and number2 == "12":
        return "27"

    if number1 == "15" and number2 == "13":
        return "28"

    if number1 == "15" and number2 == "14":
        return "29"

    if number1 == "15" and number2 == "15":
        return "30"

    if number1 == "15" and number2 == "16":
        return "31"

    if number1 == "15" and number2 == "17":
        return "32"

    if number1 == "15" and number2 == "18":
        return "33"

    if number1 == "15" and number2 == "19":
        return "34"

    if number1 == "16" and number2 == "0":
        return "16"

    if number1 == "16" and number2 == "1":
        return "17"

    if number1 == "16" and number2 == "2":
        return "18"

    if number1 == "16" and number2 == "3":
        return "19"

    if number1 == "16" and number2 == "4":
        return "20"

    if number1 == "16" and number2 == "5":
        return "21"

    if number1 == "16" and number2 == "6":
        return "22"

    if number1 == "16" and number2 == "7":
        return "23"

    if number1 == "16" and number2 == "8":
        return "24"

    if number1 == "16" and number2 == "9":
        return "25"

    if number1 == "16" and number2 == "10":
        return "26"

    if number1 == "16" and number2 == "11":
        return "27"

    if number1 == "16" and number2 == "12":
        return "28"

    if number1 == "16" and number2 == "13":
        return "29"

    if number1 == "16" and number2 == "14":
        return "30"

    if number1 == "16" and number2 == "15":
        return "31"

    if number1 == "16" and number2 == "16":
        return "32"

    if number1 == "16" and number2 == "17":
        return "33"

    if number1 == "16" and number2 == "18":
        return "34"

    if number1 == "16" and number2 == "19":
        return "35"

    if number1 == "17" and number2 == "0":
        return "17"

    if number1 == "17" and number2 == "1":
        return "18"

    if number1 == "17" and number2 == "2":
        return "19"

    if number1 == "17" and number2 == "3":
        return "20"

    if number1 == "17" and number2 == "4":
        return "21"

    if number1 == "17" and number2 == "5":
        return "22"

    if number1 == "17" and number2 == "6":
        return "23"

    if number1 == "17" and number2 == "7":
        return "24"

    if number1 == "17" and number2 == "8":
        return "25"

    if number1 == "17" and number2 == "9":
        return "26"

    if number1 == "17" and number2 == "10":
        return "27"

    if number1 == "17" and number2 == "11":
        return "28"

    if number1 == "17" and number2 == "12":
        return "29"

    if number1 == "17" and number2 == "13":
        return "30"

    if number1 == "17" and number2 == "14":
        return "31"

    if number1 == "17" and number2 == "15":
        return "32"

    if number1 == "17" and number2 == "16":
        return "33"

    if number1 == "17" and number2 == "17":
        return "34"

    if number1 == "17" and number2 == "18":
        return "35"

    if number1 == "17" and number2 == "19":
        return "36"

    if number1 == "18" and number2 == "0":
        return "18"

    if number1 == "18" and number2 == "1":
        return "19"

    if number1 == "18" and number2 == "2":
        return "20"

    if number1 == "18" and number2 == "3":
        return "21"

    if number1 == "18" and number2 == "4":
        return "22"

    if number1 == "18" and number2 == "5":
        return "23"

    if number1 == "18" and number2 == "6":
        return "24"

    if number1 == "18" and number2 == "7":
        return "25"

    if number1 == "18" and number2 == "8":
        return "26"

    if number1 == "18" and number2 == "9":
        return "27"

    if number1 == "18" and number2 == "10":
        return "28"

    if number1 == "18" and number2 == "11":
        return "29"

    if number1 == "18" and number2 == "12":
        return "30"

    if number1 == "18" and number2 == "13":
        return "31"

    if number1 == "18" and number2 == "14":
        return "32"

    if number1 == "18" and number2 == "15":
        return "33"

    if number1 == "18" and number2 == "16":
        return "34"

    if number1 == "18" and number2 == "17":
        return "35"

    if number1 == "18" and number2 == "18":
        return "36"

    if number1 == "18" and number2 == "19":
        return "37"

    if number1 == "19" and number2 == "0":
        return "19"

    if number1 == "19" and number2 == "1":
        return "20"

    if number1 == "19" and number2 == "2":
        return "21"

    if number1 == "19" and number2 == "3":
        return "22"

    if number1 == "19" and number2 == "4":
        return "23"

    if number1 == "19" and number2 == "5":
        return "24"

    if number1 == "19" and number2 == "6":
        return "25"

    if number1 == "19" and number2 == "7":
        return "26"

    if number1 == "19" and number2 == "8":
        return "27"

    if number1 == "19" and number2 == "9":
        return "28"

    if number1 == "19" and number2 == "10":
        return "29"

    if number1 == "19" and number2 == "11":
        return "30"

    if number1 == "19" and number2 == "12":
        return "31"

    if number1 == "19" and number2 == "13":
        return "32"

    if number1 == "19" and number2 == "14":
        return "33"

    if number1 == "19" and number2 == "15":
        return "34"

    if number1 == "19" and number2 == "16":
        return "35"

    if number1 == "19" and number2 == "17":
        return "36"

    if number1 == "19" and number2 == "18":
        return "37"

    if number1 == "19" and number2 == "19":
        return "38"
