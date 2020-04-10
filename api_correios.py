import pycep_correios
import json5

x = str(input('digite seu cep:'))


while len(x) != 8:
    print('Numero de caracteres invalidos, favor digite novamente com atencao')
    x = str(input('digite seu cep: \n'))



endereco = pycep_correios.get_address_from_cep(x)
busca = json5.loads(endereco)

# print(busca['bairro'])
# print(busca['cidade'])
# print(busca['logradouro'])
# print(busca['uf'])



print('oque deseja saber sobre esse cep:')
print(' 1 bairro  - 2 cidade - 3 nome da rua - 4 estado - 5 todos')
escolha = input('Digite sua escolah aqui: \n')

if escolha == '1':
    print(busca['bairro'])
elif escolha == '2':
    print(busca['cidade'])
elif escolha == '3':
    print(busca['logradouro'])
elif escolha == '4':
    print(busca['uf'])
elif escolha == '5':
    print(busca['bairro'])
    print(busca['cidade'])
    print(busca['logradouro'])
    print(busca['uf'])
else:
    print('opção invalida')
