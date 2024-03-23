-- create table; shouldn't fail if already exists first_table second_table

UPDATE second_table SET `score` = 10 WHERE `name` = Bob;
