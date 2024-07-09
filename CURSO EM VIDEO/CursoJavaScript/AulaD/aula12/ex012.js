var agora = new Date()
var hr = agora.getHours()
if (hr> 1){
console.log(`Agora são exatamente ${hr} horas.`)
}else{
    console.log(`Agora são exatamente ${hr} hora.`) 
}
if (hr< 12){
    console.log(`Bom dia!`)
}else if(hr >=12 && hr <=18){
    console.log(`Boa tarde!`)
}else{
    console.log(`Boa noite!`)
}