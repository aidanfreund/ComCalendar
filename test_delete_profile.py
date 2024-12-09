import pytest
from InputController import InputController


def test_delete_profile():
    InputController.create_profile('testuser', 'password123')
    assert InputController.get_profile() is not None
    result = InputController.delete_profile()
    assert result is True
    assert InputController.get_profile() is None