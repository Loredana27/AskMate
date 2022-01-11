import database_connection


@database_connection.connection_handler
def add_question(cursor, title, message, image, user_id):
    query = """
            INSERT INTO question(title, message, image,user_id) 
            VALUES (%(title)s, %(message)s, %(image)s, %(user_id)s );"""
    cursor.execute(query, {"title": title, "message": message, "image": image, "user_id": user_id})


@database_connection.connection_handler
def add_answer(cursor, question_id, message, image, user_id):
    query = """
            INSERT INTO answer(question_id, message, image, user_id) 
            VALUES (%(question_id)s, %(message)s, %(image)s, %(user_id)s );"""
    cursor.execute(
        query, {"question_id": question_id, "message": message, "image": image, "user_id": user_id}
    )


@database_connection.connection_handler
def get_questions(cursor):
    query = """
            SELECT * 
            FROM question
            ;"""
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def get_question(cursor, id):
    query = """
            SELECT * 
            FROM question
            WHERE id = %(id)s;
            """
    cursor.execute(query, {"id": int(id)})
    return cursor.fetchone()


@database_connection.connection_handler
def update_question(cursor, question):
    query = """
               UPDATE question
               SET vote_number = %(vote_number)s,
                   view_number = %(view_number)s, 
                   message = %(message)s, 
                   title = %(title)s
               WHERE id = %(id)s
               ;"""
    cursor.execute(query, question)


@database_connection.connection_handler
def get_answers_for_question(cursor, question):
    query = """
            SELECT * 
            FROM answer
            WHERE question_id = %(id)s
            ;"""
    cursor.execute(query, {"id": int(question["id"])})
    return cursor.fetchall()


@database_connection.connection_handler
def get_answer_by_id(cursor, answer_id):
    query = """
                SELECT * 
                FROM answer
                WHERE id = %(id)s
                ;"""
    cursor.execute(query, {"id": int(answer_id)})
    return cursor.fetchone()


@database_connection.connection_handler
def update_answer(cursor, answer):
    query = """
               UPDATE answer
               SET message = %(message)s,
                vote_number = %(vote_number)s
               WHERE id=%(id)s;"""
    cursor.execute(query, answer)


@database_connection.connection_handler
def delete_question(cursor, question_id):
    delete_answers_for_question(question_id)
    query = """
                   DELETE FROM question
                   WHERE id=%(id)s
                   ;"""
    cursor.execute(query, {"id": int(question_id)})


@database_connection.connection_handler
def delete_answers_for_question(cursor, question_id):
    query = """
                   DELETE FROM answer
                   WHERE question_id=%(id)s
                   ;"""
    cursor.execute(query, {"id": int(question_id)})


@database_connection.connection_handler
def delete_answer(cursor, answer_id):
    query = """
                   DELETE FROM answer
                   WHERE id=%(id)s
                   ;"""
    cursor.execute(query, {"id": int(answer_id)})


@database_connection.connection_handler
def get_question_seq_value(cursor):
    query = """
            SELECT last_value 
            FROM question_id_seq
            ;"""
    cursor.execute(query)
    return cursor.fetchone()


@database_connection.connection_handler
def get_answer_seq_value(cursor):
    query = """
            SELECT last_value 
            FROM answer_id_seq
            ;"""
    cursor.execute(query)
    return cursor.fetchone()


@database_connection.connection_handler
def add_comment_question(cursor, message, question_id, user_id):
    query = """
            INSERT INTO comment(message, question_id, user_id) 
            VALUES (%(message)s, %(question_id)s, %(user_id)s);"""
    cursor.execute(query, {"message": message, "question_id": question_id, "user_id": user_id})


@database_connection.connection_handler
def add_comment_answer(cursor, message, answer_id, user_id):
    query = """
            INSERT INTO comment(message, answer_id, user_id) 
            VALUES (%(message)s, %(answer_id)s, %(user_id)s);"""
    cursor.execute(query, {"message": message, "answer_id": answer_id, "user_id": user_id})


@database_connection.connection_handler
def delete_comment(cursor, comment):
    query = """
          DELETE FROM comment
          WHERE id = %(id)s
           ;"""
    cursor.execute(query, comment)


@database_connection.connection_handler
def update_comment(cursor, comment):
    query = """
            UPDATE comment
            SET 
            message = %(message)s,
            edited_count = %(edited_count)s
            WHERE id=%(id)s
            ;"""
    cursor.execute(query, comment)


@database_connection.connection_handler
def get_comment_by_id(cursor, comment_id):
    query = """
                    SELECT * 
                    FROM comment
                    WHERE id = %(id)s
                    ;"""
    cursor.execute(query, {"id": int(comment_id)})
    return cursor.fetchone()


@database_connection.connection_handler
def get_question_by_search(cursor, search_term):
    query = """
        SELECT *
        FROM question
        WHERE LOWER(title) LIKE LOWER(%(search_term)s)
        OR LOWER(message) LIKE LOWER(%(search_term)s)
        ORDER BY submission_time
            ;"""
    cursor.execute(query, {"search_term": ("%" + search_term + "%")})
    return cursor.fetchall(), search_term


@database_connection.connection_handler
def get_latest_five_questions(cursor):
    query = """
        SELECT *
        FROM question
        ORDER BY id DESC  
            ;"""
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def get_answer_comments(cursor, answer):
    query = """
            SELECT *
            FROM comment
            WHERE answer_id = %(id)s
            ;"""
    cursor.execute(query, answer)
    return cursor.fetchall()


@database_connection.connection_handler
def get_question_comments(cursor, question):
    query = """
            SELECT *
            FROM comment
            WHERE question_id = %(id)s
            ;"""
    cursor.execute(query, question)
    return cursor.fetchall()


@database_connection.connection_handler
def add_tag(cursor, name):
    query = """
        INSERT INTO tag (name)
        VALUES  (
                LOWER(%(name)s)
                )   
            ;"""
    cursor.execute(query, {"name": name})


@database_connection.connection_handler
def add_tag_relation(cursor, question_id, tag_id):
    query = """
        INSERT INTO question_tag
        VALUES  (
                %(question_id)s,
                %(tag_id)s
                )   
            ;"""
    cursor.execute(query, {"question_id": question_id, "tag_id": tag_id})


@database_connection.connection_handler
def get_tag_by_name(cursor, tag_name):
    query = """
            SELECT *
            FROM tag 
            WHERE name = LOWER(%(name)s) 
                ;"""
    cursor.execute(query, {"name": tag_name})
    return cursor.fetchone()


@database_connection.connection_handler
def get_tag_by_id(cursor, tag_id):
    query = """
            SELECT *
            FROM tag 
            WHERE id = %(id)s
                ;"""
    cursor.execute(query, {"id": tag_id})
    return cursor.fetchone()


@database_connection.connection_handler
def get_sorted_questions(cursor, sort_by, order_direction):
    query = f"""
                SELECT *
                FROM question 
                order by {sort_by} {order_direction}
                    ;"""
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def get_tag_relation(cursor, question_id):
    query = """
                SELECT *
                FROM question_tag 
                WHERE question_id = %(question_id)s 
                    ;"""
    cursor.execute(query, {"question_id": question_id})
    return cursor.fetchall()


@database_connection.connection_handler
def delete_tag_relation(cursor, question_id, tag_id):
    query = """
            DELETE FROM question_tag
            WHERE 
                question_id = %(question_id)s
            AND
                tag_id = %(tag_id)s
            ;"""
    cursor.execute(query, {"question_id": question_id, "tag_id": tag_id})


@database_connection.connection_handler
def delete_all_question_tags_relation(cursor, question_id):
    query = """
              DELETE FROM question_tag
              WHERE 
                  question_id = %(question_id)s
              ;"""
    cursor.execute(query, {"question_id": question_id})


@database_connection.connection_handler
def get_user(cursor, username):
    query = """
            SELECT *
            FROM users
            WHERE username=%(username)s
            ;"""
    cursor.execute(query, {"username": username})
    return cursor.fetchone()


@database_connection.connection_handler
def get_all_users_questions(cursor):
    query = """
            SELECT username,   
            DATE(registration_date) AS registration_date,
            COUNT(question.id) AS questions,
            COUNT(answer.id) AS answers,
            COUNT(comment.id) AS comments
            FROM users
            INNER JOIN question on users.id = question.user_id
            INNER JOIN answer on users.id = answer.user_id
            INNER JOIN comment on users.id = comment.user_id
            GROUP BY username, DATE(registration_date)
            """
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def get_all_users_questions(cursor):
    query = """
            SELECT username,   
            DATE(registration_date) AS registration_date,
            COUNT(question.id) AS questions,
            COUNT(answer.id) AS answers,
            COUNT(comment.id) AS comments
            FROM users
            INNER JOIN question on users.id = question.user_id
            INNER JOIN answer on users.id = answer.user_id
            INNER JOIN comment on users.id = comment.user_id
            GROUP BY username, DATE(registration_date)
            """
    cursor.execute(query)
    return cursor.fetchall()


@database_connection.connection_handler
def insert_user(cursor, username, password):
    query = """
                INSERT INTO users(username, password)
                VALUES(%(username)s, %(password)s )
                ;"""
    cursor.execute(query, {"username": username, "password": password})


@database_connection.connection_handler
def get_comment_number(cursor, id_user):
    query = """
            SELECT 
                COUNT(comment.id) as number_of_comment
            FROM comment
            WHERE 
                comment.user_id = %(id_user)s
        ;"""
    cursor.execute(query, {"id_user": id_user})
    return cursor.fetchall()


@database_connection.connection_handler
def get_answer_number(cursor, id_user):
    query = """
            SELECT 
                COUNT(answer.id) as number_of_answers
            FROM answer
            WHERE user_id = %(id_user)s
        ;"""
    cursor.execute(query, {"id_user": id_user})
    return cursor.fetchall()


@database_connection.connection_handler
def get_question_number(cursor, id_user):
    query = """
            SELECT COUNT(question.id) as number_of_questions
            FROM question
            WHERE user_id = %(id_user)s
        ;"""
    cursor.execute(query, {"id_user": id_user})
    return cursor.fetchall()


@database_connection.connection_handler
def get_users(cursor):
    cursor.execute("select u.id, u.username from users u;")
    users = cursor.fetchall()
    print(users)
    cursor.execute("select count(c.id) as comment, c.user_id from comment c group by c.user_id;" )
    comments = cursor.fetchall()
    print(comments)
    cursor.execute("select count(a.id) as answer, a.user_id from answer a group by a.user_id;" )
    answers = cursor.fetchall()
    print(answers)
    cursor.execute("select count(a.id) as question, a.user_id from question a group by a.user_id;" )
    questions = cursor.fetchall()
    print(questions)
    for i, u in enumerate(users):
        comment = [ c.get("comment") for c in comments if c.get("user_id") == u.get("id") ]
        comment = comment.pop() if len(comment) else 0

        answer = [c.get("answer") for c in answers if c.get("user_id") == u.get("id")]
        answer = answer.pop() if len(answer) else 0

        question = [ c.get("question") for c in questions if c.get("user_id") == u.get("id") ]
        question = question.pop() if len(question) else 0

        users[i].update({
                "comments": comment,
                "answers": answer,
                "questions": question,
            })

    return users