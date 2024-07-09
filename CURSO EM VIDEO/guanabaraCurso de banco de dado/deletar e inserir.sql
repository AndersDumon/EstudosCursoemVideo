update cursos
set ano	= '2018', carga = '0'
where ano = '2050'
limit 1;

delete from cursos
where idcurso='8';

delete from cursos
where ano ='2050'
limit 2;