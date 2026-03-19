from ui.gui import start_gui
from security.breach_checker import BreachChecker

if __name__ == "__main__":
    BreachChecker.load_passwords()
    start_gui()
