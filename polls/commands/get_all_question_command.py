from polls.controllers import get_all_question_controller


def get_all_question_command():
    questions = get_all_question_controller()
    get_all_question_controller()
    print('Poll list:')
    print('\n')
    for index, question in enumerate(questions, start=0):
        print(f'Title: {index+1}) {question.title} Id: {question.id}')
