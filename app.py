from modelos.restaurante import Restaurant

first_restaurant = Restaurant('Xis Patrola', 'Lanches')
second_restaurant = Restaurant('Primmo Pizza', 'Pizza')
third_restaurant = Restaurant('Olé Tacos', 'Mexicana')

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()