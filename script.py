# 1. Create a list with the following destinations and save it into a variable called destinations.

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# 2. Let's define a test traveler to see how our functionality is working so far. Create a test_traveler variable.

test_traveler = ["Erin Wilkes", "Shanghai, China", ["Historical site", "art"]]

# 8. When a traveler arrives at a destination, we want to know where they are!
# Since we use lists for all of our data — we are going to identify each location based on its index in our destinations list.
# But we need to retrieve that index first.
# Define a function called get_destination_index(). It should take a single parameter, destination, the destination as a string.

def get_destination_index(destination: str):
  
  # 9. In the body of get_destination_index(), find the index of destination and save the results into a variable called destination_index.
  
  destination_index = destinations.index(destination)

  # 10. In the body of get_destination_index(), after you’ve defined destination_index, return it.

  return destination_index

# 11. Test out your function. Try to call get_destination_index() with the argument "Los Angeles, USA".
# Print out the results.  

#print(get_destination_index("Los Angeles, USA"))

# 12. Try to call get_destination_index() with the argument “Paris, France” instead.
# Since that is the first element on our destinations list, it should return the index 0

#print(get_destination_index("Paris, France"))

# 15. Now let’s define a function called get_traveler_location().
# get_traveler_location() is going to take a single parameter, traveler

def get_traveler_location(traveler: list):

  # 16. In the body of get_traveler_location(), access the traveler’s destination string and save it into traveler_destination
  
  traveler_destination = traveler[1]

  # 17. Use traveler_destination along with get_destination_index() to retrieve the index of the destination where the traveler is.
  # Save the index of the traveler’s destination into the variable traveler_destination_index

  traveler_destination_index = get_destination_index(traveler_destination)

  # 18. Make get_traveler_location() return the destination index of the traveler by returning traveler_destination_index

  return traveler_destination_index

# 19. Create a variable called test_destination_index. Save the results of calling get_traveler_location() with our test_traveler

test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# 24/25. Now we want to create and maintain a list of attractions. Let’s start by defining a list called attractions.
# We want attractions to be an empty list for every destination in destinations

attractions = [[] for i in destinations]
#print(attractions)

# 27. Now let’s create a function called add_attraction().
# This function should take two parameters: destination, the name of the location and attraction, the attraction.

def add_attraction(destination: str, attraction: list):
  
  # 28. Use get_destination_index() with the passed in destination in order to retrieve the index of the destination.
  # Save the results into destination_index.
  destination_index = get_destination_index(destination)
  attractions[destination_index].append(attraction)

# Testing add_attraction
add_attraction("Los Angeles, USA", ["Venice Beach", ["Beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

# 38. Write a function called find_attractions() that takes two parameters: destination, the name of the destination and interests, a list of interests.

def find_attractions(destination: str, interests: list):
  destination_index = get_destination_index(destination)

  # 40. Look up that destination’s attractions by indexing into attractions with destination_index. Save this into the variable attractions_in_city.
  attractions_in_city = attractions[destination_index]

  # 41. Create a new list called attractions_with_interest. Make it empty when declaring it, we’ll save attractions into this list if they match one of our interests.
  attractions_with_interest = []

  # 42. Create a loop over attractions_in_city saving each item in the list into the temporary variable possible_attraction.
  for attraction in attractions_in_city:
    possible_attraction = attraction

    # 43. For each attraction, retrieve the tagged information about it.
    # In the body of the for loop, save the attraction’s tags into the variable attraction_tags.

    attraction_tags = possible_attraction[1]

    # 44. We want to see if any of the given interests are in attraction_tags.
    # We’re going to loop through the interests and check if any of them are in attraction_tags.
    # Create a for loop in the body of the current for loop to loop through each interest in interests.

    for interest in interests:

      # 45. For every interest in interests, check if that interest is in attraction_tags.
      # If the interest is in the attraction_tags, append possible_attraction to attractions_with_interest.

      if attraction_tags.count(interest) > 0:
        attractions_with_interest.append(possible_attraction[0])
  
  # 46. At the end of your function, return attractions_with_interest.
  
  return attractions_with_interest

# 47. Testing find_attractions

la_arts = find_attractions("Los Angeles, USA", ['art'])
#print(la_arts)

# 53. Define a function called get_attractions_for_traveler() that takes a single parameter, traveler.

def get_attractions_for_traveler(traveler: list):

  # 54. Let’s separate out the traveler’s data.

  traveler_name = traveler[0]
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]

  # 55. Call find_attractions() with the two arguments traveler_destination and traveler_interests.
  # Save the results into traveler_attractions.

  traveler_attractions = find_attractions(traveler_destination, traveler_interests)

  # 56. Create a new string, this is what we’ll want to show our traveler when they open our application

  attraction_string = "Hi " + traveler_name + ", we think you'll like these places around " + traveler_destination + ": "

  for i in range(len(traveler_attractions)):
    
    if traveler_attractions[-1] == traveler_attractions[i]:
      attraction_string += traveler_attractions[i] + "."
    else:
      attraction_string += traveler_attractions[i] + ", "

  return attraction_string

# Testing get_attractions_for_traveller

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)