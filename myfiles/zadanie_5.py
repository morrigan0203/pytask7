from .zadanie_4 import gen_files

def gen_files_exts(files_infos: list, min_len: int = 6, max_lengh: int = 30, min_len_byte: int = 256, max_len_byte: int = 4096):
    for i in files_infos:
        gen_files(i[0], min_len, max_lengh, min_len_byte, max_len_byte, i[1])

if __name__ == "__main__":
    gen_files_exts({("txt",3),("txt2",4),("txt3",1)},5,10,10,50)