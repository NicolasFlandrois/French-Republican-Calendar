#!/usr/bin/python3.7
# UTF8
# Date:
# Author: Nicolas Flandrois

from datetime import datetime

class FrRepCal(object):
    """FrRepCal will Handle French Republican Dates"""
    monthNames =    [
                        'Vendémiaire',
                        'Brumaire',
                        'Frimaire',
                        'Nivôse',
                        'Pluviôse',
                        'Ventôse',
                        'Germinal',
                        'Floréal',
                        'Prairial',
                        'Messidor',
                        'Thermidor',
                        'Fructidor',
                        'Sansculottides'
                        ]

    dayNames = [
                    'primidi',
                    'duodi',
                    'tridi',
                    'quartidi',
                    'quintidi',
                    'sextidi',
                    'septidi',
                    'octidi',
                    'nonidi',
                    'décadi'
                    ]

    sansculottides =    [
                            'La Fête de la Vertu',
                            'La Fête du Génie',
                            'La Fête du Travail',
                            'La Fête de l\'Opinion',
                            'La Fête des Récompenses',
                            'La Fête de la Révolution'
                            ]

    # def model():
    # """Dictionary model/view of a French Rep Date."""

class GetDate(object):
    """GetDate will manage Gregorian Dates"""

    def nowdate():
        """
        Returns Date Now at time of coputation, local time,
        Gregorian callendar, as a date tuple.
        """
        return datetime.now().timetuple()

    def leapyr(year: int):
        """"
        This function defines if the year is
        a Leap year (366 days)
        or a Normal year (365 days).
        Then it will to the variable n the value of 366 or 365, accordingly.
        """
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            n = 366
            # print("The year is a Leap year.\n")

        else:
            n = 365
            # print("The year is a normal year.\n")

        return n

class Compute(object):
    """docstring for Compute"""
    def convert(DateTuple):
        """
        The convert function, computes Gregorian Dates into French Rep. Dates.
        Takes a Date Tuple, and Returning Dictionnary.
        """
        leapyear = GetDate.leapyr(DateTuple[0])

        if DateTuple[7] < 265:
            fr_year = DateTuple[0] - 1792
            fr_month = FrRepCal.monthNames[
                        (DateTuple[7] + (GetDate.leapyr(DateTuple[0]) - 265))
                        // 30 +1]
            if fr_month == 'Sansculottides':
                fr_decadi = None
                # fr_day = FrRepCal.sansculottides[((DateTuple[7] + (GetDate.leapyr(DateTuple[0]) - 265)) % 30) % 10] # Not Sure of this line!
            else:
                fr_decadi = ((DateTuple[7] + (GetDate.leapyr(DateTuple[0]) - 265)) % 30) // 10
                fr_day = FrRepCal.dayNames[((DateTuple[7] + (GetDate.leapyr(DateTuple[0]) - 265)) % 30) % 10]
        else:
            fr_year = DateTuple[0] - 1792 +1
            fr_month = DateTuple[7] // 30
            fr_decadi = (DateTuple[7] % 30) // 10
            fr_day = (DateTuple[7] % 30) % 10

        return fr_year, fr_month, fr_decadi, fr_day

    # def translate(FrRepDateDict):
    #     """
    #     The Translate function, computes Fr. Rep. Dates back into Gregorian Dates.
    #     It returns a Date time Tuple.
    #     """

print('Test:')
# print(Compute.convert(GetDate.nowdate()))
print("\n20/09/2018 is supposed to be : Année 226, Sansculottides[13], Decade I, Jours de l'Opinion[04]")
# print("\nDate Sansculottides", Compute.convert(datetime.strptime(f'2018 09 20', '%Y %m %d').timetuple()))
print("\n01/12/2018 is suppose to be: Année 227 Mois de Frimaire[03], Decade I, Jour du Décadi[10]")
print("Date After 22Sept", Compute.convert(datetime.strptime(f'2018 12 01', '%Y %m %d').timetuple()))
print("\n01/04/2018 is suppose to be: Année 226 Mois de Germinal[07], Decade II, Jour du Duodi[02]")
print("Date Before 22Sept", Compute.convert(datetime.strptime(f'2018 04 01', '%Y %m %d').timetuple()))
