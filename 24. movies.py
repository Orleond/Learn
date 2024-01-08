favorites_movie = {}
recommended_movie = {
    'Хэнкок': {'rating': 4.5, 'review': 'Смотреть можно'},
    'Матрица': {'rating': 4.7, 'review': 'Фильм крут'},
    'Кибер': {'rating': 2.5, 'review': 'Так себе киношечка'},
    'Трон': {'rating': 3.8, 'review': 'Так себе киношечка'},
    'Мстители': {'rating': 4.7, 'review': 'Фильм крут'},
    'Хакеры': {'rating': 4.5, 'review': 'Смотреть можно'},
}
low_rating = {}

for movie, value in recommended_movie.items():
    if value['rating'] < 4:
        print(f'Фильм {movie} не интересен: {value["review"]}. Фильм удален из рекомендаций')
        low_rating[movie] = value
    if value['rating'] > 4.5:
        print(f'У фильма {movie} хороший отзыв: {value["review"]}. Фильм добавлен в избранное')
        favorites_movie[movie] = value
for movie in low_rating:
    if movie in recommended_movie:
        del recommended_movie[movie]

print(favorites_movie)