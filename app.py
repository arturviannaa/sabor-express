from models.restaurant import Restaurant

first_restaurant = Restaurant('Xis Patrola', 'Lanches')

first_restaurant.recive_rating('Vianna', 4)
first_restaurant.recive_rating('Gui', 3)
first_restaurant.recive_rating('Lais', 5)

first_restaurant.toggle_status()

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()