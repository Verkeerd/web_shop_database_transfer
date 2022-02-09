working_file = 'decompressed_file.txt'


def read_file_lines(file):
    """Takes the location of a file as input. reads the file and returns each line as an item of a list."""
    with open(file, 'r') as open_file:
        return open_file.readlines()


def write_to_file(data, file):
    """Takes data and the location of a file as input. writes the data to the file."""
    with open(file, 'w') as open_file:
        open_file.write(data)


def pass_void(string):
    r"""Takes a string as input. returns a copy of the string without empty spaces (' ', '\n', '\t') at the beginning"""
    unwanted = ' \n\t'
    for i, char in enumerate(string):
        if char not in unwanted:
            return string[i:]


def compress_file(file):
    """
    Takes the location of a file as input. Reads the content of the file and compresses it by:
    - Deleting all spaces and spaces at the beginning of a line
    - Deleting all empty lines
    Writes this compressed data to a new file.
    """
    data_list = read_file_lines(file)

    compressed_data = ''
    for line in data_list:
        trimmed_line = pass_void(line)
        if trimmed_line:
            compressed_data += trimmed_line

    new_file = file[:-4] + '_compressed.txt'

    if compressed_data[-1] == '\n':
        write_to_file(compressed_data[:-1], new_file)

    write_to_file(compressed_data, new_file)


compress_file(working_file)
