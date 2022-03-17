class movie():
    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def insert_likes(self):
        self.likes += 1


class series():
    def __init__(self, name, year, seasons):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def insert_likes(self):
        self.likes += 1

objeto01 = movie("O homem aranha", 2022, 120)
objeto01.insert_likes()
objeto01.insert_likes()
print('Nome do filme: {}. Ano: {}. Tempo de duração em minutos: {} min.'.format(objeto01.name, objeto01.year,
                                                                                objeto01.duration))



objeto02 = series("La casa del papel", 2018, 5)
objeto02.insert_likes()
print('Nome da série: {}. Ano de início: {}. Número de temporadas: {}.'.format(objeto02.name, objeto02.year,
                                                                               objeto02.seasons))



