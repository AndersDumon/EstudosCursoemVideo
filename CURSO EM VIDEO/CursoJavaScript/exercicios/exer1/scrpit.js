function carregar(){    //função oque será feito
var msg = window.document.getElementById('msg') //pegando a variavel obj mensagem
var img = window.document.getElementById('imagen') //pegando a variavel obj imagen
var data = new Date() //criando obj hora do sistema
var hora = data.getHours() // criando  obj hora do sistema ou input
//var hora = 22;// input forçado da hora
msg.innerHTML = `Agora são ${hora} horas,`//print
if (hora >= 0 &&  hora < 12){
    msg.innerHTML += ' Bom Dia!'
    img.src="imagens/manhã.png" 
    document.body.style.background = '#e2cd9f'
}else if (hora >=12 && hora <18){
    msg.innerHTML += ' Boa Tarde!'
    img.src="imagens/tarde.png" 
    document.body.style.background = '#b9845f'
}else{
    msg.innerHTML += ' Boa Noite!'
    img.src="imagens/noite.png" 
    document.body.style.background = '#515154'
}
}