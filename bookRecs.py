"""
Project 1 - Book Recommendations
Cody Behling
CS-1410-602

I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitutes cheating.
I will receive a zero on this project if I am found in violation of this policy.
"""

import operator

books = []
ratings = {}
similarities = {}

# read bookList.txt
with open('bookList.txt', 'r') as f:
    for line in f:
        books.append(line.strip().split(','))

# read ratings.txt
with open('ratings.txt', 'r') as f:
    while True:
        name = f.readline().strip().lower()
        if not name:
            break
        scores = f.readline().strip().split()
        ratings[name] = [int(score) for score in scores]


def dot_prod(x, y):
    assert(len(x) == len(y))
    theSum = 0
    for i in range(len(x)):
        theSum += x[i] * y[i]
    return theSum


def compute_scores():
    for name1 in ratings:
        for name2 in ratings:
            if name1 != name2:
                affinityScore = dot_prod(ratings[name1], ratings[name2])
                if affinityScore > 0:
                    similarities[name1] = similarities.get(name1, {})
                    similarities[name1][name2] = affinityScore


def friends(name):
    compute_scores()
    allFriends = similarities[f'{name}']
    topFriends = [name for name, _ in sorted(allFriends.items(), key=operator.itemgetter(1, 0), reverse=True)]
    return topFriends[:2]


def recommend(name):
    my_friends = friends(name)
    # get the recommendations from my_friends
    recommendations = []
    my_ratings = ratings[name]
    # compare the ratings against name's and add to a recommendations list
    # All books where the friend rate 3 or 5, and name rated 0
    for friend in my_friends:
        friend_ratings = ratings[friend]
        for i in range(len(friend_ratings)):
            if friend_ratings[i] >= 3 and my_ratings[i] == 0:
                book = ', '.join(books[i])
                if book not in recommendations:
                    recommendations.append(book)
    # sort recommendations
    return sorted(recommendations, key=aut_title)


def aut_title(book):
    aut = book[0].split()
    return aut[-1], aut[0], book[1]


def full_report():
    blankVariable = ""
    for name in ratings:
        twoFriends = friends(name)
        recommendations = recommend(name.lower().strip())
        blankVariable += f"Recommendations for {name} from {twoFriends[0]} and {twoFriends[1]}:\n"
        for printRecs in recommendations:
            blankVariable += f'\t{printRecs}\n'
    return blankVariable


def main():
    readerName = input("Enter a reader's name: ")
    if readerName not in ratings:
        print(f"No such reader {readerName}")
        return
    twoFriends = friends(readerName)
    recommendations = recommend(readerName.lower().strip())
    print(f"Recommendations for {readerName} from {twoFriends[0]} and {twoFriends[1]}:")
    for printRecs in range(len(recommendations)):
        print(f'\t{recommendations[printRecs]}')
    with open('recommendations.txt', 'w') as f:
        print(recommendations, file=f)


if __name__ == "__main__":
    main()
