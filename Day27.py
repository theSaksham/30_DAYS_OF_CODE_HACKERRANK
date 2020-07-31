
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1]
    @staticmethod
    def get_array():
        # complete this function
        return TestDataUniqueValues.data

    @staticmethod
    def get_expected_result():
        # complete this function
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))

class TestDataExactlyTwoDifferentMinimums(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1] 
    data.insert(0,0)
    @staticmethod
    def get_array():
        # complete this function
        return TestDataExactlyTwoDifferentMinimums.data

    @staticmethod
    def get_expected_result():
        # complete this function
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))
