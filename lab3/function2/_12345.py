movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def first(movie_list):
    for movie in movie_list:  
        if movie["imdb"] >= 5.5:
            print(movie["name"])

#2
def second(movie_list):
    arr = []
    for movie in movie_list:  
        if movie["imdb"] >= 5.5:
            arr.append(movie["name"])
    print(arr)

#3
def third(movie_list, category):
    for movie in movie_list: 
        if movie["category"] == category:
            print(movie['name'])

#4
def fourth(movie_list):
    sum = 0
    for movie in movie_list: 
        sum += movie["imdb"]
    print(round(sum / len(movie_list),2))

#5
def fifth(movie_list, category):
    sum = 0
    count = 0
    for movie in movie_list: 
        if movie["category"] == category:
            sum += movie["imdb"]
            count += 1
    print(round(sum / count, 2))
