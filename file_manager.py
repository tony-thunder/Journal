import os

def open(jname):
    """
    This will open a journal file in the data folder for viewing and editing.
    :param jname: Potential journal file name.
    :return:
    """

    jdata = []
    filename = get_fullpath(jname)

    if os.path.exists(filename):
        with open(filename) as jload:
            for entry in jload.readlines():
                jdata.append(entry.rstrip())


def save(jname, jdata):
    filename = get_fullpath(jname)
    print("Saving journal data to {}.".format(filename))

    with open(filename, 'w') as fsave:

        for entry in jdata:
            fsave.write(entry + '\n')


def get_fullpath(jname):
    filename = os.path.abspath(os.path.join('.', 'data', + name + '.jrl'))
    return filename