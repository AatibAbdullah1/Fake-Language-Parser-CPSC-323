def RemoveWhiteSpaces(string):
    string = string.strip()
    if len(string) == 1:
        return string

    result = ''
    previous_Char = " "

    for i in string:
        if not (previous_Char == ' ' and i == previous_Char ):
            result += i
        previous_Char = i

    return result


def Space_Out(string):

    needs_another_look = True

    while needs_another_look:

        needs_another_look = False

        for i in range(1,len(string)):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';' \
                or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' \
                or string[i] == '*' or string[i] == '/' or string[i] == '<') and (string[i -1] != ' ' \
                                                                                  and string[i -1] != '/' ):
                string = string[:i]+' '+string[i]+string[i+1:len(string)]
                needs_another_look = True

        for i in range(0,len(string)-1):
            if (string[i] == ',' or string[i] == '=' or string[i] == ':' or string[i] == ';'\
                or string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-'\
                or string[i] == '*' or string[i] == '/' or string[i] == '>') and (string[i +1] != ' ' \
                                                                                  and string[i +1] != '/' ):
                string = string[:i] + string[i] + ' ' + string[i + 1:len(string)]
                needs_another_look = True

    return  string


def Words_From_Strings_Into_List(string):

    List = []
    non_space_char = 0
    is_non_space_char_assigned = False
    for i in range(len(string)):
        if(string[i] != ' ' and is_non_space_char_assigned == False):
            non_space_char = i
            is_non_space_char_assigned = True
        elif(string[i] == ' '):
            List.append(string[non_space_char:i])
            is_non_space_char_assigned = False
    List.append(string[non_space_char:])
    return List


def If_Is_Reserved_Word(string):
    if(string == 'program' or string == 'var' or string == 'begin' or string == 'end' \
            or string == 'integer' or string == 'show'):
        return True
    return False


def Characters_From_Words_Into_List(word):
    List = []
    for i in word:
        List.append(i)

    return List


def Is_Operator(char):
    if char == ',' or char == '=' or char == ':' or char == ';' or char == '(' or char == ')' \
            or char == '+' or char == '-' or char == '*' or char == '/':
        return True
    return False


def Complete_LISTIFICATION(List):

    Temp_List = []

    for i in List:
        if If_Is_Reserved_Word(i) is False and Is_Operator(i) is False:
            Temp_List.extend(i)
        else:
            Temp_List.append(i)

    return Temp_List


def Is_Non_Terminal(string):
    list_of_nonTERMINALs = ['<prog>','<id>','X','<dec-list>','<dec>','Y','<type>','<stat-list>','Z','<stat>','<write>','<assign>','<expr>','Q','<term>','R','<factor>','<number>','B','<sign>','<digit>', '<letter>']

    return string in list_of_nonTERMINALs


def COMPILER_ERROR_message(string):
    err = {
        'var': "ERROR_2: 'var' is expected",
        'begin': "ERROR_3: 'begin' is expected",
        ';': "ERROR_8: ';' is missing",
        ',': "ERROR_9: ',' is missing",
        '(': "ERROR_10: '(' LEFT parentheses is missing",
        ')': "ERROR_11: ')' RIGHT parentheses is missing"
    }
    print('\n\n'+err[string])


def If_terminalKEY_corresponds_with_NON_TERMINAL(dictionary, non_terminal, potential_key):
    if Is_Non_Terminal(non_terminal):
        if (potential_key in dictionary[non_terminal]) == False:
            err = {
                '<type>': "ERROR_5: 'integer' is either spelled wrong or its not included",
                'Z' :   "ERROR_6: 'show' is spelled wrong"
            }
            print('\n\n'+err[non_terminal])
            exit()



def ERROR_reader(string):

    err_dictionary = {
        'ERROR_1':"'program' is expected",
        'ERROR_2':"'var' is expected",
        'ERROR_3':"'begin' is expected",
        'ERROR_4':"'end' is expected",
        'ERROR_5':"'integer' is Spelled Wrong",
        'ERROR_6':"'show' is spelled wrong",

        'ERROR_8':"';' is missing",
        'ERROR_9':"',' is missing",
        'ERROR_10':"'(' LEFT parentheses is missing",
        'ERROR_11':"')' RIGHT parentheses is missing",

        'ERROR_14':"unknown identifier",
        'ERROR_15':"illegal expression"
    }

    if string[:5] == 'ERROR':
        print('\n\n{0} : {1}'.format(string,err_dictionary[string]))
        exit()



def IF_VAR_IS_DECLARED_PROPERLY(LIST_OF_SENTENCES):

    find_word = "var"

    if find_word in LIST_OF_SENTENCES:
        index_1 = LIST_OF_SENTENCES.index(find_word)
        index_1 += 1
        sentence = LIST_OF_SENTENCES[index_1]

        list_sentence = Words_From_Strings_Into_List(sentence)


        if list_sentence[-3:] == [':','integer',';']:
            if list_sentence[0] != ',' and list_sentence[0] != ':' and list_sentence[0] != 'integer':

                stop_to_colon = len(list_sentence) - 3

                for i in range(1, stop_to_colon, 2):
                    if list_sentence[i] != ',':
                        print("\n\nERROR_9: ',' COMMA is missing")
                        exit()


def CHECK_FOR_MISSING_LEFT_PARANTHESES(LIST_OF_SENTENCES):

    if 'begin' in LIST_OF_SENTENCES and 'end' in LIST_OF_SENTENCES:

        index_after_begin = LIST_OF_SENTENCES.index('begin')
        index_after_begin += 1
        index_of_end = LIST_OF_SENTENCES.index('end')

        for i in range(index_after_begin, index_of_end, 1):

            sentence_in_list = Words_From_Strings_Into_List(LIST_OF_SENTENCES[i])

            if "show" != sentence_in_list[0] or "s" != sentence_in_list[0] or "h" != sentence_in_list[0] or \
                    "o" != sentence_in_list[0] or "w" != sentence_in_list[0]:

                left_parentheses_stack = []

                for i in range(len(sentence_in_list)):

                    if sentence_in_list[i] == '(':
                        left_parentheses_stack.append(sentence_in_list[i])
                    elif sentence_in_list[i] == ')':
                        if len(left_parentheses_stack) == 0:
                            print("\n\nERROR_10: '(' LEFT parentheses is missing")
                            exit()
                        else:
                            left_parentheses_stack.pop()


def CHECK_IF_VARIABLES_ARE_DEFINED(LIST_OF_SENTENCES):

    index_1 = LIST_OF_SENTENCES.index("var")
    index_1 += 1

    sentence = LIST_OF_SENTENCES[index_1]

    list_sentence = Words_From_Strings_Into_List(sentence)

    variables_defined = []
    variables_assigned_values_BEFORE_use = [] # This is to make sure that
    variables_USED = []

    if list_sentence[-3:] == [':', 'integer', ';']:
        if list_sentence[0] != ',' and list_sentence[0] != ':' and list_sentence[0] != 'integer':

            stop_to_colon = len(list_sentence) - 3

            for i in range(0, stop_to_colon, 2):
                variables_defined.append(list_sentence[i])
                variables_assigned_values_BEFORE_use.append(False)
                variables_USED.append(False)

    index_after_begin = LIST_OF_SENTENCES.index("begin")
    index_after_begin += 1

    index_of_end = LIST_OF_SENTENCES.index("end")

    for i in range(index_after_begin, index_of_end, 1):

        sentence_list = Words_From_Strings_Into_List(LIST_OF_SENTENCES[i])

        for k in range(len(sentence_list) - 1 ):

            if sentence_list[k].isdigit() == False and If_Is_Reserved_Word(sentence_list[k]) == False and Is_Operator(sentence_list[k]) == False:

                if sentence_list[k] in variables_defined:

                    bool_index = variables_defined.index(sentence_list[k])


                    if variables_assigned_values_BEFORE_use[bool_index] is False and variables_USED[bool_index] is False:

                        if sentence_list[k+1] == '=':
                            variables_assigned_values_BEFORE_use[bool_index] = True
                        elif sentence_list[k+1] != '=':
                            variables_USED[bool_index] = True

                    elif variables_assigned_values_BEFORE_use[bool_index] is False and variables_USED[bool_index] is True:
                        print("\n\nERROR_!!!: Must assign variable before use")
                        exit()

                elif sentence_list[k] not in variables_defined:
                    print("\n\nERROR_14: UNKNOWN IDENTIFIER, a variable is not defined")
                    exit()
