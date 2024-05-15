musicas = [
    ("musica 1","rock"),
    ("musica 2","pop"),
    ("musica 3","jazz"),
    ("musica 4","rock"),
    ("musica 5","pop"),
    
]

#histórico de músicas ouvidas pelo usúario
historico_usúario = ["rock","jazz","pop","jazz","pop"]

#função para recomendar musícas 
def recomendar_musica (histórico):
    #contar a frequencia de cada genero histórico
    frequencia = {}
    for genero in histórico:
        if genero in frequencia
              frequencia[genero]+= 1
              else:
                frequencia[genero] = 1

            # encontrar o genero mais frequente
            genero_mais_frequente = max(frequencia, key=frequencia.get)

            #recomendar musícas desse genero
            recomendaçoes = []
            for titulo, genero in musicas:
                if genero == genero_mais_frequente:
                    recomendaçoes.append(titulo)
            return recomendacoes

        #obter recomendações para o usúario
        recomendaçõ
        es_usuario = recomendar_musica(hitorico_usuario)
        print("musicas recomendadas:", recomendações_usuario)
        
           

