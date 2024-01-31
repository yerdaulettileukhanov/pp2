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
def movie(a):
    for i in range(len(movies)):
        if movies[i]["name"] == a:
            if movies[i]["imdb"] > 5.5:
                return True
    return False

m = input("Movie name: ")
print(movie(m))

#2
def movieList():
    l = []
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            l.append(movies[i])
    return l

print(movieList())

#3
def category(a):
    for i in range(len(movies)):
        if movies[i]["category"] == a:
            print(movies[i])

a = input("Category name: ")
category(a)

#4
def average(a):
    cnt = 0
    for i in range(len(movies)):
        if movies[i]["name"] in a:
            cnt += movies[i]["imdb"]
    return round(cnt / len(a), 1)

n = int(input())
l = []

for i in range(n):
    b = input()
    l.append(b)

print(average(l))

#5
def averageCategory(a):
    cnt = 0
    cnt1 = 0
    for i in range(len(movies)):
        if movies[i]["category"] == a:
            cnt += movies[i]["imdb"]
            cnt1 += 1
    return round(cnt / cnt1, 1)

b = input()

print(averageCategory(b))