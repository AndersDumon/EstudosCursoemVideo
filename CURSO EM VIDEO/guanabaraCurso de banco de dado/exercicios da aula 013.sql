select * from gafanhotos where nacionalidade not like ('Brasil');
select profissao,count(*) from gafanhotos group by profissao; 
select sexo,nascimento,count(nascimento) from gafanhotos where nascimento >= '2005-01-01' group by sexo having sexo ; 
select nacionalidade,count(nacionalidade) from gafanhotos where nacionalidade not like ('Brasil')  group by nacionalidade having count(nacionalidade)>=3 ;
select avg(altura)from gafanhotos;
select * from gafanhotos where peso > 100;
select * from gafanhotos where altura >(select avg(altura)from gafanhotos);
select nome,peso,altura,count(*) from gafanhotos where peso>=100 group by altura having altura >(select avg(altura)from gafanhotos) order by altura desc;