movies = [
    {  "Name": "Inception",
        "Year": "2010",
        "Rating": "8.7",
    },
    {
        "Name": "Inside Out",
       "Year": "2015",
       "Rating":"8.1",

    },
    {
        "Name" : "Con Air",
       "Year": "1997",
       "Rating": "6.9"
    }
]

def legg_til_movie(movieliste, name,year,rating=5.0):
    ny_movie = {
        "Name": name,
        "Year": year,
        "Rating": rating
    }
    movieliste.append(ny_movie) 


legg_til_movie(movies, "Sleeping Dogs",2012,4.8)
legg_til_movie(movies,"It Ends with US",2024,3.5)
legg_til_movie(movies,"After",2019,5.3)
legg_til_movie(movies,"Spirit",2012)

print(movies)