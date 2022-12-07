########## begin ##########
# pylint: disable=unused-variable, import-error

########## global imports ##########
import threading
import os

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


def get_file_path(file):
    return f"{os.path.dirname(os.path.realpath(file))}"


def process_items(
    task_list,
    target_function,
    run_in_parallel=True,
    additional_param_string=None,
):
    """
    This process loops thru and runs a function per item in a list.
    - It can bet set to run the tasks sequentially or in parallel threads.

     *** FOR INFO errors raised during a parallel threaded run instance will not bubble to the parent.

    :param task_list list e.g. [], note if a dictionary is passed you need to pass the items iterator i.e. list.items()
    :param target_function string e.g. name of function to be run for each item
    :param run_in_parallel boolean e.g. True
    :param additional_param_string string e.g. to be used to pass any other global variables
    :return None
    """
    if run_in_parallel == True:
        threads = []
        for t in task_list:
            if additional_param_string == None:
                thr = threading.Thread(target=target_function, args=([t]))
            else:
                thr = threading.Thread(
                    target=target_function, args=([t, additional_param_string])
                )
            threads.append(thr)

        for t in threads:
            t.start()

        for t in threads:
            t.join()
    else:
        for t in task_list:
            if additional_param_string == None:
                target_function(t)
            else:
                target_function(t, additional_param_string)


########## main ##########


########## complete ##########
