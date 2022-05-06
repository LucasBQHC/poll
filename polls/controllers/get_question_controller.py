from db import poll_list


def get_question_controller(id):
    for question in poll_list:
        if question.id == id:
            return question
