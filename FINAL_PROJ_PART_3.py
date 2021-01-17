from help import Words_From_Strings_Into_List


def PART_3_OF_FINAL_PROJECT_CPSC_323():

    print("\n\nTRANSLATING PROGRAM TO PYTHON\n\n")

    file_to_be_analyzed = open('finalp2.txt', 'r')

    outfile = open("filep3.py", "w")

    language = []       # will be used to trace
    line_of_code_in_list_form = []      # will be used for error checking

    read_line = file_to_be_analyzed.readline()

    while read_line != '':
        read_line = read_line.strip()
        line_of_code_in_list_form.append(read_line)
        list = Words_From_Strings_Into_List(read_line)
        language.extend(list)
        read_line = file_to_be_analyzed.readline()


    begin_code_line = line_of_code_in_list_form.index('begin')
    begin_code_line += 1

    end_code_line = line_of_code_in_list_form.index('end')
    end_code_line -= 1

    for i in range(begin_code_line,end_code_line,1):

        sentence = line_of_code_in_list_form[i]

        if "show" in sentence:

            sentence = sentence.lstrip("show (")
            sentence = sentence.rstrip(") ;")
            sentence = sentence.strip()

            code = "print("+sentence+")\n"
            outfile.write(code)

        else:

            sentence = sentence.rstrip(";")
            sentence = sentence.strip()

            code = sentence + '\n'
            outfile.write(code)

    sentence = line_of_code_in_list_form[end_code_line]

    if "show" in sentence:

        sentence = sentence.lstrip("show (")
        sentence = sentence.rstrip(") ;")
        sentence = sentence.strip()

        code = "print(" + sentence + ")"
        outfile.write(code)

    else:

        sentence = sentence.rstrip(";")
        sentence = sentence.strip()

        code = sentence
        outfile.write(code)

    file_to_be_analyzed.close()
    outfile.close()