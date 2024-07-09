select *from cursos where nome = 'PHP';

select*from cursos where nome like 'p%'; #todos os registros que começam com p

select* from cursos where nome like '%a'; #todos os registros que terminam com a

select* from cursos where nome like '%n%'; #todos os registros com n

select* from cursos where nome not like '%n%'; # todos os registros que não são com n

update cursos set nome = 'PáOO' where idcurso = '9';

select* from cursos where nome like '%a%';

UPDATE `cadastro`.`cursos` SET `nome` = 'POO' WHERE (`idcurso` = '9');

select* from cursos where nome like 'ph%p%'; # dois coringas = % ou _

select* from cursos where nome like 'p_p%';# corigas = _ ou %
