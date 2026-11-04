from eva_data_analysis import text_to_duration

# Test the input is working
#print(text_to_duration("10:00"))

def test_to_duration_no_minutes():
    actual = text_to_duration("10:00")
    expected = 10.00
    assert(actual == expected)
        

def test_to_duration_with_minutes():
    actual = text_to_duration("10:30")
    expected = 10.50
    assert(actual == expected)
    

# Convention over configuration

# Coverage