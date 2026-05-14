class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nWelcome to '{self.restaurant_name}'!")
        print(f"We serve the best {self.cuisine_type} dishes.")

kakhetian_spot = Restaurant("Kakhuri Gvino", "Kakhetian")
megrelian_spot = Restaurant("Diaroni", "Megrelian")
mtiulian_spot = Restaurant("Pasanauri", "Mtiulian")

kakhetian_spot.describe_restaurant()
megrelian_spot.describe_restaurant()
mtiulian_spot.describe_restaurant()