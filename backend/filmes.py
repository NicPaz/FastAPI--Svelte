import requests


api_key = "8f7bbe02620a3b00e2e842d70eb66d77"

genres = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]



#busca nome do gênero fornecido o id
def get_genero_id(id):
    ids = []
    names = []
    if type(id) == list:
        ids = id
    else:
        ids.append(id)
    for genre in genres:
        if genre['id'] in ids:
            names.append(genre)
    return names

def get_json(endpoint, params=None):
    url = f"{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()


#busca um filme pelo título
def get_movie(palavra):
    data = get_json(f"https://api.themoviedb.org/3/search/movie?query={palavra}&include_adult=false&language=en-US")
    return data

#fornecdio o nome do artista retorna sua bio
def get_artista(nome: str):
    data = get_json(f"https://api.themoviedb.org/3/search/person?query={nome}&include_adult=false&language=en-US"
    )
    return data

if __name__ == "__main__":
     print(get_movie("titanic"))

# Obter o nome dos generos
# 
#end = f"https://api.themoviedb.org/3/genre/movie/list"
#params = "?language=en"
#url = f"{end}{params}&api_key={api_key}"

# imprimir os filmes (titulo) e o nome dos generos
