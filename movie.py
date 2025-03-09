import requests
try:
    key = "87e06f54"
    search = input ("search for movie: ").title()
    url = f"http://www.omdbapi.com/?t={search}&apikey={key}"

    def movies(search):
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            my_movie = {
                "Title" : data['Title'],
                "Year" : data['Year'],
                "Plot" :data['Plot']
            }
            if my_movie:
                print (f"Title : {my_movie['Title']}")
                print (f"Year of release: {my_movie['Year']}")
                print (f"Plot: {my_movie['Plot']}")
            return "Movie not found"
    
    movies("search")
except KeyError as error:
    print (error)
    print ("movie title is invalid")

