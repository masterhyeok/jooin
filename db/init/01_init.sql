create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

create user if not exists 'nada'@'localhost' identified by 'gun';
create user if not exists 'nada'@'%' identified by 'gun';

grant select, insert, update, delete on shopping_db.* to 'nada'@'%';
flush privileges;
