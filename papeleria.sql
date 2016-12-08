create database papeleria;
use papeleria;
create table login(
usuario varchar(50) not null,
contrasena varchar(50) not null);

create table productos(
id_articulo int not null primary key auto_increment,
articulo  varchar(70) not null,
existencia  int not null,
marca varchar(50) not null,
precioneto float(9,2) not null,
precioventa float(9,2) not null,
ganancia float(9,2) not null);

INSERT INTO `papeleria`.`login` (`usuario`, `contrasena`) VALUES ('lalo', 'lalo');
