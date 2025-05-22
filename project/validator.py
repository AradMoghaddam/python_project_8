import re


def license_validator(license):
    errors = []
    if not (type(license[0]) == int and license[0]>0):
        errors.append('Person ID must be an integer > 0')

    if not (type(license[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[1])):
        errors.append('Person Name is Invalid')


    if not (type(license[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", license[2])):
        errors.append('Person Family is Invalid')

    if not (type(license[3]) == int and license[3]>0):
        errors.append('Person Account Amount must be an integer > 0')

    return errors


