########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########

########## global vars ##########

########## classes & functions ##########
def read_file_into_var(path, read_as_string=True, encoding="utf-8"):
    """
    This reads a given file into a variable.
    :param path string e.g. "/folder1/file"
    :return string
    """
    txt = ""
    try:
        with open(path, "r", encoding=encoding) as file:
            txt = file.read()
    except Exception as e:
        print(e)

    return txt


########## main ##########


########## complete ##########
