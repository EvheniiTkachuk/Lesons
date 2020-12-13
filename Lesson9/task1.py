# Files
# Write a script that creates a new output file called
# myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and
# prints its contents. Run your two scripts from the system command line.
# Does the new file show up in the directory where you ran your scripts?
# What if you add a different directory path to the filename passed to open?
# Note: file write methods do not add newline characters to your strings;
# add an explicit ‘\n’ at the end of the string if you want to fully
# terminate the line in the file.


def file_open_for_write(object, file_name=''):
    try:
        with open(file_name, 'w') as write_file:
            write_file.write(str(object + '\n'))
    except:
        return False
    else:
        return True


def file_open_for_read(file_name='myfile.txt'):
    try:
        with open(file_name, 'r') as read_file:
            temp = read_file.read()
            print(temp)
    except:
        return False
    else:
        return True


def check_implementation(object, txt):
    if object:
        print(f'\n... {txt} successfully...\n')
    else:
        print(f'\n...{txt} unsuccessfully...\n')


text = 'Hello file world!'
check_implementation(file_open_for_write(text), 'open')
check_implementation(file_open_for_read(), 'read')

check_implementation(file_open_for_write(text, 'd:\\Program learn\\PyCharm Community Edition 2019.3.2\\'
                                               'Projects\\Lesson9\\venv\\myfile.txt'), 'open')
check_implementation(file_open_for_read('d:\\Program learn\\PyCharm Community Edition 2019.3.2\\'
                                        'Projects\\Lesson9\\venv\\myfile.txt'), 'read')

