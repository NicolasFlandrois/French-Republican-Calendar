# French-Republican-Calendar
Python Converter of ISO Dates into, and translate from, French Republican Calendar

------------------------------
**Author**: Nicolas Flandrois

**Date**: Wed 04 Sep 2019 14:12:52 CEST

**License**: MIT License - Copyright (c) 2019 Nicolas Flandrois

**Version**: v1

------------------------------
What is a French Republican Calendar?
=====================================

The French Republican calendar (French: calendrier républicain français), also commonly called the French Revolutionary calendar (calendrier révolutionnaire français), was a calendar created and implemented during the French Revolution, and **used by the French government for about 12 years from late *1793* to *1805***, and for **18 days by the Paris Commune in *1871***. The revolutionary system was designed in part to remove all religious and royalist influences from the calendar, and was part of a larger attempt at decimalisation in France (which also included decimal time of day, decimalisation of currency, and metrication). It was used in government records in France and other areas under French rule, including Belgium, Luxembourg, and parts of the Netherlands, Germany, Switzerland, Malta, and Italy.

[Source Wikipedia: French Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar)

## Month Names:

The Republican calendar **year began** the **day the autumnal equinox occurred in Paris**, and had **twelve months of 30 days each**, which were given new names based on nature, principally having to do with the prevailing weather in and around Paris. The **extra five or six days in the year** were not given a month designation, but considered **Sansculottides** or Complementary Days.

+ ***Autumn***:
    - **Vendémiaire** (from French vendange, derived from Latin vindemia, "grape harvest"), starting 22, 23, or 24 September
    - **Brumaire** (from French brume, "mist"), starting 22, 23, or 24 October
    - **Frimaire** (From French frimas, "frost"), starting 21, 22, or 23 November
+ ***Winter***:
    - **Nivôse** (from Latin nivosus, "snowy"), starting 21, 22, or 23 December
    - **Pluviôse** (from French pluvieux, derived from Latin pluvius, "rainy"), starting 20, 21, or 22 January
    - **Ventôse** (from French venteux, derived from Latin ventosus, "windy"), starting 19, 20, or 21 February
+ ***Spring***:
    - **Germinal** (from French germination), starting 20 or 21 March
    - **Floréal** (from French fleur, derived from Latin flos, "flower"), starting 20 or 21 April
    - **Prairial** (from French prairie, "meadow"), starting 20 or 21 May
+ ***Summer***:
    - **Messidor** (from Latin messis, "harvest"), starting 19 or 20 June
    - **Thermidor** (or Fervidor^[1]) (from Greek thermon, "summer heat"), starting 19 or 20 July
    - **Fructidor** (from Latin fructus, "fruit"), starting 18 or 19 August

[1] Note: On many printed calendars of Year II (1793–94), the month of Thermidor was named Fervidor (from Latin fervidus, "burning hot").

Most of the month names were new words coined from French, Latin, or Greek. The endings of the names are grouped by season. "Dor" means "giving" in Greek.

[Source Wikipedia: French Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar)

## Ten days of the week

The month is divided into three décades or "weeks" of ten days each, named simply:

- **primidi** (first day)
- **duodi** (second day)
- **tridi** (third day)
- **quartidi** (fourth day)
- **quintidi** (fifth day)
- **sextidi** (sixth day)
- **septidi** (seventh day)
- **octidi** (eighth day)
- **nonidi** (ninth day)
- **décadi** (tenth day)

Décades were abandoned in Floréal an X (April 1802).

[Source Wikipedia: French Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar)

## Complementary days/Sansculottides

Five extra days – six in leap years – were national holidays at the end of every year. These were originally known as les sans-culottides (after sans-culottes), but after year III (1795) as les jours complémentaires:

- 1st complementary day: ***La Fête de la Vertu***, "Celebration of Virtue", on 17 or 18 September
- 2nd complementary day: ***La Fête du Génie***, "Celebration of Talent", on 18 or 19 September
- 3rd complementary day: ***La Fête du Travail***, "Celebration of Labour", on 19 or 20 September
- 4th complementary day: ***La Fête de l'Opinion***, "Celebration of Convictions", on 20 or 21 September
- 5th complementary day: ***La Fête des Récompenses***, "Celebration of Honors (Awards)", on 21 or 22 September
- 6th complementary day: ***La Fête de la Révolution***, "Celebration of the Revolution", on 22 or 23 September (on leap years only)

[Source Wikipedia: French Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar)

## Converting from the Gregorian Calendar

Below are the Gregorian dates each Republican year (an in French) began while the calendar was in effect.

|**An**    |      **Gregorian**       |
|----------|--------------------------|
|I (1)     |  22 September 1792       |
|II (2)    |  22 September 1793       |
|III (3)   |  22 September 1794       |
|IV (4)    |  23 September 1795^[2]   |
|V (5)     |  22 September 1796       |
|VI (6)    |  22 September 1797       |
|VII (7)   |  22 September 1798       |
|VIII (8)  |  23 September 1799^[2]   |
|IX (9)    |  23 September 1800       |
|X (10)    |  23 September 1801       |
|XI (11)   |  23 September 1802       |
|XII (12)  |  24 September 1803^[2]   |
|XIII (13) |  23 September 1804       |
|XIV (14)  |  23 September 1805       |

*[2] Extra (sextile) day inserted before date, due to previous leap year*

The calendar was abolished in the year XIV (1805). After this date, opinions seem to differ on the method by which the leap years would have been determined if the calendar were still in force. There are at least four hypotheses used to convert dates from the Gregorian calendar:

+ **Equinox**: The leap years would continue to vary in order to ensure that each year the autumnal equinox in Paris falls on 1 Vendémiaire, as was the case from year I to year XIV. This is the only method that was ever in legal effect, although it means that sometimes five years pass between leap years, such as the years 15 and 20.

+ **Romme**: Leap years would have fallen on each year divisible by four (thus in 20, 24, 28...), except most century years, according to Romme's proposed fixed rules. This would have simplified conversions between the Republican and Gregorian calendars since the Republican leap day would usually follow a few months after 29 February, at the end of each year divisible by four, so that the date of the Republican New Year remains the same (22 September) in the Gregorian calendar for the entire third century of the Republican Era (AD 1992–2091).

+ **Continuous**: The leap years would have continued in a fixed rule every four years from the last one (thus years 15, 19, 23, 27...) with the leap day added before, rather than after, each year divisible by four, except most century years. This rule has the advantage that it is both simple to calculate and is continuous with every year in which the calendar was in official use during the First Republic. Some concordances were printed in France, after the Republican Calendar was abandoned, using this rule to determine dates for long-term contracts.

+ **128-Year**: Beginning with year 20, years divisible by four would be leap years, except for years divisible by 128. Note that this rule was first proposed by von Mädler, and not until the late 19th century. The date of the Republican New Year remains the same (23 September) in the Gregorian calendar every year from 129 to 256 (AD 1920–2047).

The following table shows when several years of the Republican Era begin on the Gregorian calendar, according to each of the four above methods:

|**An Rep. Fr**     | **AD/CE**  | **Equinox**       |  **Romme**          | **Continuous**     | **128-Year**     |
|-------------------|------------|-------------------|---------------------|--------------------|------------------|
|XV (15)            |     1806   | 23 September      |  23 September       | 23 September       | 23 September     |
|XVI (16)           |     1807   | 24 September^[3]  |  23 September       | 24 September^[3]   | 24 September^[3] |
|XVII (17)          |     1808   | 23 September      |  23 September^[3]   | 23 September       | 23 September     |
|XVIII (18)         |     1809   | 23 September      |  23 September       | 23 September       | 23 September     |
|XIX (19)           |     1810   | 23 September      |  23 September       | 23 September       | 23 September     |
|XX (20)            |     1811   | 23 September      |  23 September       | 24 September^[3]   | 23 September     |
|CCXXVI (226)       |     2017   | 22 September      |  22 September       | 22 September       | 23 September     |
|CCXXVII (227)      |     2018   | 23 September^[3]  |  22 September       | 22 September       | 23 September     |
|CCXXVIII (228)     |     2019   | 23 September      |  22 September       | 23 September^[3]   | 23 September     |
|CCXXIX (229)       |     2020   | 22 September      |  22 September^[3]   | 22 September       | 23 September^[3] |

*[3]Extra (sextile) day inserted before date, due to previous leap year*

[Source Wikipedia: French Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar)

---------------------------------------------------------------------------
Ideas Taken in Considerations during Development
================================================

For the Computations we will consider the Following points:

- The Year ALWAYS starts on September 22nd, of each Year.

- We will apply leap years as they occure in the Gregorian Calendar. Easier to manage.

- Day 1 of the Calendar == **22 September 1792**  == Année I de la République Française, mois du Vendémiaire, Decade I, jour du primidi.

- Lists of names:

    + Month's Names =   ['Vendémiaire',
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
                        'Sansculottides']

    + Day's Names =     ['primidi',
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

    + Sansculottides =  ['La Fête de la Vertu',
                         'La Fête du Génie',
                         'La Fête du Travail',
                         'La Fête de l\'Opinion',
                         'La Fête des Récompenses',
                         'La Fête de la Révolution']

- Convertion Table:

    + 1 week = 10 days

    + 1 month = 3 weeks = 30 days
    + 1 season = 3 month = 9 weeks = 90 days

    + 1 year = 4 seasons = 12 months = 36 weeks = 360 days

    + 1 year + Sanscullotides:

        - Leap Year == True:

            + 1 year + Sanscullotides = 366 days (360 + 6)

        - Leap Year == False:

            + 1 year + Sanscullotides = 365 days (360 + 5)

--------------------
How To Use This Program?
========================

## Requierements & Dependencies

This program is initially created to run in Python, from the terminal.

It has been developed in **Python 3.7**.

*(If you use earlier Python versions, String formating needs to be adapted accordingly.)*

Nos other dependencies are needed, as it's been developed with standard Python 3.7 modules, and libraries.

## How to run the Program?

1. With Python 3.7 launch the program in your interpreter or terminal.

        python3.7 frrepcal.py

2. Follow the instructions from the Menu.

At launch the current Gregorian and Frenc Republican Dates will be given Automatically.

From Menu options, you can either:

- Convert a Gregorian Date into a French Republican date. (Following the instructions to input the Gregorian Date.)

- Translate a French Republican Date into a Gregorian date. (Following the instructions to input the French Rep. Date.)

- Compute Today's Gregorian Date. In the enventuality you used other options, then came back to main menu, and needed once again today's French Rep. Date.

- Go to Main menu (Basically will display the same present menu, without the Auto Todays' French Rep. Date on top.)

- Quit the program
