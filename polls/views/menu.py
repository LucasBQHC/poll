from polls.commands import create_poll_command, create_question_command, get_question_command, get_all_question_command


def execute():

    option = ''

    while option != 6:

        print('\n')
        print('==================================== MENU: ====================================\n')
        print('| 1 - CREATE Q | 2 - GET | 3 - GET ALL | 4 - CREATE P | 5 - DELETE | 6 - EXIT |\n')
        print('===============================================================================\n')

        try:
            option = int(input('- Please type a number from menu: '))
            print('\n')

            if int(option) > 0 and int(option) < 7:
                if option == 1:
                    create_question_command()

                elif option == 2:
                    get_question_command()

                elif option == 3:
                    get_all_question_command()

                elif option == 4:
                    create_poll_command()

                elif option == 5:
                    print('Not implemented yet')
                    # delete_question_command()

                elif option == 6:
                    print('\tThanks for use our app! \n'.expandtabs(tabsize=22))
                    break
            else:
                print('Invalid option')

        except Exception as e:
            print('\n')
            print(f'\t¡¡¡ {e} !!!'.expandtabs(tabsize=11))
            print('\n')
