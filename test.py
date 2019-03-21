import simple_python_data
def test_calculate_rectancle_area():
    """
    Check that running your code should calculate a rectangle's area"
    """
    assert simple_python_data.calculate_rectangle_area(0, 0) == 0, "Your calculate_rectangle_area func should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(5, 0) == 0, "Your calculate_rectangle_area func should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(0, 5) == 0, "Your calculate_rectangle_area func should be able to handle zero values"
    assert simple_python_data.calculate_rectangle_area(5, 2) == 10, "Your calculate_rectangle_area func should be able to handle positive values"
    
def test_calculate_area_of_square():
    """
    Check that running your code should calculate a square's area"
    """
    assert simple_python_data.calculate_area_of_square(0) == 0, "Your calculate_area_of_square func should be able to handle zero values"
    assert simple_python_data.calculate_area_of_square(5) == 25, "Your calculate_area_of_square func should be able to handle positive values"
    
def test_calculate_total_plus_tip_per_person():
    """
    Check that running your code should calculate a total plus tip per person"
    """
    assert simple_python_data.calculate_total_plus_tip_per_person(100, 20, 4) == 30, "Your calculate_total_plus_tip_per_person func should return correct value"
    
    
def test_fahrenheit_to_celcius():
    """
    Check that running your code should calculate fahrenheit to celcius"
    """
    assert simple_python_data.fahrenheit_to_celcius(32) == 0, "Your fahrenheit_to_celcius func should return correct value"
    assert simple_python_data.fahrenheit_to_celcius(50) == 10, "Your fahrenheit_to_celcius func should return correct value"
    
def test_calculate_the_remainder():
    """
    Check that running your code should return a correct remainder"
    """
    assert simple_python_data.calculate_the_remainder(5, 2) == 1, "Your calculate_the_remainder func should return correct value"
    assert simple_python_data.calculate_the_remainder(13, 4) == 1, "Your calculate_the_remainder func should return correct value"
    assert simple_python_data.calculate_the_remainder(100, 50) == 0, "Your calculate_the_remainder func should return correct value"
    assert simple_python_data.calculate_the_remainder(5, 9) == 4, "Your calculate_the_remainder func should return correct value"
