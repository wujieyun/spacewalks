from eva_data_analysis import text_to_duration

# Test the input is working
#print(text_to_duration("10:00"))

def test_to_duration():
    actual = text_to_duration("10:00")
    expected = 10.00

    if (actual == expected):
        print("Pass")
    else:
        print("Fail")

test_to_duration()