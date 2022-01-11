create table tag
(
    id   serial
        constraint pk_tag_id
            primary key,
    name text
);


create table users
(
    id                serial
        constraint users_pk
            primary key,
    username          text,
    password          text,
    registration_date timestamp default CURRENT_TIMESTAMP
);



create table question
(
    id              serial
        constraint pk_question_id
            primary key,
    submission_time timestamp default CURRENT_TIMESTAMP,
    view_number     integer   default 0,
    vote_number     integer   default 0,
    title           text,
    message         text,
    image           text      default ''::text,
    user_id         integer
        constraint question_users_id_fk
            references users
);



create table answer
(
    id              serial
        constraint pk_answer_id
            primary key,
    submission_time timestamp default CURRENT_TIMESTAMP,
    vote_number     integer   default 0,
    question_id     integer
        constraint fk_question_id
            references question,
    message         text,
    image           text      default ''::text,
    user_id         integer
        constraint answer_users_id_fk
            references users,
    accepted        boolean
);


create table comment
(
    id              serial
        constraint pk_comment_id
            primary key,
    question_id     integer
        constraint fk_question_id
            references question,
    answer_id       integer
        constraint fk_answer_id
            references answer,
    message         text,
    submission_time timestamp default CURRENT_TIMESTAMP,
    edited_count    integer   default 0,
    user_id         integer
        constraint comment_users_id_fk
            references users
);


create table question_tag
(
    question_id integer not null
        constraint fk_question_id
            references question,
    tag_id      integer not null
        constraint fk_tag_id
            references tag,
    constraint pk_question_tag_id
        primary key (question_id, tag_id)
);

INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id, accepted) VALUES (2, '2017-04-25 14:42:00.000000', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg', 1, null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id, accepted) VALUES (1, '2017-04-28 16:49:00.000000', 4, 1, 'You need to use brackets: my_list = []', null, 1, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (2, null, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00.000000', 0, 1);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (1, 0, null, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00.000000', 0, 1);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (2, '2017-05-01 10:41:00.000000', 1364, 57, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', null, null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (3, '2022-01-10 15:09:01.775544', 0, 0, 'hdhd', 'hedyrtu', '', 1);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (0, '2017-04-28 08:29:00.000000', 29, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', null, 1);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (1, '2017-04-29 09:19:00.000000', 15, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png', 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (0, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 3);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 3);
INSERT INTO public.tag (id, name) VALUES (1, 'python');
INSERT INTO public.tag (id, name) VALUES (2, 'sql');
INSERT INTO public.tag (id, name) VALUES (3, 'css');
INSERT INTO public.users (id, username, password, registration_date) VALUES (3, 'loredanastefania1227@gmail.com', '$2b$12$yAW5I9h2jy7o7iVpNwgVf.rGQ3v50UpU//6SByfYZ9bJ0TGCed9Cu', '2022-01-10 12:15:26.700693');
INSERT INTO public.users (id, username, password, registration_date) VALUES (2, 'loredsna', '$2b$12$rD6ChBN54RHLDhUEWXSWN.NhOpPrIwtX0oktHeFSilmiodZXtpv9i', '2022-01-10 14:58:44.277744');


