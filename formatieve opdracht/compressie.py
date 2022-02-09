working_file = 'decompressed_file.txt'


def read_file_lines(file):
    """
    takes the location of a file as input. reads the file and returns each line as an item of a list.
    args:
        :param file: the location of a file
    returns:
        :return: (list) the content of a file in a list with each item of the list being a line in the file.
    """
    with open(file, 'r') as open_file:
        return open_file.readlines()


def write_to_file(data, file):
    """
    takes data and the location of a file as input. writes the data to the file.
    args:
        :param data: (str) data you want to write to the file
        :param file: file location of the file
    returns:
        :return: doesn't return anything; data is written to the file
    """
    with open(file, 'w') as open_file:
        open_file.write(data)


def pass_void(string):
    """
    takes a string as input. returns a copy of the string without empty spaces (' ', '\n', '\t') at the beginning
    args:
        :param string: (str) a string
    returns:
        :return: (str) copy of the input string starting with the first index that isn't an empty space (' ', '\n', '\t')
    """
    unwanted = ' \n\t'
    for i, char in enumerate(string):
        if char not in unwanted:
            return string[i:]


def compress_file(file):
    """
    takes the location of a file as input. reads the content of the file and compresses it by:
    - deleting all spaces and spaces at the beginning of a line
    - deleting all empty lines
    writes this compressed data to a new file.
    args:
        :param file: location of the file
    returns:
        :return: doesn't return anything; the data is compressed and written to a new file
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
