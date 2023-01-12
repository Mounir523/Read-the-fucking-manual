# Tests (copy to tests/test_user_functions.py)
import pytest
import io
from user_functions import *
#import user_functions

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'
    
# def test_user_name_with_user_input_no_empty_string(monkeypatch):
    # monkeypatch.setattr('sys.stdin', io.StringIO(''))
    # assert get_user_name_from_input() is None
    
def test_user_name_with_user_input_no_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra kaferle'))
    assert get_user_name_from_input() is None
    
def test_user_name_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('pkaferle'))
    assert get_user_name_from_input() == 'pkaferle'