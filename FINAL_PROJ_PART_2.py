from help import Words_From_Strings_Into_List
from help import Complete_LISTIFICATION
from help import Is_Non_Terminal
from help import COMPILER_ERROR_message
from help import If_terminalKEY_corresponds_with_NON_TERMINAL
from help import ERROR_reader
from help import IF_VAR_IS_DECLARED_PROPERLY
from help import CHECK_FOR_MISSING_LEFT_PARANTHESES
from help import CHECK_IF_VARIABLES_ARE_DEFINED

from EXCEL_Rule_EXPORT import IMPORT_RULES_FROM_EXCEL


def PART_2_OF_FINAL_PROJECT_CPSC_323():

    print("\n\nSYNTAX ANALYSIS\n\n")

    RULE = IMPORT_RULES_FROM_EXCEL()
    file_to_be_analyzed = open('finalp2.txt', 'r')


    language = []       # will be used to trace
    sentences = []      # will be used for error checking

    read_line = file_to_be_analyzed.readline()
    while read_line != '':
        # read_line = file_to_be_analyzed.readline()
        read_line = read_line.strip()
        sentences.append(read_line)
        list = Words_From_Strings_Into_List(read_line)
        language.extend(list)
        read_line = file_to_be_analyzed.readline()

    #INSERT FUNCTIONS TO CHECK FOR ',' WHEN VARIABLES ARE BEING DECLARED
    IF_VAR_IS_DECLARED_PROPERLY(sentences)
    CHECK_FOR_MISSING_LEFT_PARANTHESES(sentences)

    language = Complete_LISTIFICATION(language)

    string = ''
    stack = []

    read_index = 0
    read_next = 0

    is_language_accepted = True
    is_match = False


    # stack.append('$')  # append in this case is push
    # print('\nPush: $')
    for first_key in RULE.keys():  # This is to push the starting symbol
        print('Push:' + first_key + '\n')
        stack.append(first_key)
        break

    while (is_language_accepted): #and read_index < len(language)):

        if string != 'λ':
            print(stack)

        temp = stack.pop()

        if temp != 'λ':
            print('Pop: ' + temp)

        if temp == 'end' and language[read_index] == 'end':
            break
        elif read_index >= len(language):
            print("\n\nERROR_4: 'end' is expected")
            is_language_accepted = False
            break

        If_terminalKEY_corresponds_with_NON_TERMINAL(RULE,temp,language[read_index])

        if temp == language[read_index]:
            print('match')
            is_match = True
            read_index += 1

        elif temp != 'λ':

            if (read_index == read_next):
                read_next += 1
                print('-' * 10)
                print("Read:" + language[read_index])
                print('-' * 10)

            #insert If and a function to detect if temp (string) is a terminal, temp should be non-terminal
            if Is_Non_Terminal(temp):
                string = RULE[temp][language[read_index]]
            else:
                COMPILER_ERROR_message(temp)
                exit()
                is_language_accepted = False
                break

            ERROR_reader(RULE[temp][language[read_index]]) #this will help d

            if RULE[temp][language[read_index]] == '':
                is_language_accepted = False
                print('[' + temp + ', ' + language[read_index] + ']   is an empty box/entry')
                break
            else:
                print('[' + temp + ', ' + language[read_index] + '] = ' + string)

            show_push_action = []

            if string != 'λ':
                show_push_action = Words_From_Strings_Into_List(string)
                show_push_action.reverse()
                print('Push: {0}\n'.format(show_push_action))
                stack.extend(show_push_action)



    CHECK_IF_VARIABLES_ARE_DEFINED(sentences)

    # end result
    if (is_language_accepted):
        print("\nACCPETED")
        file_to_be_analyzed.close()
    else:
        print('\nREJECTED')
        exit()
