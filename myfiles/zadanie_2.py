""" Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.


6 букв могут обозначать гласные звуки: «A», «E», «I», «O», «U», «Y»;
21 буква может обозначать согласные звуки: «B», «C», «D», «F», «G», «H», «J», «K», «L», «M», «N», «P», «Q», «R», «S», «T», «V», «W», «X», «Y», «Z».
"""


from pathlib import Path
from random import randint, choice

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnpqrstvwxz'

def name_gen(count: int, str_len_min: int, str_len_max: int, file_2 : Path) -> None:
    with open(file_2, 'a', encoding = 'utf-8') as f:
        for _ in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS) for i in range(randint(str_len_min, str_len_max)))
            f.write(f'{rad_string.capitalize()}\n')




#from pathlib import Path
# from fill_names import feel_numbers
#from frm_two_files import name_gen

if __name__ == "__main__":
    print(__name__)
    # feel_numbers()
    name_gen(10, 4, 7, Path('name_gen'))
