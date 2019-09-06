#!/usr/bin/python3.7
# UTF8
# Date: Wed 04 Sep 2019 14:12:52 CEST
# Author: Nicolas Flandrois
# Unit Test were done, using pytest==5.1.2 & pytest-watch==4.2.0
# Those are not part of the requirements.txt dependencies, as they have no
# incidences in the program's functionning.

from french_republican_date import *
import datetime
import time


def test_today():
    """Testing The get today's date function"""
    assert GregorianDate.nowdate() == datetime.datetime.today().timetuple()
    assert type(GregorianDate.nowdate()) == time.struct_time


def test_leapyr():
    assert type(GregorianDate.leapyr(2019)[0]) == int
    assert GregorianDate.leapyr(2019)[0] == 365
    assert GregorianDate.leapyr(2020)[0] == 366
    assert type(GregorianDate.leapyr(2019)[1]) == bool
    assert GregorianDate.leapyr(2019)[1] is False
    assert GregorianDate.leapyr(2020)[1] is True


def test_view_gregorian_date():
    assert View.gregorian_date(datetime.date(2019, 1, 1).timetuple()) == \
        "Tuesday, 2019 January 01"
    assert View.gregorian_date(datetime.date(2019, 4, 1).timetuple()) == \
        "Monday, 2019 April 01"
    assert View.gregorian_date(datetime.date(2019, 9, 16).timetuple()) == \
        "Monday, 2019 September 16"
    assert View.gregorian_date(datetime.date(2019, 9, 20).timetuple()) == \
        "Friday, 2019 September 20"
    assert View.gregorian_date(datetime.date(2019, 9, 22).timetuple()) == \
        "Sunday, 2019 September 22"
    assert View.gregorian_date(datetime.date(2019, 12, 31).timetuple()) == \
        "Tuesday, 2019 December 31"


def test_compute_convert():
    assert type(Compute.convert(GregorianDate.nowdate())) == dict
    assert Compute.convert(datetime.date(2019, 1, 1).timetuple()) == \
        {'FrRep_Year': 227, 'FrRep_Month': 'Nivôse', 'FrRep_Decade': 2,
            'FrRep_Weekday': 'Duodi', 'leapYear': False, 'FrRep_MonthDay': 12,
            'FrRep_YearWeek': 11, 'FrRep_YearMonth': 4, 'FrRep_YearDay': 102}
    assert Compute.convert(datetime.date(2019, 4, 1).timetuple()) == \
        {'FrRep_Year': 227, 'FrRep_Month': 'Germinal', 'FrRep_Decade': 2,
            'FrRep_Weekday': 'Duodi', 'leapYear': False, 'FrRep_MonthDay': 12,
            'FrRep_YearWeek': 20, 'FrRep_YearMonth': 7, 'FrRep_YearDay': 192}
    assert Compute.convert(datetime.date(2019, 9, 16).timetuple()) == \
        {'FrRep_Year': 227, 'FrRep_Month': 'Fructidor', 'FrRep_Decade': 3,
            'FrRep_Weekday': 'Décadi', 'leapYear': False,
            'FrRep_MonthDay': 30,
            'FrRep_YearWeek': 36, 'FrRep_YearMonth': 12, 'FrRep_YearDay': 360}
    assert Compute.convert(datetime.date(2019, 9, 20).timetuple()) == \
        {'FrRep_Year': 227, 'FrRep_Month': 'Sansculottides',
            'FrRep_Decade': None,
            'FrRep_Weekday': "La Fête de l'Opinion", 'leapYear': False,
            'FrRep_MonthDay': 4, 'FrRep_YearWeek': 37, 'FrRep_YearMonth': 13,
            'FrRep_YearDay': 364}
    assert Compute.convert(datetime.date(2019, 9, 22).timetuple()) == \
        {'FrRep_Year': 228, 'FrRep_Month': 'Vendémiaire', 'FrRep_Decade': 0,
            'FrRep_Weekday': 'Décadi', 'leapYear': False, 'FrRep_MonthDay': 1,
            'FrRep_YearWeek': 1, 'FrRep_YearMonth': 1, 'FrRep_YearDay': 1}
    assert Compute.convert(datetime.date(2019, 12, 31).timetuple()) == \
        {'FrRep_Year': 228, 'FrRep_Month': 'Nivôse', 'FrRep_Decade': 1,
            'FrRep_Weekday': 'Décadi', 'leapYear': False, 'FrRep_MonthDay': 11,
            'FrRep_YearWeek': 11, 'FrRep_YearMonth': 4, 'FrRep_YearDay': 101}


def test_compute_translate():
    assert type(Compute.translate({'FrRep_Year': 227, 'FrRep_Month': 'Nivôse',
                                   'FrRep_Decade': 2, 'FrRep_Weekday': 'Duodi',
                                   'leapYear': False, 'FrRep_MonthDay': 12,
                                   'FrRep_YearWeek': 11, 'FrRep_YearMonth': 4,
                                   'FrRep_YearDay': 102})) == time.struct_time
    assert Compute.translate({'FrRep_Year': 227, 'FrRep_Month': 'Nivôse',
                              'FrRep_Decade': 2, 'FrRep_Weekday': 'Duodi',
                              'leapYear': False, 'FrRep_MonthDay': 12,
                              'FrRep_YearWeek': 11, 'FrRep_YearMonth': 4,
                              'FrRep_YearDay': 102}) == \
        datetime.date(2019, 1, 1).timetuple()
    assert Compute.translate({'FrRep_Year': 227, 'FrRep_Month': 'Germinal',
                              'FrRep_Decade': 2, 'FrRep_Weekday': 'Duodi',
                              'leapYear': False, 'FrRep_MonthDay': 12,
                              'FrRep_YearWeek': 20, 'FrRep_YearMonth': 7,
                              'FrRep_YearDay': 192}) == \
        datetime.date(2019, 4, 1).timetuple()
    assert Compute.translate({'FrRep_Year': 227, 'FrRep_Month': 'Fructidor',
                              'FrRep_Decade': 3, 'FrRep_Weekday': 'Décadi',
                              'leapYear': False, 'FrRep_MonthDay': 30,
                              'FrRep_YearWeek': 36, 'FrRep_YearMonth': 12,
                              'FrRep_YearDay': 360}) == \
        datetime.date(2019, 9, 16).timetuple()
    assert Compute.translate({'FrRep_Year': 227,
                              'FrRep_Month': 'Sansculottides',
                              'FrRep_Decade': None,
                              'FrRep_Weekday': "La Fête de l'Opinion",
                              'leapYear': False, 'FrRep_MonthDay': 4,
                              'FrRep_YearWeek': 37, 'FrRep_YearMonth': 13,
                              'FrRep_YearDay': 364}) == \
        datetime.date(2019, 9, 20).timetuple()
    assert Compute.translate({'FrRep_Year': 227,
                              'FrRep_Month': 'Sansculottides',
                              'FrRep_Decade': None,
                              'FrRep_Weekday': "La Fête de l'Opinion",
                              'leapYear': False, 'FrRep_MonthDay': 4,
                              'FrRep_YearWeek': 37, 'FrRep_YearMonth': 13,
                              'FrRep_YearDay': 365}) == \
        datetime.date(2019, 9, 21).timetuple()
    assert Compute.translate({'FrRep_Year': 228, 'FrRep_Month': 'Vendémiaire',
                              'FrRep_Decade': 0, 'FrRep_Weekday': 'Décadi',
                              'leapYear': False, 'FrRep_MonthDay': 1,
                              'FrRep_YearWeek': 1, 'FrRep_YearMonth': 1,
                              'FrRep_YearDay': 1}) == \
        datetime.date(2019, 9, 22).timetuple()
    assert Compute.translate({'FrRep_Year': 228, 'FrRep_Month': 'Vendémiaire',
                              'FrRep_Decade': 0, 'FrRep_Weekday': 'Décadi',
                              'leapYear': False, 'FrRep_MonthDay': 1,
                              'FrRep_YearWeek': 1, 'FrRep_YearMonth': 1,
                              'FrRep_YearDay': 2}) == \
        datetime.date(2019, 9, 23).timetuple()
    assert Compute.translate({'FrRep_Year': 228, 'FrRep_Month': 'Nivôse',
                              'FrRep_Decade': 1, 'FrRep_Weekday': 'Décadi',
                              'leapYear': False, 'FrRep_MonthDay': 11,
                              'FrRep_YearWeek': 11, 'FrRep_YearMonth': 4,
                              'FrRep_YearDay': 101}) == \
        datetime.date(2019, 12, 31).timetuple()


def test_view_b1802():
    assert type(View.fr_date_b1802(Compute.convert(GregorianDate.nowdate())))\
        == str
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 1, 1).
                                              timetuple())) == \
        "Année 227 de la République Française, Mois de Nivôse, Décade 2, \
Jour du Duodi"
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 4, 1).
                                              timetuple())) == \
        "Année 227 de la République Française, Mois de Germinal, Décade 2, \
Jour du Duodi"
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 9, 16).
                                              timetuple())) == \
        "Année 227 de la République Française, Mois de Fructidor, Décade 3, \
Jour du Décadi"
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 9, 20).
                                              timetuple())) == \
        "Année 227 de la République Française, Mois de Sansculottides, Décade\
 None, Jour du La Fête de l'Opinion"
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 9, 22).
                                              timetuple())) == \
        "Année 228 de la République Française, Mois de Vendémiaire, Décade 0, \
Jour du Décadi"
    assert View.fr_date_b1802(Compute.convert(datetime.date(2019, 12, 31).
                                              timetuple())) == \
        "Année 228 de la République Française, Mois de Nivôse, Décade 1, \
Jour du Décadi"


def test_view_a1802():
    assert type(View.fr_date_a1802(Compute.convert(GregorianDate.nowdate())))\
        == str
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 1, 1).
                                              timetuple())) == \
        "12 Nivôse, de l'An 227 de la République"
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 4, 1).
                                              timetuple())) == \
        "12 Germinal, de l'An 227 de la République"
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 9, 16).
                                              timetuple())) == \
        "30 Fructidor, de l'An 227 de la République"
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 9, 20).
                                              timetuple())) == \
        "4 Sansculottides, de l'An 227 de la République"
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 9, 22).
                                              timetuple())) == \
        "1 Vendémiaire, de l'An 228 de la République"
    assert View.fr_date_a1802(Compute.convert(datetime.date(2019, 12, 31).
                                              timetuple())) == \
        "11 Nivôse, de l'An 228 de la République"
