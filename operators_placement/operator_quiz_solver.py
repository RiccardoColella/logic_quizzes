import sys

sys.setrecursionlimit(10000)


def recursive_function(numero, somma, lista_sommati=[]):
    num = numero + 1
    list_added_positive = lista_sommati.copy()
    list_added_negative = lista_sommati.copy()
    sum_positive = somma
    sum_negative = somma
    string_positive = "+" + str(num)
    string_negative = "-" + str(num)
    sum_positive += num
    sum_negative -= num
    list_added_positive.append(string_positive)
    list_added_negative.append(string_negative)
    if num == 10:
        if sum_positive == 0:
            ok_combinations.append(list_added_positive)
        if sum_negative == 0:
            ok_combinations.append(list_added_negative)
    else:
        recursive_function(num, sum_positive, list_added_positive)
        recursive_function(num, sum_negative, list_added_negative)


if __name__ == '__main__':
    print("Given the equation []1[]2[]3[]4[]5[]6[]7[]8[]9[]10 = 11")
    print("You can place a '+' or a '-' instead of every symbol '[]'")
    print("How many combinations are possible, so that the equation is true?")
    print("This is the list of combinations that leads the equation to be true:")
    ok_combinations = []
    recursive_function(0, -11)
    for combination in ok_combinations:
        print(combination)

    print("There are this number of possible combinations:", len(ok_combinations))
