def celsius_to_fahrenheit(c_temp):
    f_temp = (c_temp * 9/5) + 32
    return f_temp

# Unit test
def test_clesius_to_fahrenheit():
    actual = celsius_to_fahrenheit(38)
    expected = 100.4

    if (actual == expected):
        print("Pass")
    else:
        print("Fail")

def test_clesius_to_fahrenheit_float():
    actual = celsius_to_fahrenheit(38.5)
    expected = 101.3

    if (actual == expected):
        print("Pass")
    else:
        print("Fail")




# Call unit test
test_clesius_to_fahrenheit()