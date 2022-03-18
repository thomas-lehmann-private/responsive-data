from responsive.data import make_responsive
from responsive.observer import OutputObserver

if __name__ == "__main__":
    subject = make_responsive(
        {
            "some_str": "default string",
            "some_int": 1234567890,
            "some_list": [1, 2, 3, 4, 5],
            "some_dict": {"some_other_str": "default other string"},
        }
    )

    subject.add_observer(OutputObserver())

    # changing string field
    subject.some_str = "another string"
    # changing integer field
    subject.some_int = 9876543210
    # appending a value to a list field
    subject.some_list.append(6)
    # removing a value from a list field
    subject.some_list.remove(3)
    # change value by index
    subject.some_list[2] = 7
    # changing list field to another list
    subject.some_list = [5, 4, 3, 2, 1, 0]
    # changing string field of a nested dictionary
    subject.some_dict.some_other_str = "yet another string"



