import os
import random
'''
Script renames files e.g. img701.jpg, img702.jpg, img703.jpg ... with corresponding *.txt file in random order
'''


def rename():
    print("Enter files directory:")
    img_dir = input()
    print("Enter first part of name:")
    img_name = input()
    print("Enter first file number:")
    img_number = input()
    print("Enter files extension (e.g. .jpg):")
    ext = input()
    new_names = []
    folder_names = os.listdir(img_dir)
    to_remove = []

    i = 0

    for name in folder_names:
        if name.endswith(ext):
            new_names.append(img_name + str(int(img_number) + i) + ext)
            i += 1

    for name in new_names:
        if name in folder_names:
            to_remove.append(name)

    for name in to_remove:
        folder_names.remove(name)
        new_names.remove(name)

    for filename in folder_names:
        if filename.endswith(ext):
            rand_name = random.choice(new_names)
            print(f"rand name: {rand_name}")
            os.rename(os.path.join(img_dir, filename), os.path.join(img_dir, rand_name))
            new_names.remove(rand_name)

            txt_name = os.path.splitext(filename)[0] + ".txt"
            for filename2 in folder_names:
                if filename2 == txt_name:
                    new_txt_name = os.path.splitext(rand_name)[0] + ".txt"
                    os.rename(os.path.join(img_dir, filename2), os.path.join(img_dir, new_txt_name))


try:
    rename()

except Exception as e:
    print("ERROR: ", e)
    rename()
