programa
{
	
	funcao inicio()
	{	
	     inteiro n1
	     inteiro n2
		cadeia ni
		escreva("Digite o seu nome: ")
		leia(ni)
		se(ni == "Anderson"){
		escreva("Olá ",ni)
		escreva(" Agora digite um numero: ")
		leia(n1)
		escreva("Bom, Agora digite outro numero: ")
		leia(n2)
		inteiro s = n1+n2
		escreva("A soma dos valores é ", s)
		}senao{
			escreva("Você não é o dono!")
			}
		}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 270; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */