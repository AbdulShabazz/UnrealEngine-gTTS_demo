"""
This script moves all mp3 files from the current directory to the directory
specified by the filename in the mp3 file.
"""


import os


def rename_mp3_files_with_whitespace(directory_path_string: str) -> None:
    """
    Moves all mp3 files from the current directory to the directory
    specified by the filename in the mp3 file.
    """
    # Check if the directory exists
    if not os.path.exists(directory_path_string):
        raise FileNotFoundError("The directory does not exist.")

    for filename in os.listdir("."):
        # Check if the file is a .mp3 file
        try:
            if filename.endswith(".mp3") and filename.find(" ") != -1:
                os.rename(filename, filename.replace(" ", ""))
        except Exception as e:
            print(f"{e}")
            continue


if __name__ == '__main__':
    # Specify the directory containing the .mp3 files
    directory_path = '.'
    rename_mp3_files_with_whitespace(directory_path)

