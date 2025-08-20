from models.rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._rating = []
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