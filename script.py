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