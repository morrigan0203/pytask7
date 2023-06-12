from pathlib import Path
import os
import shutil

VIDEOS = ["mp4","mpg","mov","avi"]
IMAGES = ["gif","png","jpg"]
TEXTS = ["txt","log","properties"]

def move_to_folder(f, exts, target_dir):
    for e in exts:
        if f.name.endwith("." + e):
            shutil.move(f, target_dir)

def sort_files(source: str, target: str):
    if not os.path.exists(target):
        os.makedirs(target)
    videos_path = os.path.join(target, "videos")
    images_path = os.path.join(target, "images")
    texts_path = os.path.join(target, "texts")
    if not os.path.exists(videos_path):
        os.makedirs(videos_path)
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    if not os.path.exists(texts_path):
        os.makedirs(texts_path)
    with os.scandir(source) as files:
        for f in files:
            if f.is_file():
                move_to_folder(f, VIDEOS, videos_path)
                move_to_folder(f, IMAGES, images_path)
                move_to_folder(f, TEXTS, texts_path)


if __name__ == "__main__":
    full_source = os.path.join(Path(__file__).parent.absolute(), "source")
    full_target = os.path.join(Path(__file__).parent.absolute(), "target")

    sort_files(full_source, full_target)
