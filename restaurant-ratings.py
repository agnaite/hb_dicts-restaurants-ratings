# your code goes here
import random

the_file = open('scores.txt')

restaurant_ratings = {}

for line in the_file:
    line = line.rstrip().split(":")

    restaurant_ratings[line[0]] = line[1]

the_file.close()

# new_restaurant = raw_input("Enter new restaurant here: ")
# new_score = int(raw_input("Enter new score here: "))

# restaurant_ratings[new_restaurant] = new_score

name = raw_input("Hi, what is your name?")
print "Hello %s!" % (name)

while True:

    random_number = random.randint(0, len(restaurant_ratings)-1)
    random_restaurant = restaurant_ratings.keys()[random_number]

    print "{}'s current rating is: {}".format(random_restaurant, restaurant_ratings[random_restaurant])
    user_rating = raw_input("Enter new rating: ")

    if user_rating == 'q':
        break

    restaurant_ratings[random_restaurant] = user_rating


#this turns the dictionary into a list of tuples and sorts it and prints the restaurant and ratings

restaurant_ratings = restaurant_ratings.items()
restaurant_ratings.sort()

for restaurant, rating in restaurant_ratings:
    print '{} is rated {}'.format(restaurant, rating)