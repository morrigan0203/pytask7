import os
from pathlib import Path


def rename_file(source_dir: str, target_name: str, count_num: int, source_ext: str, target_ext: str, source_range: tuple):
    counter = 1
    with os.scandir(source_dir) as files:
        for f in files:
            if f.name.endswith("." + source_ext):
                curr_path = f.path[0:-1*len(f.name)]
                new_name = f.name[source_range[0]:source_range[1]] + target_name + str(counter).zfill(count_num) + "." + target_ext
                os.rename(f.path, curr_path + new_name)
                counter = counter + 1



if __name__ == "__main__":
    source_dir = os.path.join(Path(__file__).parent.absolute(), "source_dz")
    rename_file(source_dir, "_new_", 3, "txt", "text", (3,8))