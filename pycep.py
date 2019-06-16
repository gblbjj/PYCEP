def consulta_cep(cep):
    import requests
    url = 'https://viacep.com.br/ws/%s/json/'%cep
    response = requests.get(url)
    #print (response.content)
    response_json = (response.json())
    logradouro = response_json['logradouro']
    localidade = response_json['localidade']
    return logradouro, localidade

if __name__ == '__main__':
    logradouro, localidade = consulta_cep('06330000')
    print (logradouro)
    print (localidade)    