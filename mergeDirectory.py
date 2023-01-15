import shutil
import os

def merge_folders_train():
    for folder in os.listdir("train"):
        if folder == "shiba_dog":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/shiba_inu/" + file)
            os.rmdir("train/" + folder)  # remove empty folder

    for folder in os.listdir("train"):
        if folder == "basset":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/basset_hound/" + file)
            os.rmdir("train/" + folder)  # remove empty folder

    for folder in os.listdir("train"):
        if folder == "german_short_haired_pointer":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/german_shorthaired/" + file)
            os.rmdir("train/" + folder)  # remove empty folder

    for folder in os.listdir("train"):
        if folder == "leonberg":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/leonberger/" + file)
            os.rmdir("train/" + folder)  # remove empty folder

    for folder in os.listdir("train"):
        if folder == "scotch_terrier":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/scottish_terrier/" + file)
            os.rmdir("train/" + folder)  # remove empty folder

    for folder in os.listdir("train"):
        if folder == "staffordshire_bull_terrier":
            for file in os.listdir("train/" + folder):
                shutil.move("train/" + folder + "/" + file, "train/staffordshire_bullterrier/" + file)
            os.rmdir("train/" + folder)  # remove empty folder


merge_folders_train()


def merge_folders_test():
    for folder in os.listdir("test"):
        if folder == "shiba_dog":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/shiba_inu/" + file)
            os.rmdir("test/" + folder)  # remove empty folder

    for folder in os.listdir("test"):
        if folder == "basset":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/basset_hound/" + file)
            os.rmdir("test/" + folder)  # remove empty folder

    for folder in os.listdir("test"):
        if folder == "german_short_haired_pointer":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/german_shorthaired/" + file)
            os.rmdir("test/" + folder)  # remove empty folder

    for folder in os.listdir("test"):
        if folder == "leonberg":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/leonberger/" + file)
            os.rmdir("test/" + folder)  # remove empty folder

    for folder in os.listdir("test"):
        if folder == "scotch_terrier":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/scottish_terrier/" + file)
            os.rmdir("test/" + folder)  # remove empty folder

    for folder in os.listdir("test"):
        if folder == "staffordshire_bull_terrier":
            for file in os.listdir("test/" + folder):
                shutil.move("test/" + folder + "/" + file, "test/staffordshire_bullterrier/" + file)
            os.rmdir("test/" + folder)  # remove empty folder


merge_folders_test()


def merge_folders_validate():
    for folder in os.listdir("validate"):
        if folder == "shiba_dog":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/shiba_inu/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder

    for folder in os.listdir("validate"):
        if folder == "basset":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/basset_hound/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder

    for folder in os.listdir("validate"):
        if folder == "german_short_haired_pointer":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/german_shorthaired/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder

    for folder in os.listdir("validate"):
        if folder == "leonberg":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/leonberger/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder

    for folder in os.listdir("validate"):
        if folder == "scotch_terrier":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/scottish_terrier/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder

    for folder in os.listdir("validate"):
        if folder == "staffordshire_bull_terrier":
            for file in os.listdir("validate/" + folder):
                shutil.move("validate/" + folder + "/" + file, "validate/staffordshire_bullterrier/" + file)
            os.rmdir("validate/" + folder)  # remove empty folder


merge_folders_validate()
