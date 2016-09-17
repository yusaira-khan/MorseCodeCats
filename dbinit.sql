drop database if exists morsecode;
create DATABASE MORSECODE;
set database= morsecode;
Create table mini ( code STRing(3) , ascii String(1) Primary key);
Create table numbers ( code STRing(5) , ascii String(1) Primary key);
create table words (id int Primary key,spelling String );
insert into mini values ('...','s'),('---','o'),('..-','u'),('-..','d'),('-.-','k'),('.--','w');
-- ('---','o'),('..-','u'),('-..','d'),('-.-','k'),('.--','w');
