#!/usr/bin/env python
# -*- coding: utf-8 -
# version 1.1.8

class SYS_Convertor_Class():
    def __init__(self):
        super().__init__()

        self.sys_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def error_handler(self, number, sys_state):
        self.error_state = None
        self.error_message = None

        self.errors = []

        if sys_state is None:
            self.errors.append("ERROR! You have not entered the base of the number system")
        else:
            if sys_state > 36:
                self.errors.append("ERROR! The base of the number system cannot be greater than 36")
            if sys_state < 2:
                self.errors.append("ERROR! The base of the number system cannot be less than 2")
            if int(sys_state) != sys_state:
                self.errors.append("ERROR! The base of the number system cannot be float number")

        if self.errors:
            self.error_state = False
            self.error_message = "\n".join(self.errors) + "\n"
        else:
            self.error_state = True

    def verification_error_handler(self, number, sys_state):
        self.verification_error_state = None
        self.verification_error_message = None
        self.verification_number = number.split(".")
        self.verification_errors = []

        self.verification_index = 0
        self.verification_constant = 0

        if ("-" in number and number != "-" + number.replace("-", "")) or (len(self.verification_number) > 2) or " " in number:
            self.verification_errors.append("ERROR! The converted number is not a valid integer")

        for self.numbers_1 in number.replace("-", "").replace(".", ""):
            if not(self.numbers_1 in self.sys_alphabet):
                self.verification_errors.append("ERROR! The converted number is not a valid integer")

                number = number.replace(self.numbers_1, "")

        for self.numbers_2 in number.replace("-", "").replace(".", "").replace(" ", ""):
            if self.sys_alphabet.index(self.numbers_2) > self.verification_index:
                self.verification_index = self.sys_alphabet.index(self.numbers_2)

        if (sys_state != 0 and sys_state != 1) and self.verification_index >= (sys_state + self.verification_constant):
            self.verification_errors.append("ERROR! The converted number has gone beyond the scope of the number system")

        if self.verification_errors:
            self.verification_error_state = False
            self.verification_error_message = "\n".join(self.verification_errors) + "\n"
        else:
            self.verification_error_state = True

    def type_error_handler(self, number, sys_state):
        self.type_error_state = None
        self.type_error_message = None

        self.type_errors = []

        self.type_number = type(number)
        self.type_sys_state = type(sys_state)

        if self.mode == "sys":
            if self.type_number != int or self.type_number != float:
                self.type_errors.append("ERROR! Type of the converted number is not a integer or float")
            if self.type_sys_state != int:
                self.type_errors.append("ERROR! Type of the number system is not a integer")
        if self.mode == "resys":
            if self.type_number != str:
                self.type_errors.append("ERROR! Type of the converted number is not a string")
            if self.type_sys_state != int:
                self.type_errors.append("ERROR! Type of the number system is not a integer")

        if self.type_errors:
            self.type_error_state = False
            self.type_error_message = "\n".join(self.type_errors) + "\n"
        else:
            self.type_error_state = True

    def sys(self, number, sys_state):
        self.mode = "sys"
        self.type_error_handler(number, sys_state)

        if self.type_error_state:
            self.error_handler(number, sys_state)

            if self.error_state:
                if int(number) == number:
                    if number == 0:
                        return "0"
                    elif number < 0:
                        self.temp_number = int(str(number)[1:])
                        self.number_in_sys = []

                        while self.temp_number != 0:
                            self.number_in_sys.append(self.sys_alphabet[self.temp_number % sys_state])
                            self.temp_number //= sys_state

                        return "-" + "".join(reversed(self.number_in_sys))
                    else:
                        self.temp_number = int(number)
                        self.number_in_sys = []

                        while self.temp_number != 0:
                            self.number_in_sys.append(self.sys_alphabet[self.temp_number % sys_state])
                            self.temp_number //= sys_state

                        return "".join(reversed(self.number_in_sys))
                else:
                    self.splitted_number = str(number).split(".")
                    self.result = []

                    for self.splitted_nums in self.splitted_number:
                        self.splitted_nums = int(self.splitted_nums)

                        while self.splitted_nums != 0:
                            self.result.append(self.sys_alphabet[self.splitted_nums % sys_state])
                            self.splitted_nums //= sys_state

                        self.result.append(".")

                    return "".join(reversed(self.result[0:-1]))

            else:
                return self.error_message
        else:
            return self.type_error_message
    def resys(self, number, sys_state):
        self.mode = "resys"

        self.type_error_handler(number, sys_state)

        if self.type_error_state:
            self.verification_error_handler(number, sys_state)

            if not(self.verification_error_state):
                return self.verification_error_message
            else:
                self.error_handler(number, sys_state)

                if self.error_state:
                    if  "." in number:
                        self.number_in_sys_1 = ""

                        for self.numbers_1 in number.split("."):
                            self.number_in_sys_1 += str(int(self.numbers_1, sys_state)) + "."

                        return self.number_in_sys_1[0:-1]
                    else:
                        return int(number, sys_state)
                else:
                    return self.error_message
        else:
            return self.type_error_message

M = SYS_Convertor_Class()

def sys(n, s):
    return M.sys(n, s)
def resys(n, s):
    return M.resys(n, s)

if __name__ == '__main__':
    sys(n, s)
    resys(n, s)
