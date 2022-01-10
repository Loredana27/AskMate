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



