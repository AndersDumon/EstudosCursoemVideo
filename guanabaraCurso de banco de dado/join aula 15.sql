select gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano 
from gafanhotos join cursos on cursos.idcurso = gafanhotos.cursopreferido;

select gafanhotos.nome,gafanhotos.cursopreferido,cursos.nome,cursos.ano
from gafanhotos inner join cursos on cursos.idcurso = gafanhotos.cursopreferido
order by gafanhotos.nome;

# as serve para dar apelido no nome 
select g.nome,g.cursopreferido,c.nome,c.ano
from gafanhotos as g join cursos as c on c.idcurso = g.cursopreferido order by g.nome;

# outer mostra tds : left lado esquerdo
select g.nome,g.cursopreferido,c.nome,c.ano
from gafanhotos as g left  join cursos as c on c.idcurso = g.cursopreferido ;

# outer mostra tds : rigth lado direito
select g.nome,g.cursopreferido,c.nome,c.ano
from gafanhotos as g right outer join cursos as c on c.idcurso = g.cursopreferido;