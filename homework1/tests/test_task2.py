
import pytest
from src.task2 import int_task, float_task, string_task, boolean_task

# parameterized tests
@pytest.mark.parametrize("func, expected_type, expected_value", [
    (int_task, int, 9),
    (float_task, float, 12.56),
    (string_task, str, "Angel"),
    (boolean_task, bool, True),
])
def test_data_types(func, expected_type, expected_value):
    # Check the return type 
    assert isinstance(func(), expected_type)
    # Check the return value
    assert func() == expected_value
