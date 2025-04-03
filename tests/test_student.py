from school_schedule.student import Student

def test_student_class_instantiation():
    
    # arrange
    name = "Peter"
    grade = "junior"
    classes = ["math", "english"]

    # act
    student = Student(
        name, 
        grade, 
        classes
        )

    # assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes

def test_add_classes_new_class_added():

    # arrange
    name = "Peter"
    grade = "junior"
    classes = ["math", "english"]
    student = Student(
        name, 
        grade, 
        classes
        )
    class_name = "geography"

    # act
    result = student.add_class(class_name)

    # assert
    assert result == student.classes
    assert len(student.classes) == 3
    assert student.classes[-1] == class_name

def test_get_num_classes_check_len():
    # arrange
    name = "Peter"
    grade = "junior"
    classes = ["math", "english"]
    student = Student(
        name, 
        grade, 
        classes
        )
    
    # act
    result = student.get_num_classes()

    # assert
    assert result == 2

def test_display_classes():
    # arrange
    name = "Peter"
    grade = "junior"
    classes = ["math", "english", "potions_making"]
    student = Student(
        name, 
        grade, 
        classes
        )
    
    # act
    result = student.display_classes()

    # assert
    assert result == "math, english, potions_making"

def test_summary_gives_full_summary():
    # arrange
    name = "Peter"
    grade = "junior"
    classes = ["math", "english", "potions_making"]
    student = Student(
        name, 
        grade, 
        classes
        )
    
    # act
    result = student.summary()

    # assert
    assert result == "Peter is a junior enrolled in 3 classes: math, english, potions_making"


def test_student_add_class_invalid_data():
    student = Student("Claire", "junior", ["math", "english"])
    invalid_class_name = 123
    original_len_of_classes = len(student.classes)

    # Act
    result = student.add_class(invalid_class_name)
    
    #assert
    assert isinstance(student.invalid_class_name[-1], str) is True


def test_student_class_instantiation_invalid_data():
    
    # arrange
    name = 123
    grade = 123
    classes = [123, "english"]

    # act
    student = Student(
        name, 
        grade, 
        classes
        )

    # assert
    assert isinstance(student.name, str) 
    assert isinstance(student.grade, str)
    assert isinstance(student.classes, list)