import requests
import json

def handle(req):
    restaurant_names_url = 'http://212.101.137.114/getRestaurantNameList'
    restaurant_ratings_url = 'http://212.101.137.114/getRestaurantRatingList'
    
    # make the API calls to get the restaurant names and ratings
    restaurant_names_response = requests.get(restaurant_names_url)
    restaurant_ratings_response = requests.get(restaurant_ratings_url)
    
    # parse the JSON response for each API call
    restaurant_names = json.loads(restaurant_names_response.content)
    restaurant_ratings = json.loads(restaurant_ratings_response.content)
    
    # create a dictionary to hold the rating information for each restaurant
    restaurant_dict = {}
    
    # iterate over the rating information for each restaurant
    for rating_info in restaurant_ratings:
        restaurant_id = rating_info['restaurant_id']
        rating = rating_info['rating']
        
        # add the rating to the running total for the restaurant
        if restaurant_id in restaurant_dict:
            restaurant_dict[restaurant_id]['total_rating'] += rating
            restaurant_dict[restaurant_id]['num_ratings'] += 1
        else:
            restaurant_dict[restaurant_id] = {
                'total_rating': rating,
                'num_ratings': 1
            }
    
    # calculate the average rating for each restaurant and add it to the restaurant dictionary
    for restaurant_info in restaurant_names:
        restaurant_id = restaurant_info['id']
        restaurant_name = restaurant_info['restaurant_name']
        
        if restaurant_id in restaurant_dict:
            total_rating = restaurant_dict[restaurant_id]['total_rating']
            num_ratings = restaurant_dict[restaurant_id]['num_ratings']
            avg_rating = round(total_rating / num_ratings, 2)
            
            restaurant_dict[restaurant_id]['restaurant_name'] = restaurant_name
            restaurant_dict[restaurant_id]['avg_rating'] = avg_rating
    
    # sort the restaurants by rating in descending order
    sorted_restaurants = sorted(restaurant_dict.values(), key=lambda x: x['avg_rating'], reverse=True)
    
    # return the sorted list as a JSON string
    return json.dumps(sorted_restaurants)
