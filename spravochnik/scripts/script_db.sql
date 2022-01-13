--create nsi db
drop database if exists nsi ;
drop role nsi_user;

CREATE ROLE nsi_user WITH NOSUPERUSER LOGIN PASSWORD 'nsi';
comment on role nsi_user is 'пользователь НСИ';

create database nsi with owner nsi_user;

comment on database nsi is 'база тестового задания НСИ';