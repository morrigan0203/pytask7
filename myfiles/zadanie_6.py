from random import randint, choice
import os

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnpqrstvwxz'
FILE_CRATE_TRIES = 20

def gen_file_name(min_len, max_lengh)->str:
    return ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS) for i in range(randint(min_len, max_lengh)))

def gen_files(extension: str, dir_name: str, min_len: int = 6, max_lengh: int = 30, min_len_byte: int = 256, max_len_byte: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        rad_string = gen_file_name(min_len, max_lengh)
        data = bytes(randint(0, 255)) 

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        full_path = os.path.join(dir_name, rad_string + "." + extension)
        c = 0
        while c < FILE_CRATE_TRIES:
            if os.path.exists(full_path):
                rad_string = gen_file_name(min_len, max_lengh)
                full_path = os.path.join(dir_name, rad_string + "." + extension)
                c = c + 1
            else:
                break
        for i in range(randint(min_len_byte, max_len_byte)):
            with open(full_path, 'wb') as f:
                f.write(data)

def gen_files_all(files_infos: list, dir_name: str, min_len: int = 6, max_lengh: int = 30, min_len_byte: int = 256, max_len_byte: int = 4096):
    for i in files_infos:
        gen_files(i[0], dir_name, min_len, max_lengh, min_len_byte, max_len_byte, i[1])


if __name__ == "__main__":
    gen_files_all([("txt",2)], "gen_dir")

