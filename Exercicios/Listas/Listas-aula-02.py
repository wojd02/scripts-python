conjunto = []
dado = []
for c in range (0,3):
    dado.append(str(input('Nome paciente: ')))
    dado.append(int(input('Idade paciente: ')))
    conjunto.append(dado[:])
    dado.clear()
print(conjunto)
for p in conjunto:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade, {p[1]} anos')

print(conjunto[0][1])
print(conjunto[1][0]) #printar carla
print(conjunto[0][0]) #printar matheus
print(conjunto[2][1]) #printar 22