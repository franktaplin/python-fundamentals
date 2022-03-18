# This is the function to be tested in Section 11-2


def city_country(city, country, population=''):
    if population:
        return '{0}, {1} - {2}'.format(city, country, population).title()
    else:
        return '{0}, {1}'.format(city, country).title()
