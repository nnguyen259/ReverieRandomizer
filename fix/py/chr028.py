import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr028_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr028.dat')

# id: 0x0000 offset: 0x30CC
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_DASH_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_DASH_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_MOVE_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WALK_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'DISARM_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WAITCHANGE_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WALK_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'FATTACK1_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'FATTACK2_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'DISARM_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_STOP_DASH_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_STOP_RUN_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_TURN_L_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_TURN_R_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WAITCHANGE_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_WAIT_WALK_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR028_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTS_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTSa_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTSb_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ATTACK_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DEAD_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DEADa_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ITEM_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_POWERUP_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_POWERUPa_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DAMAGE_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_WEAK_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_FRONTSTEP_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_BACKSTEP_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ARTSb_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ATTACK_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DEAD_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DEADa_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ITEM_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_POWERUP_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_POWERUPa_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_DAMAGE_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_WEAK_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_WEAKDAMAGE_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_FRONTSTEP_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_BACKSTEP_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_ORDER',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT01_00b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR028_BT1',
            symbol     = 'BTL_CRAFT13_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_00b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC1',
            symbol     = 'BTL_S_CRAFT00_04a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_01_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_02_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_03_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_04_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_05_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_06_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_07_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_08_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_09_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_10_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_11_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_11a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR028_SC2',
            symbol     = 'BTL_S_CRAFT10_12_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'HORSE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_WAIT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_TILT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_TILT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_TILT_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_BACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_BACK_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_BACK_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_HANDLE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_HANDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_SIDE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR028_HS1',
            symbol     = 'BIKE_SIDE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_CRAPBACK_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_KNUCKLE_L2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_KNUCKLE_L2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_KNUCKLE_L2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_CHIES_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_CHIES_La',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_GJ_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_GJ_La',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_KNUCKLE_R2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_L2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_L2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_L2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR028_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_ENDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_HIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_HIT2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_RESULT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_RESULTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG1',
            symbol     = 'FISH_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG13',
            symbol     = 'MG13_SUIKA_HIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG13',
            symbol     = 'MG13_SUIKA_MISS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR028_MG13',
            symbol     = 'MG13_SUIKA_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'BTL_DEAD1_G',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'BTL_DEAD1_S',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'BTL_FLOAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'BTL_DOWNHILL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_KATATE_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_DESK_KATATE_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FALLa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARDb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_OP50_POSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_OP50_POSE_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_ATAMA_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MIRU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MIRUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MIRUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV_YAREYARE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EVC30',
            symbol     = 'EV_Z1_00_52_52',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EVC30',
            symbol     = 'EV_Z1_00_52_52_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev00025',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev00025a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03000a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03020',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03025',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev03025a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV03030',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV30000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev30205',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev30205a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev34560',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev34560a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV35000_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV45000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev45005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV54525',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV55030',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV55035',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59100',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59100a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59105',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59105a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59110',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV59110a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV70105',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV70105a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV70106',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV70106a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV7',
            symbol     = 'EV70125',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV79284',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV79285',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV79285a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV79286',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'EV79286a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev81000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR028_EV',
            symbol     = 'ev81000a',
        ),
    )

# id: 0x0001 offset: 0xC9D4
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xC9F4
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xCA0C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_CA49',
    )

    AnimeClipCmd(0x0F, PseudoChrId.Self, 0x00)
    AnimeClipCmd(0x0D, PseudoChrId.Self)
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR028_DF1', 'WAIT')

    Return()

    def _loc_CA49(): pass

    label('loc_CA49')

    AnimeClipCmd(0x0D, PseudoChrId.Self)

    Return()

# id: 0x0004 offset: 0xCA54
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CA66',
    )

    def _loc_CA66(): pass

    label('loc_CA66')

    Call(ScriptId.Current, 'PlayFakeEffect')
    Call(ScriptId.Current, 'AniSetWeaponMode')
    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0005 offset: 0xCAE4
@scena.Code('PlayFakeEffect')
def PlayFakeEffect():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_CB73',
    )

    LoadEffect(0xFFFE, 0x2F, 'system/shadow_chr_aura.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x002F), PseudoChrId.Self, 0x00000023, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_CB73(): pass

    label('loc_CB73')

    Return()

# id: 0x0006 offset: 0xCB74
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0007 offset: 0xCB9C
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0008 offset: 0xCBC8
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0009 offset: 0xCBD4
@scena.Code('AniSetWeaponMode')
def AniSetWeaponMode():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_CC0A',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CC5B')

    def _loc_CC0A(): pass

    label('loc_CC0A')

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x17),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CC5B',
    )

    If(
        (
            (Expr.Eval, "ModelGetBattleStyle(0x0017)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC4D',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CC5A')

    def _loc_CC4D(): pass

    label('loc_CC4D')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CC5A(): pass

    label('loc_CC5A')

    Return()

    def _loc_CC5B(): pass

    label('loc_CC5B')

    If(
        (
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_CD07',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_CCF1',
    )

    MenuChrFlagCmd(0x01, PseudoChrId.Self, 0x40000000)

    If(
        (
            (Expr.Eval, "ModelGetBattleStyle(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CCDB',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CCE8')

    def _loc_CCDB(): pass

    label('loc_CCDB')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CCE8(): pass

    label('loc_CCE8')

    Jump('loc_CCFE')

    def _loc_CCF1(): pass

    label('loc_CCF1')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CCFE(): pass

    label('loc_CCFE')

    Jump('loc_CD14')

    def _loc_CD07(): pass

    label('loc_CD07')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CD14(): pass

    label('loc_CD14')

    Return()

# id: 0x000A offset: 0xCD18
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000B offset: 0xCD28
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x000C offset: 0xCD38
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000400)

    Return()

# id: 0x000D offset: 0xCD48
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000E offset: 0xCD58
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000F offset: 0xCD68
@scena.Code('Ani_MG_Load')
def Ani_MG_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000020)

    Return()

# id: 0x0010 offset: 0xCD78
@scena.Code('Ani_MG1_Load')
def Ani_MG1_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR028_MG1')

    Return()

# id: 0x0011 offset: 0xCD90
@scena.Code('Ani_MG13_Load')
def Ani_MG13_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR028_MG13')

    Return()

# id: 0x0012 offset: 0xCDA8
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0013 offset: 0xCDB8
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0014 offset: 0xCDD0
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000400)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0015 offset: 0xCDE8
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0016 offset: 0xCE00
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0017 offset: 0xCE18
@scena.Code('Ani_MG_Release')
def Ani_MG_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000020)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0018 offset: 0xCE30
@scena.Code('Ani_MG1_Release')
def Ani_MG1_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR028_MG1')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0019 offset: 0xCE54
@scena.Code('Ani_MG13_Release')
def Ani_MG13_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'CHR028_MG13')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x001A offset: 0xCE78
@scena.Code('DefaultFace')
def DefaultFace():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_CECC',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Jump('loc_CEF7')

    def _loc_CECC(): pass

    label('loc_CECC')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    def _loc_CEF7(): pass

    label('loc_CEF7')

    Return()

# id: 0x001B offset: 0xCEF8
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_CF12',
    )

    Jump('loc_CF53')

    def _loc_CF12(): pass

    label('loc_CF12')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_CF53(): pass

    label('loc_CF53')

    Return()

# id: 0x001C offset: 0xCF54
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF79',
    )

    ModelCmd(0x0B, 0xFFFE)

    Jump('loc_CF93')

    def _loc_CF79(): pass

    label('loc_CF79')

    If(
        (
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            Expr.Return,
        ),
        'loc_CF93',
    )

    ModelCmd(0x0B, 0xFFFE)

    def _loc_CF93(): pass

    label('loc_CF93')

    Return()

# id: 0x001D offset: 0xCF94
@scena.Code('OnCampIn')
def OnCampIn():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
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

# id: 0x001E offset: 0xCFFC
@scena.Code('OnCostumeIn1')
def OnCostumeIn1():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
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
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x001F offset: 0xD074
@scena.Code('OnCostumeIn2')
def OnCostumeIn2():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
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
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'OnCostumeIn2_2', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x0020 offset: 0xD0DC
@scena.Code('OnCostumeIn2_2')
def OnCostumeIn2_2():
    SetEndhookFunction('DefaultFace', 0x000B)
    OP_80(0.2)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D16D',
    )

    OP_3B(0x32, ParamInt(0x1BB8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D1C2')

    def _loc_D16D(): pass

    label('loc_D16D')

    OP_3B(0x32, ParamInt(0x1BB9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_D1C2(): pass

    label('loc_D1C2')

    SetChrFace(0x03, PseudoChrId.Self, '00000000011EEEEEEEEEEEEE0', '[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0021 offset: 0xD25C
@scena.Code('OnCostumeIn3')
def OnCostumeIn3():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
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
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'OnCostumeIn3_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'OnCostumeIn3_2', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x0022 offset: 0xD300
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    OP_3B(0x32, ParamInt(0x1B8D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, 'F1', '0', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'F2', '13030134', '', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0023 offset: 0xD424
@scena.Code('AniFieldChange')
def AniFieldChange():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(7000), ParamInt(0x1B59), ParamInt(0x1B5A), ParamInt(0))

    Return()

# id: 0x0024 offset: 0xD460
@scena.Code('ShowEquip_S')
def ShowEquip_S():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0025 offset: 0xD490
@scena.Code('ShowEquip_G')
def ShowEquip_G():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0026 offset: 0xD4C0
@scena.Code('ShowEquip')
def ShowEquip():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D4EE',
    )

    Call(ScriptId.Current, 'ShowEquip_G')

    Jump('loc_D501')

    def _loc_D4EE(): pass

    label('loc_D4EE')

    Call(ScriptId.Current, 'ShowEquip_S')

    def _loc_D501(): pass

    label('loc_D501')

    Return()

# id: 0x0027 offset: 0xD504
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x0028 offset: 0xD534
@scena.Code('AniReset')
def AniReset():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'EraseEquip')

    ExecExpressionWithReg(
        0x03,
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
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0029 offset: 0xD5A4
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    Return()

# id: 0x002A offset: 0xD5A8
@scena.Code('AniResetWorkRun')
def AniResetWorkRun():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x002B offset: 0xD5B8
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB05', 0.2)

    Return()

# id: 0x002C offset: 0xD768
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB05', 0.2)

    Return()

# id: 0x002D offset: 0xD918
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x002E offset: 0xD91C
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x002F offset: 0xD920
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
        'loc_DA3B',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DA0E',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D9C9',
    )

    Call(ScriptId.Current, 'ShowEquip_S')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_DA05')

    def _loc_D9C9(): pass

    label('loc_D9C9')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'ShowEquip_G')

    def _loc_DA05(): pass

    label('loc_DA05')

    Jump('loc_DA32')

    def _loc_DA0E(): pass

    label('loc_DA0E')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_DA32(): pass

    label('loc_DA32')

    Jump('loc_DF6A')

    def _loc_DA3B(): pass

    label('loc_DA3B')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_DD39',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC0B',
    )

    Call(ScriptId.Current, 'ShowEquip_S')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DAA8',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_DAA8(): pass

    label('loc_DAA8')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DB3B',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DC02')

    def _loc_DB3B(): pass

    label('loc_DB3B')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DBD9',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x02, 0.1)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_DASH_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DC02')

    def _loc_DBD9(): pass

    label('loc_DBD9')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_DC02(): pass

    label('loc_DC02')

    Jump('loc_DD30')

    def _loc_DC0B(): pass

    label('loc_DC0B')

    Call(ScriptId.Current, 'ShowEquip_G')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC49',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_DC49(): pass

    label('loc_DC49')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCA3',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DD30')

    def _loc_DCA3(): pass

    label('loc_DCA3')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DD07',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x02, 0.1)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DD30')

    def _loc_DD07(): pass

    label('loc_DD07')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_DD30(): pass

    label('loc_DD30')

    Jump('loc_DF6A')

    def _loc_DD39(): pass

    label('loc_DD39')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_DD95',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_DF6A')

    def _loc_DD95(): pass

    label('loc_DD95')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DE2E',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DF6A')

    def _loc_DE2E(): pass

    label('loc_DE2E')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DEC0',
    )

    ExecExpressionWithReg(
        0x04,
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DF6A')

    def _loc_DEC0(): pass

    label('loc_DEC0')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DF3E',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_DF6A')

    def _loc_DF3E(): pass

    label('loc_DF3E')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_DF6A(): pass

    label('loc_DF6A')

    ExecExpressionWithReg(
        0x04,
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

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0030 offset: 0xDF94
@scena.Code('AniWalk')
def AniWalk():
    Call(ScriptId.Current, 'ResetModel1')
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_E06A',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E038',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_E038(): pass

    label('loc_E038')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E0E1')

    def _loc_E06A(): pass

    label('loc_E06A')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E0BE',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_E0BE(): pass

    label('loc_E0BE')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E0E1(): pass

    label('loc_E0E1')

    Sleep(166)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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

# id: 0x0031 offset: 0xE110
@scena.Code('AniRun')
def AniRun():
    Call(ScriptId.Current, 'SpringOff')

    ExecExpressionWithReg(
        0x06,
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
        'loc_E1C1',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E18F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E1B8')

    def _loc_E18F(): pass

    label('loc_E18F')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E1B8(): pass

    label('loc_E1B8')

    Jump('loc_E1E3')

    def _loc_E1C1(): pass

    label('loc_E1C1')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E1E3(): pass

    label('loc_E1E3')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E202',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E202(): pass

    label('loc_E202')

    Sleep(666)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0032 offset: 0xE224
@scena.Code('AniDash')
def AniDash():
    ExecExpressionWithReg(
        0x06,
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
        'loc_E2CD',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E29B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E2C4')

    def _loc_E29B(): pass

    label('loc_E29B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E2C4(): pass

    label('loc_E2C4')

    Jump('loc_E2F0')

    def _loc_E2CD(): pass

    label('loc_E2CD')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E2F0(): pass

    label('loc_E2F0')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E30F',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_E30F(): pass

    label('loc_E30F')

    Sleep(666)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xE330
@scena.Code('AniBack')
def AniBack():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(166)

    ExecExpressionWithReg(
        0x04,
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

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0034 offset: 0xE38C
@scena.Code('AniDamage')
def AniDamage():
    OP_3B(0x32, ParamInt(0x1B77), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.2)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E46B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')
    Sleep(1)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniBtlWait_S')

    Jump('loc_E4D1')

    def _loc_E46B(): pass

    label('loc_E46B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')
    Sleep(1)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniBtlWait_G')

    def _loc_E4D1(): pass

    label('loc_E4D1')

    Return()

# id: 0x0035 offset: 0xE4D4
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x06,
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
        'loc_E5A3',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E555',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E59A')

    def _loc_E555(): pass

    label('loc_E555')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E59A',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E59A(): pass

    label('loc_E59A')

    Jump('loc_E631')

    def _loc_E5A3(): pass

    label('loc_E5A3')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E5EE',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E631')

    def _loc_E5EE(): pass

    label('loc_E5EE')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E631',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E631(): pass

    label('loc_E631')

    OP_3F(PseudoChrId.Self, 0x00000000)
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0036 offset: 0xE650
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
        'loc_E6AE',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E797')

    def _loc_E6AE(): pass

    label('loc_E6AE')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_E739',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_E797')

    def _loc_E739(): pass

    label('loc_E739')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E797(): pass

    label('loc_E797')

    Return()

# id: 0x0037 offset: 0xE798
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0038 offset: 0xE7D4
@scena.Code('AniLand')
def AniLand():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0039 offset: 0xE85C
@scena.Code('AniIdle')
def AniIdle():
    SetEndhookFunction('DefaultFace', 0x000B)
    OP_80(0.2)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E8ED',
    )

    OP_3B(0x32, ParamInt(0x1BB8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E942')

    def _loc_E8ED(): pass

    label('loc_E8ED')

    OP_3B(0x32, ParamInt(0x1BB9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E942(): pass

    label('loc_E942')

    SetChrFace(0x03, PseudoChrId.Self, '00000000011EEEEEEEEEEEEE0', '[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x003A offset: 0xE9DC
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk028_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk028_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk028_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk028_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle_sys/sysmchange.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_EABF',
    )

    LoadEffect(0xFFFE, 0x27, 'battle/atk028_a0.eff', 0x00000000)

    def _loc_EABF(): pass

    label('loc_EABF')

    Return()

# id: 0x003B offset: 0xEAC0
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)
    ReleaseEffect(0xFFFE, 0x27)

    Return()

# id: 0x003C offset: 0xEAF8
@scena.Code('AniFieldAttack')
def AniFieldAttack():
    ExecExpressionWithReg(
        0x04,
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

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB44',
    )

    Call(ScriptId.Current, 'AniAttachMainWeaponSword')

    def _loc_EB44(): pass

    label('loc_EB44')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip_S')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x03, 0x00)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Sleep(166)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.7, 6.5, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(66)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EC8E',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5D), ParamInt(0x1B5E), ParamInt(0), ParamInt(0))

    Jump('loc_ECAE')

    def _loc_EC8E(): pass

    label('loc_EC8E')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5D), ParamInt(0x1B5F), ParamInt(0), ParamInt(0))

    def _loc_ECAE(): pass

    label('loc_ECAE')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.15), ParamFloat(0.5), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x02)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 30, 100, 30, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Sleep(66)

    Sleep(200)

    OP_41(0xFFFE, 0x01)
    Sleep(100)

    OP_AD(0x01, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    Sleep(333)

    OP_AD(0x00, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003D offset: 0xEDF0
@scena.Code('AniFieldAttack2')
def AniFieldAttack2():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK2_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 36.8, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Sleep(166)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.9, 6.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.072), ParamFloat(1.229), ParamFloat(0.175), -9.093, 22.424, -26.751, ParamFloat(1.1), ParamFloat(1.1), ParamFloat(1.1), 0x02)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 30, 100, 30, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EF8A',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5E), ParamInt(0x1B60), ParamInt(0), ParamInt(0))

    Jump('loc_EFAA')

    def _loc_EF8A(): pass

    label('loc_EF8A')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5E), ParamInt(0x1B5F), ParamInt(0), ParamInt(0))

    def _loc_EFAA(): pass

    label('loc_EFAA')

    Sleep(133)

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_5E(0x01, 0x0064)
    Sleep(33)

    OP_41(0xFFFE, 0x01)
    Sleep(266)

    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003E offset: 0xF044
@scena.Code('AniAssaultAttack')
def AniAssaultAttack():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetEndhookFunction('AniAssaultEnd_endHook', 0x000B)
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B60), ParamInt(0x1B61), ParamInt(0), ParamInt(0))
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 0.333333, 1.66667, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '232[autoE2]', '[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(333)

    OP_3B(0x00, ParamInt(0x1005), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0027), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x8F95), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x0104), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_41(0xFFFE, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 1.7, 2.5, -1.0, 0x00, 0x00)
    Sleep(166)

    Sleep(0)

    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Sleep(0)

    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.75, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x003F offset: 0xF418
@scena.Code('AniAssaultEnd_endHook')
def AniAssaultEnd_endHook():
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x0040 offset: 0xF450
@scena.Code('AniFieldAttackEnd')
def AniFieldAttackEnd():
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    OP_3B(0x00, ParamInt(0x753D), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Sleep(766)

    OP_3B(0x00, ParamInt(0x7534), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7538), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniFieldAttackEnd_endHook')
    Sleep(66)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0041 offset: 0xF634
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0042 offset: 0xF668
@scena.Code('AniFieldAttackEndShort')
def AniFieldAttackEndShort():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Call(ScriptId.Current, 'ShowEquip_S')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 43.6667, -1.0, -1.0, 0x00, 0x00)
    Sleep(1100)

    OP_3B(0x00, ParamInt(0x7534), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7538), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_04(0x0B, 'EraseEquip')

    Return()

# id: 0x0043 offset: 0xF7A4
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0044 offset: 0xF810
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0045 offset: 0xF864
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0046 offset: 0xF8AC
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x0047 offset: 0xF8B0
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x0048 offset: 0xF8B4
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0049 offset: 0xF8EC
@scena.Code('AniHorseRun')
def AniHorseRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004A offset: 0xF924
@scena.Code('AniHorseDash')
def AniHorseDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004B offset: 0xF95C
@scena.Code('AniHorseStop')
def AniHorseStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0xF994
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004D offset: 0xF9F0
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004E offset: 0xFA4C
@scena.Code('AniRideBikeVoice')
def AniRideBikeVoice():
    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0001)"),
            Expr.Return,
        ),
        'loc_FA68',
    )

    Jump('loc_FB64')

    def _loc_FA68(): pass

    label('loc_FA68')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0003)"),
            Expr.Return,
        ),
        'loc_FA84',
    )

    Jump('loc_FB64')

    def _loc_FA84(): pass

    label('loc_FA84')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0005)"),
            Expr.Return,
        ),
        'loc_FAA0',
    )

    Jump('loc_FB64')

    def _loc_FAA0(): pass

    label('loc_FAA0')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0007)"),
            Expr.Return,
        ),
        'loc_FABC',
    )

    Jump('loc_FB64')

    def _loc_FABC(): pass

    label('loc_FABC')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0009)"),
            Expr.Return,
        ),
        'loc_FAD8',
    )

    Jump('loc_FB64')

    def _loc_FAD8(): pass

    label('loc_FAD8')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0002)"),
            Expr.Return,
        ),
        'loc_FAF4',
    )

    Jump('loc_FB64')

    def _loc_FAF4(): pass

    label('loc_FAF4')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0004)"),
            Expr.Return,
        ),
        'loc_FB10',
    )

    Jump('loc_FB64')

    def _loc_FB10(): pass

    label('loc_FB10')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0006)"),
            Expr.Return,
        ),
        'loc_FB2C',
    )

    Jump('loc_FB64')

    def _loc_FB2C(): pass

    label('loc_FB2C')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x0008)"),
            Expr.Return,
        ),
        'loc_FB48',
    )

    Jump('loc_FB64')

    def _loc_FB48(): pass

    label('loc_FB48')

    If(
        (
            (Expr.Eval, "ModelCmd(0x39, 0x000F)"),
            Expr.Return,
        ),
        'loc_FB64',
    )

    Jump('loc_FB64')

    def _loc_FB64(): pass

    label('loc_FB64')

    Return()

# id: 0x004F offset: 0xFB68
@scena.Code('AniBikeWait')
def AniBikeWait():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FBC3',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_FBC3(): pass

    label('loc_FBC3')

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xFC08
@scena.Code('AniBikeWaitLeft')
def AniBikeWaitLeft():
    ExecExpressionWithReg(
        0x08,
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

# id: 0x0051 offset: 0xFC60
@scena.Code('AniBikeRun')
def AniBikeRun():
    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0052 offset: 0xFCB4
@scena.Code('AniBikeTilt')
def AniBikeTilt():
    ExecExpressionWithReg(
        0x08,
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

# id: 0x0053 offset: 0xFD08
@scena.Code('AniBikeTiltR')
def AniBikeTiltR():
    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0054 offset: 0xFD60
@scena.Code('AniBikeTiltL')
def AniBikeTiltL():
    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0xFDB8
@scena.Code('AniBikeBack')
def AniBikeBack():
    Call(ScriptId.Current, 'SpringOff')

    ExecExpressionWithReg(
        0x08,
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

# id: 0x0056 offset: 0xFE48
@scena.Code('AniBikeHandleWait')
def AniBikeHandleWait():
    ExecExpressionWithReg(
        0x08,
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

# id: 0x0057 offset: 0xFEA4
@scena.Code('AniBikeHandle')
def AniBikeHandle():
    ExecExpressionWithReg(
        0x08,
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

# id: 0x0058 offset: 0xFEFC
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0059 offset: 0xFF38
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0xFF74
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x005B offset: 0xFFB8
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x005C offset: 0xFFF0
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x005D offset: 0x10028
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x005E offset: 0x10050
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10089',
    )

    Call(ScriptId.Current, 'AniAttachMainWeaponGun')

    Jump('loc_100A9')

    def _loc_10089(): pass

    label('loc_10089')

    Call(ScriptId.Current, 'AniAttachMainWeaponSword')

    def _loc_100A9(): pass

    label('loc_100A9')

    Return()

# id: 0x005F offset: 0x100AC
@scena.Code('AniAttachMainWeaponGun')
def AniAttachMainWeaponGun():
    Call(ScriptId.Current, 'AniDetachMainWeaponSword')
    Call(ScriptId.Current, 'AniDetachMainWeaponGun')
    LoadAsset('C_EQU082_R')
    LoadAsset('C_EQU082_L')
    AttachEquip(0xFFFE, 'C_EQU082_R', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AttachEquip(0xFFFE, 'C_EQU082_L', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0060 offset: 0x1021C
@scena.Code('AniAttachMainWeaponSword')
def AniAttachMainWeaponSword():
    Call(ScriptId.Current, 'AniDetachMainWeaponSword')
    Call(ScriptId.Current, 'AniDetachMainWeaponGun')
    LoadAsset('C_EQU104')
    AttachEquip(0xFFFE, 'C_EQU104', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0061 offset: 0x10308
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10341',
    )

    Call(ScriptId.Current, 'AniDetachMainWeaponGun')

    Jump('loc_10361')

    def _loc_10341(): pass

    label('loc_10341')

    Call(ScriptId.Current, 'AniDetachMainWeaponSword')

    def _loc_10361(): pass

    label('loc_10361')

    Return()

# id: 0x0062 offset: 0x10364
@scena.Code('AniDetachMainWeaponGun')
def AniDetachMainWeaponGun():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU082_R')
    ReleaseAsset('C_EQU082_L')

    Return()

# id: 0x0063 offset: 0x103FC
@scena.Code('AniDetachMainWeaponSword')
def AniDetachMainWeaponSword():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU104')

    Return()

# id: 0x0064 offset: 0x10480
@scena.Code('AniAttachEQU321')
def AniAttachEQU321():
    LoadAsset('C_EQU321')
    AttachEquip(0xFFFE, 'C_EQU321', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0065 offset: 0x10518
@scena.Code('AniDetachEQU321')
def AniDetachEQU321():
    ReleaseAsset('C_EQU321')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0066 offset: 0x1056C
@scena.Code('AniFishWait')
def AniFishWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'wait', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0067 offset: 0x105C0
@scena.Code('AniFishStart')
def AniFishStart():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_START', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'start', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(830)

    OP_3B(0x00, ParamInt(0x3015), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(20)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'wait', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0068 offset: 0x106D8
@scena.Code('AniFishHit')
def AniFishHit():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_HIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0069 offset: 0x1072C
@scena.Code('AniFishHit2')
def AniFishHit2():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_HIT2', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'hit', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x006A offset: 0x10780
@scena.Code('AniFishEnd')
def AniFishEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'up', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_ENDa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'end', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x006B offset: 0x10830
@scena.Code('AniFishResult')
def AniFishResult():
    SetChrFace(0x03, PseudoChrId.Self, '', '', '[autoB0]', '#b', '0')
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)
    OP_45(PseudoChrId.Self, -10.0, 0.0, 0.0, 0x00C8, 0x0000)
    SetEndhookFunction('DefaultFace', 0x000B)
    LoadEffect(0xFFFE, 0x3E, 'minigame/mini01_7.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x00000001, ParamStr('R_hand_point:NODE_ITO'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    SetEndhookFunction('AniFishResult_sub', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_RESULT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.15, 0xFFFFFFFF)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'end', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '0#46w1#66w0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_RESULTa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'end', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006C offset: 0x10A4C
@scena.Code('AniFishResult_sub')
def AniFishResult_sub():
    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    ReleaseEffect(0xFFFE, 0x3E)

    Return()

# id: 0x006D offset: 0x10A60
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x006E offset: 0x10A8C
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'AniSetWeaponMode')
    Call(ScriptId.Current, 'AniAttachMainWeapon')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10B7F',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B2B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_10B54')

    def _loc_10B2B(): pass

    label('loc_10B2B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_10B54(): pass

    label('loc_10B54')

    ReleaseEffect(0xFFFE, 0x20)
    LoadEffect(0xFFFE, 0x20, 'battle/moncharge.eff', 0x00000000)

    def _loc_10B7F(): pass

    label('loc_10B7F')

    ReleaseEffect(0xFFFE, 0x27)
    Call(ScriptId.Current, 'PlayFakeEffect')
    Call(ScriptId.BtlCom, 'AniBtlInit')

    If(
        (
            (Expr.Eval, "BattleCmd(0x9E, 0xFFFE, 'chr028_c70_i')"),
            Expr.Return,
        ),
        'loc_10C64',
    )

    LoadAsset('C_EQU310')
    AttachEquip(0xFFFE, 'C_EQU310', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)
    OP_76(PseudoChrId.Self, 'megane_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_10C64(): pass

    label('loc_10C64')

    Return()

# id: 0x006F offset: 0x10C68
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_10C84',
    )

    Return()

    def _loc_10C84(): pass

    label('loc_10C84')

    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0070 offset: 0x10C94
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0071 offset: 0x10CAC
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_10CCD',
    )

    Return()

    def _loc_10CCD(): pass

    label('loc_10CCD')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_10D7D',
    )

    ChrSetPhysicsFlags(0x0BCC, 0x00000080)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x132),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10D59',
    )

    OP_3B(0x32, ParamInt(0x1BDD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10D59(): pass

    label('loc_10D59')

    Sleep(1000)

    OP_3B(0x39, 0xFFFE)
    ChrClearPhysicsFlags(0x0BCC, 0x00000080)

    Jump('loc_10FC7')

    def _loc_10D7D(): pass

    label('loc_10D7D')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10DF3',
    )

    OP_3B(0x32, ParamInt(0x1B86), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10FC7')

    def _loc_10DF3(): pass

    label('loc_10DF3')

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
        'loc_10E87',
    )

    OP_3B(0x32, ParamInt(0x1B85), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10FC7')

    def _loc_10E87(): pass

    label('loc_10E87')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10EFD',
    )

    OP_3B(0x32, ParamInt(0x1B88), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10FC7')

    def _loc_10EFD(): pass

    label('loc_10EFD')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10F72',
    )

    OP_3B(0x32, ParamInt(0x1B83), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10FC7')

    def _loc_10F72(): pass

    label('loc_10F72')

    OP_3B(0x32, ParamInt(0x1B84), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10FC7(): pass

    label('loc_10FC7')

    Return()

# id: 0x0072 offset: 0x10FC8
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_11005',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5B), ParamInt(0x1B5C), ParamInt(0), ParamInt(0))

    Jump('loc_11025')

    def _loc_11005(): pass

    label('loc_11005')

    OP_3B(0x3A, 0xFFFE, ParamInt(7000), ParamInt(0x1B59), ParamInt(0x1B5A), ParamInt(0))

    def _loc_11025(): pass

    label('loc_11025')

    Return()

# id: 0x0073 offset: 0x11028
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_11065',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5B), ParamInt(0x1B5C), ParamInt(0), ParamInt(0))

    Jump('loc_11085')

    def _loc_11065(): pass

    label('loc_11065')

    OP_3B(0x3A, 0xFFFE, ParamInt(7000), ParamInt(0x1B59), ParamInt(0x1B5A), ParamInt(0))

    def _loc_11085(): pass

    label('loc_11085')

    Return()

# id: 0x0074 offset: 0x11088
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x1B87), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0075 offset: 0x110E0
@scena.Code('AniBtlGetChrId')
def AniBtlGetChrId():
    ModelCmd(0x38, 0x01, 0x00000017)

    Return()

# id: 0x0076 offset: 0x110EC
@scena.Code('AniAttachEqu348')
def AniAttachEqu348():
    LoadAsset('C_EQU348')
    AttachEquip(0xFFFE, 'C_EQU348', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0077 offset: 0x11158
@scena.Code('AniDetachEqu348')
def AniDetachEqu348():
    ReleaseAsset('C_EQU348')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0078 offset: 0x111AC
@scena.Code('AniBtlWait')
def AniBtlWait():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_1120F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_112A2')

    def _loc_1120F(): pass

    label('loc_1120F')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11266',
    )

    Call(ScriptId.Current, 'ShowEquip_S')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_112A2')

    def _loc_11266(): pass

    label('loc_11266')

    Call(ScriptId.Current, 'ShowEquip_G')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_112A2(): pass

    label('loc_112A2')

    Return()

# id: 0x0079 offset: 0x112A4
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1137E',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1134C',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_11375')

    def _loc_1134C(): pass

    label('loc_1134C')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_11375(): pass

    label('loc_11375')

    Jump('loc_11403')

    def _loc_1137E(): pass

    label('loc_1137E')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_113DA',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_11403')

    def _loc_113DA(): pass

    label('loc_113DA')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_11403(): pass

    label('loc_11403')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')

    Return()

# id: 0x007A offset: 0x1141C
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1146A',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_114AF')

    def _loc_1146A(): pass

    label('loc_1146A')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_114AF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_114AF(): pass

    label('loc_114AF')

    Return()

# id: 0x007B offset: 0x114B0
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x1B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007C offset: 0x11508
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x1B81), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007D offset: 0x11560
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x1B82), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007E offset: 0x115B8
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_116E4',
    )

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFF4, 0.0, -1.0)
    OP_3B(0x32, ParamInt(0x1B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 200, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, 0.25, 0x02, 0x10)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x34, ParamInt(0x1B7F))

    Jump('loc_117F5')

    def _loc_116E4(): pass

    label('loc_116E4')

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFF4, 0.0, -1.0)
    OP_3B(0x32, ParamInt(0x1B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 200, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, 0.25, 0x02, 0x10)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x34, ParamInt(0x1B7F))

    def _loc_117F5(): pass

    label('loc_117F5')

    Return()

# id: 0x007F offset: 0x117F8
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11940',
    )

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraCmd(0x03, 0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.1, 0.0, 0x012C)
    CameraSetDistance(0x03, 5.0, 300)
    CameraCmd(0x07, 0x00BF)
    OP_3B(0x32, ParamInt(0x1B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    Sleep(30)

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.4, -2.5, 0.35, 0x01, 0x10)
    OP_3B(0x34, ParamInt(0x1B7E))

    Jump('loc_11A6D')

    def _loc_11940(): pass

    label('loc_11940')

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraCmd(0x03, 0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.1, 0.0, 0x012C)
    CameraSetDistance(0x03, 5.0, 300)
    CameraCmd(0x07, 0x00BF)
    OP_3B(0x32, ParamInt(0x1B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    Sleep(30)

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.4, -2.5, 0.35, 0x01, 0x10)
    OP_3B(0x34, ParamInt(0x1B7E))

    def _loc_11A6D(): pass

    label('loc_11A6D')

    Return()

# id: 0x0080 offset: 0x11A70
@scena.Code('AniBtlStepInKisinFace')
def AniBtlStepInKisinFace():
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0081 offset: 0x11A9C
@scena.Code('AniBtlStepInKisinPt')
def AniBtlStepInKisinPt():
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x1B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0082 offset: 0x11B20
@scena.Code('AniBtlStepOutKisinPt')
def AniBtlStepOutKisinPt():
    Return()

# id: 0x0083 offset: 0x11B24
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EDF',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11BC4',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_11BED')

    def _loc_11BC4(): pass

    label('loc_11BC4')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_11BED(): pass

    label('loc_11BED')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(733)

    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(30)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11D43',
    )

    Call(ScriptId.Current, 'AniPlayVoiceRandom_PLAYER', ParamInt(0x1B5D), ParamInt(0x1B5E), ParamInt(0x1B5F), ParamInt(0))
    Call(ScriptId.Current, 'AniPlayVoiceRandom_SHADOW', ParamInt(0), ParamInt(0), ParamInt(0), ParamInt(0))

    def _loc_11D43(): pass

    label('loc_11D43')

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.22), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(66)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_11E7F',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.4)

    def _loc_11E7F(): pass

    label('loc_11E7F')

    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_122BE')

    def _loc_11EDF(): pass

    label('loc_11EDF')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11F3B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_11F64')

    def _loc_11F3B(): pass

    label('loc_11F3B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_11F64(): pass

    label('loc_11F64')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(566)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1205E',
    )

    Call(ScriptId.Current, 'AniPlayVoiceRandom_PLAYER', ParamInt(0x1B5D), ParamInt(0x1B5E), ParamInt(0x1B60), ParamInt(0))
    Call(ScriptId.Current, 'AniPlayVoiceRandom_SHADOW', ParamInt(0), ParamInt(0), ParamInt(0), ParamInt(0))

    def _loc_1205E(): pass

    label('loc_1205E')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(66)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(66)

    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_122BE(): pass

    label('loc_122BE')

    Return()

# id: 0x0084 offset: 0x122C0
@scena.StyleName('StyleName0')
def StyleName0():
    return ScenaStyleName('Saber Mode', 'Saber Mode')

# id: 0x0085 offset: 0x12344
@scena.StyleName('StyleName1')
def StyleName1():
    return ScenaStyleName('Gunner Mode', 'Gunner Mode')

# id: 0x0086 offset: 0x123C8
@scena.Code('AniBtlChangeStyle')
def AniBtlChangeStyle():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1279B',
    )

    If(
        (
            (Expr.Eval, "ModelGetBattleStyle(0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_125C7',
    )

    ModelSetBattleStyle(0xFFFE, 0x0001)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAB))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAC))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1.5), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12792')

    def _loc_125C7(): pass

    label('loc_125C7')

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ModelSetBattleStyle(0xFFFE, 0x0000)
    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAB))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAD))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1.5), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12792(): pass

    label('loc_12792')

    Jump('loc_12C4F')

    def _loc_1279B(): pass

    label('loc_1279B')

    If(
        (
            (Expr.Eval, "ModelGetBattleStyle(0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12A0A',
    )

    ModelSetBattleStyle(0xFFFE, 0x0001)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAB))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    Sleep(533)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAC))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(-0.02), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1.5), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F81), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(300), ParamInt(0x0096), 0x0000, 0x012C, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12C4F')

    def _loc_12A0A(): pass

    label('loc_12A0A')

    ModelSetBattleStyle(0xFFFE, 0x0000)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAB))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(-0.02), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x7577), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1.5), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F81), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(300), ParamInt(0x0096), 0x0000, 0x012C, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    Sleep(166)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1BAD))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_12C4F(): pass

    label('loc_12C4F')

    Return()

# id: 0x0087 offset: 0x12C50
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B7B))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0088 offset: 0x12CA8
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D5D',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12D1D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12D48')

    def _loc_12D1D(): pass

    label('loc_12D1D')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12D48(): pass

    label('loc_12D48')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12DE5')

    def _loc_12D5D(): pass

    label('loc_12D5D')

    If(
        (
            (Expr.Eval, "BattleCmd(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12DAE',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12DD9')

    def _loc_12DAE(): pass

    label('loc_12DAE')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12DD9(): pass

    label('loc_12DD9')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_12DE5(): pass

    label('loc_12DE5')

    Return()

# id: 0x0089 offset: 0x12DE8
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_12E5A',
    )

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B79))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    Jump('loc_12ECC')

    def _loc_12E5A(): pass

    label('loc_12E5A')

    Call(ScriptId.Current, 'AniPlayVoiceRandom_PLAYER', ParamInt(0x1B77), ParamInt(0x1B78), ParamInt(0), ParamInt(0))
    Call(ScriptId.Current, 'AniPlayVoiceRandom_SHADOW', ParamInt(0), ParamInt(0), ParamInt(0), ParamInt(0))

    def _loc_12ECC(): pass

    label('loc_12ECC')

    Return()

# id: 0x008A offset: 0x12ED0
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B79))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    Return()

# id: 0x008B offset: 0x12F14
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12FFB',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12F8A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12FF2')

    def _loc_12F8A(): pass

    label('loc_12F8A')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_12FF2(): pass

    label('loc_12FF2')

    Jump('loc_130B5')

    def _loc_12FFB(): pass

    label('loc_12FFB')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1304D',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_130B5')

    def _loc_1304D(): pass

    label('loc_1304D')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_130B5(): pass

    label('loc_130B5')

    Return()

# id: 0x008C offset: 0x130B8
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1311F',
    )

    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1316B')

    def _loc_1311F(): pass

    label('loc_1311F')

    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1316B(): pass

    label('loc_1316B')

    Return()

# id: 0x008D offset: 0x1316C
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x008E offset: 0x13188
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_13372',
    )

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13298',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_13259',
    )

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B7A))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    def _loc_13259(): pass

    label('loc_13259')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_13362')

    def _loc_13298(): pass

    label('loc_13298')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1332C',
    )

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B7A))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    def _loc_1332C(): pass

    label('loc_1332C')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_13362(): pass

    label('loc_13362')

    Sleep(500)

    Jump('loc_13503')

    def _loc_13372(): pass

    label('loc_13372')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13448',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_13409',
    )

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B7A))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    def _loc_13409(): pass

    label('loc_13409')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_13503')

    def _loc_13448(): pass

    label('loc_13448')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_134CD',
    )

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B7A))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))

    def _loc_134CD(): pass

    label('loc_134CD')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_13503(): pass

    label('loc_13503')

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x008F offset: 0x1350C
@scena.Code('AniBtlAria')
def AniBtlAria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13570',
    )

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x1B73), ParamInt(0x1B73), ParamFloat(-1), ParamFloat(0))

    Jump('loc_135ED')

    def _loc_13570(): pass

    label('loc_13570')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_135C3',
    )

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0), ParamInt(0), ParamFloat(-1), ParamFloat(0))

    Jump('loc_135ED')

    def _loc_135C3(): pass

    label('loc_135C3')

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x1B73), ParamInt(0x1B74), ParamFloat(-1), ParamFloat(0))

    def _loc_135ED(): pass

    label('loc_135ED')

    Return()

# id: 0x0090 offset: 0x135F0
@scena.Code('AniBtlArts')
def AniBtlArts():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x4B, 0x00FA, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoiceRandom_PLAYER', ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    Call(ScriptId.Current, 'AniPlayVoiceRandom_SHADOW', ParamInt(0), ParamInt(0), ParamInt(0), ParamInt(0))
    Sleep(600)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_76(PseudoChrId.Self, 'R_hand_point', 'open', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_138A9',
    )

    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'btlartsb_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1392A')

    def _loc_138A9(): pass

    label('loc_138A9')

    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'btlartsb_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1392A(): pass

    label('loc_1392A')

    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x0091 offset: 0x13938
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13B2C',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_13A03',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)

    Jump('loc_13B23')

    def _loc_13A03(): pass

    label('loc_13A03')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    OP_3B(0x00, ParamInt(0x0FD5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(1000)

    def _loc_13B23(): pass

    label('loc_13B23')

    Jump('loc_13D05')

    def _loc_13B2C(): pass

    label('loc_13B2C')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_13BE5',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)

    Jump('loc_13D05')

    def _loc_13BE5(): pass

    label('loc_13BE5')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    OP_3B(0x00, ParamInt(0x0FD5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(1000)

    def _loc_13D05(): pass

    label('loc_13D05')

    Return()

# id: 0x0092 offset: 0x13D08
@scena.Code('AniBtlItem')
def AniBtlItem():
    BattleTargetsIterReset(0xFF, 0xFFFE)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13F82',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13DA7',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_13DD0')

    def _loc_13DA7(): pass

    label('loc_13DA7')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_13DD0(): pass

    label('loc_13DD0')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    Sleep(466)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)

    Jump('loc_141E5')

    def _loc_13F82(): pass

    label('loc_13F82')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13FDE',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_14007')

    def _loc_13FDE(): pass

    label('loc_13FDE')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_14007(): pass

    label('loc_14007')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Sleep(466)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Call(ScriptId.Current, 'BtlDefaultFace')
    Sleep(800)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)

    def _loc_141E5(): pass

    label('loc_141E5')

    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x0093 offset: 0x141F0
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    BattleCmd(0x6B, 0x0000)
    BattleCmd(0x47)
    OP_43(0x00, 300, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    ChrSetPhysicsFlags(0xFFF8, 0x00000040)
    ChrSetPhysicsFlags(0xFFF8, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1428A',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_142B3')

    def _loc_1428A(): pass

    label('loc_1428A')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_142B3(): pass

    label('loc_142B3')

    Call(ScriptId.CurrentCharacter, 'BtlDefaultFace')
    Sleep(200)

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_CENTER', 0.01, 0.2, 0.05, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -22.0, 6.0, 5.0, 0, 0x01)
    CameraRotateByTarget(0xFFFE, '', 0x02, -5.0, -23.0, 5.0, 10000, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraSetDistance(0x02, 2.0, 10000)
    OP_43(0x64, 300, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    Call(ScriptId.CurrentCharacter, 'AniBtlBluffVoice')
    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    ChrClearPhysicsFlags(0xFFF8, 0x00000040)
    ChrClearPhysicsFlags(0xFFF8, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x6C, 0x0000)

    Return()

# id: 0x0094 offset: 0x143C0
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, ParamInt(0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0095 offset: 0x14428
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B8E), ParamInt(0x1B8F), ParamInt(0), ParamInt(0))

    Return()

# id: 0x0096 offset: 0x1444C
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleCmd(0x6B, 0x0000)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF8, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    Call(ScriptId.CurrentCharacter, 'BtlDefaultFace')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_144E8',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_14511')

    def _loc_144E8(): pass

    label('loc_144E8')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_14511(): pass

    label('loc_14511')

    Sleep(0)

    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', -0.09, -0.2, -0.05, 0)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1457E',
    )

    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, -18.0, 0.0, 0, 0x01)

    Jump('loc_14597')

    def _loc_1457E(): pass

    label('loc_1457E')

    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, 18.0, 0.0, 0, 0x01)

    def _loc_14597(): pass

    label('loc_14597')

    CameraSetDistance(0x03, 4.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', -0.09, -0.2, -0.05, 3000)
    CameraSetDistance(0x03, 2.34, 3000)
    CameraCmd(0x0B, 0x03, 40.0, 0x0BB8)
    BattleCmd(0x4B, 0x0000, 0x03)
    Sleep(500)

    OP_3B(0x32, ParamInt(0x1BDE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x1BDE))
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 300, 0x03)
    OP_3B(0x00, ParamInt(0x8B81), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000200)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleCmd(0x47)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14732',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)

    Jump('loc_1475F')

    def _loc_14732(): pass

    label('loc_14732')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)

    def _loc_1475F(): pass

    label('loc_1475F')

    Sleep(66)

    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.5, -2.0, 0.3, 0x02, 0x10)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000200)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000200)
    BattleSetChrPos(0xFFFE, 0xFFF4, 10000.0, 0.0, 0.0, -1.0, 0x00, 0x10)
    BattleDamage(0xFFFE, 0xFFFE, 0x64, 0x00)
    ChrClearPhysicsFlags(0xFFF8, 0x00000040)
    BattleCmd(0x6C, 0x0000)

    Return()

# id: 0x0097 offset: 0x147D8
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    Call(ScriptId.Current, 'AniBtlWaitInit', ParamInt(0))
    CameraCmd(0x0A, 0.015, 0.012, 0.0, 500, 1000, 500, 0, 0, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00020103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x02)
    OP_3B(0x00, ParamInt(0x0FD5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x014D), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F5A), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    BattleDamage(0xFFFE, 0xFFFE, 0x64, 0x00)
    Sleep(1000)

    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x0098 offset: 0x149F0
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15226',
    )

    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(400)

    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(30)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14BFA',
    )

    OP_3B(0x32, ParamInt(0x1BA4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14D66')

    def _loc_14BFA(): pass

    label('loc_14BFA')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C71',
    )

    OP_3B(0x32, ParamInt(0x1BA6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14D66')

    def _loc_14C71(): pass

    label('loc_14C71')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14CE8',
    )

    OP_3B(0x32, ParamInt(0x1BA6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14D66')

    def _loc_14CE8(): pass

    label('loc_14CE8')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_14D11',
    )

    Jump('loc_14D66')

    def _loc_14D11(): pass

    label('loc_14D11')

    OP_3B(0x32, ParamInt(0x1B90), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_14D66(): pass

    label('loc_14D66')

    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.22), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14EE9',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_150CB')

    def _loc_14EE9(): pass

    label('loc_14EE9')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14FEB',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_150CB')

    def _loc_14FEB(): pass

    label('loc_14FEB')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_150CB(): pass

    label('loc_150CB')

    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(866)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(10)

    OP_3B(0x00, ParamInt(0x0FAE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(190)

    BattleCmd(0x3F, 0xFFFE)
    EffectCmd(0x12, 0xFFFE, 0x03FB)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Jump('loc_15AAC')

    def _loc_15226(): pass

    label('loc_15226')

    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(566)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_153C2',
    )

    OP_3B(0x32, ParamInt(0x1BA4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_15505')

    def _loc_153C2(): pass

    label('loc_153C2')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15439',
    )

    OP_3B(0x32, ParamInt(0x1BA6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_15505')

    def _loc_15439(): pass

    label('loc_15439')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_154B0',
    )

    OP_3B(0x32, ParamInt(0x1BA6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_15505')

    def _loc_154B0(): pass

    label('loc_154B0')

    OP_3B(0x32, ParamInt(0x1B90), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_15505(): pass

    label('loc_15505')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    Sleep(66)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(66)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15778',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_1595A')

    def _loc_15778(): pass

    label('loc_15778')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1587A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_1595A')

    def _loc_1587A(): pass

    label('loc_1587A')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_1595A(): pass

    label('loc_1595A')

    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(666)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(10)

    OP_3B(0x00, ParamInt(0x0FAE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(190)

    BattleCmd(0x3F, 0xFFFE)
    EffectCmd(0x12, 0xFFFE, 0x03FA)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    def _loc_15AAC(): pass

    label('loc_15AAC')

    Return()

# id: 0x0099 offset: 0x15AB0
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15B0E',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_15B37')

    def _loc_15B0E(): pass

    label('loc_15B0E')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_15B37(): pass

    label('loc_15B37')

    Return()

# id: 0x009A offset: 0x15B38
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15B7C',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_15BA5')

    def _loc_15B7C(): pass

    label('loc_15B7C')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_15BA5(): pass

    label('loc_15BA5')

    Return()

# id: 0x009B offset: 0x15BA8
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0xFF, 0xFFFE)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlBurstWait')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15E18',
    )

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -1.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(733)

    Sleep(30)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_15D2A',
    )

    Jump('loc_15D4A')

    def _loc_15D2A(): pass

    label('loc_15D2A')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1BF0), ParamInt(0x1BF2), ParamInt(0), ParamInt(0))

    def _loc_15D4A(): pass

    label('loc_15D4A')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.22), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(66)

    CreateThread(0xFFFF, 0x05, 'SE_LINK_C028_1', ScriptId.Sound)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FB), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0x8BF0), ParamFloat(0.5), ParamFloat(0))

    Jump('loc_160D8')

    def _loc_15E18(): pass

    label('loc_15E18')

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(566)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_15F1C',
    )

    Jump('loc_15F3C')

    def _loc_15F1C(): pass

    label('loc_15F1C')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1BF1), ParamInt(0x1BEF), ParamInt(0), ParamInt(0))

    def _loc_15F3C(): pass

    label('loc_15F3C')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    Sleep(66)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(66)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    def _loc_160D8(): pass

    label('loc_160D8')

    Sleep(666)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16127',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)

    Jump('loc_16154')

    def _loc_16127(): pass

    label('loc_16127')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)

    def _loc_16154(): pass

    label('loc_16154')

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009C offset: 0x161C8
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x009D offset: 0x161E0
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x009E offset: 0x161F8
@scena.Code('AniBtlLinkQuickCharge')
def AniBtlLinkQuickCharge():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x1BA5), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x009F offset: 0x16224
@scena.Code('AniBtlLinkCounter')
def AniBtlLinkCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x00A0 offset: 0x1623C
@scena.Code('AniBtlLinkQuickCharge2')
def AniBtlLinkQuickCharge2():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x1BA5), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x00A1 offset: 0x16268
@scena.Code('AniBtlLinkRageCounter')
def AniBtlLinkRageCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x00A2 offset: 0x16280
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x00A3 offset: 0x162A0
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x00A4 offset: 0x162BC
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16321',
    )

    SetChrFace(0x03, PseudoChrId.Self, '777776', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_16382')

    def _loc_16321(): pass

    label('loc_16321')

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '777776', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_16382(): pass

    label('loc_16382')

    Return()

# id: 0x00A5 offset: 0x16384
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_163F5',
    )

    OP_3B(0x32, ParamInt(0x1B72), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1644A')

    def _loc_163F5(): pass

    label('loc_163F5')

    OP_3B(0x32, ParamInt(0x1B71), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1644A(): pass

    label('loc_1644A')

    Return()

# id: 0x00A6 offset: 0x1644C
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x00A7 offset: 0x164A8
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16502',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1652B')

    def _loc_16502(): pass

    label('loc_16502')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1652B(): pass

    label('loc_1652B')

    Return()

# id: 0x00A8 offset: 0x1652C
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16570',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_16599')

    def _loc_16570(): pass

    label('loc_16570')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_16599(): pass

    label('loc_16599')

    Return()

# id: 0x00A9 offset: 0x1659C
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x00AA offset: 0x165B4
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x00AB offset: 0x165EC
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantWait')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x07D9, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlValiantArts_Magic', ScriptId.BtlCom)
    Sleep(2000)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_167A2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_167D8')

    def _loc_167A2(): pass

    label('loc_167A2')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb_G', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_167D8(): pass

    label('loc_167D8')

    WaitForThreadExit(PseudoChrId.Self, 0x03)

    Sleep(100)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x00AC offset: 0x16800
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x00AD offset: 0x1683C
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x00AE offset: 0x16874
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlValiantHeal_Arts_Endhook', ScriptId.Current)

    Return()

# id: 0x00AF offset: 0x168BC
@scena.Code('AniBtlValiantHeal_Arts_Endhook')
def AniBtlValiantHeal_Arts_Endhook():
    Sleep(3166)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x00B0 offset: 0x168DC
@scena.Code('AniBtlWaitInit')
def AniBtlWaitInit():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16910',
    )

    OP_80(0.0)

    Jump('loc_16919')

    def _loc_16910(): pass

    label('loc_16910')

    OP_80(0.2)

    def _loc_16919(): pass

    label('loc_16919')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1695D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_16986')

    def _loc_1695D(): pass

    label('loc_1695D')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_16986(): pass

    label('loc_16986')

    Return()

# id: 0x00B1 offset: 0x16988
@scena.Code('AniBtlKisinItemPa')
def AniBtlKisinItemPa():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B2 offset: 0x169EC
@scena.Code('AniBtlKisinChargePa')
def AniBtlKisinChargePa():
    OP_3B(0x32, ParamInt(0x1BE5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B3 offset: 0x16A84
@scena.Code('AniBtlKisinSinkiPa')
def AniBtlKisinSinkiPa():
    OP_3B(0x32, ParamInt(0x1BE6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B4 offset: 0x16B1C
@scena.Code('AniBtlKisinPartnerArts')
def AniBtlKisinPartnerArts():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B5 offset: 0x16B80
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B6 offset: 0x16BBC
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B7 offset: 0x16C20
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x00B8 offset: 0x16C5C
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B9 offset: 0x16C94
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
        'loc_16CD3',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16D08')

    def _loc_16CD3(): pass

    label('loc_16CD3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_16CFB',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_16D08')

    def _loc_16CFB(): pass

    label('loc_16CFB')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16D08(): pass

    label('loc_16D08')

    Return()

# id: 0x00BA offset: 0x16D0C
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16D7C',
    )

    OP_3B(0x32, ParamInt(0x1B8B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_16E41')

    def _loc_16D7C(): pass

    label('loc_16D7C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16DEC',
    )

    OP_3B(0x32, ParamInt(0x1B89), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_16E41')

    def _loc_16DEC(): pass

    label('loc_16DEC')

    OP_3B(0x32, ParamInt(0x1B8A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16E41(): pass

    label('loc_16E41')

    Return()

# id: 0x00BB offset: 0x16E44
@scena.Code('AniBtlWin')
def AniBtlWin():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.07, 1.49, -0.04, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 22.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.02, 1.46, 0.6, 2500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -8.0, 0.0, 2500, 0x01)
    CameraSetDistance(0x03, 1.6, 2500)
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1702B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 43.5333, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.95, 0xFFFFFFFF)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x753D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-7), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1066)

    OP_3B(0x00, ParamInt(0x7533), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    Sleep(833)

    Jump('loc_17130')

    def _loc_1702B(): pass

    label('loc_1702B')

    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    Sleep(1033)

    OP_3B(0x00, ParamInt(0x0FB6), ParamFloat(0.4), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_17130(): pass

    label('loc_17130')

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.02, 1.46, 0.03, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.0, 1.46, -0.05, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x02, 1.0, 17.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x02, 1.3, 3000)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'VoiceWin_select')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 126.667, 126.667, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '2[autoM2]', '3[autoB3]', '#b', '0')
    Sleep(150)

    Call(ScriptId.Current, 'VoiceWin_play')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_173A3',
    )

    SetChrFace(0x03, PseudoChrId.Self, '', '4[autoM4]', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'G1', '', '', '#b', '0')
    Sleep(770)

    SetChrFace(0x03, PseudoChrId.Self, '1G0', '', '0[autoB0]', '#b', '0')
    OP_46(0x02, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)
    Sleep(250)

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '4J54', '', '#b', '0')
    Sleep(300)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    Jump('loc_17491')

    def _loc_173A3(): pass

    label('loc_173A3')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17491',
    )

    SetChrFace(0x03, PseudoChrId.Self, '', '2[autoM2]', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'F3', '', '', '#b', '0')
    Sleep(770)

    SetChrFace(0x03, PseudoChrId.Self, '3F2', '', '0[autoB0]', '#b', '0')
    OP_46(0x02, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)
    Sleep(250)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    Sleep(300)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    Jump('loc_17491')

    def _loc_17491(): pass

    label('loc_17491')

    OP_3B(0x39, 0xFFFE)
    Sleep(1000)

    OP_43(0x65, 250, 1.0, 0)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, -1.0, 0x03)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.2, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17592',
    )

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '4[autoM4]', '0[autoB0]', '#b', '0')

    Jump('loc_175BD')

    def _loc_17592(): pass

    label('loc_17592')

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    def _loc_175BD(): pass

    label('loc_175BD')

    Sleep(1000)

    Return()

# id: 0x00BC offset: 0x175C8
@scena.Code('AniBtlWinBackknuckleL2')
def AniBtlWinBackknuckleL2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_L2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_L2a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BD offset: 0x1764C
@scena.Code('AniBtlWinBackknuckleL2b')
def AniBtlWinBackknuckleL2b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_L2b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    OP_3B(0x00, ParamInt(0x10B0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00BE offset: 0x17710
@scena.Code('AniBtlWinBackknuckleR')
def AniBtlWinBackknuckleR():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00BF offset: 0x17774
@scena.Code('AniBtlWinChiesL')
def AniBtlWinChiesL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_CHIES_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_CHIES_La', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C0 offset: 0x177EC
@scena.Code('AniBtlWinEnd')
def AniBtlWinEnd():
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'AniDetachEqu348')

    Return()

# id: 0x00C1 offset: 0x17818
@scena.Code('AniBtlWinGjL')
def AniBtlWinGjL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_GJ_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_GJ_La', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C2 offset: 0x17888
@scena.Code('AniBtlWinKnuckleL2')
def AniBtlWinKnuckleL2():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KNUCKLE_L2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KNUCKLE_L2a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C3 offset: 0x17910
@scena.Code('AniBtlWinKnuckleL2b')
def AniBtlWinKnuckleL2b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KNUCKLE_L2b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00C4 offset: 0x17974
@scena.Code('AniBtlWinCrapbackL')
def AniBtlWinCrapbackL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_CRAPBACK_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(900)

    OP_3B(0x00, ParamInt(0x10B0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C5 offset: 0x17A10
@scena.Code('AniBtlWinKnuckleR2')
def AniBtlWinKnuckleR2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KNUCKLE_R2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00C6 offset: 0x17A74
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetChrFace(0x03, PseudoChrId.Self, '0', 'A', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '0', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C7 offset: 0x17B60
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, ParamInt(0x1B8C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '', '4[autoM4]', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'G1', '', '', '#b', '0')
    Sleep(770)

    SetChrFace(0x03, PseudoChrId.Self, '1G0', '', '0[autoB0]', '#b', '0')
    Sleep(250)

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '4[autoM4]', '0[autoB0]', '#b', '0')
    OP_3B(0x34, ParamInt(0x1B8C))

    Return()

# id: 0x00C8 offset: 0x17CE0
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvRyoteAtama', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(PseudoChrId.Self, 0x01, 'AniEvRyoteAtama', -1.0, 1.0, 0x00000000)
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x00C9 offset: 0x17D74
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x00CA offset: 0x17D80
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17DFD',
    )

    Call(ScriptId.Current, 'ShowEquip_S')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_17E39')

    def _loc_17DFD(): pass

    label('loc_17DFD')

    Call(ScriptId.Current, 'ShowEquip_G')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_17E39(): pass

    label('loc_17E39')

    Return()

# id: 0x00CB offset: 0x17E3C
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0', '0[autoM0]', '', '#b', '0')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17F89',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 43.5333, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.95, 0xFFFFFFFF)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x753D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-7), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1066)

    OP_3B(0x00, ParamInt(0x7533), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')

    Jump('loc_18082')

    def _loc_17F89(): pass

    label('loc_17F89')

    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    Sleep(1033)

    OP_3B(0x00, ParamInt(0x0FB6), ParamFloat(0.4), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'EraseEquip')

    def _loc_18082(): pass

    label('loc_18082')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x00CC offset: 0x180D8
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00CD offset: 0x180FC
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_18169',
    )

    OP_3B(0x32, ParamInt(0x1B8D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_18169')

    def _loc_18169(): pass

    label('loc_18169')

    Return()

# id: 0x00CE offset: 0x1816C
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtLevelUp_Call', ScriptId.Current)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.25, 0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x11, 0x03, 5.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_3B(0x32, ParamInt(0x1B8D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, 'F1', '', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'F2', '13030134', '', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '4[autoM4]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x00CF offset: 0x1839C
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr028_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr028_00_1.eff', 0x00000000)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'AniBtlMove')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 10.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.25, -0.3, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -25.0, -6.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.25, 0.5, 1000)
    CameraCmd(0x11, 0x03, 0.0, 6.0, 0.0, 0x03E8, 0x01)
    CameraSetHeight(0x03, -0.25, 1000)
    BattleCmd(0x4B, 0x03E8, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8F6B), ParamFloat(0.8), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(4100), ParamFloat(2), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(175)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B64))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(125)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_5E(0x00, 0x0004, 0.5, 50, 300, 200, 0.35, 0xFFFE, '', 0.0, 1.15, 0.6)
    Sleep(500)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.45, 1.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.0, 148.0, 10.0, 0, 0x01)
    CameraSetHeight(0x03, 2.6, 0)
    CameraCmd(0x11, 0x03, 0.0, 30.0, 0.0, 0x1F40, 0x01)
    CameraSetHeight(0x03, 0.5, 8000)
    BattleCmd(0x4B, 0x1F40, 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    CameraCmd(0x0A, 0.3, 0.25, 0.0, 100, 1400, 500, 0, 0, 0x00)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_5E(0x00, 0x0000, 0.4, 150, 1250, 800, 0.5, 0xF016, '', 0.0, 1.0, 0.0)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(250)

    TerminateThread(PseudoChrId.Self, 0x02)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(250)

    TerminateThread(PseudoChrId.Self, 0x02)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(250)

    TerminateThread(PseudoChrId.Self, 0x02)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(250)

    TerminateThread(PseudoChrId.Self, 0x02)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraftDamage', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.8, 0.3)
    Sleep(500)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x03, 0x00)
    Sleep(1000)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D0 offset: 0x18AAC
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr028_01_0a.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr028_01_1a.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr028_01_2a.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr028_01_3a.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/ryu2.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.55, -0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.0, -15.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.1, 1.725, 0.1, 1000)
    CameraCmd(0x11, 0x00, -1.0, -10.0, 0.0, 0x03E8, 0x01)
    CameraSetHeight(0x00, 0.2, 1000)
    BattleCmd(0x4B, 0x03E8, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2#36w3', '2[autoM2]', '0[autoB0]', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B62))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.005, 0.006, 0.002, 500, 2000, 1000, 0, 60, 0x00)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x1015), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.99, -0.0, 3000)
    CameraCmd(0x11, 0x03, -1.0, -10.0, 0.0, 0x0BB8, 0x01)
    CameraSetHeight(0x03, -0.2, 3000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0.01), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1067), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0xFF, 0.05, 0.05, 1.7)
    Sleep(1300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '332[autoE2]', '2[autoM2]', '3#36w0[autoB0]', '#b', '0')
    Sleep(150)

    OP_3B(0x00, ParamInt(0x1005), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 1.6, 0.7, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.0, -75.0, 6.0, 500, 0x01)
    Sleep(600)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.55, 1.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.0, -145.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 5.0, 0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 15.0, 15.0, -1.0, 0x00, 0x00)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 2.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B63))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(100)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-20), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x02)
    EffectSetRGBA(0xFFFE, 0x02, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x02000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    OP_3B(0x01, ParamInt(0x1067), ParamInt(1500), 0xFFFF)
    OP_3B(0x00, ParamInt(0x8F95), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x0104), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.7, 30, 100, 200, 0.2, 0xF016, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.2, 0.13, 0.01, 30, 400, 300, 0, 60, 0x00)
    Sleep(166)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft01Damage', ScriptId.Current)
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    Sleep(600)

    Sleep(500)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D1 offset: 0x19388
@scena.Code('AniBtlCraft01Damage')
def AniBtlCraft01Damage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x0033), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00D2 offset: 0x193D8
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr028_02_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr028_02_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr028_02_2.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.3, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.5, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraCmd(0x0C, 0x03, 0.14, 0.3, 0.0, 4000)
    CameraSetHeight(0x03, -0.65, 4000)
    CameraCmd(0x11, 0x03, 0.0, 10.0, 0.0, 0x0FA0, 0x01)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'HFJE1D292', '', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B66))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_3B(0x00, ParamInt(0x10BC), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FB4), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_HEAD'), ParamFloat(-0.035), ParamFloat(-0.013), ParamFloat(0.11), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    CameraCmd(0x0A, 0.01, 0.01, 0.001, 200, 1500, 1000, 0, 100, 0x00)
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '7', '6[autoM6]', '', '#b', '0')
    Sleep(1300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8F9A), ParamFloat(3), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(366)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.02, 1.62, 0.15, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 0.35, 0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    CameraCmd(0x1B, 0.01, -2.0)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B67))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_HEAD'), ParamFloat(-0.035), ParamFloat(-0.023), ParamFloat(0.1), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_5E(0x00, 0x0000, 0.7, 150, 250, 200, 0.2, 0xF016, '', 0.0, 1.5, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', 'B', '', '#b', '0')
    OP_5E(0x00, 0x0002, 0.3, 100, 1000, 1000, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.3, 0.6, 0.4)
    CameraSetHeight(0x03, 0.1, 4000)
    BattleCmd(0x4B, 0x0064, 0x03)
    Sleep(366)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    Sleep(266)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFF5, '', 0.0, 3.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, 175.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 9.0, 0)
    CameraSetPosByTarget(0x03, 0xFFF5, '', 0.0, 2.7, 0.0, 4000)
    CameraSetHeight(0x03, 2.0, 4000)
    CameraCmd(0x11, 0x03, 0.0, 40.0, 0.0, 0x0FA0, 0x01)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    CameraCmd(0x1B, -2.0, -2.0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FB8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.3, 0.6, 0.3)
    CameraCmd(0x0A, 0.1, 0.1, 0.0, 200, 500, 100, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.3, 200, 550, 200, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(750)

    OP_3B(0xFF, 0.45, 0.7, 0.6)
    CameraCmd(0x0A, 1.0, 1.0, 0.2, 400, 3000, 1000, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.6, 400, 3000, 1000, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x10C6), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F42), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1800), ParamInt(300), 0x0000, 0x0708, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(600)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.45, 0.7, 0.6)
    Sleep(600)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.45, 0.7, 0.6)
    Sleep(600)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleCmd(0x2E, 0xFFFE)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    OP_3B(0xFF, 0.45, 0.7, 0.6)
    Sleep(600)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleCmd(0x2F, 0xFFFE)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraftDamage', ScriptId.Current)
    OP_3B(0xFF, 0.45, 0.7, 0.3)
    Sleep(1000)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D3 offset: 0x19ED0
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle_sys/tensionup.eff', 0x00000000)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 25.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.14, 1.55, 0.3, 4000)
    CameraCmd(0x11, 0x03, -2.0, -10.0, 1.0, 0x0FA0, 0x01)
    CameraSetHeight(0x03, -1.25, 3000)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    CameraCmd(0x0A, 0.0, 0.002, 0.0, 500, 5000, 0, 1, 0, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3773', '2[autoM2]', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 500, 2000, 500, 0, 0, 0x00)
    Sleep(266)

    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    Sleep(400)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B68))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(600)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6662', '6[autoM6]', '0', '#b', '0')
    CameraCmd(0x0A, 0.2, 0.2, 0.0, 60, 400, 400, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.2, 60, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    CameraSetHeight(0x03, 1.0, 400)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.4, 0.2, 400)
    Sleep(33)

    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8F6B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(300)

    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    ReleaseEffect(0xFFFE, 0x30)
    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D4 offset: 0x1A41C
@scena.Code('AniBtlCraft05')
def AniBtlCraft05():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle_sys/tensionup.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle_sys/systension.eff', 0x00000000)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 25.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.14, 1.55, 0.3, 4000)
    CameraCmd(0x11, 0x03, -2.0, -10.0, 1.0, 0x0FA0, 0x01)
    CameraSetHeight(0x03, -1.25, 3000)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    CameraCmd(0x0A, 0.0, 0.002, 0.0, 500, 5000, 0, 1, 0, 0x00)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AC7B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_S', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3773', '2[autoM2]', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    EffectSetRGBA(0xFFFE, 0x03, 0.5, 0.5, 1.0, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x03, 0.0, 0.0, 1.5, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B68))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 500, 2000, 500, 0, 0, 0x00)
    Sleep(266)

    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    Sleep(400)

    Sleep(600)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '3', '6[autoM6]', '0', '#b', '0')
    CameraCmd(0x0A, 0.2, 0.2, 0.0, 60, 400, 400, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.2, 60, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    CameraSetHeight(0x03, 1.0, 400)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.4, 0.2, 400)
    Sleep(33)

    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    EffectSetRGBA(0xFFFE, 0x02, 0.5, 0.5, 1.0, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.0, 0.0, 2.0, 1.0, 0, 0x03)
    OP_3B(0x00, ParamInt(0x8F6B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 180.0, 0.0, ParamFloat(1), ParamFloat(0.5), ParamFloat(1), 0x07)
    EffectSetRGBA(0xFFFE, 0x04, 0.1, 0.3, 1.0, 0.8, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x04, 0.0, 0.0, 2.0, 0.8, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x07, 0.15, 0.3, 1.0, 0.8, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x07, 0.0, 0.0, 2.0, 0.8, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 45.0, 0.0, ParamFloat(3), ParamFloat(1), ParamFloat(3), 0x05)
    EffectSetRGBA(0xFFFE, 0x05, 0.3, 0.3, 1.0, 0.3, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x05, 0.0, 0.2, 2.0, 0.3, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, -60.0, 0.0, ParamFloat(5), ParamFloat(1), ParamFloat(5), 0x06)
    EffectSetRGBA(0xFFFE, 0x06, 0.3, 0.3, 1.0, 0.1, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x06, 0.2, 0.8, 2.0, 0.1, 0, 0x03)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    EffectSetRGBA(0xFFFE, 0x08, 0.5, 0.5, 1.0, 0.3, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x08, 0.0, 0.1, 2.0, 0.3, 0, 0x03)
    Sleep(66)

    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '32', '', '', '#b', '0')
    Sleep(333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    Jump('loc_1B327')

    def _loc_1AC7B(): pass

    label('loc_1AC7B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_G', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3773', '2[autoM2]', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    EffectSetRGBA(0xFFFE, 0x03, 0.5, 0.5, 1.0, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x03, 0.0, 0.0, 1.5, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B68))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 500, 2000, 500, 0, 0, 0x00)
    Sleep(266)

    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    Sleep(400)

    Sleep(600)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '3', '6[autoM6]', '0', '#b', '0')
    CameraCmd(0x0A, 0.2, 0.2, 0.0, 60, 400, 400, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.2, 60, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    CameraSetHeight(0x03, 1.0, 400)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.4, 0.2, 400)
    Sleep(33)

    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    EffectSetRGBA(0xFFFE, 0x02, 0.5, 0.5, 1.0, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x02, 0.0, 0.0, 2.0, 1.0, 0, 0x03)
    OP_3B(0x00, ParamInt(0x8F6B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 180.0, 0.0, ParamFloat(1), ParamFloat(0.5), ParamFloat(1), 0x07)
    EffectSetRGBA(0xFFFE, 0x04, 0.1, 0.3, 1.0, 0.8, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x04, 0.0, 0.0, 2.0, 0.8, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x07, 0.15, 0.3, 1.0, 0.8, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x07, 0.0, 0.0, 2.0, 0.8, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, 45.0, 0.0, ParamFloat(3), ParamFloat(1), ParamFloat(3), 0x05)
    EffectSetRGBA(0xFFFE, 0x05, 0.3, 0.3, 1.0, 0.3, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x05, 0.0, 0.2, 2.0, 0.3, 0, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.2), 0.0, -60.0, 0.0, ParamFloat(5), ParamFloat(1), ParamFloat(5), 0x06)
    EffectSetRGBA(0xFFFE, 0x06, 0.3, 0.3, 1.0, 0.1, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x06, 0.2, 0.8, 2.0, 0.1, 0, 0x03)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x04000000, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    EffectSetRGBA(0xFFFE, 0x08, 0.5, 0.5, 1.0, 0.3, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x08, 0.0, 0.1, 2.0, 0.3, 0, 0x03)
    Sleep(66)

    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '32', '', '', '#b', '0')
    Sleep(333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    def _loc_1B327(): pass

    label('loc_1B327')

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D5 offset: 0x1B380
@scena.Code('AniBtlCraft13')
def AniBtlCraft13():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr028_13_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr028_13_1.eff', 0x00000000)
    Call(ScriptId.Current, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.15, 0.2, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 20.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 4.0, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.18, 0.21, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 8.0, -3.0, 2000, 0x01)
    CameraSetDistance(0x03, 1.8, 2000)
    CameraCmd(0x0B, 0x03, 40.0, 0x07D0)
    BattleCmd(0x4B, 0x07D0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT13_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', 'A', '', '#b', '0')
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 180.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1063), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x104B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.009, 0.009, 3.0)
    Sleep(1100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    CameraRotateByTarget(0xFFFE, '', 0x03, 20.0, 8.0, -3.0, 300, 0x01)
    BattleCmd(0x4B, 0x012C, 0x03)
    Sleep(300)

    BattleCmd(0x47)
    CameraCmd(0x00)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.2, 6.0, 15.0)
    BattleCmd(0x4B, 0x00C8, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    CameraCmd(0x09, 0.01, 0.01, 3.0)
    OP_5E(0x00, 0x0002, 0.5, 0, 500, 250, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B65))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1043), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.325, 0.325, 0.85)
    Sleep(200)

    BattleCmd(0x47)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft13_Damage', ScriptId.Current)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.75, 12.0, 30.0)
    BattleCmd(0x4B, 0x03E8, 0x03)
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleCmd(0x0E, 0xFFFE, 0x0000, 0x00000000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    Call(ScriptId.Current, 'AniBtlCraftEnd')

    Return()

# id: 0x00D6 offset: 0x1B9EC
@scena.Code('AniBtlCraft13_Damage')
def AniBtlCraft13_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1B9FC(): pass

    label('loc_1B9FC')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1BAA0',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(100)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1B9FC')

    def _loc_1BAA0(): pass

    label('loc_1BAA0')

    BattleTargetsIterReset(0x00, 0xFFFE)

    Return()

# id: 0x00D7 offset: 0x1BAAC
@scena.Code('AniBtlCraftEnd')
def AniBtlCraftEnd():
    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BB26',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')

    Jump('loc_1BB6D')

    def _loc_1BB26(): pass

    label('loc_1BB26')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')

    def _loc_1BB6D(): pass

    label('loc_1BB6D')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x6C, 0x0000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    ChrClearPhysicsFlags(0xFFF8, 0x00000040)
    ChrClearPhysicsFlags(0xFFF8, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    OP_4A(0x01, 1.0, 1.0, 1.0, 1.0, 300, 0x03)
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.Sound, 'SFX_NONE')
    CameraCmd(0x17, 0x0010)

    Return()

# id: 0x00D8 offset: 0x1BC38
@scena.Code('AniBtlCraftDamage')
def AniBtlCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00D9 offset: 0x1BC88
@scena.Code('AniBtlCraft00_Damage')
def AniBtlCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1BC98(): pass

    label('loc_1BC98')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1BD30',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(50)

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1BC98')

    def _loc_1BD30(): pass

    label('loc_1BD30')

    BattleTargetsIterReset(0x00, 0xFFFE)

    Return()

# id: 0x00DA offset: 0x1BD3C
@scena.Code('AniBtlCraft04')
def AniBtlCraft04():
    Call(ScriptId.BtlCom, 'SET_MOVE_SPEED', ParamFloat(4))
    Call(ScriptId.BtlCom, 'AniBtlSummonKisin')
    LoadEffect(0xFFFE, 0x3A, 'battle/rs023_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/rs023_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/rs023_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/rs023_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/rs023_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3F, 'battle/rs023_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/rs023_00_8.eff', 0x00000000)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    SetChrPos(0x0B68, 0.0, 0.0, 0.0, 0.0)
    BattleTurnChrDirection(0x0B68, 0xFFFF, 0.0, -1.0)
    ModelCmd(0x24, 0x0B68)
    Call(ScriptId.BtlCom, 'AniBtlSummonKisinSetTargets', ParamInt(0x0002), ParamInt(0x00B4))
    OP_43(0x64, 1000, 1.0, 0)
    CameraCmd(0x00)

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_1C3F6',
    )

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK20', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(4400), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0x0B68, '', 0.0, 4.7, 0.0, 0)
    CameraRotateByTarget(0x0B68, '', 0x03, -21.0, 8.0, 1.0, 0, 0x01)
    CameraSetDistance(0x03, 5.4, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0x0B68, '', 0.0, 3.88, 0.0, 2000)
    CameraRotateByTarget(0x0B68, '', 0x03, -15.0, 15.0, 5.0, 2000, 0x01)
    CameraSetDistance(0x03, 9.4, 2000)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B68, 0x00000003, ParamStr('NODE_HEAD'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x7587), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1135), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(4400), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    Sleep(300)

    Sleep(666)

    OP_3B(0x00, ParamInt(4400), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    CameraSetPosByTarget(0x03, 0x0B68, '', 0.0, 3.65, 0.71, 2500)
    CameraRotateByTarget(0x0B68, '', 0x03, 6.0, 0.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x03, 6.0, 1500)
    Sleep(1000)

    OP_3B(0x00, ParamInt(0x1151), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1144), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(30)

    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(0x0B68, 0x00000020)
    Sleep(600)

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK22', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(60)

    CameraSetDistance(0x03, 13.0, 1000)
    Sleep(1000)

    Sleep(33)

    OP_5E(0x00, 0x0003, 1.0, 0, 10000, 0, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    BattleSetChrPosAsync(0x0B68, 0x0B68, 0.0, 0.0, 65.0, 17.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1148), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    Jump('loc_1C6CD')

    def _loc_1C3F6(): pass

    label('loc_1C3F6')

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK20', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, 102.0, 103.133, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(4400), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0x0B68, '', 0.0, 4.7, 0.0, 0)
    CameraRotateByTarget(0x0B68, '', 0x03, -21.0, 8.0, 1.0, 0, 0x01)
    CameraSetDistance(0x03, 5.4, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x02, 0x0B68, '', -2.1, 3.88, 0.5, 3000)
    CameraRotateByTarget(0x0B68, '', 0x02, -15.0, 40.0, 5.0, 3000, 0x01)
    CameraSetDistance(0x02, 9.4, 3000)
    Sleep(900)

    OP_3B(0x00, ParamInt(0x1135), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1144), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0x0B68, 0.0, 0x00)

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK22', 0x00, 0x01, 0x00, 0x00, 0x00, 1.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1100)

    CameraSetPosByTarget(0x03, 0x0B68, '', 0.77, 2.61, 0.09, 150)
    CameraRotateByTarget(0x0B68, '', 0x03, 0.0, 40.0, 3.0, 150, 0x01)
    CameraSetDistance(0x03, 12.4, 150)
    OP_5E(0x00, 0x0003, 1.0, 0, 10000, 0, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    BattleSetChrPosAsync(0x0B68, 0x0B68, 0.0, 0.0, 65.0, 17.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1148), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    def _loc_1C6CD(): pass

    label('loc_1C6CD')

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleSetChrPosAsync(0x0B68, 0x0B68, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    SetChrPos(0x0B68, 0.0, 0.0, -40.0, 0.0)
    BattleSetChrPosAsync(0x0B68, 0xFFFF, 0.0, 0.0, 0.0, 0.5, 0x00, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    ChrSetPhysicsFlags(0x0B68, 0x00000080)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000080)
    OP_5E(0x00, 0x0004, 1.0, 250, 10000, 250, 0.3, 0xFFFB, 'NODE_CENTER', 0.0, 0.0, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(4), ParamFloat(4), ParamFloat(4), 0xFF)
    OP_3B(0x00, ParamInt(0x114F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x00)
    CameraSetPos(0x03, -1.77, 3.48, -31.0, 0)
    CameraRotate(0x03, 351.0, 289.0, -30.0, 0, 0x01)
    CameraRotate(0x00, 2.0, 191.0, 20.0, 5000, 0x01)
    CameraSetDistance(0x03, 10.5, 0)
    CameraCmd(0x0B, 0x03, 70.7, 0x0000)
    Sleep(600)

    BattleSetChrPosAsync(0x0B68, 0x0B68, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleSetChrPosAsync(0x0B68, 0xFFFF, 0.0, 0.0, 30.0, 20.0, 0x03, 0x00)
    CameraSetPos(0x02, -1.18, 3.48, -4.92, 1000)
    CameraRotate(0x02, 2.0, 191.0, 20.0, 2000, 0x01)
    CameraSetDistance(0x02, 5.8, 1500)
    CameraCmd(0x0B, 0x03, 70.7, 0x0000)
    Sleep(400)

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1C92F(): pass

    label('loc_1C92F')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1CA39',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 30.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    OP_3B(0x00, ParamInt(0x1150), ParamFloat(0.76), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.5, 0.5, 0.0, 2500, 250, 100, 0, 0, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(50)

    Jump('loc_1C92F')

    def _loc_1CA39(): pass

    label('loc_1CA39')

    Sleep(900)

    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    OP_5E(0x01, 0x0000)
    BattleSetChrPosAsync(0x0B68, 0xFFFF, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    SetChrPos(0x0B68, -3.0, 0.0, 120.0, 180.0)
    BattleTurnChrDirection(0x0B68, 0xFFFF, 180.0, -1.0)
    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK21', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0x0B68, '', -1.0, 3.0, 8.0, 0)
    CameraRotate(0x03, 4.0, 225.0, -5.0, 0, 0x01)
    CameraSetDistance(0x03, 8.8, 0)
    CameraSetPosByTarget(0x03, 0x0B68, '', 0.0, 4.65, 3.0, 3000)
    CameraRotate(0x03, -4.0, 66.0, 4.0, 3000, 0x01)
    CameraSetDistance(0x03, 10.7, 3000)
    CameraCmd(0x0B, 0x03, 38.0, 0x0000)
    Sleep(200)

    Sleep(500)

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK23', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, 115.0, 117.1, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(4400), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0x0B68, 0x00000003, ParamStr('NODE_L_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1156), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0x0B68, 0.0, 0x00)

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK23', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, 117.133, 117.3, -1.0, 0x00, 0x00)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(3), ParamFloat(3), ParamFloat(3), 0xFF)
    CameraSetPosByTarget(0x02, 0x0B68, '', 0.0, 3.0, 4.5, 500)
    CameraRotate(0x02, 4.0, 19.0, -10.0, 500, 0x01)
    CameraSetDistance(0x02, 16.5, 500)
    Sleep(120)

    WaitAnimeClip(0x0B68, 0.0, 0x00)

    PlayChrAnimeClip(0x0B68, 'BTL_B1A_LINK23', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, 117.333, 120.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1144), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    OP_3B(0x00, ParamInt(0x114D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_4E(0.8, 0.0, 0x03, 0x00)
    Sleep(100)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_3B(0x00, ParamInt(0x1133), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x113B), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPos(0x03, 0.0, 3.0, 6.0, 1000)
    CameraRotate(0x03, 12.0, 48.0, -10.0, 1000, 0x01)
    CameraSetDistance(0x03, 20.0, 1000)
    Sleep(700)

    OP_3B(0x00, ParamInt(0x1155), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.55, 0.55, 3.0)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1CFCE(): pass

    label('loc_1CFCE')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1D066',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Sleep(50)

    Jump('loc_1CFCE')

    def _loc_1D066(): pass

    label('loc_1D066')

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(950)

    OP_4E(0.2, 0.0, 0x03, 0x00)
    OP_84(0x00, -0.65, -0.65, -0.65, 2.0)
    OP_3B(0x00, ParamInt(0x1157), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_84(0x01, 0.75, 0.75, 0.75, 0.0)
    OP_3B(0x00, ParamInt(0x10FA), ParamFloat(1), ParamInt(1000), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(150)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_84(0x02, 0.0, 0.0, 0.0, 0.0)
    OP_3B(0x00, ParamInt(0x1135), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x114E), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    OP_43(0x03, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x00FF)
    PlayChrAnimeClip(0x0B68, 'BTL_B1A_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrClearPhysicsFlags(0x0B68, 0x00000080)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000080)
    EffectCmd(0x0F, 0x0B68, 0x0022, 0x01)
    Call(ScriptId.BtlCom, 'RESET_MOVE_SPEED')
    Call(ScriptId.BtlCom, 'AniBtlSummonKisinEnd')

    Return()

# id: 0x00DB offset: 0x1D2E0
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR028_SC1')
    LoadEffect(0xFFFE, 0x30, 'battle/sc028_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/sc028_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc028_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc028_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc028_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc028_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc028_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc028_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc028_00_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc028_00_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc028_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc028_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc028_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc028_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc028_00_14.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_1D56B',
    )

    LoadEffect(0xFFFE, 0x3F, 'battle/cic028_9.eff', 0x00000000)

    Jump('loc_1D574')

    def _loc_1D56B(): pass

    label('loc_1D56B')

    BattleCmd(0x52, 0xFFFE, 0x3F)

    def _loc_1D574(): pass

    label('loc_1D574')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000200)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    ChrSetPhysicsFlags(0xFFF9, 0x00000200)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, -30.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    Sleep(1)

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1D6DC(): pass

    label('loc_1D6DC')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1D718',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFF, 180.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1D6DC')

    def _loc_1D718(): pass

    label('loc_1D718')

    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    OP_43(0x64, 1000, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.25, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 3000)
    CameraSetDistance(0x03, 2.5, 3000)
    SetChrFace(0x03, PseudoChrId.Self, '3', '2[autoM2]', '0', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00b', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B69))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.35), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0xFF)
    OP_3B(0x00, ParamInt(0x8F5A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F41), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1333)

    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.12, 1.35, 0.2, 500)
    CameraRotateByTarget(0xFFFE, '', 0x02, 0.0, 0.0, 0.0, 500, 0x01)
    CameraSetDistance(0x02, 5.5, 250)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000004, ParamStr(''), ParamFloat(3), ParamFloat(1.6), ParamFloat(0), 0.0, -90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000004, ParamStr(''), ParamFloat(-3), ParamFloat(1.6), ParamFloat(0), 0.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.8, 150, 250, 200, 1.0, 0xF016, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.25, 0.25, 0.0, 50, 100, 50, 0, 0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(250)

    CameraSetDistance(0x02, 6.0, 500)
    Sleep(333)

    Sleep(250)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6A))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '7', '', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000004, ParamStr(''), ParamFloat(3), ParamFloat(1.6), ParamFloat(0), 0.0, -90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000004, ParamStr(''), ParamFloat(-3), ParamFloat(1.6), ParamFloat(0), 0.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    OP_3B(0xFF, 0.5, 0.6, 2.8)
    CameraCmd(0x0A, 0.175, 0.175, 0.0, 2500, 250, 100, 0, 0, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.09, 1.36, 0.25, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, 49.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCmd(0x0B, 0x03, 39.4, 0x0000)
    CameraCmd(0x11, 0x03, 5.0, 10.0, 0.0, 0x03E8, 0x01)
    Sleep(1300)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.16, 1.26, 0.3, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, -50.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCmd(0x0B, 0x03, 45.7, 0x0000)
    CameraCmd(0x11, 0x03, -2.5, -5.0, 0.0, 0x03E8, 0x01)
    Sleep(1000)

    Sleep(450)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    StopEffect(0xFFFE, 0x07, 0x01)
    StopEffect(0xFFFE, 0x08, 0x01)
    StopEffect(0xFFFE, 0x09, 0x01)
    CameraSetPos(0x03, 7.7, 5.45, -7.0, 0)
    CameraRotate(0x03, 15.0, 135.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.0, 0)
    CameraCmd(0x0C, 0x03, -1.5, 0.1, 0.0, 3000)
    CameraCmd(0x11, 0x03, 5.0, 10.0, 0.0, 0x0BB8, 0x01)
    CameraSetDistance(0x03, 2.5, 3000)
    Sleep(500)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(6), ParamFloat(6), ParamFloat(0), 45.0, -90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(-6), ParamFloat(6), ParamFloat(0), 45.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFEA, '', 3.65, 8.2, -9.0, 1000)
    CameraRotate(0x03, 30.0, 155.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 6.5, 1000)
    CameraSetPosByTarget(0x03, 0xFFEA, '', -1.5, 3.0, -5.0, 3000)
    CameraCmd(0x11, 0x03, -15.0, 55.0, 0.0, 0x0BB8, 0x01)
    CameraSetDistance(0x03, 12.5, 2000)
    Sleep(500)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(6), ParamFloat(6), ParamFloat(0), 45.0, -90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(-6), ParamFloat(6), ParamFloat(0), 45.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    CameraCmd(0x0A, 0.25, 0.25, 0.0, 1500, 250, 100, 0, 0, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.25)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.25)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_3B(0xFF, 0.5, 0.7, 0.25)
    Sleep(300)

    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x37)
    OP_43(0x65, 500, 1.0, 0)
    OP_43(0xFE, 0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    StopEffect(0xFFFE, 0x0A, 0x01)
    StopEffect(0xFFFE, 0x0B, 0x01)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    StopEffect(0xFFFE, 0x07, 0x01)
    StopEffect(0xFFFE, 0x08, 0x01)
    LoadEffect(0xFFFE, 0x33, 'battle/sc028_00_15.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc028_00_16.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc028_00_17.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    Sleep(833)

    Sleep(833)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6B))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_43(0x65, 500, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 0.65, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 15.0, -30.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.1, 1.25, 0.0, 750)
    CameraRotateByTarget(0xFFFE, '', 0x02, 0.0, -50.0, 0.0, 800, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '3', '2', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x07, 0x00BF)
    Sleep(50)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x02, 0xFFFE, '', -1.1, 1.6, 1.05, 250)
    CameraRotateByTarget(0xFFFE, '', 0x02, 18.0, -55.0, 0.0, 250, 0x01)
    CameraSetDistance(0x02, 6.0, 250)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.42, 1.15, 0.24, 600)
    CameraRotateByTarget(0xFFFE, '', 0x03, 27.0, -45.0, 0.0, 600, 0x01)
    CameraSetDistance(0x03, 4.0, 600)
    CameraCmd(0x0B, 0x03, 45.7, 0x0258)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.75), ParamFloat(1.75), ParamFloat(1.75), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.75), ParamFloat(1.75), ParamFloat(1.75), 0xFF)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -90.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -90.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)
    OP_3B(0xFF, 0.6, 0.7, 0.2)
    OP_3B(0x00, ParamInt(0x8FAD), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FC1), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.8, 150, 250, 200, 1.0, 0xF016, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.25, 0.25, 0.0, 50, 100, 50, 0, 0, 0x00)
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.42, 1.15, 0.24, 5000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 32.0, -24.0, 0.0, 5000, 0x01)
    CameraSetDistance(0x03, 4.9, 5000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1166)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    StopEffect(0xFFFE, 0x05, 0x01)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.13, 1.12, 0.21, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -22.0, -62.0, 8.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCmd(0x0B, 0x03, 50.9, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(0x014A), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1063), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(0x014A), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.75), ParamFloat(1.75), ParamFloat(1.75), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.75), ParamFloat(1.75), ParamFloat(1.75), 0xFF)
    Sleep(333)

    CameraSetPosByTarget(0x01, 0xFFFE, '', 0.23, 1.25, 0.23, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x01, -19.0, -63.0, 6.0, 1000, 0x01)
    CameraSetHeight(0x01, -0.6, 1000)
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '2', 'FE7F', '', '#b', '0')
    OP_5E(0x00, 0x0000, 0.5, 100, 700, 200, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(166)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6C))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(233)

    OP_3B(0xFF, 0.6, 0.9, 0.5)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0E)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2.5), ParamFloat(2.5), ParamFloat(2.5), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2.5), ParamFloat(2.5), ParamFloat(2.5), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    EffectSetRGBA(0xFFFE, 0x06, 1.0, 0.3, 0.2, 1.0, 0, 0x03)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x04, 0x01)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.03, 0.85, 0.74, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, -156.0, 24.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCmd(0x0B, 0x03, 50.9, 0x0000)
    CameraCmd(0x0A, 0.125, 0.1, 0.0, 0, 5000, 500, 0, 60, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x05, 0x00)
    CameraSetHeight(0x03, 0.7, 300)
    Sleep(50)

    CameraCmd(0x07, 0x00BF)
    Sleep(50)

    OP_3B(0x00, ParamInt(0x8F6F), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F71), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetHeight(0x03, 1.85, 5000)
    Sleep(1666)

    OP_43(0x65, 250, 1.0, 0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    EffectSetRGBA(0xFFFE, 0x07, 1.0, 0.8, 0.8, 1.0, 0, 0x03)
    OP_43(0xFE, 0)
    ReleaseEffect(0xFFFE, 0x3B)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 18.64, 0.81, -11.99, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -90.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 24.6, 0)
    CameraCmd(0x0B, 0x03, 52.6, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8FA6), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(400), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(400), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 18.53, 0.97, 15.0, 1800)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -90.0, 0.0, 1800, 0x01)
    OP_3B(0xFF, 0.5, 0.3, 1.6)
    Sleep(1500)

    OP_43(0x65, 150, 1.0, 0)
    OP_43(0xFE, 0)
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -6.14, 2.54, 20.31, 450)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.0, -128.0, 9.0, 450, 0x01)
    CameraSetDistance(0x03, 5.8, 450)
    Sleep(466)

    Sleep(20)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(1.5), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.75), ParamFloat(0.75), ParamFloat(0.75), 0x0F)
    OP_3B(0x00, ParamInt(0x8FAC), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.8, 150, 250, 200, 1.0, 0xF016, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.7, 0.7, 0.0, 50, 100, 50, 0, 0, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage00', ScriptId.Current)
    OP_84(0x00, -0.65, -0.65, -0.65, 2.0)
    OP_84(0x01, 0.75, 0.75, 0.75, 0.0)
    Sleep(60)

    OP_4E(0.1, 0.0, 0x03, 0x00)
    OP_3B(0xFF, 0.7, 0.9, 0.3)
    Sleep(100)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_84(0x02, 0.0, 0.0, 0.0, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -1.85, 5.69, 20.3, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 24.0, -161.0, 3.0, 3000, 0x01)
    CameraSetDistance(0x03, 6.4, 3000)
    CameraCmd(0x0B, 0x03, 52.6, 0x0BB8)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0xFFEA, 0x00000004, ParamStr(''), ParamFloat(0), ParamFloat(1.5), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.25), ParamFloat(1.25), ParamFloat(1.25), 0xFF)
    OP_3B(0x00, ParamInt(0x8F8A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1200), ParamInt(300), 0x0000, 0x04B0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F4B), ParamFloat(0.7), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(1000), ParamInt(500), 0x0000, 0x0000, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.5, 0.5, 0.0, 50, 3000, 50, 0, 0, 0x00)
    OP_3B(0xFF, 0.6, 0.8, 1.5)
    Sleep(500)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_04(0x0B, 'BtlSCraft00_Finish')

    Return()

# id: 0x00DC offset: 0x1F7A8
@scena.Code('BtlSCraft00_Finish')
def BtlSCraft00_Finish():
    OP_43(0x03, 2000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F804',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_1F82D')

    def _loc_1F804(): pass

    label('loc_1F804')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1F82D(): pass

    label('loc_1F82D')

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'BtlDefaultFace')
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR028_SC1')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000200)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000200)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x37)
    ReleaseEffect(0xFFFE, 0x38)
    ReleaseEffect(0xFFFE, 0x39)
    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    ReleaseEffect(0xFFFE, 0x3E)
    ReleaseEffect(0xFFFE, 0x3F)
    BattleDeleteTempChar(0xFFFF)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00DD offset: 0x1F9CC
@scena.Code('BtlSCraftDamage')
def BtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00DE offset: 0x1FA1C
@scena.Code('AniBtlSCraftDamage00')
def AniBtlSCraftDamage00():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1FA2C(): pass

    label('loc_1FA2C')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1FA6B',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1FA2C')

    def _loc_1FA6B(): pass

    label('loc_1FA6B')

    BattleTargetsIterReset(0x00, 0xFFFE)

    Return()

# id: 0x00DF offset: 0x1FA78
@scena.Code('BtlChrSort')
def BtlChrSort():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    Sleep(1)

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1FAB0(): pass

    label('loc_1FAB0')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1FAEC',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFF, 180.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1FAB0')

    def _loc_1FAEC(): pass

    label('loc_1FAEC')

    Return()

# id: 0x00E0 offset: 0x1FAF0
@scena.Code('AniBtlSCraft10')
def AniBtlSCraft10():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR028_SC2')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR028_C70')"),
            Expr.Return,
        ),
        'loc_1FBA4',
    )

    LoadEffect(0xFFFE, 0x30, 'battle/cic028_9.eff', 0x00000000)

    Jump('loc_1FBAD')

    def _loc_1FBA4(): pass

    label('loc_1FBA4')

    BattleCmd(0x52, 0xFFFE, 0x30)

    def _loc_1FBAD(): pass

    label('loc_1FBAD')

    LoadEffect(0xFFFE, 0x31, 'battle/sc028_10_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc028_10_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc028_10_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc028_10_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc028_10_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc028_10_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc028_10_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc028_10_8.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000003A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -50.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x00000578, 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1FE0A(): pass

    label('loc_1FE0A')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1FE4D',
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

    Jump('loc_1FE0A')

    def _loc_1FE4D(): pass

    label('loc_1FE4D')

    Call(ScriptId.Current, 'SpringOff')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    OP_CE(0x0005, 0xFFFE, 'BTL_S_CRAFT10_01_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_CE(0x0004, 0xFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0028, 'gamePos1', 0x00)
    OP_43(0x64, 500, 1.0, 0)
    OP_CE(0x0002, 'BTL_S_CRAFT10_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_CE(0x0009, 0x3F4CCCCD, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0xFFFF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(666)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(166)

    OP_CE(0x0003, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(3), ParamFloat(3), ParamFloat(3), 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '7[autoE6]', '77766777676767', '0', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6D))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_CE(0x0002, 'BTL_S_CRAFT10_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F8CCCCD, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    Sleep(600)

    OP_3B(0x00, ParamInt(0x8F25), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F83), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_CE(0x0009, 0x3F4CCCCD, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    Sleep(666)

    OP_3B(0x00, ParamInt(0x8F25), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F83), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '7[autoE6]', '2[autoM0]', '3', '#b', '0')
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '7[autoE6]', '2[autoM0]', '0', '#b', '0')
    EffectSetRGBA(0xFFFE, 0x02, 1.0, 1.0, 1.0, 0.0, 1000, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0.5), 90.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.5), -90.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    OP_3B(0x00, ParamInt(0x8F81), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FA8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(100)

    OP_CE(0x0003, 0x00)
    CameraCmd(0x09, 0.15, 0.15, 0.3)
    OP_3B(0xFF, 0.6, 0.8, 0.15)
    OP_5E(0x00, 0x0002, 0.7, 60, 100, 60, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0002, 'BTL_S_CRAFT10_03_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0003, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT10_04_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(4400), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '23#36w2[autoE2]', '2[autoM2]', '0#46w7', '#b', '0')
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x8F88), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000103, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    SetChrFace(0x03, PseudoChrId.Self, '7[autoE6]', '76767', '0', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6E))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    OP_CE(0x0002, 'BTL_S_CRAFT10_05_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(666)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    Sleep(10)

    EffectCmd(0x0E, 0xFFFE, 0x03, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x04, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000103, ParamStr('gamePos1'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 90.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F71), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F5F), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-2), 0x0001, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(4500), ParamInt(0x00B4), 0x0000, 0x0000, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(30)

    OP_3B(0x00, ParamInt(0x8FA6), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_CE(0x0003, 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT10_06_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x10EC), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_CE(0x0003, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT10_07_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_07', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x8F6B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDam10_0', ScriptId.Current)
    CameraCmd(0x09, 0.1, 0.1, 2.5)
    OP_3B(0xFF, 0.3, 0.5, 2.5)
    Sleep(2333)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    OP_CE(0x0009, 0x3F000000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    OP_CE(0x0003, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    ReleaseEffect(0xFFFE, 0x32)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0.5), 90.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.5), -90.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x07)
    OP_3B(0x00, ParamInt(0x1063), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F41), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '7', '2[autoM2]', '0', '#b', '0')
    OP_CE(0x0002, 'BTL_S_CRAFT10_08_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_08', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Sleep(600)

    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '7', '5', '#b', '0')
    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B6F))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    Sleep(333)

    WaitEffect(0xFFFE, 0x0038, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x06, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x07, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1666)

    Call(ScriptId.Current, 'AniPlayVoice_PLAYER', ParamInt(0x1B70))
    Call(ScriptId.Current, 'AniPlayVoice_SHADOW', ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0.5), 90.0, 0.0, 0.0, ParamFloat(4), ParamFloat(6), ParamFloat(4), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000103, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.5), -90.0, 0.0, 0.0, ParamFloat(4), ParamFloat(6), ParamFloat(4), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000103, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), -80.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    EffectSetRGBA(0xFFFE, 0x08, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '7', '5', '#b', '0')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT10_09_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_09', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x105A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(666)

    EffectSetRGBA(0xFFFE, 0x08, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    Sleep(866)

    OP_3B(0x00, ParamInt(0x8F00), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1400), ParamInt(0x0118), 0x0000, 0x0578, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.8, 0, 75, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(133)

    OP_CE(0x0002, 'BTL_S_CRAFT10_10_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_5E(0x00, 0x0002, 0.4, 100, 600, 60, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_CE(0x0009, 0x3FA66666, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.3, 0xFFFFFFFF)
    OP_CE(0x0003, 0x00)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_21437(): pass

    label('loc_21437')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_21473',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFEA, 0.0, 0.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_21437')

    def _loc_21473(): pass

    label('loc_21473')

    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT10_11_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_11', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F333333, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 0.7, 0xFFFFFFFF)
    Sleep(200)

    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    CameraCmd(0x09, 0.25, 1.0, 0.6)
    OP_3B(0xFF, 0.6, 1.0, 0.6)
    OP_5E(0x00, 0x0002, 0.7, 60, 150, 60, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    CameraCmd(0x09, 0.5, 1.0, 4.5)
    OP_5E(0x00, 0x0002, 0.5, 60, 1000, 60, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.5, 1.0, 4.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000103, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x09)
    OP_3B(0x00, ParamInt(0x8F07), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraftDam10_1', ScriptId.Current)
    Sleep(60)

    OP_3B(0x00, ParamInt(5100), ParamFloat(2), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F51), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F53), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x1065), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F4B), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(3000), ParamInt(1000), 0x0000, 0x0BB8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_CE(0x0003, 0x00)
    OP_3B(0x00, ParamInt(0x14BA), ParamFloat(0.9), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    EffectSetRGBA(0xFFFE, 0x06, 1.0, 1.0, 1.0, 0.0, 1000, 0x03)
    EffectSetRGBA(0xFFFE, 0x07, 1.0, 1.0, 1.0, 0.0, 1000, 0x03)
    EffectSetRGBA(0xFFFE, 0x08, 1.0, 1.0, 1.0, 0.0, 1000, 0x03)
    OP_CE(0x0002, 'BTL_S_CRAFT10_12_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT10_11a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0003, 0x00)
    WaitEffect(0xFFFE, 0x0037, 0x00)
    OP_43(0x03, 2000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    WaitForThreadExit(PseudoChrId.Self, 0x03)

    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    OP_04(0x0B, 'AniBtlSCraft10_Finish')

    Return()

# id: 0x00E1 offset: 0x219BC
@scena.Code('AniBtlSCraft10_Finish')
def AniBtlSCraft10_Finish():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR028_SC2')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x38)
    ReleaseEffect(0xFFFE, 0x39)
    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    ReleaseEffect(0xFFFE, 0x3E)
    BattleDeleteTempChar(0xFFFF)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    OP_CE(0x0001, 0x00000000, 0x00)
    Call(ScriptId.Current, 'AniDetachMainWeaponSword')
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    OP_C0(0x0001, 0xBF800000)
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00E2 offset: 0x21B84
@scena.Code('AniBtlSCraftDam10_0')
def AniBtlSCraftDam10_0():
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFF9, 0x00000103, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(600)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFF9, 0x00000103, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F74), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFF9, 0x00000103, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F74), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(350)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFF9, 0x00000103, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F74), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(750)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFF9, 0x00000103, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F74), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(2000), ParamInt(400), 0x0000, 0x07D0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x00E3 offset: 0x221F8
@scena.Code('AniBtlSCraftDam10_1')
def AniBtlSCraftDam10_1():
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(1000)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)

    Return()

# id: 0x00E4 offset: 0x22328
@scena.Code('AniAttachEQU104')
def AniAttachEQU104():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x00E5 offset: 0x22340
@scena.Code('AniDetachEQU104')
def AniDetachEQU104():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x00E6 offset: 0x22358
@scena.Code('AniPlayVoiceRandom_PLAYER')
def AniPlayVoiceRandom_PLAYER():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x01, 0x01)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x02, 0x02)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x03, 0x03)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_223C8',
    )

    OP_3B(0x3A, 0xFFFE, ArgInt(0), ArgInt(1), ArgInt(2), ArgInt(3))

    def _loc_223C8(): pass

    label('loc_223C8')

    Return()

# id: 0x00E7 offset: 0x223CC
@scena.Code('AniPlayVoiceRandom_SHADOW')
def AniPlayVoiceRandom_SHADOW():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x01, 0x01)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x02, 0x02)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x03, 0x03)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x20B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2243C',
    )

    OP_3B(0x3A, 0xFFFE, ArgInt(0), ArgInt(1), ArgInt(2), ArgInt(3))

    def _loc_2243C(): pass

    label('loc_2243C')

    Return()

# id: 0x00E8 offset: 0x22440
@scena.Code('AniPlayVoice_PLAYER')
def AniPlayVoice_PLAYER():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_224B8',
    )

    OP_3B(0x32, ArgInt(0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_224B8(): pass

    label('loc_224B8')

    Return()

# id: 0x00E9 offset: 0x224BC
@scena.Code('AniPlayVoice_SHADOW')
def AniPlayVoice_SHADOW():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x20B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22534',
    )

    OP_3B(0x32, ArgInt(0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_22534(): pass

    label('loc_22534')

    Return()

# id: 0x00EA offset: 0x22538
@scena.Code('AniEvIdle')
def AniEvIdle():
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EB offset: 0x2258C
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EC offset: 0x225BC
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00ED offset: 0x225EC
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EE offset: 0x2261C
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x2265C
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
        'loc_226EB',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_227C4')

    def _loc_226EB(): pass

    label('loc_226EB')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_22766',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_227C4')

    def _loc_22766(): pass

    label('loc_22766')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_227C4(): pass

    label('loc_227C4')

    Return()

# id: 0x00F0 offset: 0x227C8
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x22804
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00F2 offset: 0x22860
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip_S')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x228AC
@scena.Code('AniEvBtlWait_G')
def AniEvBtlWait_G():
    Call(ScriptId.Current, 'ShowEquip_G')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x228F8
@scena.Code('AniEvBtlMove_S')
def AniEvBtlMove_S():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x22950
@scena.Code('AniEvBtlMove_G')
def AniEvBtlMove_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F6 offset: 0x229A8
@scena.Code('AniEvBtlDash_S')
def AniEvBtlDash_S():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_S', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F7 offset: 0x229F0
@scena.Code('AniEvBtlDash_G')
def AniEvBtlDash_G():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH_G', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x22A38
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F9 offset: 0x22A70
@scena.Code('AniEvBtlWalk_G')
def AniEvBtlWalk_G():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FA offset: 0x22AA8
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_6C(PseudoChrId.Self, 0.95, 0xFFFFFFFF)
    Sleep(1100)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Sleep(66)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FB offset: 0x22BAC
@scena.Code('AniEvFieldAttackEnd_G')
def AniEvFieldAttackEnd_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    Sleep(1266)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FC offset: 0x22CA4
@scena.Code('AniEvFieldAttackEnd_Common')
def AniEvFieldAttackEnd_Common():
    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22D4B',
    )

    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 147.833, 147.867, -1.0, 0x00, 0x00)
    Sleep(33)

    Call(ScriptId.Current, 'AniEvFieldAttackEnd_G')

    Jump('loc_22DD7')

    def _loc_22D4B(): pass

    label('loc_22D4B')

    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAITCHANGE_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 151.167, 151.2, -1.0, 0x00, 0x00)
    Sleep(33)

    Call(ScriptId.Current, 'AniEvFieldAttackEnd')

    def _loc_22DD7(): pass

    label('loc_22DD7')

    Return()

# id: 0x00FD offset: 0x22DD8
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FE offset: 0x22E68
@scena.Code('AniEvAttack_G')
def AniEvAttack_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FF offset: 0x22EF8
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0100 offset: 0x22F88
@scena.Code('AniEvDamage_G')
def AniEvDamage_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0101 offset: 0x23018
@scena.Code('AniEvAria')
def AniEvAria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0102 offset: 0x23064
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0103 offset: 0x230CC
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0104 offset: 0x2315C
@scena.Code('AniEvBackStep_G')
def AniEvBackStep_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP_G', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0105 offset: 0x231EC
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0106 offset: 0x2327C
@scena.Code('AniEvDeada')
def AniEvDeada():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0107 offset: 0x232D4
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1_S', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0108 offset: 0x2332C
@scena.Code('AniEvDead_G')
def AniEvDead_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0109 offset: 0x233BC
@scena.Code('AniEvDeada_G')
def AniEvDeada_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010A offset: 0x23414
@scena.Code('AniEvDead1_G')
def AniEvDead1_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1_G', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010B offset: 0x2346C
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010C offset: 0x234E0
@scena.Code('AniEvItem_G')
def AniEvItem_G():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM_G', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010D offset: 0x23580
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010E offset: 0x23614
@scena.Code('AniEvFrontStep_G')
def AniEvFrontStep_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP_G', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010F offset: 0x236A8
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_S', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0110 offset: 0x23700
@scena.Code('AniEvWeak_G')
def AniEvWeak_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_G', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0111 offset: 0x23758
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0112 offset: 0x237EC
@scena.Code('AniEvWeakDamage_G')
def AniEvWeakDamage_G():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE_G', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK_G', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0113 offset: 0x23880
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa_S', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0114 offset: 0x23914
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0115 offset: 0x2397C
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0116 offset: 0x23A0C
@scena.Code('AniEvORDER')
def AniEvORDER():
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0117 offset: 0x23A74
@scena.Code('AniEvSCraft00Loop')
def AniEvSCraft00Loop():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00b', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0118 offset: 0x23AD4
@scena.Code('AniEvSCraft00')
def AniEvSCraft00():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0119 offset: 0x23B70
@scena.Code('AniEvSCraft00_1')
def AniEvSCraft00_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011A offset: 0x23BD0
@scena.Code('AniEvSCraft00_2')
def AniEvSCraft00_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011B offset: 0x23C30
@scena.Code('AniEvSCraft00_3')
def AniEvSCraft00_3():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011C offset: 0x23CCC
@scena.Code('AniEvSCraft00_4')
def AniEvSCraft00_4():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011D offset: 0x23D70
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    Call(ScriptId.Current, 'ShowEquip_G')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011E offset: 0x23DE0
@scena.Code('AniEvCraft00_1')
def AniEvCraft00_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011F offset: 0x23E3C
@scena.Code('AniEvCraft00_2')
def AniEvCraft00_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0120 offset: 0x23E98
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'ShowEquip_G')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0121 offset: 0x23F08
@scena.Code('AniEvCraft01_1')
def AniEvCraft01_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0122 offset: 0x23F64
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0123 offset: 0x23FD4
@scena.Code('AniEvCraft02b')
def AniEvCraft02b():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0124 offset: 0x24030
@scena.Code('AniEvCraft02_1')
def AniEvCraft02_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0125 offset: 0x240C8
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
        'loc_241FA',
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
        'loc_241A8',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)

    Jump('loc_241E5')

    def _loc_241A8(): pass

    label('loc_241A8')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_241E5(): pass

    label('loc_241E5')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_24617')

    def _loc_241FA(): pass

    label('loc_241FA')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_244D4',
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_2438B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIb_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1_U', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24382',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2432A',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_242F6(): pass

    label('loc_242F6')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_24323',
    )

    Sleep(10)

    Jump('loc_242F6')

    def _loc_24323(): pass

    label('loc_24323')

    Sleep(300)

    def _loc_2432A(): pass

    label('loc_2432A')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT_U', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24382(): pass

    label('loc_24382')

    Jump('loc_244CB')

    def _loc_2438B(): pass

    label('loc_2438B')

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
        'loc_244CB',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24475',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_24441(): pass

    label('loc_24441')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2446E',
    )

    Sleep(10)

    Jump('loc_24441')

    def _loc_2446E(): pass

    label('loc_2446E')

    Sleep(300)

    def _loc_24475(): pass

    label('loc_24475')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_244CB(): pass

    label('loc_244CB')

    Jump('loc_24617')

    def _loc_244D4(): pass

    label('loc_244D4')

    OP_80(0.4)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_24596',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_24617')

    def _loc_24596(): pass

    label('loc_24596')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_24617(): pass

    label('loc_24617')

    Return()

# id: 0x0126 offset: 0x24618
@scena.Code('AniEvRyoteburi')
def AniEvRyoteburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTEBURI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0127 offset: 0x246CC
@scena.Code('AniEvTeburi')
def AniEvTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEBURI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0128 offset: 0x2477C
@scena.Code('AniEvYareyare')
def AniEvYareyare():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_YAREYARE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0129 offset: 0x24830
@scena.Code('AniEv00025')
def AniEv00025():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev00025', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev00025a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012A offset: 0x24898
@scena.Code('AniEv03000')
def AniEv03000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    Sleep(333)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev03000a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012B offset: 0x24944
@scena.Code('AniEv03001')
def AniEv03001():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03001', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012C offset: 0x24998
@scena.Code('AniEv03020')
def AniEv03020():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03020', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012D offset: 0x249EC
@scena.Code('AniEv03025')
def AniEv03025():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03025', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev03025a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012E offset: 0x24A74
@scena.Code('AniEv03030')
def AniEv03030():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03030', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012F offset: 0x24AA8
@scena.Code('AniEv30000')
def AniEv30000():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV30000', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0130 offset: 0x24ADC
@scena.Code('AniEv30205')
def AniEv30205():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30205', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev30205a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0131 offset: 0x24B64
@scena.Code('AniEv34560')
def AniEv34560():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev34560', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev34560a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0132 offset: 0x24BC0
@scena.Code('AniEv34560a')
def AniEv34560a():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev34560a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0133 offset: 0x24BF4
@scena.Code('AniEv35000')
def AniEv35000():
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24DAE',
    )

    SetEndhookFunction('ShowEquip_G', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7539), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    Sleep(166)

    OP_3B(0x00, ParamInt(0x753D), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    OP_3B(0x01, ParamInt(0x753D), ParamInt(0x015E), 0xFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_G', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_24FB5')

    def _loc_24DAE(): pass

    label('loc_24DAE')

    SetEndhookFunction('ShowEquip_S', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000_2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x7538), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(233)

    OP_3B(0x00, ParamInt(0x11CC), ParamFloat(0.3), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2E(0x03, PseudoChrId.Self, 0x00, 0x00)
    Sleep(666)

    OP_3B(0x01, ParamInt(0x11CC), ParamInt(300), 0xFFFF)
    OP_3B(0x00, ParamInt(0x7534), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24FB5(): pass

    label('loc_24FB5')

    Return()

# id: 0x0134 offset: 0x24FB8
@scena.Code('AniEv35000_2')
def AniEv35000_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('AniEv35000_2_endhook', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000_2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x7538), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(233)

    OP_3B(0x00, ParamInt(0x11CC), ParamFloat(0.3), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2E(0x03, PseudoChrId.Self, 0x00, 0x00)
    Sleep(666)

    OP_3B(0x01, ParamInt(0x11CC), ParamInt(300), 0xFFFF)
    OP_3B(0x00, ParamInt(0x7534), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0135 offset: 0x251DC
@scena.Code('AniEv35000_2_endhook')
def AniEv35000_2_endhook():
    Call(ScriptId.Current, 'ShowEquip_S')
    Call(ScriptId.Current, 'SpringOff')

    Return()

# id: 0x0136 offset: 0x25204
@scena.Code('AniEv45000')
def AniEv45000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV45000', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0137 offset: 0x25258
@scena.Code('AniEv45005')
def AniEv45005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45005', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0138 offset: 0x252AC
@scena.Code('AniAttachS50EVT02')
def AniAttachS50EVT02():
    LoadAsset('O_S50EVT02')
    AttachEquip(0xFFFE, 'O_S50EVT02', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0139 offset: 0x25348
@scena.Code('AniDetachS50EVT02')
def AniDetachS50EVT02():
    ReleaseAsset('O_S50EVT02')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x013A offset: 0x2539C
@scena.Code('AniEv54525')
def AniEv54525():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV54525', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013B offset: 0x25400
@scena.Code('AniAttachEQU330')
def AniAttachEQU330():
    LoadAsset('C_EQU330')
    AttachEquip(0xFFFE, 'C_EQU330', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x013C offset: 0x25498
@scena.Code('AniDetachEQU330')
def AniDetachEQU330():
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU330')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x013D offset: 0x254EC
@scena.Code('AniAttachEQU331')
def AniAttachEQU331():
    LoadAsset('C_EQU331')
    AttachEquip(0xFFFE, 'C_EQU331', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x013E offset: 0x25584
@scena.Code('AniDetachEQU331')
def AniDetachEQU331():
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU331')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x013F offset: 0x255D8
@scena.Code('AniEv55030')
def AniEv55030():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV55030', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0140 offset: 0x2565C
@scena.Code('AniEv55035')
def AniEv55035():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV55035', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0141 offset: 0x256E0
@scena.Code('AniEv59100')
def AniEv59100():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV59100', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV59100a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0142 offset: 0x25748
@scena.Code('AniEv59105')
def AniEv59105():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV59105', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV59105a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0143 offset: 0x257B0
@scena.Code('AniEv59110')
def AniEv59110():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV59110', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV59110a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0144 offset: 0x25818
@scena.Code('AniEv70105')
def AniEv70105():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70105', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70105a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0145 offset: 0x25880
@scena.Code('AniEv70106')
def AniEv70106():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70106', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70106a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0146 offset: 0x258E8
@scena.Code('AniEv70125')
def AniEv70125():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70125', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0147 offset: 0x2593C
@scena.Code('AniEv79284')
def AniEv79284():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79284', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0148 offset: 0x25990
@scena.Code('AniEv79285')
def AniEv79285():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79285', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79285a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0149 offset: 0x25A18
@scena.Code('AniEv79286')
def AniEv79286():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79286', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79286a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014A offset: 0x25AA0
@scena.Code('AniEv81000')
def AniEv81000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev81000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev81000a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014B offset: 0x25B28
@scena.Code('AniEv81000a')
def AniEv81000a():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev81000a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014C offset: 0x25B80
@scena.Code('AniEvEquipMode_Gun')
def AniEvEquipMode_Gun():
    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x014D offset: 0x25B90
@scena.Code('AniEvEquipMode_Sword')
def AniEvEquipMode_Sword():
    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x014E offset: 0x25BA0
@scena.Code('AniEv_Z1_00_52_52')
def AniEv_Z1_00_52_52():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_52_52', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014F offset: 0x25BE4
@scena.Code('AniAttachEQU740')
def AniAttachEQU740():
    LoadAsset('C_EQU740')
    AttachEquip(0xFFFE, 'C_EQU740', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0150 offset: 0x25C7C
@scena.Code('AniDetachEQU740')
def AniDetachEQU740():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU740')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0151 offset: 0x25CD0
@scena.Code('AniMG13Wait')
def AniMG13Wait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'MG13_SUIKA_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0152 offset: 0x25D1C
@scena.Code('AniMG13Hit')
def AniMG13Hit():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'MG13_SUIKA_HIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'MG13_SUIKA_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0153 offset: 0x25D98
@scena.Code('AniMG13Miss')
def AniMG13Miss():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'MG13_SUIKA_MISS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'MG13_SUIKA_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0154 offset: 0x25E14
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR028_EV', 'ev35000')
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR028_EV', 'EV35000_2')
    LoadEffect(0xFFFE, 0x22, 'battle/atk028_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk028_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk028_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk028_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle_sys/sysmchange.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x27, 'battle/atk028_a0.eff', 0x00000000)

    Return()

# id: 0x0155 offset: 0x25F1C
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'ev35000')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'EV35000_2')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)
    ReleaseEffect(0xFFFE, 0x27)

    Return()

# id: 0x0156 offset: 0x25F94
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0157 offset: 0x2601C
@scena.Code('AniCvIdle')
def AniCvIdle():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('DefaultFace', 0x000B)
    OP_80(0.2)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_260DB',
    )

    OP_3B(0x32, ParamInt(0x1BB8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_26130')

    def _loc_260DB(): pass

    label('loc_260DB')

    OP_3B(0x32, ParamInt(0x1BB9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_26130(): pass

    label('loc_26130')

    SetChrFace(0x03, PseudoChrId.Self, '00000000011EEEEEEEEEEEEE0', '[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0158 offset: 0x261C8
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('ShowEquip_S', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000_2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x7538), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(233)

    OP_3B(0x00, ParamInt(0x11CC), ParamFloat(0.3), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2E(0x03, PseudoChrId.Self, 0x00, 0x00)
    Sleep(666)

    OP_3B(0x01, ParamInt(0x11CC), ParamInt(300), 0xFFFF)
    OP_3B(0x00, ParamInt(0x7534), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0159 offset: 0x26414
@scena.Code('AniCvAttack')
def AniCvAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x04,
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

    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip_S')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1_S', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Sleep(166)

    Sleep(66)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B5D), ParamInt(0x1B5F), ParamInt(0), ParamInt(0))

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_265A0',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.15), ParamFloat(0.5), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x02)

    def _loc_265A0(): pass

    label('loc_265A0')

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 30, 100, 30, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Sleep(66)

    Sleep(200)

    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2[autoM2]', '', '#b', '0')
    Sleep(333)

    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015A offset: 0x26688
@scena.Code('AniCvAssaultAttack')
def AniCvAssaultAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    SetEndhookFunction('AniAssaultEnd_endHook', 0x000B)
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniAttachMainWeaponGun')
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B63), ParamInt(0x1B60), ParamInt(0), ParamInt(0))
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 0.333333, 1.66667, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '232[autoE2]', '[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(333)

    OP_3B(0x00, ParamInt(0x1005), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2694D',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0027), PseudoChrId.Self, 0x00000003, ParamStr('L_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_2694D(): pass

    label('loc_2694D')

    OP_3B(0x00, ParamInt(0x8F95), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x0104), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_41(0xFFFE, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 1.7, 2.5, -1.0, 0x00, 0x00)
    Sleep(166)

    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.75, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x015B offset: 0x26AC0
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM_S', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    OP_3B(0x00, ParamInt(0x753D), ParamFloat(0.5), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Sleep(766)

    OP_3B(0x00, ParamInt(0x7534), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7538), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniFieldAttackEnd_endHook')
    Sleep(66)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x015C offset: 0x26CF4
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26D19',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_26D19(): pass

    label('loc_26D19')

    Return()

# id: 0x015D offset: 0x26D1C
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26D7E',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_26D7E(): pass

    label('loc_26D7E')

    Return()

# id: 0x015E offset: 0x26D80
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_26E23',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_26F06')

    def _loc_26E23(): pass

    label('loc_26E23')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B73), ParamInt(0x1B74), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_26F06(): pass

    label('loc_26F06')

    Return()

# id: 0x015F offset: 0x26F08
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'AniAttachMainWeaponSword')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1B75), ParamInt(0x1B76), ParamInt(0), ParamInt(0))
    Sleep(600)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_76(PseudoChrId.Self, 'R_hand_point', 'open', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'btlartsb_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb_S', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)
    Sleep(300)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_S', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0160 offset: 0x271BC
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_3B(0x32, ParamInt(0x1B8D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, 'F1', '', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, 'F2', '13030134', '', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '4[autoM4]', '0[autoB0]', '#b', '0')
    Sleep(500)

    Return()

# id: 0x0161 offset: 0x27370
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

# id: 0x0162 offset: 0x273D0
@scena.AnimeClips('_OnCostumeIn2_2')
def _OnCostumeIn2_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB9,
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

# id: 0x0163 offset: 0x274A0
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8D,
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

# id: 0x0164 offset: 0x27550
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B59,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5A,
            name   = '',
        ),
    )

# id: 0x0165 offset: 0x27600
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
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
            name   = 'BTL_STOP_RUN_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_STOP_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
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

# id: 0x0166 offset: 0x27930
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_WALK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK_S',
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

# id: 0x0167 offset: 0x27A00
@scena.AnimeClips('_AniRun')
def _AniRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x0168 offset: 0x27AB0
@scena.AnimeClips('_AniDash')
def _AniDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DASH',
        ),
    )

# id: 0x0169 offset: 0x27B60
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

# id: 0x016A offset: 0x27BC0
@scena.AnimeClips('_AniDamage')
def _AniDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B77,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_G',
        ),
    )

# id: 0x016B offset: 0x27C70
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R_S',
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

# id: 0x016C offset: 0x27D40
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

# id: 0x016D offset: 0x27E40
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

# id: 0x016E offset: 0x27EA0
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

# id: 0x016F offset: 0x27F00
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB9,
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

# id: 0x0170 offset: 0x27FD0
@scena.AnimeClips('_AniFieldAttack')
def _AniFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
    )

# id: 0x0171 offset: 0x280F0
@scena.AnimeClips('_AniFieldAttack2')
def _AniFieldAttack2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK2_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5F,
            name   = '',
        ),
    )

# id: 0x0172 offset: 0x28210
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B61,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001005,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F95,
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
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x0173 offset: 0x28380
@scena.AnimeClips('_AniFieldAttackEnd')
def _AniFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0174 offset: 0x28480
@scena.AnimeClips('_AniFieldAttackEndShort')
def _AniFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
    )

# id: 0x0175 offset: 0x28530
@scena.AnimeClips('_AniAttachPhone')
def _AniAttachPhone():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320',
        ),
    )

# id: 0x0176 offset: 0x28590
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

# id: 0x0177 offset: 0x285F0
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

# id: 0x0178 offset: 0x28650
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

# id: 0x0179 offset: 0x286B0
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

# id: 0x017A offset: 0x28710
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

# id: 0x017B offset: 0x28770
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

# id: 0x017C offset: 0x287F0
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

# id: 0x017D offset: 0x28870
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

# id: 0x017E offset: 0x288F0
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

# id: 0x017F offset: 0x28950
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

# id: 0x0180 offset: 0x289B0
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

# id: 0x0181 offset: 0x28A10
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

# id: 0x0182 offset: 0x28A70
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

# id: 0x0183 offset: 0x28AD0
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

# id: 0x0184 offset: 0x28B50
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

# id: 0x0185 offset: 0x28BB0
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

# id: 0x0186 offset: 0x28C10
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

# id: 0x0187 offset: 0x28C70
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

# id: 0x0188 offset: 0x28CD0
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

# id: 0x0189 offset: 0x28D30
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

# id: 0x018A offset: 0x28D90
@scena.AnimeClips('_AniAttachMainWeaponGun')
def _AniAttachMainWeaponGun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU082_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU082_L',
        ),
    )

# id: 0x018B offset: 0x28E10
@scena.AnimeClips('_AniAttachMainWeaponSword')
def _AniAttachMainWeaponSword():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU104',
        ),
    )

# id: 0x018C offset: 0x28E70
@scena.AnimeClips('_AniAttachEQU321')
def _AniAttachEQU321():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU321',
        ),
    )

# id: 0x018D offset: 0x28ED0
@scena.AnimeClips('_AniFishWait')
def _AniFishWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_WAIT',
        ),
    )

# id: 0x018E offset: 0x28F30
@scena.AnimeClips('_AniFishStart')
def _AniFishStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_START',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00003015,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_WAIT',
        ),
    )

# id: 0x018F offset: 0x28FE0
@scena.AnimeClips('_AniFishHit')
def _AniFishHit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_HIT',
        ),
    )

# id: 0x0190 offset: 0x29040
@scena.AnimeClips('_AniFishHit2')
def _AniFishHit2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_HIT2',
        ),
    )

# id: 0x0191 offset: 0x290A0
@scena.AnimeClips('_AniFishEnd')
def _AniFishEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_END',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_ENDa',
        ),
    )

# id: 0x0192 offset: 0x29120
@scena.AnimeClips('_AniFishResult')
def _AniFishResult():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'minigame/mini01_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_RESULT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FISH_RESULTa',
        ),
    )

# id: 0x0193 offset: 0x291D0
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU310',
        ),
    )

# id: 0x0194 offset: 0x292A0
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BDD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B86,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B85,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B88,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B83,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B84,
            name   = '',
        ),
    )

# id: 0x0195 offset: 0x293C0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B59,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5A,
            name   = '',
        ),
    )

# id: 0x0196 offset: 0x294C0
@scena.AnimeClips('_AniBtlKisinReady')
def _AniBtlKisinReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B59,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5A,
            name   = '',
        ),
    )

# id: 0x0197 offset: 0x295C0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B87,
            name   = '',
        ),
    )

# id: 0x0198 offset: 0x29620
@scena.AnimeClips('_AniAttachEqu348')
def _AniAttachEqu348():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU348',
        ),
    )

# id: 0x0199 offset: 0x29680
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
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x019A offset: 0x29730
@scena.AnimeClips('_AniBtlMove')
def _AniBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
    )

# id: 0x019B offset: 0x29800
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R_S',
        ),
    )

# id: 0x019C offset: 0x29880
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B80,
            name   = '',
        ),
    )

# id: 0x019D offset: 0x298E0
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B81,
            name   = '',
        ),
    )

# id: 0x019E offset: 0x29940
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B82,
            name   = '',
        ),
    )

# id: 0x019F offset: 0x299A0
@scena.AnimeClips('_AniBtlStepIn')
def _AniBtlStepIn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B7F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B7F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_G',
        ),
    )

# id: 0x01A0 offset: 0x29A70
@scena.AnimeClips('_AniBtlStepOut')
def _AniBtlStepOut():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_G',
        ),
    )

# id: 0x01A1 offset: 0x29B40
@scena.AnimeClips('_AniBtlStepInKisinPt')
def _AniBtlStepInKisinPt():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B7F,
            name   = '',
        ),
    )

# id: 0x01A2 offset: 0x29BA0
@scena.AnimeClips('_AniBtlAttack')
def _AniBtlAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_G',
        ),
    )

# id: 0x01A3 offset: 0x29CF0
@scena.AnimeClips('_AniBtlChangeStyle')
def _AniBtlChangeStyle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_S',
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
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007539,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F81,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007577,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F81,
            name   = '',
        ),
    )

# id: 0x01A4 offset: 0x29FA0
@scena.AnimeClips('_AniBtlDamage')
def _AniBtlDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_G',
        ),
    )

# id: 0x01A5 offset: 0x2A070
@scena.AnimeClips('_AniBtlSwoon')
def _AniBtlSwoon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
    )

# id: 0x01A6 offset: 0x2A190
@scena.AnimeClips('_AniBtlWeak')
def _AniBtlWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_G',
        ),
    )

# id: 0x01A7 offset: 0x2A210
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
    )

# id: 0x01A8 offset: 0x2A380
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
            name   = 'BTL_ARTSb_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSb_G',
        ),
    )

# id: 0x01A9 offset: 0x2A480
@scena.AnimeClips('_AniBtlCharge')
def _AniBtlCharge():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FD5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FD5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01AA offset: 0x2A5A0
@scena.AnimeClips('_AniBtlItem')
def _AniBtlItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
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
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
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
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01AB offset: 0x2A800
@scena.AnimeClips('_AniBtlBluff')
def _AniBtlBluff():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01AC offset: 0x2A880
@scena.AnimeClips('_AniBtlBluffVoice')
def _AniBtlBluffVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = '',
        ),
    )

# id: 0x01AD offset: 0x2A8E0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8F,
            name   = '',
        ),
    )

# id: 0x01AE offset: 0x2A960
@scena.AnimeClips('_AniBtlEscape')
def _AniBtlEscape():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BDE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B81,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_S',
        ),
    )

# id: 0x01AF offset: 0x2AA80
@scena.AnimeClips('_AniBtlTensionMax')
def _AniBtlTensionMax():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionmax.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FD5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5A,
            name   = '',
        ),
    )

# id: 0x01B0 offset: 0x2AB50
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B90,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B90,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAE,
            name   = '',
        ),
    )

# id: 0x01B1 offset: 0x2AF20
@scena.AnimeClips('_AniBtlLinkRushStart')
def _AniBtlLinkRushStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01B2 offset: 0x2AFA0
@scena.AnimeClips('_AniBtlLinkRushMove')
def _AniBtlLinkRushMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
    )

# id: 0x01B3 offset: 0x2B020
@scena.AnimeClips('_AniBtlLinkRush')
def _AniBtlLinkRush():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BF2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BF1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BEF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01B4 offset: 0x2B210
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ORDER',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ORDER',
        ),
    )

# id: 0x01B5 offset: 0x2B290
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B71,
            name   = '',
        ),
    )

# id: 0x01B6 offset: 0x2B310
@scena.AnimeClips('_AniBtlValiantAttack_Start')
def _AniBtlValiantAttack_Start():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
    )

# id: 0x01B7 offset: 0x2B370
@scena.AnimeClips('_AniBtlValiantAttack')
def _AniBtlValiantAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01B8 offset: 0x2B3F0
@scena.AnimeClips('_AniBtlValiantAttack_Move')
def _AniBtlValiantAttack_Move():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
    )

# id: 0x01B9 offset: 0x2B470
@scena.AnimeClips('_AniBtlValiantArts_Arts')
def _AniBtlValiantArts_Arts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
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
            name   = 'BTL_ARTSb_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSb_G',
        ),
    )

# id: 0x01BA offset: 0x2B590
@scena.AnimeClips('_AniBtlWaitInit')
def _AniBtlWaitInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01BB offset: 0x2B610
@scena.AnimeClips('_AniBtlKisinItemPa')
def _AniBtlKisinItemPa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
            name   = '',
        ),
    )

# id: 0x01BC offset: 0x2B690
@scena.AnimeClips('_AniBtlKisinChargePa')
def _AniBtlKisinChargePa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BE5,
            name   = '',
        ),
    )

# id: 0x01BD offset: 0x2B6F0
@scena.AnimeClips('_AniBtlKisinSinkiPa')
def _AniBtlKisinSinkiPa():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BE6,
            name   = '',
        ),
    )

# id: 0x01BE offset: 0x2B750
@scena.AnimeClips('_AniBtlKisinPartnerArts')
def _AniBtlKisinPartnerArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
            name   = '',
        ),
    )

# id: 0x01BF offset: 0x2B7D0
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

# id: 0x01C0 offset: 0x2B830
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

# id: 0x01C1 offset: 0x2B890
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

# id: 0x01C2 offset: 0x2B8F0
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B89,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8A,
            name   = '',
        ),
    )

# id: 0x01C3 offset: 0x2B9A0
@scena.AnimeClips('_AniBtlWin')
def _AniBtlWin():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007533,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB6,
            name   = '',
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
            name   = 'BTL_WIN',
        ),
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
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01C4 offset: 0x2BB60
@scena.AnimeClips('_AniBtlWinBackknuckleL2')
def _AniBtlWinBackknuckleL2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_L2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_L2a',
        ),
    )

# id: 0x01C5 offset: 0x2BBE0
@scena.AnimeClips('_AniBtlWinBackknuckleL2b')
def _AniBtlWinBackknuckleL2b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_L2b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01C6 offset: 0x2BC90
@scena.AnimeClips('_AniBtlWinBackknuckleR')
def _AniBtlWinBackknuckleR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01C7 offset: 0x2BD10
@scena.AnimeClips('_AniBtlWinChiesL')
def _AniBtlWinChiesL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_CHIES_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_CHIES_La',
        ),
    )

# id: 0x01C8 offset: 0x2BD90
@scena.AnimeClips('_AniBtlWinGjL')
def _AniBtlWinGjL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_GJ_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_GJ_La',
        ),
    )

# id: 0x01C9 offset: 0x2BE10
@scena.AnimeClips('_AniBtlWinKnuckleL2')
def _AniBtlWinKnuckleL2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KNUCKLE_L2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KNUCKLE_L2a',
        ),
    )

# id: 0x01CA offset: 0x2BE90
@scena.AnimeClips('_AniBtlWinKnuckleL2b')
def _AniBtlWinKnuckleL2b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KNUCKLE_L2b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01CB offset: 0x2BF10
@scena.AnimeClips('_AniBtlWinCrapbackL')
def _AniBtlWinCrapbackL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_CRAPBACK_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010B0,
            name   = '',
        ),
    )

# id: 0x01CC offset: 0x2BF90
@scena.AnimeClips('_AniBtlWinKnuckleR2')
def _AniBtlWinKnuckleR2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KNUCKLE_R2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01CD offset: 0x2C010
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

# id: 0x01CE offset: 0x2C090
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
            dword4 = 0x00001B8C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01CF offset: 0x2C140
@scena.AnimeClips('_AniBtlWinWait_burst')
def _AniBtlWinWait_burst():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01D0 offset: 0x2C1C0
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007533,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB6,
            name   = '',
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
            name   = 'WAIT',
        ),
    )

# id: 0x01D1 offset: 0x2C310
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8D,
            name   = '',
        ),
    )

# id: 0x01D2 offset: 0x2C370
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8D,
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

# id: 0x01D3 offset: 0x2C420
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001004,
            name   = '',
        ),
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
            name   = 'BTL_CRAFT00_03',
        ),
    )

# id: 0x01D4 offset: 0x2C570
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_01_0a.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_01_1a.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_01_2a.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_01_3a.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/ryu2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001015,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001067,
            name   = '',
        ),
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
            name   = 'BTL_CRAFT01_00b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001005,
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
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F95,
            name   = '',
        ),
    )

# id: 0x01D5 offset: 0x2C7D0
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB4,
            name   = '',
        ),
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
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F9A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010C6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F42,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01D6 offset: 0x2CA30
@scena.AnimeClips('_AniBtlCraft03')
def _AniBtlCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionmax.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionup.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F66,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa_S',
        ),
    )

# id: 0x01D7 offset: 0x2CB80
@scena.AnimeClips('_AniBtlCraft05')
def _AniBtlCraft05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionmax.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionup.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/systension.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F66,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F66,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa_G',
        ),
    )

# id: 0x01D8 offset: 0x2CDC0
@scena.AnimeClips('_AniBtlCraft13')
def _AniBtlCraft13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_13_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr028_13_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT13_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001063,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000104B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001043,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01D9 offset: 0x2CF30
@scena.AnimeClips('_AniBtlCraftEnd')
def _AniBtlCraftEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01DA offset: 0x2CFB0
@scena.AnimeClips('_AniBtlCraft04')
def _AniBtlCraft04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs023_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK20',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007587,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001135,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001151,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001144,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK22',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001148,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK20',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001135,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001144,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK22',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001148,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000114F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001150,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK21',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK23',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001156,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK23',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_LINK23',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001144,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000114D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001133,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000113B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001155,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001157,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010FA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001135,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000114E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_B1A_WAIT',
        ),
    )

# id: 0x01DB offset: 0x2D650
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic028_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001012,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F41,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_15.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_16.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_00_17.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FC1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001063,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F71,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F4B,
            name   = '',
        ),
    )

# id: 0x01DC offset: 0x2DDB0
@scena.AnimeClips('_BtlSCraft00_Finish')
def _BtlSCraft00_Finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01DD offset: 0x2DE30
@scena.AnimeClips('_AniBtlSCraft10')
def _AniBtlSCraft10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic028_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc028_10_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001012,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_01_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_01',
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
            dword4 = 0x00000FAE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_02_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F25,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F83,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F25,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F83,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F81,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_03_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_04_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F88,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_05_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F71,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_06_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010EC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_07_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001063,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F41,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_08_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_09_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_09',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000105A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F00,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_10_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_11_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000013EC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F51,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F53,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F4B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000014BA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_12_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT10_11a',
        ),
    )

# id: 0x01DE offset: 0x2E840
@scena.AnimeClips('_AniBtlSCraft10_Finish')
def _AniBtlSCraft10_Finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01DF offset: 0x2E8A0
@scena.AnimeClips('_AniBtlSCraftDam10_0')
def _AniBtlSCraftDam10_0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
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
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
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
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
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
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
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
            dword4 = 0x000010F8,
            name   = '',
        ),
    )

# id: 0x01E0 offset: 0x2EAE0
@scena.AnimeClips('_AniPlayVoice_PLAYER')
def _AniPlayVoice_PLAYER():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = '',
        ),
    )

# id: 0x01E1 offset: 0x2EB40
@scena.AnimeClips('_AniPlayVoice_SHADOW')
def _AniPlayVoice_SHADOW():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = '',
        ),
    )

# id: 0x01E2 offset: 0x2EBA0
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
            name   = 'WAIT',
        ),
    )

# id: 0x01E3 offset: 0x2EC20
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

# id: 0x01E4 offset: 0x2EC80
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

# id: 0x01E5 offset: 0x2ECE0
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

# id: 0x01E6 offset: 0x2ED40
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

# id: 0x01E7 offset: 0x2EDA0
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

# id: 0x01E8 offset: 0x2EEA0
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

# id: 0x01E9 offset: 0x2EF00
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

# id: 0x01EA offset: 0x2EF80
@scena.AnimeClips('_AniEvBtlWait')
def _AniEvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01EB offset: 0x2EFE0
@scena.AnimeClips('_AniEvBtlWait_G')
def _AniEvBtlWait_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01EC offset: 0x2F040
@scena.AnimeClips('_AniEvBtlMove_S')
def _AniEvBtlMove_S():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_S',
        ),
    )

# id: 0x01ED offset: 0x2F0A0
@scena.AnimeClips('_AniEvBtlMove_G')
def _AniEvBtlMove_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE_G',
        ),
    )

# id: 0x01EE offset: 0x2F100
@scena.AnimeClips('_AniEvBtlDash_S')
def _AniEvBtlDash_S():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_S',
        ),
    )

# id: 0x01EF offset: 0x2F160
@scena.AnimeClips('_AniEvBtlDash_G')
def _AniEvBtlDash_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH_G',
        ),
    )

# id: 0x01F0 offset: 0x2F1C0
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK_S',
        ),
    )

# id: 0x01F1 offset: 0x2F220
@scena.AnimeClips('_AniEvBtlWalk_G')
def _AniEvBtlWalk_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK_G',
        ),
    )

# id: 0x01F2 offset: 0x2F280
@scena.AnimeClips('_AniEvFieldAttackEnd')
def _AniEvFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01F3 offset: 0x2F300
@scena.AnimeClips('_AniEvFieldAttackEnd_G')
def _AniEvFieldAttackEnd_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01F4 offset: 0x2F380
@scena.AnimeClips('_AniEvFieldAttackEnd_Common')
def _AniEvFieldAttackEnd_Common():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAITCHANGE_S',
        ),
    )

# id: 0x01F5 offset: 0x2F400
@scena.AnimeClips('_AniEvAttack')
def _AniEvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01F6 offset: 0x2F480
@scena.AnimeClips('_AniEvAttack_G')
def _AniEvAttack_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01F7 offset: 0x2F500
@scena.AnimeClips('_AniEvDamage')
def _AniEvDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01F8 offset: 0x2F580
@scena.AnimeClips('_AniEvDamage_G')
def _AniEvDamage_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01F9 offset: 0x2F600
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

# id: 0x01FA offset: 0x2F660
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

# id: 0x01FB offset: 0x2F6E0
@scena.AnimeClips('_AniEvBackStep')
def _AniEvBackStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x01FC offset: 0x2F760
@scena.AnimeClips('_AniEvBackStep_G')
def _AniEvBackStep_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x01FD offset: 0x2F7E0
@scena.AnimeClips('_AniEvDead')
def _AniEvDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
    )

# id: 0x01FE offset: 0x2F860
@scena.AnimeClips('_AniEvDeada')
def _AniEvDeada():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_S',
        ),
    )

# id: 0x01FF offset: 0x2F8C0
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD1_S',
        ),
    )

# id: 0x0200 offset: 0x2F920
@scena.AnimeClips('_AniEvDead_G')
def _AniEvDead_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
    )

# id: 0x0201 offset: 0x2F9A0
@scena.AnimeClips('_AniEvDeada_G')
def _AniEvDeada_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa_G',
        ),
    )

# id: 0x0202 offset: 0x2FA00
@scena.AnimeClips('_AniEvDead1_G')
def _AniEvDead1_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD1_G',
        ),
    )

# id: 0x0203 offset: 0x2FA60
@scena.AnimeClips('_AniEvItem')
def _AniEvItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x0204 offset: 0x2FAE0
@scena.AnimeClips('_AniEvItem_G')
def _AniEvItem_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x0205 offset: 0x2FB60
@scena.AnimeClips('_AniEvFrontStep')
def _AniEvFrontStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x0206 offset: 0x2FBE0
@scena.AnimeClips('_AniEvFrontStep_G')
def _AniEvFrontStep_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
    )

# id: 0x0207 offset: 0x2FC60
@scena.AnimeClips('_AniEvWeak')
def _AniEvWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_S',
        ),
    )

# id: 0x0208 offset: 0x2FCC0
@scena.AnimeClips('_AniEvWeak_G')
def _AniEvWeak_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_G',
        ),
    )

# id: 0x0209 offset: 0x2FD20
@scena.AnimeClips('_AniEvWeakDamage')
def _AniEvWeakDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_S',
        ),
    )

# id: 0x020A offset: 0x2FDA0
@scena.AnimeClips('_AniEvWeakDamage_G')
def _AniEvWeakDamage_G():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK_G',
        ),
    )

# id: 0x020B offset: 0x2FE20
@scena.AnimeClips('_AniEvPowerUp')
def _AniEvPowerUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa_S',
        ),
    )

# id: 0x020C offset: 0x2FEA0
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

# id: 0x020D offset: 0x2FF20
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

# id: 0x020E offset: 0x2FFA0
@scena.AnimeClips('_AniEvORDER')
def _AniEvORDER():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ORDER',
        ),
    )

# id: 0x020F offset: 0x30000
@scena.AnimeClips('_AniEvSCraft00Loop')
def _AniEvSCraft00Loop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00b',
        ),
    )

# id: 0x0210 offset: 0x30060
@scena.AnimeClips('_AniEvSCraft00')
def _AniEvSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00a',
        ),
    )

# id: 0x0211 offset: 0x300E0
@scena.AnimeClips('_AniEvSCraft00_1')
def _AniEvSCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
    )

# id: 0x0212 offset: 0x30140
@scena.AnimeClips('_AniEvSCraft00_2')
def _AniEvSCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
    )

# id: 0x0213 offset: 0x301A0
@scena.AnimeClips('_AniEvSCraft00_3')
def _AniEvSCraft00_3():
    return ScenaAnimeClips(
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
            name   = 'BTL_S_CRAFT00_03a',
        ),
    )

# id: 0x0214 offset: 0x30220
@scena.AnimeClips('_AniEvSCraft00_4')
def _AniEvSCraft00_4():
    return ScenaAnimeClips(
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
            name   = 'BTL_S_CRAFT00_04a',
        ),
    )

# id: 0x0215 offset: 0x302A0
@scena.AnimeClips('_AniEvCraft00')
def _AniEvCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x0216 offset: 0x30300
@scena.AnimeClips('_AniEvCraft00_1')
def _AniEvCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
    )

# id: 0x0217 offset: 0x30360
@scena.AnimeClips('_AniEvCraft00_2')
def _AniEvCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
    )

# id: 0x0218 offset: 0x303C0
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
    )

# id: 0x0219 offset: 0x30420
@scena.AnimeClips('_AniEvCraft01_1')
def _AniEvCraft01_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
    )

# id: 0x021A offset: 0x30480
@scena.AnimeClips('_AniEvCraft02')
def _AniEvCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
    )

# id: 0x021B offset: 0x304E0
@scena.AnimeClips('_AniEvCraft02b')
def _AniEvCraft02b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
    )

# id: 0x021C offset: 0x30540
@scena.AnimeClips('_AniEvCraft02_1')
def _AniEvCraft02_1():
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

# id: 0x021D offset: 0x305C0
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
            name   = 'WAIT1_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'PRE_WAIT_U',
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

# id: 0x021E offset: 0x308A0
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

# id: 0x021F offset: 0x30950
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

# id: 0x0220 offset: 0x30A00
@scena.AnimeClips('_AniEvYareyare')
def _AniEvYareyare():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_YAREYARE',
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

# id: 0x0221 offset: 0x30AB0
@scena.AnimeClips('_AniEv00025')
def _AniEv00025():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00025',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00025a',
        ),
    )

# id: 0x0222 offset: 0x30B30
@scena.AnimeClips('_AniEv03000')
def _AniEv03000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03000a',
        ),
    )

# id: 0x0223 offset: 0x30BB0
@scena.AnimeClips('_AniEv03001')
def _AniEv03001():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03001',
        ),
    )

# id: 0x0224 offset: 0x30C10
@scena.AnimeClips('_AniEv03020')
def _AniEv03020():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03020',
        ),
    )

# id: 0x0225 offset: 0x30C70
@scena.AnimeClips('_AniEv03025')
def _AniEv03025():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03025',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03025a',
        ),
    )

# id: 0x0226 offset: 0x30CF0
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

# id: 0x0227 offset: 0x30D50
@scena.AnimeClips('_AniEv30000')
def _AniEv30000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV30000',
        ),
    )

# id: 0x0228 offset: 0x30DB0
@scena.AnimeClips('_AniEv30205')
def _AniEv30205():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30205',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30205a',
        ),
    )

# id: 0x0229 offset: 0x30E30
@scena.AnimeClips('_AniEv34560')
def _AniEv34560():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34560',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34560a',
        ),
    )

# id: 0x022A offset: 0x30EB0
@scena.AnimeClips('_AniEv34560a')
def _AniEv34560a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34560a',
        ),
    )

# id: 0x022B offset: 0x30F10
@scena.AnimeClips('_AniEv35000')
def _AniEv35000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev35000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007539,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_G',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV35000_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000011CC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x022C offset: 0x310B0
@scena.AnimeClips('_AniEv35000_2')
def _AniEv35000_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV35000_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000011CC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x022D offset: 0x311B0
@scena.AnimeClips('_AniEv45000')
def _AniEv45000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV45000',
        ),
    )

# id: 0x022E offset: 0x31210
@scena.AnimeClips('_AniEv45005')
def _AniEv45005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45005',
        ),
    )

# id: 0x022F offset: 0x31270
@scena.AnimeClips('_AniAttachS50EVT02')
def _AniAttachS50EVT02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'O_S50EVT02',
        ),
    )

# id: 0x0230 offset: 0x312D0
@scena.AnimeClips('_AniEv54525')
def _AniEv54525():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV54525',
        ),
    )

# id: 0x0231 offset: 0x31330
@scena.AnimeClips('_AniAttachEQU330')
def _AniAttachEQU330():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU330',
        ),
    )

# id: 0x0232 offset: 0x31390
@scena.AnimeClips('_AniAttachEQU331')
def _AniAttachEQU331():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU331',
        ),
    )

# id: 0x0233 offset: 0x313F0
@scena.AnimeClips('_AniEv55030')
def _AniEv55030():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV55030',
        ),
    )

# id: 0x0234 offset: 0x31450
@scena.AnimeClips('_AniEv55035')
def _AniEv55035():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV55035',
        ),
    )

# id: 0x0235 offset: 0x314B0
@scena.AnimeClips('_AniEv59100')
def _AniEv59100():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59100',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59100a',
        ),
    )

# id: 0x0236 offset: 0x31530
@scena.AnimeClips('_AniEv59105')
def _AniEv59105():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59105',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59105a',
        ),
    )

# id: 0x0237 offset: 0x315B0
@scena.AnimeClips('_AniEv59110')
def _AniEv59110():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59110',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV59110a',
        ),
    )

# id: 0x0238 offset: 0x31630
@scena.AnimeClips('_AniEv70105')
def _AniEv70105():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70105',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70105a',
        ),
    )

# id: 0x0239 offset: 0x316B0
@scena.AnimeClips('_AniEv70106')
def _AniEv70106():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70106',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70106a',
        ),
    )

# id: 0x023A offset: 0x31730
@scena.AnimeClips('_AniEv70125')
def _AniEv70125():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70125',
        ),
    )

# id: 0x023B offset: 0x31790
@scena.AnimeClips('_AniEv79284')
def _AniEv79284():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79284',
        ),
    )

# id: 0x023C offset: 0x317F0
@scena.AnimeClips('_AniEv79285')
def _AniEv79285():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79285',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79285a',
        ),
    )

# id: 0x023D offset: 0x31870
@scena.AnimeClips('_AniEv79286')
def _AniEv79286():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79286',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79286a',
        ),
    )

# id: 0x023E offset: 0x318F0
@scena.AnimeClips('_AniEv81000')
def _AniEv81000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev81000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev81000a',
        ),
    )

# id: 0x023F offset: 0x31970
@scena.AnimeClips('_AniEv81000a')
def _AniEv81000a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev81000a',
        ),
    )

# id: 0x0240 offset: 0x319D0
@scena.AnimeClips('_AniEv_Z1_00_52_52')
def _AniEv_Z1_00_52_52():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_52_52',
        ),
    )

# id: 0x0241 offset: 0x31A30
@scena.AnimeClips('_AniAttachEQU740')
def _AniAttachEQU740():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU740',
        ),
    )

# id: 0x0242 offset: 0x31A90
@scena.AnimeClips('_AniMG13Wait')
def _AniMG13Wait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG13_SUIKA_WAIT',
        ),
    )

# id: 0x0243 offset: 0x31AF0
@scena.AnimeClips('_AniMG13Hit')
def _AniMG13Hit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG13_SUIKA_HIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG13_SUIKA_WAIT',
        ),
    )

# id: 0x0244 offset: 0x31B70
@scena.AnimeClips('_AniMG13Miss')
def _AniMG13Miss():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG13_SUIKA_MISS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'MG13_SUIKA_WAIT',
        ),
    )

# id: 0x0245 offset: 0x31BF0
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk028_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk028_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk028_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk028_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/sysmchange.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk028_a0.eff',
        ),
    )

# id: 0x0246 offset: 0x31D10
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

# id: 0x0247 offset: 0x31D70
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001BB9,
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

# id: 0x0248 offset: 0x31E40
@scena.AnimeClips('_AniCvBtlWait')
def _AniCvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV35000_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000011CC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x0249 offset: 0x31F40
@scena.AnimeClips('_AniCvAttack')
def _AniCvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
    )

# id: 0x024A offset: 0x32010
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B63,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001005,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F95,
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
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x024B offset: 0x32180
@scena.AnimeClips('_AniCvFieldAttackEnd')
def _AniCvFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x024C offset: 0x32280
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
            dword4 = 0x00001B73,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B74,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x024D offset: 0x32380
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
            dword4 = 0x00001B75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B76,
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
            name   = 'BTL_ARTSb_S',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_S',
        ),
    )

# id: 0x024E offset: 0x324D0
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8D,
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
