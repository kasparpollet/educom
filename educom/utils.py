from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from itertools import combinations

from core.models import Person

JUBILEUM_YEARS = [50, 100, 150, 200]
MAX_AGE = 105

def find_jubileums_of_all_persons() -> list:
    unique_person_pairs = list(combinations(Person.objects.all(), 2))
    final = {jubileum_year: [] for jubileum_year in JUBILEUM_YEARS}

    for jubileum_year in JUBILEUM_YEARS:
        for pair in unique_person_pairs:
            jubileum = find_jubileum(pair[0], pair[1], jubileum_year)
            if jubileum:
                final[jubileum_year].append(jubileum)

    return final


def find_jubileum(person1: Person, person2: Person, years:int) -> str:
    # Age difference in seconds
    delta = (person1.birthdate - person2.birthdate).total_seconds()

    # Who is older and make seconds absolute
    oldest = 1
    if delta < 0:
        delta = delta * -1
        oldest = 0

    # Time to add for each person in seconds to get to jubileum
    time_to_add = (timedelta(days=(365*years) + years/4).total_seconds() - delta) / 2 # I am not proud of this 365 and /4

    # Date of the jubileum
    if oldest == 0:
        jubileum_date = person2.birthdate + timedelta(seconds=time_to_add)
    else:
        jubileum_date = person1.birthdate + timedelta(seconds=time_to_add)

    # Age of persons at jubileum
    difference_in_years1 = relativedelta(jubileum_date, person1.birthdate)
    difference_in_years2 = relativedelta(jubileum_date, person2.birthdate)

    if difference_in_years1.years > MAX_AGE or difference_in_years2.years > MAX_AGE:
        return None

    return f'{years} jaar op {jubileum_date} ({person1.full_name} {relativedate_to_string(difference_in_years1)}, {person2.full_name} {relativedate_to_string(difference_in_years2)})'


def relativedate_to_string(date:relativedelta) -> str:
    return f'{date.years} jaar {date.months} maanden en {date.days} dagen'