titles = ["Jawan", "Dangal", "Pathaan"]
genres = ["Action", "Sports", "Action"]
ratings = [7.0, 8.3, 5.8]

result = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    result.append(movie)

print(result)