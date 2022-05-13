from polls.controllers import get_question_controller


def get_question_command():
    id = input('Question id: ')
    question = get_question_controller(id)
    if question:
        print(
            f"""
            Title: {question._title}.

            Choices & votes:

                Choice: {question._choices[0]._text}.
                    - Total votes: {question._choices[0]._votes}.

                Choice: {question._choices[1]._text}.
                    - Total votes: {question._choices[1]._votes}.

                Choice: {question._choices[2]._text}.
                    - Total votes: {question._choices[2]._votes}.

                Choice: {question._choices[3]._text}.
                    - Total votes: {question._choices[3]._votes}.
            """)
    else:
        print('Question does not exist')
