def square_calc(*args, typ='circle') -> tuple:
    """
    Функция нахождения площади фигур

    по умолчанию:
    если дано только одно значение считаем площадь круга
    если давно 2 значения то возвращается ошибка
    если давно 3 значения считаем площадь треугольника
    если дано 4 и более значения, считаем кортеж с минимальной площадью многоугольника и максимальной,
    т.к. фигуры с четырьмя и более углами не жесткие

    :param args: принимает целые числа
    :param typ: принимает возможные значения "circle" и "triangle".

    :return: -кортеж с одним или двумя значениями float, если значений 2, то первое больше второго,
    возврат -1 на первом месте кортежа означает ошибку, на втором месте ее описание
    """

    from decimal import Decimal
    from math import pi
    from math import cos
    from math import sin
    from math import radians

    def triangle(a: float, b: float, c: float) -> float:
        """ Подфункция нахождения площади треугольника по 3 ем сторонам"""
        pre_return = (Decimal(a) + Decimal(b) + Decimal(c)) / Decimal(2)
        pre_return = Decimal.sqrt(pre_return * (pre_return - Decimal(a)) * (pre_return - Decimal(b)) * (pre_return - Decimal(c))).quantize(Decimal('1.000'))
        answer = pre_return.as_integer_ratio()
        return answer[0] / answer[1]
##################################################################################################################################

    def square_many_angl(*args, max_tr_min_f: bool, n: int) -> float:
        """ Подфункция для рекурсивного нахождения площади многоугольника путем отрезания от него треугольников"""
        if len(args) == 3:
            return triangle(args[0], args[1], args[2])
##################################################################################################################################

        if max_tr_min_f is False:
            if args[0] + args[-1] > args[0] + args[1]:
                second = args[-1]
                new_section = Decimal.copy_abs(Decimal(args[0]) - Decimal(args[-1])) + Decimal(0.1)

                for i in range(int((Decimal(args[0]) + Decimal(args[-1]) + Decimal(0.1) - new_section)*10)):
                    if new_section + Decimal(i * 0.1) + Decimal((len(args)-3) * 0.1) < Decimal(sum(args)) - Decimal(args[0]) - Decimal(args[-1]):
                        if len(args) == 4 and new_section + Decimal(i * 0.1) < Decimal.copy_abs(Decimal(args[1]) - Decimal(args[2])):
                            continue

                        else:
                            arg = []
                            new_section = new_section + Decimal(i * 0.1)
                            new_section = new_section.quantize(Decimal('1.0'))
                            new_section = new_section.as_integer_ratio()
                            arg.append(new_section[0] / new_section[1])

                            for j in range(0, len(args)-2):
                                arg.append(args[j + 1])

                        break
##################################################################################################################################

            else:
                second = args[1]
                new_section = Decimal.copy_abs(Decimal(args[0]) - Decimal(args[1])) + Decimal(0.1)

                for i in range(int((Decimal(args[0]) + Decimal(args[1]) + Decimal(0.1) - new_section)*10)):

                    if new_section + Decimal(i * 0.1) + Decimal((len(args)-3) * 0.1) < Decimal(sum(args)) - Decimal(args[0]) - Decimal(args[1]):
                        if len(args) == 4 and new_section + Decimal(i * 0.1) < Decimal(args[2]) - Decimal(args[3]):
                            continue

                        else:

                            arg = []
                            new_section = new_section + Decimal(i * 0.1)
                            new_section = new_section.quantize(Decimal('1.0'))
                            new_section = new_section.as_integer_ratio()
                            arg.append(new_section[0] / new_section[1])
                            for j in range(0, len(args)-2):
                                arg.append(args[j + 2])
                        break
##################################################################################################################################

            if len(arg) > 3:
                return square_many_angl(*arg, max_tr_min_f=False, n=n) + triangle(args[0], second, new_section[0] / new_section[1])
            elif len(arg) == 3:
                return triangle(a=arg[0], b=arg[1], c=arg[2])
##################################################################################################################################
##################################################################################################################################

        elif max_tr_min_f is True:
            maxx = Decimal(args[0]) + Decimal(args[1]) - Decimal(0.1)
            minn = Decimal.copy_abs(Decimal(args[0]) - Decimal(args[1])) + Decimal(0.1)
            third_side = (Decimal(maxx) + Decimal(minn)) / Decimal(2)
            third_side = third_side * (((Decimal(n) / Decimal.sqrt(Decimal(1) + (Decimal(n) * Decimal(n)))) - Decimal(2.5) / Decimal(n)) + Decimal(1))
            third_side = third_side.quantize(Decimal('1.0'))
            if third_side > maxx:
                third_side = Decimal(maxx) * (Decimal(1) - Decimal(1 / n))
                third_side = third_side.quantize(Decimal('1.0'))
                if third_side < minn:
                    third_side = maxx

            for i in range(int(Decimal(((third_side - minn) * 10) + 2))):

                if third_side - Decimal(i * 0.1) + Decimal((len(args)-3) * 0.1) < Decimal(sum(args)) - Decimal(args[0]) - Decimal(args[1]):

                    arg = []
                    third_side = third_side - Decimal(i * 0.1)
                    third_side = third_side.quantize(Decimal('1.0'))
                    third_side = third_side.as_integer_ratio()
                    arg.append(third_side[0] / third_side[1])
                    for j in range(0, len(args) - 2):
                        arg.append(args[j + 2])
                    break
##################################################################################################################################

                if i == int(Decimal((third_side - minn) * 10) + 1) and third_side != maxx:

                    range_value = int((maxx - third_side) * 10)
                    for j in range(int(Decimal(third_side * 10)), range_value):

                        if third_side + Decimal(j * 0.1) + Decimal((len(args)-3) * 0.1) < Decimal(sum(args)) - Decimal(args[0]) - Decimal(args[1]):

                            arg = []
                            third_side = third_side + Decimal(i * 0.1)
                            third_side = third_side.quantize(Decimal('1.0'))
                            third_side = third_side.as_integer_ratio()
                            arg.append(third_side[0] / third_side[1])
                            for k in range(len(args) - 2):
                                arg.append(args[j + 2])
                            break

            if len(arg) > 3:
                return square_many_angl(*arg, max_tr_min_f=True, n=n) + triangle(args[0], args[1], third_side[0] / third_side[1])
            elif len(arg) == 3:
                return triangle(a=arg[0], b=arg[1], c=arg[2])

##################################################################################################################################
##################################################################################################################################
    for i in args:
        if type(i) is not int:
            return (-1, "одно или несколько переданных значений не является целым числом")
        elif i <= 0:
            return (-1, "одно или несколько переданных значений равно нулю или является отрицательным числом")
        elif len(args) == 2:
            return (-1, "не достаточно данных для вычисления площади, передано только 2 величины")
##################################################################################################################################

    if len(args) == 1 and typ == 'circle':
        # ищем площадь по стандартной формуле
        pre_return = Decimal(args[0]) * Decimal(args[0]) * Decimal(pi)
        pre_return = pre_return.quantize(Decimal('1.000'))
        answer = pre_return.as_integer_ratio()
        return (answer[0] / answer[1],)
##################################################################################################################################

    elif (len(args) == 3 and typ == 'triangle') or (len(args) == 3):
        # Проверка возможности существования заданного треугольника
        summ = sum(args)
        for i in range(len(args)):
            if args[i] >= summ - args[i]:
                return (-1, "одна из сторон треугольника превышает или равна сумме двух оставшихся сторон")

        # Ищем площадь через полу-периметр
        return (triangle(args[0], args[1], args[2]),)
##################################################################################################################################

    elif len(args) > 3:
        # Проверка возможности существования заданного многоугольника
        summ = sum(args)
        for i in range(len(args)):
            if args[i] >= summ - args[i]:
                return (-1, "одна из сторон многоугольника превышает или равна сумме оставшихся сторон")
        if sum(args) - max(args) - max(args) < 0.1 * (len(args) - 2):
            return (-1, "такой многоугольник имеет место быть, но шаг перебора длин диагоналей, для нарезки треугольников слишком велик, текущий 0.1")
##################################################################################################################################

        maxi = [0, -1]
        for i in range(len(args)):
            if args[i] > maxi[0]:
                maxi = [args[i], i]
        if maxi[1] != -1:
            arg = []
            for i in range(len(args)):
                j = maxi[1] + i
                if j > len(args) - 1:
                    j = maxi[1] + i - len(args)
                arg.append(args[j])
##################################################################################################################################

        mini = square_many_angl(*arg, max_tr_min_f=False, n=len(args))
        if max(args) == sum(args) / len(args):
            maxi = (Decimal(len(args)) * Decimal(args[0]) * Decimal(args[0])) / Decimal(4) * (Decimal(cos(radians(180/len(args))) / sin(radians(180/len(args)))))
            maxi = maxi.quantize(Decimal('1.000'))
            maxi = maxi.as_integer_ratio()
            maxi = maxi[0] / maxi[1]
        else:
            maxi = square_many_angl(*arg, max_tr_min_f=True, n=len(args))
        return (maxi, mini)



