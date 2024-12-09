# Author: Colton Longstreth
from InputController import InputController
from Profile import Profile
from RequestValidator import RequestValidator
import pytest

#python input function will never give None as result and will turn no input into empty string so testing that 
def test_create_profile_two_empty_values():
    assert InputController.create_profile("","") == False
    assert InputController.get_profile() == None

def test_create_profile_username_empty_value():
    assert InputController.create_profile("","test") == False
    assert InputController.get_profile() == None

def test_create_profile_password_empty_value():
    assert InputController.create_profile("test","") == False
    assert InputController.get_profile() == None

def test_create_profile_both_parameters_invalid_characters():
    assert InputController.create_profile("@%!#","#Q$#$") == False
    assert InputController.get_profile() == None

def test_create_profile_username_invalid_characters():
    assert InputController.create_profile("#$@#4","test") == False
    assert InputController.get_profile() == None

def test_create_profile_password_invalid_characters():
    assert InputController.create_profile("test", "@%@#%") == False
    assert InputController.get_profile() == None

def test_create_profile_nonunique_username():
    assert InputController.create_profile("test","password") == False
    assert InputController.get_profile() == None

def test_create_profile_valid_create():
    assert InputController.create_profile("create2","profile") == True
    assert type(InputController.get_profile()) == Profile