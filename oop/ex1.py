class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
   
    def describe_restaurant(self):
        print(f"\nRestaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
       print(f"The restaurant '{self.restaurant_name}' is now OPEN!")
  
georgian_restaurant = Restaurant("Shua Qalaqshi", "Traditional Georgian")
print(f"Attribute - Name: {georgian_restaurant.restaurant_name}")
print(f"Attribute - Cuisine: {georgian_restaurant.cuisine_type}")
georgian_restaurant.describe_restaurant()
georgian_restaurant.open_restaurant() 
