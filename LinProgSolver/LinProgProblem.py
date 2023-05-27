
from .utils.LinProgInterpreter import LinProgInterpreter
from .LinProgProblemException import LinProgProblemException

class LinProgProblem:
    """Class for solving Linear Programming Problems

    Raises:
        LinProgSolverException: Solver

    Returns:
        _type_: _description_
    """

    __contraints: list  # list of constraints (list<LinProgConstraint>)
    __variables: list  # list of variables (list<LinProgVariable>)
    __interpreter: LinProgInterpreter  # Interpreter
    obj_func: None  # objective function
    solution: None  # solution

    def __init__(self, problem_name: str, optimization = None, file_name: str = None) -> None:

        if file_name:
            self.__problem_from_file(file_name)

    def add_variable(self, variable_name: str, variable_key: str) -> None:
        # add variable to problem

        if self.__is_variable_valid(variable_key):
            # logic to insert variable on the problem

            var_name = self.__adjust_name(variable_name)

        else:
            # logic to alert user (exception)
            raise LinProgProblemException("Invalid variable key name.")

    def add_obj_function(self, of_equation: str, optimization: str = None) -> None:
        # add objective function to problem

        # verify optimization (MAX, MIN or EQUALS)

        # call __add_to_problem
        pass

    def add_constraint(self, constraint_name: str, constraint_equation: str) -> None:
        # add constraint to problem

        cons_name = self.__adjust_name(constraint_name)

        # call __add_to_problem
        pass

    def solve(self) -> bool:
        # returns if the problem was solved

        # verify if all needings are complete
        if self.__is_problem_solvable():
            return True
        else:
            return False

    def extract_problem(self, file_name: str) -> None:
        # save problem to a file
        pass

    def __problem_from_file(self, file_name: str) -> None:
        # create problem from passed file
        pass

    def __add_to_problem(self, obj: dict) -> None:
        # logic to add to problem

        # call interpreter

        # add to main dict
        pass

    def __is_problem_solvable(self) -> bool:
        # verify if the problem have all needings

        return True

    def __is_variable_valid(self, variable_key: str) -> bool:
        # verify if variable key is valid

        # verify if the variable already exists on the problem

        # verify if key is valid (length and conflict)
        return True

    def __adjust_name(self, name: str) -> str:
        # adjust name

        # verify length

        # verify white spaces

        # create a warning if changed the name

        return ""
