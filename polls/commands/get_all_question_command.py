from polls.controllers import GetQuestionController


def get_all_question_command():
    questions = GetQuestionController().get_all()
    print('Poll list:')
    print('\n')
    for index, question in enumerate(questions, start=0):
        print(f'Title: {index+1}) {question.get_title()} Id: {question.get_id()}')
