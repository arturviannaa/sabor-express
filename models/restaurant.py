from models.rating import Rating
from models.menu.menu_item import MenuItem

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}\n')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | {restaurant.status}')

    @property
    def status(self):
        return 'Ativado' if self._status else 'Desativado'
    
    def toggle_status(self):
        self._status = not self._status

    def recive_rating(self, customer, grade):
        if 0 < grade <= 5:
            rating = Rating(customer, grade)
            self._rating.append(rating)

    @property
    def average_rating(self):
        if not self._rating:
            return '-'
        
        sum_of_grades = sum(rating._grade for rating in self._rating)
        amount_of_grades = len(self._rating)
        average = round(sum_of_grades / amount_of_grades, 1)

        return average

    def add_item_in_menu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)

    @property
    def show_menu(self):
        print(f'Cardápio do restaurante {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, 'description'):
                dish_message = f'{i}. Nome: {item._name} | Preço: R${item._price} | Descrição: {item.description}'
                print(dish_message)
            else:
                drink_message = f'{i}. Nome: {item._name} | Preço: R${item._price} | Tamanho: {item.size}'
                print(drink_message)