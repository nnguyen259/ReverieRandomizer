import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr035_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr035.dat')

# id: 0x0000 offset: 0x27F0
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'IDLEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'IDLE2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'IDLE2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'IDLE2_W',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'FATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'FATTACK2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR035_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_ORDER',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR035_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_15',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_16',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR035_SC1',
            symbol     = 'BTL_S_CRAFT01_17',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'HORSE_REAR_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'BIKE_SIDE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR035_HS1',
            symbol     = 'BIKE_SIDE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            symbol     = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EVC19',
            symbol     = 'EV_C4_02_02_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EVC19',
            symbol     = 'EV_C4_02_02_04_F',
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
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_NORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_NORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_NORIDASIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_WARAI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV_WARAI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
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
            asset      = 'C_CHR035_EV',
            symbol     = 'EV02005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV02005b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV02005c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev02010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev02010a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev03000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev03000a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev03001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV03540',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV03540a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev30005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev30005a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev34505',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev34505a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev34540',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV37000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV52650',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV54575',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV70001_7',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV70001_7a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV7',
            symbol     = 'EV70125',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV76050',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV76050a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79321',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79321a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79322',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79322a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79323',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR035_EV',
            symbol     = 'EV79323a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR035_MG12',
            symbol     = 'MG12_BANANA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR035_MG12',
            symbol     = 'MG12_BANANA_SLANT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000020,
            asset      = 'C_CHR035_MG12',
            symbol     = 'MG12_BANANA_SLANT_R',
        ),
    )

# id: 0x0001 offset: 0xB2E4
@scena.Code('PreInit')
def PreInit():
    AnimeClipCmd(0x0D, PseudoChrId.Self)

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_B321',
    )

    AnimeClipCmd(0x0F, PseudoChrId.Self, 0x00)
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR035_DF1', 'WAIT')

    Return()

    def _loc_B321(): pass

    label('loc_B321')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR035_C00')"),
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR035_C02')"),
            Expr.Or,
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR035_C64')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_B4B3',
    )

    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR035_C00_DF1', 'WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR035_C00_DF1', 'PRE_WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_DF1', 'PRE_WAIT_U')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_EV', 'EV_SLEEP_s')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_EV', 'EV_KINCHO_3')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_EV', 'EV_KINCHO_3_t')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_EV', 'EV_KINCHO_3a')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_C00_EV', 'EV_KINCHO_3b')

    Jump('loc_B5CD')

    def _loc_B4B3(): pass

    label('loc_B4B3')

    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR035_DF1', 'WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR035_DF1', 'PRE_WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'PRE_WAIT_U')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'EV_SLEEP_s')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'EV_KINCHO_3')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'EV_KINCHO_3_t')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'EV_KINCHO_3a')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000002, 'C_CHR035_EV', 'EV_KINCHO_3b')

    def _loc_B5CD(): pass

    label('loc_B5CD')

    Return()

# id: 0x0002 offset: 0xB5D0
@scena.Code('Init')
def Init():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR035_BT1')

    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5F8',
    )

    def _loc_B5F8(): pass

    label('loc_B5F8')

    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0003 offset: 0xB648
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0004 offset: 0xB670
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0005 offset: 0xB69C
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0006 offset: 0xB6A8
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0007 offset: 0xB6B8
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0008 offset: 0xB6C8
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    Return()

# id: 0x0009 offset: 0xB6CC
@scena.Code('Ani_SC1_Load')
def Ani_SC1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000A offset: 0xB6DC
@scena.Code('Ani_MG12_Load')
def Ani_MG12_Load():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR035_MG12')

    Return()

# id: 0x000B offset: 0xB6F4
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000C offset: 0xB704
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000D offset: 0xB714
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000E offset: 0xB72C
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000F offset: 0xB738
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0010 offset: 0xB750
@scena.Code('Ani_MG12_Release')
def Ani_MG12_Release():
    AnimeClipRemoveAsset(PseudoChrId.Self, 'CHR035_MG12')
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xB774
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0012 offset: 0xB78C
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FS01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Center_SkirtFS01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Center_SkirtFS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_SkirtSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_SkirtSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_SkirtSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_SkirtSA02', 0.2)

    Return()

# id: 0x0013 offset: 0xBA18
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FS01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Center_SkirtFS01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Center_SkirtFS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_SkirtSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_SkirtSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_SkirtSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_SkirtSA02', 0.2)

    Return()

# id: 0x0014 offset: 0xBCA4
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0015 offset: 0xBCA8
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')

    Return()

# id: 0x0016 offset: 0xBCF4
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    Call(ScriptId.Current, 'AniDetachEQU092_R')
    Call(ScriptId.Current, 'AniDetachEQU092_L')

    Return()

# id: 0x0017 offset: 0xBD28
@scena.Code('AniReset')
def AniReset():
    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_BD5D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_BD5D(): pass

    label('loc_BD5D')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOn')

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0018 offset: 0xBDE0
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0019 offset: 0xBDF0
@scena.Code('AniResetWorkRun')
def AniResetWorkRun():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001A offset: 0xBE00
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x001B offset: 0xBE2C
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_BE46',
    )

    Jump('loc_BE87')

    def _loc_BE46(): pass

    label('loc_BE46')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_BE87(): pass

    label('loc_BE87')

    Return()

# id: 0x001C offset: 0xBE88
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x23),
            Expr.Equ,
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BEAD',
    )

    ModelCmd(0x0B, 0xFFFE)

    def _loc_BEAD(): pass

    label('loc_BEAD')

    Return()

# id: 0x001D offset: 0xBEB0
@scena.Code('OnCampIn')
def OnCampIn():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
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

# id: 0x001E offset: 0xBF18
@scena.Code('OnCostumeIn')
def OnCostumeIn():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x001F offset: 0xBF7C
@scena.Code('OnCostumeIn1')
def OnCostumeIn1():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
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

# id: 0x0020 offset: 0xBFF4
@scena.Code('OnCostumeIn2')
def OnCostumeIn2():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'OnCostumeIn2_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('DefaultFace', 0x000B)
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn2_2')

    Return()

# id: 0x0021 offset: 0xC08C
@scena.Code('OnCostumeIn2_2')
def OnCostumeIn2_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_3B(0x32, ParamInt(0x2871), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', '4[autoM4]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', 'C', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0022 offset: 0xC1AC
@scena.Code('OnCostumeIn3')
def OnCostumeIn3():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x0023 offset: 0xC21C
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, ParamInt(0x2892), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '0#60s111110#100s0', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(1333)

    SetChrFace(0x03, PseudoChrId.Self, '[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0024 offset: 0xC328
@scena.Code('AniFieldChange')
def AniFieldChange():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(10300), ParamInt(0x283D), ParamInt(0x283E), ParamInt(0))

    Return()

# id: 0x0025 offset: 0xC364
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0026 offset: 0xC394
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)

    Return()

# id: 0x0027 offset: 0xC3C4
@scena.Code('AniEquipEQU092_R')
def AniEquipEQU092_R():
    LoadAsset('C_EQU092_R')
    AttachEquip(0xFFFE, 'C_EQU092_R', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0028 offset: 0xC434
@scena.Code('AniEquipEQU092_L')
def AniEquipEQU092_L():
    LoadAsset('C_EQU092_L')
    AttachEquip(0xFFFE, 'C_EQU092_L', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0029 offset: 0xC4A4
@scena.Code('AniDetachEQU092_R')
def AniDetachEQU092_R():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU092_R')

    Return()

# id: 0x002A offset: 0xC4F0
@scena.Code('AniDetachEQU092_L')
def AniDetachEQU092_L():
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU092_L')

    Return()

# id: 0x002B offset: 0xC53C
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x002C offset: 0xC540
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x002D offset: 0xC544
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x002E offset: 0xC548
@scena.Code('AniWait_Test1')
def AniWait_Test1():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 1.0, 1.03333, -1.0, 0x00, 0x00)

    Return()

# id: 0x002F offset: 0xC56C
@scena.Code('AniBtlWait_Test1')
def AniBtlWait_Test1():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 10.0, 10.0333, -1.0, 0x00, 0x00)

    Return()

# id: 0x0030 offset: 0xC594
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C644',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C617',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_C63B')

    def _loc_C617(): pass

    label('loc_C617')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C63B(): pass

    label('loc_C63B')

    Jump('loc_CA2D')

    def _loc_C644(): pass

    label('loc_C644')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_C7EC',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C69D',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_C69D(): pass

    label('loc_C69D')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C72C',
    )

    ExecExpressionWithReg(
        0x02,
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

    Jump('loc_C7E3')

    def _loc_C72C(): pass

    label('loc_C72C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7BC',
    )

    ExecExpressionWithReg(
        0x02,
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

    Jump('loc_C7E3')

    def _loc_C7BC(): pass

    label('loc_C7BC')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_C7E3(): pass

    label('loc_C7E3')

    Jump('loc_CA2D')

    def _loc_C7EC(): pass

    label('loc_C7EC')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_C848',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_CA2D')

    def _loc_C848(): pass

    label('loc_C848')

    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOn')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8F1',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(PseudoChrId.Self, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Jump('loc_CA2D')

    def _loc_C8F1(): pass

    label('loc_C8F1')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C983',
    )

    ExecExpressionWithReg(
        0x02,
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Jump('loc_CA2D')

    def _loc_C983(): pass

    label('loc_C983')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA01',
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Jump('loc_CA2D')

    def _loc_CA01(): pass

    label('loc_CA01')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_CA2D(): pass

    label('loc_CA2D')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0031 offset: 0xCA54
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
        'loc_CB15',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CAE5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_CAE5(): pass

    label('loc_CAE5')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CB8C')

    def _loc_CB15(): pass

    label('loc_CB15')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB69',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_CB69(): pass

    label('loc_CB69')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CB8C(): pass

    label('loc_CB8C')

    Sleep(166)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0032 offset: 0xCBBC
@scena.Code('AniRun')
def AniRun():
    OP_80(0.2)

    ExecExpressionWithReg(
        0x03,
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
        'loc_CC1F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CC41')

    def _loc_CC1F(): pass

    label('loc_CC1F')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CC41(): pass

    label('loc_CC41')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC60',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CC60(): pass

    label('loc_CC60')

    Sleep(666)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xCC84
@scena.Code('AniDash')
def AniDash():
    ExecExpressionWithReg(
        0x03,
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
        'loc_CCE7',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CD0A')

    def _loc_CCE7(): pass

    label('loc_CCE7')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CD0A(): pass

    label('loc_CD0A')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CD29',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CD29(): pass

    label('loc_CD29')

    Sleep(666)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0034 offset: 0xCD4C
@scena.Code('AniBack')
def AniBack():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(166)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0035 offset: 0xCDA8
@scena.Code('AniDamage')
def AniDamage():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')
    Sleep(1)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0036 offset: 0xCE10
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x03,
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
        'loc_CEDB',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CE8F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CED2')

    def _loc_CE8F(): pass

    label('loc_CE8F')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CED2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CED2(): pass

    label('loc_CED2')

    Jump('loc_CF69')

    def _loc_CEDB(): pass

    label('loc_CEDB')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_CF26',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CF69')

    def _loc_CF26(): pass

    label('loc_CF26')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_CF69',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CF69(): pass

    label('loc_CF69')

    OP_3F(PseudoChrId.Self, 0x00000000)
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0037 offset: 0xCF88
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
        'loc_CFE6',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_D0CF')

    def _loc_CFE6(): pass

    label('loc_CFE6')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_D071',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Jump('loc_D0CF')

    def _loc_D071(): pass

    label('loc_D071')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D0CF(): pass

    label('loc_D0CF')

    Return()

# id: 0x0038 offset: 0xD0D0
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0039 offset: 0xD10C
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
        'loc_D165',
    )

    Sleep(500)

    Jump('loc_D171')

    def _loc_D165(): pass

    label('loc_D165')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_D171(): pass

    label('loc_D171')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x003A offset: 0xD1A8
@scena.Code('AniIdle')
def AniIdle():
    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetEndhookFunction('DefaultFace', 0x000B)
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D25E',
    )

    OP_3B(0x32, ParamInt(0x2892), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D2B3')

    def _loc_D25E(): pass

    label('loc_D25E')

    OP_3B(0x32, ParamInt(0x2893), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_D2B3(): pass

    label('loc_D2B3')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(3000)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(4000)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2_W', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x003B offset: 0xD3E4
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk035_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk035_1.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_D4A2',
    )

    LoadEffect(0xFFFE, 0x24, 'battle/atk035_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk035_a1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk035_a2.eff', 0x00000000)

    def _loc_D4A2(): pass

    label('loc_D4A2')

    Return()

# id: 0x003C offset: 0xD4A4
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x003D offset: 0xD4D4
@scena.Code('AniFieldAttack')
def AniFieldAttack():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x00)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.5, 2.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(233)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2841), ParamInt(0x2842), ParamInt(0x2842), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.042), ParamFloat(1.17), ParamFloat(0), 4.216, -26.817, 19.116, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    Sleep(166)

    OP_AD(0x01, 0x01)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    Sleep(400)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, -0.4, 1.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003E offset: 0xD734
@scena.Code('AniFieldAttack2')
def AniFieldAttack2():
    Call(ScriptId.Current, 'SpringOff')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(366)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2842), ParamInt(0x2843), ParamInt(0), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.1), ParamFloat(0), ParamFloat(0.5), 0.0, 0.0, 15.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0xFF)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.0, 0.5, 1.0, 0, 100, 0, 0, 0, 0x00)
    Sleep(66)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.5, 4.5, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    Sleep(233)

    OP_AD(0x01, 0x01)
    Sleep(66)

    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, -0.9, 0.5, 0x00, 0x0000, 0.0, 0.0, 0x00)
    Sleep(200)

    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_41(0xFFFE, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    Call(ScriptId.Current, 'SpringOn')

    Return()

# id: 0x003F offset: 0xD980
@scena.Code('AniAssaultAttack')
def AniAssaultAttack():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    SetEndhookFunction('AniAssaultEnd_endHook', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0#56w3#36w0[autoM0]', '0[autoB0]', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    EffectSetRGBA(0xFFFE, 0x06, 1.0, 1.0, 1.0, 0.0, 800, 0x03)
    Sleep(566)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2844), ParamInt(0x2845), ParamInt(0), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    MoveChr(PseudoChrId.Self, 0xFE00, 0.0, 0.0, 0.5, 6.0, 0x00, 0x0000, 0.0, 0.0, 0x00)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1044), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(233)

    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_41(0xFFFE, 0x01)
    Call(ScriptId.Current, 'SpringOn')
    EffectCmd(0x0F, 0xFFFE, 0x0026, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0025, 0x01)

    Return()

# id: 0x0040 offset: 0xDE54
@scena.Code('AniAssaultEnd_endHook')
def AniAssaultEnd_endHook():
    Call(ScriptId.Current, 'SpringOn')

    Return()

# id: 0x0041 offset: 0xDE68
@scena.Code('AniFieldAttackEnd')
def AniFieldAttackEnd():
    ExecExpressionWithReg(
        0x02,
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

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x0042 offset: 0xDF90
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0043 offset: 0xDFC4
@scena.Code('AniFieldAttackEndShort')
def AniFieldAttackEndShort():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)

    ExecExpressionWithReg(
        0x02,
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
    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(533)

    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0044 offset: 0xE0C8
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0045 offset: 0xE10C
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0046 offset: 0xE144
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x0047 offset: 0xE17C
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x0048 offset: 0xE1A4
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0049 offset: 0xE210
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x004A offset: 0xE264
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x004B offset: 0xE268
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x004C offset: 0xE26C
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004D offset: 0xE2B4
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0xE304
@scena.Code('AniHorseRun')
def AniHorseRun():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0xE354
@scena.Code('AniHorseDash')
def AniHorseDash():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xE3A4
@scena.Code('AniHorseStop')
def AniHorseStop():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0051 offset: 0xE3F4
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0052 offset: 0xE464
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0053 offset: 0xE4D4
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
        'loc_E5E6',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5C(0xFFFE, 0x00, 'up_point')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, 8.0, 9.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, 8.0, -6.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_E5E6(): pass

    label('loc_E5E6')

    OP_80(0.0)
    OP_04(0x0B, 'AniHorseRearWait')

    Return()

# id: 0x0054 offset: 0xE604
@scena.Code('AniHorseRearEnd')
def AniHorseRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x0055 offset: 0xE648
@scena.Code('AniHorseRearWait')
def AniHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0xE680
@scena.Code('AniHorseRearWalk')
def AniHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0057 offset: 0xE6BC
@scena.Code('AniHorseRearRun')
def AniHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0058 offset: 0xE6F8
@scena.Code('AniHorseRearStop')
def AniHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0059 offset: 0xE75C
@scena.Code('AniHorseRearTurnRight')
def AniHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x005A offset: 0xE7C4
@scena.Code('AniHorseRearTurnLeft')
def AniHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x005B offset: 0xE82C
@scena.Code('AniHorseRearDash')
def AniHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005C offset: 0xE868
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0xE8A4
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005E offset: 0xE8E0
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x005F offset: 0xE90C
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_E928',
    )

    Return()

    def _loc_E928(): pass

    label('loc_E928')

    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0060 offset: 0xE938
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x20)
    LoadEffect(0xFFFE, 0x20, 'battle/moncharge.eff', 0x00000000)

    Return()

# id: 0x0061 offset: 0xE98C
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0062 offset: 0xE9A4
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_EA3C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x138),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EA24',
    )

    OP_3B(0x32, ParamInt(0x28AA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_EA24(): pass

    label('loc_EA24')

    Sleep(1000)

    OP_3B(0x39, 0xFFFE)

    Jump('loc_EC86')

    def _loc_EA3C(): pass

    label('loc_EA3C')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EAB2',
    )

    OP_3B(0x32, ParamInt(0x2866), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EC86')

    def _loc_EAB2(): pass

    label('loc_EAB2')

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
        'loc_EB46',
    )

    OP_3B(0x32, ParamInt(0x2865), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EC86')

    def _loc_EB46(): pass

    label('loc_EB46')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EBBC',
    )

    OP_3B(0x32, ParamInt(0x2868), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EC86')

    def _loc_EBBC(): pass

    label('loc_EBBC')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EC31',
    )

    OP_3B(0x32, ParamInt(0x2863), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EC86')

    def _loc_EC31(): pass

    label('loc_EC31')

    OP_3B(0x32, ParamInt(0x2864), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_EC86(): pass

    label('loc_EC86')

    Return()

# id: 0x0063 offset: 0xEC88
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_ECC5',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x283F), ParamInt(0x2840), ParamInt(0), ParamInt(0))

    Jump('loc_ECE5')

    def _loc_ECC5(): pass

    label('loc_ECC5')

    OP_3B(0x3A, 0xFFFE, ParamInt(10300), ParamInt(0x283D), ParamInt(0x283E), ParamInt(0))

    def _loc_ECE5(): pass

    label('loc_ECE5')

    Return()

# id: 0x0064 offset: 0xECE8
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_ED25',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x283F), ParamInt(0x2840), ParamInt(0), ParamInt(0))

    Jump('loc_ED45')

    def _loc_ED25(): pass

    label('loc_ED25')

    OP_3B(0x3A, 0xFFFE, ParamInt(10300), ParamInt(0x283D), ParamInt(0x283E), ParamInt(0))

    def _loc_ED45(): pass

    label('loc_ED45')

    Return()

# id: 0x0065 offset: 0xED48
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x2867), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0066 offset: 0xEDA0
@scena.Code('AniBtlWait')
def AniBtlWait():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_EDEC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

    def _loc_EDEC(): pass

    label('loc_EDEC')

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0067 offset: 0xEE3C
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x0068 offset: 0xEE78
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EED5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_EF18')

    def _loc_EED5(): pass

    label('loc_EED5')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EF18',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_EF18(): pass

    label('loc_EF18')

    Return()

# id: 0x0069 offset: 0xEF1C
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x285F))

    Return()

# id: 0x006A offset: 0xEF38
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x285E))

    Return()

# id: 0x006B offset: 0xEF54
@scena.Code('AniBtlStepInKisinPt')
def AniBtlStepInKisinPt():
    SetChrFace(0x03, PseudoChrId.Self, '6[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x006C offset: 0xEF80
@scena.Code('AniBtlStepOutKisinPt')
def AniBtlStepOutKisinPt():
    Return()

# id: 0x006D offset: 0xEF84
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(666)

    BattleCmd(0x46, 0.25, 6.0, 15.0)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F088',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2841), ParamInt(0x2842), ParamInt(0x2843), ParamInt(0))

    def _loc_F088(): pass

    label('loc_F088')

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.1), ParamFloat(0), ParamFloat(0.25), 0.0, 0.0, 15.0, ParamFloat(0.6), ParamFloat(0.6), ParamFloat(0.6), 0xFF)
    CameraCmd(0x0A, 0.01, 0.02, 0.012, 30, 450, 60, 0, 0, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_F13E',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.3)

    def _loc_F13E(): pass

    label('loc_F13E')

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.02, 0.05, 0.12)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006E offset: 0xF250
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, ParamInt(0x285B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x006F offset: 0xF2BC
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleCmd(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F32E',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_F357')

    def _loc_F32E(): pass

    label('loc_F32E')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F357(): pass

    label('loc_F357')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0070 offset: 0xF364
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_F3E9',
    )

    OP_3B(0x32, ParamInt(0x2859), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F409')

    def _loc_F3E9(): pass

    label('loc_F3E9')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2857), ParamInt(0x2858), ParamInt(0), ParamInt(0))

    def _loc_F409(): pass

    label('loc_F409')

    Return()

# id: 0x0071 offset: 0xF40C
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    OP_3B(0x32, ParamInt(0x2859), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0072 offset: 0xF464
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_F4D7',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_F53B')

    def _loc_F4D7(): pass

    label('loc_F4D7')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F53B(): pass

    label('loc_F53B')

    Return()

# id: 0x0073 offset: 0xF53C
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0074 offset: 0xF598
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x0075 offset: 0xF5B4
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_F6D1',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x138),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F68D',
    )

    OP_3B(0x32, ParamInt(0x28AD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_F68D(): pass

    label('loc_F68D')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Jump('loc_F7A2')

    def _loc_F6D1(): pass

    label('loc_F6D1')

    Sleep(200)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_F76E',
    )

    OP_3B(0x32, ParamInt(0x285A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_F76E(): pass

    label('loc_F76E')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F7A2(): pass

    label('loc_F7A2')

    Return()

# id: 0x0076 offset: 0xF7A4
@scena.Code('AniBtlAria')
def AniBtlAria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x2853), ParamInt(0x2854), ParamFloat(-1), ParamFloat(0))

    Return()

# id: 0x0077 offset: 0xF7E8
@scena.Code('AniBtlArts')
def AniBtlArts():
    CameraCmd(0x00)
    CameraCmd(0x03, 0x03, 0xFFFE, '', 0.0, 1.25, 0.0, 0x0190)
    CameraCmd(0x07, 0x00BF)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2855), ParamInt(0x2856), ParamInt(0), ParamInt(0))
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0078 offset: 0xF9A0
@scena.Code('AniBtlItem')
def AniBtlItem():
    BattleTargetsIterReset(0xFF, 0xFFFE)
    Call(ScriptId.Current, 'ShowEquip')
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2842), ParamInt(0x2843), ParamInt(0), ParamInt(0))
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x0079 offset: 0xFBA0
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x2860), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007A offset: 0xFBF8
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x2861), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007B offset: 0xFC50
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x2862), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007C offset: 0xFCA8
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    Call(ScriptId.BtlCom, 'AniBtlBluff', ParamInt(0x0001))

    Return()

# id: 0x007D offset: 0xFCC4
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, ParamInt(0x28AC), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x007E offset: 0xFD2C
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2872), ParamInt(0x2873), ParamInt(0), ParamInt(0))

    Return()

# id: 0x007F offset: 0xFD50
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    Call(ScriptId.Current, 'ShowEquip')
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

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, 0.233333, 0x00, 0x00)
    Sleep(433)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FEE7',
    )

    OP_3B(0x32, ParamInt(0x2881), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10118')

    def _loc_FEE7(): pass

    label('loc_FEE7')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x26),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF5E',
    )

    OP_3B(0x32, ParamInt(0x2883), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10118')

    def _loc_FF5E(): pass

    label('loc_FF5E')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FFD5',
    )

    OP_3B(0x32, ParamInt(0x2881), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10118')

    def _loc_FFD5(): pass

    label('loc_FFD5')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x31),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1004C',
    )

    OP_3B(0x32, ParamInt(0x2883), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10118')

    def _loc_1004C(): pass

    label('loc_1004C')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_100C3',
    )

    OP_3B(0x32, ParamInt(0x2882), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10118')

    def _loc_100C3(): pass

    label('loc_100C3')

    OP_3B(0x32, ParamInt(0x2883), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10118(): pass

    label('loc_10118')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.1), ParamFloat(0), ParamFloat(0.25), 0.0, 0.0, 15.0, ParamFloat(0.6), ParamFloat(0.6), ParamFloat(0.6), 0xFF)
    CameraCmd(0x0A, 0.01, 0.02, 0.012, 30, 450, 60, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.02, 0.05, 0.12)
    Sleep(100)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x26),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1030D',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0xFF)
    CameraCmd(0x09, 0.025, 0.025, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_106F3')

    def _loc_1030D(): pass

    label('loc_1030D')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1040F',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_106F3')

    def _loc_1040F(): pass

    label('loc_1040F')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x31),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10511',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.1), ParamFloat(1.1), ParamFloat(1.1), 0xFF)
    CameraCmd(0x09, 0.075, 0.075, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_106F3')

    def _loc_10511(): pass

    label('loc_10511')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10613',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    CameraCmd(0x09, 0.1, 0.1, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))

    Jump('loc_106F3')

    def _loc_10613(): pass

    label('loc_10613')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_106F3(): pass

    label('loc_106F3')

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
    EffectCmd(0x12, 0xFFFE, 0x03FB)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x0080 offset: 0x107F0
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0081 offset: 0x10844
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0082 offset: 0x10880
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0xFF, 0xFFFE)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Call(ScriptId.Current, 'ShowEquip')
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
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(666)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28BA), ParamInt(0x28BB), ParamInt(0x28BC), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.1), ParamFloat(0), ParamFloat(0.25), 0.0, 0.0, 15.0, ParamFloat(0.6), ParamFloat(0.6), ParamFloat(0.6), 0xFF)
    CameraCmd(0x0A, 0.01, 0.02, 0.012, 30, 450, 60, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.02, 0.05, 0.12)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FB), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0x8BF0), ParamFloat(0.5), ParamFloat(0))
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0083 offset: 0x10BCC
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0084 offset: 0x10BE4
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0085 offset: 0x10BFC
@scena.Code('AniBtlLinkMomentChase')
def AniBtlLinkMomentChase():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0086 offset: 0x10C14
@scena.Code('AniBtlLinkUtmostAttack')
def AniBtlLinkUtmostAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0087 offset: 0x10C2C
@scena.Code('AniBtlLinkMomentRageChase')
def AniBtlLinkMomentRageChase():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0088 offset: 0x10C44
@scena.Code('AniBtlLinkUltimateAttack')
def AniBtlLinkUltimateAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0089 offset: 0x10C5C
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle_sys/tensionup.eff', 0x00000000)
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 16.3333, 17.1, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '2,11111133', '2[autoM2]', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F72), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, 18.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraCmd(0x0C, 0x03, 0.0, -0.15, 0.0, 8000)
    CameraCmd(0x11, 0x03, -5.0, 22.0, 0.0, 0x1F40, 0x01)
    CameraSetHeight(0x03, -2.0, 3000)
    BattleCmd(0x4B, 0x1F40, 0x03)
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 500, 2000, 500, 0, 0, 0x00)
    OP_3B(0x32, ParamInt(0x28AB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FB0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(666)

    Sleep(833)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 17.1333, -1.0, -1.0, 0x00, 0x00)
    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8F00), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F21), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6662', '2[autoM2]', '0', '#b', '0')
    CameraCmd(0x0A, 0.2, 0.1, 0.0, 100, 1000, 500, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 100, 1500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraSetHeight(0x03, 1.0, 450)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 450)
    Sleep(333)

    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(1333)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x008A offset: 0x1117C
@scena.Code('AniBtlKisinItemPa')
def AniBtlKisinItemPa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x008B offset: 0x111C0
@scena.Code('AniBtlKisinChargePa')
def AniBtlKisinChargePa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x008C offset: 0x11204
@scena.Code('AniBtlKisinSinkiPa')
def AniBtlKisinSinkiPa():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x008D offset: 0x11248
@scena.Code('AniBtlKisinPartnerArts')
def AniBtlKisinPartnerArts():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'BBBA', '', '#b', '0')
    BattleCmd(0x83, 0xFFF7, 0xFFFE)
    BattleCmd(0x85)
    BattleCmd(0x86)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x008E offset: 0x1128C
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x008F offset: 0x112AC
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x0090 offset: 0x112C8
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    SetChrFace(0x03, PseudoChrId.Self, '777776', '', '', '#b', '0')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(600)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.25, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    Sleep(1333)

    Return()

# id: 0x0091 offset: 0x11364
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_113D5',
    )

    OP_3B(0x32, ParamInt(0x2852), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_1142A')

    def _loc_113D5(): pass

    label('loc_113D5')

    OP_3B(0x32, ParamInt(0x2851), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_1142A(): pass

    label('loc_1142A')

    Return()

# id: 0x0092 offset: 0x1142C
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x0093 offset: 0x11488
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0094 offset: 0x114A0
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x0095 offset: 0x114C4
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x0096 offset: 0x114DC
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x0097 offset: 0x11514
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x2855), ParamInt(0x2856))
    Sleep(100)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0098 offset: 0x11574
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x0099 offset: 0x115B0
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x009A offset: 0x115E8
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlValiantHeal_Arts_Endhook', ScriptId.Current)

    Return()

# id: 0x009B offset: 0x11630
@scena.Code('AniBtlValiantHeal_Arts_Endhook')
def AniBtlValiantHeal_Arts_Endhook():
    Sleep(3000)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x009C offset: 0x11650
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_11718',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)

    Jump('loc_11836')

    def _loc_11718(): pass

    label('loc_11718')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0020), PseudoChrId.Self, 0x00000103, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1.5), ParamFloat(1.5), ParamFloat(1.5), 0x00)
    OP_3B(0x00, ParamInt(0x0FD5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(1000)

    def _loc_11836(): pass

    label('loc_11836')

    Return()

# id: 0x009D offset: 0x11838
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009E offset: 0x11874
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009F offset: 0x118D8
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x00A0 offset: 0x11914
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A1 offset: 0x1194C
@scena.Code('VoiceWin_select')
def VoiceWin_select():
    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x09,
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
        'loc_1198B',
    )

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_119C0')

    def _loc_1198B(): pass

    label('loc_1198B')

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_119B3',
    )

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_119C0')

    def _loc_119B3(): pass

    label('loc_119B3')

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_119C0(): pass

    label('loc_119C0')

    Return()

# id: 0x00A2 offset: 0x119C4
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A34',
    )

    OP_3B(0x32, ParamInt(0x286B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11AF9')

    def _loc_11A34(): pass

    label('loc_11A34')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11AA4',
    )

    OP_3B(0x32, ParamInt(0x2869), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11AF9')

    def _loc_11AA4(): pass

    label('loc_11AA4')

    OP_3B(0x32, ParamInt(0x286A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11AF9(): pass

    label('loc_11AF9')

    Return()

# id: 0x00A3 offset: 0x11AFC
@scena.Code('AniBtlWin')
def AniBtlWin():
    Call(ScriptId.Current, 'SpringOff')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, -36.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 2500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, 9.0, 0.0, 2500, 0x01)
    CameraSetDistance(0x03, 1.1, 2500)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '2[autoM2]', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    Call(ScriptId.Current, 'VoiceWin_play')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11CB0',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2#46w32#106w3#76w2[autoE2]', '0[autoM0]', '0#246w3', '#b', '0')

    Jump('loc_11CEA')

    def _loc_11CB0(): pass

    label('loc_11CB0')

    SetChrFace(0x03, PseudoChrId.Self, '0#46w10#106w1#76w0[autoE0]', '0[autoM0]', '0#246w3', '#b', '0')

    def _loc_11CEA(): pass

    label('loc_11CEA')

    Call(ScriptId.Current, 'ShowEquip')
    Sleep(766)

    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1333)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '', '', '0[autoB0]', '#b', '0')
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, 1.0, 0x03)
    OP_46(0x02, PseudoChrId.Self, 0xFFFF, 0x03E8)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E83',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Jump('loc_11EB8')

    def _loc_11E83(): pass

    label('loc_11E83')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '#50sC#100sC[autoMC]', '0[autoB0]', '#b', '0')

    def _loc_11EB8(): pass

    label('loc_11EB8')

    Sleep(600)

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    OP_46(0x03, PseudoChrId.Self, 0xFFFF, 0x0000, -1.0, 0x03)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Sleep(1000)

    Return()

# id: 0x00A4 offset: 0x11F74
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    Sleep(766)

    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(833)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A5 offset: 0x12128
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#46w10#106w1#76w0[autoE0]', '1#86w0#166wC[autoMC]', '0#246w3', '#b', '0')
    OP_3B(0x32, ParamInt(0x2870), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM0]', '', '#b', '0')
    Sleep(766)

    OP_3B(0x00, ParamInt(0x0FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1333)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    Call(ScriptId.Current, 'EraseEquip')
    SetChrFace(0x03, PseudoChrId.Self, '', '', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '#50sC#100sC[autoMC]', '0[autoB0]', '#b', '0')
    OP_3B(0x34, ParamInt(0x2870))

    Return()

# id: 0x00A6 offset: 0x12384
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvIdle2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEvIdle2')
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x00A7 offset: 0x12404
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x00A8 offset: 0x12410
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A9 offset: 0x12470
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '222333333332', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(666)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(433)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x00AA offset: 0x12598
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00AB offset: 0x125BC
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12629',
    )

    OP_3B(0x32, ParamInt(0x2871), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12629')

    def _loc_12629(): pass

    label('loc_12629')

    Return()

# id: 0x00AC offset: 0x1262C
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
    OP_3B(0x32, ParamInt(0x2871), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', '4[autoM4]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', 'C', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AD offset: 0x127FC
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr035_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr035_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr035_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/damage02.eff', 0x00000000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, 48.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.5, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 2.0, 0.0, 800)
    CameraCmd(0x11, 0x03, 9.0, -15.0, 0.0, 0x0320, 0x01)
    CameraSetDistance(0x03, 4.2, 800)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, ParamInt(0x2846), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    Sleep(133)

    OP_3B(0x00, ParamInt(0x8F73), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.5, 0.0, 2000)
    CameraCmd(0x11, 0x00, 10.0, -45.0, 0.0, 0x07D0, 0x01)
    CameraSetDistance(0x00, 5.0, 900)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '3', '2', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.01), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FBC), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x1057), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.6, 0.0, 900)
    CameraCmd(0x11, 0x03, -10.0, -95.0, 0.0, 0x0384, 0x01)
    CameraSetDistance(0x03, 3.5, 900)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '2', 'A', '', '#b', '0')
    Sleep(466)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.45, -0.0, 1000)
    CameraCmd(0x11, 0x00, 1.0, -10.0, 0.0, 0x03E8, 0x01)
    CameraSetDistance(0x00, 2.9, 1000)
    Sleep(500)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.3, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, -150.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.9, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(60)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0xFF, 0, 0x0000)
    OP_3B(0x32, ParamInt(0x2847), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.5, 0.0, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, -175.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 4.8, 500)
    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x01, 0x01F4)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.7, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, -185.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x00, 6.5, 2000)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft00_Damage', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_05', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00AE offset: 0x1317C
@scena.Code('AniBtlCraft00_Damage')
def AniBtlCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)

    def _loc_1318C(): pass

    label('loc_1318C')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_13245',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_13214',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_13214(): pass

    label('loc_13214')

    Sleep(33)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1318C')

    def _loc_13245(): pass

    label('loc_13245')

    Return()

# id: 0x00AF offset: 0x13248
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr035_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr035_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr035_01_2.eff', 0x00000000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, 48.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.5, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 2.0, 0.0, 800)
    CameraCmd(0x11, 0x03, 9.0, -15.0, 0.0, 0x0320, 0x01)
    CameraSetDistance(0x03, 4.2, 800)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, ParamInt(0x2846), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    Sleep(133)

    OP_3B(0x00, ParamInt(0x8F73), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.5, 0.0, 2000)
    CameraCmd(0x11, 0x00, 10.0, -45.0, 0.0, 0x07D0, 0x01)
    CameraSetDistance(0x00, 5.0, 900)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '3', '2', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.01), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FBC), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10D6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x1057), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.6, 0.0, 900)
    CameraCmd(0x11, 0x03, -10.0, -95.0, 0.0, 0x0384, 0x01)
    CameraSetDistance(0x03, 3.5, 900)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '2', 'A', '', '#b', '0')
    Sleep(466)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.45, -0.0, 1000)
    CameraCmd(0x11, 0x00, 1.0, -10.0, 0.0, 0x03E8, 0x01)
    CameraSetDistance(0x00, 2.9, 1000)
    Sleep(500)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.3, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, -150.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.9, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(60)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0xFF, 0, 0x0000)
    OP_3B(0x32, ParamInt(0x2848), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.5, 0.0, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -175.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 4.8, 500)
    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x10D3), ParamFloat(0.6), ParamInt(0x0064), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x01, 0x01F4)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.7, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, -185.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x00, 6.5, 2000)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft00_Damage', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_05', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00B0 offset: 0x13B9C
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr035_02_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr035_02_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr035_02_2.eff', 0x00000000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, 48.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 2.5, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 2.0, 0.0, 800)
    CameraCmd(0x11, 0x03, 9.0, -15.0, 0.0, 0x0320, 0x01)
    CameraSetDistance(0x03, 4.2, 800)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    OP_3B(0x32, ParamInt(0x2846), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(133)

    OP_3B(0x00, ParamInt(0x8F73), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.5, 0.0, 2000)
    CameraCmd(0x11, 0x00, 10.0, -45.0, 0.0, 0x07D0, 0x01)
    CameraSetDistance(0x00, 5.0, 900)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '3', '2', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.01), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FBC), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x104A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x1057), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.6, 0.0, 900)
    CameraCmd(0x11, 0x03, -10.0, -95.0, 0.0, 0x0384, 0x01)
    CameraSetDistance(0x03, 3.5, 900)
    SetChrFace(0x03, PseudoChrId.Self, '3', 'A', '', '#b', '0')
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '2', 'A', '', '#b', '0')
    Sleep(466)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.45, -0.0, 1000)
    CameraCmd(0x11, 0x00, 1.0, -10.0, 0.0, 0x03E8, 0x01)
    CameraSetDistance(0x00, 2.9, 1000)
    Sleep(500)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.3, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, -150.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.9, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(60)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0xFF, 0, 0x0000)
    OP_3B(0x32, ParamInt(0x2849), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.5, 0.0, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, -175.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 4.8, 500)
    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x1044), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x01, 0x01F4)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.7, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, -185.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x00, 6.5, 2000)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft00_Damage', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_05', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00B1 offset: 0x144F0
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr035_03_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr035_03_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/damage02.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr035_04_6.eff', 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 0x00000005)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrSetPhysicsFlags(0x0B86, 0x000002A0)
    ChrSetPhysicsFlags(0x0B87, 0x000002A0)
    ChrSetPhysicsFlags(0x0B88, 0x000002A0)
    ChrSetPhysicsFlags(0x0B89, 0x000002A0)
    ChrSetPhysicsFlags(0x0B8A, 0x000002A0)
    CreateThread(PseudoChrId.Self, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    CreateThread(0x0B86, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    CreateThread(0x0B87, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    CreateThread(0x0B88, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    CreateThread(0x0B89, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    CreateThread(0x0B8A, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    WaitForThreadExit(0x0B88, 0x02)

    WaitForThreadExit(0x0B89, 0x02)

    WaitForThreadExit(0x0B8A, 0x02)

    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B89, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B89, 0xFFF5, 0.0, -1.0)
    BattleSetChrPos(0x0B8A, 0xFFF5, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B88, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B89, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B89, 0x00000040)
    ChrSetPhysicsFlags(0x0B8A, 0x00000040)
    CameraCmd(0x00)
    BattleCmd(0x47)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.1, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.2, 2200)
    CameraRotateByTarget(0xFFFE, '', 0x03, 8.0, -48.0, 0.0, 2200, 0x01)
    CameraSetDistance(0x03, 1.85, 2200)
    OP_3B(0x32, ParamInt(0x284A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft03_Mouth01', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B88, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B89, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1057), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 0.675, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.5, 1000, 0x03)
    SetChrFace(0x03, 0x0B86, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 0.6, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.4, 1000, 0x03)
    SetChrFace(0x03, 0x0B87, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B88, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B88, 0.525, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B88, 0x00000040)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.3, 1000, 0x03)
    SetChrFace(0x03, 0x0B88, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B89, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B89, 0.45, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B89, 0x00000040)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B89, '2', '0', '', '#b', '0')
    Sleep(333)

    Sleep(400)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.3, 0xFFFFFFFF)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 1.5, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, -30.0, 0.0, 300, 0x01)
    CameraSetDistance(0x03, 6.5, 300)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B86, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B88, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B89, '2', '2', '', '#b', '0')
    Sleep(33)

    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.15, 0.15, 0.35)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Sleep(1)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.15, 8.5, 9.5)
    Sleep(2)

    CreateThread(0x0B86, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(0x0B86, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B87, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B88, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B88, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B88, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B89, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B89, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B89, 1.3, 0xFFFFFFFF)
    Sleep(200)

    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0x0B8A, '', 0.0, 1.25, 0.0, 4000)
    CameraSetDistance(0x03, 5.5, 4000)
    Sleep(66)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlCraft03_Damage', ScriptId.Current)
    Sleep(133)

    EffectSetRGBA(0xFFFE, 0x0B, 1.0, 1.0, 1.0, 0.0, 300, 0x03)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    WaitForThreadExit(0x0B88, 0x02)

    WaitForThreadExit(0x0B89, 0x02)

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleDeleteChrDummy()
    Sleep(500)

    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FB7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    Sleep(166)

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 300, 0x03)
    Sleep(1000)

    WaitForThreadExit(PseudoChrId.Self, 0x03)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    Call(ScriptId.Current, 'Ani_SC_Release')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000800)

    Return()

# id: 0x00B2 offset: 0x154AC
@scena.Code('AniBtlCraft03_Dash')
def AniBtlCraft03_Dash():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 12.0, 6.5, 0x00, 0x00)

    Return()

# id: 0x00B3 offset: 0x154CC
@scena.Code('AniBtlCraft03_Mouth01')
def AniBtlCraft03_Mouth01():
    SetChrFace(0x03, PseudoChrId.Self, 'A', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, 'A', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, 'A', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '8', '', '#b', '0')

    Return()

# id: 0x00B4 offset: 0x1555C
@scena.Code('AniBtlCraft03_Damage')
def AniBtlCraft03_Damage():
    BattleTargetsIterInit(0x05)
    BattleTargetsIterReset(0x01, 0xFFFE)

    def _loc_1556C(): pass

    label('loc_1556C')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_15625',
    )

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_15600',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_15600(): pass

    label('loc_15600')

    Sleep(30)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1556C')

    def _loc_15625(): pass

    label('loc_15625')

    Return()

# id: 0x00B5 offset: 0x15628
@scena.Code('AniBtlCraft04')
def AniBtlCraft04():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr035_04_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr035_04_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr035_04_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr035_04_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr035_04_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/cr035_04_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/cr035_04_6.eff', 0x00000000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Call(ScriptId.Current, 'ShowEquip')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleCreateChrDummy(0xFFFE, 0x00000003)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B86, 0x00000080)
    ChrSetPhysicsFlags(0x0B87, 0x00000080)
    ChrSetPhysicsFlags(0x0B88, 0x00000080)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000080)
    CreateThread(PseudoChrId.Self, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    CreateThread(0x0B86, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B86, 0x02)

    CreateThread(0x0B87, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B87, 0x02)

    CreateThread(0x0B88, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B88, 0x02)

    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 120.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 240.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 180.0, -1.0)
    BattleSetChrPos(0x0B86, 0x0B86, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0x0B87, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFB, 0.0, -1.0)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    PlayChrAnimeClip(0x0B86, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Target, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 15.0, -50.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.1, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.2, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 26.0, 0.0, 700, 0x01)
    CameraSetDistance(0x03, 2.65, 700)
    OP_3B(0x32, ParamInt(0x284B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), PseudoChrId.Target, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(200)

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-0.3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(0x00FA), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.35, 0.2, 700)
    CameraSetDistance(0x00, 3.8, 700)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)

    CameraSetDistance(0x03, 4.5, 700)
    Sleep(233)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, -160.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 7.1, 0)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000020)
    OP_43(0xFF, 0, 0x0000)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000020)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 1.2, 0.0, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -240.0, 0.0, 4000, 0x01)
    CameraSetDistance(0x03, 8.1, 4000)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B86, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B87, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(400), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(166)

    SetChrFace(0x03, 0x0B86, '3', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 1.4, 0xFFFFFFFF)
    Sleep(33)

    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 1.4, 0xFFFFFFFF)
    Sleep(300)

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    WaitAnimeClip(0x0B87, 0.0, 0x00)

    WaitAnimeClip(0x0B86, 0.0, 0x00)

    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 1.4, 0xFFFFFFFF)
    OP_6C(0x0B87, 1.4, 0xFFFFFFFF)
    SetChrFace(0x03, 0x0B86, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '2', '2', '', '#b', '0')
    Sleep(100)

    CreateThread(0x0B86, 0x02, 'AniBtlCraft04_Dash', ScriptId.Current)
    CreateThread(0x0B87, 0x02, 'AniBtlCraft04_Dash', ScriptId.Current)
    Sleep(100)

    ChrClearPhysicsFlags(0x0B88, 0x00000040)
    ChrClearPhysicsFlags(0x0B88, 0x00000020)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0x0B88, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.9), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.15, 0.15, 0.5)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    OP_5E(0x00, 0x0002, 0.45, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(66)

    OP_5E(0x01, 0x0190)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_16392',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)

    def _loc_16392(): pass

    label('loc_16392')

    Sleep(33)

    CameraSetDistance(0x00, 9.1, 1500)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.4, 0xFFFFFFFF)
    Sleep(66)

    OP_3B(0x32, ParamInt(0x284C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft04_Dash2', ScriptId.Current)
    OP_3B(0x00, ParamInt(0x1043), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(200)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_16545',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0C)

    def _loc_16545(): pass

    label('loc_16545')

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleSetChrPos(0x0B86, 0x0B86, 2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0x0B87, -2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 180.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFB, 180.0, -1.0)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 0.5, 0xFFFFFFFF)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 0.5, 0xFFFFFFFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 1.2, 1.0, 0.35, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 20.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    CameraCmd(0x09, 0.2, 0.2, 2.0)
    Sleep(66)

    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FAE), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(100)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_16890',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)

    def _loc_16890(): pass

    label('loc_16890')

    OP_5E(0x01, 0x0320)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    BattleCmd(0x47)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 10.0, 11.0, 4000, 0x01)
    CameraSetHeight(0x03, 0.1, 4000)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    Sleep(1000)

    Sleep(333)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    BattleDeleteChrDummy()
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Target, 0x00000080)

    Return()

# id: 0x00B6 offset: 0x169D8
@scena.Code('AniBtlCraft04_Dash')
def AniBtlCraft04_Dash():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 6.2, 0x00, 0x00)

    Return()

# id: 0x00B7 offset: 0x169F8
@scena.Code('AniBtlCraft04_Dash2')
def AniBtlCraft04_Dash2():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 8.5, 7.2, 0x00, 0x00)

    Return()

# id: 0x00B8 offset: 0x16A18
@scena.Code('AniBtlCraft05')
def AniBtlCraft05():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x31, 'battle/cr035_06_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr035_06_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr035_06_2.eff', 0x00000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BB, 4, 0x5DC)),
            Expr.Return,
        ),
        'loc_16C0C',
    )

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0xF04B),
            (Expr.PushLong, 0xF043),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16AD3(): pass

    label('loc_16AD3')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16C0C',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0xF043),
            (Expr.PushReg, 0x4),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr035')"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16BF6',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr039')"),
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr039_0')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_16B69',
    )

    BattleCmd(0xBB, ArgReg(0x04), ParamInt(0))

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_16B69(): pass

    label('loc_16B69')

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr037')"),
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr037_0')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_16BBD',
    )

    BattleCmd(0xBB, ArgReg(0x04), ParamInt(0x0001))

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_16BBD(): pass

    label('loc_16BBD')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16BF6',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleCmd(0x0E, 0xFFFE, 0x0000, 0x00000001)
    DebugLog(0x00, ParamInt(0x000A))

    def _loc_16BF6(): pass

    label('loc_16BF6')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_16AD3')

    def _loc_16C0C(): pass

    label('loc_16C0C')

    Call(ScriptId.Current, 'ShowEquip')
    OP_43(0x64, 300, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrSetPhysicsFlags(0xF080, 0x00000080)
    ChrSetPhysicsFlags(0xF081, 0x00000080)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xF081, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0.025), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    SetChrFace(0x03, 0xF081, '3', '323232332211', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8FC2), ParamFloat(0.6), ParamInt(1000), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(6000), ParamInt(3000), 0x0000, 0x0000, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FB8), ParamFloat(1), ParamInt(500), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(0xF081, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xF081, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xF081, '', 'L_hand_point', 0x01)
    OP_6C(0xF081, 0.4, 0xFFFFFFFF)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.17, 1.25, 0.2, 0)
    CameraRotateByTarget(0xF081, '', 0x03, -29.0, 86.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.17, 1.35, 0.4, 3500)
    CameraRotateByTarget(0xF081, '', 0x03, -25.0, -36.0, 0.0, 3500, 0x01)
    CameraSetDistance(0x03, 1.5, 3500)
    CameraCmd(0x0B, 0x03, 40.0, 0x0DAC)
    Sleep(1900)

    OP_6C(0xF081, 1.1, 0xFFFFFFFF)
    SetChrFace(0x03, 0xF081, '2', '72727277332', '0', '#b', '0')
    OP_3B(0x00, ParamInt(0x8F62), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1500)

    PlayChrAnimeClip(0xF081, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0033, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xF080, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0xF080, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0.025), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(0.8), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(0xF080, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xF080, 0.3, 0xFFFFFFFF)
    CameraSetPosByTarget(0x03, 0xF080, '', 0.17, 1.1, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x03, 43.0, -81.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xF080, '', 0.17, 1.3, 0.0, 4600)
    CameraRotateByTarget(0xF080, '', 0x03, 35.0, 58.0, 0.0, 4600, 0x01)
    CameraSetDistance(0x03, 1.5, 4600)
    CameraCmd(0x0B, 0x03, 40.0, 0x11F8)
    SetChrFace(0x03, 0xF080, 'E', 'BABBABB', '0', '#b', '0')
    Sleep(1250)

    OP_6C(0xF080, 0.5, 0xFFFFFFFF)
    SetChrFace(0x03, 0xF080, '0', '5454545454545454545455444', '0', '#b', '0')
    Sleep(800)

    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2200)

    PlayChrAnimeClip(0xF080, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0033, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0.05), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '3', '2[autoM2]', '0', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.25, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x8F41), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-6), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(2000), ParamInt(400), 0x0000, 0x07D0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 6.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.17, 1.35, 0.2, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -16.0, 5.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x03, 1.0, 2000)
    CameraCmd(0x0B, 0x03, 40.0, 0x0BB8)
    Sleep(1600)

    OP_45(PseudoChrId.Self, 0.0, 12.0, 0.0, 0x00FA, 0x0000)
    Sleep(200)

    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '2', 'JJ67J6337J6', '0', '#b', '0')
    Sleep(250)

    OP_3B(0x00, ParamInt(0x8F62), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    EffectCmd(0x0F, 0xFFFE, 0x0033, 0x01)
    OP_3B(0xFF, 0.25, 0.25, 2.5)
    CameraCmd(0x09, 0.025, 0.05, 3.0)
    OP_5E(0x00, 0x0002, 0.5, 500, 1800, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(250)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0xF080, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8FAD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -2.21, 1.2, 0.13, 400)
    CameraRotateByTarget(0xFFFE, '', 0x03, 27.0, 11.0, 0.0, 400, 0x01)
    CameraSetDistance(0x03, 13.0, 400)
    CameraCmd(0x0B, 0x03, 40.0, 0x0190)
    Sleep(300)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(300)

    BattleDamage(0xFFFE, 0xFFFE, 0x64, 0x00)
    BattleDamage(0xF080, 0xFFFE, 0x64, 0x00)
    BattleDamage(0xF081, 0xFFFE, 0x64, 0x00)
    Sleep(1666)

    OP_5E(0x01, 0x0190)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xF080, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xF081, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(0xF080, 0x00000080)
    ChrClearPhysicsFlags(0xF081, 0x00000080)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x00B9 offset: 0x1783C
@scena.Code('AniBtlCOMBI')
def AniBtlCOMBI():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BB, 4, 0x5DC)),
            Expr.Return,
        ),
        'loc_17929',
    )

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0xF04B),
            (Expr.PushLong, 0xF043),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_17882(): pass

    label('loc_17882')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17929',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0xF043),
            (Expr.PushReg, 0x4),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr035')"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17913',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr039')"),
            Expr.Return,
        ),
        'loc_17901',
    )

    BattleCmd(0xBB, ArgReg(0x04), ParamInt(0))

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_17901(): pass

    label('loc_17901')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17913',
    )

    def _loc_17913(): pass

    label('loc_17913')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_17882')

    def _loc_17929(): pass

    label('loc_17929')

    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR035_SC1')
    LoadEffect(0xFFFE, 0x39, 'battle_sys/rushback2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr035_05_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr039_05_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/damage02.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr035_04_6.eff', 0x00000000)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x000005DC, 0x00000000)
    OP_C0(0x0001, 0x3FD33333)
    Call(ScriptId.Current, 'ShowEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xF080, 0x00000040)
    ChrClearPhysicsFlags(0xF080, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'SpringOff')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrSetRGBA(PseudoChrId.Self, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetRGBA(0xFFF9, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0xF080, 0x00000080)
    ChrSetPhysicsFlags(0xF080, 0x00000020)
    ChrSetRGBA(0xF080, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 15.0, 0.0)
    SetChrPos(0xF080, 0.0, 0.0, -10.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0xF080, 0xFFFB, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0x64, 300, 1.0, 0)
    OP_43(0xFE, 0)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0xF080, '7', '0', '', '#b', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xF080, '', 0.0, 1.1, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x00, 2.0, -30.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.4, 0)
    Call(ScriptId.BtlCom, 'AniBtlTurnToThis')
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(590), ParamFloat(600), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(1390), ParamFloat(600), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    Sleep(1000)

    Sleep(333)

    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3B)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xF080, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0xF080, '2', '2', '', '#b', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 1.1, 25.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.0, 149.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.4, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.14, 24.67, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -14.0, 137.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x03, 2.3, 2000)
    CameraCmd(0x0B, 0x03, 40.0, 0x07D0)
    ChrSetRGBA(0xF080, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    PlayChrAnimeClip(0xF080, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0xF080, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FB7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    ChrSetRGBA(0xF080, 1.0, 1.0, 1.0, 1.0, 300, 0x03)
    PlayChrAnimeClip(0xF080, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(0xF080, 'L_hand_point', 'equ094c6', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(500)

    OP_2A(0x00, 0xF080, '', 'R_hand_point', 0x01)
    Sleep(333)

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.38, 1.08, 16.71, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.0, 149.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 9.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.0, -154.0, 0.0, 6000, 0x01)
    Sleep(666)

    PlayEffect(0xF080, ParamInt(0x0022), 0xF080, 0x0200000C, ParamStr(''), ParamFloat(-0.2), ParamFloat(1.5), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10A7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xF080, '', 'R_hand_point', 0x00)
    OP_76(0xF080, 'L_hand_point', 'equ094c7', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(266)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0), ParamFloat(0))
    Sleep(133)

    PlayChrAnimeClip(0xF080, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    LoadEffect(0xFFFE, 0x30, 'battle/cr035_03_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr035_03_1.eff', 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 0x00000005)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B89, 0x00000020)
    ChrSetPhysicsFlags(0x0B86, 0x00000080)
    ChrSetPhysicsFlags(0x0B87, 0x00000080)
    ChrSetPhysicsFlags(0x0B88, 0x00000080)
    ChrSetPhysicsFlags(0x0B89, 0x00000080)
    CreateThread(0x0B86, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B86, 0x02)

    CreateThread(0x0B87, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B87, 0x02)

    CreateThread(0x0B88, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B88, 0x02)

    CreateThread(0x0B89, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B89, 0x02)

    CreateThread(0x0B8A, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B8A, 0x02)

    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B89, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B89, 0xFFFB, 0.0, -1.0)
    BattleSetChrPos(0x0B8A, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B88, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B89, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B89, 0x00000040)
    ChrSetPhysicsFlags(0x0B89, 0x00000020)
    ChrSetPhysicsFlags(0x0B8A, 0x00000040)
    ChrSetPhysicsFlags(0x0B8A, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.1, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.2, 2200)
    CameraRotateByTarget(0xFFFE, '', 0x03, 8.0, -48.0, 0.0, 2200, 0x01)
    CameraSetDistance(0x03, 1.85, 2200)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft03_Mouth01', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B88, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B89, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1057), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 0.675, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000020)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B86, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 0.6, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B87, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B88, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B88, 0.525, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B88, 0x00000040)
    ChrClearPhysicsFlags(0x0B88, 0x00000020)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B88, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B89, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B89, 0.45, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0x0B89, 0x00000040)
    ChrClearPhysicsFlags(0x0B89, 0x00000020)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B89, '2', '0', '', '#b', '0')
    Sleep(333)

    Sleep(400)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.3, 0xFFFFFFFF)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 1.5, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, -30.0, 0.0, 300, 0x01)
    CameraSetDistance(0x03, 6.5, 300)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B86, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B88, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B89, '2', '2', '', '#b', '0')
    Sleep(33)

    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.15, 0.15, 0.35)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    Sleep(1)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.15, 8.5, 9.5)
    Sleep(2)

    CreateThread(0x0B86, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(0x0B86, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B87, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B88, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B88, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B88, 1.3, 0xFFFFFFFF)
    Sleep(2)

    CreateThread(0x0B89, 0x02, 'AniBtlCraft03_Dash', ScriptId.Current)
    PlayChrAnimeClip(0x0B89, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B89, 1.3, 0xFFFFFFFF)
    Sleep(200)

    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0x0B8A, '', 0.0, 1.25, 0.0, 4000)
    Sleep(66)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlCraft03_Damage', ScriptId.Current)
    Sleep(133)

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)

    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    WaitForThreadExit(0x0B88, 0x02)

    WaitForThreadExit(0x0B89, 0x02)

    ChrSetRGBA(PseudoChrId.Self, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B89, 0x00000040)
    ChrSetPhysicsFlags(0x0B89, 0x00000020)
    BattleDeleteChrDummy()
    Sleep(333)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    BattleCmd(0x6C, 0x0001)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, 3.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1)

    CameraCmd(0x10)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrClearPhysicsFlags(0xF080, 0x00000080)
    ChrClearPhysicsFlags(0xF080, 0x00000020)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00BA offset: 0x19158
@scena.Code('AniBtlTRIO')
def AniBtlTRIO():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BB, 4, 0x5DC)),
            Expr.Return,
        ),
        'loc_19282',
    )

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0xF04B),
            (Expr.PushLong, 0xF043),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1919E(): pass

    label('loc_1919E')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19282',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0xF043),
            (Expr.PushReg, 0x4),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr035')"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1926C',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr039')"),
            Expr.Return,
        ),
        'loc_1921D',
    )

    BattleCmd(0xBB, ArgReg(0x04), ParamInt(0))

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1921D(): pass

    label('loc_1921D')

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, ArgReg(0x06), 'chr037')"),
            Expr.Return,
        ),
        'loc_1925A',
    )

    BattleCmd(0xBB, ArgReg(0x04), ParamInt(0x0001))

    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1925A(): pass

    label('loc_1925A')

    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1926C',
    )

    def _loc_1926C(): pass

    label('loc_1926C')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1919E')

    def _loc_19282(): pass

    label('loc_19282')

    Call(ScriptId.Current, 'ShowEquip')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR035_SC1')
    LoadEffect(0xFFFE, 0x39, 'battle_sys/rushback2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr035_05_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr037_05_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr039_05_0.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x000005DC, 0x00000000)
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xF080, 0x00000040)
    ChrClearPhysicsFlags(0xF080, 0x00000020)
    ChrClearPhysicsFlags(0xF081, 0x00000040)
    ChrClearPhysicsFlags(0xF081, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Call(ScriptId.Current, 'SpringOff')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrSetRGBA(PseudoChrId.Self, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetRGBA(0xFFF9, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0xF080, 0x00000080)
    ChrSetPhysicsFlags(0xF080, 0x00000020)
    ChrSetRGBA(0xF080, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0xF081, 0x00000080)
    ChrSetPhysicsFlags(0xF081, 0x00000020)
    ChrSetPhysicsFlags(0xF081, 0x00000100)
    ChrSetRGBA(0xF081, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 10.0, 0.0)
    SetChrPos(0xF080, -5.0, 0.0, -5.0, 0.0)
    SetChrPos(0xF081, 5.0, 0.0, -5.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0xF080, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0xF081, 0xFFFB, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0x64, 300, 1.0, 0)
    OP_43(0xFE, 0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0xF080, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0xF081, '2', '2', '', '#b', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xF080, '', 0.0, 1.1, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x00, 2.0, -30.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.4, 0)
    Call(ScriptId.BtlCom, 'AniBtlTurnToThis')
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(980), ParamFloat(600), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(380), ParamFloat(600), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(1580), ParamFloat(600), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x04)
    Sleep(833)

    Sleep(500)

    Sleep(333)

    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xF080, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr039_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr039_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr039_01_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/cr039_00_5.eff', 0x00000000)
    ChrSetPhysicsFlags(0xF080, 0x00000200)
    OP_43(0x65, 50, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xF080, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xF080, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x03, 10.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraCmd(0x0F, 0xF080, 0.0, 1.5, 0.0)
    CameraSetHeight(0x03, -1.25, 4000)
    BattleCmd(0x4B, 0x0064, 0x03)
    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xF080, 10.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0xF080, 0x00000103, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xF080, 0.0, 0x00)

    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FB7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    BattleSaveChrPosition(0xF080, 0x00000000)
    Sleep(333)

    BattleSetChrPosAsync(0xF080, 0xF080, 0.0, 4.0, 0.0, 0.5, 0x02, 0x00)
    Sleep(166)

    OP_43(0x65, 400, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xF080, '', -0.0, 1.5, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x03, -11.0, -53.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraRotateByTarget(0xF080, '', 0x03, 0.0, 22.0, 3.0, 3000, 0x01)
    CameraSetDistance(0x03, 2.9, 3000)
    Sleep(433)

    SetChrFace(0x03, 0xF080, '', 'BJ1B10', '0', '#b', '0')
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xF080, '', 0.0, 1.35, 0.0, 0)
    OP_2A(0x00, 0xF080, '', 'R_hand_point', 0x01)
    Sleep(233)

    CameraSetPosByTarget(0x03, 0xF080, '', 0.0, 1.35, 0.0, 0)
    OP_76(0xF080, 'L_hand_point', 'equ094c4', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xF080, 0x00000103, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0.95), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x7537), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1067), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    WaitAnimeClip(0xF080, 0.0, 0x00)

    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1333)

    OP_80(0.0)
    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x3A)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xF080, 0x00000003, ParamStr(''), ParamFloat(-0.38), ParamFloat(1.34), ParamFloat(0.4), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1093), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.7, 250, 1500, 500, 0.6, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_76(0xF080, 'L_hand_point', 'equ094c5', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_2A(0x00, 0xF080, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xF080, 0.0, 0x00)

    SetChrFace(0x03, 0xF080, '6', '7373', '0', '#b', '0')
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleSetChrPosAsync(0xF080, 0xF080, 0.0, 2.0, 0.0, 0.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xF080, '', 0x03, 13.0, 157.0, -10.0, 0, 0x01)
    CameraSetDistance(0x03, 11.0, 0)
    CameraSetHeight(0x03, -3.5, 8000)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 2.0, 0.0, 8000)
    CameraCmd(0x11, 0x03, -26.0, 60.0, -1.0, 0x1F40, 0x01)
    BattleCmd(0x4B, 0x1F40, 0x03)
    OP_43(0xFF, 0, 0x0000)
    OP_80(0.0)
    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xF080, 0x3A)
    ReleaseEffect(0xF080, 0x3B)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xF080, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(-0.66), ParamFloat(2), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_76(0xF080, 'L_hand_point', 'equ094c5', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    OP_2A(0x00, 0xF080, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xF080, 0.0, 0x00)

    SetChrFace(0x03, 0xF080, '6', '7373', '0', '#b', '0')
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(833)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0), ParamFloat(0))
    WaitAnimeClip(0xF080, 0.0, 0x00)

    ChrSetRGBA(0xF080, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    PlayChrAnimeClip(0xF080, 'BTL_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xF080, 0xFFF4, 0.0, 0.0, 0.0, 2.0, 0x01, 0x00)
    CameraCmd(0x10)
    WaitAnimeClip(0xF080, 0.0, 0x00)

    ChrClearPhysicsFlags(0xF080, 0x00000200)
    Sleep(33)

    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr037_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/cr037_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/cr037_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/cr037_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/cr003_25_0.eff', 0x00000000)
    ChrSetRGBA(0xF080, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0xF081, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    OP_2A(0x00, 0xF081, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xF081, '', 'L_hand_point', 0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.0, 0.75, 0.0, 0)
    CameraRotateByTarget(0xF081, '', 0x03, 0.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.0, 1.25, 0.0, 1000)
    CameraRotateByTarget(0xF081, '', 0x03, -8.0, 0.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 2.0, 1000)
    CameraCmd(0x0B, 0x03, 40.0, 0x03E8)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xF081, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(2), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x03)
    PlayChrAnimeClip(0xF081, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xF081, 2.0, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x8F5A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F41), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xF081, 0.0, 0x00)

    Sleep(10)

    OP_43(0x65, 100, 1.0, 0)
    BattleCmd(0x6E, 0xF081, 0xFFFB, 0.0, 0.0, -2.6, 0.0)
    BattleCmd(0x47)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.0, 0.0, 0.0, 0)
    CameraRotateByTarget(0xF081, '', 0x03, 22.0, 15.0, -10.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraSetPosByTarget(0x03, 0xF081, '', 0.1, 4.9, 0.0, 2000)
    CameraRotateByTarget(0xF081, '', 0x03, 0.0, -15.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x03, 1.5, 2000)
    SetChrAniFunction(0xF081, 0x0A, 'SpringOff', -1.0, -1.0, 0x00000000)
    PlayChrAnimeClip(0xF081, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xF081, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A6C7',
    )

    def _loc_1A6C7(): pass

    label('loc_1A6C7')

    Sleep(333)

    OP_4E(0.5, 0.0, 0x03, 0x00)
    SetChrFace(0x03, 0xF081, '6', 'J737J7J7J7J7J7J', '05', '#b', '0')
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x8F47), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1500), ParamInt(300), 0x0000, 0x05DC, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(400)

    Sleep(333)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    BattleSetChrPosAsync(0xF081, 0xFFEF, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xF081, '', -2.0, 0.5, -1.0, 500)
    CameraCmd(0x11, 0x03, 0.0, 60.0, 0.0, 0x01F4, 0x01)
    CameraSetDistance(0x03, 8.0, 250)
    OP_3B(0x00, ParamInt(0x8F75), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.5), ParamFloat(-1), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0x04)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0xF081, 0x00000003, ParamStr(''), ParamFloat(0.5), ParamFloat(0.1), ParamFloat(2.5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    SetChrFace(0x03, 0xF081, '6', '7373', '0', '#b', '0')
    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x8F2A), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F54), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    BattleCmd(0x48, 0xF081, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0), ParamFloat(0))
    WaitAnimeClip(0xF081, 0.0, 0x00)

    PlayChrAnimeClip(0xF081, 'BTL_CRAFT00_01a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(266)

    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    ReleaseEffect(0xFFFE, 0x3E)
    BattleTargetsIterNext(0xFFFE)
    BattleTargetsIterNext(0xFFFE)
    ChrSetRGBA(0xF081, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    LoadEffect(0xFFFE, 0x30, 'battle/cr035_04_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr035_04_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr035_04_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr035_04_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr035_04_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr035_04_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr035_04_6.eff', 0x00000000)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 0x00000003)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B86, 0x00000080)
    ChrSetPhysicsFlags(0x0B87, 0x00000080)
    ChrSetPhysicsFlags(0x0B88, 0x00000080)
    CreateThread(0x0B86, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B86, 0x02)

    CreateThread(0x0B87, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B87, 0x02)

    CreateThread(0x0B88, 0x02, 'Ani_SC1_Load', ScriptId.Current)
    WaitForThreadExit(0x0B88, 0x02)

    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 120.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 240.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 180.0, -1.0)
    BattleSetChrPos(0x0B86, 0x0B86, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0x0B87, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFB, 0.0, -1.0)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B86, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B87, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    PlayChrAnimeClip(0x0B86, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 15.0, -50.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.4, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.2, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 26.0, 0.0, 700, 0x01)
    CameraSetDistance(0x03, 2.65, 700)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Target, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(300)

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.35, 0.2, 700)
    CameraSetDistance(0x00, 3.8, 700)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)

    CameraSetDistance(0x03, 4.5, 700)
    Sleep(233)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, -160.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 7.1, 0)
    OP_43(0xFF, 0, 0x0000)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000020)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 1.2, 0.0, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -240.0, 0.0, 4000, 0x01)
    CameraSetDistance(0x03, 8.1, 4000)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B86, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B87, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10E0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    SetChrFace(0x03, 0x0B86, '3', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 1.4, 0xFFFFFFFF)
    Sleep(33)

    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 1.4, 0xFFFFFFFF)
    Sleep(300)

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.2, 0xFFFFFFFF)
    WaitAnimeClip(0x0B87, 0.0, 0x00)

    WaitAnimeClip(0x0B86, 0.0, 0x00)

    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 1.4, 0xFFFFFFFF)
    OP_6C(0x0B87, 1.4, 0xFFFFFFFF)
    SetChrFace(0x03, 0x0B86, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '2', '2', '', '#b', '0')
    Sleep(100)

    CreateThread(0x0B86, 0x02, 'AniBtlCraft04_Dash', ScriptId.Current)
    CreateThread(0x0B87, 0x02, 'AniBtlCraft04_Dash', ScriptId.Current)
    Sleep(100)

    ChrClearPhysicsFlags(0x0B88, 0x00000040)
    ChrClearPhysicsFlags(0x0B88, 0x00000020)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0x0B88, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(0.9), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.15, 0.15, 0.5)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    OP_5E(0x00, 0x0002, 0.45, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(66)

    OP_5E(0x01, 0x0190)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(33)

    CameraSetDistance(0x00, 9.1, 1500)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.4, 0xFFFFFFFF)
    Sleep(66)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft04_Dash2', ScriptId.Current)
    OP_3B(0x00, ParamInt(0x1043), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleSetChrPos(0x0B86, 0x0B86, 2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0x0B87, -2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 180.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFB, 180.0, -1.0)
    PlayChrAnimeClip(0x0B86, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B86, 0.5, 0xFFFFFFFF)
    PlayChrAnimeClip(0x0B87, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B87, 0.5, 0xFFFFFFFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 1.2, 1.0, 0.35, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 20.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 2.5, 1.0, 0.35, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 10.0, 11.0, 4000, 0x01)
    CameraSetDistance(0x03, 3.0, 4000)
    CameraCmd(0x09, 0.2, 0.2, 2.0)
    Sleep(66)

    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x01, 0x0320)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    Sleep(1333)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0), ParamFloat(0))
    Sleep(1000)

    ReleaseEffect(0xFFFE, 0x39)
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xF080, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xF081, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x02)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    BattleDeleteChrDummy()
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrClearPhysicsFlags(0xF080, 0x00000080)
    ChrClearPhysicsFlags(0xF080, 0x00000020)
    ChrClearPhysicsFlags(0xF081, 0x00000080)
    ChrClearPhysicsFlags(0xF081, 0x00000020)
    ChrClearPhysicsFlags(0xF081, 0x00000100)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00BB offset: 0x1BE4C
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x138),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BE78',
    )

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x28AD))

    def _loc_1BE78(): pass

    label('loc_1BE78')

    Return()

# id: 0x00BC offset: 0x1BE7C
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    Call(ScriptId.BtlCom, 'SET_MOVE_SPEED', ParamFloat(6))
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR035_SC1')
    BattleCmd(0x52, 0xFFFE, 0x38)
    LoadEffect(0xFFFE, 0x39, 'battle/sc035_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc035_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc035_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc035_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc035_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc035_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3F, 'battle/sc035_00_6.eff', 0x00000000)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x000005DC, 0x00000000)
    Call(ScriptId.Current, 'ShowEquip')
    OP_C0(0x0001, 0x3FD33333)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    Call(ScriptId.Current, 'SpringOff')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    BattleCreateChrDummy(0xFFFE, 0x00000005)
    AnimeClipAddAsset(0x0B86, 'C_CHR035_SC1')
    AnimeClipAddAsset(0x0B87, 'C_CHR035_SC1')
    AnimeClipAddAsset(0x0B88, 'C_CHR035_SC1')
    AnimeClipAddAsset(0x0B89, 'C_CHR035_SC1')
    AnimeClipAddAsset(0x0B8A, 'C_CHR035_SC1')
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    ChrSetPhysicsFlags(0x0B87, 0x00000020)
    ChrSetPhysicsFlags(0x0B88, 0x00000020)
    ChrSetPhysicsFlags(0x0B89, 0x00000020)
    ChrSetPhysicsFlags(0x0B8A, 0x00000020)
    ChrSetPhysicsFlags(0x0B86, 0x00000080)
    ChrSetPhysicsFlags(0x0B87, 0x00000080)
    ChrSetPhysicsFlags(0x0B88, 0x00000080)
    ChrSetPhysicsFlags(0x0B89, 0x00000080)
    ChrSetPhysicsFlags(0x0B8A, 0x00000080)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrSetPhysicsFlags(0x0B86, 0x00000800)
    ChrSetPhysicsFlags(0x0B87, 0x00000800)
    ChrSetPhysicsFlags(0x0B88, 0x00000800)
    ChrSetPhysicsFlags(0x0B89, 0x00000800)
    ChrSetPhysicsFlags(0x0B8A, 0x00000800)
    ChrSetPhysicsFlags(0x0B86, 0x00000200)
    ChrSetPhysicsFlags(0x0B87, 0x00000200)
    ChrSetPhysicsFlags(0x0B88, 0x00000200)
    ChrSetPhysicsFlags(0x0B89, 0x00000200)
    ChrSetPhysicsFlags(0x0B8A, 0x00000200)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 10.0, 0.0)
    SetChrPos(0x0B86, 0.0, 0.0, 11.0, 0.0)
    SetChrPos(0x0B87, 0.0, 0.0, 11.0, 0.0)
    SetChrPos(0x0B88, 0.0, 0.0, 11.0, 0.0)
    SetChrPos(0x0B89, 0.0, 0.0, 11.0, 0.0)
    SetChrPos(0x0B8A, 0.0, 0.0, 11.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFF, 0.0, -1.0)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B89, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B8A, 0xFFFE, 0.0, -1.0)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B88, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(33)

    PlayChrAnimeClip(0x0B89, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(33)

    PlayChrAnimeClip(0x0B8A, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B87, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B89, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B8A, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B8A, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B89, 0x00000040)
    ChrSetPhysicsFlags(0x0B8A, 0x00000040)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    OP_43(0x64, 300, 1.0, 0)
    OP_43(0xFE, 0)
    Sleep(0)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B86, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B88, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B89, '7', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B8A, '7', '0', '', '#b', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.1, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, -45.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 3.4, 0)
    Call(ScriptId.BtlCom, 'AniBtlTurnToThis')
    OP_43(0xFF, 0, 0x0000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, 35.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x00, 2.6, 3000)
    OP_3B(0x32, ParamInt(0x284D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_Mouth01', ScriptId.Current)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.4, 0.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -3.0, -5.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 1.3, 1000)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.45, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -4.0, -10.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x00, 1.1, 2000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B86, '2', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B87, '2', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B88, '2', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B89, '2', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B8A, '2', '0', '', '#b', '0')
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.5, 0.9, 0.0, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, -3.0, -60.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 4.2, 500)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B86, 0x00000080)
    ChrSetPhysicsFlags(0x0B87, 0x00000080)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    Sleep(100)

    CreateThread(0x0B86, 0x02, 'AniBtlSCraft00_DUMMY0appear', ScriptId.Current)
    CreateThread(0x0B87, 0x03, 'AniBtlSCraft00_DUMMY1appear', ScriptId.Current)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x104F), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10D7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(400)

    OP_5E(0x01, 0x03E8)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.65, 0.9, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.0, -45.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x03, 5.2, 2000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_05', 0x00, 0x01, 0x00, 0x00, 0x00, 0.35, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x01, 0x01, 0x00, 0x00, 0x00, 0.35, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_04', 0x01, 0x01, 0x00, 0x00, 0x00, 0.35, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(0x0B86, 0x02)

    WaitForThreadExit(0x0B87, 0x03)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    CameraSetPosByTarget(0x03, 0x0B86, '', -0.4, 0.9, -0.2, 500)
    CameraRotateByTarget(0x0B86, '', 0x03, 3.0, -35.0, 2.0, 500, 0x01)
    CameraSetDistance(0x03, 2.3, 500)
    Sleep(200)

    SetChrFace(0x03, 0x0B86, '3', '0', '', '#b', '0')
    Sleep(233)

    SetChrFace(0x03, 0x0B86, '2', '0', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0x0B86, '', 0.0, 0.8, -0.4, 1200)
    CameraRotateByTarget(0x0B86, '', 0x00, 7.0, -5.0, 3.0, 1200, 0x01)
    CameraSetDistance(0x00, 1.0, 1200)
    WaitAnimeClip(0x0B86, 0.0, 0x00)

    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_06', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(66)

    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    SetChrFace(0x03, 0x0B86, '2', '2', '', '#b', '0')
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    CreateThread(0x0B86, 0x02, 'AniBtlSCraft00_DUMMY0Dash01', ScriptId.Current)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    CameraSetPosByTarget(0x03, 0x0B86, '', 0.0, 0.9, 10.0, 1000)
    Sleep(33)

    WaitForThreadExit(0x0B86, 0x02)

    OP_5E(0x01, 0x012C)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CreateThread(0x0B86, 0x02, 'AniBtlSCraft00_DUMMY0Dash02', ScriptId.Current)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1034), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPos(0x00, 0.0, 1.1, 4.0, 0)
    CameraRotate(0x00, 3.0, 2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 12.5, 0)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    CameraSetPos(0x03, 0.0, 1.1, 0.0, 1200)
    CameraRotate(0x03, 6.0, -25.0, 9.0, 1200, 0x01)
    CameraSetDistance(0x03, 7.5, 1200)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(66)

    OP_5E(0x00, 0x0002, 0.55, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    WaitForThreadExit(0x0B86, 0x02)

    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFF, 60.0, -1.0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_DamageAnime', ScriptId.Current)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 1.1, -5.0, 2100)
    CameraRotate(0x03, 6.0, 15.0, 5.0, 2100, 0x01)
    CameraSetDistance(0x03, 9.5, 2100)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    CreateThread(0x0B87, 0x03, 'AniBtlSCraft00_DUMMY1Dash01', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B87, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_10', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1034), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    WaitForThreadExit(0x0B87, 0x03)

    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B87, 0xFFFF, -60.0, -1.0)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    OP_5E(0x01, 0x012C)
    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrClearPhysicsFlags(0x0B87, 0x00000040)
    ChrClearPhysicsFlags(0x0B88, 0x00000040)
    ChrClearPhysicsFlags(0x0B89, 0x00000040)
    ChrClearPhysicsFlags(0x0B8A, 0x00000040)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 0.0, 0.0)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B8A, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    SetChrPos(0x0B86, -12.0, 0.0, -9.5, 0.0)
    SetChrPos(0x0B87, 12.0, 0.0, -2.5, 0.0)
    BattleSetChrPos(0x0B88, 0x0B86, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B89, 0x0B86, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B8A, 0x0B87, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B89, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B8A, 0xFFFE, 0.0, -1.0)
    BattleSetChrPos(0x0B89, 0x0B89, 10.0, 0.0, 6.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B88, 0x0B88, -10.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 0.0, -1.0)
    BattleSetChrPos(0x0B88, 0x0B88, -6.0, 0.0, 7.6, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B8A, 0x0B8A, 9.5, 0.0, 4.6, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B87, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B89, 0xFFFE, 0.0, -1.0)
    BattleTurnChrDirection(0x0B8A, 0xFFFE, 0.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_12', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 10.0, 0.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    CameraSetPos(0x03, 0.58, 0.81, 0.44, 0)
    CameraRotate(0x03, 33.0, 63.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 9.0, 0)
    CameraCmd(0x0B, 0x03, 38.0, 0x0000)
    CameraRotate(0x00, 3.0, 110.0, 0.0, 5500, 0x01)
    CameraSetDistance(0x00, 10.6, 5500)
    OP_3B(0x32, ParamInt(0x284F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B8A, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1034), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    CreateThread(0x0B86, 0x01, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(180)

    OP_5E(0x00, 0x0002, 0.45, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 100, 0x03)
    WaitForThreadExit(0x0B86, 0x01)

    BattleTurnChrDirection(0x0B86, 0xFFFF, 130.0, -1.0)
    PlayChrAnimeClip(0x0B86, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    Sleep(66)

    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    CreateThread(0x0B87, 0x02, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_DamageAnime', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B87, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Sleep(100)

    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 300, 0x03)
    OP_43(0x65, 50, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPos(0x03, -0.39, 1.1, -0.81, 0)
    CameraRotate(0x03, 12.0, 26.0, -10.0, 0, 0x01)
    CameraSetDistance(0x03, 10.2, 0)
    CameraSetPos(0x03, -0.39, -1.1, -0.81, 6000)
    CameraRotate(0x03, 65.0, 170.0, -10.0, 6000, 0x01)
    PlayChrAnimeClip(0x0B88, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    Sleep(66)

    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    CreateThread(0x0B88, 0x03, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    OP_5E(0x00, 0x0002, 0.65, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B88, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.8), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    WaitForThreadExit(0x0B87, 0x02)

    PlayChrAnimeClip(0x0B87, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B87, 0xFFFF, -130.0, -1.0)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_DamageAnime', ScriptId.Current)
    SetChrPos(0x0B86, -8.0, 0.0, -6.0, 0.0)
    Sleep(1)

    BattleTurnChrDirection(0x0B86, 0x0B86, 0.0, -1.0)
    PlayChrAnimeClip(0x0B89, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    Sleep(66)

    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    CreateThread(0x0B89, 0x01, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B89, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    PlayChrAnimeClip(0x0B8A, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 30.5333, 31.2333, -1.0, 0x00, 0x00)
    Sleep(66)

    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    CreateThread(0x0B8A, 0x02, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CameraCmd(0x09, 0.055, 0.055, 0.3)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0x0B8A, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitForThreadExit(0x0B88, 0x03)

    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(0x0B86, 0x03, 'AniBtlSCraft00_DUMMYDashF', ScriptId.Current)
    CameraCmd(0x09, 0.15, 0.15, 3.0)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_DamageAnime', ScriptId.Current)
    Sleep(166)

    Sleep(166)

    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    OP_43(0x03, 1000, 1.0, 0)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10F0), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1063), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0xFF, 0, 0x0000)
    OP_5E(0x01, 0x0064)
    WaitForThreadExit(0x0B89, 0x01)

    WaitForThreadExit(0x0B8A, 0x02)

    PlayChrAnimeClip(0x0B88, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B89, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B8A, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B89, 0xFFFF, -55.0, -1.0)
    BattleTurnChrDirection(0x0B8A, 0xFFFF, 0.0, -1.0)
    BattleTurnChrDirection(0x0B88, 0xFFFF, 45.0, -1.0)
    WaitForThreadExit(0x0B86, 0x03)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Sleep(333)

    OP_43(0x67, 1200, 1.0, 0)
    CameraCmd(0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    SetChrPos(0x0B86, -6.0, 0.0, 6.0, 0.0)
    SetChrPos(0x0B87, 6.5, 0.0, 5.0, 0.0)
    SetChrPos(0x0B88, -5.5, 0.0, -2.0, 0.0)
    SetChrPos(0x0B89, 6.2, 0.0, -4.6, 0.0)
    SetChrPos(0x0B8A, -1.0, 0.0, -7.0, 0.0)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B86, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B87, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B88, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B89, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B8A, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.1, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, 5.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1175, 0)
    SetChrFace(0x03, PseudoChrId.Self, '7', 'A', '', '#b', '0')
    EffectCmd(0x0F, 0xFFFE, 0x003C, 0x01)
    ReleaseEffect(0xFFFE, 0x3C)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc035_00_8.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 44.0, 44.9, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.5, 0.0, 700)
    CameraRotateByTarget(0xFFFE, '', 0x00, 4.0, 15.0, 4.0, 700, 0x01)
    CameraSetDistance(0x00, 1.395, 700)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x13F0), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.7, 1.0, 0.1, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 12.0, -25.0, 9.0, 500, 0x01)
    CameraSetDistance(0x03, 2.1, 500)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x32, ParamInt(0x284E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.7, 0.8, 0.2, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 14.0, 45.0, 0.0, 4000, 0x01)
    CameraSetDistance(0x03, 3.4, 4000)
    Sleep(1800)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_15', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, 56.6667, 56.7, -1.0, 0x00, 0x00)
    CameraSetDistance(0x00, 1.0, 400)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x10F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft00_Dash02', ScriptId.Current)
    Sleep(33)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.7, 1.0, 8.0, 320)
    CameraCmd(0x11, 0x03, 2.0, 45.0, 0.0, 0x0140, 0x01)
    CameraSetDistance(0x03, 4.6, 320)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_43(0x65, 100, 1.0, 0)
    OP_3B(0x00, ParamInt(0x10F0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.9, 2.2, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 0.0, 75.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.5, 0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    ChrSetPhysicsFlags(0x0B87, 0x00000040)
    ChrSetPhysicsFlags(0x0B88, 0x00000040)
    ChrSetPhysicsFlags(0x0B89, 0x00000040)
    ChrSetPhysicsFlags(0x0B8A, 0x00000040)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -4.0, -1.0, 0x00, 0x00)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 2.0, 800)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 68.0, -7.0, 800, 0x01)
    CameraSetDistance(0x03, 4.5, 800)
    Sleep(666)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.95, 0.2, 500)
    CameraRotateByTarget(0xFFFE, '', 0x00, 0.0, 90.0, -7.0, 500, 0x01)
    CameraSetDistance(0x03, 1.575, 700)
    OP_3B(0x32, ParamInt(0x2850), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_Mouth02', ScriptId.Current)
    Sleep(500)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraft00_Camera', ScriptId.Current)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft00_Dash03', ScriptId.Current)
    Sleep(166)

    CameraSetDistance(0x03, 3.5, 500)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_15', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    Sleep(266)

    Sleep(100)

    TerminateThread(PseudoChrId.Self, 0x03)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.4, 2.2, 500)
    CameraRotateByTarget(0xFFFE, '', 0x00, 9.0, 5.0, -7.0, 500, 0x01)
    CameraSetDistance(0x00, 8.875, 500)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraCmd(0x09, 0.155, 0.225, 0.7)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1074), ParamFloat(0.4), ParamInt(0x0064), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    Sleep(100)

    OP_5E(0x01, 0x0258)
    CameraCmd(0x09, 0.175, 0.295, 3.0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_Damage', ScriptId.Current)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.4, 3.2, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 12.0, 5.0, -7.0, 2000, 0x01)
    CameraSetDistance(0x00, 10.275, 2000)
    OP_43(0x03, 2000, 1.0, 0)
    OP_3B(0x00, ParamInt(0x0FC7), ParamFloat(2), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(700)

    Sleep(1500)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_Damage02', ScriptId.Current)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    OP_43(0xFF, 0, 0x0000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    ChrClearPhysicsFlags(0x0B86, 0x00000020)
    ChrClearPhysicsFlags(0x0B87, 0x00000020)
    ChrClearPhysicsFlags(0x0B88, 0x00000020)
    ChrClearPhysicsFlags(0x0B89, 0x00000020)
    ChrClearPhysicsFlags(0x0B8A, 0x00000020)
    ChrClearPhysicsFlags(0x0B86, 0x00000080)
    ChrClearPhysicsFlags(0x0B87, 0x00000080)
    ChrClearPhysicsFlags(0x0B88, 0x00000080)
    ChrClearPhysicsFlags(0x0B89, 0x00000080)
    ChrClearPhysicsFlags(0x0B8A, 0x00000080)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrClearPhysicsFlags(0x0B86, 0x00000800)
    ChrClearPhysicsFlags(0x0B87, 0x00000800)
    ChrClearPhysicsFlags(0x0B88, 0x00000800)
    ChrClearPhysicsFlags(0x0B89, 0x00000800)
    ChrClearPhysicsFlags(0x0B8A, 0x00000800)
    ChrClearPhysicsFlags(0x0B86, 0x00000200)
    ChrClearPhysicsFlags(0x0B87, 0x00000200)
    ChrClearPhysicsFlags(0x0B88, 0x00000200)
    ChrClearPhysicsFlags(0x0B89, 0x00000200)
    ChrClearPhysicsFlags(0x0B8A, 0x00000200)
    BattleDeleteChrDummy()
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
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
    BattleCmd(0x6C, 0x0001)
    Sleep(1)

    Call(ScriptId.BtlCom, 'RESET_MOVE_SPEED')
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00BD offset: 0x1F25C
@scena.Code('AniBtlSCraft00_Mouth01')
def AniBtlSCraft00_Mouth01():
    SetChrFace(0x03, PseudoChrId.Self, '3', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '3', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')

    Return()

# id: 0x00BE offset: 0x1F338
@scena.Code('AniBtlSCraft00_Mouth02')
def AniBtlSCraft00_Mouth02():
    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '3', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '3', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', 'B', '', '#b', '0')

    Return()

# id: 0x00BF offset: 0x1F414
@scena.Code('AniBtlSCraft00_Damage')
def AniBtlSCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)

    def _loc_1F424(): pass

    label('loc_1F424')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_1F4DD',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1F4BF',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), PseudoChrId.Target, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0xFF)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    Sleep(300)

    BattleSetChrFlags(0xFFFB, 0x01000000)

    def _loc_1F4BF(): pass

    label('loc_1F4BF')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1F424')

    def _loc_1F4DD(): pass

    label('loc_1F4DD')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x00C0 offset: 0x1F4E8
@scena.Code('AniBtlSCraft00_Damage02')
def AniBtlSCraft00_Damage02():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)

    def _loc_1F4F8(): pass

    label('loc_1F4F8')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_1F55F',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1F53A',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleClearChrFlags(0xFFFB, 0x01000000)

    def _loc_1F53A(): pass

    label('loc_1F53A')

    Sleep(1)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1F4F8')

    def _loc_1F55F(): pass

    label('loc_1F55F')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x00C1 offset: 0x1F56C
@scena.Code('AniBtlSCraft00_DamageAnime')
def AniBtlSCraft00_DamageAnime():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)

    def _loc_1F57C(): pass

    label('loc_1F57C')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_1F5D7',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_1F5B2',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    def _loc_1F5B2(): pass

    label('loc_1F5B2')

    Sleep(30)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1F57C')

    def _loc_1F5D7(): pass

    label('loc_1F5D7')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x00C2 offset: 0x1F5E4
@scena.Code('AniBtlSCraft00_Dash')
def AniBtlSCraft00_Dash():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 5.2, 0x00, 0x00)

    Return()

# id: 0x00C3 offset: 0x1F604
@scena.Code('AniBtlSCraft00_DUMMY0appear')
def AniBtlSCraft00_DUMMY0appear():
    BattleSetChrPos(0xFFFE, 0xFFFE, -2.2, 0.0, 0.0, 0.7, 0x00, 0x00)

    Return()

# id: 0x00C4 offset: 0x1F624
@scena.Code('AniBtlSCraft00_DUMMY1appear')
def AniBtlSCraft00_DUMMY1appear():
    BattleSetChrPos(0xFFFE, 0xFFFE, 2.2, 0.0, 0.0, 0.7, 0x00, 0x00)

    Return()

# id: 0x00C5 offset: 0x1F644
@scena.Code('AniBtlSCraft00_DUMMY0Dash01')
def AniBtlSCraft00_DUMMY0Dash01():
    BattleTurnChrDirection(0xFFFE, 0xFFFE, 10.0, -1.0)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 20.0, 10.0, 0x00, 0x00)

    Return()

# id: 0x00C6 offset: 0x1F674
@scena.Code('AniBtlSCraft00_DUMMY0Dash02')
def AniBtlSCraft00_DUMMY0Dash02():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -30.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 40.0, 8.0, 0x00, 0x00)

    Return()

# id: 0x00C7 offset: 0x1F6B0
@scena.Code('AniBtlSCraft00_DUMMY1Dash01')
def AniBtlSCraft00_DUMMY1Dash01():
    BattleSetChrPos(0xFFFE, 0xFFFE, 5.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFE, -40.0, -1.0)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 40.0, 8.0, 0x00, 0x00)

    Return()

# id: 0x00C8 offset: 0x1F6FC
@scena.Code('AniBtlSCraft00_DUMMY0Dash03')
def AniBtlSCraft00_DUMMY0Dash03():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 20.0, 10.0, 0x00, 0x00)

    Return()

# id: 0x00C9 offset: 0x1F71C
@scena.Code('AniBtlSCraft00_DUMMYDashF')
def AniBtlSCraft00_DUMMYDashF():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 20.0, 10.0, 0x00, 0x00)

    Return()

# id: 0x00CA offset: 0x1F73C
@scena.Code('AniBtlSCraft00_Dash02')
def AniBtlSCraft00_Dash02():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 4.0, 6.0, 0x00, 0x00)

    Return()

# id: 0x00CB offset: 0x1F75C
@scena.Code('AniBtlSCraft00_Dash03')
def AniBtlSCraft00_Dash03():
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -3.0, 2.0, 0x00, 0x01)

    Return()

# id: 0x00CC offset: 0x1F77C
@scena.Code('AniBtlSCraft00_Camera')
def AniBtlSCraft00_Camera():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1F7B3',
    )

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.9, 0.2, 1)
    Sleep(1)

    Jump('AniBtlSCraft00_Camera')

    def _loc_1F7B3(): pass

    label('loc_1F7B3')

    Return()

# id: 0x00CD offset: 0x1F7B4
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x1F7E4
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CF offset: 0x1F814
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x1F844
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D1 offset: 0x1F884
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D2 offset: 0x1F8C0
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
        'loc_1F94F',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_1FA28')

    def _loc_1F94F(): pass

    label('loc_1F94F')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1F9CA',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Jump('loc_1FA28')

    def _loc_1F9CA(): pass

    label('loc_1F9CA')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1FA28(): pass

    label('loc_1FA28')

    Return()

# id: 0x00D3 offset: 0x1FA2C
@scena.Code('AniEvIdle')
def AniEvIdle():
    OP_80(0.2)
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D4 offset: 0x1FAC8
@scena.Code('AniEvIdle2')
def AniEvIdle2():
    OP_80(0.2)
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D5 offset: 0x1FB68
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x00D6 offset: 0x1FC50
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D7 offset: 0x1FCF4
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D8 offset: 0x1FD68
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x1FDCC
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DA offset: 0x1FE70
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DB offset: 0x1FF2C
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DC offset: 0x1FFE8
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DD offset: 0x20070
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x20130
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x201F0
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E0 offset: 0x202AC
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E1 offset: 0x20334
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E2 offset: 0x203F0
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E3 offset: 0x204B0
@scena.Code('AniEvAria')
def AniEvAria():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E4 offset: 0x20564
@scena.Code('AniEvArts')
def AniEvArts():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E5 offset: 0x2064C
@scena.Code('AniEvItem')
def AniEvItem():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E6 offset: 0x20760
@scena.Code('AniEvOrder')
def AniEvOrder():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E7 offset: 0x2081C
@scena.Code('AniEvWin')
def AniEvWin():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'ShowEquip')
    Sleep(3066)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x20900
@scena.Code('AniEv_C4_02_02_04')
def AniEv_C4_02_02_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_C4_02_02_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E9 offset: 0x2093C
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00EA offset: 0x209D4
@scena.Code('AniEvCraft00_01')
def AniEvCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EB offset: 0x20A58
@scena.Code('AniEvCraft00_03')
def AniEvCraft00_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EC offset: 0x20B38
@scena.Code('AniEvCraft00_03b')
def AniEvCraft00_03b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00ED offset: 0x20B74
@scena.Code('AniEvCraft01_01')
def AniEvCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EE offset: 0x20BE4
@scena.Code('AniEvSCraft01_01')
def AniEvSCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x20C20
@scena.Code('AniEvSCraft01_02')
def AniEvSCraft01_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 10.0, 11.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x20CD4
@scena.Code('AniEvSCraft01_04')
def AniEvSCraft01_04():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x20D10
@scena.Code('AniEvSCraft01_05')
def AniEvSCraft01_05():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_07', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F2 offset: 0x20DC4
@scena.Code('AniEvSCraft01_07')
def AniEvSCraft01_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_07', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x20E00
@scena.Code('AniEvSCraft01_08')
def AniEvSCraft01_08():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x20E3C
@scena.Code('AniEvSCraft01_09')
def AniEvSCraft01_09():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_09', 0x01, 0x01, 0x00, 0x01, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x20E78
@scena.Code('AniEvSCraft01_10')
def AniEvSCraft01_10():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_11', 0x01, 0x01, 0x00, 0x01, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.3, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F6 offset: 0x20F00
@scena.Code('AniEvSCraft01_12')
def AniEvSCraft01_12():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_12', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F7 offset: 0x20F3C
@scena.Code('AniEvSCraft01_13')
def AniEvSCraft01_13():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_15', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x20FF0
@scena.Code('AniEvSCraft01_14')
def AniEvSCraft01_14():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F9 offset: 0x2102C
@scena.Code('AniEvSCraft01_17')
def AniEvSCraft01_17():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_17', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FA offset: 0x21068
@scena.Code('AniEvKamiharai')
def AniEvKamiharai():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_KAMIHARAI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FB offset: 0x2111C
@scena.Code('AniEvMukkii')
def AniEvMukkii():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MUKKII', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FC offset: 0x211CC
@scena.Code('AniEvMukkii_Loop')
def AniEvMukkii_Loop():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)

    def _loc_211FE(): pass

    label('loc_211FE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2129B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_MUKKII', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    OP_17(0x03E8, 0x0BB8)

    Jump('loc_211FE')

    def _loc_2129B(): pass

    label('loc_2129B')

    Return()

# id: 0x00FD offset: 0x2129C
@scena.Code('AniEvTeKosi')
def AniEvTeKosi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_213C4',
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
        'loc_21376',
    )

    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)

    Jump('loc_213AF')

    def _loc_21376(): pass

    label('loc_21376')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_213AF(): pass

    label('loc_213AF')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2174A')

    def _loc_213C4(): pass

    label('loc_213C4')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_21601',
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_21497',
    )

    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIb_U', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_215F8')

    def _loc_21497(): pass

    label('loc_21497')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetEndhookFunction('', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_215F8',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_215A2',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_2156E(): pass

    label('loc_2156E')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_2159B',
    )

    Sleep(10)

    Jump('loc_2156E')

    def _loc_2159B(): pass

    label('loc_2159B')

    Sleep(300)

    def _loc_215A2(): pass

    label('loc_215A2')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_215F8(): pass

    label('loc_215F8')

    Jump('loc_2174A')

    def _loc_21601(): pass

    label('loc_21601')

    OP_80(0.4)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_216D1',
    )

    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_2174A')

    def _loc_216D1(): pass

    label('loc_216D1')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_2174A(): pass

    label('loc_2174A')

    Return()

# id: 0x00FE offset: 0x2174C
@scena.Code('AniEvTeKosiTeburi')
def AniEvTeKosiTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_80(0.4)
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_2182F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSI_t_U', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_218AA')

    def _loc_2182F(): pass

    label('loc_2182F')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSI_t', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEKOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_218AA(): pass

    label('loc_218AA')

    Return()

# id: 0x00FF offset: 0x218AC
@scena.Code('AniEvHookaki')
def AniEvHookaki():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1_2', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_HOOKAKI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Call(ScriptId.Common, 'LookEyeRateOn')
    Sleep(1333)

    Call(ScriptId.Common, 'LookEyeRateOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0100 offset: 0x21990
@scena.Code('AniEv02005')
def AniEv02005():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV02005', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0101 offset: 0x219F8
@scena.Code('AniEv02005b')
def AniEv02005b():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV02005b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV02005c', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0102 offset: 0x21A94
@scena.Code('AniEv02010')
def AniEv02010():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev02010', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev02010a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0103 offset: 0x21B1C
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

# id: 0x0104 offset: 0x21BC8
@scena.Code('AniEv03001')
def AniEv03001():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03001', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x0105 offset: 0x21C40
@scena.Code('AniEv03540')
def AniEv03540():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03540', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV03540a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0106 offset: 0x21CC8
@scena.Code('AniEv03540a')
def AniEv03540a():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV03540a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0107 offset: 0x21CFC
@scena.Code('AniEv30005')
def AniEv30005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30005', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev30005a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0108 offset: 0x21D84
@scena.Code('AniEv34505')
def AniEv34505():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev34505', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev34505a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0109 offset: 0x21E0C
@scena.Code('AniEv34540')
def AniEv34540():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev34540', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x010A offset: 0x21E68
@scena.Code('AniEv35000')
def AniEv35000():
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    SetEndhookFunction('ShowEquip', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Sleep(533)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_3B(0x00, ParamInt(0x7533), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7557), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x010B offset: 0x22010
@scena.Code('AniEv35000b')
def AniEv35000b():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(533)

    Sleep(833)

    OP_3B(0x00, ParamInt(0x7557), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x010C offset: 0x220D4
@scena.Code('AniEv37000')
def AniEv37000():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV37000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x010D offset: 0x22108
@scena.Code('AniAttachE07EVT02C')
def AniAttachE07EVT02C():
    LoadAsset('O_E07EVT02D')
    AttachEquip(0xFFFE, 'O_E07EVT02D', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x010E offset: 0x221A4
@scena.Code('AniDetachE07EVT02C')
def AniDetachE07EVT02C():
    ReleaseAsset('O_E07EVT02D')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x010F offset: 0x221FC
@scena.Code('AniEv52650')
def AniEv52650():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV52650', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 1.16667, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0110 offset: 0x22250
@scena.Code('AniAttachEQU962')
def AniAttachEQU962():
    LoadAsset('C_EQU962')
    AttachEquip(0xFFFE, 'C_EQU962', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0111 offset: 0x222E8
@scena.Code('AniDetachEQU962')
def AniDetachEQU962():
    ReleaseAsset('C_EQU962')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0112 offset: 0x2233C
@scena.Code('AniEv54575')
def AniEv54575():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV54575', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0113 offset: 0x22370
@scena.Code('AniEv70001_7')
def AniEv70001_7():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70001_7', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70001_7a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0114 offset: 0x223DC
@scena.Code('AniEv70125')
def AniEv70125():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70125', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0115 offset: 0x22430
@scena.Code('AniEv76050')
def AniEv76050():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV76050', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV76050a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0116 offset: 0x22498
@scena.Code('AniEv79321')
def AniEv79321():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79321', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79321a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0117 offset: 0x22520
@scena.Code('AniEv79321a')
def AniEv79321a():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79321a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0118 offset: 0x22578
@scena.Code('AniEv79322')
def AniEv79322():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79322', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79322a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0119 offset: 0x22600
@scena.Code('AniEv79323')
def AniEv79323():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79323', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79323a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011A offset: 0x22688
@scena.Code('AniMG12Wait')
def AniMG12Wait():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011B offset: 0x226C0
@scena.Code('AniMG12LeanLeft')
def AniMG12LeanLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA_SLANT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011C offset: 0x22700
@scena.Code('AniMG12LeanRight')
def AniMG12LeanRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'MG12_BANANA_SLANT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x011D offset: 0x22740
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR035_EV', 'ev35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk035_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk035_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk035_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk035_a1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk035_a2.eff', 0x00000000)

    Return()

# id: 0x011E offset: 0x22808
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'ev35000')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x011F offset: 0x22864
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOn')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0120 offset: 0x228DC
@scena.Code('AniCvIdle')
def AniCvIdle():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetEndhookFunction('DefaultFace', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_229C0',
    )

    OP_3B(0x32, ParamInt(0x2892), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_22A15')

    def _loc_229C0(): pass

    label('loc_229C0')

    OP_3B(0x32, ParamInt(0x2893), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_22A15(): pass

    label('loc_22A15')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLEa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(3000)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Sleep(4000)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE2_W', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x0121 offset: 0x22B44
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    SetEndhookFunction('ShowEquip', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    Sleep(533)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_3B(0x00, ParamInt(0x7533), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7557), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0122 offset: 0x22D20
@scena.Code('AniCvAttack')
def AniCvAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(233)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2841), ParamInt(0x2842), ParamInt(0), ParamInt(0))

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22E67',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.042), ParamFloat(1.17), ParamFloat(0), 4.216, -26.817, 19.116, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)

    def _loc_22E67(): pass

    label('loc_22E67')

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-4), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    Sleep(166)

    OP_AD(0x01, 0x01)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    Sleep(400)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0123 offset: 0x22F58
@scena.Code('AniCvAssaultAttack')
def AniCvAssaultAttack():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    SetEndhookFunction('AniAssaultEnd_endHook', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0#56w3#36w0[autoM0]', '0[autoB0]', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_231D7',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT02'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)

    def _loc_231D7(): pass

    label('loc_231D7')

    OP_3B(0x00, ParamInt(0x10F3), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    EffectSetRGBA(0xFFFE, 0x06, 1.0, 1.0, 1.0, 0.0, 800, 0x03)
    Sleep(566)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2844), ParamInt(0x2845), ParamInt(0), ParamInt(0))
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_232D5',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_232D5(): pass

    label('loc_232D5')

    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1044), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(233)

    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_41(0xFFFE, 0x01)
    Call(ScriptId.Current, 'SpringOn')
    EffectCmd(0x0F, 0xFFFE, 0x0026, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0025, 0x01)

    Return()

# id: 0x0124 offset: 0x23438
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)

    Return()

# id: 0x0125 offset: 0x23580
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_235A5',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_235A5(): pass

    label('loc_235A5')

    Return()

# id: 0x0126 offset: 0x235A8
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2360A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_2360A(): pass

    label('loc_2360A')

    Return()

# id: 0x0127 offset: 0x2360C
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_236A6',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_23789')

    def _loc_236A6(): pass

    label('loc_236A6')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2853), ParamInt(0x2854), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_23789(): pass

    label('loc_23789')

    Return()

# id: 0x0128 offset: 0x2378C
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2855), ParamInt(0x2856), ParamInt(0), ParamInt(0))
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_CENTER'), ParamInt(0), ParamInt(0), ParamInt(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Sleep(500)

    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x03)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0129 offset: 0x23938
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_3B(0x32, ParamInt(0x2871), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', '4[autoM4]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '0#96w3', 'C', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x012A offset: 0x23A80
@scena.AnimeClips('_OnCostumeIn2_2')
def _OnCostumeIn2_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002871,
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

# id: 0x012B offset: 0x23B30
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002892,
            name   = '',
        ),
    )

# id: 0x012C offset: 0x23BB0
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283E,
            name   = '',
        ),
    )

# id: 0x012D offset: 0x23C60
@scena.AnimeClips('_AniEquipEQU092_R')
def _AniEquipEQU092_R():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU092_R',
        ),
    )

# id: 0x012E offset: 0x23CC0
@scena.AnimeClips('_AniEquipEQU092_L')
def _AniEquipEQU092_L():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU092_L',
        ),
    )

# id: 0x012F offset: 0x23D20
@scena.AnimeClips('_AniWait_Test1')
def _AniWait_Test1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0130 offset: 0x23D80
@scena.AnimeClips('_AniBtlWait_Test1')
def _AniBtlWait_Test1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0131 offset: 0x23DE0
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

# id: 0x0132 offset: 0x24070
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

# id: 0x0133 offset: 0x24140
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

# id: 0x0134 offset: 0x241C0
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

# id: 0x0135 offset: 0x24240
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

# id: 0x0136 offset: 0x242A0
@scena.AnimeClips('_AniDamage')
def _AniDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0137 offset: 0x24300
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

# id: 0x0138 offset: 0x243D0
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

# id: 0x0139 offset: 0x244D0
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

# id: 0x013A offset: 0x24530
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

# id: 0x013B offset: 0x24590
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002892,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002893,
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
            name   = 'IDLE2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2_W',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x013C offset: 0x24700
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
            dword4 = 0x00002841,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x013D offset: 0x24820
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
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002843,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
    )

# id: 0x013E offset: 0x248F0
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002844,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002845,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001044,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x013F offset: 0x24A60
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
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0140 offset: 0x24B10
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
            dword4 = 0x00007536,
            name   = '',
        ),
    )

# id: 0x0141 offset: 0x24B90
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

# id: 0x0142 offset: 0x24BF0
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

# id: 0x0143 offset: 0x24C50
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

# id: 0x0144 offset: 0x24CB0
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

# id: 0x0145 offset: 0x24D10
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

# id: 0x0146 offset: 0x24D70
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

# id: 0x0147 offset: 0x24DD0
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

# id: 0x0148 offset: 0x24E30
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

# id: 0x0149 offset: 0x24E90
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

# id: 0x014A offset: 0x24F10
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

# id: 0x014B offset: 0x24F90
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

# id: 0x014C offset: 0x24FF0
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

# id: 0x014D offset: 0x25050
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

# id: 0x014E offset: 0x250B0
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

# id: 0x014F offset: 0x25130
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

# id: 0x0150 offset: 0x251B0
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

# id: 0x0151 offset: 0x25230
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

# id: 0x0152 offset: 0x25290
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

# id: 0x0153 offset: 0x252F0
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

# id: 0x0154 offset: 0x25350
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
    )

# id: 0x0155 offset: 0x253B0
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028AA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002866,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002865,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002868,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002863,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002864,
            name   = '',
        ),
    )

# id: 0x0156 offset: 0x254D0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002840,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283E,
            name   = '',
        ),
    )

# id: 0x0157 offset: 0x255D0
@scena.AnimeClips('_AniBtlKisinReady')
def _AniBtlKisinReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002840,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000283E,
            name   = '',
        ),
    )

# id: 0x0158 offset: 0x256D0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002867,
            name   = '',
        ),
    )

# id: 0x0159 offset: 0x25730
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

# id: 0x015A offset: 0x257B0
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

# id: 0x015B offset: 0x25830
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
            dword4 = 0x00002841,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002843,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
    )

# id: 0x015C offset: 0x25930
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000285B,
            name   = '',
        ),
    )

# id: 0x015D offset: 0x25990
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

# id: 0x015E offset: 0x25A10
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002859,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002857,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002858,
            name   = '',
        ),
    )

# id: 0x015F offset: 0x25AC0
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002859,
            name   = '',
        ),
    )

# id: 0x0160 offset: 0x25B20
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

# id: 0x0161 offset: 0x25BD0
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

# id: 0x0162 offset: 0x25C30
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
            dword4 = 0x000028AD,
            name   = '',
        ),
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000285A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0163 offset: 0x25D50
@scena.AnimeClips('_AniBtlArts')
def _AniBtlArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002855,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002856,
            name   = '',
        ),
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0164 offset: 0x25E50
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
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002843,
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

# id: 0x0165 offset: 0x25F50
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002860,
            name   = '',
        ),
    )

# id: 0x0166 offset: 0x25FB0
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002861,
            name   = '',
        ),
    )

# id: 0x0167 offset: 0x26010
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002862,
            name   = '',
        ),
    )

# id: 0x0168 offset: 0x26070
@scena.AnimeClips('_AniBtlBluffVoice')
def _AniBtlBluffVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028AC,
            name   = '',
        ),
    )

# id: 0x0169 offset: 0x260D0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002872,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002873,
            name   = '',
        ),
    )

# id: 0x016A offset: 0x26150
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
            dword4 = 0x00002881,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002883,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002881,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002883,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002882,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002883,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
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

# id: 0x016B offset: 0x263E0
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

# id: 0x016C offset: 0x26440
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

# id: 0x016D offset: 0x264A0
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
            dword4 = 0x000028BA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
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

# id: 0x016E offset: 0x26610
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
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionup.eff',
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
            dword4 = 0x00008F72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028AB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB0,
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
            dword4 = 0x00008F00,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F21,
            name   = '',
        ),
    )

# id: 0x016F offset: 0x267B0
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
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

# id: 0x0170 offset: 0x26830
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002852,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002851,
            name   = '',
        ),
    )

# id: 0x0171 offset: 0x268B0
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

# id: 0x0172 offset: 0x26910
@scena.AnimeClips('_AniBtlCharge')
def _AniBtlCharge():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0173 offset: 0x269C0
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

# id: 0x0174 offset: 0x26A20
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

# id: 0x0175 offset: 0x26A80
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

# id: 0x0176 offset: 0x26AE0
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000286B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002869,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000286A,
            name   = '',
        ),
    )

# id: 0x0177 offset: 0x26B90
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
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0178 offset: 0x26C60
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
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0179 offset: 0x26D30
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
            dword4 = 0x00002870,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x017A offset: 0x26E30
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

# id: 0x017B offset: 0x26E90
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
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x017C offset: 0x26F40
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002871,
            name   = '',
        ),
    )

# id: 0x017D offset: 0x26FA0
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002871,
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

# id: 0x017E offset: 0x27050
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002846,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F73,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001057,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002847,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_05',
        ),
    )

# id: 0x017F offset: 0x27300
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002846,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F73,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010D6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001057,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002848,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010D3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_05',
        ),
    )

# id: 0x0180 offset: 0x27590
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002846,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F73,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000104A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001057,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002849,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001044,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_05',
        ),
    )

# id: 0x0181 offset: 0x27820
@scena.AnimeClips('_AniBtlCraft03')
def _AniBtlCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_03_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284A,
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
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001057,
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
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB7,
            name   = '',
        ),
    )

# id: 0x0182 offset: 0x27CE0
@scena.AnimeClips('_AniBtlCraft04')
def _AniBtlCraft04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
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
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001043,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0183 offset: 0x281F0
@scena.AnimeClips('_AniBtlCraft05')
def _AniBtlCraft05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_06_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_06_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_06_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FC2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
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
            dword4 = 0x00008F41,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F66,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
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
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0184 offset: 0x28540
@scena.AnimeClips('_AniBtlCOMBI')
def _AniBtlCOMBI():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/rushback2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_05_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_05_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_6.eff',
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
            name   = 'BTL_S_CRAFT01_14',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010A7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_03_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001057,
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
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
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

# id: 0x0185 offset: 0x28B90
@scena.AnimeClips('_AniBtlTRIO')
def _AniBtlTRIO():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/rushback2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_05_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_05_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_05_0.eff',
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
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_01_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
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
            dword4 = 0x00007537,
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
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02',
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
            dword4 = 0x00001093,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF080,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr003_25_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
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
            type   = 0x0009,
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F47,
            name   = '',
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
            dword4 = 0x00008F75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2A,
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
            type2  = 0xF081,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr035_04_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
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
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001043,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0186 offset: 0x29610
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B8A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001012,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000104F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010D7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_06',
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
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001034,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001034,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_12',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001034,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B87,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B8A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
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
            dword4 = 0x000010F8,
            name   = '',
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
            dword4 = 0x00001066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F0,
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
            type2  = 0x0B88,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B89,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B8A,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000013F0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_14',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000284E,
            name   = '',
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
            name   = 'BTL_S_CRAFT01_15',
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
            dword4 = 0x000010F0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002850,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_15',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001074,
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
            dword4 = 0x00000FC7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0187 offset: 0x2A250
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

# id: 0x0188 offset: 0x2A2B0
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

# id: 0x0189 offset: 0x2A310
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

# id: 0x018A offset: 0x2A370
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

# id: 0x018B offset: 0x2A3D0
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

# id: 0x018C offset: 0x2A430
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

# id: 0x018D offset: 0x2A530
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

# id: 0x018E offset: 0x2A5B0
@scena.AnimeClips('_AniEvIdle2')
def _AniEvIdle2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2a',
        ),
    )

# id: 0x018F offset: 0x2A630
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
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0190 offset: 0x2A6E0
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

# id: 0x0191 offset: 0x2A740
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

# id: 0x0192 offset: 0x2A7A0
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

# id: 0x0193 offset: 0x2A800
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

# id: 0x0194 offset: 0x2A860
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

# id: 0x0195 offset: 0x2A8E0
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

# id: 0x0196 offset: 0x2A960
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

# id: 0x0197 offset: 0x2A9C0
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

# id: 0x0198 offset: 0x2AA40
@scena.AnimeClips('_AniEvPowerUp')
def _AniEvPowerUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa',
        ),
    )

# id: 0x0199 offset: 0x2AAC0
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

# id: 0x019A offset: 0x2AB40
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

# id: 0x019B offset: 0x2ABA0
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

# id: 0x019C offset: 0x2AC20
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

# id: 0x019D offset: 0x2ACA0
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

# id: 0x019E offset: 0x2AD00
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

# id: 0x019F offset: 0x2AD80
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

# id: 0x01A0 offset: 0x2AE00
@scena.AnimeClips('_AniEvOrder')
def _AniEvOrder():
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A1 offset: 0x2AE80
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

# id: 0x01A2 offset: 0x2AF00
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

# id: 0x01A3 offset: 0x2AF60
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

# id: 0x01A4 offset: 0x2AFE0
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
            name   = 'BTL_CRAFT00_02',
        ),
    )

# id: 0x01A5 offset: 0x2B060
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
            name   = 'BTL_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A6 offset: 0x2B130
@scena.AnimeClips('_AniEvCraft00_03b')
def _AniEvCraft00_03b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
    )

# id: 0x01A7 offset: 0x2B190
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A8 offset: 0x2B210
@scena.AnimeClips('_AniEvSCraft01_01')
def _AniEvSCraft01_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
        ),
    )

# id: 0x01A9 offset: 0x2B270
@scena.AnimeClips('_AniEvSCraft01_02')
def _AniEvSCraft01_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AA offset: 0x2B320
@scena.AnimeClips('_AniEvSCraft01_04')
def _AniEvSCraft01_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
    )

# id: 0x01AB offset: 0x2B380
@scena.AnimeClips('_AniEvSCraft01_05')
def _AniEvSCraft01_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_07',
        ),
    )

# id: 0x01AC offset: 0x2B430
@scena.AnimeClips('_AniEvSCraft01_07')
def _AniEvSCraft01_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_07',
        ),
    )

# id: 0x01AD offset: 0x2B490
@scena.AnimeClips('_AniEvSCraft01_08')
def _AniEvSCraft01_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
    )

# id: 0x01AE offset: 0x2B4F0
@scena.AnimeClips('_AniEvSCraft01_09')
def _AniEvSCraft01_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_09',
        ),
    )

# id: 0x01AF offset: 0x2B550
@scena.AnimeClips('_AniEvSCraft01_10')
def _AniEvSCraft01_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_11',
        ),
    )

# id: 0x01B0 offset: 0x2B5D0
@scena.AnimeClips('_AniEvSCraft01_12')
def _AniEvSCraft01_12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_12',
        ),
    )

# id: 0x01B1 offset: 0x2B630
@scena.AnimeClips('_AniEvSCraft01_13')
def _AniEvSCraft01_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_15',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_14',
        ),
    )

# id: 0x01B2 offset: 0x2B6E0
@scena.AnimeClips('_AniEvSCraft01_14')
def _AniEvSCraft01_14():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_14',
        ),
    )

# id: 0x01B3 offset: 0x2B740
@scena.AnimeClips('_AniEvSCraft01_17')
def _AniEvSCraft01_17():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_17',
        ),
    )

# id: 0x01B4 offset: 0x2B7A0
@scena.AnimeClips('_AniEvKamiharai')
def _AniEvKamiharai():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_KAMIHARAI',
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

# id: 0x01B5 offset: 0x2B850
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

# id: 0x01B6 offset: 0x2B900
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

# id: 0x01B7 offset: 0x2B9B0
@scena.AnimeClips('_AniEvTeKosi')
def _AniEvTeKosi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSIa_U',
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
            name   = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSIb_U',
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
            name   = 'EV_TEKOSIb',
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
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSIa',
        ),
    )

# id: 0x01B8 offset: 0x2BC40
@scena.AnimeClips('_AniEvTeKosiTeburi')
def _AniEvTeKosiTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSI_t_U',
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
            name   = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_TEKOSIa',
        ),
    )

# id: 0x01B9 offset: 0x2BD40
@scena.AnimeClips('_AniEvHookaki')
def _AniEvHookaki():
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
            name   = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01BA offset: 0x2BDF0
@scena.AnimeClips('_AniEv02005')
def _AniEv02005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02005',
        ),
    )

# id: 0x01BB offset: 0x2BE50
@scena.AnimeClips('_AniEv02005b')
def _AniEv02005b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02005b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02005c',
        ),
    )

# id: 0x01BC offset: 0x2BED0
@scena.AnimeClips('_AniEv02010')
def _AniEv02010():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev02010',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev02010a',
        ),
    )

# id: 0x01BD offset: 0x2BF50
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

# id: 0x01BE offset: 0x2BFD0
@scena.AnimeClips('_AniEv03001')
def _AniEv03001():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03001',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01BF offset: 0x2C050
@scena.AnimeClips('_AniEv03540')
def _AniEv03540():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03540',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03540a',
        ),
    )

# id: 0x01C0 offset: 0x2C0D0
@scena.AnimeClips('_AniEv03540a')
def _AniEv03540a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV03540a',
        ),
    )

# id: 0x01C1 offset: 0x2C130
@scena.AnimeClips('_AniEv30005')
def _AniEv30005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30005',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30005a',
        ),
    )

# id: 0x01C2 offset: 0x2C1B0
@scena.AnimeClips('_AniEv34505')
def _AniEv34505():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34505',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34505a',
        ),
    )

# id: 0x01C3 offset: 0x2C230
@scena.AnimeClips('_AniEv34540')
def _AniEv34540():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34540',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01C4 offset: 0x2C2B0
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
            dword4 = 0x00007533,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007557,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01C5 offset: 0x2C380
@scena.AnimeClips('_AniEv35000b')
def _AniEv35000b():
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
            dword4 = 0x00007557,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01C6 offset: 0x2C430
@scena.AnimeClips('_AniEv37000')
def _AniEv37000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV37000',
        ),
    )

# id: 0x01C7 offset: 0x2C490
@scena.AnimeClips('_AniAttachE07EVT02C')
def _AniAttachE07EVT02C():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'O_E07EVT02D',
        ),
    )

# id: 0x01C8 offset: 0x2C4F0
@scena.AnimeClips('_AniEv52650')
def _AniEv52650():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV52650',
        ),
    )

# id: 0x01C9 offset: 0x2C550
@scena.AnimeClips('_AniAttachEQU962')
def _AniAttachEQU962():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU962',
        ),
    )

# id: 0x01CA offset: 0x2C5B0
@scena.AnimeClips('_AniEv54575')
def _AniEv54575():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV54575',
        ),
    )

# id: 0x01CB offset: 0x2C610
@scena.AnimeClips('_AniEv70001_7')
def _AniEv70001_7():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70001_7',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70001_7a',
        ),
    )

# id: 0x01CC offset: 0x2C690
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

# id: 0x01CD offset: 0x2C6F0
@scena.AnimeClips('_AniEv76050')
def _AniEv76050():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV76050',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV76050a',
        ),
    )

# id: 0x01CE offset: 0x2C770
@scena.AnimeClips('_AniEv79321')
def _AniEv79321():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79321',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79321a',
        ),
    )

# id: 0x01CF offset: 0x2C7F0
@scena.AnimeClips('_AniEv79321a')
def _AniEv79321a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79321a',
        ),
    )

# id: 0x01D0 offset: 0x2C850
@scena.AnimeClips('_AniEv79322')
def _AniEv79322():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79322',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79322a',
        ),
    )

# id: 0x01D1 offset: 0x2C8D0
@scena.AnimeClips('_AniEv79323')
def _AniEv79323():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79323',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79323a',
        ),
    )

# id: 0x01D2 offset: 0x2C950
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

# id: 0x01D3 offset: 0x2C9B0
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

# id: 0x01D4 offset: 0x2CA10
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

# id: 0x01D5 offset: 0x2CA70
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk035_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk035_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk035_a0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk035_a1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk035_a2.eff',
        ),
    )

# id: 0x01D6 offset: 0x2CB70
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

# id: 0x01D7 offset: 0x2CBD0
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002892,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002893,
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
            name   = 'IDLE2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE2_W',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01D8 offset: 0x2CD40
@scena.AnimeClips('_AniCvBtlWait')
def _AniCvBtlWait():
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
            dword4 = 0x00007533,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007557,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01D9 offset: 0x2CE10
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
            dword4 = 0x00002841,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002842,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DA offset: 0x2CF10
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002844,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002845,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001044,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DB offset: 0x2D080
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
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01DC offset: 0x2D130
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
            dword4 = 0x00002853,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002854,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x01DD offset: 0x2D230
@scena.AnimeClips('_AniCvArts')
def _AniCvArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002855,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002856,
            name   = '',
        ),
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01DE offset: 0x2D330
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002871,
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
