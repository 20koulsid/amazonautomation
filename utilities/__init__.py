class Utils:

    def assert_title(self,actual_title,expected_title):
        assert actual_title == expected_title
        print(f"Actual title: {actual_title}")
        if actual_title == expected_title:
            print(f"Title Matched")
            print("Title assertion passed")
        else:
            print(f"Title Mismatched. Expected: {expected_title}, Actual: {actual_title}")
