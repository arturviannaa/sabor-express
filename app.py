from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

first_restaurant = Restaurant('Xis Patrola', 'Lanches')
first_drink = Drink('Suco de Melancia', 7.0, 'grande')
first_drink.apply_discount()
first_dish = Dish('Xis Calabresa', 34.0, 'O melhor pão da cidade')
first_dish.apply_discount()

first_restaurant.add_item_in_menu(first_drink)
first_restaurant.add_item_in_menu(first_dish)

def main():
    first_restaurant.show_menu

if __name__ == '__main__':
    main()