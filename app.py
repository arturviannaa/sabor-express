from models.restaurant import Restaurant

first_restaurant = Restaurant('Xis Patrola', 'Lanches')
# second_restaurant = Restaurant('Primmo Pizza', 'Pizza')
# third_restaurant = Restaurant('Olé Tacos', 'Mexicana')

first_restaurant.recive_rating('Vianna', 10)
first_restaurant.recive_rating('Gui', 8)
first_restaurant.recive_rating('Lais', 2)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()