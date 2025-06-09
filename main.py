def summarize(x: int, y: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        raise ValueError("Не для единицы")
    return x + y

def factorial(num):
    if num < 0:
        raise ValueError
    if not float(num).is_integer():
        raise ValueError

    result = 1
    while num > 1:
        result *= num
        num -= 1

    return result




#
# def test_function(func, expected, *args, **kwargs):
#     try:
#         result = func(*args, **kwargs)
#         assert result == expected
#         print('Тест прошел')
#     except AssertionError:
#         print('Тест не пройден')
#     except Exception as e:
#         print(f'Вылетело исключение {e}. Тест не пройден')
#
#
# test_function(summarize, 12, 5, 7)
# test_function(summarize, 7, 0, 7)
# test_function(summarize, 8, 1, 7)


if __name__ == '__main__':
    print('main')