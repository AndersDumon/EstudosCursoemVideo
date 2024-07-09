let num =[]
console.log(num)
num.push(4,5,6,7,8,9)
let p = 0
let maior = 0
let menor = 0
for (let c in num){
    //console.log(num[c])
    p +=num[c]
    if(c == 0){
        maior  = num[c]  
        menor = num[c]
    }else if (num[c] > maior ){
        maior = num[c]
    }else if(num[c] < menor){
        menor = num[c]
    }
}
console.log(`Nosso vetor: ${num}`)
console.log(`Ao todo temos ${num.length} valores cadastrados `)
console.log(`o maior numero é = ${maior}`)
console.log(`o menor numero é = ${menor}`)
console.log(`Somando todos os valores, temos ${p}`)
console.log(`a média dos valores é ${p/num.length}`)