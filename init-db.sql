CREATE DATABASE IF NOT EXISTS bankmole;
USE bankmole;

CREATE TABLE IF NOT EXISTS
users(
    id             INTEGER UNIQUE NOT NULL,
    login          TEXT NOT NULL,
    money_amount   INTEGER NOT NULL,
    card_number    TEXT NOT NULL,
    status         BIT(1)  NOT NULL
);

CREATE TABLE IF NOT EXISTS
passwords(
    id             INTEGER UNIQUE NOT NULL,
    password       TEXT NOT NULL
);

REPLACE INTO users VALUES
        (1, 'admin',             50,     '4485415276100340',   b'1'),
        (2, 'Alexey',            179,    '5249360526294911',   b'0'),
        (3, 'Maria',             210,    '4539113610370481',   b'1'),
        (4, 'Petya',             7,      '345203422952873',    b'1'),
        (5, 'Nikola',            0,      '6011693356565974',   b'0'),
        (6, 'SUPER_HACKER_1337', 999999, '1234567890123456',   b'0')
;
REPLACE INTO passwords VALUES
        (1, 'password'),
        (2, 'iloveyou'),
        (3, 'princess'),
        (4, '123123123'),
        (5, '000000000'),
        (6, 'rockyou')
;