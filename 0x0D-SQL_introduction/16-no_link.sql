-- create table; shouldn't fail if already exists first_table second_table

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
