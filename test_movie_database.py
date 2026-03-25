from AssignmentTwo import valid_genre, valid_rating

def main():
    test_valid_genre()
    test_valid_rating()
    print("Testing Completed")

def test_valid_genre():
    assert valid_genre("Action") == True
    assert valid_genre("Sci-Fi") == True
    assert valid_genre("Random") == False
    assert valid_genre("Fake") == False

def test_valid_rating():
    assert valid_rating("8") == True
    assert valid_rating("10") == True
    assert valid_rating("9.5") == True
    assert valid_rating("8.75") == False
    assert valid_rating("abcd") == False

if __name__ == "__main__":
    main()