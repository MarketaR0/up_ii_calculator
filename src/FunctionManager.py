from src.BasicFunctions import add, subtract, multiply, divide
from src.AdvFunctions import int_division, factorial, quadratic_eq

class FunctionManager:
    functions = {
        0: (add, 2, "Add"),
        1: (subtract, 2, "Subtract"),
        2: (multiply, 2, "Multiply"),
        3: (divide, 2, "Divide"),
        4: (int_division, 2, "Intereger divition"),
        5: (factorial, 1, "Factorial"),
        6: (quadratic_eq, 3, "Quadratic equation")
    }

    def use_function(self, choice, *args):
        return self.functions[choice][0](*args)

    def calc_num_of_args(self, choice):
        return self.functions[choice][1]

    # Shows users which function of calculator they can choose
    def show_functions(self):
        print("Please select operation by choosing its number -")

        # Iterates through the dictionary "functions" to print all possible functions.
        for func in self.functions.items():
            print("{} - {}".format(
                func[0], func[1][2]
            ))
