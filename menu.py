class Menu:

    def __init__(self):
        self.descriptions = {}
        self.functions = {}

    def add_command(self, key, description, function):
        self.descriptions[key] = description
        self.functions[key] = function

    def is_valid(self, command):
        return command in self.descriptions

    def get_action(self, command):
        return self.functions.get(command)

    def __str__(self):
        texts = [f'{key}: {self.descriptions[key]}' for key in self.descriptions.keys()]
        return '\n'.join(texts)
