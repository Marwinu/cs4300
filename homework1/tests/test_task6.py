import pytest
from src.task6 import count_words

# Parameterized test
@pytest.mark.parametrize("path, confirmed_total", [
    ("src/task6_read_me.txt", 127),
    # more files can be added for parameterized testing
])

def test_word_counts(path, confirmed_total):
    assert count_words(path) == confirmed_total