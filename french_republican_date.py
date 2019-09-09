#!/usr/bin/python3.7
# UTF8
# Date: Wed 04 Sep 2019 14:12:52 CEST
# Author: Nicolas Flandrois

import datetime
from sys import exit
import wikipedia


class FrRepCal(object):
    """FrRepCal (French Republican Calendar) will handle
    French Republican Dates data and constants"""
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

        # Note a constant of 100 days timedelta is set
        # between Sept 22 and Dec 31

        if DateTuple[7] < (totalYrdays[0] - 100):  # Dates [01 Jan - 21 Sept]
            # This if condition defines if your date is bellow or
            # over Sept 22nd.
            # (totalYrdays[0] - 100) defines ISO Year day for Sept 22nd in a
            # leap Year of not
            fr_year = DateTuple[0] - 1792
            fr_yrday = DateTuple[7] + 100
            fr_yrweek = fr_yrday // 10

            if fr_yrday > 359:  # Define the Sansculottides exception.
                fr_month = FrRepCal.monthNames[-1]
                fr_decade = None
                fr_weekday = FrRepCal.sansculottides[fr_yrday - 360]
                fr_monthday = fr_yrday - 359

            else:  # Normal days (Non sansculottides days)
                fr_month = FrRepCal.monthNames[(fr_yrweek // 3)]
                fr_decade = (fr_yrweek % 3)+1
                fr_weekday = FrRepCal.dayNames[(fr_yrday % 10)]
                fr_monthday = (fr_yrday % 30) + 1

        else:  # Dates [22 Sept - 31 Dec]
            fr_year = DateTuple[0] - 1792 + 1
            fr_yrday = DateTuple[7] - (totalYrdays[0] - 100)
            fr_yrweek = fr_yrday // 10
            fr_month = FrRepCal.monthNames[(fr_yrweek // 3)]
            fr_decade = (fr_yrweek % 3) + 1
            fr_weekday = FrRepCal.dayNames[(fr_yrday % 10)]
            fr_monthday = (fr_yrday % 30) + 1

        return {
                'FrRep_Year': fr_year,  # Integer
                'FrRep_Month': fr_month,  # String
                'FrRep_Decade': fr_decade,  # Integer
                'FrRep_Weekday': fr_weekday,  # String
                'leapYear': totalYrdays[1],  # Boolean
                'FrRep_MonthDay': fr_monthday,  # Integer
                'FrRep_YearWeek': fr_yrweek + 1,  # Integer
                'FrRep_YearMonth': (fr_yrweek // 3) + 1,  # Integer
                'FrRep_YearDay': fr_yrday + 1  # Integer
                }
        # I could implement the dictionary directly as I create
        # them along the way. However This way Here, we can have a
        # clearer view of what comes from where, and the type of data
        # (cf inline comments).

    def translate(fr_date: dict):
        """
        The Translate function, computes Fr. Rep. Dates back into Gregorian
        Dates.
        It returns a Date time Tuple.
        """
        fr_year = fr_date['FrRep_Year']
        fr_yrday = fr_date['FrRep_YearDay']

        if fr_yrday in range(1, 102):
            year = fr_year + 1791  # (1792 - 1)
            yearday = fr_yrday + (GregorianDate.leapyr(year)[0] - 101)
        else:
            year = fr_year + 1792
            yearday = fr_yrday-101

        return datetime.datetime.strptime(f'{year} {yearday}', '%Y %j')\
            .timetuple()


class View(object):
    """ View returns readable dates in each section, as readable String"""

    def fr_date_b1802(date: dict):
        """
        french_republican_date_early_format_before1802(date: dict)
        Returns a readable string, as French Republican Date.
        Commun Official Format.
        Dates as use before Décades were abandoned in
        'Floréal de l'an X' (April 1802).
        """
        return f"Année {date['FrRep_Year']} de la République Française, \
Mois de {date['FrRep_Month']}, Décade {date['FrRep_Decade']}, \
Jour du {date['FrRep_Weekday']}"

    def fr_date_a1802(date: dict):
        """
        french_repuplican_date_late_format_after1802(date: dict)
        Returns a readable string, as French Republican Date.
        Unofficial Format.
        Dates as use after Décades were abandoned in
        'Floréal de l'an X' (April 1802).
        """
        return f"{date['FrRep_MonthDay']} {date['FrRep_Month']}, \
de l'An {date['FrRep_Year']} de la République"

    def gregorian_date(date):
        """Given a Date Tupple, will return the Gregorian date
        as a readable String."""
        return datetime.datetime.strptime((f"{date[0]} {date[1]} {date[2]}"),
                                          '%Y %m %d').strftime('%A, %Y %B %d')


# class Input(object):
#     """Asking for Input in a specific Format,
#     and convert it in a Specific Format accordingly,
#     either French Republican Date Dictionary, or Gregorian Date Tuple."""


class App(object):
    """App will Manage the App"""
# Menu Choices:
# Print() > Disclaimer, See README on calculations, and considered approche
# to dev. ROMME Computation(Or add this disclaimer in the menu)
# 1/ Today's Fr Rep Date
    # a/ To Long Format (Before 1802)
    # b/ To Short Format (After 1802)
    # c/ Return to main menu
    # d/ Quit
# 2/ Convert a Greg Date into Fr Rep Date
    # a/ To Long Format (Before 1802)
    # b/ To Short Format (After 1802)
    # c/ Return to main menu
    # d/ Quit
# 3/ Translate a Fr Rep Date into Greg Date
    # a/ From Long Format (Before 1802)
    # b/ From Short Format (After 1802)
    # c/ Return to main menu
    # d/ Quit
# 4/ What is The French Republican Calendar
#       wikipedia.summary('French_Republican_calendar')
#       wikipedia.page('French_Republican_calendar').url
# 5/ Return to main menu
# 6/ Quit


    def clean():
        """
        This function will clear the terminal's screen. The command is
        automaticaly detected according to the system OS you run it.
        Compatible with Windows, OSx, and Linux.
        """
        os.system("cls" if platform.system() == "Windows" else "clear")


    def ask_integer(message: str, range, error_message: str = ""):
        """
        This function's purpose is to ask and verify an Integer.
        """
        var = None
        while True:
            try:
                var = int(input(message))
                if var in range:
                    return var
                    raise

            except KeyboardInterrupt:
                break

            except:
                print(error_message)


    def wikipedia(request: str):
        """
        Given a String, this function will fetch a wikipedia summary, and URL.
        If not found, or exception raised, an error message will be displaid.
        """
        try:
            return(wikipedia.summary(request), wikipedia.page(request).url)
        except:
            return ('Information not found.', 'Information not found.')


    # @staticmethod
    # def menu(question, choices=None):
    #   """skeleton menu's view for each query and set of question."""
    #   clean()
    #   print(question)
    #   if choices:
    #       for num, choice in enumerate(choices):
    #           print(str(num+1) + " : " + choice)
    #   print('\n(Appuyer sur: Q pour QUITTER ou \
    # R pour RETOUR au menu précédent.)\n')
    #   while True:
    #       try:
    #           choice = input()
    #           if choice.strip().lower() in ['r', 'q']:
    #               break
    #           elif choices:
    #               choice = int(choice)
    #               if choice in range(1, len(choices)+1):
    #                   break
    #               else:
    #                   raise
    #       except:
    #           print(
    #               "Veuillez entrer un nombre entre 1 et " +
    #               str(len(choices)) + "."
    #               )
    #   return choice


  # def main_menu():
  #     """
  #     Main Menu:
  #       1/ Today's Fr Rep Date
  #       2/ Convert a Greg Date into Fr Rep Date
  #       3/ Translate a Fr Rep Date into Greg Date
  #       4/ What is The French Republican Calendar
  #       5/ Return to main menu
  #       6/ Quit
  #     """
  # Using the (generic) Menu function


  # def sub_menu():
  #     """
  #     Sub Menu:
  #       a/ Long Format (Before 1802)
  #       b/ Short Format (After 1802)
  #       c/ Return to main menu
  #       d/ Quit
  #     """
  # Using the (generic) Menu function


  # def main():
  #   """
  #   This function will run the program according to user story, and menu logic.
  #   """
  # Exemple:
  #       def set_view(view, top_level=False):
  #           res = view()
  #           if res == "r":
  #               if not top_level:
  #                   return None
  #           elif res == "q":
  #               exit()
  #           else:
  #               return res


  #       def main():
  #           """Program's Main running function."""

  #           while True:
  #               res = set_view(View.main_view, True)
  #               if res == 1:
  #                   while True:
  #                       cat_id = set_view(View.cats_view)
  #                       if cat_id:
  #                           while True:
  #                               prod_id = set_view(lambda: View.prods_view(cat_id))
  #                               if not prod_id:
  #                                   break
  #                               while True:
  #                                   set_view(lambda: View.sheet_view(prod_id))
  #                                   set_view(lambda: View.substitution(prod_id))
  #                                   break
  #                       if not cat_id:
  #                           break

  #               elif res == 2:
  #                   set_view(View.sub_tbl)
  #                   res = set_view(lambda: View.menu("Question:", [
  #                       "Retour Menu Principal", "Quitter"]))
  #                   if res == 2:
  #                       exit()
  #                   if not res:
  #                       continue

# if __name__ == '__main__':
#     App.main()
