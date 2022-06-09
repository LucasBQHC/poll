from polls.repository import QuestionRepository


class GetQuestionController:

    def get_by_id(self, id):
        return QuestionRepository().get_by_id(id)

    def get_all(self):
        return QuestionRepository().get_all()