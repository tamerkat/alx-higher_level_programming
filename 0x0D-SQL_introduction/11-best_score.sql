-- create table; shouldn't fail if already exists first_table second_table

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
