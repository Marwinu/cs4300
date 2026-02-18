import pytest
from src.task1 import main

def test_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"