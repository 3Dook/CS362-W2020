import classroom_manager


class TestStudent:
    def test_init(self):
        #make variables
        id = 123
        firstName = "John"
        lastName = "Smith"

        #call function
        newStudent = classroom_manager.Student(id, firstName, lastName)

        #assert
        assert 124 == newStudent.id
        assert "John" == newStudent.first_name
        assert "Smith" == newStudent.last_name

    def test_get_full_name(self):

        #make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")

        #call function
        nameCheck = newStudent.get_full_name()

        #assert
        assert nameCheck == "John Smith"

    def test_submit_assignment(self):

        #make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")
        newAssignment = classroom_manager.Assignment("Assignment4", 100.42)

        #call function
        newStudent.submit_assignment(newAssignment)

        #assert
        check = newStudent.get_assignment(newAssignment)
        assert check.name == "Assignment4"

    def test_get_assignments(self):
        #returns a list of assignments
        #make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")
        newAssignment = classroom_manager.Assignment("Assignment4", 100.42)
        newAssignment2 = classroom_manager.Assignment("Assignment5", 100.42)
        newStudent.submit_assignment(newAssignment)
        newStudent.submit_assignment(newAssignment2)

        #call function
        check = newStudent.get_assignment()

        #assert
        #check should contain the list of assignments. hence we we check
        # with len of list to ensure we have the accurate count. Aka there
        # should be 2 assignments since we only added 2
        assert len(check) == 2

    def test_get_assignment(self):
        #make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")
        newAssignment = classroom_manager.Assignment("Assignment4", 100.42)
        newStudent.submit_assignment(newAssignment)

        #call function
        check = newStudent.get_assignment(newAssignment)

        #assert
        #check should contain the name of the newAssignment since we just added it
        assert check.name == "Assignment4"

    def test_get_average(self):
        # returns a list of assignments
        # make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")
        newAssignment = classroom_manager.Assignment("Assignment4", 100)
        newAssignment2 = classroom_manager.Assignment("Assignment5", 50)
        newAssignment2 = classroom_manager.Assignment("Assignment6", 60)
        newStudent.submit_assignment(newAssignment)
        newStudent.submit_assignment(newAssignment2)
        newStudent.submit_assignment(newAssignment3)

        # call function
        check = newStudent.get_average()

        # assert
        # check should contain the 3 assignments with the average of 210/3 == 70
        assert check == 70

    def test_remove_assignment(self):
        # returns a list of assignments
        # make variables
        newStudent = classroom_manager.Student(123, "John", "Smith")
        newAssignment = classroom_manager.Assignment("Assignment4", 100)
        newAssignment2 = classroom_manager.Assignment("Assignment5", 50)
        newAssignment2 = classroom_manager.Assignment("Assignment6", 60)
        newStudent.submit_assignment(newAssignment)
        newStudent.submit_assignment(newAssignment2)
        newStudent.submit_assignment(newAssignment3)

        # call function
        newStudent.remove_assignment(newAssignment)

        # assert
        # Check to see if remove took out the correct assignment
        # THERE SHOULD ONLY BE TWO LEFT
        assert len(newStudent.get_assignments()) == 2
        #assert newStudent.get_assignment(newAssignment).name == None
        assert newStudent.get_assignment(newAssignment2).name == "Assignment5"
        assert newStudent.get_assignment(newAssignment3).name == "Assignment6"

class TestAssignment:

    def test_init(self):
        #make variables
        name = "Assignment4"
        max_score = 100.42

        #call function
        newAssignment = classroom_manager.Assignment(name, max_score)

        #assert
        assert "Assignment4" == newAssignment.name
        assert 100.42 == newAssignment.max_score
        #assert None == newAssignment.grade
        assert newAssignment.grade == None

    def test_assign_grade(self):

        #NOTE WE WILL CHANGE GRADES TWICE AND CHECK ASSERTS

        #make variables
        newAssignment = classroom_manager.Assignment("Assignment4", 100)
        newGrade = 42.42
        #sameGrade = 100
        overGrade = 101

        #call function
        newAssignment.assign_grade(newGrade)
        #assert
        assert newAssignment.grade == 42.42

        #callfunction again to check for void
        newAssignment.assign_grade(overGrade)
        #assert
        assert newAssignment.grade == None
