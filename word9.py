def is_palidrome(motherAge, daughterAge):
    motherAge = str(motherAge)
    daughterAge = str(daughterAge)
    difference = len(motherAge) - len(daughterAge)
    daughterAge = daughterAge.zfill(len(motherAge))
    motherAge = motherAge[::-1]
    if motherAge == daughterAge:
        return True
    else:
        return False
