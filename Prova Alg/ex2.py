vogs = 'aeiou'


def comeca_vogs_ou_consoante ():
    lista_de_nomes = []
    while True:
        nome_user = str(input('Digite um nome (ou "Sair" para ver o resultado): ')).lower()
        if nome_user == "sair":
            print(tupla_final)
            print('Saindo! ...')
            break
        else:
            lista_de_nomes.append(nome_user)
        começa_vogal = [] 
        começa_consoante = []
        tupla_final = (começa_vogal, começa_consoante)
        for i in lista_de_nomes:
            if i[0] in vogs:
                começa_vogal.append(i)
            else:
                começa_consoante.append(i)






comeca_vogs_ou_consoante()