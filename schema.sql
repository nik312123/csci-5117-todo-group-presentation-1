CREATE TYPE PRIORITY_T AS ENUM ('low', 'medium', 'high');

CREATE TABLE usr (
    email       VARCHAR(254) NOT NULL,
    first_name  VARCHAR(30)  NOT NULL,
    middle_name VARCHAR(30)  NULL,
    last_name   VARCHAR(30)  NOT NULL,
    profile_url VARCHAR(512) NOT NULL
);

CREATE TABLE task (
    id           SERIAL PRIMARY KEY,
    title        VARCHAR(30)  NOT NULL,
    description  VARCHAR(200) NOT NULL,
    due_datetime TIMESTAMP    NOT NULL,
    email        VARCHAR(254) NOT NULL,
    color        CHAR(6)      NOT NULL,
    priority     PRIORITY_T   NOT NULL,
    is_completed BOOLEAN      NOT NULL
);
