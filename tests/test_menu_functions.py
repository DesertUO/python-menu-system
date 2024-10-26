import pytest
from menu_system import Menu, MenuMessages, validateInput

# Mock input function for testing
def mock_input(prompt):
    return '1'  # Change this to simulate different user inputs

# Test for MenuMessages class
def test_menu_messages():
    msgs = MenuMessages()
    assert msgs.welcome == "Welcome to the program..."
    assert msgs.quit_program == "Exit"

# Test for validateInput function (string input)
def test_validate_input_str(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'valid_input')
    result = validateInput("Enter something:", type="str")
    assert result == 'valid_input'

# Test for validateInput function (int input)
def test_validate_input_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    result = validateInput("Enter a number:", type="int", inputRange=range(1, 10))
    assert result == 5

# Test for validateInput function (invalid int input)
def test_validate_input_int_valid_after_invalid(capfd, monkeypatch):
    # Simulate invalid input followed by valid input
    inputs = iter(['15', '5'])  # First '15' (invalid), then '5' (valid)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call validateInput, it should handle the invalid input
    result = validateInput("Enter a number:", type="int", inputRange=range(1, 10))

    # Capture the printed output
    captured = capfd.readouterr()

    # Check that the expected error message was printed
    assert "Input is invalid Input out of range (range(1, 10)). Try again..." in captured.out

    # Assert that the valid input is returned
    assert result == 5

# Test for the Menu class
def test_menu_init():
    functions = [lambda: None]  # Dummy function for testing
    menu = Menu(functions)
    assert menu.functions == functions

def test_menu_quit(monkeypatch):
    functions = [lambda: None]
    menu = Menu(functions)
    
    # Test quitting the menu
    with pytest.raises(SystemExit):
        menu.quit()

# Add more tests as needed...

# To run the tests, use the command:
# pytest test_menu.py