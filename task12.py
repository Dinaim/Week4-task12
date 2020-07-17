# 4) Напишите функцию который будет конвертировать Фаренгейт в Цельсии и
# наоборот.


def fah2cel(fah):
    cel = 5.0*(fah - 32) / 9
    return cel

c1 = fah2cel(32)
c2 = fah2cel(44)
print(c1, c2)

def cel2fah(cel):
    fah = (9 / 5.0 * cel) + 32
    return fah

f1 = cel2fah(6.67)
f2 = cel2fah(0)
print(f1, f2)