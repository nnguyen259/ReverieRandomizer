import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr111.dat')

# id: 0x0000 offset: 0x340C
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BASEPOSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BATTLEPOSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'IDLEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'IDLEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'FATTACK1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR111_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR001_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_POWERUP_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_POWERUP_Fa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT00_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR111_BT1',
            symbol     = 'BTL_CRAFT02_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_00_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_01_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_02_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_04_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_07_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_08_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_09_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_10_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_10_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_12_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_12_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_13_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_14_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_15_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_16',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_16_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR111_SC1',
            symbol     = 'BTL_S_CRAFT00_16_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB_a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HITOUCHDB_b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HOLD_HAND_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR111_BT3',
            symbol     = 'BTL_WIN_HOLD_HAND_Ra',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_ENDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_HIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_HIT2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_RESULT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_RESULTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR111_MG1',
            symbol     = 'FISH_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR111_HS1',
            symbol     = 'BIKE_SIDE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR111_HS1',
            symbol     = 'BIKE_SIDE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_ENZETU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_ENZETU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_MAEKAGAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_MAEKAGAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP51_TEHIKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP51_TEHIKI_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP52_TUREHASIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP52_TUREHASIRI_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP53_NAKAYOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_OP53_NAKAYOSI_F',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIANF_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
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
            asset      = 'C_CHR111_EV',
            symbol     = 'EV31065',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV31065a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV31066',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV31066a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV50585',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV50585_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV50585a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV50585a_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV51545',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV51545w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV52655',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV52660',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV52665',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV52665w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV71505',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV71505a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV71550',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV71550a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV74305',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV74305a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV76055',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV76055a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV77065',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV79435',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV79435_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV79436',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EV',
            symbol     = 'EV79436_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC',
            symbol     = 'EV_C1_00_00_cut001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC',
            symbol     = 'EV_C1_00_00_cut002',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC',
            symbol     = 'EV_C1_00_00_cut003',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC',
            symbol     = 'FC_C2_12_02_cut007',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC',
            symbol     = 'EV_I5_24_00_CUT021',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_02_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_03_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_04_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_05_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_06_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_07_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_10_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_11_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_12_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_13_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC08',
            symbol     = 'EV_C1_01_01_14_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_01_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_02_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_03_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_08_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_09_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_10_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_11_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_13_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_14_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_15',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_15_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_16',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_16_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_18',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_18_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_19',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_19_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_20',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_20_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_21',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC19',
            symbol     = 'EV_C4_02_02_21_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_06_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_06_06_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_49_49',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_49_49_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_53',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_53_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_54',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_54_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_55',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR111_EVC30',
            symbol     = 'EV_Z1_00_53_55_F',
        ),
    )

# id: 0x0001 offset: 0xDD04
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xDD24
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xDD3C
@scena.Code('PlayFakeEffect')
def PlayFakeEffect():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_DDCB',
    )

    LoadEffect(0xFFFE, 0x2F, 'system/shadow_chr_aura.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x002F), PseudoChrId.Self, 0x00000023, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_DDCB(): pass

    label('loc_DDCB')

    Return()

# id: 0x0004 offset: 0xDDCC
@scena.Code('PreInit')
def PreInit():
    AnimeClipCmd(0x0D, PseudoChrId.Self)

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_DE09',
    )

    AnimeClipCmd(0x0F, PseudoChrId.Self, 0x00)
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR111_DF1', 'WAIT')

    Return()

    def _loc_DE09(): pass

    label('loc_DE09')

    Return()

# id: 0x0005 offset: 0xDE0C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "ModelCmd(0x3F)"),
            Expr.Return,
        ),
        'loc_DE1E',
    )

    Return()

    def _loc_DE1E(): pass

    label('loc_DE1E')

    Call(ScriptId.Current, 'PlayFakeEffect')

    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE46',
    )

    def _loc_DE46(): pass

    label('loc_DE46')

    OP_2A(0x04, 0xFFFE, '', 'gamePos0', '')
    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0006 offset: 0xDEBC
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0007 offset: 0xDEE4
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0008 offset: 0xDF10
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0009 offset: 0xDF1C
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_EV_Load')

    Return()

# id: 0x000A offset: 0xDF40
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_BT1_Load')

    Return()

# id: 0x000B offset: 0xDF64
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR111_BT3')

    Return()

# id: 0x000C offset: 0xDF7C
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000D offset: 0xDF8C
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000E offset: 0xDF9C
@scena.Code('Ani_MG1_Load')
def Ani_MG1_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR111_MG1')

    Return()

# id: 0x000F offset: 0xDFB4
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_EV_Release')

    Return()

# id: 0x0010 offset: 0xDFDC
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_BT1_Release')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xE010
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR111_BT3')

    Return()

# id: 0x0012 offset: 0xE028
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0013 offset: 0xE040
@scena.Code('Ani_MG1_Release')
def Ani_MG1_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR111_MG1')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0014 offset: 0xE064
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU605')

    If(
        (
            (Expr.Eval, "FormationCmd(0x0A, 0x0BCC)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E14B',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_E0EA',
    )

    ModelCmd(0x3B, 0x00, 0xFFFE, 0x0F56, 0x0BCC, 0x06, 1.6, 0.0)
    ChrClearPhysicsFlags(0x0BCC, 0x00000001)
    ChrSetPhysicsFlags(0x0BCC, 0x04010000)

    Jump('loc_E14B')

    def _loc_E0EA(): pass

    label('loc_E0EA')

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x223),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E11D',
    )

    ModelCmd(0x3B, 0x00, 0xFFFE, 0x0F57, 0x0BCC, 0x00, 1.6, 0.0)

    Jump('loc_E133')

    def _loc_E11D(): pass

    label('loc_E11D')

    ModelCmd(0x3B, 0x00, 0xFFFE, 0x0F56, 0x0BCC, 0x07, 1.6, 0.0)

    def _loc_E133(): pass

    label('loc_E133')

    ChrClearPhysicsFlags(0x0BCC, 0x00000001)
    ChrSetPhysicsFlags(0x0BCC, 0x04010000)

    def _loc_E14B(): pass

    label('loc_E14B')

    ChrClearPhysicsFlags(0x0BCC, 0x00000040)
    ChrSetPhysicsFlags(0x0BCC, 0x00800000)
    AttachEquip(0xFFFE, 'C_EQU605', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_8A(0x00, 0x0BCC, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0015 offset: 0xE21C
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    ChrSetPhysicsFlags(0x0BCC, 0x00000040)
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU605')
    OP_8A(0x01, 0x0BCC, 0xFFFE, '', '')

    Return()

# id: 0x0016 offset: 0xE280
@scena.Code('AniEraseBear')
def AniEraseBear():
    ChrSetPhysicsFlags(0x0BCC, 0x00000040)

    Return()

# id: 0x0017 offset: 0xE290
@scena.Code('AniReset')
def AniReset():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_E2C5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_E2C5(): pass

    label('loc_E2C5')

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

# id: 0x0018 offset: 0xE348
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

# id: 0x0019 offset: 0xE358
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

# id: 0x001A offset: 0xE368
@scena.Code('DefaultFace')
def DefaultFace():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_E3BC',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Jump('loc_E3E7')

    def _loc_E3BC(): pass

    label('loc_E3BC')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    def _loc_E3E7(): pass

    label('loc_E3E7')

    Return()

# id: 0x001B offset: 0xE3E8
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_E402',
    )

    Jump('loc_E443')

    def _loc_E402(): pass

    label('loc_E402')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_E443(): pass

    label('loc_E443')

    Return()

# id: 0x001C offset: 0xE444
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x001D offset: 0xE450
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

# id: 0x001E offset: 0xE4B8
@scena.Code('OnCostumeColor')
def OnCostumeColor():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_E4CA',
    )

    Return()

    def _loc_E4CA(): pass

    label('loc_E4CA')

    If(
        (
            (Expr.Eval, "WeatherCmd(4002, 0xFFFE)"),
            Expr.Return,
        ),
        'loc_E51E',
    )

    OP_4C(0xFE19, 0.05, 0.05, 0.2, 0x0000, 0x03)
    ChrSetRGBA(0xFE19, 0.6, 1.0, 0.9, 0.9, 0, 0x03)
    WeatherCmd(4000, 0xFE19, 0.8, 0x0000, 0x03)

    def _loc_E51E(): pass

    label('loc_E51E')

    Return()

# id: 0x001F offset: 0xE520
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

# id: 0x0020 offset: 0xE584
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

# id: 0x0021 offset: 0xE5FC
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

# id: 0x0022 offset: 0xE66C
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
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x0023 offset: 0xE704
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    OP_3B(0x32, ParamInt(0x13BD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#66w5#66w0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0024 offset: 0xE7F0
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

    OP_3B(0x3A, 0xFFFE, ParamInt(5000), ParamInt(0x1389), ParamInt(0x138A), ParamInt(0))

    Return()

# id: 0x0025 offset: 0xE82C
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0026 offset: 0xE85C
@scena.Code('ShowEquipL')
def ShowEquipL():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0027 offset: 0xE874
@scena.Code('ShowEquipR')
def ShowEquipR():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0028 offset: 0xE88C
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x0029 offset: 0xE8BC
@scena.Code('EraseEquipL')
def EraseEquipL():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x002A offset: 0xE8D4
@scena.Code('EraseEquipR')
def EraseEquipR():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x002B offset: 0xE8EC
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Ahoge01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftRibon01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftRibon02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightRibon01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightRibon02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftBH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightBH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSode', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSode', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Tai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Tai02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftKutu', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightKutu', 0.2)

    Return()

# id: 0x002C offset: 0xEB68
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Ahoge01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftRibon01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftRibon02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightRibon01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightRibon02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSode', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSode', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Tai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Tai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftKutu', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightKutu', 0.2)

    Return()

# id: 0x002D offset: 0xEDE4
@scena.Code('SpringEvOff')
def SpringEvOff():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Ahoge01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftRibon01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftRibon02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightRibon01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightRibon02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightBH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSode', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSode', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Tai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Tai02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftKutu', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightKutu', 0.2)

    Return()

# id: 0x002E offset: 0xEFE0
@scena.Code('SpringOp49Off')
def SpringOp49Off():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'Ahoge01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'LeftSH01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'LeftSH02', 0.0)
    OP_8A(0xFF, 0xFFFE, 'RightSH01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'RightSH02', 0.0)

    Return()

# id: 0x002F offset: 0xF05C
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x0030 offset: 0xF060
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x0031 offset: 0xF064
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x0032 offset: 0xF068
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F12C',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F0FF',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_F123')

    def _loc_F0FF(): pass

    label('loc_F0FF')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F123(): pass

    label('loc_F123')

    Jump('loc_F5FF')

    def _loc_F12C(): pass

    label('loc_F12C')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_F3CE',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F185',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_F185(): pass

    label('loc_F185')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F270',
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
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlStartWalk')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Jump('loc_F3C5')

    def _loc_F270(): pass

    label('loc_F270')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F35B',
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
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlStopDash')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Jump('loc_F3C5')

    def _loc_F35B(): pass

    label('loc_F35B')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_F3C5(): pass

    label('loc_F3C5')

    Jump('loc_F5FF')

    def _loc_F3CE(): pass

    label('loc_F3CE')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_F42A',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_F5FF')

    def _loc_F42A(): pass

    label('loc_F42A')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F4C3',
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

    Jump('loc_F5FF')

    def _loc_F4C3(): pass

    label('loc_F4C3')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F555',
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

    Jump('loc_F5FF')

    def _loc_F555(): pass

    label('loc_F555')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F5D3',
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

    Jump('loc_F5FF')

    def _loc_F5D3(): pass

    label('loc_F5D3')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_F5FF(): pass

    label('loc_F5FF')

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

# id: 0x0033 offset: 0xF628
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
        'loc_F742',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F6D2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlStartWalk')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_F6D2(): pass

    label('loc_F6D2')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWalk')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Jump('loc_F7B9')

    def _loc_F742(): pass

    label('loc_F742')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F796',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_F796(): pass

    label('loc_F796')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F7B9(): pass

    label('loc_F7B9')

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

# id: 0x0034 offset: 0xF7E8
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
        'loc_F85E',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlRun')

    Jump('loc_F880')

    def _loc_F85E(): pass

    label('loc_F85E')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F880(): pass

    label('loc_F880')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F89F',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F89F(): pass

    label('loc_F89F')

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

# id: 0x0035 offset: 0xF8C0
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
        'loc_F937',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDash')

    Jump('loc_F95A')

    def _loc_F937(): pass

    label('loc_F937')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F95A(): pass

    label('loc_F95A')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F979',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F979(): pass

    label('loc_F979')

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

# id: 0x0036 offset: 0xF99C
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

# id: 0x0037 offset: 0xF9F8
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringEvOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0038 offset: 0xFA3C
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x0039 offset: 0xFA7C
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
        'loc_FB71',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FB10',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnL')

    Jump('loc_FB68')

    def _loc_FB10(): pass

    label('loc_FB10')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FB68',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnR')

    def _loc_FB68(): pass

    label('loc_FB68')

    Jump('loc_FBFF')

    def _loc_FB71(): pass

    label('loc_FB71')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FBBC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FBFF')

    def _loc_FBBC(): pass

    label('loc_FBBC')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FBFF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FBFF(): pass

    label('loc_FBFF')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x003A offset: 0xFC20
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
        'loc_FC7E',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_FD67')

    def _loc_FC7E(): pass

    label('loc_FC7E')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_FD09',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_FD67')

    def _loc_FD09(): pass

    label('loc_FD09')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_FD67(): pass

    label('loc_FD67')

    Return()

# id: 0x003B offset: 0xFD68
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003C offset: 0xFDA4
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
        'loc_FDFD',
    )

    Sleep(500)

    Jump('loc_FE09')

    def _loc_FDFD(): pass

    label('loc_FDFD')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_FE09(): pass

    label('loc_FE09')

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

# id: 0x003D offset: 0xFE40
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

    SetEndhookFunction('AniIdle_endhook', 0x000B)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FED9',
    )

    OP_3B(0x32, ParamInt(0x13DF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FF2E')

    def _loc_FED9(): pass

    label('loc_FED9')

    OP_3B(0x32, ParamInt(0x13E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_FF2E(): pass

    label('loc_FF2E')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniIdle')
    SetChrFace(0x03, PseudoChrId.Self, '00001110#236w1', '0[autoM0]', '0#56w4#166w5', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 28)
    Call(ScriptId.Current, 'ShowEquipL')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1', '0[autoM0]', '5', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1110#116wA550[autoE0]', '0[autoM0]', '40000#50e44#100e4#86w0[autoB0]', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 39)
    Call(ScriptId.Current, 'EraseEquipL')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003E offset: 0x10104
@scena.Code('AniIdle_endhook')
def AniIdle_endhook():
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'EraseEquipL')

    Return()

# id: 0x003F offset: 0x1012C
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk111_0.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_101CB',
    )

    LoadEffect(0xFFFE, 0x23, 'battle/cr111_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/cr111_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk111_1.eff', 0x00000000)

    def _loc_101CB(): pass

    label('loc_101CB')

    Return()

# id: 0x0040 offset: 0x101CC
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)

    Return()

# id: 0x0041 offset: 0x101F4
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
    SetEndhookFunction('AniFieldAttack_endhook', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.2, 1.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    Call(ScriptId.Current, 'EraseEquipR')
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x000A))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x138D), ParamInt(0x138E), ParamInt(0x138F), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.3), ParamFloat(0.3), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.3), ParamFloat(0.9), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(1), 0x02)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 19)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 1.0, 0xFFFFFFFF)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.633333)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 44)
    Call(ScriptId.Current, 'ShowEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0042 offset: 0x10578
@scena.Code('AniFieldAttack_endhook')
def AniFieldAttack_endhook():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquipR')

    Return()

# id: 0x0043 offset: 0x105A4
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
    ChrSetPhysicsFlags(0x0BCC, 0x00000040)
    AttachEquip(0xFFFE, 'C_EQU605', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    SetEndhookFunction('AniAssaultAttackEnd', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1390), ParamInt(0x1391), ParamInt(0), ParamInt(0))
    Sleep(66)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(66)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.5, 3.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(100)

    Sleep(133)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0002000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0002000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)
    EffectCmd(0x17, 0xFFFE, 0x03, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(0), -1.0, -1.8, 215.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.1), ParamFloat(0), 2.5, -2.0, -20.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    EffectCmd(0x17, 0xFFFE, 0x05, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x0014))
    OP_5E(0x00, 0x0003, 0.8, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(266)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.666667, 0x00, 0x00)
    ChrClearPhysicsFlags(0x0BCC, 0x00000040)
    Sleep(200)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_41(0xFFFE, 0x01)
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(500)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0044 offset: 0x10B08
@scena.Code('AniAssaultAttackEnd')
def AniAssaultAttackEnd():
    Call(ScriptId.Current, 'BtlDefaultFace')
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x0045 offset: 0x10B5C
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
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttackEnd')
    Sleep(100)

    OP_3B(0x00, ParamInt(0x1785), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'DISARM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0046 offset: 0x10CE0
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0047 offset: 0x10D14
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
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttackEndShort')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'DISARM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x1785), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0048 offset: 0x10E68
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x0049 offset: 0x10E6C
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x004A offset: 0x10E70
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004B offset: 0x10EA8
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0x10EE8
@scena.Code('AniHorseRun')
def AniHorseRun():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0x10F28
@scena.Code('AniHorseDash')
def AniHorseDash():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0x10F68
@scena.Code('AniHorseStop')
def AniHorseStop():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0x10FA8
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0050 offset: 0x11004
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0051 offset: 0x11060
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
        'loc_11172',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5C(0xFFFE, 0x00, 'up_point')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, 8.0, 9.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, 8.0, -6.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_11172(): pass

    label('loc_11172')

    OP_80(0.0)
    OP_04(0x0B, 'AniHorseRearWait')

    Return()

# id: 0x0052 offset: 0x11190
@scena.Code('AniHorseRearEnd')
def AniHorseRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x0053 offset: 0x111D4
@scena.Code('AniHorseRearWait')
def AniHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0054 offset: 0x1120C
@scena.Code('AniHorseRearWalk')
def AniHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0x11248
@scena.Code('AniHorseRearRun')
def AniHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0x11284
@scena.Code('AniHorseRearStop')
def AniHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0057 offset: 0x112E8
@scena.Code('AniHorseRearTurnRight')
def AniHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0058 offset: 0x11350
@scena.Code('AniHorseRearTurnLeft')
def AniHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0059 offset: 0x113B8
@scena.Code('AniHorseRearDash')
def AniHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0x113F4
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
        'loc_1144F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_1144F(): pass

    label('loc_1144F')

    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005B offset: 0x11494
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

# id: 0x005C offset: 0x114EC
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

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0x11540
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

# id: 0x005E offset: 0x11594
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

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0x115EC
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

    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0x11644
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

# id: 0x0061 offset: 0x116D4
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

# id: 0x0062 offset: 0x11730
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

# id: 0x0063 offset: 0x11788
@scena.Code('AniBikeRearWait')
def AniBikeRearWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0064 offset: 0x117D4
@scena.Code('AniBikeRearRun')
def AniBikeRearRun():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0065 offset: 0x11820
@scena.Code('AniBikeRearTilt')
def AniBikeRearTilt():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0066 offset: 0x1186C
@scena.Code('AniBikeRearBack')
def AniBikeRearBack():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_BACK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0067 offset: 0x118B8
@scena.Code('AniBikeRearHandleWait')
def AniBikeRearHandleWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_HANDLE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0068 offset: 0x1190C
@scena.Code('AniBikeRearTiltL')
def AniBikeRearTiltL():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0069 offset: 0x1195C
@scena.Code('AniBikeRearTiltR')
def AniBikeRearTiltR():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006A offset: 0x119AC
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006B offset: 0x119E8
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006C offset: 0x11A24
@scena.Code('AniAttachEQU321')
def AniAttachEQU321():
    LoadAsset('C_EQU321')
    AttachEquip(0xFFFE, 'C_EQU321', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x006D offset: 0x11ABC
@scena.Code('AniDetachEQU321')
def AniDetachEQU321():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU321')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x006E offset: 0x11B10
@scena.Code('AniFishWait')
def AniFishWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'wait', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x006F offset: 0x11B64
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

# id: 0x0070 offset: 0x11C7C
@scena.Code('AniFishHit')
def AniFishHit():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_HIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0071 offset: 0x11CD0
@scena.Code('AniFishHit2')
def AniFishHit2():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_HIT2', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'hit', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0072 offset: 0x11D24
@scena.Code('AniFishEnd')
def AniFishEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'up', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_ENDa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'end', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0073 offset: 0x11DD4
@scena.Code('AniFishResult')
def AniFishResult():
    LoadEffect(0xFFFE, 0x3E, 'minigame/mini01_7.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x00000001, ParamStr('R_hand_point:NODE_ITO'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    SetEndhookFunction('AniFishResult_sub', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_RESULT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(600)

    SetChrFace(0x03, PseudoChrId.Self, 'G', '', '', '#b', '0')
    Sleep(66)

    SetChrFace(0x03, PseudoChrId.Self, '1', '', '3', '#b', '0')
    Sleep(600)

    SetChrFace(0x03, PseudoChrId.Self, 'H', '', '3', '#b', '0')
    Sleep(66)

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '4[autoM4]', '3', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'FISH_RESULTa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0074 offset: 0x11F50
@scena.Code('AniFishResult_sub')
def AniFishResult_sub():
    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    ReleaseEffect(0xFFFE, 0x3E)

    Return()

# id: 0x0075 offset: 0x11F64
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0076 offset: 0x11F90
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_11FAC',
    )

    Return()

    def _loc_11FAC(): pass

    label('loc_11FAC')

    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_BT1_Load')

    Return()

# id: 0x0077 offset: 0x11FD0
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_11FF8',
    )

    Return()

    def _loc_11FF8(): pass

    label('loc_11FF8')

    ChrClearPhysicsFlags(0x0BCC, 0x00000001)
    Call(ScriptId.BtlCom, 'AniBtlInit')
    OP_38(0x0BCC, 0x00, 0x00, 'Ani_BT1_Load')
    Call(ScriptId.Current, 'PlayFakeEffect')

    Return()

# id: 0x0078 offset: 0x12044
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12175',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_12086',
    )

    Jump('loc_1216C')

    def _loc_12086(): pass

    label('loc_12086')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_120F6',
    )

    OP_3B(0x32, ParamInt(0x1408), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1215D')

    def _loc_120F6(): pass

    label('loc_120F6')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x12E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1215D',
    )

    OP_3B(0x32, ParamInt(0x1405), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1215D(): pass

    label('loc_1215D')

    Sleep(1000)

    OP_3B(0x39, 0xFFFE)

    def _loc_1216C(): pass

    label('loc_1216C')

    Jump('loc_123BF')

    def _loc_12175(): pass

    label('loc_12175')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_121EB',
    )

    OP_3B(0x32, ParamInt(0x13B6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_123BF')

    def _loc_121EB(): pass

    label('loc_121EB')

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
        'loc_1227F',
    )

    OP_3B(0x32, ParamInt(0x13B5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_123BF')

    def _loc_1227F(): pass

    label('loc_1227F')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122F5',
    )

    OP_3B(0x32, ParamInt(0x13B8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_123BF')

    def _loc_122F5(): pass

    label('loc_122F5')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1236A',
    )

    OP_3B(0x32, ParamInt(0x13B3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_123BF')

    def _loc_1236A(): pass

    label('loc_1236A')

    OP_3B(0x32, ParamInt(0x13B4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_123BF(): pass

    label('loc_123BF')

    Return()

# id: 0x0079 offset: 0x123C0
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_123FD',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x138B), ParamInt(0x138C), ParamInt(0), ParamInt(0))

    Jump('loc_1241D')

    def _loc_123FD(): pass

    label('loc_123FD')

    OP_3B(0x3A, 0xFFFE, ParamInt(5000), ParamInt(0x1389), ParamInt(0), ParamInt(0))

    def _loc_1241D(): pass

    label('loc_1241D')

    Return()

# id: 0x007A offset: 0x12420
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_1243D',
    )

    Jump('loc_1243D')

    def _loc_1243D(): pass

    label('loc_1243D')

    Return()

# id: 0x007B offset: 0x12440
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x13B7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007C offset: 0x12498
@scena.Code('AniBtlWait')
def AniBtlWait():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x007D offset: 0x1251C
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x007E offset: 0x12558
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_125B9',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnL')

    Jump('loc_12642')

    def _loc_125B9(): pass

    label('loc_125B9')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12642',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnR')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_TURN_R', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_12642(): pass

    label('loc_12642')

    Return()

# id: 0x007F offset: 0x12644
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x13AF))

    Return()

# id: 0x0080 offset: 0x12660
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x13AE))

    Return()

# id: 0x0081 offset: 0x1267C
@scena.Code('AniBtlStepInKisinPt')
def AniBtlStepInKisinPt():
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0082 offset: 0x126A8
@scena.Code('AniBtlStepOutKisinPt')
def AniBtlStepOutKisinPt():
    Return()

# id: 0x0083 offset: 0x126AC
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 1.0, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x03)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ATTACK', 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0666667)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12801',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_127E1',
    )

    Jump('loc_12801')

    def _loc_127E1(): pass

    label('loc_127E1')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x138D), ParamInt(0x138E), ParamInt(0x138F), ParamInt(0))

    def _loc_12801(): pass

    label('loc_12801')

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(1), 0.0, -3.0, 0.0, ParamFloat(0.3), ParamFloat(0.3), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(-0.3), ParamFloat(0.9), ParamFloat(1), 0.0, -6.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(1), 0x02)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x000A))

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1294F',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.3)

    def _loc_1294F(): pass

    label('loc_1294F')

    CameraCmd(0x0A, 0.0, 0.005, 0.25, 0, 400, 0, 0, 0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 29)
    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 55)
    Call(ScriptId.Current, 'ShowEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0084 offset: 0x12A94
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_12ABD',
    )

    Jump('loc_12B12')

    def _loc_12ABD(): pass

    label('loc_12ABD')

    OP_3B(0x32, ParamInt(0x13AB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12B12(): pass

    label('loc_12B12')

    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0085 offset: 0x12B28
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
        'loc_12BEA',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWeakDamage')
    OP_6C(PseudoChrId.Self, 1.05, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 30)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)

    Jump('loc_12C29')

    def _loc_12BEA(): pass

    label('loc_12BEA')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDamage')

    def _loc_12C29(): pass

    label('loc_12C29')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0086 offset: 0x12C38
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_12C61',
    )

    Jump('loc_12C81')

    def _loc_12C61(): pass

    label('loc_12C61')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x13A7), ParamInt(0x13A8), ParamInt(0x13A9), ParamInt(0))

    def _loc_12C81(): pass

    label('loc_12C81')

    Return()

# id: 0x0087 offset: 0x12C84
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_12CAD',
    )

    Jump('loc_12D02')

    def _loc_12CAD(): pass

    label('loc_12CAD')

    OP_3B(0x32, ParamInt(0x13A9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12D02(): pass

    label('loc_12D02')

    Return()

# id: 0x0088 offset: 0x12D04
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
        'loc_12DAB',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDeada')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Jump('loc_12E82')

    def _loc_12DAB(): pass

    label('loc_12DAB')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDead')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEAD', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_12E82(): pass

    label('loc_12E82')

    Return()

# id: 0x0089 offset: 0x12E84
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWeak')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WEAK', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x008A offset: 0x12F04
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')

    Return()

# id: 0x008B offset: 0x12F1C
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, PseudoChrId.Self, '9', '7', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDead')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEAD', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_130ED',
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
        'loc_13064',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_13003',
    )

    Jump('loc_13064')

    def _loc_13003(): pass

    label('loc_13003')

    OP_3B(0x32, ParamInt(0x13AA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x13AA))

    def _loc_13064(): pass

    label('loc_13064')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDeada')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(500)

    Jump('loc_1320A')

    def _loc_130ED(): pass

    label('loc_130ED')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_13191',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_13130',
    )

    Jump('loc_13191')

    def _loc_13130(): pass

    label('loc_13130')

    OP_3B(0x32, ParamInt(0x13AA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x13AA))

    def _loc_13191(): pass

    label('loc_13191')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDeada')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_1320A(): pass

    label('loc_1320A')

    Return()

# id: 0x008C offset: 0x1320C
@scena.Code('AniBtlAria')
def AniBtlAria():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x17),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13280',
    )

    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAria')
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x13A3), ParamInt(0x13A3), ParamFloat(-1), ParamFloat(0))

    Jump('loc_1334B')

    def _loc_13280(): pass

    label('loc_13280')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_132FA',
    )

    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAria')
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0), ParamInt(0), ParamFloat(-1), ParamFloat(0))

    Jump('loc_1334B')

    def _loc_132FA(): pass

    label('loc_132FA')

    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAria')
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x13A3), ParamInt(0x13A4), ParamFloat(-1), ParamFloat(0))

    def _loc_1334B(): pass

    label('loc_1334B')

    Return()

# id: 0x008D offset: 0x1334C
@scena.Code('AniBtlArts')
def AniBtlArts():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x4B, 0x00FA, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.05, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArts')
    Call(ScriptId.Current, 'EraseEquipR')
    WaitAnimeClipFrames(PseudoChrId.Self, 7)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 16)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_13450',
    )

    Jump('loc_13470')

    def _loc_13450(): pass

    label('loc_13450')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x13A5), ParamInt(0x13A6), ParamInt(0), ParamInt(0))

    def _loc_13470(): pass

    label('loc_13470')

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArtsa')
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArtsb')
    Call(ScriptId.Current, 'ShowEquip')
    OP_76(PseudoChrId.Self, 'Rarm', 'BTL_ARTSb', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x008E offset: 0x13624
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

    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlItem')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ITEM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '32#116w3332[autoE2]', '2[autoM2]', '#85e04#46w601#66w#100e0[autoB0]', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x13A5), ParamInt(0x13A6), ParamInt(0), ParamInt(0))
    WaitAnimeClipFrames(PseudoChrId.Self, 20)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x008F offset: 0x1388C
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x13B0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0090 offset: 0x138E4
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x13B1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0091 offset: 0x1393C
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x13B2), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0092 offset: 0x13994
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x13BE), ParamInt(0x13BF), ParamInt(0), ParamInt(0))

    Return()

# id: 0x0093 offset: 0x139B8
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139ED',
    )

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x1409))

    Jump('loc_13A07')

    def _loc_139ED(): pass

    label('loc_139ED')

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x1407))

    def _loc_13A07(): pass

    label('loc_13A07')

    Return()

# id: 0x0094 offset: 0x13A08
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlTensionMax')

    Return()

# id: 0x0095 offset: 0x13A24
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlFrontStep')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ATTACK', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 22)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13C3C',
    )

    OP_3B(0x32, ParamInt(0x13CE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13CBA')

    def _loc_13C3C(): pass

    label('loc_13C3C')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_13C65',
    )

    Jump('loc_13CBA')

    def _loc_13C65(): pass

    label('loc_13C65')

    OP_3B(0x32, ParamInt(0x13C0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_13CBA(): pass

    label('loc_13CBA')

    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x000A))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.3), ParamFloat(1.1), ParamFloat(1), 2.0, -5.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.7), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.3), ParamFloat(0.3), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.3), ParamFloat(0.9), ParamFloat(1), -3.0, 5.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(1), 0x02)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))
    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(1000)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlBackStep')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
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
        'loc_13F80',
    )

    EffectCmd(0x12, 0xFFFE, 0x03FA)

    def _loc_13F80(): pass

    label('loc_13F80')

    EffectCmd(0x12, 0xFFFE, 0x0038)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x0096 offset: 0x13FA8
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')

    Return()

# id: 0x0097 offset: 0x14000
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlRun')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0098 offset: 0x14068
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
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDash')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF2, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ATTACK', 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0666667)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x000A))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(1), 0.0, -3.0, 0.0, ParamFloat(0.3), ParamFloat(0.3), ParamFloat(1), 0x02)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.3), ParamFloat(0.9), ParamFloat(1), 0.0, -6.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(1), 0x02)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_14356',
    )

    Jump('loc_14376')

    def _loc_14356(): pass

    label('loc_14356')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x141E), ParamInt(0x141F), ParamInt(0x1420), ParamInt(0))

    def _loc_14376(): pass

    label('loc_14376')

    CameraCmd(0x09, 0.1, 0.1, 0.3)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_0', ScriptId.Current)
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlBackStep')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')

    Return()

# id: 0x0099 offset: 0x14484
@scena.Code('_Lambda_0')
def _Lambda_0():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x009A offset: 0x144D4
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x009B offset: 0x144EC
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x009C offset: 0x14504
@scena.Code('AniBtlLinkQuickRevive')
def AniBtlLinkQuickRevive():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x13D0), ParamStr('NODE_R_HAND'))
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x009D offset: 0x14554
@scena.Code('AniBtlLinkQuickRevive2')
def AniBtlLinkQuickRevive2():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x13D0), ParamStr('NODE_R_HAND'))
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x009E offset: 0x145A4
@scena.Code('AniBtlLinkQuickCure')
def AniBtlLinkQuickCure():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x13CF), ParamStr('R_hand_point:NODE_EFFECT01'))
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x009F offset: 0x14604
@scena.Code('AniBtlLinkQuickCure2')
def AniBtlLinkQuickCure2():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x13CF), ParamStr('R_hand_point:NODE_EFFECT01'))
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x00A0 offset: 0x14664
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x00A1 offset: 0x14684
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x00A2 offset: 0x146A0
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'EraseEquipR')
    SetChrFace(0x03, PseudoChrId.Self, '333332', '', '', '#b', '0')
    Sleep(333)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '333332', '', '', '#b', '0')
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttack')
    WaitAnimeClipFrames(PseudoChrId.Self, 5)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 7)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 16)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A3 offset: 0x147D8
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "BattleCmd(0xA9, 0x00, 0x00000000)"),
            (Expr.PushLong, 0x1951),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14852',
    )

    OP_3B(0x32, ParamInt(0x13A0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14918')

    def _loc_14852(): pass

    label('loc_14852')

    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_148C3',
    )

    OP_3B(0x32, ParamInt(0x13A1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14918')

    def _loc_148C3(): pass

    label('loc_148C3')

    OP_3B(0x32, ParamInt(0x139F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_14918(): pass

    label('loc_14918')

    Return()

# id: 0x00A4 offset: 0x1491C
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    Call(ScriptId.Current, 'EraseEquipR')
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A5 offset: 0x14974
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x00A6 offset: 0x1499C
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x00A7 offset: 0x149C0
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x00A8 offset: 0x149C4
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x00A9 offset: 0x149F8
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x13A5), ParamInt(0x13A6))
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x00AA offset: 0x14A34
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x00AB offset: 0x14A58
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x00AC offset: 0x14A8C
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.Current, 'EraseEquipR')
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x00AD offset: 0x14AC0
@scena.Code('AniBtlValiantHeal_End')
def AniBtlValiantHeal_End():
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x00AE offset: 0x14AD4
@scena.Code('AniBtlKisinItemPa')
def AniBtlKisinItemPa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00AF offset: 0x14B18
@scena.Code('AniBtlKisinChargePa')
def AniBtlKisinChargePa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B0 offset: 0x14B5C
@scena.Code('AniBtlKisinSinkiPa')
def AniBtlKisinSinkiPa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B1 offset: 0x14BA0
@scena.Code('AniBtlKisinPartnerArts')
def AniBtlKisinPartnerArts():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x00B2 offset: 0x14BE4
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B3 offset: 0x14C20
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B4 offset: 0x14C84
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x00B5 offset: 0x14CC0
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B6 offset: 0x14CF8
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
        'loc_14D37',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_14D71')

    def _loc_14D37(): pass

    label('loc_14D37')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_14D64',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_14D71')

    def _loc_14D64(): pass

    label('loc_14D64')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_14D71(): pass

    label('loc_14D71')

    Return()

# id: 0x00B7 offset: 0x14D74
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14DE4',
    )

    OP_3B(0x32, ParamInt(0x13BB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14EA9')

    def _loc_14DE4(): pass

    label('loc_14DE4')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14E54',
    )

    OP_3B(0x32, ParamInt(0x13B9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14EA9')

    def _loc_14E54(): pass

    label('loc_14E54')

    OP_3B(0x32, ParamInt(0x13BA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_14EA9(): pass

    label('loc_14EA9')

    Return()

# id: 0x00B8 offset: 0x14EAC
@scena.Code('AniBtlWin')
def AniBtlWin():
    Call(ScriptId.Current, 'SpringOff')
    CameraCmd(0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_1', ScriptId.Current)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '2[autoM2]', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000180)
    ChrSetPhysicsFlags(0x0BCC, 0x00000180)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0BCC, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15041',
    )

    SetChrFace(0x03, PseudoChrId.Self, '0#136w3#36w0#86w2[autoE2]', '4[autoM4]', '0[autoB0]', '#b', '0')
    Call(ScriptId.Current, 'VoiceWin_play')

    Jump('loc_15089')

    def _loc_15041(): pass

    label('loc_15041')

    SetChrFace(0x03, PseudoChrId.Self, '0#136w5#36w0#86w5', '0[autoM0]', '0[autoB0]', '#b', '0')
    Call(ScriptId.Current, 'VoiceWin_play')

    def _loc_15089(): pass

    label('loc_15089')

    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_150AB',
    )

    Jump('loc_150F6')

    def _loc_150AB(): pass

    label('loc_150AB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_150DE',
    )

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM4]', '', '#b', '0')

    Jump('loc_150F6')

    def _loc_150DE(): pass

    label('loc_150DE')

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM0]', '', '#b', '0')

    def _loc_150F6(): pass

    label('loc_150F6')

    WaitAnimeClipFrames(PseudoChrId.Self, 100)
    TerminateThread(PseudoChrId.Self, 0x02)
    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.25, 1.0, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0BCC, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)
    Sleep(1000)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000180)
    ChrClearPhysicsFlags(0x0BCC, 0x00000180)

    Return()

# id: 0x00B9 offset: 0x151F0
@scena.Code('_Lambda_1')
def _Lambda_1():
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.27, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 0.8, 0)
    CameraCmd(0x0B, 0x03, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x4B, 0x0683, 0x03)
    Sleep(1666)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.21, 0.02, 667)
    CameraRotateByTarget(0xFFFE, '', 0x03, -0.0, 10.36, 0.0, 667, 0x01)
    CameraSetDistance(0x03, 1.2, 667)
    BattleCmd(0x4B, 0x029B, 0x03)
    Sleep(666)

    BattleCmd(0x4B, 0x0960, 0x03)
    Sleep(2400)

    Return()

# id: 0x00BA offset: 0x152B4
@scena.Code('AniBtlWinHitouchdb')
def AniBtlWinHitouchdb():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB_a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BB offset: 0x15330
@scena.Code('AniBtlWinHitouchdbb')
def AniBtlWinHitouchdbb():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HITOUCHDB_b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00BC offset: 0x15394
@scena.Code('AniBtlWinHoldL')
def AniBtlWinHoldL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLDa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BD offset: 0x15404
@scena.Code('AniBtlWinHoldHandR')
def AniBtlWinHoldHandR():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLD_HAND_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_HOLD_HAND_Ra', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BE offset: 0x15484
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '2[autoM2]', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000180)
    ChrSetPhysicsFlags(0x0BCC, 0x00000180)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0BCC, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#136w5#36w0#86w5', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM4]', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 100)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00BF offset: 0x155F4
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0BCC, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#136w5#36w0#86w5', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x13BC), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0BCC, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x34, ParamInt(0x13BC))

    Return()

# id: 0x00C0 offset: 0x15768
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C1 offset: 0x157A8
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvAkubi', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEvAkubi')
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x00C2 offset: 0x15828
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x00C3 offset: 0x15834
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    OP_80(0.2)
    SetChrFace(0x03, PseudoChrId.Self, '222111111110[autoE0]', '[autoM4]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttackEnd')
    Sleep(100)

    OP_3B(0x00, ParamInt(0x1785), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'DISARM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00C4 offset: 0x159C0
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00C5 offset: 0x159E4
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_159FC',
    )

    Jump('loc_159FC')

    def _loc_159FC(): pass

    label('loc_159FC')

    Return()

# id: 0x00C6 offset: 0x15A00
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
        'loc_15B38',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x13BD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_15B45')

    def _loc_15B38(): pass

    label('loc_15B38')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_15B45(): pass

    label('loc_15B45')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetEndhookFunction('SpringOn', 0x000B)
    SetChrFace(0x03, PseudoChrId.Self, '00005#76w0#46w5#46w4', 'A#20sB', '0#96w#90e33#75e3#65e33#50e33#40e33#57e3332', '#b', '0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15C0B',
    )

    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '', '#100s4', '', '#b', '0')

    Jump('loc_15C28')

    def _loc_15C0B(): pass

    label('loc_15C0B')

    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '', '#100s4', '', '#b', '0')

    def _loc_15C28(): pass

    label('loc_15C28')

    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '', '4[autoM4]', '', '#b', '0')
    Sleep(1400)

    SetChrFace(0x03, PseudoChrId.Self, '', '4', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C7 offset: 0x15CB4
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr111_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr111_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr111_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr111_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr111_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr111_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr111_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/cr111_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/cr111_00_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr111_00_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr111_00_10.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOn')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    ReleaseAsset('C_EQU605')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)
    LoadAsset('C_EQU605_C04')
    AttachEquip(0xFFFE, 'C_EQU605_C04', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    LoadAsset('C_EQU605_C04')
    AttachEquip(0xFFFE, 'C_EQU605_C04', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    OP_4E(1.5, 1.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.24, 0.06, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, -1.61, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.18, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.24, 0.09, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -1.65, 0.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x00, 1.15, 1000)
    CameraCmd(0x0B, 0x00, 35.0, 0x03E8)
    BattleCmd(0x4B, 0x03E8, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft00_00')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT00_00', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'BTL_CRAFT00_00_L', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    EffectCmd(0x15, 0xFFFE, 0x0A, 0.05, 0.0, 0.01, 1.0, 0, 0x03)
    OP_5E(0x00, 0x0002, 0.1, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 20)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_162ED',
    )

    Jump('loc_16342')

    def _loc_162ED(): pass

    label('loc_162ED')

    OP_3B(0x32, ParamInt(0x1392), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16342(): pass

    label('loc_16342')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.1, 0xFFFFFFFF)
    Sleep(200)

    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_2', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT00_01', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'BTL_CRAFT00_01_L', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '4442[autoE2]', '444220[autoM0]', '0[autoB0]', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x04000000, ParamStr('NODE_R_HAND'), ParamFloat(-0.1), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x04000000, ParamStr('NODE_L_HAND'), ParamFloat(0.1), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_RED'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_BLUE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_RED'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_BLUE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x0064))
    Sleep(100)

    Sleep(133)

    OP_5E(0x01, 0x00C8)
    CameraCmd(0x09, 0.125, 0.125, 0.2)
    OP_3B(0xFF, 0.6, 0.6, 0.2)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    EffectCmd(0x15, 0xFFFE, 0x0A, 0.02, 0.0, 0.1, 1.0, 200, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x0C)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    Sleep(66)

    Sleep(266)

    SetChrFace(0x03, PseudoChrId.Self, '', '0', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 29)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.05, 0.88, 0.07, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 0.68, 3.17, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.21, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x01, 0xFFFE, '', 0.19, 0.85, 0.07, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x01, 6.02, 103.13, -0.0, 1200, 0x01)
    CameraSetDistance(0x01, 2.06, 1200)
    BattleCmd(0x4B, 0x04B0, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_RED'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_BLUE'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x04000000, ParamStr('R_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_RED'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_BLUE'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x04000000, ParamStr('L_hand_point:NODE_EFFECT_PURPLE'), ParamFloat(0), ParamFloat(0.2), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_5E(0x00, 0x0003, 0.5, 60, 1, 600, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 5)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(66)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT00_03', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'BTL_CRAFT00_03_L', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0', '1', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(333)

    EffectCmd(0x15, 0xFFFE, 0x0A, 0.1, 0.02, 0.1, 1.0, 300, 0x03)
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x08)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_170FB',
    )

    Jump('loc_17150')

    def _loc_170FB(): pass

    label('loc_170FB')

    OP_3B(0x32, ParamInt(0x1393), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_17150(): pass

    label('loc_17150')

    SetChrFace(0x03, PseudoChrId.Self, '', '0[autoM0]', '', '#b', '0')
    OP_4E(1.0, 0.0, 0x00, 0x00)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.43, 0.93, 2.62, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.41, 150.24, -0.0, 0, 0x01)
    CameraSetDistance(0x00, 6.0, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.41, 160.24, -0.0, 300, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.566667, 0x00, 0x03)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.2, 1.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_3', ScriptId.Current)
    EffectCmd(0x15, 0xFFFE, 0x0A, 0.05, 0.0, 0.05, 1.0, 300, 0x03)
    Sleep(100)

    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x0C)
    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    BattleCmd(0x8A)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    Sleep(200)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x00, 2.0, 300)
    BattleCmd(0x4B, 0x012C, 0x00)
    CameraCmd(0x0A, 0.125, 0.125, 0.01, 400, 500, 700, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Call(ScriptId.Current, 'AniBtlCraftDamageZan')
    Sleep(266)

    CameraSetHeight(0x00, 1.5, 1000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT00_03a', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'BTL_CRAFT00_03a_L', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(1333)

    ReleaseAsset('C_EQU605_C04')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU605_C04')
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
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
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    AttachEquip(0xFFFE, 'C_EQU605', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00C8 offset: 0x1768C
@scena.Code('_Lambda_2')
def _Lambda_2():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.19, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, -3.26, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.59, 0)
    CameraCmd(0x0B, 0x00, 34.6274, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.09, 100)
    CameraRotateByTarget(0xFFFE, '', 0x00, -3.52, 0.0, 0.0, 100, 0x01)
    BattleCmd(0x4B, 0x0064, 0x00)
    Sleep(100)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.0, 1.26, 0.09, 133)
    CameraRotateByTarget(0xFFFE, '', 0x00, -5.91, 0.12, -0.0, 133, 0x01)
    CameraSetDistance(0x00, 1.6, 133)
    BattleCmd(0x4B, 0x0085, 0x00)
    Sleep(133)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.0, 1.21, 0.09, 100)
    CameraRotateByTarget(0xFFFE, '', 0x00, -3.47, 0.09, -0.0, 100, 0x01)
    CameraSetDistance(0x00, 1.81, 100)
    BattleCmd(0x4B, 0x0064, 0x00)
    Sleep(100)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.75, 0.11, 233)
    CameraRotateByTarget(0xFFFE, '', 0x00, 8.56, 0.0, 0.0, 233, 0x01)
    CameraSetDistance(0x00, 2.33, 233)
    CameraCmd(0x0B, 0x00, 41.5546, 0x00E9)
    BattleCmd(0x4B, 0x00E9, 0x00)
    Sleep(233)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.82, 0.1, 267)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.05, 0.0, 0.0, 267, 0x01)
    CameraSetDistance(0x00, 2.31, 267)
    CameraCmd(0x0B, 0x00, 42.9111, 0x010B)
    BattleCmd(0x4B, 0x010B, 0x00)
    Sleep(266)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.83, 0.09, 167)
    CameraRotateByTarget(0xFFFE, '', 0x00, 6.79, 0.0, 0.0, 167, 0x01)
    CameraSetDistance(0x00, 2.3, 167)
    CameraCmd(0x0B, 0x00, 42.9957, 0x00A7)
    BattleCmd(0x4B, 0x00A7, 0x00)
    Sleep(166)

    Return()

# id: 0x00C9 offset: 0x178DC
@scena.Code('_Lambda_3')
def _Lambda_3():
    Sleep(133)

    EffectCmd(0x17, 0xFFFE, 0x07, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(-2), ParamFloat(0.8), ParamFloat(0), -2.8, -5.0, 215.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0.7), ParamFloat(1), ParamFloat(0), 4.3, -5.0, -25.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.4), ParamFloat(0.6), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.4), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.4), ParamFloat(1.4), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.4), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.4), ParamFloat(0.6), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.4), ParamFloat(1.4), ParamFloat(0), 1.0, -1.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1), 0x02)

    Return()

# id: 0x00CA offset: 0x17B48
@scena.Code('AniBtlCraftDamage')
def AniBtlCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00CB offset: 0x17B98
@scena.Code('AniBtlCraftDamageZan')
def AniBtlCraftDamageZan():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00CC offset: 0x17BE8
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr111_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr111_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr111_01_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr111_01_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr111_01_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr111_01_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr111_01_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/cr111_01_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/cr111_01_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr111_01_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr111_01_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr089_01_04.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/gra00.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOn')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    ReleaseAsset('C_CHR975')
    OP_8A(0x01, 0x0BCC, 0xFFFE, '', '')
    BattleCreateTempChar(0x0001, 0xFFFF, 'C_CHR975_C00', 'chr975')
    ChrSetPhysicsFlags(0x0B69, 0x000002A0)
    OP_8A(0x00, 0x0B69, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    ChrSetPhysicsFlags(0x0BCC, 0x000000E0)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSaveChrPosition(0xFFFE, 0x00000001)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.93, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, -11.99, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.34, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    BattleCmd(0x4B, 0x042B, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0B69, 0x00, 0x00, 'AniBtlCraft01_00')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT01_00', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '33332#36w002[autoE2]', '0#46wHH154', '#90e0000333189', '#b', '0')
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x006E))
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_4', ScriptId.Current)
    OP_4E(1.1, 0.0, 0x03, 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 28)
    OP_4E(1.2, 1.0, 0x03, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.2), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    OP_3B(0xFF, 0.3, 0.3, 0.2)
    WaitAnimeClipFrames(PseudoChrId.Self, 40)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(3), ParamFloat(1), 0x09)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_5', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0B69, 0x00, 0x00, 'AniBtlCraft01_01')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT01_01', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '4,#36wA322A4CC4[autoE4]', 'H,224', '#90e8,#100e8888#92e7#36w1', '4,#36wA32244CC4[autoE4]', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_4E(1.3, 1.0, 0x03, 0x01)
    ReleaseEffect(0xFFFE, 0x37)
    ReleaseEffect(0xFFFE, 0x38)
    EffectCmd(0x0E, 0xFFFE, 0x0B, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    SetChrFace(0x03, PseudoChrId.Self, '', '4[autoM4]', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 25)
    SetChrFace(0x03, PseudoChrId.Self, '', '4', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 30)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.51), ParamFloat(0), -25.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleDeleteTempChar(0x0001)
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHR975_C00', 'chr975')
    ChrSetPhysicsFlags(0x0B68, 0x000002A0)
    BattleSetChrPos(0x0B68, 0xFFFA, 0.0, 4.0, 0.0, -1.0, 0x00, 0x00)
    AnimeClipLoadByCatalog(0x0B68, 0x00000100)
    BattleCreateTempChar(0x0001, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B69, 0x00000260)
    BattleSetChrPos(0x0B69, 0xFFFA, 0.0, 4.0, 0.0, -1.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0x0B68, '', -0.0, 0.1, 0.19, 0)
    CameraRotateByTarget(0x0B68, '', 0x00, 0.14, -41.37, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.58, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_CRAFT01_02a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0x0B68, 0x00000003, ParamStr('NODE_ROOT'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_18605',
    )

    Jump('loc_1865A')

    def _loc_18605(): pass

    label('loc_18605')

    OP_3B(0x32, ParamInt(0x140D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1865A(): pass

    label('loc_1865A')

    WaitAnimeClip(0x0B68, 0.0, 0x00)

    CameraSetPosByTarget(0x00, 0x0B68, '', 0.0, 0.1, 0.11, 200)
    CameraRotateByTarget(0x0B68, '', 0x00, 0.14, -38.8, 0.0, 200, 0x01)
    CameraSetDistance(0x00, 1.36, 200)
    BattleCmd(0x4B, 0x00C8, 0x00)
    BattleCmd(0x4B, 0x0085, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x35)
    OP_3B(0xFF, 1.0, 1.0, 0.2)
    CameraCmd(0x09, 0.125, 0.125, 0.1)
    OP_5E(0x00, 0x0002, 0.6, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    CameraSetPosByTarget(0x00, 0x0B68, '', -0.0, 0.1, 0.11, 133)
    CameraRotateByTarget(0x0B68, '', 0x00, 0.13, -38.63, 0.0, 133, 0x01)
    CameraSetDistance(0x00, 1.31, 133)
    BattleCmd(0x4B, 0x0085, 0x00)
    OP_5E(0x01, 0x0320)
    Sleep(133)

    CameraSetPosByTarget(0x00, 0x0B68, '', 0.0, 0.1, 0.11, 133)
    CameraRotateByTarget(0x0B68, '', 0x00, 0.14, -38.8, 0.0, 133, 0x01)
    CameraSetDistance(0x00, 1.36, 133)
    OP_4C(0x0B68, 1.0, 1.0, 1.0, 0x03E8, 0x03)
    WaitAnimeClip(0x0B68, 0.0, 0x00)

    CameraSetPosByTarget(0x00, 0x0B68, '', 0.0, 0.1, 0.11, 767)
    CameraRotateByTarget(0x0B68, '', 0x00, 3.69, -35.57, 0.0, 767, 0x01)
    CameraSetDistance(0x00, 1.37, 767)
    BattleCmd(0x4B, 0x02FF, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_CRAFT01_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    OP_3B(0xFF, 0.2, 1.0, 0.9)
    Sleep(766)

    CameraRotateByTarget(0x0B68, '', 0x00, 3.96, -35.22, 0.0, 100, 0x01)
    CameraSetDistance(0x00, 2.89, 100)
    BattleCmd(0x4B, 0x0064, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B69, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -30.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0x0B69, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -30.0, 0.0, ParamFloat(0.37), ParamFloat(0.37), ParamFloat(0.37), 0x0C)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0x0B69, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(1.5), 0.0, -30.0, 0.0, ParamFloat(0.05), ParamFloat(0.05), ParamFloat(0.05), 0x0D)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0x0B69, 0x0000000C, ParamStr(''), ParamFloat(-1.5), ParamFloat(0), ParamFloat(1.5), 0.0, -30.0, 0.0, ParamFloat(0.05), ParamFloat(0.05), ParamFloat(0.05), 0x0E)
    OP_3B(0xFF, 0.6, 0.6, 0.6)
    OP_5E(0x00, 0x0002, 0.15, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    EffectCmd(0x15, 0xFFFE, 0x0D, 0.15, 0.15, 0.0, 1.0, 0, 0x03)
    EffectCmd(0x15, 0xFFFE, 0x0E, 0.15, 0.15, 0.0, 1.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B68, 0x00000040)
    CameraSetPosByTarget(0x00, 0x0B68, '', -0.0, 0.1, 0.11, 467)
    CameraRotateByTarget(0x0B68, '', 0x00, 4.0, -35.21, 0.0, 467, 0x01)
    CameraSetDistance(0x00, 3.21, 467)
    BattleCmd(0x4B, 0x01D3, 0x00)
    Sleep(666)

    OP_5E(0x01, 0x0320)
    Sleep(333)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_18B1D',
    )

    Jump('loc_18B72')

    def _loc_18B1D(): pass

    label('loc_18B1D')

    OP_3B(0x32, ParamInt(0x1395), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_18B72(): pass

    label('loc_18B72')

    Sleep(333)

    AnimeClipReleaseByCatalog(0x0B68, 0x00000100)
    BattleDeleteTempChar(0x0000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4[autoM4]', '0[autoB0]', '#b', '0')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 180.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0C)
    CameraCmd(0x00)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, -38.0, 0.0, 0, 0x01)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    EffectCmd(0x13, 0xFFFE, 0x03, 0x02DA)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x03, 1.5, 3000)
    CameraCmd(0x11, 0x00, 0.0, 12.0, 0.0, 0x0BB8, 0x01)
    BattleCmd(0x4B, 0x0BB8, 0x03)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(500)

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_18D60(): pass

    label('loc_18D60')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_18DF6',
    )

    Sleep(133)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleTargetsIterNext(0xFFFE)
    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFF9, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_18D60')

    def _loc_18DF6(): pass

    label('loc_18DF6')

    Sleep(1500)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
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
    BattleDeleteTempChar(0x0001)
    ChrClearPhysicsFlags(0x0BCC, 0x000000E0)
    ReleaseEffect(0xFFFE, 0x39)
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFE9, 0.0, -1.0)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0))

    Return()

# id: 0x00CD offset: 0x18FB4
@scena.Code('_Lambda_4')
def _Lambda_4():
    Sleep(233)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_18FE4',
    )

    Jump('loc_19039')

    def _loc_18FE4(): pass

    label('loc_18FE4')

    OP_3B(0x32, ParamInt(0x1394), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_19039(): pass

    label('loc_19039')

    Sleep(833)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 3.18, 0.09, 333)
    CameraRotateByTarget(0xFFFE, '', 0x00, -50.12, 0.0, 0.0, 333, 0x01)
    CameraSetDistance(0x00, 3.57, 333)
    Sleep(333)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 4.19, 0.09, 267)
    CameraRotateByTarget(0xFFFE, '', 0x00, -58.58, 0.0, 0.0, 267, 0x01)
    CameraSetDistance(0x00, 4.39, 267)
    Sleep(266)

    Return()

# id: 0x00CE offset: 0x190CC
@scena.Code('_Lambda_5')
def _Lambda_5():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.24, 1.18, -0.12, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.33, 45.92, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.46, 0)
    CameraCmd(0x0B, 0x00, 34.6274, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.24, 1.18, -0.14, 667)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.31, 45.22, 0.0, 667, 0x01)
    CameraSetDistance(0x00, 1.48, 667)
    BattleCmd(0x4B, 0x029B, 0x00)
    Sleep(666)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.23, 1.2, -0.14, 367)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.49, 45.22, 0.0, 367, 0x01)
    CameraSetDistance(0x00, 1.47, 367)
    BattleCmd(0x4B, 0x016F, 0x00)
    Sleep(366)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.22, 1.26, 0.31, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, -0.83, 60.2, 0.0, 300, 0x01)
    CameraSetDistance(0x00, 1.19, 300)
    BattleCmd(0x4B, 0x012C, 0x00)
    Sleep(300)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.2, 1.27, 0.38, 400)
    CameraRotateByTarget(0xFFFE, '', 0x00, -1.38, 62.67, 0.0, 400, 0x01)
    CameraSetDistance(0x00, 1.14, 400)
    BattleCmd(0x4B, 0x0190, 0x00)
    Sleep(400)

    Return()

# id: 0x00CF offset: 0x19268
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr111_02_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr111_02_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr111_02_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr111_02_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr111_02_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr111_02_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr111_02_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/cr111_02_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/cr111_02_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr111_02_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr111_02_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr111_02_11.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOn')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    ReleaseAsset('C_EQU605')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU605_C03')
    AttachEquip(0xFFFE, 'C_EQU605_C03', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_195FE',
    )

    Jump('loc_19653')

    def _loc_195FE(): pass

    label('loc_195FE')

    OP_3B(0x32, ParamInt(0x1396), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_19653(): pass

    label('loc_19653')

    SetChrFace(0x03, PseudoChrId.Self, 'A,AAAAA#1s3', '2[autoM2]', '#70e4,', '#b', '0')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.0, 1.17, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.14, -0.71, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.01, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.02, 1.17, 0.05, 1600)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.0, 21.0, 0.0, 1600, 0x01)
    CameraSetDistance(0x03, 1.03, 1600)
    CameraCmd(0x0B, 0x03, 35.0, 0x0640)
    BattleCmd(0x4B, 0x0640, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft02_00')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_00', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    EffectCmd(0x15, 0xFFFE, 0x0A, 0.0, 0.0, 0.05, 1.0, 1000, 0x03)
    Sleep(0)

    SetChrFace(0x03, PseudoChrId.Self, '', '', '#5s4', '#b', '0')
    Sleep(200)

    OP_3B(0xFF, 0.0, 0.05, 0.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_00a', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(533)

    SetChrFace(0x03, PseudoChrId.Self, '#100s1#100s0', '#20s0#100s0', '4', '#b', '0')
    Sleep(333)

    EffectCmd(0x15, 0xFFFE, 0x0A, 0.0, 0.02, 0.1, 1.0, 500, 0x03)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x0078))
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_6', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x04000000, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft02_01')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_01', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '22332', '0', '5503', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '', 'A,#10sB', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    SetChrFace(0x03, PseudoChrId.Self, '', '#100s141JA', '', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 13)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_19ADE',
    )

    Jump('loc_19B33')

    def _loc_19ADE(): pass

    label('loc_19ADE')

    OP_3B(0x32, ParamInt(0x140E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_19B33(): pass

    label('loc_19B33')

    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x04000000, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    OP_3B(0xFF, 0.3, 0.3, 0.2)
    OP_5E(0x00, 0x0002, 0.07, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(166)

    OP_5E(0x01, 0x012C)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_01a', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(266)

    EffectCmd(0x15, 0xFFFE, 0x0A, 0.0, 0.065, 0.13, 1.0, 300, 0x03)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft02_02')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_02', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '3', '#b', '0')
    OP_4E(2.0, 0.5, 0x00, 0x01)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_7', ScriptId.Current)
    WaitAnimeClipFrames(PseudoChrId.Self, 7)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x04000000, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    WaitAnimeClipFrames(PseudoChrId.Self, 22)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft02_03')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_CRAFT02_03', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '3#56w8', '#b', '0')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_4E(1.0, 0.0, 0x00, 0x01)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_8', ScriptId.Current)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x04000000, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    EffectCmd(0x15, 0xFFFE, 0x0A, 0.0, 0.01, 0.01, 0.0, 300, 0x03)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_19F14',
    )

    Jump('loc_19F69')

    def _loc_19F14(): pass

    label('loc_19F14')

    OP_3B(0x32, ParamInt(0x1397), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_19F69(): pass

    label('loc_19F69')

    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    OP_6C(PseudoChrId.Self, 1.4, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(-2), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0x03)
    OP_3B(0xFF, 0.0, 0.3, 1.5)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateTempChar(0x0000, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B68, 0x00000260)
    BattleSetChrPos(0x0B68, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B68, 0xFFFE, 0.0, -1.0)
    BattleCreateTempChar(0x0001, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B69, 0x00000260)
    BattleSetChrPos(0x0B69, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B69, 0xFFFE, 0.0, -1.0)
    BattleCreateTempChar(0x0002, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B6A, 0x00000260)
    BattleSetChrPos(0x0B6A, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B6A, 0xFFFB, 0.0, -1.0)
    Sleep(0)

    BattleSetChrPos(0x0B6A, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleCreateTempChar(0x0003, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B6B, 0x00000260)
    BattleSetChrPos(0x0B6B, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B6B, 0xFFFB, 0.0, -1.0)
    Sleep(0)

    BattleSetChrPos(0x0B6B, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleCreateTempChar(0x0004, 0xFFFF, 'O_A00OBJ06', 'dummy')
    ChrSetPhysicsFlags(0x0B6C, 0x00000260)
    BattleSetChrPos(0x0B6C, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B6C, 0xFFFB, 0.0, -1.0)
    Sleep(0)

    BattleSetChrPos(0x0B6C, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000260)
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_9', ScriptId.Current)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x35)
    Sleep(133)

    OP_4E(1.5, 0.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFF3, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTargetsIterInit(0x05)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0x0B69, 0xFFFB, 0.0, 0.0, 1.0, -1.0, 0x00, 0x01)
    BattleTurnChrDirection(0x0B6A, 0x0B6A, 0.0, -1.0)
    BattleTurnChrDirection(0x0B6B, 0x0B6B, 108.0, -1.0)

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 2.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A3F1',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A3F1(): pass

    label('loc_1A3F1')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 4.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A456',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A456(): pass

    label('loc_1A456')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 6.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A4BB',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A4BB(): pass

    label('loc_1A4BB')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 8.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A520',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A520(): pass

    label('loc_1A520')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 10.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A585',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A585(): pass

    label('loc_1A585')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 12.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A5EA',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A5EA(): pass

    label('loc_1A5EA')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 14.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A64F',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A64F(): pass

    label('loc_1A64F')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 16.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A6B4',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A6B4(): pass

    label('loc_1A6B4')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 18.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A719',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A719(): pass

    label('loc_1A719')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 20.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A77E',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A77E(): pass

    label('loc_1A77E')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 22.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A7E3',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A7E3(): pass

    label('loc_1A7E3')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 24.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A848',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A848(): pass

    label('loc_1A848')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 26.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A8AD',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A8AD(): pass

    label('loc_1A8AD')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 28.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A912',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A912(): pass

    label('loc_1A912')

    If(
        (
            (Expr.Eval, "OP_A5(0x00, 0xFFFE, 0x0B69, 30.0, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A977',
    )

    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x7D0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    BattleSetChrPos(0x0B6A, 0x0B6A, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B6B, 0x0B6B, 0.0, 0.0, 2.0, -1.0, 0x00, 0x00)

    def _loc_1A977(): pass

    label('loc_1A977')

    CameraSetHeight(0x02, 8.0, 300)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    BattleTurnChrDirection(0x0B6A, 0xFFFE, 0.0, -1.0)
    Sleep(100)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, 180.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0xFF, 0.6, 0.6, 0.6)
    CameraCmd(0x09, 0.4, 0.4, 0.7)
    OP_5E(0x00, 0x0000, 0.6, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(33)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, -108.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    Sleep(100)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, 180.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(33)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, -108.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    Sleep(100)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, 144.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(33)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, 36.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    Sleep(1)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, -108.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    Sleep(1)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, -108.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    BattleTurnChrDirection(0x0B6B, 0xFFFE, 0.0, -1.0)
    Sleep(1)

    BattleTurnChrDirection(0xFFFE, 0xFFFE, -72.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ArgReg(0x0A), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x02)
    Sleep(1)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Sleep(500)

    OP_5E(0x01, 0x0320)
    OP_4E(1.0, 0.0, 0x00, 0x00)
    BattleCmd(0x2E, 0xFFFE)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1AEB2(): pass

    label('loc_1AEB2')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1AF4F',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1AF31',
    )

    BattleSetChrFlags(0xFFFB, 0x01000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_1AF31(): pass

    label('loc_1AF31')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1AEB2')

    def _loc_1AF4F(): pass

    label('loc_1AF4F')

    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCmd(0x2F, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0xFA0),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_1B125',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)

    Jump('loc_1B84A')

    def _loc_1B125(): pass

    label('loc_1B125')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x1F40),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_1B331',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(0.5), 0x03)

    Jump('loc_1B84A')

    def _loc_1B331(): pass

    label('loc_1B331')

    If(
        (
            (Expr.PushReg, 0xA),
            (Expr.PushLong, 0x2EE0),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_1B584',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1.5), 0x03)

    Jump('loc_1B84A')

    def _loc_1B584(): pass

    label('loc_1B584')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -18.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, -36.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(2), 0x03)

    def _loc_1B84A(): pass

    label('loc_1B84A')

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0D)
    Sleep(1000)

    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_10', ScriptId.Current)
    OP_4A(0x01, 0.1, 0.1, 0.3, 1.0, 0, 0x03)
    Sleep(200)

    OP_3B(0xFF, 0.6, 0.6, 0.2)
    Sleep(600)

    EffectCmd(0x15, 0xFFFE, 0x0A, 0.075, 0.0, 0.15, 1.0, 200, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x03)
    CameraSetHeight(0x03, 3.0, 3000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(166)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1B9D7',
    )

    Jump('loc_1BA2C')

    def _loc_1B9D7(): pass

    label('loc_1B9D7')

    OP_3B(0x32, ParamInt(0x1398), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1BA2C(): pass

    label('loc_1BA2C')

    Sleep(133)

    Sleep(20)

    OP_4A(0x01, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Sleep(13)

    EffectCmd(0x15, 0xFFFE, 0x0A, 0.12, 0.0, 0.15, 1.0, 1500, 0x03)
    OP_4A(0x01, 0.5, 0.5, 0.5, 1.0, 100, 0x03)
    BattleInitHit(0xFFFE)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1BAAB(): pass

    label('loc_1BAAB')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1BB70',
    )

    BattleClearChrFlags(0xFFFB, 0x01000000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1BB52',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(33)

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)

    def _loc_1BB52(): pass

    label('loc_1BB52')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1BAAB')

    def _loc_1BB70(): pass

    label('loc_1BB70')

    BattleTargetsIterReset(0x00, 0xFFFE)
    Sleep(2000)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    ReleaseAsset('C_EQU605_C03')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    LoadAsset('C_EQU605')
    AttachEquip(0xFFFE, 'C_EQU605', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlWait')
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
    BattleDeleteTempChar(0xFFFF)
    BattleClearChrFlags(0xFFF9, 0x01000000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000260)
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0))

    Return()

# id: 0x00D0 offset: 0x1BD6C
@scena.Code('_Lambda_6')
def _Lambda_6():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.02, 1.12, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.62, -0.35, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.04, 0)
    CameraCmd(0x0B, 0x03, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.36, -0.35, -0.0, 100, 0x01)
    BattleCmd(0x4B, 0x0064, 0x03)
    Sleep(100)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.38, 1.15, 0.09, 333)
    CameraRotateByTarget(0xFFFE, '', 0x03, -6.85, 19.09, -0.0, 333, 0x01)
    CameraSetDistance(0x03, 1.1, 333)
    BattleCmd(0x4B, 0x014D, 0x03)
    Sleep(333)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.39, 1.15, 0.09, 133)
    CameraRotateByTarget(0xFFFE, '', 0x03, -6.87, 19.69, 0.0, 133, 0x01)
    BattleCmd(0x4B, 0x0085, 0x03)
    Sleep(133)

    CameraRotateByTarget(0xFFFE, '', 0x03, -6.6, 19.52, 0.0, 167, 0x01)
    BattleCmd(0x4B, 0x00A7, 0x03)
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.38, 1.14, 0.09, 267)
    CameraRotateByTarget(0xFFFE, '', 0x03, -6.35, 18.86, 0.0, 267, 0x01)
    BattleCmd(0x4B, 0x010B, 0x03)
    Sleep(200)

    Return()

# id: 0x00D1 offset: 0x1BEF0
@scena.Code('_Lambda_7')
def _Lambda_7():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.19, 1.02, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.96, 7.02, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.54, 0)
    CameraCmd(0x0B, 0x00, 30.6801, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.16, 0.95, 0.09, 833)
    CameraRotateByTarget(0xFFFE, '', 0x00, 6.75, -5.85, -0.0, 833, 0x01)
    CameraCmd(0x0B, 0x00, 25.1104, 0x0341)
    BattleCmd(0x4B, 0x0341, 0x00)
    Sleep(833)

    Return()

# id: 0x00D2 offset: 0x1BFA0
@scena.Code('_Lambda_8')
def _Lambda_8():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.17, 0.84, 0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 9.96, 4.21, -0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.42, 0)
    CameraCmd(0x0B, 0x00, 34.6274, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.1, 0.71, 0.1, 200)
    CameraRotateByTarget(0xFFFE, '', 0x00, 12.92, 2.45, 0.0, 200, 0x01)
    CameraSetDistance(0x00, 2.43, 200)
    BattleCmd(0x4B, 0x00C8, 0x00)
    Sleep(200)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.68, 0.11, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, 13.14, 0.0, 0.0, 300, 0x01)
    CameraSetDistance(0x00, 2.42, 300)
    BattleCmd(0x4B, 0x012C, 0x00)
    Sleep(300)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.06, 1.9, 0.14, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, -9.62, -0.79, -0.0, 300, 0x01)
    CameraSetDistance(0x00, 4.43, 300)
    CameraCmd(0x0B, 0x00, 65.7652, 0x012C)
    BattleCmd(0x4B, 0x012C, 0x00)
    Sleep(300)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.09, 2.74, 0.14, 400)
    CameraRotateByTarget(0xFFFE, '', 0x00, -19.9, -1.23, 0.0, 400, 0x01)
    CameraSetDistance(0x00, 4.63, 400)
    CameraCmd(0x0B, 0x00, 96.323, 0x0190)
    BattleCmd(0x4B, 0x0190, 0x00)
    Sleep(400)

    Return()

# id: 0x00D3 offset: 0x1C154
@scena.Code('_Lambda_9')
def _Lambda_9():
    CameraSetPosByTarget(0x03, 0x0B68, '', 0.05, 5.0, -0.01, 0)
    CameraRotateByTarget(0x0B68, '', 0x03, -10.75, 9.94, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.95, 0)
    CameraCmd(0x0B, 0x03, 34.63, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0x0B68, '', 0.05, 1.0, -0.01, 133)
    CameraRotateByTarget(0x0B68, '', 0x03, 2.75, 9.94, 0.0, 133, 0x01)
    Sleep(166)

    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 1.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x03E8, 0x03)
    BattleCmd(0x47)
    Sleep(133)

    CameraRotateByTarget(0x0B68, '', 0x00, 2.61, 11.62, 0.0, 200, 0x01)
    CameraSetDistance(0x00, 10.32, 200)
    BattleCmd(0x4B, 0x00C8, 0x00)
    Sleep(200)

    CameraRotateByTarget(0x0B68, '', 0x00, 2.53, 12.66, 0.0, 200, 0x01)
    CameraSetDistance(0x00, 10.54, 200)
    BattleCmd(0x4B, 0x00C8, 0x00)
    Sleep(200)

    CameraRotateByTarget(0x0B68, '', 0x00, 2.49, 13.25, 0.0, 133, 0x01)
    CameraSetDistance(0x00, 10.67, 133)
    BattleCmd(0x4B, 0x0085, 0x00)
    Sleep(133)

    Return()

# id: 0x00D4 offset: 0x1C2CC
@scena.Code('_Lambda_10')
def _Lambda_10():
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0x0B68, '', 0.05, 0.75, -0.01, 0)
    CameraRotateByTarget(0x0B68, '', 0x00, 23.41, -33.4, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 18.54, 0)
    CameraCmd(0x0B, 0x00, 35.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraRotateByTarget(0x0B68, '', 0x00, 23.41, -32.24, 0.0, 133, 0x01)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x47)
    CameraSetDistance(0x00, 18.54, 0)

    Return()

# id: 0x00D5 offset: 0x1C38C
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle_sys/tensionup.eff', 0x00000000)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.8, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 15.0, 5.0, 0, 0x01)
    CameraSetDistance(0x03, 2.25, 0)
    CameraCmd(0x0C, 0x03, 0.14, 0.45, 0.0, 4000)
    CameraSetHeight(0x03, -1.25, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 11.0, -2.0, 5.0, 4000, 0x01)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_F', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft03_00')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_POWERUP_F', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_4E(1.1, 0.0, 0x03, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '3,', '2[autoM2]', '0', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    Sleep(500)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1C5C4',
    )

    Jump('loc_1C619')

    def _loc_1C5C4(): pass

    label('loc_1C5C4')

    OP_3B(0x32, ParamInt(0x1406), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1C619(): pass

    label('loc_1C619')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10BC), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    Sleep(666)

    OP_4E(1.0, 0.0, 0x03, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlCraft03_01')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_POWERUP', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(233)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1059), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x0154), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '7', '0', '#b', '0')
    CameraCmd(0x0A, 0.05, 0.1, 0.0, 30, 600, 600, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.12, 200, 800, 700, 0.3, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraSetHeight(0x02, 1.0, 450)
    CameraCmd(0x0C, 0x02, 0.0, -0.1, 0.0, 450)
    CameraRotateByTarget(0xFFFE, '', 0x02, 2.0, -3.0, 5.0, 450, 0x01)
    Sleep(266)

    CameraSetHeight(0x00, 2.0, 5000)
    CameraCmd(0x0C, 0x00, 0.0, -0.1, 0.0, 5000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, -10.0, 5.0, 5000, 0x01)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '0', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    Call(ScriptId.Current, 'BtlDefaultFace')
    ReleaseEffect(0xFFFE, 0x30)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00D6 offset: 0x1C9D8
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR111_SC1')
    LoadEffect(0xFFFE, 0x30, 'battle/sc111_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/sc111_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc111_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc111_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc111_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc111_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc111_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc111_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc111_00_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc111_00_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc111_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc111_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc111_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc111_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc111_00_21.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1CC63',
    )

    LoadEffect(0xFFFE, 0x3F, 'battle/cic111_9.eff', 0x00000000)

    Jump('loc_1CC6C')

    def _loc_1CC63(): pass

    label('loc_1CC63')

    BattleCmd(0x52, 0xFFFE, 0x3F)

    def _loc_1CC6C(): pass

    label('loc_1CC6C')

    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(400))
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -50.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000258, 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1CD62(): pass

    label('loc_1CD62')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1CDA5',
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

    Jump('loc_1CD62')

    def _loc_1CDA5(): pass

    label('loc_1CDA5')

    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    ChrSetPhysicsFlags(0x0BCC, 0x00000040)
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0001, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0002, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0003, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0004, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0005, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0006, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0007, 0xFFFF, 'C_CHR975', 'chr975')
    BattleCreateTempChar(0x0008, 0xFFFF, 'C_CHR975', 'chr975')
    AnimeClipAddAsset(0x0B68, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B69, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6A, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6B, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6C, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6D, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6E, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B6F, 'C_CHR975_SC1')
    AnimeClipAddAsset(0x0B70, 'C_CHR975_SC1')
    ChrSetPhysicsFlags(0x0B68, 0x000003A0)
    ChrSetPhysicsFlags(0x0B69, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6A, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6B, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6C, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6D, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6E, 0x000003E0)
    ChrSetPhysicsFlags(0x0B6F, 0x000003E0)
    ChrSetPhysicsFlags(0x0B70, 0x000003E0)
    OP_CE(0x0005, 0xFFFE, 'BTL_S_CRAFT00_01_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_8A(0x00, 0x0B68, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_CE(0x0014, 0x0B69, 'gamePos2', 0x00)
    OP_CE(0x0014, 0x0B6A, 'gamePos3', 0x00)
    OP_CE(0x0014, 0x0B6B, 'gamePos4', 0x00)
    OP_CE(0x0014, 0x0B6C, 'gamePos5', 0x00)
    OP_CE(0x0014, 0x0B6D, 'gamePos6', 0x00)
    OP_CE(0x0014, 0x0B6E, 'gamePos7', 0x00)
    OP_CE(0x0014, 0x0B6F, 'gamePos8', 0x00)
    OP_CE(0x0014, 0x0B70, 'gamePos9', 0x00)
    OP_CE(0x0004, 0xFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'disable', 'disable', 'disable', '#b', '0')
    OP_43(0x64, 500, 1.0, 0)
    OP_4E(0.9, 0.0, 0x03, 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_00_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_00_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.85, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F59999A, 0x00000000, 0x03, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1D276',
    )

    Jump('loc_1D2CB')

    def _loc_1D276(): pass

    label('loc_1D276')

    OP_3B(0x32, ParamInt(0x1399), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1D2CB(): pass

    label('loc_1D2CB')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_01_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3FC00000, 0x00000000, 0x03, 0x00)
    Sleep(1000)

    OP_5E(0x00, 0x0001, 0.35, 0, 200, 100, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.25, 0.3, 0.2)
    Sleep(480)

    OP_4E(0.82, 0.0, 0x03, 0x01)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B69, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT00_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_02_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)

    OP_6C(PseudoChrId.Self, 0.95, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    ReleaseEffect(0xFFFE, 0x32)
    LoadEffect(0xFFFE, 0x32, 'battle/sc111_00_23.eff', 0x00000000)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_03_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_03_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClipFrames(0x0B69, 5)
    ChrClearPhysicsFlags(0x0B6A, 0x00000040)
    ChrClearPhysicsFlags(0x0B6B, 0x00000040)
    ChrClearPhysicsFlags(0x0B6C, 0x00000040)
    ChrClearPhysicsFlags(0x0B6D, 0x00000040)
    ChrClearPhysicsFlags(0x0B6E, 0x00000040)
    ChrClearPhysicsFlags(0x0B6F, 0x00000040)
    ChrClearPhysicsFlags(0x0B70, 0x00000040)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_03_2', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_03_3', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_03_4', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_03_5', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_03_6', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_03_7', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_03_8', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 100, 500, 300, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.35, 0.9, 0.4)
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    Sleep(533)

    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3E99999A, 0x00000000, 0x03, 0x00)
    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(0x0B69, 0x00000040)
    ChrSetPhysicsFlags(0x0B6A, 0x00000040)
    ChrSetPhysicsFlags(0x0B6B, 0x00000040)
    ChrSetPhysicsFlags(0x0B6C, 0x00000040)
    ChrSetPhysicsFlags(0x0B6D, 0x00000040)
    ChrSetPhysicsFlags(0x0B6E, 0x00000040)
    ChrSetPhysicsFlags(0x0B6F, 0x00000040)
    ChrSetPhysicsFlags(0x0B70, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT00_04_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 5)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F4CCCCD, 0x00000000, 0x03, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1DD83',
    )

    Jump('loc_1DDD8')

    def _loc_1DD83(): pass

    label('loc_1DD83')

    OP_3B(0x32, ParamInt(0x139A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1DDD8(): pass

    label('loc_1DDD8')

    Sleep(300)

    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_6C(PseudoChrId.Self, 1.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3FE66666, 0x00000000, 0x03, 0x00)
    OP_CE(0x0003, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B69, 0x00000040)
    ChrClearPhysicsFlags(0x0B6A, 0x00000040)
    ChrClearPhysicsFlags(0x0B6B, 0x00000040)
    ChrClearPhysicsFlags(0x0B6C, 0x00000040)
    ChrClearPhysicsFlags(0x0B6D, 0x00000040)
    ChrClearPhysicsFlags(0x0B6E, 0x00000040)
    ChrClearPhysicsFlags(0x0B6F, 0x00000040)
    ChrClearPhysicsFlags(0x0B70, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT00_05_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_05_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 13.0, 280.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    Sleep(266)

    CameraCmd(0x0A, 0.02, 0.03, 0.01, 0, 200, 100, 0, 0, 0x00)
    OP_3B(0xFF, 0.25, 0.4, 0.15)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x40000000, 0x00000000, 0x03, 0x00)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x03, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x04, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x05, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x06, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x07, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x08, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x09, 0x00)
    EffectCmd(0x0E, 0xFFFE, 0x0A, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_06_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_06_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.02, 0.03, 0.01, 0, 150, 80, 0, 0, 0x00)
    OP_3B(0xFF, 0.25, 0.4, 0.08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos3'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos4'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos5'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos6'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos7'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x08)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos8'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x09)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos9'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    Sleep(166)

    OP_6C(PseudoChrId.Self, 3.2, 0xFFFFFFFF)
    OP_CE(0x0009, 0x404CCCCD, 0x00000000, 0x03, 0x00)
    OP_CE(0x0003, 0x00)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x30)
    LoadEffect(0xFFFE, 0x30, 'battle/sc111_00_22.eff', 0x00000000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    OP_CE(0x000B, 0x00000000, 0x00)
    CameraCmd(0x00)
    BattleCmd(0x8A)
    CameraRotateByTarget(0xFFFB, '', 0x03, 19.0, -28.0, 0.0, 0, 0x01)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x03, 1.0, 3000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraRotateByTarget(0xFFFB, '', 0x03, 5.0, -5.0, 0.0, 3000, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_07_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_07_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0xFFF2, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFFF2, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EC9C',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1EC9C(): pass

    label('loc_1EC9C')

    Sleep(33)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ED3A',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1ED3A(): pass

    label('loc_1ED3A')

    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EDD8',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1EDD8(): pass

    label('loc_1EDD8')

    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EE76',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1EE76(): pass

    label('loc_1EE76')

    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EF14',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1EF14(): pass

    label('loc_1EF14')

    Sleep(33)

    OP_3B(0xFF, 0.5, 0.5, 0.6)
    ChrSetPhysicsFlags(0x0B6F, 0x00000040)
    ChrSetPhysicsFlags(0x0B70, 0x00000040)
    OP_CE(0x0015, 0x0B6F, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B70, 0x00000000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B6F, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0x0B70, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(100)

    ChrClearPhysicsFlags(0x0B6F, 0x00000040)
    BattleSetChrPos(0x0B6F, 0xFFFF, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0x0B6F, 0xFFFB, 0.0, 0.0, 6.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B6F, 0xFFFB, -1.0, 0.5)
    CreateThread(0x0B6F, 0x02, '_Lambda_11', ScriptId.Current)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F09A',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1F09A(): pass

    label('loc_1F09A')

    Sleep(100)

    ChrClearPhysicsFlags(0x0B70, 0x00000040)
    BattleSetChrPos(0x0B70, 0xFFFF, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B70, 0xFFFB, 0.0, 0.0, 6.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B70, 0xFFFB, -1.0, 0.5)
    CreateThread(0x0B70, 0x02, '_Lambda_12', ScriptId.Current)
    Sleep(266)

    CameraSetHeight(0x02, 1.5, 300)
    CameraCmd(0x0A, 0.0, 0.5, 0.0, 0, 1000, 0, 1, 1000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFF2, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_6C(PseudoChrId.Self, 0.7, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F333333, 0x00000000, 0x03, 0x00)
    Sleep(1000)

    CameraSetDistance(0x00, 0.1, 1000)
    OP_CE(0x0003, 0x00)
    WaitForThreadExit(0x0B6F, 0x02)

    WaitForThreadExit(0x0B70, 0x02)

    OP_8A(0x01, 0xFFFE, 0x0B68, '', '')
    BattleDeleteTempChar(0x0000)
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHR975_C01', 'chr975')
    AnimeClipAddAsset(0x0B68, 'C_CHR975_SC1')
    ChrSetPhysicsFlags(0x0B68, 0x000003A0)
    OP_8A(0x00, 0x0B68, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_CE(0x0015, 0x0B69, 0x00000000, 0x00)
    BattleDeleteTempChar(0x0001)
    BattleCreateTempChar(0x0001, 0xFFFF, 'C_CHR975_C01', 'chr975')
    AnimeClipAddAsset(0x0B69, 'C_CHR975_SC1')
    ChrSetPhysicsFlags(0x0B69, 0x000003A0)
    OP_CE(0x0014, 0x0B69, 'gamePos2', 0x00)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(0x0B69, 0x00000040)
    ChrSetPhysicsFlags(0x0B6A, 0x00000040)
    ChrSetPhysicsFlags(0x0B6B, 0x00000040)
    ChrSetPhysicsFlags(0x0B6C, 0x00000040)
    ChrSetPhysicsFlags(0x0B6D, 0x00000040)
    ChrSetPhysicsFlags(0x0B6E, 0x00000040)
    ChrSetPhysicsFlags(0x0B6F, 0x00000040)
    ChrSetPhysicsFlags(0x0B70, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    BattleCmd(0x47)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_08_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_08_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 5)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1F458',
    )

    Jump('loc_1F4AD')

    def _loc_1F458(): pass

    label('loc_1F458')

    OP_3B(0x32, ParamInt(0x139B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1F4AD(): pass

    label('loc_1F4AD')

    Sleep(500)

    OP_6C(PseudoChrId.Self, 1.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3FE66666, 0x00000000, 0x03, 0x00)
    Sleep(133)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_CE(0x0003, 0x00)
    Call(ScriptId.Current, 'SpringOn')
    OP_CE(0x0002, 'BTL_S_CRAFT00_16_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_16', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_16_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 50, 100, 30, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(600)

    OP_4E(0.8, 0.0, 0x03, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_09_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_09_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(500)

    OP_4E(0.9, 0.0, 0x03, 0x01)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1F76B',
    )

    Jump('loc_1F7C0')

    def _loc_1F76B(): pass

    label('loc_1F76B')

    OP_3B(0x32, ParamInt(0x140C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1F7C0(): pass

    label('loc_1F7C0')

    OP_CE(0x0003, 0x00)
    OP_63(0xFFFE, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_10_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_10_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_10_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F99999A, 0x00000000, 0x03, 0x00)
    Sleep(833)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(1666)

    OP_CE(0x0003, 0x00)
    OP_43(0x65, 50, 1.0, 0)
    OP_CE(0x0002, 'BTL_S_CRAFT00_12_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_12', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_12_F', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, -0.0333333, 0x02, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_12_0', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_1FA0D',
    )

    Jump('loc_1FA62')

    def _loc_1FA0D(): pass

    label('loc_1FA0D')

    OP_3B(0x32, ParamInt(0x139C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1FA62(): pass

    label('loc_1FA62')

    OP_6C(PseudoChrId.Self, 0.9, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F666666, 0x00000000, 0x03, 0x00)
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0x0B68, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(233)

    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F8CCCCD, 0x00000000, 0x03, 0x00)
    Sleep(100)

    OP_3B(0xFF, 0.5, 0.8, 0.2)
    CameraCmd(0x0A, 0.15, 0.25, 0.01, 0, 250, 150, 0, 0, 0x00)
    Sleep(300)

    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    LoadEffect(0xFFFE, 0x30, 'battle/sc111_00_14.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/sc111_00_15.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc111_00_16.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc111_00_17.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc111_00_18.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc111_00_19.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc111_00_20.eff', 0x00000000)
    OP_43(0x67, 400, 1.0, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B69, 0x00000040)
    ChrClearPhysicsFlags(0x0B6A, 0x00000040)
    ChrClearPhysicsFlags(0x0B6B, 0x00000040)
    ChrClearPhysicsFlags(0x0B6C, 0x00000040)
    ChrClearPhysicsFlags(0x0B6D, 0x00000040)
    ChrClearPhysicsFlags(0x0B6E, 0x00000040)
    ChrSetPhysicsFlags(0x0B6F, 0x00000040)
    ChrSetPhysicsFlags(0x0B70, 0x00000040)
    OP_CE(0x0002, 'BTL_S_CRAFT00_13_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_13_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_13_2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(1666)

    OP_CE(0x0015, 0x0B6A, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B6B, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B6C, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B6D, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B6E, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B6F, 0x00000000, 0x00)
    OP_CE(0x0015, 0x0B70, 0x00000000, 0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleSetChrPos(0x0B6A, 0xFFFB, 0.0, 0.0, 2.0, -1.0, 0x03, 0x01)
    BattleTurnChrDirection(0x0B6A, 0xFFFB, 0.0, -1.0)
    BattleSetChrPosAsync(0x0B6A, 0x0B6A, 0.0, 0.5, 2.4, 0.2, 0x03, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20010',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_20010(): pass

    label('loc_20010')

    BattleSetChrPos(0x0B6B, 0xFFFB, 0.0, 0.0, 2.0, -1.0, 0x03, 0x01)
    BattleTurnChrDirection(0x0B6B, 0xFFFB, 0.0, -1.0)
    BattleSetChrPosAsync(0x0B6B, 0x0B6B, 0.0, 0.5, 2.4, 0.2, 0x03, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2008A',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_2008A(): pass

    label('loc_2008A')

    BattleSetChrPos(0x0B6C, 0xFFFB, 0.0, 0.0, 2.0, -1.0, 0x03, 0x01)
    BattleTurnChrDirection(0x0B6C, 0xFFFB, 0.0, -1.0)
    BattleSetChrPosAsync(0x0B6C, 0x0B6C, 0.0, 0.5, 2.4, 0.2, 0x03, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20104',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_20104(): pass

    label('loc_20104')

    BattleSetChrPos(0x0B6D, 0xFFFB, 0.0, 0.0, 2.0, -1.0, 0x03, 0x01)
    BattleTurnChrDirection(0x0B6D, 0xFFFB, 0.0, -1.0)
    BattleSetChrPosAsync(0x0B6D, 0x0B6D, 0.0, 0.5, 2.4, 0.2, 0x03, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2017E',
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_2017E(): pass

    label('loc_2017E')

    BattleSetChrPos(0x0B6E, 0xFFFB, 0.0, 0.0, 2.0, -1.0, 0x03, 0x01)
    BattleTurnChrDirection(0x0B6E, 0xFFFB, 0.0, -1.0)
    BattleSetChrPosAsync(0x0B6E, 0x0B6E, 0.0, 0.5, 2.4, 0.2, 0x03, 0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(833)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6A, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6B, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6C, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6D, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B6E, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_CE(0x0003, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_14_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_14_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6A, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6B, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.166667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6C, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6D, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6E, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.666667, 0x00, 0x00)
    PlayChrAnimeClip(0x0B6F, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.833333, 0x00, 0x00)
    PlayChrAnimeClip(0x0B70, 'BTL_S_CRAFT00_14_2', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(833)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_CE(0x0003, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_15_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B69, 'BTL_S_CRAFT00_15_1', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F4CCCCD, 0x00000000, 0x03, 0x00)
    Sleep(166)

    CameraCmd(0x0A, 0.15, 0.25, 0.01, 0, 1500, 0, 0, 0, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F000000, 0x00000000, 0x03, 0x00)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 0.2, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3E4CCCCD, 0x00000000, 0x03, 0x00)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_CE(0x0009, 0x3F800000, 0x00000000, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraftDamage_2', ScriptId.Current)
    OP_5E(0x00, 0x0002, 0.35, 10, 1700, 800, 0.2, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Call(ScriptId.Current, 'AniBtlSCraftDamageSpecial')
    Sleep(833)

    CameraCmd(0x0C, 0x00, 0.0, 2.0, 0.0, 2800)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR111_C70')"),
            Expr.Return,
        ),
        'loc_207FA',
    )

    Jump('loc_208C4')

    def _loc_207FA(): pass

    label('loc_207FA')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2086F',
    )

    OP_3B(0x32, ParamInt(0x139D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_208C4')

    def _loc_2086F(): pass

    label('loc_2086F')

    OP_3B(0x32, ParamInt(0x139E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_208C4(): pass

    label('loc_208C4')

    Sleep(666)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFE14, 0x00000003, ParamStr('gamePos2'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_CE(0x0003, 0x00)
    OP_63(0xFFFE, 0x00)
    OP_43(0x03, 1500, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    OP_04(0x0B, 'AniBtlSCraft00_Finish')

    Return()

# id: 0x00D7 offset: 0x20974
@scena.Code('_Lambda_11')
def _Lambda_11():
    BattleSetChrPos(0x0B6F, 0xFFFB, 0.0, 0.0, 0.0, 2.0, 0x00, 0x00)
    ChrSetPhysicsFlags(0x0B6F, 0x00000040)
    CameraCmd(0x0A, 0.03, 0.03, 0.01, 30, 400, 80, 0, 0, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.7)

    Return()

# id: 0x00D8 offset: 0x209CC
@scena.Code('_Lambda_12')
def _Lambda_12():
    BattleSetChrPos(0x0B70, 0xFFFB, 0.0, 0.0, 0.0, 2.0, 0x00, 0x00)
    ChrSetPhysicsFlags(0x0B70, 0x00000040)
    CameraCmd(0x0A, 0.03, 0.03, 0.01, 30, 400, 80, 0, 0, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.9)

    Return()

# id: 0x00D9 offset: 0x20A24
@scena.Code('AniBtlSCraft00_Finish')
def AniBtlSCraft00_Finish():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x02, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR111_SC1')
    ChrClearPhysicsFlags(0x0BCC, 0x00000040)
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

# id: 0x00DA offset: 0x20B70
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00DB offset: 0x20BC0
@scena.Code('AniBtlSCraftDamageSpecial')
def AniBtlSCraftDamageSpecial():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    OP_3B(0xFF, 0.35, 0.9, 2.3)

    Return()

# id: 0x00DC offset: 0x20C20
@scena.Code('AniBtlSCraftDamage_2')
def AniBtlSCraftDamage_2():
    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(250)

    BattleDamageAnime(0xFFF9, ParamFloat(0), ParamFloat(0), 0x01)

    Return()

# id: 0x00DD offset: 0x20DA4
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x20DD4
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x20E04
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E0 offset: 0x20E34
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E1 offset: 0x20E74
@scena.Code('AniEvFieldAttack')
def AniEvFieldAttack():
    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('ShowEquipR', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    Call(ScriptId.Current, 'EraseEquipR')
    WaitAnimeClipFrames(PseudoChrId.Self, 19)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 1.0, 0xFFFFFFFF)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.633333)
    WaitAnimeClipFrames(PseudoChrId.Self, 44)
    Call(ScriptId.Current, 'ShowEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E2 offset: 0x20FE0
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
        'loc_2106F',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_21148')

    def _loc_2106F(): pass

    label('loc_2106F')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_210EA',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_21148')

    def _loc_210EA(): pass

    label('loc_210EA')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_21148(): pass

    label('loc_21148')

    Return()

# id: 0x00E3 offset: 0x2114C
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E4 offset: 0x21188
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E5 offset: 0x211E4
@scena.Code('AniEvIdle')
def AniEvIdle():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00E6 offset: 0x21244
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvBtlWait')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E7 offset: 0x212D0
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x21330
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvBtlDash')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E9 offset: 0x213B8
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvBtlWalk')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WALK', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EA offset: 0x21434
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvFieldAttackEnd')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'DISARM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(133)

    OP_3B(0x00, ParamInt(0x1785), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(600)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00EB offset: 0x21568
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ATTACK', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EC offset: 0x21648
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvDamage')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00ED offset: 0x21724
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvAria')
    Call(ScriptId.Current, 'EraseEquipR')

    Return()

# id: 0x00EE offset: 0x21774
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvArts')
    Call(ScriptId.Current, 'EraseEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x21804
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvFrontStep')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x218E4
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvBackStep')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x219C4
@scena.Code('AniEvDead')
def AniEvDead():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvDead')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEAD', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F2 offset: 0x21AA0
@scena.Code('AniEvDead1')
def AniEvDead1():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvDead1')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_DEADa', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x21B1C
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvItem')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_ITEM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x21BF4
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvWeak')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WEAK', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x21C6C
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvWin')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F6 offset: 0x21CE4
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniEvLevel')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00F7 offset: 0x21D5C
@scena.Code('AniEvHorseWait')
def AniEvHorseWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x21D90
@scena.Code('AniEvHorseWalk')
def AniEvHorseWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F9 offset: 0x21DC8
@scena.Code('AniEvHorseRun')
def AniEvHorseRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FA offset: 0x21E00
@scena.Code('AniEvHorseStop')
def AniEvHorseStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00FB offset: 0x21E5C
@scena.Code('AniEvHorseTurnRight')
def AniEvHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00FC offset: 0x21EB8
@scena.Code('AniEvHorseTurnLeft')
def AniEvHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00FD offset: 0x21F14
@scena.Code('AniEvHorseDash')
def AniEvHorseDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FE offset: 0x21F4C
@scena.Code('AniEvHorseRearWait')
def AniEvHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FF offset: 0x21F84
@scena.Code('AniEvHorseRearWalk')
def AniEvHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0100 offset: 0x21FC0
@scena.Code('AniEvHorseRearRun')
def AniEvHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0101 offset: 0x21FFC
@scena.Code('AniEvHorseRearStop')
def AniEvHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0102 offset: 0x22060
@scena.Code('AniEvHorseRearTurnRight')
def AniEvHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0103 offset: 0x220C8
@scena.Code('AniEvHorseRearTurnLeft')
def AniEvHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0104 offset: 0x22130
@scena.Code('AniEvHorseRearDash')
def AniEvHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0105 offset: 0x2216C
@scena.Code('AniEvCraft00_00')
def AniEvCraft00_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0106 offset: 0x221E0
@scena.Code('AniEvCraft00_01')
def AniEvCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0107 offset: 0x22254
@scena.Code('AniEvCraft00_02')
def AniEvCraft00_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0108 offset: 0x222C8
@scena.Code('AniEvCraft00_03')
def AniEvCraft00_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0109 offset: 0x2233C
@scena.Code('AniEvCraft01_00')
def AniEvCraft01_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010A offset: 0x223B0
@scena.Code('AniEvCraft01_01')
def AniEvCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010B offset: 0x22424
@scena.Code('AniEvCraft02_00')
def AniEvCraft02_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010C offset: 0x22498
@scena.Code('AniEvCraft02_01')
def AniEvCraft02_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010D offset: 0x2250C
@scena.Code('AniEvCraft02_02')
def AniEvCraft02_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010E offset: 0x22580
@scena.Code('AniEvCraft02_03')
def AniEvCraft02_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010F offset: 0x225F4
@scena.Code('AniEvSCraft00_01')
def AniEvSCraft00_01():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0110 offset: 0x22678
@scena.Code('AniEvSCraft00_04')
def AniEvSCraft00_04():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0111 offset: 0x226FC
@scena.Code('AniEvSCraft00_08')
def AniEvSCraft00_08():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0112 offset: 0x22780
@scena.Code('AniEvSCraft00_09')
def AniEvSCraft00_09():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0113 offset: 0x227EC
@scena.Code('AniEvSCraft00_10')
def AniEvSCraft00_10():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0114 offset: 0x22858
@scena.Code('AniEvSCraft00_12')
def AniEvSCraft00_12():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_12', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0115 offset: 0x228C4
@scena.Code('AniEvAseNugui')
def AniEvAseNugui():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_22996',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_22CBD')

    def _loc_22996(): pass

    label('loc_22996')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_22AB1',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
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
        'loc_22AA8',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_22A85',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_22A51(): pass

    label('loc_22A51')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_22A7E',
    )

    Sleep(10)

    Jump('loc_22A51')

    def _loc_22A7E(): pass

    label('loc_22A7E')

    Sleep(300)

    def _loc_22A85(): pass

    label('loc_22A85')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_22AA8(): pass

    label('loc_22AA8')

    Jump('loc_22CBD')

    def _loc_22AB1(): pass

    label('loc_22AB1')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_22C22',
    )

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Sleep(833)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUIb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22C19',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_22BF6',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_22BC2(): pass

    label('loc_22BC2')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_22BEF',
    )

    Sleep(10)

    Jump('loc_22BC2')

    def _loc_22BEF(): pass

    label('loc_22BEF')

    Sleep(300)

    def _loc_22BF6(): pass

    label('loc_22BF6')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_22C19(): pass

    label('loc_22C19')

    Jump('loc_22CBD')

    def _loc_22C22(): pass

    label('loc_22C22')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ASENUGUIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_22CBD(): pass

    label('loc_22CBD')

    Return()

# id: 0x0116 offset: 0x22CC0
@scena.Code('AniEvSitEnzetu')
def AniEvSitEnzetu():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_22DB1',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ENZETU_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_22EED')

    def _loc_22DB1(): pass

    label('loc_22DB1')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_22E4E',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ENZETU_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_22EED')

    def _loc_22E4E(): pass

    label('loc_22E4E')

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ENZETU_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_ENZETU_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_22EED(): pass

    label('loc_22EED')

    Return()

# id: 0x0117 offset: 0x22EF0
@scena.Code('AniEvGakkari')
def AniEvGakkari():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_22FC1',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GAKKARIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_23174')

    def _loc_22FC1(): pass

    label('loc_22FC1')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_230DB',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GAKKARIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
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
        'loc_230D2',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_230AF',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2307B(): pass

    label('loc_2307B')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_230A8',
    )

    Sleep(10)

    Jump('loc_2307B')

    def _loc_230A8(): pass

    label('loc_230A8')

    Sleep(300)

    def _loc_230AF(): pass

    label('loc_230AF')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_230D2(): pass

    label('loc_230D2')

    Jump('loc_23174')

    def _loc_230DB(): pass

    label('loc_230DB')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GAKKARI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_GAKKARIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_23174(): pass

    label('loc_23174')

    Return()

# id: 0x0118 offset: 0x23178
@scena.Code('AniEvMaekagami')
def AniEvMaekagami():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('SpringOn', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_23220',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MAEKAGAMIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2338F')

    def _loc_23220(): pass

    label('loc_23220')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_23317',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MAEKAGAMIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2330E',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_232EB',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_232B7(): pass

    label('loc_232B7')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_232E4',
    )

    Sleep(10)

    Jump('loc_232B7')

    def _loc_232E4(): pass

    label('loc_232E4')

    Sleep(300)

    def _loc_232EB(): pass

    label('loc_232EB')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_2330E(): pass

    label('loc_2330E')

    Jump('loc_2338F')

    def _loc_23317(): pass

    label('loc_23317')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MAEKAGAMI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MAEKAGAMIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2338F(): pass

    label('loc_2338F')

    Return()

# id: 0x0119 offset: 0x23390
@scena.Code('AniEvSitHakushu')
def AniEvSitHakushu():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_234CE',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23464',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_23490')

    def _loc_23464(): pass

    label('loc_23464')

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sc', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_23490(): pass

    label('loc_23490')

    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2368C')

    def _loc_234CE(): pass

    label('loc_234CE')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_2356C',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_2368C')

    def _loc_2356C(): pass

    label('loc_2356C')

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23621',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_23680')

    def _loc_23621(): pass

    label('loc_23621')

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.05, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(133)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_sc', 0x01, 0x01, 0x00, 0x00, 0x00, 0.05, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_23680(): pass

    label('loc_23680')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2368C(): pass

    label('loc_2368C')

    Return()

# id: 0x011A offset: 0x23690
@scena.Code('AniEvSitHakushu2')
def AniEvSitHakushu2():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_237D2',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23766',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_23794')

    def _loc_23766(): pass

    label('loc_23766')

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sc', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_23794(): pass

    label('loc_23794')

    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2399A')

    def _loc_237D2(): pass

    label('loc_237D2')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_23872',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_2399A')

    def _loc_23872(): pass

    label('loc_23872')

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2392B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_2398E')

    def _loc_2392B(): pass

    label('loc_2392B')

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.05, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(133)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HAKUSHU_2_sc', 0x01, 0x01, 0x00, 0x00, 0x00, 0.05, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_2398E(): pass

    label('loc_2398E')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2399A(): pass

    label('loc_2399A')

    Return()

# id: 0x011B offset: 0x2399C
@scena.Code('AniEvMokurei')
def AniEvMokurei():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_23A6D',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREIa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_23D66')

    def _loc_23A6D(): pass

    label('loc_23A6D')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_23B87',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
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
        'loc_23B7E',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_23B5B',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_23B27(): pass

    label('loc_23B27')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_23B54',
    )

    Sleep(10)

    Jump('loc_23B27')

    def _loc_23B54(): pass

    label('loc_23B54')

    Sleep(300)

    def _loc_23B5B(): pass

    label('loc_23B5B')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_23B7E(): pass

    label('loc_23B7E')

    Jump('loc_23D66')

    def _loc_23B87(): pass

    label('loc_23B87')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_23CCD',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREIb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23CC4',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_23CA1',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_23C6D(): pass

    label('loc_23C6D')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_23C9A',
    )

    Sleep(10)

    Jump('loc_23C6D')

    def _loc_23C9A(): pass

    label('loc_23C9A')

    Sleep(300)

    def _loc_23CA1(): pass

    label('loc_23CA1')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_23CC4(): pass

    label('loc_23CC4')

    Jump('loc_23D66')

    def _loc_23CCD(): pass

    label('loc_23CCD')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MOKUREIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_23D66(): pass

    label('loc_23D66')

    Return()

# id: 0x011C offset: 0x23D68
@scena.Code('AniEvMukkii')
def AniEvMukkii():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
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
        'loc_23E88',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_23E65',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_23E31(): pass

    label('loc_23E31')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_23E5E',
    )

    Sleep(10)

    Jump('loc_23E31')

    def _loc_23E5E(): pass

    label('loc_23E5E')

    Sleep(300)

    def _loc_23E65(): pass

    label('loc_23E65')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_23E88(): pass

    label('loc_23E88')

    Return()

# id: 0x011D offset: 0x23E8C
@scena.Code('AniEvMukkii_Loop')
def AniEvMukkii_Loop():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)

    def _loc_23EBC(): pass

    label('loc_23EBC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_23FCD',
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
        'loc_23FBB',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_23F98',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_23F64(): pass

    label('loc_23F64')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_23F91',
    )

    Sleep(10)

    Jump('loc_23F64')

    def _loc_23F91(): pass

    label('loc_23F91')

    Sleep(300)

    def _loc_23F98(): pass

    label('loc_23F98')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_23FBB(): pass

    label('loc_23FBB')

    OP_17(0x03E8, 0x0BB8)

    Jump('loc_23EBC')

    def _loc_23FCD(): pass

    label('loc_23FCD')

    Return()

# id: 0x011E offset: 0x23FD0
@scena.Code('AniEvRei')
def AniEvRei():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_243AD',
    )

    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_240B5',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIa_U', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_243A4')

    def _loc_240B5(): pass

    label('loc_240B5')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_241CD',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIb_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_241C4',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_241A1',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2416D(): pass

    label('loc_2416D')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2419A',
    )

    Sleep(10)

    Jump('loc_2416D')

    def _loc_2419A(): pass

    label('loc_2419A')

    Sleep(300)

    def _loc_241A1(): pass

    label('loc_241A1')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_241C4(): pass

    label('loc_241C4')

    Jump('loc_243A4')

    def _loc_241CD(): pass

    label('loc_241CD')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_2430F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIb_U', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24306',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_242E3',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_242AF(): pass

    label('loc_242AF')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_242DC',
    )

    Sleep(10)

    Jump('loc_242AF')

    def _loc_242DC(): pass

    label('loc_242DC')

    Sleep(300)

    def _loc_242E3(): pass

    label('loc_242E3')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24306(): pass

    label('loc_24306')

    Jump('loc_243A4')

    def _loc_2430F(): pass

    label('loc_2430F')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIa_U', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_243A4(): pass

    label('loc_243A4')

    Jump('loc_246C5')

    def _loc_243AD(): pass

    label('loc_243AD')

    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('SpringOn', 0x0010)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_2444F',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_246C5')

    def _loc_2444F(): pass

    label('loc_2444F')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_24540',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24537',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_24514',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_244E0(): pass

    label('loc_244E0')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2450D',
    )

    Sleep(10)

    Jump('loc_244E0')

    def _loc_2450D(): pass

    label('loc_2450D')

    Sleep(300)

    def _loc_24514(): pass

    label('loc_24514')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24537(): pass

    label('loc_24537')

    Jump('loc_246C5')

    def _loc_24540(): pass

    label('loc_24540')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_24659',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24650',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_2462D',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_245F9(): pass

    label('loc_245F9')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_24626',
    )

    Sleep(10)

    Jump('loc_245F9')

    def _loc_24626(): pass

    label('loc_24626')

    Sleep(300)

    def _loc_2462D(): pass

    label('loc_2462D')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24650(): pass

    label('loc_24650')

    Jump('loc_246C5')

    def _loc_24659(): pass

    label('loc_24659')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_REIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_246C5(): pass

    label('loc_246C5')

    Return()

# id: 0x011F offset: 0x246C8
@scena.Code('AniEvRyoteAwase')
def AniEvRyoteAwase():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_2479D',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_AWASEa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2495C')

    def _loc_2479D(): pass

    label('loc_2479D')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_248BB',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_AWASEb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
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
        'loc_248B2',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_2488F',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2485B(): pass

    label('loc_2485B')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_24888',
    )

    Sleep(10)

    Jump('loc_2485B')

    def _loc_24888(): pass

    label('loc_24888')

    Sleep(300)

    def _loc_2488F(): pass

    label('loc_2488F')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_248B2(): pass

    label('loc_248B2')

    Jump('loc_2495C')

    def _loc_248BB(): pass

    label('loc_248BB')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_AWASE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_AWASEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2495C(): pass

    label('loc_2495C')

    Return()

# id: 0x0120 offset: 0x24960
@scena.Code('AniEvSitSian')
def AniEvSitSian():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1_2', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_24A62',
    )

    OP_80(0.0)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_24BC3')

    def _loc_24A62(): pass

    label('loc_24A62')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_24B13',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_sb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_24BC3')

    def _loc_24B13(): pass

    label('loc_24B13')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_s', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_24BC3(): pass

    label('loc_24BC3')

    Return()

# id: 0x0121 offset: 0x24BC4
@scena.Code('AniEvSitSianTeburi')
def AniEvSitSianTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    OP_80(0.2)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_t', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0122 offset: 0x24CB8
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
        'loc_24D9A',
    )

    OP_80(0.0)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANFa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_24F72')

    def _loc_24D9A(): pass

    label('loc_24D9A')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_24EC8',
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
        'loc_24EBF',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_24E9C',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_24E68(): pass

    label('loc_24E68')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_24E95',
    )

    Sleep(10)

    Jump('loc_24E68')

    def _loc_24E95(): pass

    label('loc_24E95')

    Sleep(300)

    def _loc_24E9C(): pass

    label('loc_24E9C')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_24EBF(): pass

    label('loc_24EBF')

    Jump('loc_24F72')

    def _loc_24EC8(): pass

    label('loc_24EC8')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANFa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_24F72(): pass

    label('loc_24F72')

    Return()

# id: 0x0123 offset: 0x24F74
@scena.Code('AniEvSitSianF')
def AniEvSitSianF():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1_2', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_25077',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 0.9, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_251DB')

    def _loc_25077(): pass

    label('loc_25077')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_25129',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF_sb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_251DB')

    def _loc_25129(): pass

    label('loc_25129')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIANF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_251DB(): pass

    label('loc_251DB')

    Return()

# id: 0x0124 offset: 0x251DC
@scena.Code('AniEvSitUdegumiF')
def AniEvSitUdegumiF():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_252CF',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_25411')

    def _loc_252CF(): pass

    label('loc_252CF')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_2536E',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Common, 'SitWaitSwitch')

    Jump('loc_25411')

    def _loc_2536E(): pass

    label('loc_2536E')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_25411(): pass

    label('loc_25411')

    Return()

# id: 0x0125 offset: 0x25414
@scena.Code('AniEvSitDown')
def AniEvSitDown():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_255A2',
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIT_DOWN', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    OP_B5(0xFFFE, 0x02, 0.0, 0.0, 0.0, 0x0190, 0x0003)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.35, 0.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_25533',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_254FF(): pass

    label('loc_254FF')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2552C',
    )

    Sleep(10)

    Jump('loc_254FF')

    def _loc_2552C(): pass

    label('loc_2552C')

    Sleep(300)

    def _loc_25533(): pass

    label('loc_25533')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.CurrentCharacter, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_25696')

    def _loc_255A2(): pass

    label('loc_255A2')

    OP_B5(0xFFFE, 0x02, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x01, 0x01, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, -0.35, 0.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_SIT_DOWN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0190, 0x0003)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_25696(): pass

    label('loc_25696')

    Return()

# id: 0x0126 offset: 0x25698
@scena.Code('AniAttachEQU033')
def AniAttachEQU033():
    LoadAsset('C_EQU033')
    AttachEquip(0xFFFE, 'C_EQU033', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0127 offset: 0x25730
@scena.Code('AniDetachEQU033')
def AniDetachEQU033():
    ReleaseAsset('C_EQU033')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0128 offset: 0x25784
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320_C03')
    AttachEquip(0xFFFE, 'C_EQU320_C03', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0129 offset: 0x257F8
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320_C03')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x012A offset: 0x25850
@scena.Code('AniEv50585')
def AniEv50585():
    OP_CE(0x0005, 0xFFFE, 'EV50585_GS', 0x00)
    CreateChr(0x0B68, 'C_EQU320_C03', '', '', 0x00, 0x00000000, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    OP_CE(0x0014, 0x0B68, 'gamePos1', 0x00)
    ChrSetPhysicsFlags(0x0B68, 0x00000260)
    OP_CE(0x0004, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0002, 'EV50585_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    LoadAsset('C_EQU320_C03')
    AttachEquip(0xFFFE, 'C_EQU320_C03', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV50585', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(1166)

    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV50585a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    ReleaseAsset('C_EQU320_C03')
    OP_CE(0x0001, 0x00000000, 0x00)

    Return()

# id: 0x012B offset: 0x25A34
@scena.Code('AniAttachEQU605_C07')
def AniAttachEQU605_C07():
    LoadAsset('C_EQU605_C07')
    AttachEquip(0xFFFE, 'C_EQU605_C07', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x012C offset: 0x25AD4
@scena.Code('AniDetachEQU605_C07')
def AniDetachEQU605_C07():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU605_C07')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x012D offset: 0x25B2C
@scena.Code('AniEv31065')
def AniEv31065():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV31065', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 69)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 93)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 145)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 173)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 221)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 251)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 298)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 327)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 365)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_25CD0(): pass

    label('loc_25CD0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25D9E',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV31065a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 43)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 70)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 115)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_25CD0')

    def _loc_25D9E(): pass

    label('loc_25D9E')

    Return()

# id: 0x012E offset: 0x25DA0
@scena.Code('AniEv31066')
def AniEv31066():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV31066', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV31066a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x012F offset: 0x25E08
@scena.Code('AniAttachEQU720')
def AniAttachEQU720():
    LoadAsset('C_EQU720')
    AttachEquip(0xFFFE, 'C_EQU720', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0130 offset: 0x25EA0
@scena.Code('AniDetachEQU720')
def AniDetachEQU720():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU720')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0131 offset: 0x25EF4
@scena.Code('AniEv51545')
def AniEv51545():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV51545', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0132 offset: 0x25F28
@scena.Code('AniEv51545w')
def AniEv51545w():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV51545w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0133 offset: 0x25F5C
@scena.Code('AniAttachEQU714')
def AniAttachEQU714():
    LoadAsset('C_EQU714')
    AttachEquip(0xFFFE, 'C_EQU714', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0134 offset: 0x25FF4
@scena.Code('AniDetachEQU714')
def AniDetachEQU714():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU714')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0135 offset: 0x26048
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "FormationCmd(0x0A, ChrTable['Colins Plushie'])"),
            Expr.Return,
        ),
        'loc_260B5',
    )

    OP_38(ChrTable['Colins Plushie'], 0x00, 0x00, 'AniEv35000')

    Jump('loc_260DC')

    def _loc_260B5(): pass

    label('loc_260B5')

    If(
        (
            (Expr.Eval, "FormationCmd(0x0A, 0x0BCC)"),
            Expr.Return,
        ),
        'loc_260DC',
    )

    OP_38(0x0BCC, 0x00, 0x00, 'AniEv35000')

    def _loc_260DC(): pass

    label('loc_260DC')

    Sleep(366)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Sleep(133)

    OP_3B(0x00, ParamInt(0x17B4), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1033)

    OP_3B(0x00, ParamInt(0x17B5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0136 offset: 0x26204
@scena.Code('AniEv52655')
def AniEv52655():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52655', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0137 offset: 0x26258
@scena.Code('AniEv52660')
def AniEv52660():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52660', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0138 offset: 0x262AC
@scena.Code('AniAttachEQU715')
def AniAttachEQU715():
    LoadAsset('C_EQU715')
    AttachEquip(0xFFFE, 'C_EQU715', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0139 offset: 0x26344
@scena.Code('AniDetachEQU715')
def AniDetachEQU715():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU715')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x013A offset: 0x26398
@scena.Code('AniEv52665')
def AniEv52665():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52665', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013B offset: 0x263CC
@scena.Code('AniEv52665w')
def AniEv52665w():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52665w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013C offset: 0x26400
@scena.Code('AniEv71505')
def AniEv71505():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV71505', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV71505a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013D offset: 0x26468
@scena.Code('AniEv71550')
def AniEv71550():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV71550', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV71550a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013E offset: 0x264D0
@scena.Code('AniEv74305')
def AniEv74305():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74305', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV74305a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x013F offset: 0x26538
@scena.Code('AniEv76055')
def AniEv76055():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV76055', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV76055a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0140 offset: 0x265A0
@scena.Code('AniEv77065')
def AniEv77065():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV77065', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0141 offset: 0x265D4
@scena.Code('AniEv79435')
def AniEv79435():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79435', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0142 offset: 0x26608
@scena.Code('AniEv79436')
def AniEv79436():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79436', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0143 offset: 0x2665C
@scena.Code('AniEv_88_88_88_01')
def AniEv_88_88_88_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_88_88_88_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0144 offset: 0x26698
@scena.Code('AniEv_88_88_88_02')
def AniEv_88_88_88_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_88_88_88_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0145 offset: 0x266D4
@scena.Code('AniEv_C1_01_01_01')
def AniEv_C1_01_01_01():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0146 offset: 0x26720
@scena.Code('AniEv_C1_01_01_02')
def AniEv_C1_01_01_02():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0147 offset: 0x2676C
@scena.Code('AniEv_C1_01_01_03')
def AniEv_C1_01_01_03():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0148 offset: 0x267B8
@scena.Code('AniEv_C1_01_01_04')
def AniEv_C1_01_01_04():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0149 offset: 0x26804
@scena.Code('AniEv_C1_01_01_05')
def AniEv_C1_01_01_05():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014A offset: 0x26850
@scena.Code('AniEv_C1_01_01_06')
def AniEv_C1_01_01_06():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014B offset: 0x2689C
@scena.Code('AniEv_C1_01_01_07')
def AniEv_C1_01_01_07():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014C offset: 0x268E8
@scena.Code('AniEv_C1_01_01_08')
def AniEv_C1_01_01_08():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014D offset: 0x26934
@scena.Code('AniEv_C1_01_01_09')
def AniEv_C1_01_01_09():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014E offset: 0x26980
@scena.Code('AniEv_C1_01_01_10')
def AniEv_C1_01_01_10():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x014F offset: 0x269CC
@scena.Code('AniEv_C1_01_01_11')
def AniEv_C1_01_01_11():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0150 offset: 0x26A18
@scena.Code('AniEv_C1_01_01_12')
def AniEv_C1_01_01_12():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_12', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0151 offset: 0x26A64
@scena.Code('AniEv_C1_01_01_13')
def AniEv_C1_01_01_13():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_13', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0152 offset: 0x26AB0
@scena.Code('AniEv_C1_01_01_14')
def AniEv_C1_01_01_14():
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C1_01_01_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0153 offset: 0x26AFC
@scena.Code('AniEv_C4_02_02_01')
def AniEv_C4_02_02_01():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0154 offset: 0x26B48
@scena.Code('AniEv_C4_02_02_02')
def AniEv_C4_02_02_02():
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0155 offset: 0x26B94
@scena.Code('AniEv_C4_02_02_03')
def AniEv_C4_02_02_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0156 offset: 0x26BD0
@scena.Code('AniEv_C4_02_02_08')
def AniEv_C4_02_02_08():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0157 offset: 0x26C0C
@scena.Code('AniEv_C4_02_02_09')
def AniEv_C4_02_02_09():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0158 offset: 0x26C48
@scena.Code('AniEv_C4_02_02_10')
def AniEv_C4_02_02_10():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0159 offset: 0x26C84
@scena.Code('AniEv_C4_02_02_11')
def AniEv_C4_02_02_11():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015A offset: 0x26CC0
@scena.Code('AniEv_C4_02_02_13')
def AniEv_C4_02_02_13():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_13', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015B offset: 0x26CFC
@scena.Code('AniEv_C4_02_02_14')
def AniEv_C4_02_02_14():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015C offset: 0x26D38
@scena.Code('AniEv_C4_02_02_15')
def AniEv_C4_02_02_15():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_15', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015D offset: 0x26D74
@scena.Code('AniEv_C4_02_02_16')
def AniEv_C4_02_02_16():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_16', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015E offset: 0x26DB0
@scena.Code('AniEv_C4_02_02_18')
def AniEv_C4_02_02_18():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_18', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x015F offset: 0x26DEC
@scena.Code('AniEv_C4_02_02_19')
def AniEv_C4_02_02_19():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_19', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0160 offset: 0x26E28
@scena.Code('AniEv_C4_02_02_20')
def AniEv_C4_02_02_20():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_20', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0161 offset: 0x26E64
@scena.Code('AniEv_C4_02_02_21')
def AniEv_C4_02_02_21():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_21', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0162 offset: 0x26EA0
@scena.Code('AniEv_Z1_00_06_06')
def AniEv_Z1_00_06_06():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_06_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0163 offset: 0x26F04
@scena.Code('AniEv_Z1_00_49_49')
def AniEv_Z1_00_49_49():
    Call(ScriptId.Current, 'SpringOp49Off')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_49_49', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0164 offset: 0x26F6C
@scena.Code('AniEv_Z1_00_53_53')
def AniEv_Z1_00_53_53():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_53', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0165 offset: 0x26FB0
@scena.Code('AniEv_Z1_00_53_54')
def AniEv_Z1_00_53_54():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_54', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0166 offset: 0x26FF4
@scena.Code('AniEv_Z1_00_53_55')
def AniEv_Z1_00_53_55():
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_Z1_00_53_55', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0167 offset: 0x27038
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR111_EV', 'EV35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk111_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/cr111_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/cr111_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk111_1.eff', 0x00000000)

    Return()

# id: 0x0168 offset: 0x270E0
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'EV35000')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)

    Return()

# id: 0x0169 offset: 0x27134
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x016A offset: 0x271C8
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

    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('AniIdle_endhook', 0x000B)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2728F',
    )

    OP_3B(0x32, ParamInt(0x13DF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_272E4')

    def _loc_2728F(): pass

    label('loc_2728F')

    OP_3B(0x32, ParamInt(0x13E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_272E4(): pass

    label('loc_272E4')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniIdle')
    SetChrFace(0x03, PseudoChrId.Self, '00001110#236w1', '0[autoM0]', '0#56w4#166w5', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 28)
    Call(ScriptId.Current, 'ShowEquipL')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1', '0[autoM0]', '5', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '1110#116wA550[autoE0]', '0[autoM0]', '40000#50e44#100e4#86w0[autoB0]', '#b', '0')
    WaitAnimeClipFrames(PseudoChrId.Self, 39)
    Call(ScriptId.Current, 'EraseEquipL')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x016B offset: 0x274BC
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_38(0x0BCC, 0x00, 0x00, 'AniWait')
    Call(ScriptId.Current, 'EraseEquipL')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    Call(ScriptId.Current, 'ShowEquipL')
    Sleep(133)

    OP_3B(0x00, ParamInt(0x17B4), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1033)

    OP_3B(0x00, ParamInt(0x17B5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x016C offset: 0x276A4
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
    SetEndhookFunction('AniFieldAttack_endhook', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttack')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.2, 1.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 10)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 12)
    Call(ScriptId.Current, 'EraseEquipR')
    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x000A))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x138D), ParamInt(0x138E), ParamInt(0x138F), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_278AE',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.25), ParamFloat(1), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(1), 0x02)

    def _loc_278AE(): pass

    label('loc_278AE')

    Sleep(33)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2790E',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.3), ParamFloat(0.3), ParamFloat(1), 0x02)

    def _loc_2790E(): pass

    label('loc_2790E')

    Sleep(33)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2796E',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.3), ParamFloat(0.9), ParamFloat(1), 0.0, 0.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(1), 0x02)

    def _loc_2796E(): pass

    label('loc_2796E')

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    WaitAnimeClipFrames(PseudoChrId.Self, 19)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_6C(0x0BCC, 1.0, 0xFFFFFFFF)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'FATTACK1', 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.633333)
    WaitAnimeClipFrames(PseudoChrId.Self, 24)
    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 44)
    Call(ScriptId.Current, 'ShowEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x016D offset: 0x27A70
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
    ChrSetPhysicsFlags(0x0BCC, 0x00000040)
    AttachEquip(0xFFFE, 'C_EQU605', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    SetEndhookFunction('AniAssaultAttackEnd', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1390), ParamInt(0x1391), ParamInt(0), ParamInt(0))
    Sleep(66)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(66)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.5, 3.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(100)

    Sleep(133)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27DEC',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0002000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0002000C, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x04)

    def _loc_27DEC(): pass

    label('loc_27DEC')

    EffectCmd(0x17, 0xFFFE, 0x03, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27E99',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.8), ParamFloat(0), -1.0, -1.8, 215.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1.1), ParamFloat(0), 2.5, -2.0, -20.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)

    def _loc_27E99(): pass

    label('loc_27E99')

    EffectCmd(0x17, 0xFFFE, 0x05, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27EFF',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)

    def _loc_27EFF(): pass

    label('loc_27EFF')

    CreateThread(0xFFFF, 0x05, 'SE_BTL_CHR111', ScriptId.Sound2, ParamInt(0x0014))
    OP_5E(0x00, 0x0003, 0.8, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(266)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.666667, 0x00, 0x00)
    ChrClearPhysicsFlags(0x0BCC, 0x00000040)
    Sleep(200)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_41(0xFFFE, 0x01)
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(500)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x016E offset: 0x28018
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniFieldAttackEnd')
    Sleep(100)

    OP_3B(0x00, ParamInt(0x1785), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'DISARM', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    WaitAnimeClipFrames(PseudoChrId.Self, 23)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x016F offset: 0x281BC
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_281E1',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_281E1(): pass

    label('loc_281E1')

    Return()

# id: 0x0170 offset: 0x281E4
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28246',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_28246(): pass

    label('loc_28246')

    Return()

# id: 0x0171 offset: 0x28248
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquipL')
    OP_38(0x0BCC, 0x00, 0x00, 'AniWait')
    Call(ScriptId.Current, 'EraseEquipR')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_2831F',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_28402')

    def _loc_2831F(): pass

    label('loc_2831F')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x13A3), ParamInt(0x13A4), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_28402(): pass

    label('loc_28402')

    Return()

# id: 0x0172 offset: 0x28404
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.05, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArts')
    Call(ScriptId.Current, 'EraseEquipR')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'BTL_WAIT', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    WaitAnimeClipFrames(PseudoChrId.Self, 7)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 16)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x13A5), ParamInt(0x13A6), ParamInt(0), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArtsa')
    Sleep(500)

    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlArtsb')
    OP_76(PseudoChrId.Self, 'Rarm', 'BTL_ARTSb', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(500)

    Call(ScriptId.Current, 'ShowEquipR')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)
    Sleep(300)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0173 offset: 0x28724
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_287CC',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x13BD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_287D9')

    def _loc_287CC(): pass

    label('loc_287CC')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_287D9(): pass

    label('loc_287D9')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetEndhookFunction('SpringOn', 0x000B)
    SetChrFace(0x03, PseudoChrId.Self, '0#66w5#66w0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2886A',
    )

    Sleep(200)

    Jump('loc_28878')

    def _loc_2886A(): pass

    label('loc_2886A')

    Sleep(100)

    Sleep(100)

    def _loc_28878(): pass

    label('loc_28878')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x0174 offset: 0x288C0
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

# id: 0x0175 offset: 0x28920
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605',
        ),
    )

# id: 0x0176 offset: 0x28980
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BD,
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

# id: 0x0177 offset: 0x28A30
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001388,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001389,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138A,
            name   = '',
        ),
    )

# id: 0x0178 offset: 0x28AE0
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

# id: 0x0179 offset: 0x28D70
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

# id: 0x017A offset: 0x28E40
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

# id: 0x017B offset: 0x28EC0
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

# id: 0x017C offset: 0x28F40
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

# id: 0x017D offset: 0x28FA0
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

# id: 0x017E offset: 0x29000
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

# id: 0x017F offset: 0x29060
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

# id: 0x0180 offset: 0x29130
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

# id: 0x0181 offset: 0x29230
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

# id: 0x0182 offset: 0x29290
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

# id: 0x0183 offset: 0x292F0
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013DF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013E0,
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
            name   = 'IDLEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0184 offset: 0x29440
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
            dword4 = 0x0000138D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0185 offset: 0x29540
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
            name   = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001390,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001391,
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
            name   = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0186 offset: 0x296E0
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
            dword4 = 0x00001785,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0187 offset: 0x29790
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
            dword4 = 0x00001785,
            name   = '',
        ),
    )

# id: 0x0188 offset: 0x29810
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

# id: 0x0189 offset: 0x29870
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

# id: 0x018A offset: 0x298D0
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

# id: 0x018B offset: 0x29930
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

# id: 0x018C offset: 0x29990
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

# id: 0x018D offset: 0x299F0
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

# id: 0x018E offset: 0x29A70
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

# id: 0x018F offset: 0x29AF0
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

# id: 0x0190 offset: 0x29B50
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

# id: 0x0191 offset: 0x29BB0
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

# id: 0x0192 offset: 0x29C10
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

# id: 0x0193 offset: 0x29C90
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

# id: 0x0194 offset: 0x29D10
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

# id: 0x0195 offset: 0x29D90
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

# id: 0x0196 offset: 0x29DF0
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

# id: 0x0197 offset: 0x29E70
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

# id: 0x0198 offset: 0x29ED0
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

# id: 0x0199 offset: 0x29F30
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

# id: 0x019A offset: 0x29F90
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

# id: 0x019B offset: 0x29FF0
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

# id: 0x019C offset: 0x2A050
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

# id: 0x019D offset: 0x2A0D0
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

# id: 0x019E offset: 0x2A130
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

# id: 0x019F offset: 0x2A190
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

# id: 0x01A0 offset: 0x2A1F0
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

# id: 0x01A1 offset: 0x2A250
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

# id: 0x01A2 offset: 0x2A2B0
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

# id: 0x01A3 offset: 0x2A310
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

# id: 0x01A4 offset: 0x2A370
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

# id: 0x01A5 offset: 0x2A3D0
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

# id: 0x01A6 offset: 0x2A430
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

# id: 0x01A7 offset: 0x2A490
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

# id: 0x01A8 offset: 0x2A4F0
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

# id: 0x01A9 offset: 0x2A550
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

# id: 0x01AA offset: 0x2A5B0
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

# id: 0x01AB offset: 0x2A660
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

# id: 0x01AC offset: 0x2A6C0
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

# id: 0x01AD offset: 0x2A720
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

# id: 0x01AE offset: 0x2A7A0
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

# id: 0x01AF offset: 0x2A850
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001408,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001405,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B4,
            name   = '',
        ),
    )

# id: 0x01B0 offset: 0x2A9A0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001388,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001389,
            name   = '',
        ),
    )

# id: 0x01B1 offset: 0x2AA70
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B7,
            name   = '',
        ),
    )

# id: 0x01B2 offset: 0x2AAD0
@scena.AnimeClips('_AniBtlWait')
def _AniBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01B3 offset: 0x2AB30
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

# id: 0x01B4 offset: 0x2ABB0
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
            dword4 = 0x0000138D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01B5 offset: 0x2ACB0
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013AB,
            name   = '',
        ),
    )

# id: 0x01B6 offset: 0x2AD10
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

# id: 0x01B7 offset: 0x2AD90
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A9,
            name   = '',
        ),
    )

# id: 0x01B8 offset: 0x2AE40
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A9,
            name   = '',
        ),
    )

# id: 0x01B9 offset: 0x2AEA0
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

# id: 0x01BA offset: 0x2AF50
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

# id: 0x01BB offset: 0x2AFB0
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
            dword4 = 0x000013AA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013AA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x01BC offset: 0x2B0B0
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
            dword4 = 0x000013A5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A6,
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

# id: 0x01BD offset: 0x2B1D0
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
            dword4 = 0x000013A5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A6,
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

# id: 0x01BE offset: 0x2B2D0
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B0,
            name   = '',
        ),
    )

# id: 0x01BF offset: 0x2B330
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B1,
            name   = '',
        ),
    )

# id: 0x01C0 offset: 0x2B390
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B2,
            name   = '',
        ),
    )

# id: 0x01C1 offset: 0x2B3F0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BF,
            name   = '',
        ),
    )

# id: 0x01C2 offset: 0x2B470
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
            dword4 = 0x000013CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013C0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
    )

# id: 0x01C3 offset: 0x2B570
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

# id: 0x01C4 offset: 0x2B5D0
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

# id: 0x01C5 offset: 0x2B630
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000141E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000141F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001420,
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

# id: 0x01C6 offset: 0x2B780
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
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

# id: 0x01C7 offset: 0x2B830
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139F,
            name   = '',
        ),
    )

# id: 0x01C8 offset: 0x2B8E0
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

# id: 0x01C9 offset: 0x2B940
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

# id: 0x01CA offset: 0x2B9A0
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

# id: 0x01CB offset: 0x2BA00
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

# id: 0x01CC offset: 0x2BA60
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BA,
            name   = '',
        ),
    )

# id: 0x01CD offset: 0x2BB10
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
            type   = 0x0009,
            type2  = 0x0BCC,
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
            type2  = 0x0BCC,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01CE offset: 0x2BBE0
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

# id: 0x01CF offset: 0x2BC60
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

# id: 0x01D0 offset: 0x2BCE0
@scena.AnimeClips('_AniBtlWinHoldL')
def _AniBtlWinHoldL():
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

# id: 0x01D1 offset: 0x2BD60
@scena.AnimeClips('_AniBtlWinHoldHandR')
def _AniBtlWinHoldHandR():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HOLD_HAND_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_HOLD_HAND_Ra',
        ),
    )

# id: 0x01D2 offset: 0x2BDE0
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
            type2  = 0x0BCC,
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

# id: 0x01D3 offset: 0x2BE90
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
            type   = 0x0009,
            type2  = 0x0BCC,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0BCC,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x01D4 offset: 0x2BF90
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

# id: 0x01D5 offset: 0x2BFF0
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
            dword4 = 0x00001785,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01D6 offset: 0x2C0A0
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BD,
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

# id: 0x01D7 offset: 0x2C150
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605_C04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605_C04',
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
            dword4 = 0x00001392,
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
            name   = 'BTL_CRAFT00_01',
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
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001393,
            name   = '',
        ),
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
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01D8 offset: 0x2C520
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_01_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr089_01_04.eff',
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
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001394,
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
            name   = 'BTL_CRAFT01_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000140D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001395,
            name   = '',
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
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01D9 offset: 0x2C940
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_02_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605_C03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001396,
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
            name   = 'BTL_CRAFT02_00a',
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
            dword4 = 0x0000140E,
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
            dword4 = 0x00001397,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001398,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DA offset: 0x2CD60
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
            name   = 'BTL_POWERUP_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001406,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001059,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa',
        ),
    )

# id: 0x01DB offset: 0x2CF00
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_21.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic111_9.eff',
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
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001399,
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
            name   = 'BTL_S_CRAFT00_01_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_23.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_4',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_5',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_6',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_7',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_8',
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_22.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07_1',
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
            name   = 'BTL_S_CRAFT00_08_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_16_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_16',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_16_F',
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
            name   = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000140C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12_F',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12_0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_15.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_16.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_17.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_18.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_19.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc111_00_20.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6B,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6C,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6D,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6E,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B6F,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B70,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14_2',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_15_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B69,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_15_1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000139E,
            name   = '',
        ),
    )

# id: 0x01DC offset: 0x2E1F0
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

# id: 0x01DD offset: 0x2E250
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

# id: 0x01DE offset: 0x2E2B0
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

# id: 0x01DF offset: 0x2E310
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

# id: 0x01E0 offset: 0x2E370
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

# id: 0x01E1 offset: 0x2E3D0
@scena.AnimeClips('_AniEvFieldAttack')
def _AniEvFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1',
        ),
    )

# id: 0x01E2 offset: 0x2E430
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

# id: 0x01E3 offset: 0x2E530
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

# id: 0x01E4 offset: 0x2E590
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

# id: 0x01E5 offset: 0x2E610
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

# id: 0x01E6 offset: 0x2E690
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

# id: 0x01E7 offset: 0x2E6F0
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

# id: 0x01E8 offset: 0x2E750
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

# id: 0x01E9 offset: 0x2E7B0
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

# id: 0x01EA offset: 0x2E810
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
            dword4 = 0x00001785,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01EB offset: 0x2E8C0
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

# id: 0x01EC offset: 0x2E940
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

# id: 0x01ED offset: 0x2E9C0
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

# id: 0x01EE offset: 0x2EA20
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

# id: 0x01EF offset: 0x2EAA0
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

# id: 0x01F0 offset: 0x2EB20
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

# id: 0x01F1 offset: 0x2EBA0
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

# id: 0x01F2 offset: 0x2EC20
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

# id: 0x01F3 offset: 0x2EC80
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

# id: 0x01F4 offset: 0x2ED00
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

# id: 0x01F5 offset: 0x2ED60
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

# id: 0x01F6 offset: 0x2EDE0
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

# id: 0x01F7 offset: 0x2EE60
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

# id: 0x01F8 offset: 0x2EEC0
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

# id: 0x01F9 offset: 0x2EF20
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

# id: 0x01FA offset: 0x2EF80
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

# id: 0x01FB offset: 0x2F000
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

# id: 0x01FC offset: 0x2F080
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

# id: 0x01FD offset: 0x2F100
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

# id: 0x01FE offset: 0x2F160
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

# id: 0x01FF offset: 0x2F1C0
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

# id: 0x0200 offset: 0x2F220
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

# id: 0x0201 offset: 0x2F280
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

# id: 0x0202 offset: 0x2F300
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

# id: 0x0203 offset: 0x2F380
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

# id: 0x0204 offset: 0x2F400
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

# id: 0x0205 offset: 0x2F460
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

# id: 0x0206 offset: 0x2F4E0
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

# id: 0x0207 offset: 0x2F560
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

# id: 0x0208 offset: 0x2F5E0
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

# id: 0x0209 offset: 0x2F660
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

# id: 0x020A offset: 0x2F6E0
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

# id: 0x020B offset: 0x2F760
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

# id: 0x020C offset: 0x2F7E0
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

# id: 0x020D offset: 0x2F860
@scena.AnimeClips('_AniEvCraft02_02')
def _AniEvCraft02_02():
    return ScenaAnimeClips(
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
            name   = 'BTL_CRAFT02_02a',
        ),
    )

# id: 0x020E offset: 0x2F8E0
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

# id: 0x020F offset: 0x2F960
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

# id: 0x0210 offset: 0x2F9C0
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

# id: 0x0211 offset: 0x2FA20
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

# id: 0x0212 offset: 0x2FA80
@scena.AnimeClips('_AniEvSCraft00_09')
def _AniEvSCraft00_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09',
        ),
    )

# id: 0x0213 offset: 0x2FAE0
@scena.AnimeClips('_AniEvSCraft00_10')
def _AniEvSCraft00_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10',
        ),
    )

# id: 0x0214 offset: 0x2FB40
@scena.AnimeClips('_AniEvSCraft00_12')
def _AniEvSCraft00_12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12',
        ),
    )

# id: 0x0215 offset: 0x2FBA0
@scena.AnimeClips('_AniEvAseNugui')
def _AniEvAseNugui():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ASENUGUIa',
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
            name   = 'EV_ASENUGUIb',
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
            name   = 'EV_ASENUGUI',
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
            name   = 'EV_ASENUGUIb',
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
            name   = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ASENUGUIa',
        ),
    )

# id: 0x0216 offset: 0x2FDB0
@scena.AnimeClips('_AniEvSitEnzetu')
def _AniEvSitEnzetu():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ENZETU_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ENZETU_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ENZETU_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_ENZETU_sa',
        ),
    )

# id: 0x0217 offset: 0x2FF00
@scena.AnimeClips('_AniEvGakkari')
def _AniEvGakkari():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_GAKKARIa',
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
            name   = 'EV_GAKKARIb',
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
            name   = 'EV_GAKKARI',
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
            name   = 'EV_GAKKARIa',
        ),
    )

# id: 0x0218 offset: 0x30070
@scena.AnimeClips('_AniEvMaekagami')
def _AniEvMaekagami():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MAEKAGAMIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MAEKAGAMIb',
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
            name   = 'EV_MAEKAGAMI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MAEKAGAMIa',
        ),
    )

# id: 0x0219 offset: 0x30170
@scena.AnimeClips('_AniEvSitHakushu')
def _AniEvSitHakushu():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sc',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_sc',
        ),
    )

# id: 0x021A offset: 0x30330
@scena.AnimeClips('_AniEvSitHakushu2')
def _AniEvSitHakushu2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sc',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_HAKUSHU_2_sc',
        ),
    )

# id: 0x021B offset: 0x304F0
@scena.AnimeClips('_AniEvMokurei')
def _AniEvMokurei():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MOKUREIa',
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
            name   = 'EV_MOKUREIb',
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
            name   = 'EV_MOKUREI',
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
            name   = 'EV_MOKUREIb',
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
            name   = 'EV_MOKUREI',
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
            name   = 'EV_MOKUREIa',
        ),
    )

# id: 0x021C offset: 0x30700
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

# id: 0x021D offset: 0x307B0
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

# id: 0x021E offset: 0x30860
@scena.AnimeClips('_AniEvRei')
def _AniEvRei():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_REIa_U',
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
            name   = 'EV_REIb_U',
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
            name   = 'EV_REI_U',
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
            name   = 'EV_REIb_U',
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
            name   = 'EV_REI_U',
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
            name   = 'EV_REIa_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_REIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_REIb',
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
            name   = 'EV_REI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_REIb',
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
            name   = 'EV_REI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_REIa',
        ),
    )

# id: 0x021F offset: 0x30BB0
@scena.AnimeClips('_AniEvRyoteAwase')
def _AniEvRyoteAwase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_AWASEa',
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
            name   = 'EV_RYOTE_AWASEb',
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
            name   = 'EV_RYOTE_AWASE',
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
            name   = 'EV_RYOTE_AWASEa',
        ),
    )

# id: 0x0220 offset: 0x30D20
@scena.AnimeClips('_AniEvSitSian')
def _AniEvSitSian():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
    )

# id: 0x0221 offset: 0x30E70
@scena.AnimeClips('_AniEvSitSianTeburi')
def _AniEvSitSianTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_t',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
    )

# id: 0x0222 offset: 0x30F20
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

# id: 0x0223 offset: 0x31090
@scena.AnimeClips('_AniEvSitSianF')
def _AniEvSitSianF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANF_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANF_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANF_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIANF_sa',
        ),
    )

# id: 0x0224 offset: 0x311E0
@scena.AnimeClips('_AniEvSitUdegumiF')
def _AniEvSitUdegumiF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sa',
        ),
    )

# id: 0x0225 offset: 0x31330
@scena.AnimeClips('_AniEvSitDown')
def _AniEvSitDown():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIT_DOWN',
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
            name   = 'PRE_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x0226 offset: 0x31480
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

# id: 0x0227 offset: 0x314E0
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

# id: 0x0228 offset: 0x31540
@scena.AnimeClips('_AniEv50585')
def _AniEv50585():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'EV50585_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320_C03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV50585',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV50585a',
        ),
    )

# id: 0x0229 offset: 0x31610
@scena.AnimeClips('_AniAttachEQU605_C07')
def _AniAttachEQU605_C07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU605_C07',
        ),
    )

# id: 0x022A offset: 0x31670
@scena.AnimeClips('_AniEv31065')
def _AniEv31065():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31065',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31065a',
        ),
    )

# id: 0x022B offset: 0x316F0
@scena.AnimeClips('_AniEv31066')
def _AniEv31066():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31066',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31066a',
        ),
    )

# id: 0x022C offset: 0x31770
@scena.AnimeClips('_AniAttachEQU720')
def _AniAttachEQU720():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU720',
        ),
    )

# id: 0x022D offset: 0x317D0
@scena.AnimeClips('_AniEv51545')
def _AniEv51545():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV51545',
        ),
    )

# id: 0x022E offset: 0x31830
@scena.AnimeClips('_AniEv51545w')
def _AniEv51545w():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV51545w',
        ),
    )

# id: 0x022F offset: 0x31890
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

# id: 0x0230 offset: 0x318F0
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
            dword4 = 0x000017B4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000017B5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0231 offset: 0x319C0
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

# id: 0x0232 offset: 0x31A20
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

# id: 0x0233 offset: 0x31A80
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

# id: 0x0234 offset: 0x31AE0
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

# id: 0x0235 offset: 0x31B40
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

# id: 0x0236 offset: 0x31BA0
@scena.AnimeClips('_AniEv71505')
def _AniEv71505():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV71505',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV71505a',
        ),
    )

# id: 0x0237 offset: 0x31C20
@scena.AnimeClips('_AniEv71550')
def _AniEv71550():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV71550',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV71550a',
        ),
    )

# id: 0x0238 offset: 0x31CA0
@scena.AnimeClips('_AniEv74305')
def _AniEv74305():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74305',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74305a',
        ),
    )

# id: 0x0239 offset: 0x31D20
@scena.AnimeClips('_AniEv76055')
def _AniEv76055():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV76055',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV76055a',
        ),
    )

# id: 0x023A offset: 0x31DA0
@scena.AnimeClips('_AniEv77065')
def _AniEv77065():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV77065',
        ),
    )

# id: 0x023B offset: 0x31E00
@scena.AnimeClips('_AniEv79435')
def _AniEv79435():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79435',
        ),
    )

# id: 0x023C offset: 0x31E60
@scena.AnimeClips('_AniEv79436')
def _AniEv79436():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79436',
        ),
    )

# id: 0x023D offset: 0x31EC0
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

# id: 0x023E offset: 0x31F20
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

# id: 0x023F offset: 0x31F80
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

# id: 0x0240 offset: 0x31FE0
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

# id: 0x0241 offset: 0x32040
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

# id: 0x0242 offset: 0x320A0
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

# id: 0x0243 offset: 0x32100
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

# id: 0x0244 offset: 0x32160
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

# id: 0x0245 offset: 0x321C0
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

# id: 0x0246 offset: 0x32220
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

# id: 0x0247 offset: 0x32280
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

# id: 0x0248 offset: 0x322E0
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

# id: 0x0249 offset: 0x32340
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

# id: 0x024A offset: 0x323A0
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

# id: 0x024B offset: 0x32400
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

# id: 0x024C offset: 0x32460
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

# id: 0x024D offset: 0x324C0
@scena.AnimeClips('_AniEv_C4_02_02_01')
def _AniEv_C4_02_02_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_01',
        ),
    )

# id: 0x024E offset: 0x32520
@scena.AnimeClips('_AniEv_C4_02_02_02')
def _AniEv_C4_02_02_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_02',
        ),
    )

# id: 0x024F offset: 0x32580
@scena.AnimeClips('_AniEv_C4_02_02_03')
def _AniEv_C4_02_02_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_03',
        ),
    )

# id: 0x0250 offset: 0x325E0
@scena.AnimeClips('_AniEv_C4_02_02_08')
def _AniEv_C4_02_02_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_08',
        ),
    )

# id: 0x0251 offset: 0x32640
@scena.AnimeClips('_AniEv_C4_02_02_09')
def _AniEv_C4_02_02_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_09',
        ),
    )

# id: 0x0252 offset: 0x326A0
@scena.AnimeClips('_AniEv_C4_02_02_10')
def _AniEv_C4_02_02_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_10',
        ),
    )

# id: 0x0253 offset: 0x32700
@scena.AnimeClips('_AniEv_C4_02_02_11')
def _AniEv_C4_02_02_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_11',
        ),
    )

# id: 0x0254 offset: 0x32760
@scena.AnimeClips('_AniEv_C4_02_02_13')
def _AniEv_C4_02_02_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_13',
        ),
    )

# id: 0x0255 offset: 0x327C0
@scena.AnimeClips('_AniEv_C4_02_02_14')
def _AniEv_C4_02_02_14():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_14',
        ),
    )

# id: 0x0256 offset: 0x32820
@scena.AnimeClips('_AniEv_C4_02_02_15')
def _AniEv_C4_02_02_15():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_15',
        ),
    )

# id: 0x0257 offset: 0x32880
@scena.AnimeClips('_AniEv_C4_02_02_16')
def _AniEv_C4_02_02_16():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_16',
        ),
    )

# id: 0x0258 offset: 0x328E0
@scena.AnimeClips('_AniEv_C4_02_02_18')
def _AniEv_C4_02_02_18():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_18',
        ),
    )

# id: 0x0259 offset: 0x32940
@scena.AnimeClips('_AniEv_C4_02_02_19')
def _AniEv_C4_02_02_19():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_19',
        ),
    )

# id: 0x025A offset: 0x329A0
@scena.AnimeClips('_AniEv_C4_02_02_20')
def _AniEv_C4_02_02_20():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_20',
        ),
    )

# id: 0x025B offset: 0x32A00
@scena.AnimeClips('_AniEv_C4_02_02_21')
def _AniEv_C4_02_02_21():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_C4_02_02_21',
        ),
    )

# id: 0x025C offset: 0x32A60
@scena.AnimeClips('_AniEv_Z1_00_06_06')
def _AniEv_Z1_00_06_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_06_06',
        ),
    )

# id: 0x025D offset: 0x32AC0
@scena.AnimeClips('_AniEv_Z1_00_49_49')
def _AniEv_Z1_00_49_49():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_Z1_00_49_49',
        ),
    )

# id: 0x025E offset: 0x32B20
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

# id: 0x025F offset: 0x32B80
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

# id: 0x0260 offset: 0x32BE0
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

# id: 0x0261 offset: 0x32C40
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk111_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr111_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk111_1.eff',
        ),
    )

# id: 0x0262 offset: 0x32D10
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

# id: 0x0263 offset: 0x32D70
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013DF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013E0,
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
            name   = 'IDLEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLEa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLEb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0264 offset: 0x32EC0
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
            dword4 = 0x000017B4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000017B5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0265 offset: 0x32F90
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
            dword4 = 0x0000138D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000138F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0266 offset: 0x33090
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
            name   = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001390,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001391,
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
            name   = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0267 offset: 0x33230
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
            dword4 = 0x00001785,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0268 offset: 0x332E0
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
            dword4 = 0x000013A3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x0269 offset: 0x333E0
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
            dword4 = 0x000013A5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013A6,
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

# id: 0x026A offset: 0x33530
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000013BD,
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
