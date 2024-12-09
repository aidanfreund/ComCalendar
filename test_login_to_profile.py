#Author: Colton Longstreth
from InputController import InputController
import pytest

def test_login_two_empty_values():
    assert InputController.login("","") == False

def test_login_username_empty_value():
    assert InputController.login("","abcd") == False

def test_login_password_empty_value():
    assert InputController.login("aaa","") == False

def test_login_two_strings_not_saved_profile():
    assert InputController.login("Not","Profile") == False

def test_login_both_parameters_invalid_characters():
    assert InputController.create_profile("!#$!#$","$@%@") == False

def test_login_invalid_character_username():
    assert InputController.login("@!$!#$","aaaa") == False

def test_login_invalid_character_password():
    assert InputController.login("asbs","#%@#%") == False

def test_login_correct_credentials_saved_profile():
    assert InputController.login("test","login") == True