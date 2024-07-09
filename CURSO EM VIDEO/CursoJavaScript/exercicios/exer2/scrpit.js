function verificar(){
   // window.alert('Funcionou!') //para testar
   var data = new Date()  // input na data
   var ano = data.getFullYear() //  fullyear ele ira pegar com 4 digitos o ano atual
   var fano = document.getElementById('txtano') //irá pegar da caixa de texto (id=1°)
   //var res = document.getElementById('res') // de um jeito
    var res = document.querySelector('div#res') // de outro jeito (div = local, res = var)
    if (fano.value.length == 0 || Number(fano.value) > ano){
        window.alert('[ERRO]')
        window.alert('Verifique novamente os daddos e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value) // decobrindo a idade
        //res.innerHTML = `Idade calculada ${idade}`// teste
        var genero =''
        var img = document.createElement('img')// criando elemento ou var img
        img.setAttribute('id','img') //a msm coisa de ir no html e fazer na div <img id='foto'>
        if (fsex[0].checked){ /*se o masc for marcado faça*/
            genero = 'Homem'
            if (idade <= 10){
                //criança
                img.setAttribute('src','imagens/criahomem.png')
            }else if (idade <=21){
                //adolescente
                img.setAttribute('src','imagens/adolhomem.png')
            }else if (idade <= 50){
                //adulto
                img.setAttribute('src','imagens/aduhomem.png')
            }else{
                //idoso
                img.setAttribute('src','imagens/idosohomem.png')
            }
        }else if(fsex[1].checked){/*se o femi for marcado faça*/
            genero = 'Mulher'
            if (idade <=10){
                // criança
                img.setAttribute('src','imagens/criamulher.png')
            }else if (idade <=21){
                //adolescente
                img.setAttribute('src','imagens/adolmulher.png')
            }else if (idade <=50){
                //adulta
                img.setAttribute('src','imagens/adumulher.png')
            }else{
                //idosa
                img.setAttribute('src','imagens/idosamulher.png')
            }
        }
        res.style.textAlign = 'center'/*centralizar*/
        res.innerHTML = `${genero} com a idade de ${idade} anos.` /*print*/
        res.appendChild(img)//adicionando a imagem e dando print
        
    }


}
 /*se o masc for marcado faça*/