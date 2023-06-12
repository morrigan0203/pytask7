""" *** Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла, возвращайтесь в его начало.
***   """

from pathlib import Path
from typing import TextIO

#from zadanie_1 import  as z1
#import zadanie_2 as z2
# from two_files_in_one import two_files_in_one


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def two_files_in_one(numbers: Path, words: Path, result: Path ) -> None:
    with (open(numbers, 'r', encoding='utf-8') as f_num,
        open(words, 'r', encoding='utf-8') as f_word,
        open(result, 'w', encoding='utf-8') as f_res
    ):
        lem_numbers = sum(1 for _ in f_num)
        len_word = sum(1 for _ in f_word)
        for _ in range(max(lem_numbers, len_word)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_word)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()}{abs(mult)}\n')
            elif mult > 0:
                f_res.write((f'{word.upper()}{round(mult)}\n'))
            f_res.write('')

if __name__ == '__main__':
    #z1.feel_numbers(3, 'file_1.txt')
    #z2.name_gen(10, 4, 7, Path('name_gen'))
    two_files_in_one('file_1.txt', 'name_gen', 'result.txt' )
