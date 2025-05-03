class MenuService:
    def __init__(self, menu_repository):
        self.menu_repository = menu_repository

    def browse_menu(self):
        all_items = self.menu_repository.get_all_items()
        return [item for item in all_items if item.is_available()]
