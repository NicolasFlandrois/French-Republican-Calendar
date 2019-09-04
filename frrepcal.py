#!/usr/bin/python3.7
# UTF8
# Date:
# Author: Nicolas Flandrois

import datetime


class FrRepCal(object):
    """FrRepCal will Handle French Republican Dates"""
    monthNames = [
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
                'Primidi',
                'Duodi',
                'Tridi',
                'Quartidi',
                'Quintidi',
                'Sextidi',
                'Septidi',
                'Octidi',
                'Nonidi',
                'Décadi'
                ]

    sansculottides = [
                      'La Fête de la Vertu',
                      'La Fête du Génie',
                      'La Fête du Travail',
                      'La Fête de l\'Opinion',
                      'La Fête des Récompenses',
                      'La Fête de la Révolution'
                      ]


class GregorianDate(object):
    """GregorianDate will manage Gregorian Dates"""

    def nowdate():
        """
        Returns Date Now at time of coputation, local time,
        Gregorian callendar, as a date tuple.
        """
        return datetime.datetime.now().timetuple()

    def leapyr(year: int):
        """"
        This function defines if the year is
        a Leap year (366 days)
        or a Normal year (365 days).
        Then it will to the variable n the value of 366 or 365, accordingly.
        Returns a Tuple:
            - number of days tha year,
            - and a Boolean :
                            True == Leap Year
                            False == Normal Year
        """
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            n = 366
            leapyear = True

        else:
            n = 365
            leapyear = False

        return (n, leapyear)


class Compute(object):
    """Compute will manage all calculation to Convert and translate."""

    def convert(DateTuple):
        """
        The convert function, computes Gregorian Dates into
        French Republican Dates.
        Takes a Date Tuple, and Returning Dictionnary.
        """
        totalYrdays = GregorianDate.leapyr(DateTuple[0])
        endYrConstant = 100
        leapyear = totalYrdays[1]


        if DateTuple[7] < (totalYrdays[0] - 100):
            fr_year = DateTuple[0] - 1792
            fr_yrday = DateTuple[7] + endYrConstant
            fr_yrweek = fr_yrday // 10

            if fr_yrday > 360: # Define the Sansculottides exception.
                fr_month = FrRepCal.monthNames[-1]
                fr_decade = None
                fr_weekday = FrRepCal.sansculottides[fr_yrday - 360]
                fr_monthday = fr_yrday - 359

            else:
                fr_month = FrRepCal.monthNames[(fr_yrweek // 3)]
                fr_decade = (fr_yrweek % 3)+1
                fr_weekday = FrRepCal.dayNames[(fr_yrday % 10)]
                fr_monthday = (((fr_yrday // 10) % 3)+1 * 10) + (fr_yrday % 10)

        else:
            fr_year = DateTuple[0] - 1792 + 1
            fr_yrday = DateTuple[7] - (totalYrdays[0] - endYrConstant)
            fr_yrweek = fr_yrday // 10
            fr_month = FrRepCal.monthNames[(fr_yrweek // 3)]
            fr_decade = fr_yrweek % 3
            fr_weekday = FrRepCal.dayNames[(fr_yrday % 10)-1]
            fr_monthday = (((fr_yrday // 10) % 3)+1 * 10) + (fr_yrday % 10)

        return {
                'FrRep_Year':fr_year,  # Integer
                'FrRep_Month':fr_month,  # String
                'FrRep_Decade':fr_decade,  # Integer
                'FrRep_Weekday':fr_weekday,  # String
                'leapYear':leapyear,  # Boolean
                'FrRep_MonthDay': fr_monthday,  # Integer
                'FrRep_YearWeek':fr_yrweek + 1,  # Integer
                'FrRep_YearMonth': (fr_yrweek // 3) + 1,  # Integer
                'FrRep_YearDay':fr_yrday + 1  # Integer
                }

    # def translate(FrRepDateDict):
    #     """
    #     The Translate function, computes Fr. Rep. Dates back into Gregorian Dates.
    #     It returns a Date time Tuple.
    #     """


class View(object):
    """ View returns readable dates in each section, as readable String"""

    def frrepdate_official(dictdate: dict):
        """Returns a readable string, as French Republican Date.
        Commun Official Format."""
        return f"Année {dictdate['FrRep_Year']} de la République Française, \
Mois de {dictdate['FrRep_Month']}, Décade {dictdate['FrRep_Decade']}, \
Jour du {dictdate['FrRep_Weekday']}"

    def frrepdate_unofficial(dictdate):
        """Returns a readable string, as French Republican Date.
        Unofficial Format"""
        return f"An {dictdate['FrRep_Year']} de la République, \
{dictdate['FrRep_MonthDay']} {dictdate['FrRep_Month']}"

    def gregorian_date(date):
        """Given a Date Tupple, will return the Gregorian date
        as a readable String."""
        dstring = f"{date[0]} {date[1]} {date[2]}"
        d = datetime.datetime.strptime(dstring, '%Y %m %d')
        return d.strftime('%A, %Y %B %d')


# class Input(object):
#     """Asking for Input in a specific Format,
#     and convert it in a Specific Format accordingly,
#     either French Republican Date Dictionary, or Gregorian Date Tuple."""
#     def __init__(self, arg):
#         super(Input, self).__init__()
#         self.arg = arg


# class Menu/APP(object):
#             """Menu (or name it APP?)Will Manage the App"""
#             def __init__(self, arg):
#                 super(Menu, self).__init__()
#                 self.arg = arg

# Test
# print(GregorianDate.nowdate())
# print(View.gregorian_date(GregorianDate.nowdate()))
# print(View.frrepdate_unofficial(Compute.convert(GregorianDate.nowdate())))
