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

# asks user to enter new restaurant ratings and updates dictionary until user enters 'q'

while True:
    #generates random number from 0 to length of dictionary - 1
    random_number = random.randint(0, len(restaurant_ratings)-1)
    #picks a random key
    random_restaurant = restaurant_ratings.keys()[random_number]
    #prompts user for new rating after displaying the current one
    print "{}'s current rating is: {}".format(random_restaurant, restaurant_ratings[random_restaurant])
    user_rating = raw_input("Enter new rating: ")
    #breaks out of loop if user enters 'q'
    if user_rating == 'q':
        break

    #updates the dictionary
    restaurant_ratings[random_restaurant] = user_rating

#this turns the dictionary into a list of tuples and sorts it and prints the restaurant and ratings

restaurant_ratings = restaurant_ratings.items()
restaurant_ratings.sort()

#prints list of restaurants and ratings
for restaurant, rating in restaurant_ratings:
    print '{} is rated {}'.format(restaurant, rating)