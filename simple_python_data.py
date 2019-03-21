def calculate_rectangle_area(height, width):    
    ## Todo: update `None` to contain the formula for `rectangle_area`
    rectangle_area = height * width
    return rectangle_area

def calculate_area_of_square(side):
    ## Todo: update `None` to contain the formula for `squre_area`
    square_area = side ** 2
    return square_area

def calculate_total_plus_tip_per_person(total_bill, tip_percent, number_of_people):
    ## Todo: update `None` to contain the formula for `total_plus_tip_` and `total_plus_tip_per_person`.
    total_plus_tip = total_bill * (1+(tip_percent / 100))
    total_plus_tip_per_person = total_plus_tip / number_of_people
    return total_plus_tip_per_person

def fahrenheit_to_celcius(degrees):
    ## Todo: update `None` to contain the formula for `degrees_in_celcius`
    ## use the formula (F − 32) × 5/9 = C
    degrees_in_celcius = (degrees − 32) * (5/9)
    return degrees_in_celcius

def calculate_the_remainder(num1, num2):
    ## Todo: update `None` to contain the formula for `remainder`
    remainder = num1 % num2
    return remainder
