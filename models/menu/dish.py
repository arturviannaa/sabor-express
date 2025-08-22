from models.menu.menu_item import MenuItem

class Dish(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price) # função super() para herdar funções da classe mãe
        self.description = description