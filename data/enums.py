from enum import Enum, unique


@unique
class CommonEnum(Enum):

    def describe(self):
        return self.name, self.value


class MOS(CommonEnum):

    MOS1 = 1


class HighestEducation(CommonEnum):

    HIGH_SCHOOL_DEGREE = ('HSD', 'High School Degree')
    SOME_COLLEGE = ('SC', 'Some College, No Degree')
    ASSOCIATES_DEGREE = ('AD', 'Associates Degree')
    BACHELORS_DEGREE = ('BD', 'Bachelors Degree')
    MASTERS_DEGREE = ('MD', 'Masters Degree')
    PHD_DEGREE = ('PHD', 'PHD Degree')

    def __init__(self, code, description):
        self.code = code
        self.description = description


class Rank(CommonEnum):

    PVT = ('PVT', 'PRIVATE')
    PV2 = ('PV2', 'PRIVATE SECOND CLASS')
    PFC = ('PFC', 'PRIVATE FIRST CLASS')
    SPC = ('SPC', 'SPECIALIST')
    CPL = ('CPL', 'CORPORAL')
    SGT = ('SGT', 'SERGEANT')
    SSG = ('SSG', 'STAFF SERGEANT')
    SFC = ('SFC', 'SERGEANT FIRST CLASS')
    MSG = ('MSG', 'MASTER SERGEANT')
    SG1 = ('1SG', 'FIRST SERGEANT')
    SGM = ('SGM', 'SERGEANT MAJOR')
    CSM = ('CSM', 'COMMAND SERGEANT MAJOR')
    SMA = ('SMA', 'SERGEANT MAJOR OF THE ARMY')
    WO1 = ('WO1', 'WARRANT OFFICER')
    CS2 = ('CS2', 'CHIEF WARRANT OFFICER 2')
    CW3 = ('CW3', 'CHIEF WARRANT OFFICER 3')
    CW4 = ('CW4', 'CHIEF WARRANT OFFICER 4')
    CW5 = ('CW5', 'CHIEF WARRANT OFFICER 5')
    LT2 = ('2LT', 'SECOND LIEUTENANT')
    LT1 = ('1LT', 'FIRST LIEUTENANT')
    CPT = ('CPT', 'CAPTAIN')
    MAJ = ('MAJ', 'MAJOR')
    LTC = ('LTC', 'LIEUTENANT COLONEL')
    COL = ('COL', 'COLONEL')
    BG = ('BG', 'BRIGADIER GENERAL')
    MG = ('MG', 'MAJOR GENERAL')
    LTG = ('LTG', 'LIEUTENANT GENERAL')
    GEN = ('GEN', 'GENERAL')
    GOA = ('GOA', 'GENERAL OF THE ARMY')

    def __init__(self, rank_abbrev, rank_full_title):
        self.rank_abbrev = rank_abbrev
        self.rank_full_title = rank_full_title


class TDYUnit(CommonEnum):

    TDY1 = 1

class OtherUnits(CommonEnum):

    OSUT = 1
    Airborne = 2
    SFAS =3

