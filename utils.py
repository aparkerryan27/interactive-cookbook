from unicodedata import numeric

def string_frac_to_fraction(i):
    if len(i) == 1:
        v = numeric(i)
    elif i[-1].isdigit():
        # normal number, ending in [0-9]
        v = float(i)
    else:
        # Assume the last character is a vulgar fraction
        v = float(i[:-1]) + numeric(i[-1])
    return v