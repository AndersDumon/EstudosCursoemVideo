create table if not exists curso (
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2024'
) default charset=utf8;

describe cursos;

alter table cursos
add primary key (idcurso);


alter table cursos 
add column idcurso int first;