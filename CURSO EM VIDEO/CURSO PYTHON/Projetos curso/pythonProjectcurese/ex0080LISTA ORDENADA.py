l = []
for c in range(0,5):
  n = int(input('digite um valor'))
  if c == 0 or n > l [-1]:
    l.append(n)
    print('Adiciona ao final da lista!')
  else:
    pos = 0
    while pos < len(l):
      if n <= l[pos]:
        l.insert(pos,n)
        print(f'Adicionado  na posição {pos} da lista')
        break
      pos += 1
  print(l)

print(f'LISTA COMPLETA: {l}')