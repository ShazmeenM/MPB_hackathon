from main.py import process_guess
import pytest

def test_get_random_word():
    """Test that a random word from the word list is chosen."""
    word_list = ["Alert", "Argue", "Beach"]
    assert main.get_random_word(word_list) in word_list

def test_length_guess():
    """Test that the process_guess function is rasing ValueError."""
    with pytest.raises(ValueError):
        process_guess([])
        
def test_strings_guess():
    """Test that the process_guess function is rasing TypeError."""
    with pytest.raises(TypeError):
        process_guess(["cat1*"])
        
