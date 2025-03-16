class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def show(self):
        print(self.title)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def choose(self):
        while True:
            try:
                choice = int(input("Choose an option: "))
                if choice < 1 or choice > len(self.options):
                    raise ValueError
                return choice
            except ValueError:
                print("Invalid choice. Try again.")