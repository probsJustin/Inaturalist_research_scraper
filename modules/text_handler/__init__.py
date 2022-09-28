

def appendToTextFile(file_name, text_line):
    # Appending to file
    with open(file_name, 'a', encoding='utf-8') as new_file:
        new_file.write(text_line)


