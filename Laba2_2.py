from Laba2_1 import is_prime

def calculate(a):
    if type(a) == tuple:
        print("Длинна слов кортежа: ")
        for i in a:
            print(len(i), end = " ")
    elif type(a) == list:
        a = set(a)
        a = list(a)
        index_null_first = -1
        index_null_second = -1
        for i in range(len(a)):
            if a[i] == 0:
                if index_null_first == -1:
                    index_null_first = i
                elif index_null_second == -1:
                    index_null_second = i
                else:
                    break

        p = 1

        for i in range(index_null_first, index_null_second+1):
            p *= a[i]
        print("Список после изменений:")
        print(a)
        if index_null_first == -1:
            print("В списке нет нолей")
        elif index_null_second == -1:
            print("В списке один ноль")
        else:
            print("Произведение между первым и вторым нулём:",p)
    elif type(a) == int:
        if is_prime(a):
            print("Это число простое")
        else:
            print("Это не простое число")
    elif type(a) == str:
        b = []
        for i in a:
            b.append(ord(i))
        print("Unicode коды символов строки: ")
        print(b)



calculate("asdasddsa")