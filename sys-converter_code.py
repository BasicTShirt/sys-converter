#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version 2.0.0

class SYSConvertor():
    def __init__(self):
        self.sys_alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def error_handler(
            self,
            number: str | int,
            sys_state: int
    ) -> None:
        errors = []

        if sys_state is None:
            errors.append("ERROR! You have not entered the base of the number system")
        else:
            if sys_state > 36:
                errors.append("ERROR! The base of the number system cannot be greater than 36")
            if sys_state < 2:
                errors.append("ERROR! The base of the number system cannot be less than 2")

        if errors:
            raise ValueError("\n".join(errors))

    def verification_error_handler(
            self,
            number: str,
            sys_state: int
    ) -> None:
        verification_number = number.split(".")
        verification_errors = []

        verification_index = 0

        if (
                ("-" in number and number != "-" + number.replace("-", ""))
                or (len(verification_number) > 2)
                or " " in number
        ):
            verification_errors.append("ERROR! The converted number is not a valid integer")

        for numbers_1 in number.replace("-", "").replace(".", ""):
            if not (numbers_1 in self.sys_alphabet):
                verification_errors.append("ERROR! The converted number is not a valid integer")
                number = number.replace(numbers_1, "")

        for numbers_2 in number.replace("-", "").replace(".", "").replace(" ", ""):
            if self.sys_alphabet.index(numbers_2) > verification_index:
                verification_index = self.sys_alphabet.index(numbers_2)

        if (
                (sys_state != 0 and sys_state != 1)
                and verification_index >= (sys_state)
        ):
            verification_errors.append("ERROR! The converted number has gone beyond the scope of the number system")

        if verification_errors:
            raise ValueError("\n".join(verification_errors))

    def type_error_handler(
            self,
            number: str | int,
            sys_state: int,
            mode: str
    ) -> None:
        type_errors = []

        if mode == "sys":
            if (
                    not isinstance(number, int)
                    and not isinstance(number, float)
            ):
                type_errors.append("ERROR! Type of the converted number is not a integer or float")
            if not isinstance(sys_state, int):
                type_errors.append("ERROR! Type of the number system is not a integer")
        if mode == "resys":
            if not isinstance(number, str):
                type_errors.append("ERROR! Type of the converted number is not a string")
            if not isinstance(sys_state, int):
                type_errors.append("ERROR! Type of the number system is not a integer")

        if type_errors:
            raise ValueError("\n".join(type_errors))

    def sys(
            self,
            number: int | float,
            sys_state: int
    ) -> str:
        self.type_error_handler(number, sys_state, "sys")
        self.error_handler(number, sys_state)

        if isinstance(number, int):
            if number == 0:
                return "0"
            elif number < 0:
                temp_number = int(str(number)[1:])
                number_in_sys = []

                while temp_number != 0:
                    number_in_sys.append(self.sys_alphabet[temp_number % sys_state])
                    temp_number //= sys_state

                return "-" + "".join(reversed(number_in_sys))
            else:
                temp_number = int(number)
                number_in_sys = []

                while temp_number != 0:
                    number_in_sys.append(self.sys_alphabet[temp_number % sys_state])
                    temp_number //= sys_state

                return "".join(reversed(number_in_sys))
        else:
            splitted_number = str(number).replace("-", "").split(".")
            result = []

            integer_part = int(splitted_number[0])
            if integer_part == 0:
                result.append("0")
            while integer_part != 0:
                result.append(self.sys_alphabet[integer_part % sys_state])
                integer_part //= sys_state
            result = ["".join(reversed(result))]

            if len(splitted_number) == 2:
                fractional = float("0." + splitted_number[1])
                result.append(".")
                precision = 0
                while fractional > 1e-10 and precision < 12:
                    fractional *= sys_state
                    digit = int(fractional)
                    result.append(self.sys_alphabet[digit])
                    fractional -= digit
                    fractional = round(fractional, 10)
                    precision += 1

            if number < 0:
                return "-" + "".join(result)
            return "".join(result)

    def resys(
            self,
            number: str,
            sys_state: int
    ) -> int | float:
        self.type_error_handler(number, sys_state, "resys")
        self.verification_error_handler(number, sys_state)
        self.error_handler(number, sys_state)

        if "." in number:
            parts = number.split(".")
            integer_part = int(parts[0], sys_state)
            fractional = 0.0
            divisor = sys_state
            for digit in parts[1]:
                fractional += int(digit, sys_state) / divisor
                divisor *= sys_state
            return integer_part + fractional
        else:
            return int(number, sys_state)

def sys(n, s):
    converter = SYSConvertor()
    return converter.sys(n, s)

def resys(n, s):
    converter = SYSConvertor()
    return converter.resys(n, s)

if __name__ == '__main__':
    pass
