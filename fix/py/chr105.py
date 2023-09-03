import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr105.dat')

# id: 0x0000 offset: 0x2AA4
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'POSETEST',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR001_DF1',
            symbol     = 'IDLEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'FATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR105_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_ORDER',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT00_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT01_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR105_BT1',
            symbol     = 'BTL_CRAFT02_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_00_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_00_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_01_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_02_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_02_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_03_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_04_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_05_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_06_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_07_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_08_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_11_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_11_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR105_SC1',
            symbol     = 'BTL_S_CRAFT00_11a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR105_BT3',
            symbol     = 'BTL_WIN_HITOUCH_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR105_BT3',
            symbol     = 'BTL_WIN_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR105_BT3',
            symbol     = 'BTL_WIN_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_WAIT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_TILT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_TILT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_TILT_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_BACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_BACK_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_BACK_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_HANDLE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_HANDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_TILT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_BACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_HANDLE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_TILT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'BIKE_REAR_TILT_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_SIDE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR105_HS1',
            symbol     = 'BIKE_SIDE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'BTL_FLOAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'BTL_DOWNHILL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV04065',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV70000_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV70000_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV70001_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV70001_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV91010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV91010a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV91015',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV91015a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV91015b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIRE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIRE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIRE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKO_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKO_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BURIKKO_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_KATATE_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_KATATE_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ENZETU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FALLa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_FUAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GOUREI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_3_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HIRUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HIRUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HIRUMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HISOHISO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HISOHISOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HISOHISOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_JUMP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_JUMPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KATATE_DAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KATATE_DAKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KATATE_DAKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARDb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MAEKAGAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NAISHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NAISHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NAISHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_NORIDASIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MIRU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MIRUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MIRUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANF_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WARAI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAREYARE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC30',
            symbol     = 'EV_Z1_00_08_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC30',
            symbol     = 'EV_Z1_00_08_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11A',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11B',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11C',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_11D_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_13_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_16',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR105_EVC13',
            symbol     = 'EV_B3_14_00_1_16_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR105_MG12',
            symbol     = 'MG12_BANANA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR105_MG12',
            symbol     = 'MG12_BANANA_SLANT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR105_MG12',
            symbol     = 'MG12_BANANA_SLANT_R',
        ),
    )

# id: 0x0001 offset: 0xC2E0
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xC300
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xC318
@scena.Code('PreInit')
def PreInit():
    AnimeClipCmd(0x0D, PseudoChrId.Self)

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_C355',
    )

    AnimeClipCmd(0x0F, PseudoChrId.Self, 0x00)
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR105_DF1', 'WAIT')

    Return()

    def _loc_C355(): pass

    label('loc_C355')

    Return()

# id: 0x0004 offset: 0xC358
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "ModelCmd(0x3F)"),
            Expr.Return,
        ),
        'loc_C36A',
    )

    Return()

    def _loc_C36A(): pass

    label('loc_C36A')

    Call(ScriptId.Current, 'PlayFakeEffect')
    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0005 offset: 0xC3E0
@scena.Code('PlayFakeEffect')
def PlayFakeEffect():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_C46F',
    )

    LoadEffect(0xFFFE, 0x2F, 'system/shadow_chr_aura.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x002F), PseudoChrId.Self, 0x00000023, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_C46F(): pass

    label('loc_C46F')

    Return()

# id: 0x0006 offset: 0xC470
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0007 offset: 0xC498
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0008 offset: 0xC4C4
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0009 offset: 0xC4D0
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000A offset: 0xC4E0
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x000B offset: 0xC4F0
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR105_BT3')

    Return()

# id: 0x000C offset: 0xC508
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000D offset: 0xC518
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000E offset: 0xC528
@scena.Code('Ani_MG12_Load')
def Ani_MG12_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR105_MG12')

    Return()

# id: 0x000F offset: 0xC540
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0010 offset: 0xC550
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xC568
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR105_BT3')

    Return()

# id: 0x0012 offset: 0xC580
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0013 offset: 0xC598
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0014 offset: 0xC5B0
@scena.Code('Ani_MG12_Release')
def Ani_MG12_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR105_MG12')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0015 offset: 0xC5D4
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0016 offset: 0xC718
@scena.Code('AniAttachMainWeapon_L')
def AniAttachMainWeapon_L():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0017 offset: 0xC7C8
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU622')
    ReleaseAsset('C_EQU622')

    Return()

# id: 0x0018 offset: 0xC85C
@scena.Code('AniReset')
def AniReset():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_C891',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_C891(): pass

    label('loc_C891')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOn')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0019 offset: 0xC914
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001A offset: 0xC924
@scena.Code('AniResetWorkRun')
def AniResetWorkRun():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001B offset: 0xC934
@scena.Code('DefaultFace')
def DefaultFace():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_C988',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Jump('loc_C9B3')

    def _loc_C988(): pass

    label('loc_C988')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    def _loc_C9B3(): pass

    label('loc_C9B3')

    Return()

# id: 0x001C offset: 0xC9B4
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_C9CE',
    )

    Jump('loc_CA0F')

    def _loc_C9CE(): pass

    label('loc_C9CE')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_CA0F(): pass

    label('loc_CA0F')

    Return()

# id: 0x001D offset: 0xCA10
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x001E offset: 0xCA1C
@scena.Code('OnCampIn')
def OnCampIn():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x001F offset: 0xCA84
@scena.Code('OnCostumeIn')
def OnCostumeIn():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x0020 offset: 0xCAE8
@scena.Code('OnCostumeIn1')
def OnCostumeIn1():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x0021 offset: 0xCB60
@scena.Code('OnCostumeIn2')
def OnCostumeIn2():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '4', '', '#b', '0')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniIdle')

    Return()

# id: 0x0022 offset: 0xCBD0
@scena.Code('OnCostumeIn3')
def OnCostumeIn3():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'OnCostumeIn3_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x0023 offset: 0xCC68
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0024 offset: 0xCCC4
@scena.Code('AniFieldChange')
def AniFieldChange():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(1800), ParamInt(0x0709), ParamInt(0x070A), ParamInt(0))

    Return()

# id: 0x0025 offset: 0xCD00
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0026 offset: 0xCD30
@scena.Code('ShowEquipL')
def ShowEquipL():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0027 offset: 0xCD48
@scena.Code('ShowEquipR')
def ShowEquipR():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0028 offset: 0xCD60
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x0029 offset: 0xCD90
@scena.Code('EraseEquipL')
def EraseEquipL():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x002A offset: 0xCDA8
@scena.Code('EraseEquipR')
def EraseEquipR():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x002B offset: 0xCDC0
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'LeftHD02', 0.6)
    OP_8A(0xFE, 0xFFFE, 'BS01', 0.2)

    Return()

# id: 0x002C offset: 0xCDE8
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS01', 0.2)

    Return()

# id: 0x002D offset: 0xCE10
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x002E offset: 0xCE14
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x002F offset: 0xCE18
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x0030 offset: 0xCE1C
@scena.Code('AniEv04065')
def AniEv04065():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV04065', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0031 offset: 0xCE50
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0032 offset: 0xCF6C
@scena.Code('AniEv70000_3')
def AniEv70000_3():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70000_3', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70000_3a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xCFD8
@scena.Code('AniEv70001_3')
def AniEv70001_3():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70001_3', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70001_3a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0034 offset: 0xD044
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x0035 offset: 0xD048
@scena.Code('AniWait')
def AniWait():
    Call(ScriptId.Current, 'SpringOn')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D108',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D0DB',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_D0FF')

    def _loc_D0DB(): pass

    label('loc_D0DB')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D0FF(): pass

    label('loc_D0FF')

    Jump('loc_D4E1')

    def _loc_D108(): pass

    label('loc_D108')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D2B0',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D161',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_D161(): pass

    label('loc_D161')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F0',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_D2A7')

    def _loc_D1F0(): pass

    label('loc_D1F0')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D280',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_D2A7')

    def _loc_D280(): pass

    label('loc_D280')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_D2A7(): pass

    label('loc_D2A7')

    Jump('loc_D4E1')

    def _loc_D2B0(): pass

    label('loc_D2B0')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_D30C',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_D4E1')

    def _loc_D30C(): pass

    label('loc_D30C')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D3A5',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.13)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_D4E1')

    def _loc_D3A5(): pass

    label('loc_D3A5')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D437',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.1)
    OP_AD(0x02, 0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_D4E1')

    def _loc_D437(): pass

    label('loc_D437')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4B5',
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_D4E1')

    def _loc_D4B5(): pass

    label('loc_D4B5')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_D4E1(): pass

    label('loc_D4E1')

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0036 offset: 0xD508
@scena.Code('AniWalk')
def AniWalk():
    Call(ScriptId.Current, 'ResetModel1')
    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D5C9',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D599',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_D599(): pass

    label('loc_D599')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_D640')

    def _loc_D5C9(): pass

    label('loc_D5C9')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D61D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_D61D(): pass

    label('loc_D61D')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D640(): pass

    label('loc_D640')

    Sleep(166)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0037 offset: 0xD670
@scena.Code('AniRun')
def AniRun():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D6E4',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_D706')

    def _loc_D6E4(): pass

    label('loc_D6E4')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D706(): pass

    label('loc_D706')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D725',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D725(): pass

    label('loc_D725')

    Sleep(666)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0038 offset: 0xD748
@scena.Code('AniDash')
def AniDash():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D7BC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_D7DF')

    def _loc_D7BC(): pass

    label('loc_D7BC')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D7DF(): pass

    label('loc_D7DF')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D7FE',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D7FE(): pass

    label('loc_D7FE')

    Sleep(666)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0039 offset: 0xD820
@scena.Code('AniBack')
def AniBack():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(166)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003A offset: 0xD87C
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x003B offset: 0xD8C0
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x003C offset: 0xD900
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D9F5',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D994',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnL')

    Jump('loc_D9EC')

    def _loc_D994(): pass

    label('loc_D994')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D9EC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnR')

    def _loc_D9EC(): pass

    label('loc_D9EC')

    Jump('loc_DA83')

    def _loc_D9F5(): pass

    label('loc_D9F5')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_DA40',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_DA83')

    def _loc_DA40(): pass

    label('loc_DA40')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DA83',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_DA83(): pass

    label('loc_DA83')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x003D offset: 0xDAA4
@scena.Code('AniSquat')
def AniSquat():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_DB02',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_DBEB')

    def _loc_DB02(): pass

    label('loc_DB02')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_DB8D',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DBEB')

    def _loc_DB8D(): pass

    label('loc_DB8D')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_DBEB(): pass

    label('loc_DBEB')

    Return()

# id: 0x003E offset: 0xDBEC
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003F offset: 0xDC28
@scena.Code('AniLand')
def AniLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_DC81',
    )

    Sleep(500)

    Jump('loc_DC8D')

    def _loc_DC81(): pass

    label('loc_DC81')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_DC8D(): pass

    label('loc_DC8D')

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x0040 offset: 0xDCC4
@scena.Code('AniIdle')
def AniIdle():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetEndhookFunction('DefaultFace', 0x000B)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DD59',
    )

    OP_3B(0x32, ParamInt(0x075A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_DDAE')

    def _loc_DD59(): pass

    label('loc_DD59')

    OP_3B(0x32, ParamInt(0x075B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_DDAE(): pass

    label('loc_DDAE')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '00001#276w0[autoE0]', '0[autoM0]', '#0e0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0041 offset: 0xDE4C
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk105_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk001b.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_DEE7',
    )

    LoadEffect(0xFFFE, 0x25, 'battle/atk105_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk105_a1.eff', 0x00000000)

    def _loc_DEE7(): pass

    label('loc_DEE7')

    Return()

# id: 0x0042 offset: 0xDEE8
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x0043 offset: 0xDF10
@scena.Code('AniFieldAttack')
def AniFieldAttack():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(333)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x070D), ParamInt(0x070E), ParamInt(0x070F), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(66)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    CameraCmd(0x0A, 0.0, 0.05, 0.05, 0, 350, 0, 0, 0, 0x00)
    Sleep(666)

    OP_AD(0x01, 0x01)
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0044 offset: 0xE104
@scena.Code('AniAssaultAttack')
def AniAssaultAttack():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('AniAssaultAttackEnd', 0x000B)
    Call(ScriptId.Current, 'SpringOff')
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 16.6667, 17.3333, -1.0, 0x00, 0x00)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(0x0014))
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    Sleep(166)

    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU466')
    AttachEquip(0xFFFE, 'C_EQU466', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0710), ParamInt(0x0711), ParamInt(0), ParamInt(0))
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 17.3333, 18.9333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0xFF, 0.6, 0.6, 0.1)
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    Sleep(233)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    Sleep(200)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    Sleep(200)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    Sleep(200)

    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(400)

    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(500)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x0045 offset: 0xE790
@scena.Code('AniAssaultAttackEnd')
def AniAssaultAttackEnd():
    Call(ScriptId.Current, 'BtlDefaultFace')
    ReleaseAsset('C_EQU466')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0046 offset: 0xE8C0
@scena.Code('AniFieldAttackEnd')
def AniFieldAttackEnd():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(633)

    Call(ScriptId.Current, 'EraseEquipL')
    Call(ScriptId.Current, 'EraseEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0047 offset: 0xE9FC
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0048 offset: 0xEA30
@scena.Code('AniFieldAttackEndShort')
def AniFieldAttackEndShort():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(533)

    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0049 offset: 0xEB38
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x004A offset: 0xEB3C
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x004B offset: 0xEB40
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004C offset: 0xEB78
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0xEBB8
@scena.Code('AniHorseRun')
def AniHorseRun():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0xEBF8
@scena.Code('AniHorseDash')
def AniHorseDash():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0xEC38
@scena.Code('AniHorseStop')
def AniHorseStop():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xEC78
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0051 offset: 0xECD4
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0052 offset: 0xED30
@scena.Code('AniHorseRearStart')
def AniHorseRearStart():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_EE42',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5C(0xFFFE, 0x00, 'up_point')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, 8.0, 9.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, 8.0, -6.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_EE42(): pass

    label('loc_EE42')

    OP_80(0.0)
    OP_04(0x0B, 'AniHorseRearWait')

    Return()

# id: 0x0053 offset: 0xEE60
@scena.Code('AniHorseRearEnd')
def AniHorseRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x0054 offset: 0xEEA4
@scena.Code('AniHorseRearWait')
def AniHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0xEEDC
@scena.Code('AniHorseRearWalk')
def AniHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0xEF18
@scena.Code('AniHorseRearRun')
def AniHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0057 offset: 0xEF54
@scena.Code('AniHorseRearStop')
def AniHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0058 offset: 0xEFB8
@scena.Code('AniHorseRearTurnRight')
def AniHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0059 offset: 0xF020
@scena.Code('AniHorseRearTurnLeft')
def AniHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x005A offset: 0xF088
@scena.Code('AniHorseRearDash')
def AniHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005B offset: 0xF0C4
@scena.Code('AniBikeWait')
def AniBikeWait():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F11F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_F11F(): pass

    label('loc_F11F')

    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005C offset: 0xF164
@scena.Code('AniBikeWaitLeft')
def AniBikeWaitLeft():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0xF1BC
@scena.Code('AniBikeRun')
def AniBikeRun():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005E offset: 0xF210
@scena.Code('AniBikeTilt')
def AniBikeTilt():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0xF264
@scena.Code('AniBikeTiltR')
def AniBikeTiltR():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0xF2B8
@scena.Code('AniBikeTiltL')
def AniBikeTiltL():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0061 offset: 0xF30C
@scena.Code('AniBikeBack')
def AniBikeBack():
    Call(ScriptId.Current, 'SpringOff')

    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_START', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0062 offset: 0xF39C
@scena.Code('AniBikeHandleWait')
def AniBikeHandleWait():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_HANDLE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0063 offset: 0xF3F8
@scena.Code('AniBikeHandle')
def AniBikeHandle():
    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_HANDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0064 offset: 0xF450
@scena.Code('AniBikeRearWait')
def AniBikeRearWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0065 offset: 0xF49C
@scena.Code('AniBikeRearRun')
def AniBikeRearRun():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0066 offset: 0xF4E8
@scena.Code('AniBikeRearTilt')
def AniBikeRearTilt():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0067 offset: 0xF534
@scena.Code('AniBikeRearBack')
def AniBikeRearBack():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_BACK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0068 offset: 0xF580
@scena.Code('AniBikeRearHandleWait')
def AniBikeRearHandleWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_HANDLE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0069 offset: 0xF5D4
@scena.Code('AniBikeRearTiltL')
def AniBikeRearTiltL():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006A offset: 0xF624
@scena.Code('AniBikeRearTiltR')
def AniBikeRearTiltR():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006B offset: 0xF674
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006C offset: 0xF6B0
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006D offset: 0xF6EC
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x006E offset: 0xF718
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_F734',
    )

    Return()

    def _loc_F734(): pass

    label('loc_F734')

    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x006F offset: 0xF744
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_F76C',
    )

    Return()

    def _loc_F76C(): pass

    label('loc_F76C')

    Call(ScriptId.Current, 'PlayFakeEffect')
    Call(ScriptId.BtlCom, 'AniBtlInit')

    Return()

# id: 0x0070 offset: 0xF798
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0071 offset: 0xF7B0
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_F7D1',
    )

    Return()

    def _loc_F7D1(): pass

    label('loc_F7D1')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F847',
    )

    OP_3B(0x32, ParamInt(0x0731), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FA1B')

    def _loc_F847(): pass

    label('loc_F847')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_F8DB',
    )

    OP_3B(0x32, ParamInt(0x0730), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FA1B')

    def _loc_F8DB(): pass

    label('loc_F8DB')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F951',
    )

    OP_3B(0x32, ParamInt(0x0733), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FA1B')

    def _loc_F951(): pass

    label('loc_F951')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F9C6',
    )

    OP_3B(0x32, ParamInt(0x072E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FA1B')

    def _loc_F9C6(): pass

    label('loc_F9C6')

    OP_3B(0x32, ParamInt(0x072F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_FA1B(): pass

    label('loc_FA1B')

    Return()

# id: 0x0072 offset: 0xFA1C
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_FA59',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x070B), ParamInt(0x070C), ParamInt(0), ParamInt(0))

    Jump('loc_FA79')

    def _loc_FA59(): pass

    label('loc_FA59')

    OP_3B(0x3A, 0xFFFE, ParamInt(1800), ParamInt(0x0709), ParamInt(0x070A), ParamInt(0))

    def _loc_FA79(): pass

    label('loc_FA79')

    Return()

# id: 0x0073 offset: 0xFA7C
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_FAB9',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x070B), ParamInt(0x070C), ParamInt(0), ParamInt(0))

    Jump('loc_FAD9')

    def _loc_FAB9(): pass

    label('loc_FAB9')

    OP_3B(0x3A, 0xFFFE, ParamInt(1800), ParamInt(0x0709), ParamInt(0x070A), ParamInt(0))

    def _loc_FAD9(): pass

    label('loc_FAD9')

    Return()

# id: 0x0074 offset: 0xFADC
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x0732), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0075 offset: 0xFB34
@scena.Code('AniBtlWait')
def AniBtlWait():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_FB69',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_FB69(): pass

    label('loc_FB69')

    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseAsset('C_EQU466')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0076 offset: 0xFD40
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x0077 offset: 0xFD7C
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FDC8',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FE0B')

    def _loc_FDC8(): pass

    label('loc_FDC8')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FE0B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FE0B(): pass

    label('loc_FE0B')

    Return()

# id: 0x0078 offset: 0xFE0C
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x072A))

    Return()

# id: 0x0079 offset: 0xFE28
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x0729))

    Return()

# id: 0x007A offset: 0xFE44
@scena.Code('AniBtlStepInKisinPt')
def AniBtlStepInKisinPt():
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x072A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007B offset: 0xFEC8
@scena.Code('AniBtlStepOutKisinPt')
def AniBtlStepOutKisinPt():
    OP_3B(0x32, ParamInt(0x0729), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007C offset: 0xFF20
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 1.0, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 15)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10021',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_10001',
    )

    Jump('loc_10021')

    def _loc_10001(): pass

    label('loc_10001')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x070D), ParamInt(0x070E), ParamInt(0x070F), ParamInt(0))

    def _loc_10021(): pass

    label('loc_10021')

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(-0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    CameraCmd(0x0A, 0.0, 0.15, 0.15, 0, 350, 0, 0, 0, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_10120',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.3)

    def _loc_10120(): pass

    label('loc_10120')

    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(200)

    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x007D offset: 0x10200
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_10229',
    )

    Jump('loc_1027E')

    def _loc_10229(): pass

    label('loc_10229')

    OP_3B(0x32, ParamInt(0x0726), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1027E(): pass

    label('loc_1027E')

    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x007E offset: 0x10294
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleCmd(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_102F5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1031E')

    def _loc_102F5(): pass

    label('loc_102F5')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1031E(): pass

    label('loc_1031E')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x007F offset: 0x1032C
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_10355',
    )

    Jump('loc_10375')

    def _loc_10355(): pass

    label('loc_10355')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x0722), ParamInt(0x0723), ParamInt(0x0724), ParamInt(0))

    def _loc_10375(): pass

    label('loc_10375')

    Return()

# id: 0x0080 offset: 0x10378
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_103DA',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1043E')

    def _loc_103DA(): pass

    label('loc_103DA')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1043E(): pass

    label('loc_1043E')

    Return()

# id: 0x0081 offset: 0x10440
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0082 offset: 0x1047C
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')

    Return()

# id: 0x0083 offset: 0x10494
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '01', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1056F',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_1051A',
    )

    Jump('loc_1056F')

    def _loc_1051A(): pass

    label('loc_1051A')

    OP_3B(0x32, ParamInt(0x0725), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1056F(): pass

    label('loc_1056F')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0084 offset: 0x105A4
@scena.Code('AniBtlAria')
def AniBtlAria():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_105F7',
    )

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0), ParamInt(0), ParamFloat(-1), ParamFloat(0))

    Jump('loc_10621')

    def _loc_105F7(): pass

    label('loc_105F7')

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x071E), ParamInt(0x071F), ParamFloat(1), ParamFloat(0))

    def _loc_10621(): pass

    label('loc_10621')

    Return()

# id: 0x0085 offset: 0x10624
@scena.Code('AniBtlArts')
def AniBtlArts():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_10678',
    )

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0), ParamInt(0), ParamStr('NODE_R_HAND'))

    Jump('loc_106A3')

    def _loc_10678(): pass

    label('loc_10678')

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0x0720), ParamInt(0x0721), ParamStr('NODE_R_HAND'))

    def _loc_106A3(): pass

    label('loc_106A3')

    Return()

# id: 0x0086 offset: 0x106A4
@scena.Code('AniBtlItem')
def AniBtlItem():
    BattleTargetsIterReset(0xFF, 0xFFFE)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(266)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0720), ParamInt(0x0721), ParamInt(0), ParamInt(0))
    Sleep(466)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(600)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x0087 offset: 0x10898
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x072B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0088 offset: 0x108F0
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x072C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0089 offset: 0x10948
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x072D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x008A offset: 0x109A0
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0739), ParamInt(0x073A), ParamInt(0), ParamInt(0))

    Return()

# id: 0x008B offset: 0x109C4
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlTensionMax')

    Return()

# id: 0x008C offset: 0x109E0
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B5F',
    )

    OP_3B(0x32, ParamInt(0x0749), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10CCB')

    def _loc_10B5F(): pass

    label('loc_10B5F')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10BD6',
    )

    OP_3B(0x32, ParamInt(0x074A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10CCB')

    def _loc_10BD6(): pass

    label('loc_10BD6')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10C4D',
    )

    OP_3B(0x32, ParamInt(0x074A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10CCB')

    def _loc_10C4D(): pass

    label('loc_10C4D')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_10C76',
    )

    Jump('loc_10CCB')

    def _loc_10C76(): pass

    label('loc_10C76')

    OP_3B(0x32, ParamInt(0x073B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10CCB(): pass

    label('loc_10CCB')

    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(-0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(200)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10EA4',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_1103C')

    def _loc_10EA4(): pass

    label('loc_10EA4')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10FA6',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    Jump('loc_1103C')

    def _loc_10FA6(): pass

    label('loc_10FA6')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_1103C(): pass

    label('loc_1103C')

    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(1000)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)

    BattleCmd(0x3F, 0xFFFE)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_11144',
    )

    EffectCmd(0x12, 0xFFFE, 0x03FA)

    def _loc_11144(): pass

    label('loc_11144')

    EffectCmd(0x12, 0xFFFE, 0x0038)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x008D offset: 0x1116C
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008E offset: 0x111B0
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008F offset: 0x111D8
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0xFF, 0xFFFE)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    Call(ScriptId.BtlCom, 'AniBtlBurstWait')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -3.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.35), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_11462',
    )

    Jump('loc_11482')

    def _loc_11462(): pass

    label('loc_11462')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x079E), ParamInt(0x079F), ParamInt(0x07A0), ParamInt(0))

    def _loc_11482(): pass

    label('loc_11482')

    Sleep(150)

    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0090 offset: 0x115A0
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0091 offset: 0x115B8
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0092 offset: 0x115D0
@scena.Code('AniBtlLinkCounter')
def AniBtlLinkCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0093 offset: 0x115E8
@scena.Code('AniBtlLinkRageCounter')
def AniBtlLinkRageCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0094 offset: 0x11600
@scena.Code('AniBtlLinkLivelyYell')
def AniBtlLinkLivelyYell():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x074B), ParamStr('NODE_R_HAND'))

    Return()

# id: 0x0095 offset: 0x1162C
@scena.Code('AniBtlLinkLivelyYell2')
def AniBtlLinkLivelyYell2():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x074B), ParamStr('NODE_R_HAND'))

    Return()

# id: 0x0096 offset: 0x11658
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x0097 offset: 0x11678
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x0098 offset: 0x11694
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    BattleTurnChrDirection(0xFFFE, 0xFFFE, -20.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '3#46w2[autoE2]', '0[autoM6]', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0099 offset: 0x1171C
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_1178D',
    )

    OP_3B(0x32, ParamInt(0x071D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_117E2')

    def _loc_1178D(): pass

    label('loc_1178D')

    OP_3B(0x32, ParamInt(0x071C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_117E2(): pass

    label('loc_117E2')

    Return()

# id: 0x009A offset: 0x117E4
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009B offset: 0x11850
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x009C offset: 0x11868
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x009D offset: 0x1188C
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x009E offset: 0x11890
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x009F offset: 0x118B0
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x0720), ParamInt(0x0721))

    Return()

# id: 0x00A0 offset: 0x118DC
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x00A1 offset: 0x11900
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x00A2 offset: 0x11920
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x00A3 offset: 0x11940
@scena.Code('AniBtlKisinItemPa')
def AniBtlKisinItemPa():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0720), ParamInt(0x0721), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00A4 offset: 0x119A4
@scena.Code('AniBtlKisinChargePa')
def AniBtlKisinChargePa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00A5 offset: 0x119E8
@scena.Code('AniBtlKisinSinkiPa')
def AniBtlKisinSinkiPa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00A6 offset: 0x11A2C
@scena.Code('AniBtlKisinPartnerArts')
def AniBtlKisinPartnerArts():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0720), ParamInt(0x0721), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00A7 offset: 0x11A90
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A8 offset: 0x11ACC
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A9 offset: 0x11B30
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x00AA offset: 0x11B6C
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AB offset: 0x11BA4
@scena.Code('VoiceWin_select')
def VoiceWin_select():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x01,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 3, 0x42B)),
            Expr.Return,
        ),
        'loc_11BE3',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11C1D')

    def _loc_11BE3(): pass

    label('loc_11BE3')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11C10',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11C1D')

    def _loc_11C10(): pass

    label('loc_11C10')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11C1D(): pass

    label('loc_11C1D')

    Return()

# id: 0x00AC offset: 0x11C20
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11C90',
    )

    OP_3B(0x32, ParamInt(0x0736), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11D55')

    def _loc_11C90(): pass

    label('loc_11C90')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D00',
    )

    OP_3B(0x32, ParamInt(0x0734), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11D55')

    def _loc_11D00(): pass

    label('loc_11D00')

    OP_3B(0x32, ParamInt(0x0735), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11D55(): pass

    label('loc_11D55')

    Return()

# id: 0x00AD offset: 0x11D58
@scena.Code('AniBtlWin')
def AniBtlWin():
    Call(ScriptId.Current, 'SpringOff')
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_0', ScriptId.Current)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11DC0',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '', '#b', '0')

    Jump('loc_11DE2')

    def _loc_11DC0(): pass

    label('loc_11DC0')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '2[autoM2]', '', '#b', '0')

    def _loc_11DE2(): pass

    label('loc_11DE2')

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EBC',
    )

    SetChrFace(0x03, PseudoChrId.Self, '3#156w2[autoE2]', '2[autoM2]', '001112234455667', '#b', '0')

    Jump('loc_11EF3')

    def _loc_11EBC(): pass

    label('loc_11EBC')

    SetChrFace(0x03, PseudoChrId.Self, 'E#156w4[autoE4]', '0[autoM0]', '001112234455667', '#b', '0')

    def _loc_11EF3(): pass

    label('loc_11EF3')

    Call(ScriptId.Current, 'VoiceWin_play')
    Sleep(1400)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11FD5',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '7', '#b', '0')

    Jump('loc_11FF8')

    def _loc_11FD5(): pass

    label('loc_11FD5')

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '0[autoM0]', '7', '#b', '0')

    def _loc_11FF8(): pass

    label('loc_11FF8')

    Sleep(600)

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1207B',
    )

    Jump('loc_1207B')

    def _loc_1207B(): pass

    label('loc_1207B')

    CreateThread(PseudoChrId.Self, 0x02, 'BtlWinKea', ScriptId.BtlWin)
    Sleep(1000)

    Return()

# id: 0x00AE offset: 0x12098
@scena.Code('_Lambda_0')
def _Lambda_0():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.05, 1.02, 0.22, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -10.17, 129.59, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.31, 0)
    CameraCmd(0x0B, 0x03, 25.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.14, 1.28, 0.22, 2067)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.14, 11.08, 0.0, 2067, 0x01)
    CameraSetDistance(0x03, 1.88, 2067)
    BattleCmd(0x4B, 0x0813, 0x03)
    Sleep(2066)

    BattleCmd(0x4B, 0x01B1, 0x02)
    Sleep(433)

    Return()

# id: 0x00AF offset: 0x1214C
@scena.Code('AniBtlWinKeirei')
def AniBtlWinKeirei():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KEIREI', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KEIREIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B0 offset: 0x121C0
@scena.Code('AniBtlWinHitouchR')
def AniBtlWinHitouchR():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCH_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00B1 offset: 0x12220
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '5', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'E#156w4[autoE4]', '0[autoM0]', '001112234455667', '#b', '0')
    Sleep(1400)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '0[autoM0]', '7', '#b', '0')
    Sleep(600)

    Return()

# id: 0x00B2 offset: 0x12358
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '11111111114', '0[autoM0]', '7', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1400)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x32, ParamInt(0x0737), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x00B3 offset: 0x124B4
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00B4 offset: 0x124F4
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvYasume', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEvYasume')
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x00B5 offset: 0x12578
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x00B6 offset: 0x12584
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '222333333334', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(600)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '4', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x00B7 offset: 0x126AC
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00B8 offset: 0x126D0
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1273D',
    )

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12792')

    def _loc_1273D(): pass

    label('loc_1273D')

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12792(): pass

    label('loc_12792')

    Return()

# id: 0x00B9 offset: 0x12794
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtLevelUp_Call', ScriptId.Current)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.12, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x11, 0x03, 2.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_128DE',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '5', '5', '', '#b', '0')

    Jump('loc_12952')

    def _loc_128DE(): pass

    label('loc_128DE')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4', '', '#b', '0')

    def _loc_12952(): pass

    label('loc_12952')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1#36w4#106w5', '0[autoM0]', '0[autoB0]', '#b', '0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129CC',
    )

    Sleep(200)

    Jump('loc_129DA')

    def _loc_129CC(): pass

    label('loc_129CC')

    Sleep(100)

    Sleep(100)

    def _loc_129DA(): pass

    label('loc_129DA')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '4[autoM4]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x00BA offset: 0x12A40
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr105_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr105_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr105_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr105_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr105_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr105_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr105_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/cr105_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/cr105_00_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr105_00_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr105_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr105_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr105_00_12.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetChrFace(0x03, PseudoChrId.Self, '3[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU406')
    AttachEquip(0xFFFE, 'C_EQU406', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 0x00000002)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    DeatchEquip(0x0B87, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0x0B87, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0x0B87, 'C_EQU406', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x0B87, '', 'R_hand_point', 0x01)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_1', ScriptId.Current)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_12EFB',
    )

    Jump('loc_12F50')

    def _loc_12EFB(): pass

    label('loc_12EFB')

    OP_3B(0x32, ParamInt(0x0712), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12F50(): pass

    label('loc_12F50')

    BattleCmd(0x4B, 0x0064, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(0x0064))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '33332[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2#36w12[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(333)

    BattleSetChrPosAsync(0x0B86, 0xFFFB, 0.0, 0.0, 6.0, float('nan'), 0x02, 0x00)
    BattleSetChrPosAsync(0x0B87, 0xFFFB, 0.0, 0.0, 7.0, float('nan'), 0x02, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00020003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'attack', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.5, 0.5, 0.2)
    Sleep(666)

    BattleTurnChrDirection(0x0B87, 0xFFF5, 0.0, -1.0)
    TerminateThread(PseudoChrId.Self, 0x02)
    StopEffect(0xFFFE, 0x03, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    StopEffect(0xFFFE, 0x03, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    OP_4E(0.8, 0.0, 0x03, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 4.35, 0.0, 0)
    CameraRotateByTarget(0xFFFB, '', 0x03, -15.0, -40.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.25, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 3.35, 0.0, 3000)
    CameraRotateByTarget(0xFFFB, '', 0x03, -15.0, -20.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x03, 12.25, 1000)
    BattleCmd(0x4B, 0x03E8, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B87, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_133B5(): pass

    label('loc_133B5')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_13909',
    )

    Sleep(66)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0xA),
            (Expr.PushLong, 0x5DC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13466',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0xA),
            (Expr.PushLong, 0x8FC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13466',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0xA),
            (Expr.PushLong, 0xBB8),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13466',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0xA),
            (Expr.PushLong, 0xFA0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13466',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13466(): pass

    label('loc_13466')

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x384),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_134EA',
    )

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x5DC),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_134EA',
    )

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x7D0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_134EA',
    )

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x9C4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_134EA',
    )

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_134EA(): pass

    label('loc_134EA')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13555',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_13555(): pass

    label('loc_13555')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_135C0',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_135C0(): pass

    label('loc_135C0')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x2),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1362B',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_1362B(): pass

    label('loc_1362B')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13696',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_13696(): pass

    label('loc_13696')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13701',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_13701(): pass

    label('loc_13701')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1376C',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_1376C(): pass

    label('loc_1376C')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_137D7',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_137D7(): pass

    label('loc_137D7')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            (Expr.PushReg, 0xB),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13842',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_13842(): pass

    label('loc_13842')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_138A4',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_138EB')

    def _loc_138A4(): pass

    label('loc_138A4')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Target, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_138EB(): pass

    label('loc_138EB')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_133B5')

    def _loc_13909(): pass

    label('loc_13909')

    Sleep(433)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_3B(0xFF, 1.0, 1.0, 0.2)
    Sleep(333)

    OP_3B(0xFF, 0.1, 0.1, 5.0)
    Sleep(233)

    TerminateThread(PseudoChrId.Self, 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0x0B87, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0x0B87, '', 0x03, 0.0, 175.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x48, 0x0B86, 0x0001)
    BattleCmd(0x46, 2.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(2000)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    CameraCmd(0x0A, 0.1, 0.05, 0.0, 100, 100, 100, 0, 0, 0x00)
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    ReleaseAsset('C_EQU466')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleDeleteTempChar(0xFFFF)
    BattleCmd(0x47)
    BattleDeleteChrDummy()
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00BB offset: 0x13DAC
@scena.Code('_Lambda_1')
def _Lambda_1():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.78, -0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.48, 9.75, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.19, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 0.76, -0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.69, 134.93, -0.0, 2000, 0x01)
    CameraSetDistance(0x03, 1.72, 2000)
    BattleCmd(0x4B, 0x07D0, 0x03)
    Sleep(2000)

    Return()

# id: 0x00BC offset: 0x13E50
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr105_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr105_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr105_01_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr105_01_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/ryu3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/gra00.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr105_01_4.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU466')
    AttachEquip(0xFFFE, 'C_EQU466', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCreateChrDummy(0xFFFE, 0x00000003)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    DeatchEquip(0x0B87, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0x0B87, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0x0B87, 'C_EQU466', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x0B87, '', 'R_hand_point', 0x01)
    BattleSetChrPos(0x0B88, 0xFFFB, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(0x006E))
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_2', ScriptId.Current)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_14270',
    )

    Jump('loc_142C5')

    def _loc_14270(): pass

    label('loc_14270')

    OP_3B(0x32, ParamInt(0x0713), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_142C5(): pass

    label('loc_142C5')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.048), ParamFloat(0.1), ParamFloat(0.06), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.048), ParamFloat(0.1), ParamFloat(0.06), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.048), ParamFloat(0.1), ParamFloat(-0.045), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.048), ParamFloat(0.1), ParamFloat(-0.045), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '3#36w2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(333)

    BattleSetChrPosAsync(0x0B86, 0xFFFB, 0.0, 0.0, 8.0, float('nan'), 0x02, 0x00)
    BattleSetChrPosAsync(0x0B87, 0xFFFB, 0.0, 0.0, 8.0, float('nan'), 0x02, 0x00)
    BattleSetChrPosAsync(0x0B88, 0xFFFB, 0.0, 0.0, 5.0, float('nan'), 0x02, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '66226662[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_14618',
    )

    Jump('loc_1466D')

    def _loc_14618(): pass

    label('loc_14618')

    OP_3B(0x32, ParamInt(0x0714), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1466D(): pass

    label('loc_1466D')

    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.6, 0.6, 0.1)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    Sleep(266)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)
    Sleep(266)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x05)
    Sleep(266)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x06)
    Sleep(266)

    OP_3B(0xFF, 0.6, 0.6, 0.1)
    OP_3B(0xFF, 0.1, 0.1, 6.0)
    BattleTurnChrDirection(0x0B87, 0xFFF5, 0.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    TerminateThread(PseudoChrId.Self, 0x02)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, -5.0, 120.0, 0.0, 0, 0x01)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0x0B86, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B87, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
    Sleep(1166)

    TerminateThread(PseudoChrId.Self, 0x02)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 3.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 160.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.25, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraCmd(0x07, 0x00BF)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    BattleCmd(0x47)
    BattleCmd(0x48, 0x0B88, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x03, 3.0, 3000)
    BattleCmd(0x4B, 0x0000, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00020003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_5E(0x00, 0x0002, 0.15, 300, 300, 600, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    OP_3B(0xFF, 1.0, 1.0, 0.3)
    CameraCmd(0x0A, 0.1, 0.05, 0.0, 0, 200, 100, 0, 0, 0x00)
    Sleep(300)

    OP_3B(0xFF, 0.1, 0.1, 0.5)
    Sleep(1166)

    OP_43(0x03, 0, 1.0, 0)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    ReleaseAsset('C_EQU466')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU622')
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleDeleteTempChar(0xFFFF)
    BattleDeleteChrDummy()
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00BD offset: 0x14DE4
@scena.Code('_Lambda_2')
def _Lambda_2():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.51, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.41, -28.94, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.01, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.71, 0.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.89, 0.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 1.57, 1000)
    BattleCmd(0x4B, 0x03E8, 0x03)
    Sleep(1000)

    BattleCmd(0x4B, 0x014D, 0x03)
    Sleep(333)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.68, 0.0, 1167)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.84, 0.0, -0.0, 1167, 0x01)
    CameraSetDistance(0x03, 1.8, 1167)
    BattleCmd(0x4B, 0x048F, 0x03)
    Sleep(1166)

    Return()

# id: 0x00BE offset: 0x14EE8
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr105_02_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr105_02_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr105_02_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr105_02_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr105_02_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr105_02_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/craftworld_0.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 0x00000001)
    ChrSetPhysicsFlags(0x0B86, 0x00000220)
    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    OP_4E(1.2, 0.0, 0x03, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_15110',
    )

    Jump('loc_15165')

    def _loc_15110(): pass

    label('loc_15110')

    OP_3B(0x32, ParamInt(0x0715), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_15165(): pass

    label('loc_15165')

    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(0x0078))
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_3', ScriptId.Current)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '23#76w2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(1200)

    OP_5E(0x00, 0x0002, 0.3, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.3, 0.3, 0.2)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    ReleaseEffect(0xFFFE, 0x30)
    ChrSetPhysicsFlags(0xFFF8, 0x00000040)
    ChrSetPhysicsFlags(0xFFF8, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleTargetsIterReset(0xFF, 0xFFFE)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000200)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000200)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSaveChrPosition(0xFFF9, 0x00000000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_15358(): pass

    label('loc_15358')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_153BE',
    )

    BattleSaveChrPosition(0xFFFB, 0x00000000)
    BattleSaveChrPosition(0xFFFB, 0x00000001)
    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153A8',
    )

    BattleTargetsIterNext(0xFFFE)

    def _loc_153A8(): pass

    label('loc_153A8')

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_15358')

    def _loc_153BE(): pass

    label('loc_153BE')

    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -45.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, -45.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    Call(ScriptId.BtlCom, 'CRAFT_SPACE_BEGIN')
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFF3, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    EffectSetRGBA(0xFFFE, 0x02, 0.5, 0.7, 0.5, 0.5, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.5, 0.7, 0.5, 0.5, 0, 0x03)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0x0B86, '', 3.0, 0.95, 0.54, 0)
    CameraRotateByTarget(0x0B86, '', 0x03, 1.54, 165.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 0.55, 0)
    CameraCmd(0x0B, 0x03, 35.0, 0x0000)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_4', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_5E(0x00, 0x0002, 0.3, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleSetChrPosAsync(0xFFFE, 0xFFFB, 0.0, 0.0, -25.0, 3.5, 0x00, 0x00)
    BattleSetChrPosAsync(0x0B86, 0xFFFB, 0.0, 0.0, -20.0, 1.5, 0x00, 0x00)
    BattleCmd(0x3F, 0xFFFE)
    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_5E(0x01, 0x0000)
    TerminateThread(PseudoChrId.Self, 0x02)
    CameraCmd(0x00)
    OP_4A(0x01, 0.0, 0.0, 0.0, 0.0, 200, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.03, 1.08, -1.71, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.58, 90.0, -0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.23, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '667', '0[autoM0]', '0[autoB0]', '#b', '0')
    BattleSetChrPos(0xFFFE, 0xFFF5, 0.0, 0.0, -5.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    Sleep(166)

    OP_3B(0xFF, 0.3, 0.3, 0.5)
    BattleSetChrPos(0xFFFE, 0xFFF5, 0.0, 0.0, 0.0, 0.9, 0x00, 0x01)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    TerminateThread(PseudoChrId.Self, 0x02)
    ReleaseEffect(0xFFFE, 0x31)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_157CF',
    )

    Jump('loc_15824')

    def _loc_157CF(): pass

    label('loc_157CF')

    OP_3B(0x32, ParamInt(0x0716), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_15824(): pass

    label('loc_15824')

    BattleCmd(0x47)
    CameraCmd(0x00)

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x23),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_5', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '776#66w2#46w6[autoE6]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(133)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(166)

    OP_3B(0xFF, 0.3, 0.3, 10.5)
    Sleep(500)

    OP_4E(1.1, 0.0, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(1500)

    OP_4E(1.1, 0.0, 0x03, 0x00)
    OP_43(0x03, 6, 1.0, 0)
    ReleaseEffect(0xFFFE, 0x34)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_6', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(100)

    OP_43(0x67, 1, 1.0, 0)
    Sleep(1333)

    TerminateThread(PseudoChrId.Self, 0x02)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    Sleep(666)

    OP_4E(0.3, 5.0, 0x03, 0x00)
    OP_43(0x03, 900, 1.0, 0)
    Sleep(500)

    TerminateThread(PseudoChrId.Self, 0x02)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x35)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_15BE0(): pass

    label('loc_15BE0')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_15C56',
    )

    BattleSetChrPos(0xFFFB, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFE9, 0.0, -1.0)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000020)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15C40',
    )

    BattleTargetsIterNext(0xFFFE)

    def _loc_15C40(): pass

    label('loc_15C40')

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_15BE0')

    def _loc_15C56(): pass

    label('loc_15C56')

    Sleep(333)

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleDeleteTempChar(0xFFFF)
    BattleDeleteChrDummy()
    Call(ScriptId.BtlCom, 'CRAFT_SPACE_FINISH')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    OP_43(0x67, 10, 1.0, 0)

    Return()

# id: 0x00BF offset: 0x15CC8
@scena.Code('_Lambda_3')
def _Lambda_3():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.27, -0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.32, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.42, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.68, 0.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x03, 2.43, 2000)
    BattleCmd(0x4B, 0x07D0, 0x03)
    Sleep(1666)

    Return()

# id: 0x00C0 offset: 0x15D6C
@scena.Code('_Lambda_4')
def _Lambda_4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15DD6',
    )

    CameraSetPosByTarget(0x03, 0x0B86, '', 1.5, 0.72, -1.07, 100)
    CameraRotateByTarget(0x0B86, '', 0x03, 1.54, 165.0, -0.0, 300, 0x01)
    CameraSetDistance(0x03, 0.55, 300)
    CameraCmd(0x0B, 0x03, 5.0, 0x012C)
    Sleep(33)

    Jump('_Lambda_4')

    def _loc_15DD6(): pass

    label('loc_15DD6')

    Return()

# id: 0x00C1 offset: 0x15DD8
@scena.Code('_Lambda_5')
def _Lambda_5():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.11, 0.85, 0.15, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -9.42, 20.51, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.23, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.11, 1.13, 0.59, 667)
    CameraRotateByTarget(0xFFFE, '', 0x03, -12.9, -72.33, -0.0, 667, 0x01)
    CameraSetDistance(0x03, 1.52, 667)
    BattleCmd(0x4B, 0x029B, 0x03)
    Sleep(666)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.11, 0.18, 1667)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.68, 173.93, 0.0, 1667, 0x01)
    CameraSetDistance(0x03, 1.7, 1667)
    BattleCmd(0x4B, 0x0683, 0x03)
    Sleep(1666)

    def _loc_15EC8(): pass

    label('loc_15EC8')

    If(
        (
            (Expr.PushReg, 0x8),
            Expr.Return,
        ),
        'loc_15F16',
    )

    BattleTargetsIterReset(0xFF, 0xFFFE)
    Call(ScriptId.Current, 'AniBtlCraft00_Damage')
    Sleep(150)

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_15EC8')

    def _loc_15F16(): pass

    label('loc_15F16')

    Sleep(2000)

    Return()

# id: 0x00C2 offset: 0x15F20
@scena.Code('_Lambda_6')
def _Lambda_6():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.05, 0.93, 0.05, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.11, 83.69, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.49, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.03, 0.94, 0.02, 2267)
    CameraRotateByTarget(0xFFFE, '', 0x03, 23.06, -8.09, 0.0, 2267, 0x01)
    CameraSetDistance(0x03, 9.08, 2267)
    BattleCmd(0x4B, 0x08DB, 0x03)
    Sleep(2266)

    def _loc_15FC2(): pass

    label('loc_15FC2')

    If(
        (
            (Expr.PushReg, 0x8),
            Expr.Return,
        ),
        'loc_16010',
    )

    BattleTargetsIterReset(0xFF, 0xFFFE)
    Call(ScriptId.Current, 'AniBtlCraft00_Damage')
    Sleep(150)

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_15FC2')

    def _loc_16010(): pass

    label('loc_16010')

    Sleep(2266)

    Return()

# id: 0x00C3 offset: 0x16018
@scena.Code('AniBtlCraft00_Damage')
def AniBtlCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_16028(): pass

    label('loc_16028')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_16067',
    )

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_16028')

    def _loc_16067(): pass

    label('loc_16067')

    BattleTargetsIterReset(0x00, 0xFFFE)

    Return()

# id: 0x00C4 offset: 0x16074
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR105_SC1')
    LoadEffect(0xFFFE, 0x30, 'battle/sc105_00_00.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/sc105_00_01.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc105_00_02.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc105_00_03.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc105_00_04.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc105_00_05.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc105_00_06.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc105_00_07.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc105_00_08.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc105_00_09.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc105_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc105_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc105_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc105_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc105_00_14.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_16309',
    )

    LoadEffect(0xFFFE, 0x3F, 'battle/cic105_9.eff', 0x00000000)

    Jump('loc_16312')

    def _loc_16309(): pass

    label('loc_16309')

    BattleCmd(0x52, 0xFFFE, 0x3F)

    def _loc_16312(): pass

    label('loc_16312')

    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    SetChrFace(0x03, PseudoChrId.Self, 'disable', 'disable', 'disable', '#b', '0')
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -50.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_163C8(): pass

    label('loc_163C8')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1640B',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFE, -1.0, 0.5)
    BattleTargetsIterNext(0xFFFE)
    Sleep(1)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_163C8')

    def _loc_1640B(): pass

    label('loc_1640B')

    Call(ScriptId.Current, 'SpringOff')
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHR980', 'chr980')
    ModelCmd(0x35, 0x00, 0x0B68, '', 0xFFFFFFFF, 'I_BIKE_P008', 'I_BIKE_P008_MARK', '')
    PlayChrAnimeClip(0x0B68, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetPhysicsFlags(0x0B68, 0x000002A0)
    BattleSetChrPosAsync(0x0B68, 0xFFFF, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    OP_8A(0x00, 0xFFFE, 0x0B68, '', 'chr_locator', 0x01)
    AnimeClipAddAsset(0x0B68, 'C_CHR980_SC1')
    OP_CE(0x0005, 0xFFFE, 'BTL_S_CRAFT00_01_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0x0B68, 'gamePos0', 0x00)
    OP_CE(0x0004, 0xFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_43(0x64, 1000, 1.0, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_16588',
    )

    Jump('loc_165DD')

    def _loc_16588(): pass

    label('loc_16588')

    OP_3B(0x32, ParamInt(0x0717), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_165DD(): pass

    label('loc_165DD')

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    ChrSetRGBA(PseudoChrId.Self, 0.0, 0.0, 0.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B68, 0.3, 0.3, 0.3, 1.0, 0, 0x03)
    OP_CE(0x0002, 'BTL_S_CRAFT00_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(400))
    WaitAnimeClipFrames(PseudoChrId.Self, 35)
    ChrSetRGBA(0x0B68, 0.4, 0.4, 0.4, 1.0, 300, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0x0B68, 0x00000003, ParamStr('NODE_BIKE_LIGHT00'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B68, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    OP_3B(0xFF, 0.3, 0.3, 0.1)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 70)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B68, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    OP_CE(0x0002, 'BTL_S_CRAFT00_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0x0B68, 0x00000003, ParamStr('NODE_BIKE_LIGHT00'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    Sleep(333)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_16A24',
    )

    Jump('loc_16A79')

    def _loc_16A24(): pass

    label('loc_16A24')

    OP_3B(0x32, ParamInt(0x0718), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16A79(): pass

    label('loc_16A79')

    OP_3B(0xFF, 0.3, 0.3, 0.3)
    CameraCmd(0x0A, 0.0, 0.001, 0.5, 0, 900, 0, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.35, 0, 1400, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(333)

    OP_3B(0xFF, 0.3, 0.3, 0.3)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    ReleaseEffect(0xFFFE, 0x3C)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc105_00_18.eff', 0x00000000)
    OP_CE(0x0002, 'BTL_S_CRAFT00_03_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0xFF, 0.3, 0.3, 0.8)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    CameraCmd(0x0A, 0.01, 0.01, 0.5, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x03, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_04_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0xFF, 0.4, 0.4, 2.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B68, 0x00000003, ParamStr('NODE_ROOT'), ParamFloat(0), ParamFloat(0.991), ParamFloat(-0.973), -0.0, 0.0, 1.608, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    CameraCmd(0x0A, 0.01, 0.01, 0.5, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.55, 0, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(333)

    OP_3B(0xFF, 0.2, 0.2, 2.0)
    CameraCmd(0x0A, 0.01, 0.01, 0.5, 0, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.55, 0, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x04, 0x01)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x0A, 0x01)
    StopEffect(0xFFFE, 0x0F, 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_05_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0D)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0F)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0x0B68, 0x00000003, ParamStr('NODE_BIKE_LIGHT00'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.25), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    CameraCmd(0x0A, 0.02, 0.0, 0.5, 0, 1000, 0, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.55, 0, 1000, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.2, 0.2, 3.0)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x0D, 0x01)
    StopEffect(0xFFFE, 0x0B, 0x01)
    StopEffect(0xFFFE, 0x0F, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_06_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_17283',
    )

    Jump('loc_172D8')

    def _loc_17283(): pass

    label('loc_17283')

    OP_3B(0x32, ParamInt(0x0719), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_172D8(): pass

    label('loc_172D8')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), -0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), -0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-15), 1.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x0B)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x0D)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-15), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0F)
    CameraCmd(0x0A, 0.0, 0.0, 0.01, 0, 900, 0, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.15, 0, 900, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(666)

    CameraCmd(0x0A, 0.02, 0.02, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x06, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    StopEffect(0xFFFE, 0x0B, 0x01)
    StopEffect(0xFFFE, 0x0D, 0x01)
    StopEffect(0xFFFE, 0x0F, 0x01)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(0x0B68, 0x00000040)
    ChrSetPhysicsFlags(0x0B68, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    OP_CE(0x000B, 0x00000000, 0x00)
    CameraCmd(0x00)
    CameraRotateByTarget(0xFFFB, '', 0x03, 33.0, 89.2, 0.0, 0, 0x01)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0xFFF9, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    Sleep(100)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(300)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(300)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(300)

    StopEffect(0xFFFE, 0x07, 0x01)
    TerminateThread(PseudoChrId.Self, 0x02)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_CE(0x0015, 0xFFFE, 0x00000000, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFF, 0.0, 0.0, -20.0, -1.0, 0x00, 0x00)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000000, 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -10.0, 0.0, 0x00, 0x01)
    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    OP_CE(0x0004, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    BattleCmd(0x47)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_07_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_07', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B68, 0x00000003, ParamStr('NODE_ROOT'), ParamFloat(0), ParamFloat(0.991), ParamFloat(-0.973), -0.0, 0.0, 1.608, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0E)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0F)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    OP_3B(0xFF, 0.1, 0.1, 2.0)
    OP_5E(0x00, 0x0000, 0.55, 100, 2000, 100, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(1000)

    OP_3B(0xFF, 0.5, 0.5, 1.0)
    Sleep(333)

    OP_3B(0xFF, 0.3, 0.3, 0.8)
    WaitAnimeClipFrames(PseudoChrId.Self, 50)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    StopEffect(0xFFFE, 0x0E, 0x01)
    StopEffect(0xFFFE, 0x03, 0x01)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    LoadEffect(0xFFFE, 0x31, 'battle/sc105_00_15.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc105_00_16.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc105_00_17.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc105_00_19.eff', 0x00000000)
    Sleep(1800)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_17BB6',
    )

    Jump('loc_17C0B')

    def _loc_17BB6(): pass

    label('loc_17BB6')

    OP_3B(0x32, ParamInt(0x071A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_17C0B(): pass

    label('loc_17C0B')

    Sleep(200)

    StopEffect(0xFFFE, 0x04, 0x01)
    StopEffect(0xFFFE, 0x0A, 0x01)
    StopEffect(0xFFFE, 0x0F, 0x01)
    StopEffect(0xFFFE, 0x05, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    OP_CE(0x0015, 0xFFFE, 0x00000000, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFF, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    OP_CE(0x0004, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_08_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B68, 0x00000003, ParamStr('NODE_ROOT'), ParamFloat(0), ParamFloat(0.991), ParamFloat(-0.973), -0.0, 0.0, 1.608, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    OP_CE(0x0003, 0x00)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x000008FC, 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0xFFFE, 0xFFFF, 0.0, 0.0, 1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    OP_CE(0x0004, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    TerminateThread(PseudoChrId.Self, 0x02)
    OP_CE(0x0002, 'BTL_S_CRAFT00_11_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_11', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_11_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_11', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0x0B68, 0x00000003, ParamStr('NODE_BIKE_TRUNK'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    OP_4E(0.9, 0.0, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0x0B68, 0x00000003, ParamStr('NODE_ROOT'), ParamFloat(0), ParamFloat(0.991), ParamFloat(-0.973), -0.0, 0.0, 1.608, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    OP_3B(0xFF, 0.1, 0.1, 3.0)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 2900, 0x03)
    ChrSetRGBA(0x0B68, 1.0, 1.0, 1.0, 0.0, 2900, 0x03)
    Sleep(333)

    OP_3B(0xFF, 0.2, 0.2, 3.0)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(500)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR105_C70')"),
            Expr.Return,
        ),
        'loc_181D6',
    )

    Jump('loc_1822B')

    def _loc_181D6(): pass

    label('loc_181D6')

    OP_3B(0x32, ParamInt(0x071B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1822B(): pass

    label('loc_1822B')

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    OP_CE(0x0003, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_11a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_11a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B68, 1.25, 0xFFFFFFFF)
    OP_3B(0xFF, 0.3, 0.3, 3.0)
    OP_4E(0.9, 0.0, 0x03, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    StopEffect(0xFFFE, 0x06, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    CameraCmd(0x0A, 0.2, 0.2, 0.2, 2000, 4000, 1000, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.45, 1000, 4000, 1000, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_6C(0x0B68, 1.5, 0xFFFFFFFF)
    OP_4E(0.9, 0.0, 0x03, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    Sleep(333)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage', ScriptId.Current)
    OP_3B(0xFF, 0.4, 0.4, 3.0)
    OP_4E(0.9, 0.0, 0x03, 0x00)
    CameraCmd(0x0A, 0.01, 0.01, 0.2, 0, 2000, 0, 0, 0, 0x00)
    OP_5E(0x00, 0x0000, 0.45, 0, 2000, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_43(0x03, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    OP_04(0x0B, 'AniBtlSCraft00_Finish')

    Return()

# id: 0x00C5 offset: 0x1853C
@scena.Code('AniBtlSCraft00_Finish')
def AniBtlSCraft00_Finish():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    OP_3B(0xFF, 0.0, 0.0, 1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_8A(0x01, 0xFFFE, 0x0B68, '', '')
    BattleDeleteTempChar(0xFFFF)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR105_SC1')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    OP_CE(0x0001, 0x00000000, 0x00)
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00C6 offset: 0x186AC
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    OP_3B(0xFF, 0.6, 0.6, 0.1)

    Return()

# id: 0x00C7 offset: 0x1870C
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C8 offset: 0x1873C
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C9 offset: 0x1876C
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CA offset: 0x1879C
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CB offset: 0x187DC
@scena.Code('AniEvSquat')
def AniEvSquat():
    Call(ScriptId.CurrentCharacter, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1886B',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_18944')

    def _loc_1886B(): pass

    label('loc_1886B')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_188E6',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_18944')

    def _loc_188E6(): pass

    label('loc_188E6')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_18944(): pass

    label('loc_18944')

    Return()

# id: 0x00CC offset: 0x18948
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CD offset: 0x18984
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CE offset: 0x189E0
@scena.Code('AniEvIdle')
def AniEvIdle():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CF offset: 0x18A40
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x18A88
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D1 offset: 0x18ABC
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D2 offset: 0x18B00
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D3 offset: 0x18B34
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(633)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D4 offset: 0x18C1C
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D5 offset: 0x18C88
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D6 offset: 0x18CF4
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D7 offset: 0x18D28
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D8 offset: 0x18D90
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x18DFC
@scena.Code('AniEvDead')
def AniEvDead():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DA offset: 0x18E64
@scena.Code('AniEvDead1')
def AniEvDead1():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DB offset: 0x18E9C
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DC offset: 0x18F04
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DD offset: 0x18F70
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x18FA4
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x19014
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E0 offset: 0x1907C
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E1 offset: 0x190E0
@scena.Code('AniEvHorseWait')
def AniEvHorseWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E2 offset: 0x19114
@scena.Code('AniEvHorseWalk')
def AniEvHorseWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E3 offset: 0x1914C
@scena.Code('AniEvHorseRun')
def AniEvHorseRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E4 offset: 0x19184
@scena.Code('AniEvHorseStop')
def AniEvHorseStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E5 offset: 0x191E0
@scena.Code('AniEvHorseTurnRight')
def AniEvHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E6 offset: 0x1923C
@scena.Code('AniEvHorseTurnLeft')
def AniEvHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E7 offset: 0x19298
@scena.Code('AniEvHorseDash')
def AniEvHorseDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x192D0
@scena.Code('AniEvHorseRearWait')
def AniEvHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E9 offset: 0x19308
@scena.Code('AniEvHorseRearWalk')
def AniEvHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EA offset: 0x19344
@scena.Code('AniEvHorseRearRun')
def AniEvHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EB offset: 0x19380
@scena.Code('AniEvHorseRearStop')
def AniEvHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EC offset: 0x193E4
@scena.Code('AniEvHorseRearTurnRight')
def AniEvHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00ED offset: 0x1944C
@scena.Code('AniEvHorseRearTurnLeft')
def AniEvHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EE offset: 0x194B4
@scena.Code('AniEvHorseRearDash')
def AniEvHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x194F0
@scena.Code('AniEvCraft00_01')
def AniEvCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x19564
@scena.Code('AniEvCraft01_01')
def AniEvCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x195D8
@scena.Code('AniEvCraft01_02')
def AniEvCraft01_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F2 offset: 0x1964C
@scena.Code('AniBikeBackStart')
def AniBikeBackStart():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_START', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x19688
@scena.Code('AniBikeBackEnd')
def AniBikeBackEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x196C4
@scena.Code('AniBikeWaitL')
def AniBikeWaitL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x196FC
@scena.Code('AniEvSCraft00_01')
def AniEvSCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F6 offset: 0x19738
@scena.Code('AniEvSCraft00_02')
def AniEvSCraft00_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F7 offset: 0x19774
@scena.Code('AniEvSCraft00_03')
def AniEvSCraft00_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x197B0
@scena.Code('AniEvSCraft00_04')
def AniEvSCraft00_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F9 offset: 0x197EC
@scena.Code('AniEvSCraft00_05')
def AniEvSCraft00_05():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FA offset: 0x19828
@scena.Code('AniEvSCraft00_06')
def AniEvSCraft00_06():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FB offset: 0x19864
@scena.Code('AniEvSCraft00_07')
def AniEvSCraft00_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FC offset: 0x198A0
@scena.Code('AniEvSCraft00_08')
def AniEvSCraft00_08():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FD offset: 0x198DC
@scena.Code('AniEvSCraft00_11')
def AniEvSCraft00_11():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_11a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FE offset: 0x19954
@scena.Code('AniEvCraft00_02')
def AniEvCraft00_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FF offset: 0x199C8
@scena.Code('AniEvCraft00_03')
def AniEvCraft00_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0100 offset: 0x19A3C
@scena.Code('AniEvCraft01_03')
def AniEvCraft01_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0101 offset: 0x19AB0
@scena.Code('AniEvCraft02_01')
def AniEvCraft02_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0102 offset: 0x19AEC
@scena.Code('AniEvCraft02_03')
def AniEvCraft02_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0103 offset: 0x19B60
@scena.Code('AniEvCraft02_02')
def AniEvCraft02_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_02', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0104 offset: 0x19B9C
@scena.Code('AniEvCraft02_04')
def AniEvCraft02_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0105 offset: 0x19BD8
@scena.Code('AniEvCraft02_05')
def AniEvCraft02_05():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0106 offset: 0x19C14
@scena.Code('AniAttachEQU033')
def AniAttachEQU033():
    LoadAsset('C_EQU033')
    AttachEquip(0xFFFE, 'C_EQU033', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0107 offset: 0x19CAC
@scena.Code('AniDetachEQU033')
def AniDetachEQU033():
    ReleaseAsset('C_EQU033')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0108 offset: 0x19D00
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320_C03')
    AttachEquip(0xFFFE, 'C_EQU320_C03', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0109 offset: 0x19D74
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320_C03')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x010A offset: 0x19DCC
@scena.Code('AniEv91010')
def AniEv91010():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV91010', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV91010a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x010B offset: 0x19E28
@scena.Code('AniEv91015')
def AniEv91015():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV91015', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV91015a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x010C offset: 0x19E84
@scena.Code('AniEv91015b')
def AniEv91015b():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV91015b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV91010a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x010D offset: 0x19EE0
@scena.Code('AniAttachEQU757')
def AniAttachEQU757():
    LoadAsset('C_EQU757')
    AttachEquip(0xFFFE, 'C_EQU757', 'R_hand_point', -0.01, -0.01, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x010E offset: 0x19F78
@scena.Code('AniDetachEQU757')
def AniDetachEQU757():
    ReleaseAsset('C_EQU757')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x010F offset: 0x19FCC
@scena.Code('AniEv_B3_14_00_05')
def AniEv_B3_14_00_05():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0110 offset: 0x1A008
@scena.Code('AniEv_B3_14_00_06')
def AniEv_B3_14_00_06():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0111 offset: 0x1A044
@scena.Code('AniEv_B3_14_00_1_07')
def AniEv_B3_14_00_1_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_07', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0112 offset: 0x1A080
@scena.Code('AniEv_B3_14_00_1_08')
def AniEv_B3_14_00_1_08():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_08', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0113 offset: 0x1A0BC
@scena.Code('AniEv_B3_14_00_1_09')
def AniEv_B3_14_00_1_09():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_09', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0114 offset: 0x1A0F8
@scena.Code('AniEv_B3_14_00_1_11')
def AniEv_B3_14_00_1_11():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0115 offset: 0x1A134
@scena.Code('AniEv_B3_14_00_1_11A')
def AniEv_B3_14_00_1_11A():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_11A', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0116 offset: 0x1A174
@scena.Code('AniEv_B3_14_00_1_11B')
def AniEv_B3_14_00_1_11B():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_11B', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0117 offset: 0x1A1B4
@scena.Code('AniEv_B3_14_00_1_11C')
def AniEv_B3_14_00_1_11C():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_11C', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0118 offset: 0x1A1F4
@scena.Code('AniEv_B3_14_00_1_11D')
def AniEv_B3_14_00_1_11D():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_11D', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0119 offset: 0x1A234
@scena.Code('AniEv_B3_14_00_1_12')
def AniEv_B3_14_00_1_12():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_12', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011A offset: 0x1A270
@scena.Code('AniEv_B3_14_00_1_13')
def AniEv_B3_14_00_1_13():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011B offset: 0x1A2AC
@scena.Code('AniEv_B3_14_00_1_16')
def AniEv_B3_14_00_1_16():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_B3_14_00_1_16', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011C offset: 0x1A2E8
@scena.Code('AniEv_Z1_00_08_08')
def AniEv_Z1_00_08_08():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_08_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011D offset: 0x1A34C
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR105_EV', 'EV35000')
    LoadAsset('C_EQU466')
    LoadEffect(0xFFFE, 0x22, 'battle/atk105_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk001b.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk105_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk105_a1.eff', 0x00000000)

    Return()

# id: 0x011E offset: 0x1A400
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'EV35000')
    ReleaseAsset('C_EQU466')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x011F offset: 0x1A464
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'EraseEquip')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0120 offset: 0x1A4DC
@scena.Code('AniCvIdle')
def AniCvIdle():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetEndhookFunction('DefaultFace', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1A59F',
    )

    OP_3B(0x32, ParamInt(0x075A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1A5F4')

    def _loc_1A59F(): pass

    label('loc_1A59F')

    OP_3B(0x32, ParamInt(0x075B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1A5F4(): pass

    label('loc_1A5F4')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '00001#276w0[autoE0]', '0[autoM0]', '#0e0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0121 offset: 0x1A690
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0122 offset: 0x1A7DC
@scena.Code('AniCvAttack')
def AniCvAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(333)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x070D), ParamInt(0x070E), ParamInt(0x070F), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A90F',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_1A90F(): pass

    label('loc_1A90F')

    Sleep(66)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A97C',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1.3), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_1A97C(): pass

    label('loc_1A97C')

    CameraCmd(0x0A, 0.0, 0.05, 0.05, 0, 350, 0, 0, 0, 0x00)
    Sleep(666)

    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0123 offset: 0x1A9FC
@scena.Code('AniCvAssaultAttack')
def AniCvAssaultAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('AniCvAssaultAttack_endfook', 0x000B)
    Call(ScriptId.Current, 'SpringOff')
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 16.6667, 17.3333, -1.0, 0x00, 0x00)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR105', ScriptId.Sound2, ParamInt(0x0014))
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    Sleep(166)

    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0xFFFE, 'C_EQU466', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0710), ParamInt(0x0711), ParamInt(0), ParamInt(0))
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 17.3333, 18.9333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0xFF, 0.6, 0.6, 0.1)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AD7E',
    )

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)

    def _loc_1AD7E(): pass

    label('loc_1AD7E')

    Sleep(233)

    OP_3B(0xFF, 0.6, 0.6, 0.1)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AE5A',
    )

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)

    def _loc_1AE5A(): pass

    label('loc_1AE5A')

    Sleep(200)

    OP_3B(0xFF, 0.6, 0.6, 0.1)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AF36',
    )

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(-0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)

    def _loc_1AF36(): pass

    label('loc_1AF36')

    Sleep(200)

    OP_3B(0xFF, 0.6, 0.6, 0.1)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B012',
    )

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.05), ParamFloat(0.2), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)

    def _loc_1B012(): pass

    label('loc_1B012')

    Sleep(200)

    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(400)

    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(500)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x0124 offset: 0x1B220
@scena.Code('AniCvAssaultAttack_endfook')
def AniCvAssaultAttack_endfook():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0xFFFE, 'C_EQU622', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0xFFFE, 'C_EQU622', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0125 offset: 0x1B35C
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x1780), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(633)

    Call(ScriptId.Current, 'EraseEquipL')
    Call(ScriptId.Current, 'EraseEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0126 offset: 0x1B4B8
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B4DD',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_1B4DD(): pass

    label('loc_1B4DD')

    Return()

# id: 0x0127 offset: 0x1B4E0
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B542',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_1B542(): pass

    label('loc_1B542')

    Return()

# id: 0x0128 offset: 0x1B544
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_1B5C7',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_1B6AA')

    def _loc_1B5C7(): pass

    label('loc_1B5C7')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x071E), ParamInt(0x071F), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_1B6AA(): pass

    label('loc_1B6AA')

    Return()

# id: 0x0129 offset: 0x1B6AC
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x0720), ParamInt(0x0721), ParamInt(0), ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0xF54),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B7DC',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), 0xFFE0, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_1B82E')

    def _loc_1B7DC(): pass

    label('loc_1B7DC')

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_1B82E(): pass

    label('loc_1B82E')

    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Sleep(500)

    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)
    Sleep(300)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x012A offset: 0x1B948
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1BA02',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '5', '5', '', '#b', '0')

    Jump('loc_1BA76')

    def _loc_1BA02(): pass

    label('loc_1BA02')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x0738), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4', '', '#b', '0')

    def _loc_1BA76(): pass

    label('loc_1BA76')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1#36w4#106w5#76w4[autoE4]', '0[autoM0]', '0[autoB0]', '#b', '0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BB15',
    )

    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '', '13434134', '', '#b', '0')

    Jump('loc_1BB3B')

    def _loc_1BB15(): pass

    label('loc_1BB15')

    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', '13434134', '', '#b', '0')
    Sleep(100)

    def _loc_1BB3B(): pass

    label('loc_1BB3B')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(500)

    Return()

# id: 0x012B offset: 0x1BBA8
@scena.Code('AniMG12Wait')
def AniMG12Wait():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012C offset: 0x1BBE0
@scena.Code('AniMG12LeanLeft')
def AniMG12LeanLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA_SLANT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012D offset: 0x1BC20
@scena.Code('AniMG12LeanRight')
def AniMG12LeanRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA_SLANT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012E offset: 0x1BC60
@scena.AnimeClips('_PlayFakeEffect')
def _PlayFakeEffect():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'system/shadow_chr_aura.eff',
        ),
    )

# id: 0x012F offset: 0x1BCC0
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
    )

# id: 0x0130 offset: 0x1BD40
@scena.AnimeClips('_AniAttachMainWeapon_L')
def _AniAttachMainWeapon_L():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
    )

# id: 0x0131 offset: 0x1BDA0
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0132 offset: 0x1BE20
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000708,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000709,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070A,
            name   = '',
        ),
    )

# id: 0x0133 offset: 0x1BED0
@scena.AnimeClips('_AniEv04065')
def _AniEv04065():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV04065',
        ),
    )

# id: 0x0134 offset: 0x1BF30
@scena.AnimeClips('_AniEv35000')
def _AniEv35000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV35000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007539,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0135 offset: 0x1BFE0
@scena.AnimeClips('_AniEv70000_3')
def _AniEv70000_3():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70000_3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70000_3a',
        ),
    )

# id: 0x0136 offset: 0x1C060
@scena.AnimeClips('_AniEv70001_3')
def _AniEv70001_3():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70001_3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70001_3a',
        ),
    )

# id: 0x0137 offset: 0x1C0E0
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'STOP_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'PRE_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0138 offset: 0x1C370
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x0139 offset: 0x1C440
@scena.AnimeClips('_AniRun')
def _AniRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x013A offset: 0x1C4C0
@scena.AnimeClips('_AniDash')
def _AniDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DASH',
        ),
    )

# id: 0x013B offset: 0x1C540
@scena.AnimeClips('_AniBack')
def _AniBack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x013C offset: 0x1C5A0
@scena.AnimeClips('_AniSitWait')
def _AniSitWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x013D offset: 0x1C600
@scena.AnimeClips('_AniWait1')
def _AniWait1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
    )

# id: 0x013E offset: 0x1C660
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_LEFT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_RIGHT',
        ),
    )

# id: 0x013F offset: 0x1C730
@scena.AnimeClips('_AniSquat')
def _AniSquat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
    )

# id: 0x0140 offset: 0x1C830
@scena.AnimeClips('_AniFall')
def _AniFall():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FALL',
        ),
    )

# id: 0x0141 offset: 0x1C890
@scena.AnimeClips('_AniLand')
def _AniLand():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'LAND',
        ),
    )

# id: 0x0142 offset: 0x1C8F0
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000075A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000075B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0143 offset: 0x1C9C0
@scena.AnimeClips('_AniFieldAttack')
def _AniFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0144 offset: 0x1CAC0
@scena.AnimeClips('_AniAssaultAttack')
def _AniAssaultAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU466',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000710,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000711,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0145 offset: 0x1CC10
@scena.AnimeClips('_AniAssaultAttackEnd')
def _AniAssaultAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
    )

# id: 0x0146 offset: 0x1CC90
@scena.AnimeClips('_AniFieldAttackEnd')
def _AniFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0147 offset: 0x1CD40
@scena.AnimeClips('_AniFieldAttackEndShort')
def _AniFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
    )

# id: 0x0148 offset: 0x1CDC0
@scena.AnimeClips('_AniHorse')
def _AniHorse():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x0149 offset: 0x1CE20
@scena.AnimeClips('_AniHorseWalk')
def _AniHorseWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_WALK',
        ),
    )

# id: 0x014A offset: 0x1CE80
@scena.AnimeClips('_AniHorseRun')
def _AniHorseRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_RUN',
        ),
    )

# id: 0x014B offset: 0x1CEE0
@scena.AnimeClips('_AniHorseDash')
def _AniHorseDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_DASH',
        ),
    )

# id: 0x014C offset: 0x1CF40
@scena.AnimeClips('_AniHorseStop')
def _AniHorseStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_STOP',
        ),
    )

# id: 0x014D offset: 0x1CFA0
@scena.AnimeClips('_AniHorseTurnRight')
def _AniHorseTurnRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x014E offset: 0x1D020
@scena.AnimeClips('_AniHorseTurnLeft')
def _AniHorseTurnLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x014F offset: 0x1D0A0
@scena.AnimeClips('_AniHorseRearWait')
def _AniHorseRearWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x0150 offset: 0x1D100
@scena.AnimeClips('_AniHorseRearWalk')
def _AniHorseRearWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_WALK',
        ),
    )

# id: 0x0151 offset: 0x1D160
@scena.AnimeClips('_AniHorseRearRun')
def _AniHorseRearRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_RUN',
        ),
    )

# id: 0x0152 offset: 0x1D1C0
@scena.AnimeClips('_AniHorseRearStop')
def _AniHorseRearStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_STOP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x0153 offset: 0x1D240
@scena.AnimeClips('_AniHorseRearTurnRight')
def _AniHorseRearTurnRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x0154 offset: 0x1D2C0
@scena.AnimeClips('_AniHorseRearTurnLeft')
def _AniHorseRearTurnLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x0155 offset: 0x1D340
@scena.AnimeClips('_AniHorseRearDash')
def _AniHorseRearDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_DASH',
        ),
    )

# id: 0x0156 offset: 0x1D3A0
@scena.AnimeClips('_AniBikeWait')
def _AniBikeWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_BACK_END',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_WAIT',
        ),
    )

# id: 0x0157 offset: 0x1D420
@scena.AnimeClips('_AniBikeWaitLeft')
def _AniBikeWaitLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_WAIT_L',
        ),
    )

# id: 0x0158 offset: 0x1D480
@scena.AnimeClips('_AniBikeRun')
def _AniBikeRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_RUN',
        ),
    )

# id: 0x0159 offset: 0x1D4E0
@scena.AnimeClips('_AniBikeTilt')
def _AniBikeTilt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_TILT',
        ),
    )

# id: 0x015A offset: 0x1D540
@scena.AnimeClips('_AniBikeTiltR')
def _AniBikeTiltR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_TILT_R',
        ),
    )

# id: 0x015B offset: 0x1D5A0
@scena.AnimeClips('_AniBikeTiltL')
def _AniBikeTiltL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_TILT_L',
        ),
    )

# id: 0x015C offset: 0x1D600
@scena.AnimeClips('_AniBikeBack')
def _AniBikeBack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_BACK_START',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_BACK',
        ),
    )

# id: 0x015D offset: 0x1D680
@scena.AnimeClips('_AniBikeHandleWait')
def _AniBikeHandleWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_HANDLE_WAIT',
        ),
    )

# id: 0x015E offset: 0x1D6E0
@scena.AnimeClips('_AniBikeHandle')
def _AniBikeHandle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_HANDLE',
        ),
    )

# id: 0x015F offset: 0x1D740
@scena.AnimeClips('_AniBikeRearWait')
def _AniBikeRearWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_WAIT',
        ),
    )

# id: 0x0160 offset: 0x1D7A0
@scena.AnimeClips('_AniBikeRearRun')
def _AniBikeRearRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_RUN',
        ),
    )

# id: 0x0161 offset: 0x1D800
@scena.AnimeClips('_AniBikeRearTilt')
def _AniBikeRearTilt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_TILT',
        ),
    )

# id: 0x0162 offset: 0x1D860
@scena.AnimeClips('_AniBikeRearBack')
def _AniBikeRearBack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_BACK',
        ),
    )

# id: 0x0163 offset: 0x1D8C0
@scena.AnimeClips('_AniBikeRearHandleWait')
def _AniBikeRearHandleWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_HANDLE_WAIT',
        ),
    )

# id: 0x0164 offset: 0x1D920
@scena.AnimeClips('_AniBikeRearTiltL')
def _AniBikeRearTiltL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_TILT_L',
        ),
    )

# id: 0x0165 offset: 0x1D980
@scena.AnimeClips('_AniBikeRearTiltR')
def _AniBikeRearTiltR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_TILT_R',
        ),
    )

# id: 0x0166 offset: 0x1D9E0
@scena.AnimeClips('_AniBikeSideWait')
def _AniBikeSideWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_SIDE_WAIT',
        ),
    )

# id: 0x0167 offset: 0x1DA40
@scena.AnimeClips('_AniBikeSideRun')
def _AniBikeSideRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_SIDE_RUN',
        ),
    )

# id: 0x0168 offset: 0x1DAA0
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000731,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000730,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000733,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072F,
            name   = '',
        ),
    )

# id: 0x0169 offset: 0x1DBA0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000708,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000709,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070A,
            name   = '',
        ),
    )

# id: 0x016A offset: 0x1DCA0
@scena.AnimeClips('_AniBtlKisinReady')
def _AniBtlKisinReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000708,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000709,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070A,
            name   = '',
        ),
    )

# id: 0x016B offset: 0x1DDA0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000732,
            name   = '',
        ),
    )

# id: 0x016C offset: 0x1DE00
@scena.AnimeClips('_AniBtlWait')
def _AniBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x016D offset: 0x1DF00
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R',
        ),
    )

# id: 0x016E offset: 0x1DF80
@scena.AnimeClips('_AniBtlStepInKisinPt')
def _AniBtlStepInKisinPt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072A,
            name   = '',
        ),
    )

# id: 0x016F offset: 0x1DFE0
@scena.AnimeClips('_AniBtlStepOutKisinPt')
def _AniBtlStepOutKisinPt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000729,
            name   = '',
        ),
    )

# id: 0x0170 offset: 0x1E040
@scena.AnimeClips('_AniBtlAttack')
def _AniBtlAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0171 offset: 0x1E140
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000726,
            name   = '',
        ),
    )

# id: 0x0172 offset: 0x1E1A0
@scena.AnimeClips('_AniBtlDamage')
def _AniBtlDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0173 offset: 0x1E220
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000722,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000723,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000724,
            name   = '',
        ),
    )

# id: 0x0174 offset: 0x1E2D0
@scena.AnimeClips('_AniBtlSwoon')
def _AniBtlSwoon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0175 offset: 0x1E380
@scena.AnimeClips('_AniBtlWeak')
def _AniBtlWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0176 offset: 0x1E3E0
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000725,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0177 offset: 0x1E490
@scena.AnimeClips('_AniBtlItem')
def _AniBtlItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000720,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000721,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B80,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0178 offset: 0x1E590
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072B,
            name   = '',
        ),
    )

# id: 0x0179 offset: 0x1E5F0
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072C,
            name   = '',
        ),
    )

# id: 0x017A offset: 0x1E650
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000072D,
            name   = '',
        ),
    )

# id: 0x017B offset: 0x1E6B0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000739,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000073A,
            name   = '',
        ),
    )

# id: 0x017C offset: 0x1E730
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000749,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000074A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000074A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000073B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
    )

# id: 0x017D offset: 0x1E8D0
@scena.AnimeClips('_AniBtlLinkRushStart')
def _AniBtlLinkRushStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x017E offset: 0x1E930
@scena.AnimeClips('_AniBtlLinkRushMove')
def _AniBtlLinkRushMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x017F offset: 0x1E990
@scena.AnimeClips('_AniBtlLinkRush')
def _AniBtlLinkRush():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001093,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000079E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000079F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000007A0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0180 offset: 0x1EB00
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ORDER',
        ),
    )

# id: 0x0181 offset: 0x1EB60
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071C,
            name   = '',
        ),
    )

# id: 0x0182 offset: 0x1EBE0
@scena.AnimeClips('_AniBtlValiantAttack_Start')
def _AniBtlValiantAttack_Start():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ORDER',
        ),
    )

# id: 0x0183 offset: 0x1EC60
@scena.AnimeClips('_AniBtlKisinItemPa')
def _AniBtlKisinItemPa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000720,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000721,
            name   = '',
        ),
    )

# id: 0x0184 offset: 0x1ECE0
@scena.AnimeClips('_AniBtlKisinPartnerArts')
def _AniBtlKisinPartnerArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000720,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000721,
            name   = '',
        ),
    )

# id: 0x0185 offset: 0x1ED60
@scena.AnimeClips('_AniBtlCrucifixion')
def _AniBtlCrucifixion():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
    )

# id: 0x0186 offset: 0x1EDC0
@scena.AnimeClips('_AniBtlFloat')
def _AniBtlFloat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FLOAT',
        ),
    )

# id: 0x0187 offset: 0x1EE20
@scena.AnimeClips('_AniBtlDownHill')
def _AniBtlDownHill():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DOWNHILL',
        ),
    )

# id: 0x0188 offset: 0x1EE80
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000736,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000734,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000735,
            name   = '',
        ),
    )

# id: 0x0189 offset: 0x1EF30
@scena.AnimeClips('_AniBtlWin')
def _AniBtlWin():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x018A offset: 0x1EFE0
@scena.AnimeClips('_AniBtlWinKeirei')
def _AniBtlWinKeirei():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KEIREI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KEIREIa',
        ),
    )

# id: 0x018B offset: 0x1F060
@scena.AnimeClips('_AniBtlWinHitouchR')
def _AniBtlWinHitouchR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HITOUCH_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x018C offset: 0x1F0E0
@scena.AnimeClips('_AniBtlWin_link')
def _AniBtlWin_link():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x018D offset: 0x1F160
@scena.AnimeClips('_AniBtlWin_burst')
def _AniBtlWin_burst():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000737,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x018E offset: 0x1F230
@scena.AnimeClips('_AniBtlWinWait_burst')
def _AniBtlWinWait_burst():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x018F offset: 0x1F290
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0190 offset: 0x1F340
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
    )

# id: 0x0191 offset: 0x1F3C0
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0192 offset: 0x1F490
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU406',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000712,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0193 offset: 0x1F880
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_01_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/ryu3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/gra00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_01_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU466',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000713,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000714,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU622',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0194 offset: 0x1FB60
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr105_02_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/craftworld_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000715,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000716,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0195 offset: 0x1FDF0
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_04.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_06.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_07.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_08.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_09.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic105_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000717,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000718,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_18.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000719,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_15.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_16.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_17.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc105_00_19.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11a',
        ),
    )

# id: 0x0196 offset: 0x20850
@scena.AnimeClips('_AniBtlSCraft00_Finish')
def _AniBtlSCraft00_Finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0197 offset: 0x208B0
@scena.AnimeClips('_AniEvWait')
def _AniEvWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0198 offset: 0x20910
@scena.AnimeClips('_AniEvWalk')
def _AniEvWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x0199 offset: 0x20970
@scena.AnimeClips('_AniEvRun')
def _AniEvRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x019A offset: 0x209D0
@scena.AnimeClips('_AniEvDash')
def _AniEvDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DASH',
        ),
    )

# id: 0x019B offset: 0x20A30
@scena.AnimeClips('_AniEvSquat')
def _AniEvSquat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
    )

# id: 0x019C offset: 0x20B30
@scena.AnimeClips('_AniEvFall')
def _AniEvFall():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FALL',
        ),
    )

# id: 0x019D offset: 0x20B90
@scena.AnimeClips('_AniEvLand')
def _AniEvLand():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'LAND',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x019E offset: 0x20C10
@scena.AnimeClips('_AniEvIdle')
def _AniEvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLEa',
        ),
    )

# id: 0x019F offset: 0x20C90
@scena.AnimeClips('_AniEvBtlWait')
def _AniEvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A0 offset: 0x20CF0
@scena.AnimeClips('_AniEvBtlMove')
def _AniEvBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x01A1 offset: 0x20D50
@scena.AnimeClips('_AniEvBtlDash')
def _AniEvBtlDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
    )

# id: 0x01A2 offset: 0x20DB0
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x01A3 offset: 0x20E10
@scena.AnimeClips('_AniEvFieldAttackEnd')
def _AniEvFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01A4 offset: 0x20EC0
@scena.AnimeClips('_AniEvAttack')
def _AniEvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A5 offset: 0x20F40
@scena.AnimeClips('_AniEvDamage')
def _AniEvDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A6 offset: 0x20FC0
@scena.AnimeClips('_AniEvAria')
def _AniEvAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x01A7 offset: 0x21020
@scena.AnimeClips('_AniEvArts')
def _AniEvArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSa',
        ),
    )

# id: 0x01A8 offset: 0x210A0
@scena.AnimeClips('_AniEvBackStep')
def _AniEvBackStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A9 offset: 0x21120
@scena.AnimeClips('_AniEvDead')
def _AniEvDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x01AA offset: 0x211A0
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD1',
        ),
    )

# id: 0x01AB offset: 0x21200
@scena.AnimeClips('_AniEvItem')
def _AniEvItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AC offset: 0x21280
@scena.AnimeClips('_AniEvFrontStep')
def _AniEvFrontStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AD offset: 0x21300
@scena.AnimeClips('_AniEvWeak')
def _AniEvWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x01AE offset: 0x21360
@scena.AnimeClips('_AniEvWeakDamage')
def _AniEvWeakDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x01AF offset: 0x213E0
@scena.AnimeClips('_AniEvWin')
def _AniEvWin():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01B0 offset: 0x21460
@scena.AnimeClips('_AniEvLevelUp')
def _AniEvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x01B1 offset: 0x214E0
@scena.AnimeClips('_AniEvHorseWait')
def _AniEvHorseWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x01B2 offset: 0x21540
@scena.AnimeClips('_AniEvHorseWalk')
def _AniEvHorseWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_WALK',
        ),
    )

# id: 0x01B3 offset: 0x215A0
@scena.AnimeClips('_AniEvHorseRun')
def _AniEvHorseRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_RUN',
        ),
    )

# id: 0x01B4 offset: 0x21600
@scena.AnimeClips('_AniEvHorseStop')
def _AniEvHorseStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_STOP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x01B5 offset: 0x21680
@scena.AnimeClips('_AniEvHorseTurnRight')
def _AniEvHorseTurnRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x01B6 offset: 0x21700
@scena.AnimeClips('_AniEvHorseTurnLeft')
def _AniEvHorseTurnLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x01B7 offset: 0x21780
@scena.AnimeClips('_AniEvHorseDash')
def _AniEvHorseDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_DASH',
        ),
    )

# id: 0x01B8 offset: 0x217E0
@scena.AnimeClips('_AniEvHorseRearWait')
def _AniEvHorseRearWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x01B9 offset: 0x21840
@scena.AnimeClips('_AniEvHorseRearWalk')
def _AniEvHorseRearWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_WALK',
        ),
    )

# id: 0x01BA offset: 0x218A0
@scena.AnimeClips('_AniEvHorseRearRun')
def _AniEvHorseRearRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_RUN',
        ),
    )

# id: 0x01BB offset: 0x21900
@scena.AnimeClips('_AniEvHorseRearStop')
def _AniEvHorseRearStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_STOP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x01BC offset: 0x21980
@scena.AnimeClips('_AniEvHorseRearTurnRight')
def _AniEvHorseRearTurnRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x01BD offset: 0x21A00
@scena.AnimeClips('_AniEvHorseRearTurnLeft')
def _AniEvHorseRearTurnLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR',
        ),
    )

# id: 0x01BE offset: 0x21A80
@scena.AnimeClips('_AniEvHorseRearDash')
def _AniEvHorseRearDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_REAR_DASH',
        ),
    )

# id: 0x01BF offset: 0x21AE0
@scena.AnimeClips('_AniEvCraft00_01')
def _AniEvCraft00_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01a',
        ),
    )

# id: 0x01C0 offset: 0x21B60
@scena.AnimeClips('_AniEvCraft01_01')
def _AniEvCraft01_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
    )

# id: 0x01C1 offset: 0x21BE0
@scena.AnimeClips('_AniEvCraft01_02')
def _AniEvCraft01_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02a',
        ),
    )

# id: 0x01C2 offset: 0x21C60
@scena.AnimeClips('_AniBikeBackStart')
def _AniBikeBackStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_BACK_START',
        ),
    )

# id: 0x01C3 offset: 0x21CC0
@scena.AnimeClips('_AniBikeBackEnd')
def _AniBikeBackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_BACK_END',
        ),
    )

# id: 0x01C4 offset: 0x21D20
@scena.AnimeClips('_AniBikeWaitL')
def _AniBikeWaitL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_WAIT_L',
        ),
    )

# id: 0x01C5 offset: 0x21D80
@scena.AnimeClips('_AniEvSCraft00_01')
def _AniEvSCraft00_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
    )

# id: 0x01C6 offset: 0x21DE0
@scena.AnimeClips('_AniEvSCraft00_02')
def _AniEvSCraft00_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
    )

# id: 0x01C7 offset: 0x21E40
@scena.AnimeClips('_AniEvSCraft00_03')
def _AniEvSCraft00_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
    )

# id: 0x01C8 offset: 0x21EA0
@scena.AnimeClips('_AniEvSCraft00_04')
def _AniEvSCraft00_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
    )

# id: 0x01C9 offset: 0x21F00
@scena.AnimeClips('_AniEvSCraft00_05')
def _AniEvSCraft00_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
    )

# id: 0x01CA offset: 0x21F60
@scena.AnimeClips('_AniEvSCraft00_06')
def _AniEvSCraft00_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
    )

# id: 0x01CB offset: 0x21FC0
@scena.AnimeClips('_AniEvSCraft00_07')
def _AniEvSCraft00_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
    )

# id: 0x01CC offset: 0x22020
@scena.AnimeClips('_AniEvSCraft00_08')
def _AniEvSCraft00_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
    )

# id: 0x01CD offset: 0x22080
@scena.AnimeClips('_AniEvSCraft00_11')
def _AniEvSCraft00_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11a',
        ),
    )

# id: 0x01CE offset: 0x22100
@scena.AnimeClips('_AniEvCraft00_02')
def _AniEvCraft00_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02a',
        ),
    )

# id: 0x01CF offset: 0x22180
@scena.AnimeClips('_AniEvCraft00_03')
def _AniEvCraft00_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03a',
        ),
    )

# id: 0x01D0 offset: 0x22200
@scena.AnimeClips('_AniEvCraft01_03')
def _AniEvCraft01_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03a',
        ),
    )

# id: 0x01D1 offset: 0x22280
@scena.AnimeClips('_AniEvCraft02_01')
def _AniEvCraft02_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
    )

# id: 0x01D2 offset: 0x222E0
@scena.AnimeClips('_AniEvCraft02_03')
def _AniEvCraft02_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_03a',
        ),
    )

# id: 0x01D3 offset: 0x22360
@scena.AnimeClips('_AniEvCraft02_02')
def _AniEvCraft02_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_02',
        ),
    )

# id: 0x01D4 offset: 0x223C0
@scena.AnimeClips('_AniEvCraft02_04')
def _AniEvCraft02_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_04',
        ),
    )

# id: 0x01D5 offset: 0x22420
@scena.AnimeClips('_AniEvCraft02_05')
def _AniEvCraft02_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_05',
        ),
    )

# id: 0x01D6 offset: 0x22480
@scena.AnimeClips('_AniAttachEQU033')
def _AniAttachEQU033():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU033',
        ),
    )

# id: 0x01D7 offset: 0x224E0
@scena.AnimeClips('_AniAttachPhone')
def _AniAttachPhone():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320_C03',
        ),
    )

# id: 0x01D8 offset: 0x22540
@scena.AnimeClips('_AniEv91010')
def _AniEv91010():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91010',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91010a',
        ),
    )

# id: 0x01D9 offset: 0x225C0
@scena.AnimeClips('_AniEv91015')
def _AniEv91015():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91015',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91015a',
        ),
    )

# id: 0x01DA offset: 0x22640
@scena.AnimeClips('_AniEv91015b')
def _AniEv91015b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91015b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV91010a',
        ),
    )

# id: 0x01DB offset: 0x226C0
@scena.AnimeClips('_AniAttachEQU757')
def _AniAttachEQU757():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU757',
        ),
    )

# id: 0x01DC offset: 0x22720
@scena.AnimeClips('_AniEv_B3_14_00_05')
def _AniEv_B3_14_00_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_05',
        ),
    )

# id: 0x01DD offset: 0x22780
@scena.AnimeClips('_AniEv_B3_14_00_06')
def _AniEv_B3_14_00_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_06',
        ),
    )

# id: 0x01DE offset: 0x227E0
@scena.AnimeClips('_AniEv_B3_14_00_1_07')
def _AniEv_B3_14_00_1_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_07',
        ),
    )

# id: 0x01DF offset: 0x22840
@scena.AnimeClips('_AniEv_B3_14_00_1_08')
def _AniEv_B3_14_00_1_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_08',
        ),
    )

# id: 0x01E0 offset: 0x228A0
@scena.AnimeClips('_AniEv_B3_14_00_1_09')
def _AniEv_B3_14_00_1_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_09',
        ),
    )

# id: 0x01E1 offset: 0x22900
@scena.AnimeClips('_AniEv_B3_14_00_1_11')
def _AniEv_B3_14_00_1_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_11',
        ),
    )

# id: 0x01E2 offset: 0x22960
@scena.AnimeClips('_AniEv_B3_14_00_1_11A')
def _AniEv_B3_14_00_1_11A():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_11A',
        ),
    )

# id: 0x01E3 offset: 0x229C0
@scena.AnimeClips('_AniEv_B3_14_00_1_11B')
def _AniEv_B3_14_00_1_11B():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_11B',
        ),
    )

# id: 0x01E4 offset: 0x22A20
@scena.AnimeClips('_AniEv_B3_14_00_1_11C')
def _AniEv_B3_14_00_1_11C():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_11C',
        ),
    )

# id: 0x01E5 offset: 0x22A80
@scena.AnimeClips('_AniEv_B3_14_00_1_11D')
def _AniEv_B3_14_00_1_11D():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_11D',
        ),
    )

# id: 0x01E6 offset: 0x22AE0
@scena.AnimeClips('_AniEv_B3_14_00_1_12')
def _AniEv_B3_14_00_1_12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_12',
        ),
    )

# id: 0x01E7 offset: 0x22B40
@scena.AnimeClips('_AniEv_B3_14_00_1_13')
def _AniEv_B3_14_00_1_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_13',
        ),
    )

# id: 0x01E8 offset: 0x22BA0
@scena.AnimeClips('_AniEv_B3_14_00_1_16')
def _AniEv_B3_14_00_1_16():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_B3_14_00_1_16',
        ),
    )

# id: 0x01E9 offset: 0x22C00
@scena.AnimeClips('_AniEv_Z1_00_08_08')
def _AniEv_Z1_00_08_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_08_08',
        ),
    )

# id: 0x01EA offset: 0x22C60
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU466',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk105_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk001b.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk105_a0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk105_a1.eff',
        ),
    )

# id: 0x01EB offset: 0x22D60
@scena.AnimeClips('_AniCvWait')
def _AniCvWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01EC offset: 0x22DC0
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000075A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000075B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01ED offset: 0x22E90
@scena.AnimeClips('_AniCvBtlWait')
def _AniCvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV35000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007539,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01EE offset: 0x22F40
@scena.AnimeClips('_AniCvAttack')
def _AniCvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000070F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01EF offset: 0x23040
@scena.AnimeClips('_AniCvAssaultAttack')
def _AniCvAssaultAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000710,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000711,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01F0 offset: 0x23160
@scena.AnimeClips('_AniCvFieldAttackEnd')
def _AniCvFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001780,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01F1 offset: 0x23210
@scena.AnimeClips('_AniCvAria')
def _AniCvAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000071F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x01F2 offset: 0x23310
@scena.AnimeClips('_AniCvArts')
def _AniCvArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000720,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000721,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01F3 offset: 0x23460
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x01F4 offset: 0x23530
@scena.AnimeClips('_AniMG12Wait')
def _AniMG12Wait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG12_BANANA',
        ),
    )

# id: 0x01F5 offset: 0x23590
@scena.AnimeClips('_AniMG12LeanLeft')
def _AniMG12LeanLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG12_BANANA_SLANT_L',
        ),
    )

# id: 0x01F6 offset: 0x235F0
@scena.AnimeClips('_AniMG12LeanRight')
def _AniMG12LeanRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG12_BANANA_SLANT_R',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
