# your code goes here
the_file = open('scores.txt')

restaurant_ratings = {}

for line in the_file:
    line = line.rstrip().split(":")

    restaurant_ratings[line[0]] = line[1]

the_file.close()

restaurant_ratings = restaurant_ratings.items()
restaurant_ratings.sort()

for restaurant, rating in restaurant_ratings:
    print '{} is rated {}'.format(restaurant, rating)