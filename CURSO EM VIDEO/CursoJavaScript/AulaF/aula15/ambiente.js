let num = [5,8,9,3]
console.log(num)
console.log(`nosso vetor é ${num}`)
console.log(`o vetor tem ${num.length} variaveis`)
console.log(num[0])
console.log(num[1],num[2],num[3])
num.sort()
console.log(num)
for(var c= 0;c<num.length;c++ ){
    console.log(`o valor na posição ${c} é ${num[c]}`)
}
console.log(`------------------------------------------`)
num.push(5)
num.push(2)
for(let pos in num ){
    console.log(`o valor na posição ${pos} é ${num[pos]}`)
}
let pos =num.indexOf(9)
console.log( `o valor 9 está na posição ${pos}`)