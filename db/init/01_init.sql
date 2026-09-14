create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

<<<<<<< HEAD
create user if not exists 'bssmMrchoi'@'localhost' identified by 'q1w2e3';
create user if not exists 'appuser'@'%' identified by 'q1w2e3';

grant select, insert, update, delete on shopping_db.* to 'appuser'@'%';
=======
create user if not exists 'nada'@'localhost' identified by 'gun';
create user if not exists 'nada'@'%' identified by 'gun';

grant select, insert, update, delete on shopping_db.* to 'nada'@'%';
>>>>>>> joo
flush privileges;
