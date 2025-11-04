import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import is_palindrome
import pytest

def test_palindrome_true_simple():
    assert is_palindrome("radar") == True

def test_palindrome_true_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_palindrome_false():
    assert is_palindrome("python") == False

def test_palindrome_invalid_input():
    with pytest.raises(TypeError):
        is_palindrome(12345)

