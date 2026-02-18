import pytest
from src.task5 import favorite_books, get_first_books, student_database, get_student_id


# tests for books

def test_length_is_three():
    assert len(get_first_books(favorite_books)) == 3

def test_books_correct():
    assert get_first_books(favorite_books) == favorite_books[:3]


# tests for database

def test_student_id():
    assert get_student_id("Julian Romero") == 1301

def test_student_id_not_found():
    assert get_student_id("Unknown Person") is None