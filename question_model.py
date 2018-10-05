class Question():
    def __init__(self, id, title, description, answers):
        self.counter = 0
        #self.questions = []
        pass

    def get(self, id):
        for question in self.questions:
            if question['id'] == id:
                return question
            else:
                return('Question not found!')

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        question = self.get(id)
        pass
