from help import RemoveWhiteSpaces
from help import Space_Out


def PART_1_OF_FINAL_PROJECT_CPSC_323():

    print("\n\nWHITE SPACE AND COMMENT REMOVEAL\n\n")

    infile = open('finalp1.txt','r')
    whole = infile.read()
    number_of_lines = whole.count('\n')
    infile.close()


    file1 = open('finalp1.txt', 'r')

    output_to_file2 = open('finalp2.txt', 'w')

    for i in range(number_of_lines):

        read_line = file1.readline()            #This will read a line from the .txt file

        read_line = read_line.strip()              # This will strip whitespaces, \t s, and \n s from both sides of the string in variable
        read_line = read_line.replace('\t', '')  #It will remove any \t characters that still exist in the string

        read_line = RemoveWhiteSpaces(read_line) # will remove any excess whitespaces

        are_there_comments = False
        comments_start_index = 0

        if read_line[0:2] !='/*' and read_line[len(read_line)-2:] != '*/' and read_line[0:2] !='//' and read_line != '':

            read_line = Space_Out(read_line)
            read_line = RemoveWhiteSpaces(read_line)

            for i in range(len(read_line)):

                if read_line[i - 2:i] == '//':
                    are_there_comments = True
                    comments_start_index = i - 2

            if are_there_comments:
                read_line = read_line[0:comments_start_index]
                read_line = read_line.strip()
                output_to_file2.write(read_line + '\n')
            else:
                read_line = read_line.strip()
                output_to_file2.write(read_line + '\n')

    read_line = file1.readline()  # This will read a line from the .txt file
    read_line = read_line.strip()  # This will strip whitespaces, \t s, and \n s from both sides of the string in variable
    read_line = read_line.replace('\t', '')  # It will remove any \t characters that still exist in the string

    read_line = RemoveWhiteSpaces(read_line)  # will remove any excess whitespaces

    are_there_comments = False
    comments_start_index = 0

    if read_line[0:2] != '/*' and read_line[len(read_line) - 2:] != '*/' and read_line[0:2] != '//' and read_line != '':

        read_line = Space_Out(read_line)
        read_line = RemoveWhiteSpaces(read_line)

        for i in range(len(read_line)):

            if read_line[i - 2:i] == '//':
                are_there_comments = True
                comments_start_index = i - 2

        if are_there_comments:
            read_line = read_line[0:comments_start_index]
            read_line = read_line.strip()
            output_to_file2.write(read_line)
        else:
            read_line = read_line.strip()
            output_to_file2.write(read_line)


    file1.close()
    output_to_file2.close()
    print("\nFINISHED PART 1\n")