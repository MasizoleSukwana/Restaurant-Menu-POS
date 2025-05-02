# ui_factory.py

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextField(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Buttons
class WindowsButton(Button):
    def render(self):
        return "Windows-style Button"

class MacOSButton(Button):
    def render(self):
        return "MacOS-style Button"

# Concrete TextFields
class WindowsTextField(TextField):
    def display(self):
        return "Windows-style Text Field"

class MacOSTextField(TextField):
    def display(self):
        return "MacOS-style Text Field"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_text_field(self):
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_field(self):
        return WindowsTextField()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_text_field(self):
        return MacOSTextField()
