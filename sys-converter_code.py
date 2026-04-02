#!/usr/bin/env python
# -*- coding: utf-8 -
# version 1.1.0

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
        self.verification_errors = []

        try:
            num = int(number)
            if str(num) != number.lstrip():
                raise ValueError
        except ValueError:
            self.verification_errors.append("ERROR! The converted number is not a valid integer")

        if self.verification_errors:
            self.verification_error_state = False
            self.verification_error_message = "\n".join(self.verification_errors) + "\n"
        else:
            self.verification_error_state = True

    def sys(self, number, sys_state):
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
                self.number_str = str(number)
                if '.' in self.number_str:
                    self.integer_part, self.fractional_part = self.number_str.split('.')
                    self.integer_part_number = int(self.integer_part)
                    self.fractional_part_number = float('0.' + self.fractional_part)
                else:
                    self.integer_part_number = int(number)
                    self.fractional_part_number = 0.0

                self.limitation = 10
                self.count = 0

                self.number_in_sys = []
                self.result = None

                if self.integer_part_number != 0:
                    while self.integer_part_number != 0:
                        self.number_in_sys.append(self.sys_alphabet[self.integer_part_number % sys_state])
                        self.integer_part_number //= sys_state
                else:
                    self.number_in_sys.append("0")
                self.result = "".join(reversed(self.number_in_sys))

                self.fractional_digits = []
                self.fractional_temp = self.fractional_part_number

                while self.fractional_temp > 0 and self.count < self.limitation:
                    self.fractional_temp *= sys_state
                    self.digit = int(self.fractional_temp)
                    self.fractional_digits.append(self.sys_alphabet[self.digit])
                    self.fractional_temp -= self.digit
                    self.count += 1

                if self.fractional_digits:
                    self.result += "." + "".join(self.fractional_digits)

                return self.result

        else:
            return self.error_message
    def resys(self, number, sys_state):
        self.verification_error_handler(number, sys_state)

        if not(self.verification_error_state):
            return self.verification_error_message
        else:
            self.error_handler(int(number), sys_state)

            if self.error_state:
                return int(number, sys_state)
            else:
                return self.error_message

M = SYS_Convertor_Class()

def sys(n, s):
    return M.sys(n, s)
def resys(n, s):
    return M.resys(n, s)

if __name__ == '__main__':
    sys(n, s)
    resys(n, s)
