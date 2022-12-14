import os
from os.path import join, dirname, realpath

from werkzeug.utils import secure_filename
from flask import url_for

import database_manager

UPLOADS_PATH = join(dirname(realpath(__file__)), "static", "images")


def upload_picture(file, owner_table):
    if file:
        filename = f"{owner_table}_id_{str(database_manager.get_question_seq_value().get('last_value') + 1) if owner_table == 'question' else str(database_manager.get_answer_seq_value().get('last_value') + 1)}.jpg"
        path_to_file = join(UPLOADS_PATH, filename)
        file.save(path_to_file)
        return "images/" + filename

    return ""


def add_answer_number(questions):
    for index in range(len(questions)):
        answer_number = len(database_manager.get_answers_for_question(questions[index]))
        questions[index].update({"answer_number": answer_number})
    return questions


def add_answers_to_question(question):
    answers = database_manager.get_answers_for_question(question)
    for index in range(len(answers)):
        answers[index] = add_comments_to_answer(answers[index])
    question.update({"answers": answers})
    return question


def add_comments_to_question(question):
    comments = database_manager.get_question_comments(question)
    question.update({"comments": comments})
    return question


def add_comments_to_answer(answer):
    comments = database_manager.get_answer_comments(answer)
    answer.update({"comments": comments})
    return answer


def keep_view_question_untouch(question_id):
    question = database_manager.get_question_by_id(question_id)
    question.update({"view_number": int(question.get("view_number")) - 1})
    database_manager.update_question(question)
    return question


def get_first_five_dicts(dicts):
    first_five = []
    try:
        for index in range(5):
            first_five.append(dicts[index])
    except:
        print("less than 5 questions available")
    return first_five


def add_tag_to_question(question_id, tag_name):
    tag = database_manager.get_tag_by_name(tag_name)
    if tag:
        database_manager.add_tag_relation(question_id, tag.get("id"))
    else:
        database_manager.add_tag(tag_name)
        tag = database_manager.get_tag_by_name(tag_name)
        database_manager.add_tag_relation(question_id, tag.get("id"))


def get_tag_for_question(question):
    question_tags = database_manager.get_tag_relation(question.get("id"))
    try:
        tags = [
            database_manager.get_tag_by_id(tag.get("tag_id")) for tag in question_tags
        ]
        question.update({"tags": tags})
    except:
        print("No tag")
    return question


def get_tag_for_questions(questions):
    for index in range(len(questions)):
        questions[index] = get_tag_for_question(questions[index])
    return questions


def delete_question(question_id):
    database_manager.delete_answers_for_question(question_id)
    database_manager.delete_all_question_tags_relation(question_id)
    database_manager.delete_question(question_id)


def get_question_id_from_comment(comment):
    if comment.get("answer_id"):
        answer = database_manager.get_answer_by_id(comment.get("answer_id"))
        comment.update({"question_id": answer.get("question_id")})
    return comment


def blah_blah(user_id):
    user = database_manager.get_user_by_id(user_id)
    questions = database_manager.get_questions_user(user_id)
    answers = database_manager.get_answers_user(user_id)
    comments = database_manager.get_comments_user(user_id)
    user.update({"questions": questions, "answers": answers, "comments": comments})
    return user
