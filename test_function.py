from main_SM.py import process_guess
import pytest

def test_length_guess():
    with pytest.raises(ValueError):
        process_guess([])
        
def test_strings_guess():
    with pytest.raises(TypeError):
        process_guess(["cat1*"])