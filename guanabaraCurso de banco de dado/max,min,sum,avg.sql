select count(*) from cursos;
select count(*) from cursos where carga >40; 

select max(carga) from cursos;
select * from cursos where ano = '2016';
select max(totaulas) from cursos where ano = '2016';

select min(totaulas) from cursos where ano = '2016';
select nome, min(totaulas) from cursos where ano = '2016';

select sum(totaulas) from cursos;

select avg (totaulas) from cursos;