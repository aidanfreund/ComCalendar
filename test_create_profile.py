# Author: Colton Longstreth
from InputController import InputController
import pytest

def test_create_profile_two_empty_values():
    assert InputController.create_profile("","") == False

def test_create_profile_username_empty_value():
    assert InputController.create_profile("","test") == False

def test_create_profile_password_empty_value():
    assert InputController.create_profile("test","") == False

def test_create_profile_both_parameters_invalid_characters():
    assert InputController.create_profile("@%!#","#Q$#$") == False

def test_create_profile_username_invalid_character():
    assert InputController.create_profile("#$@#4","test") == False

def test_create_profile_password_invalid_character():
    assert InputController.create_profile("test", "@%@#%") == False

def test_create_profile_nonunique_username():
    assert InputController.create_profile("test","password") == False

def test_create_profile_valid_create():
    assert InputController.create_profile("create","profile") == True