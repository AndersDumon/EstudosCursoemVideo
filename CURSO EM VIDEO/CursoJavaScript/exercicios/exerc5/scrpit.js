let num = document.querySelector('input#valor')
let lista = document.querySelector('select#flista')
let res = document.querySelector('div#res')
let vet = []

function isNumero(n){
    if(Number(n) >= 1 && Number(n)<=100){
        return true
    }else{
        return false
    }
}
function inlista(n, l){
    if (l.indexOf(Number(n)) != -1){
        return true
    }else{
        return false
    }

}

function add(){
    if(!inlista(num.value,vet) && isNumero(num.value)){
        vet.push(Number(num.value))   
        let item=document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        lista.appendChild(item)
        res.innerHTML=''
    }else{
        window.alert('[ERRO] Valor invalido ou já encontrado, digite novamente!')
    }
    num.value = ''
    num.focus()
}
function final(){
    if (vet.length > 0){
    let p = 0
    let maior = 0
    let menor = 0
    for (let c in vet){
    p +=vet[c]
    if(c == 0){
        maior  = vet[c]  
        menor = vet[c]
    }else if (vet[c] > maior ){
        maior = vet[c]
    }else if(vet[c] < menor){
        menor = vet[c]
    }
}
res.innerHTML =''
res.innerHTML += `<p>Nosso vetor: [${vet}] <br></p>`
res.innerHTML += `<p>Ao todo temos ${vet.length} valores cadastrados <br></p> `
res.innerHTML += `<p>O maior numero é = ${maior} <br></p>`
res.innerHTML += `<p>O menor numero é = ${menor} <br></p>`
res.innerHTML +=`<p>Somando todos os valores, da ${p} <br></p>`
res.innerHTML += `<p>A média dos valores é ${p/vet.length} <br></p>`
}else{
    window.alert('[ERRO]Você deve adicionar um valor primeiro!')
}
}

    
