import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr113.dat')

# id: 0x0000 offset: 0x33C4
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'DISARM_SHORT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'FATTACK1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'FATTACK2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR113_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR010_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT01_00b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT03_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT03_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT03_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT03_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR113_BT1',
            symbol     = 'BTL_CRAFT03_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_00_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_00_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_01_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_02_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_02_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_03_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_04_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_05_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_06_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_07_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_08_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR113_SC1',
            symbol     = 'BTL_S_CRAFT00_09_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB_a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB_b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_PONPON',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR113_BT3',
            symbol     = 'BTL_WIN_PONPON_a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR001_HS1',
            symbol     = 'HORSE_REAR',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_WAIT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_TILT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_BACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_HANDLE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_TILT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_REAR_TILT_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_SIDE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR113_HS1',
            symbol     = 'BIKE_SIDE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_I5_24_00_CUT023',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_NAISHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_NAISHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP51_TEHIKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP51_TEHIKI_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP51_TEHIKI_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP52_TUREHASIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP52_TUREHASIRI_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP52_TUREHASIRI_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP53_NAKAYOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP53_NAKAYOSI_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_OP53_NAKAYOSI_GS',
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
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SIANF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SIANFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
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
            asset      = 'C_CHR113_EV',
            symbol     = 'EV00400',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV00400a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV03030',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV03544',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV03545',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV04105',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV09030_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV09030_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV09035',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV09035a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV40070',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV40072',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV40072a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV40074',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV40085',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV52655',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV52660',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV52665',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV52665w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70145',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70150',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70150a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70161',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70161a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70162',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV70162a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV73535',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV73535_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV73535a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV73535a_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV74300',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV74300a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV74310',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV77069',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV77070',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV77070_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV77070_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV77070a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79410',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79412',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79412a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79414',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79416',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79416a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79416w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79422',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79424',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79424a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79426',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79426a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79430',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79430_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79431',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79431_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79432',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79432_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79432a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79432a_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79433',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79433_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79433a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EV',
            symbol     = 'EV79433a_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C2_12_02_cut001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C2_12_02_cut002',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C2_12_02_cut005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C2_12_02_cut006',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut001a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut001b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut001c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut003',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut003a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'FC_C3_10_00_cut005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_02_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_03_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_05_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_06_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_10_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_11_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_12_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_13_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC08',
            symbol     = 'EV_C1_01_01_14_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT002',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT003',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT004',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT006',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT009',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT011',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC',
            symbol     = 'EV_C3_03_00_CUT012',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC19',
            symbol     = 'EV_C4_02_02_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC19',
            symbol     = 'EV_C4_02_02_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC19',
            symbol     = 'EV_C4_02_02_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC19',
            symbol     = 'EV_C4_02_02_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_07_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_07_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_17_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_17_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_24_25',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_24_25_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_53',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_53_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_54',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_54_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_55',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR113_EVC30',
            symbol     = 'EV_Z1_00_53_55_F',
        ),
    )

# id: 0x0001 offset: 0xE0FC
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xE11C
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xE134
@scena.Code('PreInit')
def PreInit():
    AnimeClipCmd(0x0D, PseudoChrId.Self)

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_E179',
    )

    AnimeClipCmd(0x0F, PseudoChrId.Self, 0x00)
    AnimeClipCmd(0x0D, PseudoChrId.Self)
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR113_DF1', 'WAIT')

    Return()

    def _loc_E179(): pass

    label('loc_E179')

    Return()

# id: 0x0004 offset: 0xE17C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "ModelCmd(0x3F)"),
            Expr.Return,
        ),
        'loc_E18E',
    )

    Return()

    def _loc_E18E(): pass

    label('loc_E18E')

    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0xFFFE, 0x25, 'battle/disarm113.eff', 0x00000000)
    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'EraseEquip')
    OP_2A(0x04, 0xFFFE, '', 'gamePos0', '')

    Return()

# id: 0x0005 offset: 0xE220
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0006 offset: 0xE248
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0007 offset: 0xE274
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0008 offset: 0xE280
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0009 offset: 0xE290
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x000A offset: 0xE2A0
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR113_BT3')

    Return()

# id: 0x000B offset: 0xE2B8
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000C offset: 0xE2C8
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000D offset: 0xE2D8
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000E offset: 0xE2E8
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000F offset: 0xE300
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR113_BT3')

    Return()

# id: 0x0010 offset: 0xE318
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xE330
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0012 offset: 0xE348
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU610')
    AttachEquip(0xFFFE, 'C_EQU610', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0013 offset: 0xE3F8
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU610')

    Return()

# id: 0x0014 offset: 0xE444
@scena.Code('AniDebugFlagOff')
def AniDebugFlagOff():
    ExecExpressionWithReg(
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0xE454
@scena.Code('AniReset')
def AniReset():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_E489',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_E489(): pass

    label('loc_E489')

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

# id: 0x0016 offset: 0xE50C
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

# id: 0x0017 offset: 0xE51C
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

# id: 0x0018 offset: 0xE52C
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0019 offset: 0xE558
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_E572',
    )

    Jump('loc_E5B3')

    def _loc_E572(): pass

    label('loc_E572')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_E5B3(): pass

    label('loc_E5B3')

    Return()

# id: 0x001A offset: 0xE5B4
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x001B offset: 0xE5C0
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

# id: 0x001C offset: 0xE628
@scena.Code('OnCostumeColor')
def OnCostumeColor():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_E63A',
    )

    Return()

    def _loc_E63A(): pass

    label('loc_E63A')

    If(
        (
            (Expr.Eval, "WeatherCmd(4002, 0xFFFE)"),
            Expr.Return,
        ),
        'loc_E68E',
    )

    OP_4C(0xFE19, 0.05, 0.05, 0.2, 0x0000, 0x03)
    ChrSetRGBA(0xFE19, 0.6, 1.0, 0.9, 0.9, 0, 0x03)
    WeatherCmd(4000, 0xFE19, 0.8, 0x0000, 0x03)

    def _loc_E68E(): pass

    label('loc_E68E')

    Return()

# id: 0x001D offset: 0xE690
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

# id: 0x001E offset: 0xE6F4
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

# id: 0x001F offset: 0xE76C
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

# id: 0x0020 offset: 0xE7DC
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

# id: 0x0021 offset: 0xE874
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0022 offset: 0xE8D0
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

    OP_3B(0x3A, 0xFFFE, ParamInt(4600), ParamInt(0x11F9), ParamInt(0x11FA), ParamInt(0))

    Return()

# id: 0x0023 offset: 0xE90C
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0024 offset: 0xE924
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x0025 offset: 0xE93C
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHeadTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHeadTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMuneTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMuneTai02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMuneTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMuneTai02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftKosiTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftKosiTai02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftKosiTai03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightKosiTai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightKosiTai02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightKosiTai03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_k_yure', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_k_yure', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_Sode_In', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_Sode_Out', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_Sode_F', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_Sode_B', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_Sode_In', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_Sode_Out', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_Sode_F', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_Sode_B', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FSIn02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FSIn03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BSIn02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BSIn03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftInSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftInSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftInSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftInSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightInSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightInSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightInSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightInSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BSOut02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BSOut03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BSOut04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftOutSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftOutSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftOutSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftOutSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftOutSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightOutSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightOutSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightOutSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightOutSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightOutSB04', 0.2)

    Return()

# id: 0x0026 offset: 0xEE6C
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHeadTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHeadTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMuneTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMuneTai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMuneTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMuneTai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftKosiTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftKosiTai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftKosiTai03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightKosiTai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightKosiTai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightKosiTai03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_k_yure', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_k_yure', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_In', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_Out', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_F', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_B', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_Sode_In', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_Sode_Out', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_Sode_F', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_Sode_B', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FSIn02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FSIn03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BSIn02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BSIn03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftInSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftInSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftInSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftInSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightInSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightInSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightInSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightInSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BSOut02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BSOut03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BSOut04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftOutSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftOutSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftOutSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftOutSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftOutSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightOutSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightOutSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightOutSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightOutSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightOutSB04', 0.2)

    Return()

# id: 0x0027 offset: 0xF39C
@scena.Code('SpringOffHead_0')
def SpringOffHead_0():
    OP_8A(0xFF, 0xFFFE, 'RightBH01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'RightBH02', 0.0)
    OP_8A(0xFF, 0xFFFE, 'LeftBH01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'LeftBH02', 0.0)

    Return()

# id: 0x0028 offset: 0xF3F4
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0029 offset: 0xF3F8
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x002A offset: 0xF3FC
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x002B offset: 0xF400
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x002C offset: 0xF404
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
        'loc_F4C4',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F497',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_F4BB')

    def _loc_F497(): pass

    label('loc_F497')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F4BB(): pass

    label('loc_F4BB')

    Jump('loc_F89D')

    def _loc_F4C4(): pass

    label('loc_F4C4')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_F66C',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F51D',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_F51D(): pass

    label('loc_F51D')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F5AC',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_F663')

    def _loc_F5AC(): pass

    label('loc_F5AC')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F63C',
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

    Jump('loc_F663')

    def _loc_F63C(): pass

    label('loc_F63C')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_F663(): pass

    label('loc_F663')

    Jump('loc_F89D')

    def _loc_F66C(): pass

    label('loc_F66C')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_F6C8',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_F89D')

    def _loc_F6C8(): pass

    label('loc_F6C8')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F761',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_F89D')

    def _loc_F761(): pass

    label('loc_F761')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F7F3',
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

    Jump('loc_F89D')

    def _loc_F7F3(): pass

    label('loc_F7F3')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F871',
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

    Jump('loc_F89D')

    def _loc_F871(): pass

    label('loc_F871')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_F89D(): pass

    label('loc_F89D')

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

# id: 0x002D offset: 0xF8C4
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
        'loc_F985',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F955',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_F955(): pass

    label('loc_F955')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_F9FC')

    def _loc_F985(): pass

    label('loc_F985')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F9D9',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_F9D9(): pass

    label('loc_F9D9')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F9FC(): pass

    label('loc_F9FC')

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

# id: 0x002E offset: 0xFA2C
@scena.Code('AniRun')
def AniRun():
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
        'loc_FA8F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FAB1')

    def _loc_FA8F(): pass

    label('loc_FA8F')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FAB1(): pass

    label('loc_FAB1')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FAD0',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FAD0(): pass

    label('loc_FAD0')

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

# id: 0x002F offset: 0xFAF4
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

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_FB57',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FB7A')

    def _loc_FB57(): pass

    label('loc_FB57')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FB7A(): pass

    label('loc_FB7A')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FB99',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FB99(): pass

    label('loc_FB99')

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

# id: 0x0030 offset: 0xFBBC
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

# id: 0x0031 offset: 0xFC18
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0032 offset: 0xFC5C
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x0033 offset: 0xFC9C
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
        'loc_FD67',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FD1B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FD5E')

    def _loc_FD1B(): pass

    label('loc_FD1B')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FD5E',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FD5E(): pass

    label('loc_FD5E')

    Jump('loc_FDF5')

    def _loc_FD67(): pass

    label('loc_FD67')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FDB2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FDF5')

    def _loc_FDB2(): pass

    label('loc_FDB2')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FDF5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FDF5(): pass

    label('loc_FDF5')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0034 offset: 0xFE14
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
        'loc_FE72',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FF5B')

    def _loc_FE72(): pass

    label('loc_FE72')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_FEFD',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_FF5B')

    def _loc_FEFD(): pass

    label('loc_FEFD')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FF5B(): pass

    label('loc_FF5B')

    Return()

# id: 0x0035 offset: 0xFF5C
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0036 offset: 0xFF98
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
        'loc_FFF1',
    )

    Sleep(500)

    Jump('loc_FFFD')

    def _loc_FFF1(): pass

    label('loc_FFF1')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_FFFD(): pass

    label('loc_FFFD')

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

# id: 0x0037 offset: 0x10034
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
        'loc_100C9',
    )

    OP_3B(0x32, ParamInt(0x1251), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1011E')

    def _loc_100C9(): pass

    label('loc_100C9')

    OP_3B(0x32, ParamInt(0x1252), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1011E(): pass

    label('loc_1011E')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '0#46w1110#306w5#186w4#86w10[autoE0]', '0[autoM0]', '#50e0#106w77#100e7#106w#55e7#100e0#47e3#100e3#246w7#146w#51e0#100e0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0038 offset: 0x10208
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk113_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk113_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk113_3.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_102C5',
    )

    LoadEffect(0xFFFE, 0x24, 'battle/atk113_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x27, 'battle/cr113_01_1.eff', 0x00000000)

    def _loc_102C5(): pass

    label('loc_102C5')

    Return()

# id: 0x0039 offset: 0x102C8
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x26)
    ReleaseEffect(0xFFFE, 0x27)

    Return()

# id: 0x003A offset: 0x102F8
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
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 5)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.74, 3.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 9)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FD), ParamInt(0x11FE), ParamInt(0x11FF), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.019), ParamFloat(0.945), ParamFloat(0.422), -5.243, 33.689, 133.311, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x0FE5), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    CameraCmd(0x0A, 0.0, 0.2, 1.0, 0, 100, 0, 0, 0, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.881), ParamFloat(-0.012), ParamFloat(1.359), 0.0, 0.0, 0.0, ParamFloat(1.3), ParamFloat(1.3), ParamFloat(1.3), 0x11)
    OP_3B(0x00, ParamInt(0x0FE7), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_AD(0x01, 0x01)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003B offset: 0x105E0
@scena.Code('AniFieldAttack2')
def AniFieldAttack2():
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
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK2', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 9)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FD), ParamInt(0x11FE), ParamInt(0x11FF), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.005), ParamFloat(0.794), ParamFloat(0.75), 0.968, 3.641, 33.77, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x0FE5), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(600), ParamInt(0x0064), 0x0000, 0x0258, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 11)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.74, 5.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 13)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x14)
    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_AD(0x01, 0x01)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003C offset: 0x10854
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
    SetEndhookFunction('AniAssaultAttack_endhook', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '006#96w0[autoB0]', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x0FB7), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1010), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0027), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.9), ParamFloat(0), 0.0, 0.0, 90.0, ParamFloat(0.25), ParamFloat(0.5), ParamFloat(0.25), 0x15)
    WaitAnimeClipFrames(PseudoChrId.Self, 30)
    EffectSetRGBA(0xFFFE, 0x15, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 42)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 1.66667, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 55)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1200), ParamInt(0x11FE), ParamInt(0x1201), ParamInt(0))
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0014))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0.5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x12)
    OP_3B(0x00, ParamInt(0x0FC4), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10F4), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F54), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1200), ParamInt(300), 0x0000, 0x04B0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 70)
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003D offset: 0x10D4C
@scena.Code('AniAssaultAttack_endhook')
def AniAssaultAttack_endhook():
    OP_41(0xFFFE, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')

    Return()

# id: 0x003E offset: 0x10D7C
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

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'fold', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_3B(0x00, ParamInt(0x177F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 29)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x13)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClipFrames(PseudoChrId.Self, 71)
    StopEffect(0xFFFE, 0x13, 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003F offset: 0x10F84
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    StopEffect(0xFFFE, 0x13, 0x01)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0040 offset: 0x10FEC
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
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_SHORT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(466)

    OP_3B(0x00, ParamInt(0x7537), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(366)

    Call(ScriptId.Current, 'EraseEquip')
    Sleep(133)

    Return()

# id: 0x0041 offset: 0x110F4
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x0042 offset: 0x110F8
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x0043 offset: 0x110FC
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0044 offset: 0x11134
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0045 offset: 0x11174
@scena.Code('AniHorseRun')
def AniHorseRun():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0046 offset: 0x111B4
@scena.Code('AniHorseDash')
def AniHorseDash():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0047 offset: 0x111F4
@scena.Code('AniHorseStop')
def AniHorseStop():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0048 offset: 0x11234
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0049 offset: 0x11290
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004A offset: 0x112EC
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
        'loc_113FE',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5C(0xFFFE, 0x00, 'up_point')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, 8.0, 9.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, 8.0, -6.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_113FE(): pass

    label('loc_113FE')

    OP_80(0.0)
    OP_04(0x0B, 'AniHorseRearWait')

    Return()

# id: 0x004B offset: 0x1141C
@scena.Code('AniHorseRearEnd')
def AniHorseRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x004C offset: 0x11460
@scena.Code('AniHorseRearWait')
def AniHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0x11498
@scena.Code('AniHorseRearWalk')
def AniHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0x114D4
@scena.Code('AniHorseRearRun')
def AniHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0x11510
@scena.Code('AniHorseRearStop')
def AniHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0050 offset: 0x11574
@scena.Code('AniHorseRearTurnRight')
def AniHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0051 offset: 0x115DC
@scena.Code('AniHorseRearTurnLeft')
def AniHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0052 offset: 0x11644
@scena.Code('AniHorseRearDash')
def AniHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0053 offset: 0x11680
@scena.Code('AniBikeRearStart')
def AniBikeRearStart():
    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_1175E',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, -10.0, -5.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, -5.0, 5.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_1175E(): pass

    label('loc_1175E')

    OP_80(0.0)
    OP_04(0x0B, 'AniBikeRearWait')

    Return()

# id: 0x0054 offset: 0x1177C
@scena.Code('AniBikeRearEnd')
def AniBikeRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x0055 offset: 0x117C0
@scena.Code('AniBikeRearWait')
def AniBikeRearWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0x1180C
@scena.Code('AniBikeRearWaitLeft')
def AniBikeRearWaitLeft():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0057 offset: 0x1185C
@scena.Code('AniBikeRearRun')
def AniBikeRearRun():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0058 offset: 0x118A8
@scena.Code('AniBikeRearTilt')
def AniBikeRearTilt():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0059 offset: 0x118F4
@scena.Code('AniBikeRearBack')
def AniBikeRearBack():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_BACK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0x11940
@scena.Code('AniBikeRearHandleWait')
def AniBikeRearHandleWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_HANDLE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005B offset: 0x11994
@scena.Code('AniBikeRearTiltL')
def AniBikeRearTiltL():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005C offset: 0x119E4
@scena.Code('AniBikeRearTiltR')
def AniBikeRearTiltR():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0x11A34
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005E offset: 0x11A70
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0x11AAC
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0060 offset: 0x11AD8
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_11AF4',
    )

    Return()

    def _loc_11AF4(): pass

    label('loc_11AF4')

    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0061 offset: 0x11B04
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_11B2C',
    )

    Return()

    def _loc_11B2C(): pass

    label('loc_11B2C')

    Call(ScriptId.BtlCom, 'AniBtlInit')

    Return()

# id: 0x0062 offset: 0x11B40
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0063 offset: 0x11B58
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_11DBC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11BE1',
    )

    OP_3B(0x32, ParamInt(0x1270), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11DA4')

    def _loc_11BE1(): pass

    label('loc_11BE1')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x12E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11C51',
    )

    OP_3B(0x32, ParamInt(0x126E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11DA4')

    def _loc_11C51(): pass

    label('loc_11C51')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11DA4',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11CD9',
    )

    OP_3B(0x32, ParamInt(0x127B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11DA4')

    def _loc_11CD9(): pass

    label('loc_11CD9')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D4F',
    )

    OP_3B(0x32, ParamInt(0x127C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11DA4')

    def _loc_11D4F(): pass

    label('loc_11D4F')

    OP_3B(0x32, ParamInt(0x127D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11DA4(): pass

    label('loc_11DA4')

    Sleep(1000)

    OP_3B(0x39, 0xFFFE)

    Jump('loc_12006')

    def _loc_11DBC(): pass

    label('loc_11DBC')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E32',
    )

    OP_3B(0x32, ParamInt(0x1227), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12006')

    def _loc_11E32(): pass

    label('loc_11E32')

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
        'loc_11EC6',
    )

    OP_3B(0x32, ParamInt(0x1226), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12006')

    def _loc_11EC6(): pass

    label('loc_11EC6')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11F3C',
    )

    OP_3B(0x32, ParamInt(0x1229), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12006')

    def _loc_11F3C(): pass

    label('loc_11F3C')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11FB1',
    )

    OP_3B(0x32, ParamInt(0x1224), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12006')

    def _loc_11FB1(): pass

    label('loc_11FB1')

    OP_3B(0x32, ParamInt(0x1225), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12006(): pass

    label('loc_12006')

    Return()

# id: 0x0064 offset: 0x12008
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_12045',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FB), ParamInt(0x11FC), ParamInt(0), ParamInt(0))

    Jump('loc_12065')

    def _loc_12045(): pass

    label('loc_12045')

    OP_3B(0x3A, 0xFFFE, ParamInt(4600), ParamInt(0x11F9), ParamInt(0x11FA), ParamInt(0))

    def _loc_12065(): pass

    label('loc_12065')

    Return()

# id: 0x0065 offset: 0x12068
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_120A5',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FB), ParamInt(0x11FC), ParamInt(0), ParamInt(0))

    Jump('loc_120C5')

    def _loc_120A5(): pass

    label('loc_120A5')

    OP_3B(0x3A, 0xFFFE, ParamInt(4600), ParamInt(0x11F9), ParamInt(0x11FA), ParamInt(0))

    def _loc_120C5(): pass

    label('loc_120C5')

    Return()

# id: 0x0066 offset: 0x120C8
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x1228), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0067 offset: 0x12120
@scena.Code('AniBtlWait')
def AniBtlWait():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_12155',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_12155(): pass

    label('loc_12155')

    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0068 offset: 0x12194
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x0069 offset: 0x121D0
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1221C',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1225F')

    def _loc_1221C(): pass

    label('loc_1221C')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1225F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1225F(): pass

    label('loc_1225F')

    Return()

# id: 0x006A offset: 0x12260
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x1220))

    Return()

# id: 0x006B offset: 0x1227C
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x121F))

    Return()

# id: 0x006C offset: 0x12298
@scena.Code('AniBtlStepInKisinPt')
def AniBtlStepInKisinPt():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x1220), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x1220))

    Return()

# id: 0x006D offset: 0x12328
@scena.Code('AniBtlStepOutKisinPt')
def AniBtlStepOutKisinPt():
    OP_3B(0x32, ParamInt(0x121F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x121F))

    Return()

# id: 0x006E offset: 0x1238C
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 1.0, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_3B(0x00, ParamInt(0xFFFF), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.019), ParamFloat(0.945), ParamFloat(0.422), -5.243, 33.689, 133.311, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x000A))

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12638',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12618',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x12E),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1255B',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FD), ParamInt(0x11FE), ParamInt(0x11FF), ParamInt(0))

    Jump('loc_1260F')

    def _loc_1255B(): pass

    label('loc_1255B')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1260F',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_125AE',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x127E), ParamInt(0x127F), ParamInt(0x1280), ParamInt(0x1282))

    Jump('loc_1260F')

    def _loc_125AE(): pass

    label('loc_125AE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_125EF',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x127E), ParamInt(0x1282), ParamInt(0x1283), ParamInt(0x1284))

    Jump('loc_1260F')

    def _loc_125EF(): pass

    label('loc_125EF')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1280), ParamInt(0x1282), ParamInt(0x1283), ParamInt(0x1284))

    def _loc_1260F(): pass

    label('loc_1260F')

    Jump('loc_12638')

    def _loc_12618(): pass

    label('loc_12618')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FD), ParamInt(0x11FE), ParamInt(0x11FF), ParamInt(0))

    def _loc_12638(): pass

    label('loc_12638')

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_12678',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.3)

    def _loc_12678(): pass

    label('loc_12678')

    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 27)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.881), ParamFloat(-0.012), ParamFloat(1.359), 0.0, 0.0, 0.0, ParamFloat(1.3), ParamFloat(1.3), ParamFloat(1.3), 0x11)
    CameraCmd(0x0A, 0.0, 0.2, 1.0, 0, 100, 0, 0, 0, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x006F offset: 0x127C0
@scena.Code('AniBtlTargetScaleTest')
def AniBtlTargetScaleTest():
    BattleCmd(0x54, 0xFFFB, 0x01, 1.1, 4.5, -1.0)

    Return()

# id: 0x0070 offset: 0x127D8
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, ParamInt(0x121C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0071 offset: 0x12844
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
        'loc_128A5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_128CE')

    def _loc_128A5(): pass

    label('loc_128A5')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_128CE(): pass

    label('loc_128CE')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0072 offset: 0x128DC
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_1292C',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1218), ParamInt(0x1219), ParamInt(0), ParamInt(0))

    Jump('loc_1294C')

    def _loc_1292C(): pass

    label('loc_1292C')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1218), ParamInt(0x1219), ParamInt(0x121A), ParamInt(0))

    def _loc_1294C(): pass

    label('loc_1294C')

    Return()

# id: 0x0073 offset: 0x12950
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12AE7',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x12E),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_129E2',
    )

    OP_3B(0x32, ParamInt(0x121A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12ADE')

    def _loc_129E2(): pass

    label('loc_129E2')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12ADE',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12A4D',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1274), ParamInt(0x1275), ParamInt(0), ParamInt(0))
    OP_3B(0x34, ParamInt(0x1274))
    OP_3B(0x34, ParamInt(0x1275))

    Jump('loc_12ADE')

    def _loc_12A4D(): pass

    label('loc_12A4D')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x0D)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12AA6',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1274), ParamInt(0x1275), ParamInt(0), ParamInt(0))
    OP_3B(0x34, ParamInt(0x1274))
    OP_3B(0x34, ParamInt(0x1275))

    Jump('loc_12ADE')

    def _loc_12AA6(): pass

    label('loc_12AA6')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1274), ParamInt(0x1275), ParamInt(0), ParamInt(0))
    OP_3B(0x34, ParamInt(0x1274))
    OP_3B(0x34, ParamInt(0x1275))

    def _loc_12ADE(): pass

    label('loc_12ADE')

    Jump('loc_12B3C')

    def _loc_12AE7(): pass

    label('loc_12AE7')

    OP_3B(0x32, ParamInt(0x121A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12B3C(): pass

    label('loc_12B3C')

    Return()

# id: 0x0074 offset: 0x12B40
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12BB3',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12C17')

    def _loc_12BB3(): pass

    label('loc_12BB3')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12C17(): pass

    label('loc_12C17')

    Return()

# id: 0x0075 offset: 0x12C18
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    Call(ScriptId.Current, 'SpringOn')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0076 offset: 0x12C64
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')

    Return()

# id: 0x0077 offset: 0x12C7C
@scena.Code('AniBtlDead')
def AniBtlDead():
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, '9', '7', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12D7B',
    )

    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_12D52',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D52',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1276), ParamInt(0x1277), ParamInt(0), ParamInt(0))
    OP_3B(0x34, ParamInt(0x1276))
    OP_3B(0x34, ParamInt(0x1277))

    def _loc_12D52(): pass

    label('loc_12D52')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12D72',
    )

    Sleep(500)

    def _loc_12D72(): pass

    label('loc_12D72')

    Jump('loc_12E2A')

    def _loc_12D7B(): pass

    label('loc_12D7B')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_12DF6',
    )

    OP_3B(0x32, ParamInt(0x121B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x121B))

    def _loc_12DF6(): pass

    label('loc_12DF6')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12E2A(): pass

    label('loc_12E2A')

    Return()

# id: 0x0078 offset: 0x12E2C
@scena.Code('AniBtlAria')
def AniBtlAria():
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x1214), ParamInt(0x1215), ParamFloat(0.8), ParamFloat(0))

    Return()

# id: 0x0079 offset: 0x12E58
@scena.Code('AniBtlArts')
def AniBtlArts():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x4B, 0x00FA, 0x03)
    BattleTargetsIterReset(0x00, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12EBF',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)

    Jump('loc_12ED1')

    def _loc_12EBF(): pass

    label('loc_12EBF')

    BattleTurnChrDirection(0xFFFE, 0xFFF2, 0.0, 0.5)

    def _loc_12ED1(): pass

    label('loc_12ED1')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1216), ParamInt(0x1217), ParamInt(0), ParamInt(0))
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x007A offset: 0x13080
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
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1216), ParamInt(0x1217), ParamInt(0), ParamInt(0))
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x007B offset: 0x13240
@scena.Code('AniBtlChainBattleAppear')
def AniBtlChainBattleAppear():
    Return()

# id: 0x007C offset: 0x13244
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x1221), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007D offset: 0x1329C
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x1222), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007E offset: 0x132F4
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x1223), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007F offset: 0x1334C
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x122F), ParamInt(0x1230), ParamInt(0), ParamInt(0))

    Return()

# id: 0x0080 offset: 0x13370
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

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_3B(0x00, ParamInt(0xFFFF), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13556',
    )

    OP_3B(0x32, ParamInt(0x1240), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13699')

    def _loc_13556(): pass

    label('loc_13556')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_135CD',
    )

    OP_3B(0x32, ParamInt(0x1242), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13699')

    def _loc_135CD(): pass

    label('loc_135CD')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13644',
    )

    OP_3B(0x32, ParamInt(0x1240), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13699')

    def _loc_13644(): pass

    label('loc_13644')

    OP_3B(0x32, ParamInt(0x1231), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_13699(): pass

    label('loc_13699')

    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.019), ParamFloat(0.945), ParamFloat(0.422), -5.243, 33.689, 133.311, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10A7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    Sleep(100)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13988',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1056), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13B6A')

    def _loc_13988(): pass

    label('loc_13988')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13ADF',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.03, 0.03, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13B6A')

    def _loc_13ADF(): pass

    label('loc_13ADF')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_13B6A(): pass

    label('loc_13B6A')

    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(666)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)

    BattleCmd(0x3F, 0xFFFE)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x0081 offset: 0x13C58
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0082 offset: 0x13C9C
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0083 offset: 0x13CC4
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
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_3B(0x00, ParamInt(0xFFFF), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.019), ParamFloat(0.945), ParamFloat(0.422), -5.243, 33.689, 133.311, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10A7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1290), ParamInt(0), ParamInt(0), ParamInt(0))
    CameraCmd(0x0A, 0.0, 0.0025, 0.25, 0, 400, 0, 0, 0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_0', ScriptId.Current)
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0084 offset: 0x14058
@scena.Code('_Lambda_0')
def _Lambda_0():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FB), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x0085 offset: 0x140A8
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0086 offset: 0x140C0
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0087 offset: 0x140D8
@scena.Code('AniBtlLinkUltimateAttack')
def AniBtlLinkUltimateAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0088 offset: 0x140F0
@scena.Code('AniBtlLinkUtmostAttack')
def AniBtlLinkUtmostAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0089 offset: 0x14108
@scena.Code('AniBtlLinkLivelyYell')
def AniBtlLinkLivelyYell():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x1241), ParamStr('NODE_R_HAND'))

    Return()

# id: 0x008A offset: 0x14134
@scena.Code('AniBtlLinkLivelyYell2')
def AniBtlLinkLivelyYell2():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x1241), ParamStr('NODE_R_HAND'))

    Return()

# id: 0x008B offset: 0x14160
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x008C offset: 0x14180
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x008D offset: 0x1419C
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    SetChrFace(0x03, PseudoChrId.Self, '21112[autoE2]', '2[autoM2]', '0#36w3', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008E offset: 0x141FC
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_1426D',
    )

    OP_3B(0x32, ParamInt(0x1213), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_142C2')

    def _loc_1426D(): pass

    label('loc_1426D')

    OP_3B(0x32, ParamInt(0x1212), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_142C2(): pass

    label('loc_142C2')

    Return()

# id: 0x008F offset: 0x142C4
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0090 offset: 0x14330
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0091 offset: 0x14348
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x0092 offset: 0x1436C
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x0093 offset: 0x14370
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x0094 offset: 0x14390
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x1216), ParamInt(0x1217))

    Return()

# id: 0x0095 offset: 0x143BC
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x0096 offset: 0x143E0
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x0097 offset: 0x14400
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x0098 offset: 0x14420
@scena.Code('AniBtlKisinItemPa')
def AniBtlKisinItemPa():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1216), ParamInt(0x1217), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x0099 offset: 0x14484
@scena.Code('AniBtlKisinChargePa')
def AniBtlKisinChargePa():
    OP_3B(0x32, ParamInt(0x1279), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x009A offset: 0x1451C
@scena.Code('AniBtlKisinSinkiPa')
def AniBtlKisinSinkiPa():
    OP_3B(0x32, ParamInt(0x127A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x009B offset: 0x145B4
@scena.Code('AniBtlKisinPartnerArts')
def AniBtlKisinPartnerArts():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1216), ParamInt(0x1217), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x009C offset: 0x14618
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009D offset: 0x14654
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009E offset: 0x146B8
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x009F offset: 0x146F4
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A0 offset: 0x1472C
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
        'loc_1476B',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_147A5')

    def _loc_1476B(): pass

    label('loc_1476B')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_14798',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_147A5')

    def _loc_14798(): pass

    label('loc_14798')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_147A5(): pass

    label('loc_147A5')

    Return()

# id: 0x00A1 offset: 0x147A8
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14818',
    )

    OP_3B(0x32, ParamInt(0x122C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_148DD')

    def _loc_14818(): pass

    label('loc_14818')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14888',
    )

    OP_3B(0x32, ParamInt(0x122A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_148DD')

    def _loc_14888(): pass

    label('loc_14888')

    OP_3B(0x32, ParamInt(0x122B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_148DD(): pass

    label('loc_148DD')

    Return()

# id: 0x00A2 offset: 0x148E0
@scena.Code('AniBtlWin')
def AniBtlWin():
    CameraCmd(0x00)
    CameraCmd(0x20)
    CameraSetPos(0x03, 0.01, 0.79, 0.04, 0)
    CameraRotate(0x03, -3.21, -25.18, -0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.91, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    CameraSetPos(0x07, 0.02, 0.89, 0.04, 1110)
    CameraRotate(0x07, -2.97, -10.33, 0.0, 1110, 0x01)
    CameraSetDistance(0x07, 1.83, 1110)
    CameraSetPos(0x07, 0.02, 1.22, 0.04, 416)
    CameraRotate(0x07, -8.81, -1.83, 0.0, 416, 0x01)
    CameraSetDistance(0x07, 2.22, 500)
    CameraSetPos(0x07, 0.05, 1.22, 0.08, 1666)
    CameraRotate(0x07, -2.59, 17.63, -0.0, 1666, 0x01)
    CameraSetDistance(0x07, 2.41, 1666)
    CameraCmd(0x21, 0xFFFE, '')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14AE9',
    )

    SetChrFace(0x03, PseudoChrId.Self, '011110#86w0[autoE0]', '2[autoM2]', '002230712340000#55e3', '#b', '0')
    Call(ScriptId.Current, 'VoiceWin_play')

    Jump('loc_14B6A')

    def _loc_14AE9(): pass

    label('loc_14AE9')

    SetChrFace(0x03, PseudoChrId.Self, '#120s05#36w0#106w4445#96w4[autoE4]', '4[autoM4]', '#120s00122307812340#36w#55e333#100e3#96w0[autoB0]', '#b', '0')
    Call(ScriptId.Current, 'VoiceWin_play')

    def _loc_14B6A(): pass

    label('loc_14B6A')

    Sleep(425)

    OP_3B(0x00, ParamInt(0x178E), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(575)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14BE8',
    )

    Jump('loc_14BE8')

    def _loc_14BE8(): pass

    label('loc_14BE8')

    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    CameraCmd(0x0A, 0.0, 0.05, 0.0, 0, 100, 100, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x178F), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-6), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(366)

    OP_3B(0x00, ParamInt(0x1790), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x39, 0xFFFE)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.21, 1.07, 0.28, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.0, 17.87, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.1, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    Sleep(1000)

    Return()

# id: 0x00A3 offset: 0x14D80
@scena.Code('AniBtlWinHitouchdb')
def AniBtlWinHitouchdb():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB_a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A4 offset: 0x14DFC
@scena.Code('AniBtlWinHitouchdbb')
def AniBtlWinHitouchdbb():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB_b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00A5 offset: 0x14E60
@scena.Code('AniBtlWinHoldR')
def AniBtlWinHoldR():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLDa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A6 offset: 0x14ED0
@scena.Code('AniBtlWinPonpon')
def AniBtlWinPonpon():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_PONPON', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_PONPON_a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A7 offset: 0x14F48
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '#120s05#36w0#106w4445#96w4[autoE4]', '4[autoM4]', '#120s00122307812340#36w#55e333#100e3#96w0[autoB0]', '#b', '0')
    Sleep(425)

    OP_3B(0x00, ParamInt(0x178E), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(575)

    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    OP_3B(0x00, ParamInt(0x178F), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-6), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(366)

    OP_3B(0x00, ParamInt(0x1790), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A8 offset: 0x1519C
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    OP_3B(0x32, ParamInt(0x122D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '#120s05#36w0#106w4445#96w4[autoE4]', '4[autoM4]', '#120s00122307812340#36w#55e333#100e3#96w0[autoB0]', '#b', '0')
    Sleep(425)

    OP_3B(0x00, ParamInt(0x178E), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(575)

    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    OP_3B(0x00, ParamInt(0x178F), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-6), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(366)

    OP_3B(0x00, ParamInt(0x1790), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x00A9 offset: 0x15470
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AA offset: 0x154B0
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AB offset: 0x15510
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '2', '4[autoM4]', '', '#b', '0')
    OP_45(PseudoChrId.Self, -30.0, 0.0, 0.0, 0x012C, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'fold', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_3B(0x00, ParamInt(0x177F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 29)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x13)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x012C, 0x0000)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '1', '', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 71)
    StopEffect(0xFFFE, 0x13, 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '4', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x00AC offset: 0x15754
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00AD offset: 0x15778
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_157E5',
    )

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1583A')

    def _loc_157E5(): pass

    label('loc_157E5')

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1583A(): pass

    label('loc_1583A')

    Return()

# id: 0x00AE offset: 0x1583C
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
    Call(ScriptId.Current, 'DefaultFace')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_15987',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_159E9')

    def _loc_15987(): pass

    label('loc_15987')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_159E9(): pass

    label('loc_159E9')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5#56w4[autoE4]', '4[autoM4]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AF offset: 0x15A7C
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15AB1',
    )

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x1271))

    Jump('loc_15ACB')

    def _loc_15AB1(): pass

    label('loc_15AB1')

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x126F))

    def _loc_15ACB(): pass

    label('loc_15ACB')

    Return()

# id: 0x00B0 offset: 0x15ACC
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr113_00_00.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr113_00_01.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/gra00.eff', 0x00000000)
    OP_43(0x65, 350, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000180)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_1', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2233332[autoE2]', '0[autoM0]', '0[autoB0]', '223', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0C)
    EffectSetRGBA(0xFFFE, 0x0C, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0C, 0.0, 0.2, 0.5, 0.5, 500, 0x03)
    Sleep(333)

    OP_3B(0x32, ParamInt(0x1202), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 20)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000023, ParamStr(''), ParamFloat(0.046), ParamFloat(1.082), ParamFloat(0.087), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0064))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_43(0x65, 350, 1.0, 0)
    OP_43(0xFE, 0)
    StopEffect(0xFFFE, 0x02, 0x01)
    StopEffect(0xFFFE, 0x0C, 0x01)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', -0.0, 0.43, 0.0, 0)
    CameraRotateByTarget(0xFFFB, '', 0x03, 0.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.22, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x03, -1.0, 3000)
    BattleCmd(0x4B, 0x0BB8, 0x03)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Target, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0065))
    Sleep(2600)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_15FAF',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15FA6',
    )

    OP_3B(0x32, ParamInt(0x1282), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_15FA6(): pass

    label('loc_15FA6')

    Jump('loc_15FCF')

    def _loc_15FAF(): pass

    label('loc_15FAF')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1203), ParamInt(0x1204), ParamInt(0), ParamInt(0))

    def _loc_15FCF(): pass

    label('loc_15FCF')

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    CameraCmd(0x07, 0x00BF)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0066))
    BattleCmd(0x63, 0xFFFB)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000100)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    CameraCmd(0x17, 0x0040)

    Return()

# id: 0x00B1 offset: 0x16040
@scena.Code('_Lambda_1')
def _Lambda_1():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.97, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetDistance(0x03, 1.56, 500)
    BattleCmd(0x4B, 0x01F4, 0x03)
    Sleep(500)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.09, 0.05, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.82, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 0.89, 0)
    CameraCmd(0x0B, 0x03, 22.17, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x4B, 0x0341, 0x03)
    Sleep(833)

    Return()

# id: 0x00B2 offset: 0x1612C
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    LoadEffect(0xFFFE, 0x30, 'battle/cr113_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr113_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr113_01_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr113_01_3.eff', 0x00000000)
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_2', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x006E))
    OP_3B(0x32, ParamInt(0x1205), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 25)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.9), ParamFloat(0), 0.0, 0.0, 90.0, ParamFloat(0.25), ParamFloat(0.25), ParamFloat(0.25), 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    EffectSetRGBA(0xFFFE, 0x03, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 50)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    TerminateThread(PseudoChrId.Self, 0x02)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_3', ScriptId.Current)
    StopEffect(0xFFFE, 0x03, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 1.66667, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.969), ParamFloat(-0.262), 0.0, 0.0, 90.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(0.4), 0x04)
    EffectCmd(0x13, 0xFFFE, 0x04, 0x0064)
    WaitAnimeClipFrames(PseudoChrId.Self, 52)
    OP_3B(0x32, ParamInt(0x1206), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 55)
    CameraCmd(0x09, 0.125, 0.125, 1.0)
    OP_3B(0xFF, 0.6, 0.6, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    WaitAnimeClipFrames(PseudoChrId.Self, 64)
    TerminateThread(PseudoChrId.Self, 0x02)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 1.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x03E8, 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 73)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_4', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x02, 1.0, 1000)
    BattleCmd(0x4B, 0x0000, 0x02)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_04(0x0B, 'AniBtlCraft01_finish')

    Return()

# id: 0x00B3 offset: 0x166A0
@scena.Code('_Lambda_2')
def _Lambda_2():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 0.97, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -3.95, 36.23, -0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.72, 0.08, 367)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.5, 37.67, 0.0, 367, 0x01)
    CameraSetDistance(0x03, 2.28, 367)
    BattleCmd(0x4B, 0x016F, 0x03)
    Sleep(366)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 1.72, 0.08, 533)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.84, 38.34, 0.0, 533, 0x01)
    CameraSetDistance(0x03, 2.12, 533)
    BattleCmd(0x4B, 0x0215, 0x03)
    Sleep(533)

    Return()

# id: 0x00B4 offset: 0x16794
@scena.Code('_Lambda_3')
def _Lambda_3():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.75, 1.17, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -3.22, 149.34, -0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.81, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.75, 1.52, 300)
    CameraRotateByTarget(0xFFFE, '', 0x03, 9.51, 138.83, -0.0, 300, 0x01)
    CameraSetDistance(0x03, 4.29, 300)
    BattleCmd(0x4B, 0x012C, 0x03)
    Sleep(300)

    Return()

# id: 0x00B5 offset: 0x1682C
@scena.Code('_Lambda_4')
def _Lambda_4():
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_16835(): pass

    label('loc_16835')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_168D9',
    )

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(100)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_16835')

    def _loc_168D9(): pass

    label('loc_168D9')

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_16943',
    )

    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16943(): pass

    label('loc_16943')

    Return()

# id: 0x00B6 offset: 0x16944
@scena.Code('AniBtlCraft01_finish')
def AniBtlCraft01_finish():
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00B7 offset: 0x169A4
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    LoadEffect(0xFFFE, 0x30, 'battle/cr113_02_0.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_16A99',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.75), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x03E8)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0[autoM0]', '0[autoB0]', '#b', '0')

    Jump('loc_16D46')

    def _loc_16A99(): pass

    label('loc_16A99')

    OP_4A(0x00, 0.2, 0.2, 0.2, 1.0, 300, 0x03)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_5', ScriptId.Current)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2#36w3', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 5)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_16BD1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16BC8',
    )

    OP_3B(0x32, ParamInt(0x1282), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16BC8(): pass

    label('loc_16BC8')

    Jump('loc_16C26')

    def _loc_16BD1(): pass

    label('loc_16BD1')

    OP_3B(0x32, ParamInt(0x1207), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16C26(): pass

    label('loc_16C26')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.75), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_5E(0x00, 0x0003, 0.6, 100, 100, 500, 0.1, 0xFFFE, '', 0.0, 0.75, 0.0)
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 0, 100, 100, 0, 0, 0x00)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0078))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_5E(0x01, 0x0000)
    TerminateThread(PseudoChrId.Self, 0x02)
    OP_4A(0x00, 1.0, 1.0, 1.0, 1.0, 300, 0x03)

    def _loc_16D46(): pass

    label('loc_16D46')

    Return()

# id: 0x00B8 offset: 0x16D48
@scena.Code('_Lambda_5')
def _Lambda_5():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.96, 0.38, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -6.11, 0.59, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.1, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.96, 0.34, 167)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.9, 0.0, 0.0, 167, 0x01)
    CameraSetDistance(0x03, 1.14, 167)
    BattleCmd(0x4B, 0x00A7, 0x03)
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.96, 0.3, 167)
    CameraRotateByTarget(0xFFFE, '', 0x03, -6.21, 0.0, 0.0, 167, 0x01)
    CameraSetDistance(0x03, 1.08, 167)
    BattleCmd(0x4B, 0x00A7, 0x03)
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.96, 0.21, 667)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.76, 0.0, 0.0, 667, 0x01)
    CameraSetDistance(0x03, 1.17, 667)
    BattleCmd(0x4B, 0x029B, 0x03)
    Sleep(666)

    Return()

# id: 0x00B9 offset: 0x16E88
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    LoadEffect(0xFFFE, 0x31, 'battle/cr113_02_1.eff', 0x00000000)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_6', ScriptId.Current)
    CreateThread(PseudoChrId.Self, 0x03, '_Lambda_7', ScriptId.Current)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.75), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3#196w2[autoE2]', '1#146w2[autoM2]', '0[autoB0]', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 3)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_17059',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x134),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17050',
    )

    OP_3B(0x32, ParamInt(0x1284), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_17050(): pass

    label('loc_17050')

    Jump('loc_170AE')

    def _loc_17059(): pass

    label('loc_17059')

    OP_3B(0x32, ParamInt(0x1208), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_170AE(): pass

    label('loc_170AE')

    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0079))
    WaitAnimeClipFrames(PseudoChrId.Self, 30)
    WaitAnimeClipFrames(PseudoChrId.Self, 50)
    WaitAnimeClipFrames(PseudoChrId.Self, 65)
    WaitAnimeClipFrames(PseudoChrId.Self, 70)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '27', '0[autoB0]', '#b', '0')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    TerminateThread(PseudoChrId.Self, 0x03)
    CameraCmd(0x0A, 0.05, 0.05, 0.0, 100, 1500, 1000, 0, 0, 0x00)
    OP_5E(0x00, 0x0003, 0.8, 0, 500, 500, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(666)

    OP_43(0x03, 333, 1.0, 0)
    Sleep(666)

    OP_43(0x67, 1000, 1.0, 0)
    TerminateThread(PseudoChrId.Self, 0x02)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00BA offset: 0x17238
@scena.Code('_Lambda_6')
def _Lambda_6():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.12, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -12.19, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.06, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -10.61, 0.0, 0.0, 2333, 0x01)
    CameraSetDistance(0x03, 2.37, 2333)
    Sleep(2333)

    CameraRotateByTarget(0xFFFE, '', 0x03, -11.97, 0.0, 0.0, 333, 0x01)
    CameraSetDistance(0x03, 2.1, 333)
    Sleep(333)

    Sleep(666)

    Return()

# id: 0x00BB offset: 0x172E8
@scena.Code('_Lambda_7')
def _Lambda_7():
    Sleep(333)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(466)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(400)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(333)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(266)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(200)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(100)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(100)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(100)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(100)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(166)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')
    Sleep(166)

    Call(ScriptId.Current, 'AniBtlCraft02_Heartbeat')

    Return()

# id: 0x00BC offset: 0x174B4
@scena.Code('AniBtlCraft02_Heartbeat')
def AniBtlCraft02_Heartbeat():
    OP_5E(0x00, 0x0003, 0.6, 100, 33, 100, 0.15, 0xFFFE, '', 0.0, 0.75, 0.0)
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 0, 100, 100, 0, 0, 0x00)

    Return()

# id: 0x00BD offset: 0x174F8
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr113_03_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr113_03_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr113_03_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr113_03_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/disarm113.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Call(ScriptId.BtlCom, 'SET_MOVE_SPEED', ParamFloat(9))
    BattleCreateChrDummy(0xFFFE, 0x00000001)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000180)
    OP_3B(0x32, ParamInt(0x1209), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_8', ScriptId.Current)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0082))
    SetChrAniFunction(PseudoChrId.Self, 0x01, 'AniEvCraft03_00', 0.0, 1.0, 0x00000008)
    SetChrFace(0x03, PseudoChrId.Self, '1110#116w5', '4[autoM4]', '0#46w#45e5#56w#100e0[autoB0]', '1110[autoE0]', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 50)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    Sleep(1000)

    TerminateThread(PseudoChrId.Self, 0x02)
    BattleCmd(0x47)
    CameraCmd(0x00)
    OP_3B(0x32, ParamInt(0x120A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_9', ScriptId.Current)
    EffectSetRGBA(0xFFFE, 0x02, 1.0, 1.0, 1.0, 0.0, 500, 0x00)
    SetChrAniFunction(PseudoChrId.Self, 0x01, 'AniEvCraft03_01', 0.0, 1.0, 0x00000000)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '006#96w0[autoB0]', '#b', '0')
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0083))
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '4[autoM4]', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.122), ParamFloat(0.717), ParamFloat(0.242), -18.001, -10.001, 4.469, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0084))
    OP_3B(0x32, ParamInt(0x120B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 50)
    Sleep(333)

    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.91, 0.87, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.43, 137.4, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.29, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.75, 6.0, 15.0)
    BattleCmd(0x4B, 0x0001, 0x03)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(0.242), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFF3, 0.0, 0.0)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    BattleSetChrPosAsync(0x0B86, 0xFFF3, 0.0, 0.0, 0.0, 0.76, 0x02, 0x10)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_17B9B(): pass

    label('loc_17B9B')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_17C43',
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0xDAC),
            Expr.Gtr,
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17BD1',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17BD1(): pass

    label('loc_17BD1')

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x1B58),
            Expr.Gtr,
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17BFB',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17BFB(): pass

    label('loc_17BFB')

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x2904),
            Expr.Gtr,
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17C25',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17C25(): pass

    label('loc_17C25')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_17B9B')

    def _loc_17C43(): pass

    label('loc_17C43')

    Switch(
        (
            (Expr.PushReg, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_17C70'),
        (0x00000001, 'loc_17CC0'),
        (0x00000002, 'loc_17D10'),
        (0x00000003, 'loc_17D60'),
        (-1, 'loc_17DB0'),
    )

    def _loc_17C70(): pass

    label('loc_17C70')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)

    Jump('loc_17DB0')

    def _loc_17CC0(): pass

    label('loc_17CC0')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x04)

    Jump('loc_17DB0')

    def _loc_17D10(): pass

    label('loc_17D10')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(4), ParamFloat(4), ParamFloat(4), 0x04)

    Jump('loc_17DB0')

    def _loc_17D60(): pass

    label('loc_17D60')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.717), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(8), ParamFloat(8), ParamFloat(8), 0x04)

    Jump('loc_17DB0')

    def _loc_17DB0(): pass

    label('loc_17DB0')

    SetChrAniFunction(PseudoChrId.Self, 0x01, 'AniEvCraft03_02', 0.0, 1.0, 0x00000000)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '7', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.6, 0.6, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    CameraSetDistance(0x03, 4.2, 300)
    Sleep(2333)

    OP_04(0x0B, 'AniBtlCraft03_finish')

    Return()

# id: 0x00BE offset: 0x17ED0
@scena.Code('_Lambda_8')
def _Lambda_8():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.85, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.71, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.38, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.89, 0.0, 0.0, 2500, 0x01)
    CameraSetDistance(0x03, 1.1, 2500)
    BattleCmd(0x4B, 0x09C4, 0x03)
    Sleep(2500)

    Return()

# id: 0x00BF offset: 0x17F5C
@scena.Code('_Lambda_9')
def _Lambda_9():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.01, 0.88, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.57, 0.78, -0.0, 0, 0x01)
    CameraSetDistance(0x03, 0.7, 0)
    CameraCmd(0x0B, 0x03, 42.7991, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x4B, 0x04F3, 0x03)
    Sleep(1266)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.64, 0.91, 0.08, 733)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.57, 17.92, 0.0, 733, 0x01)
    CameraSetDistance(0x03, 2.1, 733)
    BattleCmd(0x4B, 0x02DD, 0x03)
    Sleep(733)

    Return()

# id: 0x00C0 offset: 0x18010
@scena.Code('AniBtlCraft03_finish')
def AniBtlCraft03_finish():
    TerminateThread(PseudoChrId.Self, 0x02)
    TerminateThread(PseudoChrId.Self, 0x01)
    Call(ScriptId.Current, 'SpringOn')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000180)
    ReleaseEffect(0xFFFE, 0x30)
    BattleDeleteChrDummy()
    Call(ScriptId.BtlCom, 'RESET_MOVE_SPEED')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU610_C00')
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C1 offset: 0x18114
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    BattleCmd(0x52, 0xFFFE, 0x3F)
    LoadEffect(0xFFFE, 0x30, 'battle/sc113_00_00.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/sc113_00_01.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc113_00_02.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc113_00_03.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc113_00_04.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc113_00_05.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc113_00_06.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc113_00_07.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc113_00_08.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc113_00_09.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc113_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc113_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc113_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc113_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc113_00_20.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleCreateChrDummy(0xFFFE, 0x00000001)
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR113_SC1')
    AnimeClipAddAsset(0x0B86, 'C_CHR113_SC1')
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0001, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0002, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0003, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0004, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0005, 0xFFFF, 'C_CHRX10', '')
    BattleCreateTempChar(0x0006, 0xFFFF, 'C_CHRX10', '')
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0x0B86, 0x000002E0)
    ChrSetPhysicsFlags(0x0B68, 0x000002E0)
    ChrSetPhysicsFlags(0x0B69, 0x000002E0)
    ChrSetPhysicsFlags(0x0B6A, 0x000002E0)
    ChrSetPhysicsFlags(0x0B6B, 0x000002E0)
    ChrSetPhysicsFlags(0x0B6C, 0x000002E0)
    ChrSetPhysicsFlags(0x0B6D, 0x000002E0)
    ChrSetPhysicsFlags(0x0B6E, 0x000002E0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002E0)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -50.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_18569',
    )

    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)

    Jump('loc_18585')

    def _loc_18569(): pass

    label('loc_18569')

    BattleSetChrPos(0xFFFB, 0xFFFF, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)

    def _loc_18585(): pass

    label('loc_18585')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_185C8',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFEA, -1.0, 0.5)
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

    Jump('loc_18585')

    def _loc_185C8(): pass

    label('loc_185C8')

    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'disable', 'disable', 'disable', '#b', '0')
    OP_CE(0x0005, 0xFFFE, 'BTL_S_CRAFT00_00_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_CE(0x0004, 0xFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0028, 'gamePos2', 0x00)
    OP_CE(0x0028, 'gamePos3', 0x00)
    OP_CE(0x0028, 'gamePos4', 0x00)
    OP_CE(0x0028, 'gamePos5', 0x00)
    OP_CE(0x0028, 'gamePos6', 0x00)
    OP_CE(0x0028, 'gamePos7', 0x00)
    OP_CE(0x0028, 'gamePos8', 0x00)
    OP_CE(0x0028, 'gamePos9', 0x00)
    OP_43(0x64, 800, 1.0, 0)
    OP_C0(0x0001, 0x3FD33333)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(400))
    Call(ScriptId.Current, 'EraseEquip')
    OP_4E(0.7, 0.0, 0x03, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_00_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Sleep(166)

    OP_4E(1.0, 0.0, 0x03, 0x01)
    Sleep(133)

    OP_3B(0x32, ParamInt(0x120C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    Sleep(200)

    OP_5E(0x00, 0x0000, 0.5, 10, 100, 150, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(233)

    OP_5E(0x00, 0x0000, 0.5, 10, 100, 150, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    EffectSetRGBA(0xFFFE, 0x02, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Sleep(33)

    CameraCmd(0x0A, 0.05, 0.03, 0.0, 10, 50, 200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 500, 170, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.3, 0.2, 0.3)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    Sleep(500)

    OP_3B(0x32, ParamInt(0x129A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    EffectSetRGBA(0xFFFE, 0x02, 1.0, 1.0, 1.0, 1.0, 1200, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.0, 0.0, 0.0, 0.0, 1200, 0x03)
    OP_CE(0x0003, 0x00)
    OP_4E(0.8, 0.0, 0x03, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(1.5), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    Sleep(333)

    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3E99999A, 0x00000000, 0x03, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 300, 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 20)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F99999A, 0x00000000, 0x03, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    Sleep(130)

    OP_5E(0x00, 0x0002, 0.65, 10, 700, 300, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0035, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0036, 0x01)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_CE(0x0015, 0xFFFE, 0x00000000, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(0x0B69, 0x00000040)
    ChrClearPhysicsFlags(0x0B6A, 0x00000040)
    ChrClearPhysicsFlags(0x0B6B, 0x00000040)
    ChrClearPhysicsFlags(0x0B6C, 0x00000040)
    ChrClearPhysicsFlags(0x0B6D, 0x00000040)
    ChrClearPhysicsFlags(0x0B6E, 0x00000040)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B68, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B69, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B6A, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B6B, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B6C, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B6D, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B6E, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    OP_CE(0x000B, 0x00000000, 0x00)
    CameraRotate(0x03, 25.0, 200.0, 0.0, 0, 0x01)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFF, 0.0, 1.0)
    BattleTargetsIterInit(0x05)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0x0B86, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, 0.1, 0.0, 0x00, 0x01)
    BattleSetChrPos(0x0B68, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B68, 0xFFFF, 45.0, -1.0)
    BattleTurnChrDirection(0x0B69, 0xFFFF, 80.0, -1.0)
    BattleTurnChrDirection(0x0B6A, 0xFFFF, 132.0, -1.0)
    BattleTurnChrDirection(0x0B6B, 0xFFFF, 166.0, -1.0)
    BattleTurnChrDirection(0x0B6C, 0xFFFF, 219.0, -1.0)
    BattleTurnChrDirection(0x0B6D, 0xFFFF, 251.0, -1.0)
    BattleTurnChrDirection(0x0B6E, 0xFFFF, 307.0, -1.0)

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 3.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19241',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -3.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -3.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -3.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -3.15, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -3.45, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -3.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -3.15, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -3.6, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19241(): pass

    label('loc_19241')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 4.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1934A',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -4.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -4.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -4.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -4.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -4.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -4.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -4.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -4.8, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1934A(): pass

    label('loc_1934A')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 5.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19453',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -5.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -6.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -5.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -5.25, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -5.75, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -5.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -5.25, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -6.0, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19453(): pass

    label('loc_19453')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 6.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1955C',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -6.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -7.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -6.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -6.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -6.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -6.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -6.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -7.2, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1955C(): pass

    label('loc_1955C')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 7.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19665',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -7.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -8.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -7.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -7.35, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -8.05, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -7.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -7.35, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -8.4, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19665(): pass

    label('loc_19665')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 8.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1976E',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -8.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -9.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -8.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -8.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -9.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -8.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -8.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -9.6, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1976E(): pass

    label('loc_1976E')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 9.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19877',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -9.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -10.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -9.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -9.45, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -10.35, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -9.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -9.45, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -10.8, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19877(): pass

    label('loc_19877')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 10.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19980',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -10.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -12.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -11.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -10.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -11.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -11.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -10.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -12.0, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19980(): pass

    label('loc_19980')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 11.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A89',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -11.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -13.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -12.1, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -11.55, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -12.65, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -12.1, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -11.55, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -13.2, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19A89(): pass

    label('loc_19A89')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 12.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19B92',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -12.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -14.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -13.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -12.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -13.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -13.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -12.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -14.4, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19B92(): pass

    label('loc_19B92')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 13.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19C9B',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -13.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -15.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -14.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -13.65, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -14.95, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -14.3, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -13.65, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -15.6, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19C9B(): pass

    label('loc_19C9B')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 14.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19DA4',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -14.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -16.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -15.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -14.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -16.1, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -15.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -14.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -16.8, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19DA4(): pass

    label('loc_19DA4')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 15.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19EAD',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -15.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -18.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -16.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -15.75, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -17.25, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -16.5, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -15.75, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -18.0, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19EAD(): pass

    label('loc_19EAD')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 16.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19FB6',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -16.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B68, 0.0, 0.0, -19.2, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B69, 0.0, 0.0, -17.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6A, 0.0, 0.0, -16.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6B, 0.0, 0.0, -18.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6C, 0.0, 0.0, -17.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6D, 0.0, 0.0, -16.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6F, 0x0B6E, 0.0, 0.0, -19.2, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_19FB6(): pass

    label('loc_19FB6')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 17.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A0BF',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -17.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -20.4, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -18.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -17.85, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -19.55, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -18.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -17.85, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -20.4, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1A0BF(): pass

    label('loc_1A0BF')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 18.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A1C8',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -18.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -21.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -19.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -18.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -20.7, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -19.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -18.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -21.6, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1A1C8(): pass

    label('loc_1A1C8')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B86, 19.0, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A2D1',
    )

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -19.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -22.8, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -20.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -19.95, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -21.85, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -20.9, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -19.95, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -22.8, -1.0, 0x00, 0x00)

    Jump('loc_1A3B1')

    def _loc_1A2D1(): pass

    label('loc_1A2D1')

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -20.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 0.0, -24.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 0.0, -22.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, -21.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, -23.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 0.0, -22.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 0.0, -21.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 0.0, -24.0, -1.0, 0x00, 0x00)

    def _loc_1A3B1(): pass

    label('loc_1A3B1')

    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0x0B68, 0x0001)
    BattleCmd(0x48, 0x0B69, 0x0001)
    BattleCmd(0x48, 0x0B6A, 0x0001)
    BattleCmd(0x48, 0x0B6B, 0x0001)
    BattleCmd(0x48, 0x0B6C, 0x0001)
    BattleCmd(0x48, 0x0B6D, 0x0001)
    BattleCmd(0x48, 0x0B6E, 0x0001)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 4.0, 0.0, 0)
    CameraSetHeight(0x03, 5.0, 0)
    CameraSetHeight(0x03, 1.0, 1500)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 4.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B68, 0x0B68, 0.0, 4.2, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B69, 0x0B69, 0.0, 4.4, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 4.1, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 4.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6C, 0x0B6C, 0.0, 4.1, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6D, 0x0B6D, 0.0, 4.3, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6E, 0x0B6E, 0.0, 4.2, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, -4.0, 0.0, 0.3, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B68, 0x0B68, 0.0, -4.0, 0.0, 0.4, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B69, 0x0B69, 0.0, -4.0, 0.0, 0.2, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B6A, 0x0B6A, 0.0, -4.0, 0.0, 0.35, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B6B, 0x0B6B, 0.0, -4.0, 0.0, 0.6, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B6C, 0x0B6C, 0.0, -4.0, 0.0, 0.25, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B6D, 0x0B6D, 0.0, -4.0, 0.0, 0.5, 0x02, 0x00)
    BattleSetChrPosAsync(0x0B6E, 0x0B6E, 0.0, -4.0, 0.0, 0.45, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B69, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B6A, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B6B, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B6C, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B6D, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B6E, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x09)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    EffectSetRGBA(0xFFFE, 0x02, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x03, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x03, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x04, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x04, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x05, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x05, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x06, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x06, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x07, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x07, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x08, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x08, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x09, 0.8, 1.0, 0.2, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x09, 1.0, 0.0, 0.8, 1.0, 0, 0x03)
    Sleep(33)

    CameraCmd(0x11, 0x03, 0.0, 15.0, 0.0, 0x0898, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B69, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6A, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6B, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6C, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6D, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6E, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x03, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x04, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x05, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x06, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x07, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x08, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x09, 0.9, 0.8, 0.5, 1.0, 500, 0x03)
    CameraCmd(0x0C, 0x03, 0.0, -3.0, 0.0, 1500)
    Sleep(500)

    EffectSetRGBA(0xFFFE, 0x02, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x03, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x03, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x04, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x04, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x05, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x05, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x06, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x06, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x07, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x07, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x08, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x08, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    EffectSetRGBA(0xFFFE, 0x09, 1.0, 1.0, 1.0, 1.0, 1100, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x09, 0.0, 0.0, 0.0, 0.0, 1100, 0x03)
    Sleep(800)

    OP_4E(0.8, 0.0, 0x03, 0x01)
    Sleep(200)

    Sleep(600)

    BattleCmd(0x47)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0032, 0x01)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_5E(0x00, 0x0002, 0.55, 10, 300, 200, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x03)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_CE(0x0014, 0x0B86, 'gamePos1', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 400, 0x03)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 400, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    OP_38(0x0B86, 0x00, 0x00, 'AniDetachMainWeapon')
    OP_CE(0x0002, 'BTL_S_CRAFT00_04_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT00_04_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT00_04_1_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Sleep(500)

    OP_3B(0x32, ParamInt(0x120D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    OP_63(0xFFFE, 0x00)
    Sleep(333)

    OP_63(0xFFFE, 0x00)
    OP_CE(0x0003, 0x00)
    OP_63(0xFFFE, 0x00)
    TerminateThread(0x0B86, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    ReleaseEffect(0xFFFE, 0x36)
    LoadEffect(0xFFFE, 0x36, 'battle/sc113_00_16.eff', 0x00000000)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    OP_CE(0x0002, 'BTL_S_CRAFT00_05_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Sleep(0)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    If(
        (
            (Expr.Eval, "BattleCmd(0x55, 0xFFFB)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B472',
    )

    BattleCmd(0x54, 0xFFFB, 0x01, 1.4, 2.3, -1.0)

    Jump('loc_1B4A3')

    def _loc_1B472(): pass

    label('loc_1B472')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Target, 'C_MON470')"),
            Expr.Return,
        ),
        'loc_1B4A3',
    )

    BattleCmd(0x54, 0xFFFB, 0x01, 0.5, 1.0, -1.0)

    def _loc_1B4A3(): pass

    label('loc_1B4A3')

    BattleSetChrPos(0xFFFB, 0xFFFE, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, -1.0)
    BattleSetChrPos(0xFFFB, 0xFFFE, 0.0, 0.0, -1.0, 0.0, 0x00, 0x00)
    Sleep(166)

    OP_3B(0x32, ParamInt(0x1210), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(533)

    Sleep(566)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.25, 0.3, 0.2)
    OP_5E(0x00, 0x0000, 0.5, 10, 700, 150, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(733)

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    WaitAnimeClipFrames(PseudoChrId.Self, 65)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    OP_CE(0x000B, 0x00000000, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, 'NODE_HEAD', 0.0, 0.0, 0.0, 700)
    CameraSetHeight(0x03, -1.0, 700)
    BattleTurnChrDirection(0xFFFB, 0xFFFF, -90.0, 0.0)
    BattleTurnChrDirection(0xFFFB, 0xFFFF, -180.0, 2.0)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_HEAD'), ParamFloat(-0.26), ParamFloat(0.22), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.14, 0.3, 1.0)
    CameraCmd(0x0A, 0.1, 0.06, 0.1, 0, 100, 200, 0, 0, 0x00)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    OP_CE(0x000A, 'gameCamera', 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x02)
    OP_5E(0x00, 0x0002, 0.55, 10, 400, 200, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1BA36(): pass

    label('loc_1BA36')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1BAC3',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x55, 0xFFFB)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BA74',
    )

    BattleCmd(0x54, 0xFFFB, 0x01, 1.4, 2.3, -1.0)

    Jump('loc_1BAA5')

    def _loc_1BA74(): pass

    label('loc_1BA74')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Target, 'C_MON470')"),
            Expr.Return,
        ),
        'loc_1BAA5',
    )

    BattleCmd(0x54, 0xFFFB, 0x01, 0.5, 1.0, -1.0)

    def _loc_1BAA5(): pass

    label('loc_1BAA5')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1BA36')

    def _loc_1BAC3(): pass

    label('loc_1BAC3')

    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'ShowEquip')
    OP_CE(0x0002, 'BTL_S_CRAFT00_06_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    OP_CE(0x0014, 0x0B68, 'gamePos4', 0x00)
    OP_CE(0x0014, 0x0B69, 'gamePos5', 0x00)
    OP_CE(0x0014, 0x0B6A, 'gamePos3', 0x00)
    OP_CE(0x0014, 0x0B6B, 'gamePos6', 0x00)
    OP_CE(0x0014, 0x0B6C, 'gamePos2', 0x00)
    OP_CE(0x0014, 0x0B6D, 'gamePos9', 0x00)
    Sleep(0)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BC9A',
    )

    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    BattleSetChrPos(0xFFFB, 0x0B68, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFB, 0xFFFB, 0.0, 0.0, -2.5, 0.0, 0x00, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_1BC9A(): pass

    label('loc_1BC9A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BD17',
    )

    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    BattleSetChrPos(0xFFFB, 0x0B69, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFB, 0xFFFB, 0.0, 0.0, -2.5, 0.0, 0x00, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_1BD17(): pass

    label('loc_1BD17')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BD94',
    )

    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    BattleSetChrPos(0xFFFB, 0x0B6A, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFB, 0xFFFB, 0.0, 0.0, -2.5, 0.0, 0x00, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_1BD94(): pass

    label('loc_1BD94')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BE11',
    )

    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    BattleSetChrPos(0xFFFB, 0x0B6B, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFB, 0xFFFB, 0.0, 0.0, -2.5, 0.0, 0x00, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_1BE11(): pass

    label('loc_1BE11')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1BE8E',
    )

    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    BattleSetChrPos(0xFFFB, 0x0B6C, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFB, 0xFFFB, 0.0, 0.0, -2.5, 0.0, 0x00, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    def _loc_1BE8E(): pass

    label('loc_1BE8E')

    Sleep(666)

    OP_4E(0.5, 0.0, 0x03, 0x01)
    Sleep(700)

    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_5E(0x00, 0x0002, 0.55, 10, 300, 200, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0002, 'BTL_S_CRAFT00_07_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x32, ParamInt(0x1211), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_4E(0.7, 0.0, 0x03, 0x01)
    Sleep(400)

    OP_4E(0.35, 0.0, 0x03, 0x01)
    Sleep(233)

    OP_3B(0xFF, 0.25, 0.3, 0.2)
    OP_5E(0x00, 0x0000, 0.25, 10, 100, 0, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(1900)

    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    LoadEffect(0xFFFE, 0x34, 'battle/sc113_00_14.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc113_00_15.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x0A)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x0B)
    OP_CE(0x0002, 'BTL_S_CRAFT00_08_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3E99999A, 0x00000000, 0x03, 0x00)
    OP_3B(0xFF, 0.3, 0.2, 0.6)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(666)

    OP_3B(0x32, ParamInt(0x129B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    EffectCmd(0x0F, 0xFFFE, 0x0035, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x003C, 0x01)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_4E(1.2, 0.0, 0x03, 0x01)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    OP_CE(0x0002, 'BTL_S_CRAFT00_09_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09_0_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(333)

    OP_84(0x00, -0.85, -0.85, -0.85, 1.0)
    OP_84(0x01, 0.75, 0.75, 0.75, 0.0)
    OP_4E(0.15, 0.0, 0x03, 0x00)
    OP_3B(0xFF, 0.4, 1.3, 0.3)
    Sleep(66)

    OP_84(0x02, 0.0, 0.0, 0.0, 0.0)
    OP_4E(1.0, 0.0, 0x03, 0x00)
    Sleep(266)

    Sleep(666)

    OP_4E(1.2, 0.0, 0x03, 0x01)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F19999A, 0x00000000, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x04, 0x00)
    OP_3B(0xFF, 0.4, 0.7, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x0B, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x0A, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x09, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x08, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x07, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x06, 0x00)
    OP_3B(0xFF, 0.3, 0.5, 0.4)
    CameraCmd(0x0A, 0.014, 0.014, 0.008, 100, 200, 100, 0, 60, 0x00)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    EffectCmd(0x0E, 0xFFFE, 0x05, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 1.0)
    CameraCmd(0x0A, 0.6, 0.5, 0.03, 30, 400, 300, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.2, 30, 300, 300, 0.4, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(800)

    OP_43(0x03, 1200, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    Sleep(666)

    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    OP_04(0x0B, 'AniBtlSCraft00_Finish')

    Return()

# id: 0x00C2 offset: 0x1CC6C
@scena.Code('AniBtlSCraft00_Finish')
def AniBtlSCraft00_Finish():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1CCB5(): pass

    label('loc_1CCB5')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1CCF4',
    )

    BattleCmd(0x54, 0xFFFB, 0x01, -1.0, -1.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1CCB5')

    def _loc_1CCF4(): pass

    label('loc_1CCF4')

    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR113_SC1')
    BattleDeleteChrDummy()
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    BattleDeleteTempChar(0xFFFF)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    OP_CE(0x0001, 0x00000000, 0x00)
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00C3 offset: 0x1CDF8
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00C4 offset: 0x1CE48
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C5 offset: 0x1CE78
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C6 offset: 0x1CEA8
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C7 offset: 0x1CED8
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C8 offset: 0x1CF18
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
        'loc_1CFA7',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1D080')

    def _loc_1CFA7(): pass

    label('loc_1CFA7')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1D022',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_1D080')

    def _loc_1D022(): pass

    label('loc_1D022')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1D080(): pass

    label('loc_1D080')

    Return()

# id: 0x00C9 offset: 0x1D084
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CA offset: 0x1D0C0
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CB offset: 0x1D11C
@scena.Code('AniEvIdle')
def AniEvIdle():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CC offset: 0x1D17C
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CD offset: 0x1D1C4
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x1D1F8
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CF offset: 0x1D23C
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x1D270
@scena.Code('AniEvFieldAttack')
def AniEvFieldAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D1 offset: 0x1D2CC
@scena.Code('AniEvFieldAttack2')
def AniEvFieldAttack2():
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D2 offset: 0x1D328
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D3 offset: 0x1D394
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'fold', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(33)

    OP_3B(0x00, ParamInt(0x177F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 35)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x13)
    WaitAnimeClipFrames(PseudoChrId.Self, 46)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClipFrames(PseudoChrId.Self, 77)
    StopEffect(0xFFFE, 0x13, 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D4 offset: 0x1D55C
@scena.Code('AniEvFieldAttackEndShort')
def AniEvFieldAttackEndShort():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_SHORT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(466)

    OP_3B(0x00, ParamInt(0x7537), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(366)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D5 offset: 0x1D650
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D6 offset: 0x1D6BC
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D7 offset: 0x1D72C
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D8 offset: 0x1D760
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x1D7C8
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DA offset: 0x1D834
@scena.Code('AniEvDead')
def AniEvDead():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DB offset: 0x1D89C
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DC offset: 0x1D8E4
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DD offset: 0x1D94C
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x1D9B8
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x1D9EC
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E0 offset: 0x1DA54
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E1 offset: 0x1DAB8
@scena.Code('AniEvHorseWait')
def AniEvHorseWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E2 offset: 0x1DAEC
@scena.Code('AniEvHorseWalk')
def AniEvHorseWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E3 offset: 0x1DB24
@scena.Code('AniEvHorseRun')
def AniEvHorseRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E4 offset: 0x1DB5C
@scena.Code('AniEvHorseStop')
def AniEvHorseStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E5 offset: 0x1DBB8
@scena.Code('AniEvHorseTurnRight')
def AniEvHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E6 offset: 0x1DC14
@scena.Code('AniEvHorseTurnLeft')
def AniEvHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E7 offset: 0x1DC70
@scena.Code('AniEvHorseDash')
def AniEvHorseDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x1DCA8
@scena.Code('AniEvHorseRearWait')
def AniEvHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E9 offset: 0x1DCE0
@scena.Code('AniEvHorseRearWalk')
def AniEvHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EA offset: 0x1DD1C
@scena.Code('AniEvHorseRearRun')
def AniEvHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EB offset: 0x1DD58
@scena.Code('AniEvHorseRearStop')
def AniEvHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EC offset: 0x1DDBC
@scena.Code('AniEvHorseRearTurnRight')
def AniEvHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00ED offset: 0x1DE24
@scena.Code('AniEvHorseRearTurnLeft')
def AniEvHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EE offset: 0x1DE8C
@scena.Code('AniEvHorseRearDash')
def AniEvHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x1DEC8
@scena.Code('AniEvCraft00_00')
def AniEvCraft00_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x1DF3C
@scena.Code('AniEvCraft01_00')
def AniEvCraft01_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x1DFB0
@scena.Code('AniEvCraft02_00')
def AniEvCraft02_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F2 offset: 0x1E024
@scena.Code('AniEvCraft02_01')
def AniEvCraft02_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x1E098
@scena.Code('AniEvCraft03_00')
def AniEvCraft03_00():
    LoadEffect(0xFFFE, 0x25, 'battle/disarm113.eff', 0x00000000)
    Call(ScriptId.Current, 'AniAttachMainWeapon')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_1E121',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_00', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)

    Jump('loc_1E14E')

    def _loc_1E121(): pass

    label('loc_1E121')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1E14E(): pass

    label('loc_1E14E')

    OP_8A(0xFF, 0xFFFE, 'Left_Sode_In', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_Out', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_F', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_Sode_B', 0.2)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'fold', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 17)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x13)
    WaitAnimeClipFrames(PseudoChrId.Self, 26)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 28)
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    StopEffect(0xFFFE, 0x13, 0x01)
    LoadAsset('C_EQU610_C00')
    AttachEquip(0xFFFE, 'C_EQU610_C00', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'keep_appear', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 31)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x1E39C
@scena.Code('AniEvCraft03_01')
def AniEvCraft03_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'keep_appear', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'craft_open', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x1E480
@scena.Code('AniEvCraft03_02')
def AniEvCraft03_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT03_02', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F6 offset: 0x1E4BC
@scena.Code('AniBikeRearWaitL')
def AniBikeRearWaitL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F7 offset: 0x1E4F8
@scena.Code('AniEvCraft01_00b')
def AniEvCraft01_00b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00F8 offset: 0x1E55C
@scena.Code('AniEvSCraft00_00')
def AniEvSCraft00_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F9 offset: 0x1E59C
@scena.Code('AniEvSCraft00_01')
def AniEvSCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FA offset: 0x1E5DC
@scena.Code('AniEvSCraft00_02')
def AniEvSCraft00_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FB offset: 0x1E61C
@scena.Code('AniEvSCraft00_04')
def AniEvSCraft00_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FC offset: 0x1E65C
@scena.Code('AniEvSCraft00_05')
def AniEvSCraft00_05():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_05_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FD offset: 0x1E69C
@scena.Code('AniEvSCraft00_06')
def AniEvSCraft00_06():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_06_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FE offset: 0x1E6DC
@scena.Code('AniEvSCraft00_07')
def AniEvSCraft00_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_07_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FF offset: 0x1E71C
@scena.Code('AniEvSCraft00_08')
def AniEvSCraft00_08():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0100 offset: 0x1E75C
@scena.Code('AniEvSCraft00_09')
def AniEvSCraft00_09():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09_0', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0101 offset: 0x1E79C
@scena.Code('AniEvAkubi')
def AniEvAkubi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_AKUBI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E8BD',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1E89A',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1E866(): pass

    label('loc_1E866')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1E893',
    )

    Sleep(10)

    Jump('loc_1E866')

    def _loc_1E893(): pass

    label('loc_1E893')

    Sleep(300)

    def _loc_1E89A(): pass

    label('loc_1E89A')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1E8BD(): pass

    label('loc_1E8BD')

    Return()

# id: 0x0102 offset: 0x1E8C0
@scena.Code('AniEvGyu')
def AniEvGyu():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1E98D',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GYUa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1EB34')

    def _loc_1E98D(): pass

    label('loc_1E98D')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EAA3',
    )

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GYUb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EA9A',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EA77',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1EA43(): pass

    label('loc_1EA43')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EA70',
    )

    Sleep(10)

    Jump('loc_1EA43')

    def _loc_1EA70(): pass

    label('loc_1EA70')

    Sleep(300)

    def _loc_1EA77(): pass

    label('loc_1EA77')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1EA9A(): pass

    label('loc_1EA9A')

    Jump('loc_1EB34')

    def _loc_1EAA3(): pass

    label('loc_1EAA3')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GYU', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GYUa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1EB34(): pass

    label('loc_1EB34')

    Return()

# id: 0x0103 offset: 0x1EB38
@scena.Code('AniEvMegane')
def AniEvMegane():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1_2', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EC1B',
    )

    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MEGANEa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1EE81')

    def _loc_1EC1B(): pass

    label('loc_1EC1B')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1ED4A',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MEGANEb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ED41',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1ED1E',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1ECEA(): pass

    label('loc_1ECEA')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1ED17',
    )

    Sleep(10)

    Jump('loc_1ECEA')

    def _loc_1ED17(): pass

    label('loc_1ED17')

    Sleep(300)

    def _loc_1ED1E(): pass

    label('loc_1ED1E')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1ED41(): pass

    label('loc_1ED41')

    Jump('loc_1EE81')

    def _loc_1ED4A(): pass

    label('loc_1ED4A')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MEGANE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    Sleep(66)

    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EE40',
    )

    Sleep(600)

    OP_3B(0x00, ParamInt(0x7551), ParamFloat(0.3), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1EE40(): pass

    label('loc_1EE40')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MEGANEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1EE81(): pass

    label('loc_1EE81')

    Return()

# id: 0x0104 offset: 0x1EE84
@scena.Code('AniEvMukkii')
def AniEvMukkii():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MUKKII', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EFA6',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EF83',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1EF4F(): pass

    label('loc_1EF4F')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1EF7C',
    )

    Sleep(10)

    Jump('loc_1EF4F')

    def _loc_1EF7C(): pass

    label('loc_1EF7C')

    Sleep(300)

    def _loc_1EF83(): pass

    label('loc_1EF83')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1EFA6(): pass

    label('loc_1EFA6')

    Return()

# id: 0x0105 offset: 0x1EFA8
@scena.Code('AniEvMukkii_Loop')
def AniEvMukkii_Loop():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)

    def _loc_1EFDA(): pass

    label('loc_1EFDA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1F0EB',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MUKKII', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F0D9',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F0B6',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1F082(): pass

    label('loc_1F082')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F0AF',
    )

    Sleep(10)

    Jump('loc_1F082')

    def _loc_1F0AF(): pass

    label('loc_1F0AF')

    Sleep(300)

    def _loc_1F0B6(): pass

    label('loc_1F0B6')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1F0D9(): pass

    label('loc_1F0D9')

    OP_17(0x03E8, 0x0BB8)

    Jump('loc_1EFDA')

    def _loc_1F0EB(): pass

    label('loc_1F0EB')

    Return()

# id: 0x0106 offset: 0x1F0EC
@scena.Code('AniEvNaisho')
def AniEvNaisho():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F1BC',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_NAISHOa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1F36C')

    def _loc_1F1BC(): pass

    label('loc_1F1BC')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F2D5',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_NAISHOb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F2CC',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F2A9',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1F275(): pass

    label('loc_1F275')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F2A2',
    )

    Sleep(10)

    Jump('loc_1F275')

    def _loc_1F2A2(): pass

    label('loc_1F2A2')

    Sleep(300)

    def _loc_1F2A9(): pass

    label('loc_1F2A9')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1F2CC(): pass

    label('loc_1F2CC')

    Jump('loc_1F36C')

    def _loc_1F2D5(): pass

    label('loc_1F2D5')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_NAISHO', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_NAISHOa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1F36C(): pass

    label('loc_1F36C')

    Return()

# id: 0x0107 offset: 0x1F370
@scena.Code('AniEvRyoteburi')
def AniEvRyoteburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTEBURI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F495',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F472',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1F43E(): pass

    label('loc_1F43E')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F46B',
    )

    Sleep(10)

    Jump('loc_1F43E')

    def _loc_1F46B(): pass

    label('loc_1F46B')

    Sleep(300)

    def _loc_1F472(): pass

    label('loc_1F472')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1F495(): pass

    label('loc_1F495')

    Return()

# id: 0x0108 offset: 0x1F498
@scena.Code('AniEvRyoteKosi')
def AniEvRyoteKosi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F5CA',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F578',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)

    Jump('loc_1F5B5')

    def _loc_1F578(): pass

    label('loc_1F578')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1F5B5(): pass

    label('loc_1F5B5')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1F957')

    def _loc_1F5CA(): pass

    label('loc_1F5CA')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F814',
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F6FF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIb_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F6F6',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F6D3',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1F69F(): pass

    label('loc_1F69F')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F6CC',
    )

    Sleep(10)

    Jump('loc_1F69F')

    def _loc_1F6CC(): pass

    label('loc_1F6CC')

    Sleep(300)

    def _loc_1F6D3(): pass

    label('loc_1F6D3')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1F6F6(): pass

    label('loc_1F6F6')

    Jump('loc_1F80B')

    def _loc_1F6FF(): pass

    label('loc_1F6FF')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetEndhookFunction('', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F80B',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F7E8',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1F7B4(): pass

    label('loc_1F7B4')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F7E1',
    )

    Sleep(10)

    Jump('loc_1F7B4')

    def _loc_1F7E1(): pass

    label('loc_1F7E1')

    Sleep(300)

    def _loc_1F7E8(): pass

    label('loc_1F7E8')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1F80B(): pass

    label('loc_1F80B')

    Jump('loc_1F957')

    def _loc_1F814(): pass

    label('loc_1F814')

    OP_80(0.4)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F8D6',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1F957')

    def _loc_1F8D6(): pass

    label('loc_1F8D6')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1F957(): pass

    label('loc_1F957')

    Return()

# id: 0x0109 offset: 0x1F958
@scena.Code('AniEvRyoteSiri')
def AniEvRyoteSiri():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FA2C',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_SIRIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1FBE8')

    def _loc_1FA2C(): pass

    label('loc_1FA2C')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FB49',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_SIRIb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FB40',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FB1D',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1FAE9(): pass

    label('loc_1FAE9')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FB16',
    )

    Sleep(10)

    Jump('loc_1FAE9')

    def _loc_1FB16(): pass

    label('loc_1FB16')

    Sleep(300)

    def _loc_1FB1D(): pass

    label('loc_1FB1D')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1FB40(): pass

    label('loc_1FB40')

    Jump('loc_1FBE8')

    def _loc_1FB49(): pass

    label('loc_1FB49')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_SIRI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_SIRIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1FBE8(): pass

    label('loc_1FBE8')

    Return()

# id: 0x010A offset: 0x1FBEC
@scena.Code('AniEvSian')
def AniEvSian():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1_2', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FCCD',
    )

    OP_80(0.0)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1FEA2')

    def _loc_1FCCD(): pass

    label('loc_1FCCD')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FDFA',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FDF1',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FDCE',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_1FD9A(): pass

    label('loc_1FD9A')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FDC7',
    )

    Sleep(10)

    Jump('loc_1FD9A')

    def _loc_1FDC7(): pass

    label('loc_1FDC7')

    Sleep(300)

    def _loc_1FDCE(): pass

    label('loc_1FDCE')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_1FDF1(): pass

    label('loc_1FDF1')

    Jump('loc_1FEA2')

    def _loc_1FDFA(): pass

    label('loc_1FDFA')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1FEA2(): pass

    label('loc_1FEA2')

    Return()

# id: 0x010B offset: 0x1FEA4
@scena.Code('AniEvSianF')
def AniEvSianF():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1_2', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1FF86',
    )

    OP_80(0.0)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANFa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2015E')

    def _loc_1FF86(): pass

    label('loc_1FF86')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_200B4',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANFb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_200AB',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_20088',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_20054(): pass

    label('loc_20054')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_20081',
    )

    Sleep(10)

    Jump('loc_20054')

    def _loc_20081(): pass

    label('loc_20081')

    Sleep(300)

    def _loc_20088(): pass

    label('loc_20088')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_200AB(): pass

    label('loc_200AB')

    Jump('loc_2015E')

    def _loc_200B4(): pass

    label('loc_200B4')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANFa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2015E(): pass

    label('loc_2015E')

    Return()

# id: 0x010C offset: 0x20160
@scena.Code('AniEvTeburi')
def AniEvTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEBURI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20282',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_2025F',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2022B(): pass

    label('loc_2022B')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_20258',
    )

    Sleep(10)

    Jump('loc_2022B')

    def _loc_20258(): pass

    label('loc_20258')

    Sleep(300)

    def _loc_2025F(): pass

    label('loc_2025F')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_20282(): pass

    label('loc_20282')

    Return()

# id: 0x010D offset: 0x20284
@scena.Code('AniEvTeMune')
def AniEvTeMune():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_20354',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEMUNEa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_20504')

    def _loc_20354(): pass

    label('loc_20354')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_2046D',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEMUNEb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20464',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_20441',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2040D(): pass

    label('loc_2040D')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2043A',
    )

    Sleep(10)

    Jump('loc_2040D')

    def _loc_2043A(): pass

    label('loc_2043A')

    Sleep(300)

    def _loc_20441(): pass

    label('loc_20441')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_20464(): pass

    label('loc_20464')

    Jump('loc_20504')

    def _loc_2046D(): pass

    label('loc_2046D')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEMUNE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEMUNEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_20504(): pass

    label('loc_20504')

    Return()

# id: 0x010E offset: 0x20508
@scena.Code('AniEvTeUkase')
def AniEvTeUkase():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_205D9',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEUKASEa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2078C')

    def _loc_205D9(): pass

    label('loc_205D9')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_206F3',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEUKASEb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_206EA',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_206C7',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_20693(): pass

    label('loc_20693')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_206C0',
    )

    Sleep(10)

    Jump('loc_20693')

    def _loc_206C0(): pass

    label('loc_206C0')

    Sleep(300)

    def _loc_206C7(): pass

    label('loc_206C7')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_206EA(): pass

    label('loc_206EA')

    Jump('loc_2078C')

    def _loc_206F3(): pass

    label('loc_206F3')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEUKASE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEUKASEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2078C(): pass

    label('loc_2078C')

    Return()

# id: 0x010F offset: 0x20790
@scena.Code('AniEvUdegumiF')
def AniEvUdegumiF():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_20862',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIFa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_20A17')

    def _loc_20862(): pass

    label('loc_20862')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_2097C',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20973',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_20950',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2091C(): pass

    label('loc_2091C')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_20949',
    )

    Sleep(10)

    Jump('loc_2091C')

    def _loc_20949(): pass

    label('loc_20949')

    Sleep(300)

    def _loc_20950(): pass

    label('loc_20950')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_20973(): pass

    label('loc_20973')

    Jump('loc_20A17')

    def _loc_2097C(): pass

    label('loc_2097C')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIFa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_20A17(): pass

    label('loc_20A17')

    Return()

# id: 0x0110 offset: 0x20A18
@scena.Code('AniEvYorikakari')
def AniEvYorikakari():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_20AC7',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YORIKAKARIa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_20C45')

    def _loc_20AC7(): pass

    label('loc_20AC7')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_20BCB',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YORIKAKARIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20BC2',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_20B93',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_20B5F(): pass

    label('loc_20B5F')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_20B8C',
    )

    Sleep(10)

    Jump('loc_20B5F')

    def _loc_20B8C(): pass

    label('loc_20B8C')

    Sleep(300)

    def _loc_20B93(): pass

    label('loc_20B93')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_20BC2(): pass

    label('loc_20BC2')

    Jump('loc_20C45')

    def _loc_20BCB(): pass

    label('loc_20BCB')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YORIKAKARI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YORIKAKARIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_20C45(): pass

    label('loc_20C45')

    Return()

# id: 0x0111 offset: 0x20C48
@scena.Code('AniEvYubisasiMae')
def AniEvYubisasiMae():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_20D1E',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YUBISASI_MAEa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_20EE0')

    def _loc_20D1E(): pass

    label('loc_20D1E')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_20E3D',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YUBISASI_MAEb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20E34',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_20E11',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_20DDD(): pass

    label('loc_20DDD')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_20E0A',
    )

    Sleep(10)

    Jump('loc_20DDD')

    def _loc_20E0A(): pass

    label('loc_20E0A')

    Sleep(300)

    def _loc_20E11(): pass

    label('loc_20E11')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_20E34(): pass

    label('loc_20E34')

    Jump('loc_20EE0')

    def _loc_20E3D(): pass

    label('loc_20E3D')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YUBISASI_MAE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YUBISASI_MAEa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_20EE0(): pass

    label('loc_20EE0')

    Return()

# id: 0x0112 offset: 0x20EE4
@scena.Code('AniAttachEQU033')
def AniAttachEQU033():
    LoadAsset('C_EQU033')
    AttachEquip(0xFFFE, 'C_EQU033', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0113 offset: 0x20F7C
@scena.Code('AniDetachEQU033')
def AniDetachEQU033():
    ReleaseAsset('C_EQU033')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0114 offset: 0x20FD0
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320_C03')
    AttachEquip(0xFFFE, 'C_EQU320_C03', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0115 offset: 0x21044
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320_C03')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0116 offset: 0x2109C
@scena.Code('AniAttachEQU610_C00')
def AniAttachEQU610_C00():
    LoadAsset('C_EQU610_C00')
    AttachEquip(0xFFFE, 'C_EQU610_C00', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0117 offset: 0x2113C
@scena.Code('AniDetachEQU610_C00')
def AniDetachEQU610_C00():
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU610_C00')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0118 offset: 0x21194
@scena.Code('AniEv00400')
def AniEv00400():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV00400', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV00400a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0119 offset: 0x211FC
@scena.Code('AniEv00400a')
def AniEv00400a():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV00400a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011A offset: 0x21230
@scena.Code('AniEv03030')
def AniEv03030():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03030', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011B offset: 0x21264
@scena.Code('AniEv03544')
def AniEv03544():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03544', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011C offset: 0x212B8
@scena.Code('AniEv03545')
def AniEv03545():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03545', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011D offset: 0x2130C
@scena.Code('AniEv04105')
def AniEv04105():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV04105', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011E offset: 0x21360
@scena.Code('AniEv09030_1')
def AniEv09030_1():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV09030_1', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011F offset: 0x21398
@scena.Code('AniEv09030_2')
def AniEv09030_2():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV09030_2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0120 offset: 0x213D0
@scena.Code('AniEv09035')
def AniEv09035():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV09035', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV09035a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0121 offset: 0x21438
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    OP_3B(0x00, ParamInt(0x17B1), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0122 offset: 0x2151C
@scena.Code('AniEv40070')
def AniEv40070():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV40070', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0123 offset: 0x21570
@scena.Code('AniEv40072')
def AniEv40072():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV40072', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV40072a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0124 offset: 0x215F8
@scena.Code('AniEv40074')
def AniEv40074():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV40074', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV40070', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0125 offset: 0x21680
@scena.Code('AniEv40085')
def AniEv40085():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV40085', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0126 offset: 0x216D4
@scena.Code('AniAttachEQU714')
def AniAttachEQU714():
    LoadAsset('C_EQU714')
    AttachEquip(0xFFFE, 'C_EQU714', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0127 offset: 0x2176C
@scena.Code('AniDetachEQU714')
def AniDetachEQU714():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU714')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0128 offset: 0x217C0
@scena.Code('AniEv52655')
def AniEv52655():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52655', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0129 offset: 0x21814
@scena.Code('AniEv52660')
def AniEv52660():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52660', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012A offset: 0x21868
@scena.Code('AniAttachEQU715')
def AniAttachEQU715():
    LoadAsset('C_EQU715')
    AttachEquip(0xFFFE, 'C_EQU715', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x012B offset: 0x21900
@scena.Code('AniDetachEQU715')
def AniDetachEQU715():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU715')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x012C offset: 0x21954
@scena.Code('AniEv52665')
def AniEv52665():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52665', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012D offset: 0x21988
@scena.Code('AniEv52665w')
def AniEv52665w():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52665w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012E offset: 0x219BC
@scena.Code('AniEv70145')
def AniEv70145():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70145', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012F offset: 0x219F0
@scena.Code('AniEv70150')
def AniEv70150():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70150', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70150a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0130 offset: 0x21A58
@scena.Code('AniEv70161')
def AniEv70161():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70161', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70161a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0131 offset: 0x21AE0
@scena.Code('AniEv70162')
def AniEv70162():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70162', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70162a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0132 offset: 0x21B68
@scena.Code('AniEv73535')
def AniEv73535():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV73535', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV73535a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0133 offset: 0x21BF0
@scena.Code('AniEv74300')
def AniEv74300():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74300', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV74300a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0134 offset: 0x21C58
@scena.Code('AniEv74310')
def AniEv74310():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74310', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0135 offset: 0x21CAC
@scena.Code('AniEv77069')
def AniEv77069():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV77069', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0136 offset: 0x21CE0
@scena.Code('AniEv77070')
def AniEv77070():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV77070', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV77070a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0137 offset: 0x21D48
@scena.Code('AniEv77070_2')
def AniEv77070_2():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV77070_2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV77070_2a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0138 offset: 0x21DB4
@scena.Code('AniEv79412')
def AniEv79412():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79412', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79412a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0139 offset: 0x21E3C
@scena.Code('AniEv79414')
def AniEv79414():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79414', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013A offset: 0x21E90
@scena.Code('AniEv79416')
def AniEv79416():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79416', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79416a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013B offset: 0x21F18
@scena.Code('AniEv79416w')
def AniEv79416w():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79416w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013C offset: 0x21F70
@scena.Code('AniEv79422')
def AniEv79422():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79422', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013D offset: 0x21FC4
@scena.Code('AniEv79424')
def AniEv79424():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79424', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79424a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013E offset: 0x2204C
@scena.Code('AniEv79426')
def AniEv79426():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79426', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79426a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013F offset: 0x220D4
@scena.Code('AniEv79430')
def AniEv79430():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79430', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0140 offset: 0x22108
@scena.Code('AniEv79431')
def AniEv79431():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79431', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0141 offset: 0x2213C
@scena.Code('AniEv79432')
def AniEv79432():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79432', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79432a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0142 offset: 0x221C4
@scena.Code('AniEv79433')
def AniEv79433():
    Call(ScriptId.Current, 'SpringOffHead_0')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79433', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79433a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0143 offset: 0x22254
@scena.Code('AniEv79433a')
def AniEv79433a():
    Call(ScriptId.Current, 'SpringOffHead_0')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79433a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0144 offset: 0x222B0
@scena.Code('AniEv_88_88_88_01')
def AniEv_88_88_88_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_88_88_88_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0145 offset: 0x222EC
@scena.Code('AniEv_88_88_88_02')
def AniEv_88_88_88_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_88_88_88_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0146 offset: 0x22328
@scena.Code('AniEv_C1_01_01_01')
def AniEv_C1_01_01_01():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0147 offset: 0x22374
@scena.Code('AniEv_C1_01_01_02')
def AniEv_C1_01_01_02():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0148 offset: 0x223C0
@scena.Code('AniEv_C1_01_01_03')
def AniEv_C1_01_01_03():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0149 offset: 0x2240C
@scena.Code('AniEv_C1_01_01_04')
def AniEv_C1_01_01_04():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014A offset: 0x22458
@scena.Code('AniEv_C1_01_01_05')
def AniEv_C1_01_01_05():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014B offset: 0x224A4
@scena.Code('AniEv_C1_01_01_06')
def AniEv_C1_01_01_06():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014C offset: 0x224F0
@scena.Code('AniEv_C1_01_01_07')
def AniEv_C1_01_01_07():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014D offset: 0x2253C
@scena.Code('AniEv_C1_01_01_08')
def AniEv_C1_01_01_08():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014E offset: 0x22588
@scena.Code('AniEv_C1_01_01_09')
def AniEv_C1_01_01_09():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014F offset: 0x225D4
@scena.Code('AniEv_C1_01_01_10')
def AniEv_C1_01_01_10():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0150 offset: 0x22620
@scena.Code('AniEv_C1_01_01_11')
def AniEv_C1_01_01_11():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0151 offset: 0x2266C
@scena.Code('AniEv_C1_01_01_12')
def AniEv_C1_01_01_12():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_12', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0152 offset: 0x226B8
@scena.Code('AniEv_C1_01_01_13')
def AniEv_C1_01_01_13():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_13', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0153 offset: 0x22704
@scena.Code('AniEv_C1_01_01_14')
def AniEv_C1_01_01_14():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2275E(): pass

    label('loc_2275E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2277D',
    )

    Sleep(100)

    Jump('loc_2275E')

    def _loc_2277D(): pass

    label('loc_2277D')

    Return()

# id: 0x0154 offset: 0x22780
@scena.Code('AniEv_C4_02_02_04')
def AniEv_C4_02_02_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0155 offset: 0x227BC
@scena.Code('AniEv_C4_02_02_07')
def AniEv_C4_02_02_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0156 offset: 0x227F8
@scena.Code('AniEv_Z1_00_07_07')
def AniEv_Z1_00_07_07():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_07_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0157 offset: 0x2285C
@scena.Code('AniEv_Z1_00_17_01')
def AniEv_Z1_00_17_01():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_17_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0158 offset: 0x228B8
@scena.Code('AniEv_Z1_00_24_25')
def AniEv_Z1_00_24_25():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_24_25', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0159 offset: 0x2291C
@scena.Code('AniEv_Z1_00_53_53')
def AniEv_Z1_00_53_53():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_53', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015A offset: 0x22960
@scena.Code('AniEv_Z1_00_53_54')
def AniEv_Z1_00_53_54():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_54', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015B offset: 0x229A4
@scena.Code('AniEv_Z1_00_53_55')
def AniEv_Z1_00_53_55():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_55', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015C offset: 0x229E8
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR113_EV', 'EV35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk113_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk113_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk113_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk113_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x27, 'battle/cr113_01_1.eff', 0x00000000)

    Return()

# id: 0x015D offset: 0x22AAC
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'EV35000')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)
    ReleaseEffect(0xFFFE, 0x27)

    Return()

# id: 0x015E offset: 0x22B10
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22BD5',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_22D11')

    def _loc_22BD5(): pass

    label('loc_22BD5')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22C67',
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

    Jump('loc_22D11')

    def _loc_22C67(): pass

    label('loc_22C67')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22CE5',
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

    Jump('loc_22D11')

    def _loc_22CE5(): pass

    label('loc_22CE5')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_22D11(): pass

    label('loc_22D11')

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

# id: 0x015F offset: 0x22D38
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
        'loc_22DFB',
    )

    OP_3B(0x32, ParamInt(0x1251), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_22E50')

    def _loc_22DFB(): pass

    label('loc_22DFB')

    OP_3B(0x32, ParamInt(0x1252), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_22E50(): pass

    label('loc_22E50')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '0#46w1110#306w5#186w4#86w10[autoE0]', '0[autoM0]', '#50e0#106w77#100e7#106w#55e7#100e0#47e3#100e3#246w7#146w#51e0#100e0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0160 offset: 0x22F3C
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    OP_3B(0x00, ParamInt(0x17B1), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0161 offset: 0x23054
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
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 5)
    WaitAnimeClipFrames(PseudoChrId.Self, 9)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x11FD), ParamInt(0x11FE), ParamInt(0x11FF), ParamInt(0))

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2318E',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.019), ParamFloat(0.945), ParamFloat(0.422), -5.243, 33.689, 133.311, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x10)

    def _loc_2318E(): pass

    label('loc_2318E')

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    CameraCmd(0x0A, 0.0, 0.2, 1.0, 0, 100, 0, 0, 0, 0x00)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23283',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.881), ParamFloat(-0.012), ParamFloat(1.359), 0.0, 0.0, 0.0, ParamFloat(1.3), ParamFloat(1.3), ParamFloat(1.3), 0x11)

    def _loc_23283(): pass

    label('loc_23283')

    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_AD(0x01, 0x01)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0162 offset: 0x232F4
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
    SetEndhookFunction('AniAssaultAttack_endhook', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '006#96w0[autoB0]', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR113', ScriptId.Sound2, ParamInt(0x0014))
    OP_3B(0x00, ParamInt(0x0FB7), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1010), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_234F3',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0027), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.9), ParamFloat(0), 0.0, 0.0, 90.0, ParamFloat(0.25), ParamFloat(0.5), ParamFloat(0.25), 0x15)

    def _loc_234F3(): pass

    label('loc_234F3')

    WaitAnimeClipFrames(PseudoChrId.Self, 30)
    EffectSetRGBA(0xFFFE, 0x15, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 42)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 1.66667, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 55)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1200), ParamInt(0x11FE), ParamInt(0x1201), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_236C8',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0.5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x12)

    def _loc_236C8(): pass

    label('loc_236C8')

    OP_3B(0x00, ParamInt(0x0FC4), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10F4), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F54), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1200), ParamInt(300), 0x0000, 0x04B0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 70)
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0163 offset: 0x23820
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    WaitAnimeClipFrames(PseudoChrId.Self, 18)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'fold', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_3B(0x00, ParamInt(0x177F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 29)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_239C7',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x13)

    def _loc_239C7(): pass

    label('loc_239C7')

    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClipFrames(PseudoChrId.Self, 71)
    StopEffect(0xFFFE, 0x13, 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0164 offset: 0x23A5C
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23A81',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_23A81(): pass

    label('loc_23A81')

    Return()

# id: 0x0165 offset: 0x23A84
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23AE6',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_23AE6(): pass

    label('loc_23AE6')

    Return()

# id: 0x0166 offset: 0x23AE8
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_23B6B',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_23C4E')

    def _loc_23B6B(): pass

    label('loc_23B6B')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1214), ParamInt(0x1215), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_23C4E(): pass

    label('loc_23C4E')

    Return()

# id: 0x0167 offset: 0x23C50
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1216), ParamInt(0x1217), ParamInt(0), ParamInt(0))
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
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

# id: 0x0168 offset: 0x23E7C
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_23F37',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_23F99')

    def _loc_23F37(): pass

    label('loc_23F37')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x122E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_23F99(): pass

    label('loc_23F99')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5#56w4[autoE4]', '4[autoM4]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x0169 offset: 0x24040
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU610',
        ),
    )

# id: 0x016A offset: 0x240A0
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

# id: 0x016B offset: 0x24120
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FA,
            name   = '',
        ),
    )

# id: 0x016C offset: 0x241D0
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

# id: 0x016D offset: 0x24460
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

# id: 0x016E offset: 0x24530
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

# id: 0x016F offset: 0x245B0
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

# id: 0x0170 offset: 0x24630
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

# id: 0x0171 offset: 0x24690
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

# id: 0x0172 offset: 0x246F0
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

# id: 0x0173 offset: 0x24750
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

# id: 0x0174 offset: 0x24820
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

# id: 0x0175 offset: 0x24920
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

# id: 0x0176 offset: 0x24980
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

# id: 0x0177 offset: 0x249E0
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001251,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001252,
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

# id: 0x0178 offset: 0x24AB0
@scena.AnimeClips('_AniFieldAttack')
def _AniFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0179 offset: 0x24C00
@scena.AnimeClips('_AniFieldAttack2')
def _AniFieldAttack2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x017A offset: 0x24D20
@scena.AnimeClips('_AniAssaultAttack')
def _AniAssaultAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001010,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001200,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001201,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F54,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00b',
        ),
    )

# id: 0x017B offset: 0x24F30
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
            dword4 = 0x0000177F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x017C offset: 0x24FE0
@scena.AnimeClips('_AniFieldAttackEndShort')
def _AniFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_SHORT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
    )

# id: 0x017D offset: 0x25060
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

# id: 0x017E offset: 0x250C0
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

# id: 0x017F offset: 0x25120
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

# id: 0x0180 offset: 0x25180
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

# id: 0x0181 offset: 0x251E0
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

# id: 0x0182 offset: 0x25240
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

# id: 0x0183 offset: 0x252C0
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

# id: 0x0184 offset: 0x25340
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

# id: 0x0185 offset: 0x253A0
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

# id: 0x0186 offset: 0x25400
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

# id: 0x0187 offset: 0x25460
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

# id: 0x0188 offset: 0x254E0
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

# id: 0x0189 offset: 0x25560
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

# id: 0x018A offset: 0x255E0
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

# id: 0x018B offset: 0x25640
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

# id: 0x018C offset: 0x256A0
@scena.AnimeClips('_AniBikeRearWaitLeft')
def _AniBikeRearWaitLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_WAIT_L',
        ),
    )

# id: 0x018D offset: 0x25700
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

# id: 0x018E offset: 0x25760
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

# id: 0x018F offset: 0x257C0
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

# id: 0x0190 offset: 0x25820
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

# id: 0x0191 offset: 0x25880
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

# id: 0x0192 offset: 0x258E0
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

# id: 0x0193 offset: 0x25940
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

# id: 0x0194 offset: 0x259A0
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

# id: 0x0195 offset: 0x25A00
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001270,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000126E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001227,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001226,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001229,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001224,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001225,
            name   = '',
        ),
    )

# id: 0x0196 offset: 0x25BC0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FA,
            name   = '',
        ),
    )

# id: 0x0197 offset: 0x25CC0
@scena.AnimeClips('_AniBtlKisinReady')
def _AniBtlKisinReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011F9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FA,
            name   = '',
        ),
    )

# id: 0x0198 offset: 0x25DC0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001228,
            name   = '',
        ),
    )

# id: 0x0199 offset: 0x25E20
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
    )

# id: 0x019A offset: 0x25EA0
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

# id: 0x019B offset: 0x25F20
@scena.AnimeClips('_AniBtlStepInKisinPt')
def _AniBtlStepInKisinPt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001220,
            name   = '',
        ),
    )

# id: 0x019C offset: 0x25F80
@scena.AnimeClips('_AniBtlStepOutKisinPt')
def _AniBtlStepOutKisinPt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121F,
            name   = '',
        ),
    )

# id: 0x019D offset: 0x25FE0
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000FFFF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001280,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001282,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001282,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001283,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001284,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001280,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001282,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001283,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001284,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x019E offset: 0x26360
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121C,
            name   = '',
        ),
    )

# id: 0x019F offset: 0x263C0
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

# id: 0x01A0 offset: 0x26440
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001218,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001219,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001218,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001219,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121A,
            name   = '',
        ),
    )

# id: 0x01A1 offset: 0x26540
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001274,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001275,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001274,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001275,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001274,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001275,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121A,
            name   = '',
        ),
    )

# id: 0x01A2 offset: 0x266B0
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

# id: 0x01A3 offset: 0x26760
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

# id: 0x01A4 offset: 0x267C0
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
            dword4 = 0x00001276,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001277,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000121B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x01A5 offset: 0x268C0
@scena.AnimeClips('_AniBtlArts')
def _AniBtlArts():
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
            dword4 = 0x00001216,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001217,
            name   = '',
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
            name   = 'BTL_ARTSa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSb',
        ),
    )

# id: 0x01A6 offset: 0x269E0
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
            dword4 = 0x00001216,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001217,
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

# id: 0x01A7 offset: 0x26AE0
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001221,
            name   = '',
        ),
    )

# id: 0x01A8 offset: 0x26B40
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001222,
            name   = '',
        ),
    )

# id: 0x01A9 offset: 0x26BA0
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001223,
            name   = '',
        ),
    )

# id: 0x01AA offset: 0x26C00
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001230,
            name   = '',
        ),
    )

# id: 0x01AB offset: 0x26C80
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000FFFF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001240,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001242,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001240,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001231,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001093,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010A7,
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
            dword4 = 0x00008F69,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001056,
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
            dword4 = 0x00008F69,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
    )

# id: 0x01AC offset: 0x26F10
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

# id: 0x01AD offset: 0x26F70
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

# id: 0x01AE offset: 0x26FD0
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
            dword4 = 0x0000FFFF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001093,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010A7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001290,
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

# id: 0x01AF offset: 0x27140
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
    )

# id: 0x01B0 offset: 0x271A0
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001213,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001212,
            name   = '',
        ),
    )

# id: 0x01B1 offset: 0x27220
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
            name   = 'BTL_ARTS',
        ),
    )

# id: 0x01B2 offset: 0x272A0
@scena.AnimeClips('_AniBtlKisinItemPa')
def _AniBtlKisinItemPa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001216,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001217,
            name   = '',
        ),
    )

# id: 0x01B3 offset: 0x27320
@scena.AnimeClips('_AniBtlKisinChargePa')
def _AniBtlKisinChargePa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001279,
            name   = '',
        ),
    )

# id: 0x01B4 offset: 0x27380
@scena.AnimeClips('_AniBtlKisinSinkiPa')
def _AniBtlKisinSinkiPa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000127A,
            name   = '',
        ),
    )

# id: 0x01B5 offset: 0x273E0
@scena.AnimeClips('_AniBtlKisinPartnerArts')
def _AniBtlKisinPartnerArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001216,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001217,
            name   = '',
        ),
    )

# id: 0x01B6 offset: 0x27460
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

# id: 0x01B7 offset: 0x274C0
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

# id: 0x01B8 offset: 0x27520
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

# id: 0x01B9 offset: 0x27580
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122B,
            name   = '',
        ),
    )

# id: 0x01BA offset: 0x27630
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
            dword4 = 0x0000178E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000178F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001790,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01BB offset: 0x27730
@scena.AnimeClips('_AniBtlWinHitouchdb')
def _AniBtlWinHitouchdb():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HITOUCHDB',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HITOUCHDB_a',
        ),
    )

# id: 0x01BC offset: 0x277B0
@scena.AnimeClips('_AniBtlWinHitouchdbb')
def _AniBtlWinHitouchdbb():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HITOUCHDB_b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01BD offset: 0x27830
@scena.AnimeClips('_AniBtlWinHoldR')
def _AniBtlWinHoldR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HOLD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HOLDa',
        ),
    )

# id: 0x01BE offset: 0x278B0
@scena.AnimeClips('_AniBtlWinPonpon')
def _AniBtlWinPonpon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_PONPON',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_PONPON_a',
        ),
    )

# id: 0x01BF offset: 0x27930
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000178E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000178F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001790,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01C0 offset: 0x27A30
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000178E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000178F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001790,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01C1 offset: 0x27B50
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

# id: 0x01C2 offset: 0x27BB0
@scena.AnimeClips('_AniBtlWinWait')
def _AniBtlWinWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x01C3 offset: 0x27C10
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
            dword4 = 0x0000177F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01C4 offset: 0x27CC0
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
            name   = '',
        ),
    )

# id: 0x01C5 offset: 0x27D40
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
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

# id: 0x01C6 offset: 0x27E10
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_00_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_00_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/gra00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001202,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001282,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001203,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001204,
            name   = '',
        ),
    )

# id: 0x01C7 offset: 0x27FB0
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_01_3.eff',
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
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001205,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001206,
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
            name   = 'BTL_CRAFT01_00b',
        ),
    )

# id: 0x01C8 offset: 0x281A0
@scena.AnimeClips('_AniBtlCraft01_finish')
def _AniBtlCraft01_finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01C9 offset: 0x28200
@scena.AnimeClips('_AniBtlCharge')
def _AniBtlCharge():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001282,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001207,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00a',
        ),
    )

# id: 0x01CA offset: 0x28320
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001284,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001208,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01CB offset: 0x28440
@scena.AnimeClips('_AniBtlCraft03')
def _AniBtlCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_03_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_03_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_03_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/disarm113.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001209,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000120A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000120B,
            name   = '',
        ),
    )

# id: 0x01CC offset: 0x285B0
@scena.AnimeClips('_AniBtlCraft03_finish')
def _AniBtlCraft03_finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01CD offset: 0x28610
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_04.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_06.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_07.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_08.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_09.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_20.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000120C,
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
            name   = 'BTL_S_CRAFT00_01_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000129A,
            name   = '',
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
            name   = 'BTL_S_CRAFT00_02_0',
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
            name   = 'BTL_S_CRAFT00_04_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000120D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_16.eff',
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
            name   = 'BTL_S_CRAFT00_05_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001210,
            name   = '',
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
            name   = 'BTL_S_CRAFT00_06_0',
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
            name   = 'BTL_S_CRAFT00_07_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001211,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc113_00_15.eff',
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
            name   = 'BTL_S_CRAFT00_08_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000129B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_0',
        ),
    )

# id: 0x01CE offset: 0x28D00
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

# id: 0x01CF offset: 0x28D60
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

# id: 0x01D0 offset: 0x28DC0
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

# id: 0x01D1 offset: 0x28E20
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

# id: 0x01D2 offset: 0x28E80
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

# id: 0x01D3 offset: 0x28EE0
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

# id: 0x01D4 offset: 0x28FE0
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

# id: 0x01D5 offset: 0x29040
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

# id: 0x01D6 offset: 0x290C0
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

# id: 0x01D7 offset: 0x29140
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

# id: 0x01D8 offset: 0x291A0
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

# id: 0x01D9 offset: 0x29200
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

# id: 0x01DA offset: 0x29260
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

# id: 0x01DB offset: 0x292C0
@scena.AnimeClips('_AniEvFieldAttack')
def _AniEvFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DC offset: 0x29340
@scena.AnimeClips('_AniEvFieldAttack2')
def _AniEvFieldAttack2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DD offset: 0x293C0
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

# id: 0x01DE offset: 0x29440
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
            dword4 = 0x0000177F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01DF offset: 0x294F0
@scena.AnimeClips('_AniEvFieldAttackEndShort')
def _AniEvFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_SHORT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01E0 offset: 0x295A0
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

# id: 0x01E1 offset: 0x29620
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

# id: 0x01E2 offset: 0x296A0
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

# id: 0x01E3 offset: 0x29700
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

# id: 0x01E4 offset: 0x29780
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

# id: 0x01E5 offset: 0x29800
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

# id: 0x01E6 offset: 0x29880
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

# id: 0x01E7 offset: 0x298E0
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

# id: 0x01E8 offset: 0x29960
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

# id: 0x01E9 offset: 0x299E0
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

# id: 0x01EA offset: 0x29A40
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

# id: 0x01EB offset: 0x29AC0
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

# id: 0x01EC offset: 0x29B40
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

# id: 0x01ED offset: 0x29BA0
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

# id: 0x01EE offset: 0x29C00
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

# id: 0x01EF offset: 0x29C60
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

# id: 0x01F0 offset: 0x29CE0
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

# id: 0x01F1 offset: 0x29D60
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

# id: 0x01F2 offset: 0x29DE0
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

# id: 0x01F3 offset: 0x29E40
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

# id: 0x01F4 offset: 0x29EA0
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

# id: 0x01F5 offset: 0x29F00
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

# id: 0x01F6 offset: 0x29F60
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

# id: 0x01F7 offset: 0x29FE0
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

# id: 0x01F8 offset: 0x2A060
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

# id: 0x01F9 offset: 0x2A0E0
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

# id: 0x01FA offset: 0x2A140
@scena.AnimeClips('_AniEvCraft00_00')
def _AniEvCraft00_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00a',
        ),
    )

# id: 0x01FB offset: 0x2A1C0
@scena.AnimeClips('_AniEvCraft01_00')
def _AniEvCraft01_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x01FC offset: 0x2A240
@scena.AnimeClips('_AniEvCraft02_00')
def _AniEvCraft02_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00a',
        ),
    )

# id: 0x01FD offset: 0x2A2C0
@scena.AnimeClips('_AniEvCraft02_01')
def _AniEvCraft02_01():
    return ScenaAnimeClips(
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
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x01FE offset: 0x2A340
@scena.AnimeClips('_AniEvCraft03_00')
def _AniEvCraft03_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/disarm113.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU610_C00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_00a',
        ),
    )

# id: 0x01FF offset: 0x2A440
@scena.AnimeClips('_AniEvCraft03_01')
def _AniEvCraft03_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_01a',
        ),
    )

# id: 0x0200 offset: 0x2A4C0
@scena.AnimeClips('_AniEvCraft03_02')
def _AniEvCraft03_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_02',
        ),
    )

# id: 0x0201 offset: 0x2A520
@scena.AnimeClips('_AniBikeRearWaitL')
def _AniBikeRearWaitL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_REAR_WAIT_L',
        ),
    )

# id: 0x0202 offset: 0x2A580
@scena.AnimeClips('_AniEvCraft01_00b')
def _AniEvCraft01_00b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0203 offset: 0x2A600
@scena.AnimeClips('_AniEvSCraft00_00')
def _AniEvSCraft00_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00_0',
        ),
    )

# id: 0x0204 offset: 0x2A660
@scena.AnimeClips('_AniEvSCraft00_01')
def _AniEvSCraft00_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01_0',
        ),
    )

# id: 0x0205 offset: 0x2A6C0
@scena.AnimeClips('_AniEvSCraft00_02')
def _AniEvSCraft00_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02_0',
        ),
    )

# id: 0x0206 offset: 0x2A720
@scena.AnimeClips('_AniEvSCraft00_04')
def _AniEvSCraft00_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04_0',
        ),
    )

# id: 0x0207 offset: 0x2A780
@scena.AnimeClips('_AniEvSCraft00_05')
def _AniEvSCraft00_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_0',
        ),
    )

# id: 0x0208 offset: 0x2A7E0
@scena.AnimeClips('_AniEvSCraft00_06')
def _AniEvSCraft00_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_0',
        ),
    )

# id: 0x0209 offset: 0x2A840
@scena.AnimeClips('_AniEvSCraft00_07')
def _AniEvSCraft00_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_0',
        ),
    )

# id: 0x020A offset: 0x2A8A0
@scena.AnimeClips('_AniEvSCraft00_08')
def _AniEvSCraft00_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08_0',
        ),
    )

# id: 0x020B offset: 0x2A900
@scena.AnimeClips('_AniEvSCraft00_09')
def _AniEvSCraft00_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_0',
        ),
    )

# id: 0x020C offset: 0x2A960
@scena.AnimeClips('_AniEvAkubi')
def _AniEvAkubi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_AKUBI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x020D offset: 0x2AA10
@scena.AnimeClips('_AniEvGyu')
def _AniEvGyu():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_GYUa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_GYUb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_GYU',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_GYUa',
        ),
    )

# id: 0x020E offset: 0x2AB80
@scena.AnimeClips('_AniEvMegane')
def _AniEvMegane():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007551,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANEa',
        ),
    )

# id: 0x020F offset: 0x2AD20
@scena.AnimeClips('_AniEvMukkii')
def _AniEvMukkii():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MUKKII',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0210 offset: 0x2ADD0
@scena.AnimeClips('_AniEvMukkii_Loop')
def _AniEvMukkii_Loop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MUKKII',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0211 offset: 0x2AE80
@scena.AnimeClips('_AniEvNaisho')
def _AniEvNaisho():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_NAISHOa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_NAISHOb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_NAISHO',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_NAISHOa',
        ),
    )

# id: 0x0212 offset: 0x2AFF0
@scena.AnimeClips('_AniEvRyoteburi')
def _AniEvRyoteburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0213 offset: 0x2B0A0
@scena.AnimeClips('_AniEvRyoteKosi')
def _AniEvRyoteKosi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_RYOTE_KOSIb',
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
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIa',
        ),
    )

# id: 0x0214 offset: 0x2B300
@scena.AnimeClips('_AniEvRyoteSiri')
def _AniEvRyoteSiri():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_SIRIa',
        ),
    )

# id: 0x0215 offset: 0x2B470
@scena.AnimeClips('_AniEvSian')
def _AniEvSian():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_SIAN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANa',
        ),
    )

# id: 0x0216 offset: 0x2B5E0
@scena.AnimeClips('_AniEvSianF')
def _AniEvSianF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANFa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANFb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_SIANF',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANFa',
        ),
    )

# id: 0x0217 offset: 0x2B750
@scena.AnimeClips('_AniEvTeburi')
def _AniEvTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEBURI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0218 offset: 0x2B800
@scena.AnimeClips('_AniEvTeMune')
def _AniEvTeMune():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_TEMUNE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEMUNEa',
        ),
    )

# id: 0x0219 offset: 0x2B970
@scena.AnimeClips('_AniEvTeUkase')
def _AniEvTeUkase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_TEUKASE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEUKASEa',
        ),
    )

# id: 0x021A offset: 0x2BAE0
@scena.AnimeClips('_AniEvUdegumiF')
def _AniEvUdegumiF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIFa',
        ),
    )

# id: 0x021B offset: 0x2BC50
@scena.AnimeClips('_AniEvYorikakari')
def _AniEvYorikakari():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YORIKAKARIb',
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
            name   = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YORIKAKARIa',
        ),
    )

# id: 0x021C offset: 0x2BD50
@scena.AnimeClips('_AniEvYubisasiMae')
def _AniEvYubisasiMae():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
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
            name   = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YUBISASI_MAEa',
        ),
    )

# id: 0x021D offset: 0x2BEC0
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

# id: 0x021E offset: 0x2BF20
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

# id: 0x021F offset: 0x2BF80
@scena.AnimeClips('_AniAttachEQU610_C00')
def _AniAttachEQU610_C00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU610_C00',
        ),
    )

# id: 0x0220 offset: 0x2BFE0
@scena.AnimeClips('_AniEv00400')
def _AniEv00400():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00400',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00400a',
        ),
    )

# id: 0x0221 offset: 0x2C060
@scena.AnimeClips('_AniEv00400a')
def _AniEv00400a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00400a',
        ),
    )

# id: 0x0222 offset: 0x2C0C0
@scena.AnimeClips('_AniEv03030')
def _AniEv03030():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03030',
        ),
    )

# id: 0x0223 offset: 0x2C120
@scena.AnimeClips('_AniEv03544')
def _AniEv03544():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03544',
        ),
    )

# id: 0x0224 offset: 0x2C180
@scena.AnimeClips('_AniEv03545')
def _AniEv03545():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03545',
        ),
    )

# id: 0x0225 offset: 0x2C1E0
@scena.AnimeClips('_AniEv04105')
def _AniEv04105():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV04105',
        ),
    )

# id: 0x0226 offset: 0x2C240
@scena.AnimeClips('_AniEv09030_1')
def _AniEv09030_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV09030_1',
        ),
    )

# id: 0x0227 offset: 0x2C2A0
@scena.AnimeClips('_AniEv09030_2')
def _AniEv09030_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV09030_2',
        ),
    )

# id: 0x0228 offset: 0x2C300
@scena.AnimeClips('_AniEv09035')
def _AniEv09035():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV09035',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV09035a',
        ),
    )

# id: 0x0229 offset: 0x2C380
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
            dword4 = 0x000017B1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x022A offset: 0x2C430
@scena.AnimeClips('_AniEv40070')
def _AniEv40070():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40070',
        ),
    )

# id: 0x022B offset: 0x2C490
@scena.AnimeClips('_AniEv40072')
def _AniEv40072():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40072',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40072a',
        ),
    )

# id: 0x022C offset: 0x2C510
@scena.AnimeClips('_AniEv40074')
def _AniEv40074():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40074',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40070',
        ),
    )

# id: 0x022D offset: 0x2C590
@scena.AnimeClips('_AniEv40085')
def _AniEv40085():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV40085',
        ),
    )

# id: 0x022E offset: 0x2C5F0
@scena.AnimeClips('_AniAttachEQU714')
def _AniAttachEQU714():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU714',
        ),
    )

# id: 0x022F offset: 0x2C650
@scena.AnimeClips('_AniEv52655')
def _AniEv52655():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV52655',
        ),
    )

# id: 0x0230 offset: 0x2C6B0
@scena.AnimeClips('_AniEv52660')
def _AniEv52660():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV52660',
        ),
    )

# id: 0x0231 offset: 0x2C710
@scena.AnimeClips('_AniAttachEQU715')
def _AniAttachEQU715():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU715',
        ),
    )

# id: 0x0232 offset: 0x2C770
@scena.AnimeClips('_AniEv52665')
def _AniEv52665():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV52665',
        ),
    )

# id: 0x0233 offset: 0x2C7D0
@scena.AnimeClips('_AniEv52665w')
def _AniEv52665w():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV52665w',
        ),
    )

# id: 0x0234 offset: 0x2C830
@scena.AnimeClips('_AniEv70145')
def _AniEv70145():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70145',
        ),
    )

# id: 0x0235 offset: 0x2C890
@scena.AnimeClips('_AniEv70150')
def _AniEv70150():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70150',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70150a',
        ),
    )

# id: 0x0236 offset: 0x2C910
@scena.AnimeClips('_AniEv70161')
def _AniEv70161():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70161',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70161a',
        ),
    )

# id: 0x0237 offset: 0x2C990
@scena.AnimeClips('_AniEv70162')
def _AniEv70162():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70162',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70162a',
        ),
    )

# id: 0x0238 offset: 0x2CA10
@scena.AnimeClips('_AniEv73535')
def _AniEv73535():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV73535',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV73535a',
        ),
    )

# id: 0x0239 offset: 0x2CA90
@scena.AnimeClips('_AniEv74300')
def _AniEv74300():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74300',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74300a',
        ),
    )

# id: 0x023A offset: 0x2CB10
@scena.AnimeClips('_AniEv74310')
def _AniEv74310():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74310',
        ),
    )

# id: 0x023B offset: 0x2CB70
@scena.AnimeClips('_AniEv77069')
def _AniEv77069():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77069',
        ),
    )

# id: 0x023C offset: 0x2CBD0
@scena.AnimeClips('_AniEv77070')
def _AniEv77070():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77070',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77070a',
        ),
    )

# id: 0x023D offset: 0x2CC50
@scena.AnimeClips('_AniEv77070_2')
def _AniEv77070_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77070_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77070_2a',
        ),
    )

# id: 0x023E offset: 0x2CCD0
@scena.AnimeClips('_AniEv79412')
def _AniEv79412():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79412',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79412a',
        ),
    )

# id: 0x023F offset: 0x2CD50
@scena.AnimeClips('_AniEv79414')
def _AniEv79414():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79414',
        ),
    )

# id: 0x0240 offset: 0x2CDB0
@scena.AnimeClips('_AniEv79416')
def _AniEv79416():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79416',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79416a',
        ),
    )

# id: 0x0241 offset: 0x2CE30
@scena.AnimeClips('_AniEv79416w')
def _AniEv79416w():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79416w',
        ),
    )

# id: 0x0242 offset: 0x2CE90
@scena.AnimeClips('_AniEv79422')
def _AniEv79422():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79422',
        ),
    )

# id: 0x0243 offset: 0x2CEF0
@scena.AnimeClips('_AniEv79424')
def _AniEv79424():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79424',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79424a',
        ),
    )

# id: 0x0244 offset: 0x2CF70
@scena.AnimeClips('_AniEv79426')
def _AniEv79426():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79426',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79426a',
        ),
    )

# id: 0x0245 offset: 0x2CFF0
@scena.AnimeClips('_AniEv79430')
def _AniEv79430():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79430',
        ),
    )

# id: 0x0246 offset: 0x2D050
@scena.AnimeClips('_AniEv79431')
def _AniEv79431():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79431',
        ),
    )

# id: 0x0247 offset: 0x2D0B0
@scena.AnimeClips('_AniEv79432')
def _AniEv79432():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79432',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79432a',
        ),
    )

# id: 0x0248 offset: 0x2D130
@scena.AnimeClips('_AniEv79433')
def _AniEv79433():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79433',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79433a',
        ),
    )

# id: 0x0249 offset: 0x2D1B0
@scena.AnimeClips('_AniEv79433a')
def _AniEv79433a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79433a',
        ),
    )

# id: 0x024A offset: 0x2D210
@scena.AnimeClips('_AniEv_88_88_88_01')
def _AniEv_88_88_88_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_88_88_88_01',
        ),
    )

# id: 0x024B offset: 0x2D270
@scena.AnimeClips('_AniEv_88_88_88_02')
def _AniEv_88_88_88_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_88_88_88_02',
        ),
    )

# id: 0x024C offset: 0x2D2D0
@scena.AnimeClips('_AniEv_C1_01_01_01')
def _AniEv_C1_01_01_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_01',
        ),
    )

# id: 0x024D offset: 0x2D330
@scena.AnimeClips('_AniEv_C1_01_01_02')
def _AniEv_C1_01_01_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_02',
        ),
    )

# id: 0x024E offset: 0x2D390
@scena.AnimeClips('_AniEv_C1_01_01_03')
def _AniEv_C1_01_01_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_03',
        ),
    )

# id: 0x024F offset: 0x2D3F0
@scena.AnimeClips('_AniEv_C1_01_01_04')
def _AniEv_C1_01_01_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_04',
        ),
    )

# id: 0x0250 offset: 0x2D450
@scena.AnimeClips('_AniEv_C1_01_01_05')
def _AniEv_C1_01_01_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_05',
        ),
    )

# id: 0x0251 offset: 0x2D4B0
@scena.AnimeClips('_AniEv_C1_01_01_06')
def _AniEv_C1_01_01_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_06',
        ),
    )

# id: 0x0252 offset: 0x2D510
@scena.AnimeClips('_AniEv_C1_01_01_07')
def _AniEv_C1_01_01_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_07',
        ),
    )

# id: 0x0253 offset: 0x2D570
@scena.AnimeClips('_AniEv_C1_01_01_08')
def _AniEv_C1_01_01_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_08',
        ),
    )

# id: 0x0254 offset: 0x2D5D0
@scena.AnimeClips('_AniEv_C1_01_01_09')
def _AniEv_C1_01_01_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_09',
        ),
    )

# id: 0x0255 offset: 0x2D630
@scena.AnimeClips('_AniEv_C1_01_01_10')
def _AniEv_C1_01_01_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_10',
        ),
    )

# id: 0x0256 offset: 0x2D690
@scena.AnimeClips('_AniEv_C1_01_01_11')
def _AniEv_C1_01_01_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_11',
        ),
    )

# id: 0x0257 offset: 0x2D6F0
@scena.AnimeClips('_AniEv_C1_01_01_12')
def _AniEv_C1_01_01_12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_12',
        ),
    )

# id: 0x0258 offset: 0x2D750
@scena.AnimeClips('_AniEv_C1_01_01_13')
def _AniEv_C1_01_01_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_13',
        ),
    )

# id: 0x0259 offset: 0x2D7B0
@scena.AnimeClips('_AniEv_C1_01_01_14')
def _AniEv_C1_01_01_14():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C1_01_01_14',
        ),
    )

# id: 0x025A offset: 0x2D810
@scena.AnimeClips('_AniEv_C4_02_02_04')
def _AniEv_C4_02_02_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_04',
        ),
    )

# id: 0x025B offset: 0x2D870
@scena.AnimeClips('_AniEv_C4_02_02_07')
def _AniEv_C4_02_02_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_07',
        ),
    )

# id: 0x025C offset: 0x2D8D0
@scena.AnimeClips('_AniEv_Z1_00_07_07')
def _AniEv_Z1_00_07_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_07_07',
        ),
    )

# id: 0x025D offset: 0x2D930
@scena.AnimeClips('_AniEv_Z1_00_17_01')
def _AniEv_Z1_00_17_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_17_01',
        ),
    )

# id: 0x025E offset: 0x2D990
@scena.AnimeClips('_AniEv_Z1_00_24_25')
def _AniEv_Z1_00_24_25():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_24_25',
        ),
    )

# id: 0x025F offset: 0x2D9F0
@scena.AnimeClips('_AniEv_Z1_00_53_53')
def _AniEv_Z1_00_53_53():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_53_53',
        ),
    )

# id: 0x0260 offset: 0x2DA50
@scena.AnimeClips('_AniEv_Z1_00_53_54')
def _AniEv_Z1_00_53_54():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_53_54',
        ),
    )

# id: 0x0261 offset: 0x2DAB0
@scena.AnimeClips('_AniEv_Z1_00_53_55')
def _AniEv_Z1_00_53_55():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_53_55',
        ),
    )

# id: 0x0262 offset: 0x2DB10
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk113_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk113_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk113_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk113_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr113_01_1.eff',
        ),
    )

# id: 0x0263 offset: 0x2DC10
@scena.AnimeClips('_AniCvWait')
def _AniCvWait():
    return ScenaAnimeClips(
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

# id: 0x0264 offset: 0x2DD60
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001251,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001252,
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

# id: 0x0265 offset: 0x2DE30
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
            dword4 = 0x000017B1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0266 offset: 0x2DEE0
@scena.AnimeClips('_AniCvAttack')
def _AniCvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001093,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0267 offset: 0x2E000
@scena.AnimeClips('_AniCvAssaultAttack')
def _AniCvAssaultAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001010,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001200,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000011FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001201,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F54,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00b',
        ),
    )

# id: 0x0268 offset: 0x2E210
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
            dword4 = 0x0000177F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0269 offset: 0x2E2C0
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
            dword4 = 0x00001214,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001215,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x026A offset: 0x2E3C0
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
            dword4 = 0x00001216,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001217,
            name   = '',
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
            name   = 'BTL_ARTSa',
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

# id: 0x026B offset: 0x2E510
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000122E,
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
