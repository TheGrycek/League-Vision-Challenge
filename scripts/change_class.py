import os

'''
Script changes every class number in every *.txt yolo labeling file in given directory
'''

def change_class_num(num):
    print("Enter directory:")
    directory = input()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_dir = os.path.join(directory, filename)
            file_size = os.path.getsize(file_dir)
            file = open(file_dir, 'r+')

            if file_size == 0:
                print("Empty file:")
                print(filename)

            lines = file.readlines()
            new_file = ""

            for line in lines:
                new_line = line.split(" ")
                new_line[0] = num
                new_line = " ".join(new_line)
                new_file += new_line

            with open(file_dir, 'w') as file:
                file.write(new_file)


try:
    change_class_num("0")

except Exception as e:
    print("ERROR: ", e)
    change_class_num("0")
