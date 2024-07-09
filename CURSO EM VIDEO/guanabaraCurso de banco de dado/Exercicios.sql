select*from gafanhotos;
select* from gafanhotos where sexo = 'F';
select* from gafanhotos where nascimento between '2000-01-01' and '2015-12-31' order by nascimento;
select id , nome , profissao,sexo from gafanhotos where profissao = ('programador') and sexo = ('m');
select* from gafanhotos where sexo ='f'and nacionalidade = ('Brasil') and nome  like 'j%';
select nome, nacionalidade,peso from gafanhotos where sexo = 'm' and nacionalidade not like 'Brasil' and peso < 100 ;
select avg(altura) from gafanhotos where sexo = 'm' and nacionalidade = 'Brasil';
select avg(peso)from gafanhotos;
select min(peso) from gafanhotos 
where sexo = 'f' and nacionalidade not like 'Brasil' and nascimento between '1990-01-01' and '2000-12-31' ;
select count(*) from gafanhotos where sexo = 'f' and altura >= 1.90