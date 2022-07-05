import matplotlib.pyplot as plt
import csv

def grafico_linha():
    def filtrar_dados():
        lista_filtrada_pais = []
        lista_filtrada_tipo = []
        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if pais == row[7]:
                    lista_filtrada_pais.append(row)
            for i in lista_filtrada_pais:
                if tipo_de_olimpiada == i[10]:
                    lista_filtrada_tipo.append(i)
            return lista_filtrada_tipo

    def ordenar_dados(args, args2):
        lista_ordenada = []
        args2.sort(key=lambda x: x[9])
        for i in args2:
            if args == 0:
                break
            lista_ordenada.append(i)
            try:
                if i[9] == args2[args2.index(i) + 1][9]:
                    continue
            except:
                None
            args = args - 1
        return (lista_ordenada)

    def primeirosAnos(args):
        primeiros_anos = []
        for row in args:
            if row[9] not in primeiros_anos:
                primeiros_anos.append((row[9]))
        return primeiros_anos

    def dicionario(args):
        ano_medalhas = dict()
        for i in primeirosAnos(ordenar_dados(x_primeiras, filtrar_dados())):
            for j in args:
                if i in j:
                    ano_medalhas[i] = ano_medalhas.get(i, 0) + 1
        for i in primeirosAnos(ordenar_dados(x_primeiras, filtrar_dados())):
            if i not in ano_medalhas.keys():
                ano_medalhas[i] = 0
        return ano_medalhas

    def medalhasBronze(args):
        lista_Bronze = []
        eventos_passados = []
        ano_medalhas = dict()
        for row in args:
            if 'Bronze' == row[14] and (row[13] not in eventos_passados):
                lista_Bronze.append(row)
                eventos_passados.append(row[13])

        return lista_Bronze

    def medalhasSilver(args):
        lista_Silver = []
        eventos_passados = []
        ano_medalhas = dict()
        for row in args:
            if 'Silver' == row[14] and (row[13] not in eventos_passados):
                lista_Silver.append(row)
                eventos_passados.append(row[13])

        return lista_Silver

    def medalhasGold(args):
        lista_Gold = []
        eventos_passados = []
        ano_medalhas = dict()
        for row in args:
            if 'Gold' == row[14] and (row[13] not in eventos_passados):
                lista_Gold.append(row)
                eventos_passados.append(row[13])

        return lista_Gold

    def dicionarioLista(args):
        lista = []
        for i, j in args.items():
            lista.append([i, j])
        lista.sort(key=lambda x: x[0])
        return lista

    def valoreslista(args):
        lista = []
        for i, j in args:
            lista.append(j)
        return lista

    def keyslista(args):
        lista = []
        for i, j in args:
            lista.append(i)
        return lista

    def gerar_grafico(x, y, a, b, c, d):
        plt.plot(x, y, 'p', color='brown')
        plt.plot(x, y, color='brown')
        plt.plot(a, b, 's', color='grey')
        plt.plot(a, b, color='grey')
        plt.plot(c, d, '*', color='y')
        plt.plot(c, d, color='y')
        line1, = plt.plot([], label='Bronze', color='brown')
        line2, = plt.plot([], label='Silver', color='grey')
        line3, = plt.plot([], label='Gold', color='y')

        plt.legend(handles=[line1, line2, line3], shadow=True)
        plt.title('Olimpíadas ' + pais)
        plt.xlabel('Years')
        plt.ylabel('Medals')
        plt.show()

    pais = str(input('Informe o pais:')).upper()
    x_primeiras = int(input('Quantas primeiras olimpiadas:'))
    tipo_de_olimpiada = str(input('Qual tipo de olimpiada:')).title()
    print('Aguarde um momento...')

    y_bronze = valoreslista(
        dicionarioLista(((dicionario(medalhasBronze(ordenar_dados(x_primeiras, filtrar_dados())))))))

    y_silver = valoreslista(
        dicionarioLista(((dicionario(medalhasSilver(ordenar_dados(x_primeiras, filtrar_dados())))))))

    y_gold = valoreslista(dicionarioLista(((dicionario(medalhasGold(ordenar_dados(x_primeiras, filtrar_dados())))))))

    x_bronze = keyslista(dicionarioLista(((dicionario(medalhasBronze(ordenar_dados(x_primeiras, filtrar_dados())))))))

    x_silver = keyslista(dicionarioLista(((dicionario(medalhasSilver(ordenar_dados(x_primeiras, filtrar_dados())))))))

    x_gold = keyslista(dicionarioLista(((dicionario(medalhasGold(ordenar_dados(x_primeiras, filtrar_dados())))))))

    return gerar_grafico(x_bronze, (y_bronze), x_silver, (y_silver), x_gold, (y_gold))


def grafico_barras():
    def filtrar_arquivo(x_ultimas,tipo_de_olimpiada):
        lista_anos = []
        lista_filtrada_M = []
        lista_filtrada_F = []
        lista_anos_string=[]

        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if tipo_de_olimpiada == row[10]:
                    lista_anos.append(int(row[9]))
        lista_anos = sorted(set(lista_anos), reverse=True)
        lista_anos = lista_anos[:x_ultimas]
        for i in lista_anos:
            lista_filtrada_M.append(lipar_A(i)[0])
            lista_filtrada_F.append(lipar_A(i)[1])
        for i in lista_anos:
            lista_anos_string.append(str(i))
        
        
        
        return lista_filtrada_M, lista_filtrada_F,lista_anos_string

    def lipar_A(ano):
        listaM = []
        listaF = []
        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if row[2] == 'M' and int(row[9]) == ano:
                    listaM.append(int(row[0]))
                elif row[2] == 'F' and int(row[9]) == ano:
                    listaF.append(int(row[0]))
            listaM = sorted(set(listaM))
            listaF = sorted(set(listaF))
        return len(listaM),len(listaF)

    def gerar_grafico(x,y,a,b):
        line1, = plt.plot([], label='Homens',color='#F4A460')
        line2, = plt.plot([], label='Mulheres',color='#836FFF')

        plt.legend(handles=[line1, line2],shadow=True)
        plt.bar(x ,y,width=-0.3,align='edge',color='#F4A460')
        plt.bar(a ,b,width=0.3,align='edge',color='#836FFF')
        plt.ylabel('Sexo')
        plt.xlabel('Ano')
        plt.title('Gráfico Barras(B2)')
        plt.show()
    x_ultimas = int(input('Quantas ultimas olimpiadas:'))
    tipo_de_olimpiada = str(input('Qual tipo de olimpiada:')).title()
    print('Aguarde um momento...')
    dados=filtrar_arquivo(x_ultimas,tipo_de_olimpiada)
    return gerar_grafico(dados[2],dados[0],dados[2],dados[1])

def pergunta_T10():
    def filtrar_arquivo():
        lista_filtrada_tipo = []
        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if cidade == row[11] and 'F' == row[2]:
                    lista_filtrada_tipo.append(int(row[0]))

        lista_filtrada_tipo = sorted(set(lista_filtrada_tipo))

        if len(lista_filtrada_tipo) == 0:
            print(cidade)
            return 'Cidade nao encontrada!'
        else:
            return f'A cidade de {cidade} teve {len(lista_filtrada_tipo)} mulheres participando.'

    cidade = str(input('Informe a cidade:'))

    return filtrar_arquivo()

def pergunta_T11():
    def filtrar_arquivo():
        lista_filtrada_tipo = []
        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if cidade == row[11] and esporte == row[12]:
                    lista_filtrada_tipo.append(int(row[0]))

        lista_filtrada_tipo = sorted(set(lista_filtrada_tipo))

        if len(lista_filtrada_tipo) == 0:
            return 'Cidade ou esporte nao encontrados!'
        else:
            return f'A cidade de {cidade} teve {len(lista_filtrada_tipo)} atletas na modalidade de {esporte}.'

    cidade = str(input('Informe a cidade:'))
    esporte = str(input('Informe o esporte:'))

    return filtrar_arquivo()


def grafico_boxplot():
    evento=input('Digite o nome do evento:')
    x_ultimas=int(input('Digite quantas ultimas olimpiadas:'))
    tipo_de_olimpiada=input('Digite o nome do tipo de olimpiada:').title()
    print('Aguarde um momento...')
    def filtrar_arquivo():
        lista_anos=[]
        lista_anos_string=[]
        lista_ordenada=[]
        with open(r'athlete_events.csv') as csvfile:
            reader=csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if evento==row[13] and tipo_de_olimpiada==row[10]:
                    lista_anos.append(int(row[9]))

                    
        lista_anos = sorted(set(lista_anos), reverse=True)
        lista_anos = lista_anos[:x_ultimas]
        for i in lista_anos:
            lista_ordenada.append(lipar_A(i))
        for i in lista_anos:
            lista_anos_string.append(str(i))
        
            
        return lista_ordenada,lista_anos_string

    def lipar_A(ano):
        lista_idades=[]
        lista_id=[]
        with open(r'athlete_events.csv') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if int(row[9]) == ano and row[0] not in lista_id:
                    lista_id.append(row[0])
                    try:
                        lista_idades.append(int(row[3]))
                    except:
                        None
            lista_idades = sorted((lista_idades))
        return (lista_idades)
    

    def gerar_grafico(lista_idades,lista_anos):
        data = lista_idades
        anos=lista_anos
        plt.boxplot(data,labels=anos)
        plt.ylabel('Idades')
        plt.xlabel('Ultimos Anos')
        plt.show()
    arquivo=filtrar_arquivo()
    
    return gerar_grafico(arquivo[0],arquivo[1])



def menu():
    while True:
        print('0-Sair\n'
              '1-(L4)Desempenho do <País> nas primeiras <X> olimpíadas de <Tipo de Olimpíada>.\n'
              '2-(B2)Quantidade de homens e mulheres das últimas <X> olimpíadas de <Tipo de Olimpíada>, separados por sexo.\n'
              '3-(X15)Idade dos atletas do <Evento> nas últimas <X> olimpíadas de <Tipo de Olimpíada>.\n'
              '4-(T10)Quantas mulheres participaram da Olimpíada de <Cidade>?\n'
              '5-(T11)Quantos atletas participaram da modalidade <Esporte> na Olimpíada de <Cidade>?')
        opcao = input('Opção:')
        if opcao == '0':
            break
        elif opcao == '1':
            grafico_linha()
        elif opcao == '2':
            grafico_barras()
        elif opcao == '3':
            grafico_boxplot()
        elif opcao == '4':
            print(pergunta_T10())
        elif opcao == '5':
            print(pergunta_T11())

        else:
            print('Informe um valor válido')
            continue



menu()








