import simple_python_data
def test_calculate_rectancle_area():
    """
    Check that running your code should calculate a rectangle's area"
    """
    assert simple_python_data.calculate_rectangle_area(0, 0) == 0, "Your rectangle should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(5, 0) == 0, "Your rectangle should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(0, 5) == 0, "Your rectangle should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(5, 2) == 10, "Your rectangle should be able to handle positive values"
