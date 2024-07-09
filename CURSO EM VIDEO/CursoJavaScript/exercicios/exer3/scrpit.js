function contar(){
    var pri = document.getElementById('a')
    var seg = document.getElementById('b')
    var ter = document.getElementById('c')
    var res = document.querySelector('div#res')
    if (pri.value.length == 0 || seg.value.length == 0 || ter.value.length == 0){
        window.alert('[erro] Faltam dados!')
        res.innerHTML ='🙎🏿‍♂️ Impossivel contar 🤷🏻‍♀️'
    }else{
    res.innerHTML = 'Contando: <br>'
    var a  = Number(pri.value)
    var b = Number(seg.value)
    var c = Number(ter.value)
    if(c <= 0){
        window.alert('Passo Inválido! Irei considerar como  Passo = 1')
        c = 1
    }
    if (a < b){
    while (a <=b){
        res.innerHTML +=`${a} \u{1F449}	`
        a+=c
    }
    }else{
        while (a >=b ){
            res.innerHTML += `${a} \u{1F449}`
            a-=c
        }
    }
    res.innerHTML += '🏁 Fim! 🏴'
}
}