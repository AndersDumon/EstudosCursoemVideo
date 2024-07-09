function mult(){
    var mut = document.getElementById('valor')
    var tab = document.getElementById('re')
    if (mut.value.length == 0){
        window.alert('[ERRO] Por favor, digite um número!')
    }else{
    var valor = Number(mut.value)}
    re.innerHTML = `Tabuada do ${valor} `
    var c = 1
    var r = 1
    tab.innerHTML =''
    for(c ;c <=10;c++){
        var item = document.createElement('option')
        var r = c*valor
        item.text = `${valor}X ${c} = ${r} `
        item.value = 'tab${valor}'
        tab.appendChild(item)
    }
}