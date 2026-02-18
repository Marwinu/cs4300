from src.task2 import boolean_task, int_task, float_task, string_task

def test_integer():
    # tests data type integer
    assert isinstance(int_task(), int)
    assert int_task() == 9

def test_float():
     # tests data type float
    assert isinstance(float_task(), float)
    assert float_task() == 12.56

def test_string():
     # tests data type string
    assert isinstance(string_task(), str)
    assert string_task() == "Angel"

def test_boolean():
     # tests data type boolean
    assert isinstance(boolean_task(), bool)
    assert boolean_task() is True