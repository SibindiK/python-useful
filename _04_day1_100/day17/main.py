from question_model import Question
from data import question_data


def main():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    for question in question_bank:
        print(question.text)


if __name__ == "__main__":
    main()
