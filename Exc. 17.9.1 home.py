element = int(input('Введите число ', )) #вводим число
array = list(map(int, input('Введите элементы списка ', ).split())) #вводим элементы списка через пробел

# функция сортировки:
def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние

def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# функция двоичного поиска:
def binary_search(array, element, left, right):

    if element<array[0] or element > array[-1]: #если элемент вне границы списка
        return 'Число вне границы списка'

    if left > right:  # если левая граница превысила правую,
        return 'Число не найдено в списке'  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:# если элемент в середине,
        if array[0] == element: # если ввёденное число (element) соотвествует элементу в списке с индекcом 0
            return 'Ошибка: Элемент, который меньше введенного пользователем числа, не найден в списке'
        return middle - 1  # возвращаем индекс элемента (позицию), который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

print(merge_sort(array)) #выводим для визулизации отсортированный список
array = merge_sort(array) #перезаписываем переменную array (наш список) после сортировки

print ('Ответ (искомый индекс) = ', binary_search(array, element, 0, len(array))) #ищем индекс элемента, соответствующего условию задачи, иначе выдаём ошибку
