import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr019_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr019.dat')

# id: 0x0000 offset: 0x22FC
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'FATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'FATTACK2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR019_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_GUARD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_V_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_ORDER',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_CRAFT00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_CRAFT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR019_BT1',
            symbol     = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR019_SC1',
            symbol     = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR019_SC1',
            symbol     = 'BTL_S_CRAFT01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR019_SC1',
            symbol     = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR019_SC1',
            symbol     = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR019_SC1',
            symbol     = 'BTL_S_CRAFT01_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_STOP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'HORSE_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_WAIT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_TILT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_TILT_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_TILT_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_BACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_BACK_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_BACK_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_HANDLE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000004,
            asset      = 'C_CHR019_HS1',
            symbol     = 'BIKE_HANDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR019_BT3',
            symbol     = 'BTL_WIN_KNUCKLE_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR019_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR019_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000400,
            asset      = 'C_CHR019_BT3',
            symbol     = 'BTL_WIN_BACKKNUCKLE_R2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'BTL_DEAD1_B',
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
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_MAEKAGAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_MAEKAGAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            symbol     = 'EV_MUKKII',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_OP51_HAGU',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_YARUKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_YARUKI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
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
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev02050',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev40050',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev40055',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev40055a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45010a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45015',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45020',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45020a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV45085',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev45090',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53550',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53550w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53555',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53555a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53560',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53561',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'ev53561a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV70120',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV7',
            symbol     = 'EV70125',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV74195',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'EV74310',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79290',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79290a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79291',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79291a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79292',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79292a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79293',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79293a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79294',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79294a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79295',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79295a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79296',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR019_EV',
            symbol     = 'Ev79296a',
        ),
    )

# id: 0x0001 offset: 0xADF0
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xAE10
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xAE28
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "ModelCmd(0x3F)"),
            Expr.Return,
        ),
        'loc_AE3A',
    )

    Return()

    def _loc_AE3A(): pass

    label('loc_AE3A')

    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE4C',
    )

    def _loc_AE4C(): pass

    label('loc_AE4C')

    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')

    Return()

# id: 0x0004 offset: 0xAE88
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0005 offset: 0xAEB0
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0006 offset: 0xAEDC
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0007 offset: 0xAEE8
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0008 offset: 0xAEF8
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0009 offset: 0xAF08
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000400)

    Return()

# id: 0x000A offset: 0xAF18
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000B offset: 0xAF28
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000C offset: 0xAF38
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000D offset: 0xAF48
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000E offset: 0xAF60
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000400)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000F offset: 0xAF78
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0010 offset: 0xAF90
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xAFA8
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU072_R')
    AttachEquip(0xFFFE, 'C_EQU072_R', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    LoadAsset('C_EQU072_L')
    AttachEquip(0xFFFE, 'C_EQU072_L', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    LoadAsset('C_EQU072_R2')
    AttachEquip(0xFFFE, 'C_EQU072_R2', 'R_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x01)
    LoadAsset('C_EQU072_L2')
    AttachEquip(0xFFFE, 'C_EQU072_L2', 'L_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x01)

    Return()

# id: 0x0012 offset: 0xB184
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'R_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    DeatchEquip(0xFFFE, 'L_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU072_R')
    ReleaseAsset('C_EQU072_L')
    ReleaseAsset('C_EQU072_R2')
    ReleaseAsset('C_EQU072_L2')

    Return()

# id: 0x0013 offset: 0xB2BC
@scena.Code('AniReset')
def AniReset():
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0014 offset: 0xB32C
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BH_03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Stoll02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Stoll03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftChest', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightChest', 0.2)

    Return()

# id: 0x0015 offset: 0xB3D0
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BH_03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Stoll02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Stoll03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftChest', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightChest', 0.2)

    Return()

# id: 0x0016 offset: 0xB474
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0017 offset: 0xB478
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0018 offset: 0xB488
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

# id: 0x0019 offset: 0xB498
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x001A offset: 0xB4C4
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_B4DE',
    )

    Jump('loc_B51F')

    def _loc_B4DE(): pass

    label('loc_B4DE')

    Call(ScriptId.BtlCom, 'LoadOnHorse')
    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_B51F(): pass

    label('loc_B51F')

    Return()

# id: 0x001B offset: 0xB520
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x001C offset: 0xB52C
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

# id: 0x001D offset: 0xB594
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

# id: 0x001E offset: 0xB60C
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
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniIdle', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x001F offset: 0xB66C
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

    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'OnCostumeIn3_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x0020 offset: 0xB6F0
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '4', '', '#b', '0')
    Sleep(200)

    OP_3B(0x32, ParamInt(0x1D78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '3', '5554', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '4', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM4]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0021 offset: 0xB848
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

    OP_3B(0x3A, 0xFFFE, ParamInt(7500), ParamInt(0x1D4D), ParamInt(0x1D4E), ParamInt(0))

    Return()

# id: 0x0022 offset: 0xB884
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x01)

    Return()

# id: 0x0023 offset: 0xB8E8
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x00)

    Return()

# id: 0x0024 offset: 0xB94C
@scena.Code('AniAttachEQU072')
def AniAttachEQU072():
    LoadAsset('C_EQU072_R')
    AttachEquip(0xFFFE, 'C_EQU072_R', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU072_R2')
    AttachEquip(0xFFFE, 'C_EQU072_R2', 'R_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_forearm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU072_L')
    AttachEquip(0xFFFE, 'C_EQU072_L', 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    LoadAsset('C_EQU072_L2')
    AttachEquip(0xFFFE, 'C_EQU072_L2', 'L_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x01)
    OP_76(PseudoChrId.Self, 'L_forearm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0025 offset: 0xBBC4
@scena.Code('AniDetachEQU072')
def AniDetachEQU072():
    ReleaseAsset('C_EQU072_R')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU072_R2')
    DeatchEquip(0xFFFE, 'R_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU072_L')
    DeatchEquip(0xFFFE, 'L_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU072_L2')
    DeatchEquip(0xFFFE, 'L_forearm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x0026 offset: 0xBCFC
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320_C04')
    AttachEquip(0xFFFE, 'C_EQU320_C04', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0027 offset: 0xBD70
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320_C04')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x0028 offset: 0xBDC0
@scena.Code('AniEv02050')
def AniEv02050():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev02050', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0029 offset: 0xBE14
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x002A offset: 0xBE5C
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x002B offset: 0xBE60
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x002C offset: 0xBE64
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002D offset: 0xBE9C
@scena.Code('AniHorseRun')
def AniHorseRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002E offset: 0xBED4
@scena.Code('AniHorseDash')
def AniHorseDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002F offset: 0xBF0C
@scena.Code('AniHorseStop')
def AniHorseStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0030 offset: 0xBF44
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0031 offset: 0xBFA0
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0032 offset: 0xBFFC
@scena.Code('AniBikeWait')
def AniBikeWait():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C057',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_C057(): pass

    label('loc_C057')

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xC09C
@scena.Code('AniBikeWaitLeft')
def AniBikeWaitLeft():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x0034 offset: 0xC0F4
@scena.Code('AniBikeRun')
def AniBikeRun():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x0035 offset: 0xC148
@scena.Code('AniBikeTilt')
def AniBikeTilt():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x0036 offset: 0xC19C
@scena.Code('AniBikeTiltR')
def AniBikeTiltR():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x0037 offset: 0xC1F4
@scena.Code('AniBikeTiltL')
def AniBikeTiltL():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x0038 offset: 0xC24C
@scena.Code('AniBikeBack')
def AniBikeBack():
    Call(ScriptId.Current, 'SpringOff')

    ExecExpressionWithReg(
        0x07,
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

# id: 0x0039 offset: 0xC2DC
@scena.Code('AniBikeHandleWait')
def AniBikeHandleWait():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x003A offset: 0xC338
@scena.Code('AniBikeHandle')
def AniBikeHandle():
    ExecExpressionWithReg(
        0x07,
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

# id: 0x003B offset: 0xC390
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x003C offset: 0xC394
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
        'loc_C45F',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C413',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C456')

    def _loc_C413(): pass

    label('loc_C413')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C456',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C456(): pass

    label('loc_C456')

    Jump('loc_C4ED')

    def _loc_C45F(): pass

    label('loc_C45F')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_C4AA',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C4ED')

    def _loc_C4AA(): pass

    label('loc_C4AA')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C4ED',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C4ED(): pass

    label('loc_C4ED')

    OP_3F(PseudoChrId.Self, 0x00000000)
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x003D offset: 0xC50C
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
        'loc_C56A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C653')

    def _loc_C56A(): pass

    label('loc_C56A')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_C5F5',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_C653')

    def _loc_C5F5(): pass

    label('loc_C5F5')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C653(): pass

    label('loc_C653')

    Return()

# id: 0x003E offset: 0xC654
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003F offset: 0xC690
@scena.Code('AniLand')
def AniLand():
    OP_80(0.05)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_C6E2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, 108.333, -1.0, 0x00, 0x00)

    Jump('loc_C705')

    def _loc_C6E2(): pass

    label('loc_C6E2')

    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C705(): pass

    label('loc_C705')

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

    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniWait', 0.3, 1.0, 0x00000000)

    Return()

# id: 0x0040 offset: 0xC748
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7F8',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C7CB',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_C7EF')

    def _loc_C7CB(): pass

    label('loc_C7CB')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C7EF(): pass

    label('loc_C7EF')

    Jump('loc_CC3F')

    def _loc_C7F8(): pass

    label('loc_C7F8')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_CA0E',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8B5',
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
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CA05')

    def _loc_C8B5(): pass

    label('loc_C8B5')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C94F',
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
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CA05')

    def _loc_C94F(): pass

    label('loc_C94F')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C9DE',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.3)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 40.1667, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CA05')

    def _loc_C9DE(): pass

    label('loc_C9DE')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_CA05(): pass

    label('loc_CA05')

    Jump('loc_CC3F')

    def _loc_CA0E(): pass

    label('loc_CA0E')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_CA6A',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_CC3F')

    def _loc_CA6A(): pass

    label('loc_CA6A')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB03',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CC3F')

    def _loc_CB03(): pass

    label('loc_CB03')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB95',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CC3F')

    def _loc_CB95(): pass

    label('loc_CB95')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC13',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_CC3F')

    def _loc_CC13(): pass

    label('loc_CC13')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_CC3F(): pass

    label('loc_CC3F')

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

# id: 0x0041 offset: 0xCC68
@scena.Code('AniWalk')
def AniWalk():
    Call(ScriptId.Current, 'ResetModel1')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_CD20',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CCF0',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_CCF0(): pass

    label('loc_CCF0')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CD97')

    def _loc_CD20(): pass

    label('loc_CD20')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CD74',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_CD74(): pass

    label('loc_CD74')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CD97(): pass

    label('loc_CD97')

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

# id: 0x0042 offset: 0xCDC8
@scena.Code('AniRun')
def AniRun():
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
        'loc_CE2B',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CE4D')

    def _loc_CE2B(): pass

    label('loc_CE2B')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CE4D(): pass

    label('loc_CE4D')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE6C',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CE6C(): pass

    label('loc_CE6C')

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

# id: 0x0043 offset: 0xCE90
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
        'loc_CEF3',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CF16')

    def _loc_CEF3(): pass

    label('loc_CEF3')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CF16(): pass

    label('loc_CF16')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CF35',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_CF35(): pass

    label('loc_CF35')

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

# id: 0x0044 offset: 0xCF58
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

# id: 0x0045 offset: 0xCFB4
@scena.Code('AniDamage')
def AniDamage():
    OP_3B(0x32, ParamInt(0x1D63), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'B', '3', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0046 offset: 0xD064
@scena.Code('AniIdle')
def AniIdle():
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
        'loc_D0EC',
    )

    OP_3B(0x32, ParamInt(0x1D98), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D141')

    def _loc_D0EC(): pass

    label('loc_D0EC')

    OP_3B(0x32, ParamInt(0x1D99), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_D141(): pass

    label('loc_D141')

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '1', '', '', '#b', '0')
    Sleep(1333)

    Call(ScriptId.Current, 'DefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0047 offset: 0xD1D4
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk019.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_D24D',
    )

    LoadEffect(0xFFFE, 0x23, 'battle/atk019_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk019_a1.eff', 0x00000000)

    def _loc_D24D(): pass

    label('loc_D24D')

    Return()

# id: 0x0048 offset: 0xD250
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)

    Return()

# id: 0x0049 offset: 0xD26C
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

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DC9), ParamInt(0x1DCA), ParamInt(0), ParamInt(0))
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.04), ParamFloat(0.06), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    Sleep(166)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x004A offset: 0xD44C
@scena.Code('AniFieldAttack2')
def AniFieldAttack2():
    OP_80(0.05)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK2', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DCA), ParamInt(0x1DCB), ParamInt(0), ParamInt(0))
    Sleep(66)

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.15), ParamFloat(0.05), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(500)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x004B offset: 0xD5D8
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

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    SetChrFace(0x03, PseudoChrId.Self, '3', '6[autoM6]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 76.6667, 77.0667, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D54), ParamInt(0x1D55), ParamInt(0), ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 77.1, 78.6667, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FE6), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(5)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0.75), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1059), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, ParamInt(0x1059), ParamInt(1500), 0xFFFF)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    Sleep(666)

    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    OP_41(0xFFFE, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.3, 6.66667, 6.66667, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0xD988
@scena.Code('AniFieldAttackEnd')
def AniFieldAttackEnd():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    Sleep(266)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('EraseEquip', 0x000B)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x004D offset: 0xDB3C
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x004E offset: 0xDBC4
@scena.Code('AniFieldAttackEndShort')
def AniFieldAttackEndShort():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    Sleep(300)

    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x004F offset: 0xDCFC
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0050 offset: 0xDD40
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0051 offset: 0xDD78
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0052 offset: 0xDDA4
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0053 offset: 0xDDBC
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)

    If(
        (
            (Expr.Eval, "BattleCmd(0x9E, 0xFFFE, 'chr019_c70_i')"),
            Expr.Return,
        ),
        'loc_DEA4',
    )

    LoadAsset('C_EQU172')
    AttachEquip(0xFFFE, 'C_EQU172', 'head_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'head_point', 0x01)
    OP_76(PseudoChrId.Self, 'head_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_DEA4(): pass

    label('loc_DEA4')

    Return()

# id: 0x0054 offset: 0xDEA8
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0055 offset: 0xDEC0
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DF36',
    )

    OP_3B(0x32, ParamInt(0x1D72), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E10A')

    def _loc_DF36(): pass

    label('loc_DF36')

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
        'loc_DFCA',
    )

    OP_3B(0x32, ParamInt(0x1D71), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E10A')

    def _loc_DFCA(): pass

    label('loc_DFCA')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E040',
    )

    OP_3B(0x32, ParamInt(0x1D74), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E10A')

    def _loc_E040(): pass

    label('loc_E040')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E0B5',
    )

    OP_3B(0x32, ParamInt(0x1D6F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E10A')

    def _loc_E0B5(): pass

    label('loc_E0B5')

    OP_3B(0x32, ParamInt(0x1D70), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E10A(): pass

    label('loc_E10A')

    Return()

# id: 0x0056 offset: 0xE10C
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_E149',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D4F), ParamInt(0x1D50), ParamInt(0), ParamInt(0))

    Jump('loc_E169')

    def _loc_E149(): pass

    label('loc_E149')

    OP_3B(0x3A, 0xFFFE, ParamInt(7500), ParamInt(0x1D4D), ParamInt(0x1D4E), ParamInt(0))

    def _loc_E169(): pass

    label('loc_E169')

    Return()

# id: 0x0057 offset: 0xE16C
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x1D73), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0058 offset: 0xE1C4
@scena.Code('AniBtlWait')
def AniBtlWait():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0059 offset: 0xE204
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x005A offset: 0xE240
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E28C',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E2CF')

    def _loc_E28C(): pass

    label('loc_E28C')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E2CF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E2CF(): pass

    label('loc_E2CF')

    Return()

# id: 0x005B offset: 0xE2D0
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x1D6B))

    Return()

# id: 0x005C offset: 0xE2EC
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x1D6A))

    Return()

# id: 0x005D offset: 0xE308
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.08), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E4D2',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D51), ParamInt(0x1D52), ParamInt(0x1D53), ParamInt(0))

    def _loc_E4D2(): pass

    label('loc_E4D2')

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_E5A4',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.3, 0.3, 0.2)

    def _loc_E5A4(): pass

    label('loc_E5A4')

    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.09), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E6DD',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DC9), ParamInt(0x1DCA), ParamInt(0x1DCB), ParamInt(0))

    def _loc_E6DD(): pass

    label('loc_E6DD')

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    CameraCmd(0x09, 0.02, 0.02, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_E7CD',
    )

    OP_3B(0xFF, 0.0, 0.0, 0.0)
    Sleep(0)

    OP_3B(0xFF, 0.6, 0.6, 0.1)

    def _loc_E7CD(): pass

    label('loc_E7CD')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'AniBtlWait')
    Sleep(230)

    Return()

# id: 0x005E offset: 0xE7F4
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, ParamInt(0x1D67), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x005F offset: 0xE860
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
        'loc_E8C1',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E8EA')

    def _loc_E8C1(): pass

    label('loc_E8C1')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E8EA(): pass

    label('loc_E8EA')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0xE8F8
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D63), ParamInt(0x1D64), ParamInt(0x1D65), ParamInt(0))

    Return()

# id: 0x0061 offset: 0xE91C
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    Return()

# id: 0x0062 offset: 0xE920
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
        'loc_E982',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_E9E6')

    def _loc_E982(): pass

    label('loc_E982')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E9E6(): pass

    label('loc_E9E6')

    Return()

# id: 0x0063 offset: 0xE9E8
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0064 offset: 0xEA24
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')

    Return()

# id: 0x0065 offset: 0xEA3C
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_EAF0',
    )

    OP_3B(0x32, ParamInt(0x1D66), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x1D66))

    def _loc_EAF0(): pass

    label('loc_EAF0')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0066 offset: 0xEB28
@scena.Code('AniBtlAria')
def AniBtlAria():
    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x1D5F), ParamInt(0x1D60), ParamFloat(-1), ParamFloat(0))

    Return()

# id: 0x0067 offset: 0xEB54
@scena.Code('AniBtlArts')
def AniBtlArts():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x4B, 0x00FA, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D61), ParamInt(0x1D62), ParamInt(0), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x0068 offset: 0xED48
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

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D61), ParamInt(0x1D62), ParamInt(0), ParamInt(0))
    Sleep(600)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x0069 offset: 0xEF18
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0))

    Return()

# id: 0x006A offset: 0xEF34
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    Call(ScriptId.BtlCom, 'AniBtlBluff', ParamInt(0x0001))

    Return()

# id: 0x006B offset: 0xEF50
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, ParamInt(0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Return()

# id: 0x006C offset: 0xEFCC
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x1D6C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x006D offset: 0xF024
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x1D6D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x006E offset: 0xF07C
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x1D6E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x006F offset: 0xF0D4
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D79), ParamInt(0x1D7A), ParamInt(0), ParamInt(0))

    Return()

# id: 0x0070 offset: 0xF0F8
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_F17E',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/damage02.eff', 0x00000000)

    def _loc_F17E(): pass

    label('loc_F17E')

    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F2E8',
    )

    OP_3B(0x32, ParamInt(0x1D8A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F519')

    def _loc_F2E8(): pass

    label('loc_F2E8')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F35F',
    )

    OP_3B(0x32, ParamInt(0x1D8A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F519')

    def _loc_F35F(): pass

    label('loc_F35F')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F3D6',
    )

    OP_3B(0x32, ParamInt(0x1D89), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F519')

    def _loc_F3D6(): pass

    label('loc_F3D6')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F44D',
    )

    OP_3B(0x32, ParamInt(0x1D8A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F519')

    def _loc_F44D(): pass

    label('loc_F44D')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F4C4',
    )

    OP_3B(0x32, ParamInt(0x1D89), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F519')

    def _loc_F4C4(): pass

    label('loc_F4C4')

    OP_3B(0x32, ParamInt(0x1D7B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_F519(): pass

    label('loc_F519')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.08), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(150)

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F73C',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x03E8)
    Sleep(100)

    Jump('loc_FBE8')

    def _loc_F73C(): pass

    label('loc_F73C')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F8FC',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.1), ParamFloat(1.1), ParamFloat(1.1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x07D0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1056), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FBE8')

    def _loc_F8FC(): pass

    label('loc_F8FC')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FA67',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.03, 0.03, 0.5)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x07D0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FBE8')

    def _loc_FA67(): pass

    label('loc_FA67')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FB7D',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x03E8)
    Sleep(100)

    Jump('loc_FBE8')

    def _loc_FB7D(): pass

    label('loc_FB7D')

    CameraCmd(0x09, 0.01, 0.01, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(200)

    def _loc_FBE8(): pass

    label('loc_FBE8')

    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.09), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(150)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FE10',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x07D0)

    Jump('loc_102A0')

    def _loc_FE10(): pass

    label('loc_FE10')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FFC9',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.1), ParamFloat(1.1), ParamFloat(1.1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1056), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x01, 0x07D0)

    Jump('loc_102A0')

    def _loc_FFC9(): pass

    label('loc_FFC9')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1012D',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.03, 0.03, 0.5)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F69), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x01, 0x07D0)

    Jump('loc_102A0')

    def _loc_1012D(): pass

    label('loc_1012D')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1023C',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_5E(0x00, 0x0002, 0.5, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    OP_5E(0x01, 0x07D0)

    Jump('loc_102A0')

    def _loc_1023C(): pass

    label('loc_1023C')

    CameraCmd(0x09, 0.01, 0.01, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_102A0(): pass

    label('loc_102A0')

    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(666)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)

    BattleCmd(0x3F, 0xFFFE)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x0071 offset: 0x1038C
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0072 offset: 0x103D0
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0073 offset: 0x103F8
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    Call(ScriptId.BtlCom, 'AniBtlBurstWait')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 100, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.5, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.08), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DBA), ParamInt(0x1DBC), ParamInt(0x1DBE), ParamInt(0))
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1066E(): pass

    label('loc_1066E')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_106FF',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1066E')

    def _loc_106FF(): pass

    label('loc_106FF')

    Sleep(200)

    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.09), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(50)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DBB), ParamInt(0x1DBD), ParamInt(0x1DBF), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    CameraCmd(0x09, 0.02, 0.02, 0.5)
    OP_3B(0x00, ParamInt(0x0FE7), ParamFloat(0.8), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_108B9(): pass

    label('loc_108B9')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1095D',
    )

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
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

    Jump('loc_108B9')

    def _loc_1095D(): pass

    label('loc_1095D')

    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0074 offset: 0x10A0C
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0075 offset: 0x10A24
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0076 offset: 0x10A3C
@scena.Code('AniBtlLinkUtmostAttack')
def AniBtlLinkUtmostAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0077 offset: 0x10A54
@scena.Code('AniBtlLinkCounter')
def AniBtlLinkCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0078 offset: 0x10A6C
@scena.Code('AniBtlLinkUltimateAttack')
def AniBtlLinkUltimateAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0079 offset: 0x10A84
@scena.Code('AniBtlLinkRageCounter')
def AniBtlLinkRageCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x007A offset: 0x10A9C
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x007B offset: 0x10ABC
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x007C offset: 0x10AD8
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    SetChrFace(0x03, PseudoChrId.Self, '777776', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ORDER', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x007D offset: 0x10B24
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_10B95',
    )

    OP_3B(0x32, ParamInt(0x1DCC), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10BEA')

    def _loc_10B95(): pass

    label('loc_10B95')

    OP_3B(0x32, ParamInt(0x1D5E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10BEA(): pass

    label('loc_10BEA')

    Return()

# id: 0x007E offset: 0x10BEC
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x007F offset: 0x10C30
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0080 offset: 0x10C48
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x0081 offset: 0x10C6C
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x0082 offset: 0x10C70
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    EffectSetRGBA(0xFFFE, 0x00, 1.0, 1.0, 1.0, 0.5, 0, 0x03)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_V_ARIA', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0083 offset: 0x10D6C
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x1D61), ParamInt(0x1D62))

    Return()

# id: 0x0084 offset: 0x10D98
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    PlayEffect(PseudoChrId.Self, ParamInt(0x082F), PseudoChrId.Self, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_V_ARIA', 0x00, 0x00, 0x00, 0x00, 0x00, 0.7, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '7', 'A[autoMA]', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0085 offset: 0x10E78
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    SetChrFace(0x03, PseudoChrId.Self, '7', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_V_ARIA', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0086 offset: 0x10EBC
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x0087 offset: 0x10EDC
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
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
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.15, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 15.0, 5.0, 0, 0x01)
    CameraSetDistance(0x03, 2.75, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.5, 0.0, 4000)
    CameraSetHeight(0x03, -1.05, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 11.0, -2.0, 5.0, 4000, 0x01)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.55, 103.333, 103.967, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.7, 0xFFFFFFFF)
    OP_3B(0x32, ParamInt(0x1D59), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2F3', '2[autoM2]', '0', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FAA), ParamFloat(0.7), ParamInt(800), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F38), ParamFloat(0.8), ParamInt(800), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x0A, 0.015, 0.015, 0.0, 500, 2000, 500, 0, 0, 0x00)
    Sleep(2000)

    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 104.267, 105.767, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    SetChrFace(0x03, PseudoChrId.Self, '2', '7', '0', '#b', '0')
    CameraCmd(0x0A, 0.2, 0.1, 0.0, 100, 1000, 500, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 100, 1500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x8FAE), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x107D), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x32, ParamInt(0x1D5A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.6, 0.8, 0.4)
    CameraSetHeight(0x03, 1.0, 450)
    CameraCmd(0x0C, 0x03, 0.0, -0.1, 0.0, 450)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, -3.0, 5.0, 450, 0x01)
    Sleep(200)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(200)

    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    Sleep(1166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x0088 offset: 0x114E4
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
        'loc_11523',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1155D')

    def _loc_11523(): pass

    label('loc_11523')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11550',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1155D')

    def _loc_11550(): pass

    label('loc_11550')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1155D(): pass

    label('loc_1155D')

    Return()

# id: 0x0089 offset: 0x11560
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_115D0',
    )

    OP_3B(0x32, ParamInt(0x1D76), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11695')

    def _loc_115D0(): pass

    label('loc_115D0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11640',
    )

    OP_3B(0x32, ParamInt(0x1D75), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11695')

    def _loc_11640(): pass

    label('loc_11640')

    OP_3B(0x32, ParamInt(0x1D76), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11695(): pass

    label('loc_11695')

    Return()

# id: 0x008A offset: 0x11698
@scena.Code('AniBtlWin')
def AniBtlWin():
    Call(ScriptId.Current, 'EraseEquip')
    CameraCmd(0x00)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.15, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.25, 15.77, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.0, 1.35, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x02, 0.75, 2.77, 0.0, 2000, 0x01)
    CameraSetDistance(0x02, 1.2, 2000)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '[autoM4]', '', '#b', '0')
    Call(ScriptId.Current, 'VoiceWin_select')
    Sleep(1000)

    Call(ScriptId.Current, 'VoiceWin_play')
    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x77D0), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.0, 3500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.75, 2.63, 0.0, 3500, 0x01)
    CameraSetDistance(0x03, 1.6, 3500)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(1800)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)
    Sleep(600)

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    Sleep(1000)

    Return()

# id: 0x008B offset: 0x1199C
@scena.Code('AniBtlWinKnuckleL')
def AniBtlWinKnuckleL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_KNUCKLE_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x008C offset: 0x119FC
@scena.Code('AniBtlWinBackknuckleL')
def AniBtlWinBackknuckleL():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x008D offset: 0x11A60
@scena.Code('AniBtlWinBackknuckleR')
def AniBtlWinBackknuckleR():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x008E offset: 0x11AC4
@scena.Code('AniBtlWinBackknuckleR2')
def AniBtlWinBackknuckleR2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN_BACKKNUCKLE_R2', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x008F offset: 0x11B2C
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x77D0), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(1800)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')

    Return()

# id: 0x0090 offset: 0x11C28
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '[autoM4]', '', '#b', '0')
    OP_3B(0x32, ParamInt(0x1D77), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x77D0), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(1800)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    OP_3B(0x34, ParamInt(0x1D77))

    Return()

# id: 0x0091 offset: 0x11DC4
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvIdle', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEvIdle')
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x0092 offset: 0x11E44
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x0093 offset: 0x11E50
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0094 offset: 0x11E90
@scena.Code('AniLvup')
def AniLvup():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0095 offset: 0x11EF4
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0', '0[autoM0]', '0', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '00110', '', '0[autoB0]', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(700)

    Return()

# id: 0x0096 offset: 0x120A0
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x0097 offset: 0x120C4
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12131',
    )

    OP_3B(0x32, ParamInt(0x1D78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12186')

    def _loc_12131(): pass

    label('loc_12131')

    OP_3B(0x32, ParamInt(0x1D78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12186(): pass

    label('loc_12186')

    Return()

# id: 0x0098 offset: 0x12188
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtLevelUp_Call', ScriptId.Current)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.23, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x11, 0x03, 5.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1231D',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    OP_3B(0x32, ParamInt(0x1D78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '4', '', '#b', '0')

    Jump('loc_1232A')

    def _loc_1231D(): pass

    label('loc_1231D')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1232A(): pass

    label('loc_1232A')

    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '3', '5554', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '4', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM4]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0099 offset: 0x123C0
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr019_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr019_00_1.eff', 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    OP_3B(0x32, ParamInt(0x1D56), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x104A), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1034), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.65, 0.0, 0)
    CameraSetDistance(0x00, 3.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, -10.0, 0.0, 0, 0x01)
    BattleCmd(0x4B, 0x0000, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 76.6667, 77.8333, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.0, 1.0, -0.1, 1000)
    CameraSetDistance(0x02, 2.5, 1000)
    CameraCmd(0x11, 0x02, -2.0, -5.0, 0.0, 0x03E8, 0x01)
    BattleCmd(0x4B, 0x03E8, 0x02)
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    Sleep(100)

    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(400)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 77.8667, 78.3333, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 1.0, 400)
    CameraSetDistance(0x03, 3.5, 500)
    BattleCmd(0x4B, 0x01F4, 0x03)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x0FE6), ParamFloat(1.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0.75), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.15, 0.15, 0.9)
    OP_3B(0x00, ParamInt(0x1059), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 12.0, -145.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 4.75, 0)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraCmd(0x11, 0x02, 2.0, -10.0, 0.0, 0x0708, 0x01)
    BattleCmd(0x4B, 0x0708, 0x02)
    Sleep(200)

    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 78.3667, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft00_Damage', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x01, ParamInt(0x1059), ParamInt(1000), 0xFFFF)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Sleep(50)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009A offset: 0x12A20
@scena.Code('AniBtlCraft00_Damage')
def AniBtlCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_12A30(): pass

    label('loc_12A30')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_12AD4',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(50)

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

    Jump('loc_12A30')

    def _loc_12AD4(): pass

    label('loc_12AD4')

    Return()

# id: 0x009B offset: 0x12AD8
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr019_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr019_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr019_01_2.eff', 0x00000000)
    BattleCreateChrAfterImage(0xFFFE)
    BattleCmd(0x33, 0xFFFE, 'C_CHR019_BT1', '')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.0, 0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, 22.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 5.0, 0)
    BattleCmd(0x4B, 0x0000, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.8, 0.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 9.0, 35.0, 0.0, 1500, 0x01)
    CameraSetDistance(0x00, 4.7, 800)
    BattleCmd(0x4B, 0x0320, 0x00)
    OP_3B(0x32, ParamInt(0x1D57), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.4, 6.0, 6.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1046), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10D7), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleSetChrAfterImageOn(0xFFFE, 0.05, 0.2, 0.05, 0.5, 1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x00, 0x01, 0x00, 0x00, 0x00, 0.05, -1.0, -1.0, -1.0, 0x00, 0x00)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlCraft01_Move', ScriptId.Current)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 97.3667, 97.8333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.35, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    Sleep(100)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleSetChrAfterImageOff(0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2[autoM2]', '', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0A)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.1, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, -20.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 1.4, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    OP_43(0xFF, 0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.1, 0.0, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.0, -30.0, 0.0, 1500, 0x01)
    CameraSetDistance(0x03, 1.2, 1500)
    BattleCmd(0x4B, 0x05DC, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 97.8667, 98.4667, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FE3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x32, ParamInt(0x1D58), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.2, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 13.0, -90.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 5.0, 0)
    BattleCmd(0x4B, 0x0000, 0x03)
    OP_43(0xFF, 0, 0x0000)
    Sleep(30)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x0000000C, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 10.0, 90.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1326B',
    )

    EffectSetRGBA(0xFFFE, 0x0B, 1.0, 1.0, 1.0, 0.5, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0B, 1.0, 1.0, 1.0, 0.0, 150, 0x03)
    EffectSetRGBA(0xFFFE, 0x0A, 1.0, 1.0, 1.0, 0.0, 150, 0x03)

    def _loc_1326B(): pass

    label('loc_1326B')

    OP_3B(0x00, ParamInt(0x10CE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 2.01, 200)
    CameraSetDistance(0x03, 7.0, 200)
    BattleCmd(0x4B, 0x00C8, 0x03)
    BattleCmd(0x8A)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    BattleCmd(0x4B, 0x01F4, 0x03)
    OP_5E(0x00, 0x0002, 0.75, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(66)

    OP_3B(0x00, ParamInt(0x1042), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(20), ParamFloat(0.8), 0x01)
    CameraCmd(0x09, 0.275, 0.275, 0.85)
    OP_4E(0.2, 0.0, 0x03, 0x00)
    Sleep(200)

    OP_5E(0x01, 0x012C)
    OP_4E(1.0, 0.0, 0x03, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Sleep(200)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 98.5, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    OP_3B(0x01, ParamInt(0x1042), ParamInt(2000), 0xFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    BattleCmd(0x32)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    BattleSetChrPos(0xFFFE, 0xFFF0, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)

    Return()

# id: 0x009C offset: 0x134F0
@scena.Code('AniBtlCraft01_Move')
def AniBtlCraft01_Move():
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -1.0, 2.5, 0x00, 0x01)

    Return()

# id: 0x009D offset: 0x13510
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x38, 'battle/cr019_02_0.eff', 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.85, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, 15.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 4.0, 0)
    BattleCmd(0x4B, 0x0000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.55, 103.333, 104.2, -1.0, 0x00, 0x00)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.8, 0.0, 2300)
    CameraCmd(0x11, 0x03, 2.0, -8.0, 0.0, 0x0A28, 0x01)
    CameraSetDistance(0x03, 2.2, 2700)
    BattleCmd(0x4B, 0x0A8C, 0x03)
    OP_6C(PseudoChrId.Self, 0.4, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    OP_3B(0x32, ParamInt(0x1D59), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '7', 'J', '', '#b', '0')
    OP_3B(0x00, ParamInt(0x1067), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 0.6, 0xFFFFFFFF)
    Sleep(300)

    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    WaitAnimeClipFrames(PseudoChrId.Self, 15)
    OP_6C(PseudoChrId.Self, 0.17, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x00, ParamInt(0x8FAE), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 104.233, 105.767, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, ParamInt(0x1067), ParamInt(500), 0xFFFF)
    OP_3B(0x32, ParamInt(0x1D5A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.0, 200)
    CameraCmd(0x11, 0x00, 1.0, -6.0, 0.0, 0x00C8, 0x01)
    CameraSetDistance(0x00, 5.0, 200)
    BattleCmd(0x4B, 0x00C8, 0x03)
    CameraCmd(0x09, 0.24, 0.24, 1.0)
    OP_5E(0x00, 0x0002, 0.75, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.45, 0.0, 2000)
    CameraCmd(0x11, 0x00, 1.0, -22.0, 0.0, 0x07D0, 0x01)
    CameraSetDistance(0x00, 7.0, 2000)
    BattleCmd(0x4B, 0x07D0, 0x00)
    OP_5E(0x01, 0x012C)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 105.8, 106.667, -1.0, 0x00, 0x00)
    Sleep(50)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(50)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009E offset: 0x13B1C
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    Call(ScriptId.BtlCom, 'SET_MOVE_SPEED', ParamFloat(6))
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR019_SC1')
    BattleCmd(0x52, 0xFFFE, 0x38)
    LoadEffect(0xFFFE, 0x39, 'battle/sc019_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc019_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc019_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc019_00_5.eff', 0x00000000)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 10.0, 0.0)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, -10.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF4, 0.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10F1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x32, ParamInt(0x1D5B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraft00_Mouth01', ScriptId.Current)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    Sleep(0)

    CameraCmd(0x00)
    CameraCmd(0x03, 0x03, 0xFFFE, '', 0.0, 1.1, 0.0, 0x0000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, 40.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.75, 0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0[autoM0]', '', '#b', '0')
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.0, 0.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, -32.0, 0.0, 2000, 0x01)
    CameraSetDistance(0x00, 3.6, 1500)
    Sleep(650)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.9, 0.0, 1200)
    CameraSetDistance(0x03, 2.8, 1200)
    Sleep(850)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, 118.7, 119.0, -1.0, 0x00, 0x00)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, 1.0, 0.0, 400, 0x01)
    CameraSetDistance(0x00, 2.2, 400)
    Sleep(266)

    OP_6C(PseudoChrId.Self, 0.1, 0xFFFFFFFF)
    Sleep(433)

    CameraSetDistance(0x00, 2.0, 1000)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.1, 0.0, 1200)
    CameraSetDistance(0x00, 5.5, 300)
    OP_5E(0x00, 0x0002, 0.35, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 119.033, 119.233, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1047), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1062), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_6C(PseudoChrId.Self, 0.1, 0xFFFFFFFF)
    CameraSetDistance(0x00, 5.9, 1000)
    Sleep(400)

    OP_5E(0x01, 0x02BC)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 119.267, 119.567, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.6, 0.0, 400)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, -26.0, 0.0, 400, 0x01)
    CameraSetDistance(0x00, 3.4, 400)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitForThreadExit(PseudoChrId.Self, 0x03)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 119.6, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x10ED), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000200)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft00_Jump', ScriptId.Current)
    Sleep(100)

    OP_3B(0x32, ParamInt(0x1D5C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPos(0x03, 0.0, 4.0, -10.0, 400)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.0, 45.0, 0.0, 700, 0x01)
    CameraSetDistance(0x00, 6.0, 700)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Sleep(100)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 10.0, -10.0, 0)
    CameraSetDistance(0x03, 4.2, 0)
    SetChrFace(0x03, PseudoChrId.Self, '1', '0[autoM0]', '', '#b', '0')
    OP_43(0xFF, 0, 0x0000)
    CameraSetPos(0x00, 0.0, 12.5, -10.0, 200)
    CameraRotateByTarget(0xFFFE, '', 0x00, -4.0, 75.0, 10.0, 200, 0x01)
    CameraSetDistance(0x03, 3.0, 400)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 120.033, 120.333, -1.0, 0x00, 0x00)
    CameraSetPos(0x03, 0.0, 12.8, -10.0, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x00, -2.0, 195.0, 10.0, 200, 0x01)
    CameraSetDistance(0x03, 1.7, 700)
    Sleep(200)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 120.333, 120.833, -1.0, 0x00, 0x00)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, 315.0, 10.0, 200, 0x01)
    Sleep(200)

    CameraRotateByTarget(0xFFFE, '', 0x00, 9.0, 395.0, 10.0, 400, 0x01)
    Sleep(200)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 120.867, 121.267, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x10E9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, -0.2, 400)
    CameraRotateByTarget(0xFFFE, '', 0x00, 12.0, 395.0, 10.0, 400, 0x01)
    CameraSetDistance(0x03, 1.8, 400)
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(366)

    OP_6C(PseudoChrId.Self, 0.05, 0xFFFFFFFF)
    Sleep(33)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.85, 0.9, 600)
    CameraRotateByTarget(0xFFFE, '', 0x00, -3.0, 365.0, 10.0, 900, 0x01)
    CameraSetDistance(0x03, 2.2, 1500)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(300)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 0.65, 1.1, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -9.0, 377.0, 10.0, 1000, 0x01)
    Sleep(600)

    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x32, ParamInt(0x1D5D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 121.3, 121.367, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraft00_FAll', ScriptId.Current)
    OP_3B(0x00, ParamInt(0x1059), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1043), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_05', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, -5.0, 5.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -12.0, 382.0, 0.0, 400, 0x01)
    CameraSetDistance(0x03, 6.0, 400)
    OP_5E(0x00, 0x0002, 0.25, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraCmd(0x09, 0.125, 0.15, 1.0)
    OP_3B(0xFF, 0.5, 0.7, 0.4)
    Sleep(350)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.4, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, 12.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.2, 0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_5E(0x00, 0x0002, 0.3, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraCmd(0x09, 0.15, 0.25, 5.0)
    OP_43(0xFF, 0, 0x0000)
    CameraSetDistance(0x03, 6.5, 700)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, 30.0, 0.0, 1000, 0x01)
    WaitForThreadExit(PseudoChrId.Self, 0x03)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraft00_FAll2', ScriptId.Current)
    Sleep(1000)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(1), ParamInt(0x0032), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x14BF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetDistance(0x03, 9.5, 500)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, -0.5, 1.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 7.0, 45.0, 0.0, 2000, 0x01)
    Sleep(900)

    Sleep(500)

    WaitForThreadExit(PseudoChrId.Self, 0x03)

    CreateThread(PseudoChrId.Self, 0x03, 'AniBtlSCraft00_FAll3', ScriptId.Current)
    OP_3B(0x00, ParamInt(0x10CE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1059), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-5), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, -4.0, 2.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 40.0, 135.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 10.2, 800)
    Sleep(500)

    CameraRotateByTarget(0xFFFE, '', 0x00, 43.0, 145.0, 0.0, 1000, 0x01)
    Sleep(500)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    EffectCmd(0x0F, 0xFFFE, 0x003C, 0x01)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x000007D0, 0x00000000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 5.5, 10.0, 0)
    CameraRotate(0x00, 4.0, -115.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 18.5, 0)
    SetChrFace(0x03, PseudoChrId.Self, '1', '0', '', '#b', '0')
    CameraCmd(0x09, 0.15, 0.25, 5.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(2), ParamFloat(2), ParamFloat(2), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0xFFFF, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_5E(0x00, 0x0002, 0.3, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_43(0xFF, 0, 0x0000)
    CameraSetPos(0x03, 0.0, 4.0, 6.0, 800)
    CameraRotate(0x00, 10.0, -5.0, 10.0, 800, 0x01)
    CameraSetDistance(0x03, 12.0, 800)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x105D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F52), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0002, 0.65, 0, 100, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    OP_3B(0x00, ParamInt(0x0FC7), ParamFloat(1), ParamInt(0x000A), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 2.0, 2.0, 1.0)
    CameraSetPos(0x00, 0.0, 3.0, 0.0, 3000)
    CameraRotate(0x00, 6.0, 45.0, 10.0, 3000, 0x01)
    CameraSetDistance(0x00, 23.0, 500)
    Sleep(500)

    CameraCmd(0x09, 1.0, 1.0, 3.0)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft00_Damage', ScriptId.Current)
    CameraSetDistance(0x00, 35.0, 2000)
    Sleep(700)

    OP_43(0x03, 1200, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    OP_5E(0x01, 0x0064)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x03)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000800)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR019_SC1')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'RESET_MOVE_SPEED')
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x009F offset: 0x15154
@scena.Code('AniBtlSCraft00_Jump')
def AniBtlSCraft00_Jump():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 6.0, 0.0, 4.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 3.0, 0.0, 4.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 1.5, 0.0, 4.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.75, 0.0, 4.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.375, 0.0, 4.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.18, 0.0, 4.0, 0x00, 0x00)

    Return()

# id: 0x00A0 offset: 0x15200
@scena.Code('AniBtlSCraft00_FAll')
def AniBtlSCraft00_FAll():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, -7.0, 7.0, 5.0, 0x00, 0x00)

    Return()

# id: 0x00A1 offset: 0x15220
@scena.Code('AniBtlSCraft00_FAll2')
def AniBtlSCraft00_FAll2():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, -1.0, 1.0, 0.1, 0x00, 0x00)

    Return()

# id: 0x00A2 offset: 0x15240
@scena.Code('AniBtlSCraft00_FAll3')
def AniBtlSCraft00_FAll3():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, -8.0, 8.0, 5.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, -11.0, 11.0, 5.0, 0x00, 0x00)

    Return()

# id: 0x00A3 offset: 0x1527C
@scena.Code('AniBtlSCraft00_Damage')
def AniBtlSCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1528C(): pass

    label('loc_1528C')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_15324',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(150)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1528C')

    def _loc_15324(): pass

    label('loc_15324')

    Return()

# id: 0x00A4 offset: 0x15328
@scena.Code('AniBtlSCraft00_Mouth01')
def AniBtlSCraft00_Mouth01():
    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '3', '', '', '#b', '0')
    Sleep(800)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')

    Return()

# id: 0x00A5 offset: 0x154A4
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A6 offset: 0x154D4
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A7 offset: 0x15504
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A8 offset: 0x15534
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A9 offset: 0x15574
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
        'loc_15603',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_156DC')

    def _loc_15603(): pass

    label('loc_15603')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1567E',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_156DC')

    def _loc_1567E(): pass

    label('loc_1567E')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_156DC(): pass

    label('loc_156DC')

    Return()

# id: 0x00AA offset: 0x156E0
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AB offset: 0x1571C
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AC offset: 0x15778
@scena.Code('AniEvIdle')
def AniEvIdle():
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AD offset: 0x157D8
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AE offset: 0x1580C
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AF offset: 0x15840
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B0 offset: 0x15884
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B1 offset: 0x158B8
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    Sleep(433)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x00)
    SetEndhookFunction('EraseEquip', 0x000B)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00B2 offset: 0x1599C
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B3 offset: 0x15A08
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B4 offset: 0x15A74
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B5 offset: 0x15AE4
@scena.Code('AniEvGuard')
def AniEvGuard():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_GUARD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B6 offset: 0x15B1C
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B7 offset: 0x15B50
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B8 offset: 0x15BB8
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B9 offset: 0x15C24
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BA offset: 0x15C90
@scena.Code('AniEvDead')
def AniEvDead():
    CreateThread(PseudoChrId.Self, 0x01, 'SpringOff', ScriptId.Current)
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BB offset: 0x15D1C
@scena.Code('AniEvDead1')
def AniEvDead1():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BC offset: 0x15D54
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BD offset: 0x15DBC
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BE offset: 0x15DF0
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BF offset: 0x15E58
@scena.Code('AniEvWinA')
def AniEvWinA():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C0 offset: 0x15E8C
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C1 offset: 0x15EFC
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C2 offset: 0x15F5C
@scena.Code('AniEvHorseWait')
def AniEvHorseWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C3 offset: 0x15FA0
@scena.Code('AniEvHorseWalk')
def AniEvHorseWalk():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C4 offset: 0x15FE8
@scena.Code('AniEvHorseRun')
def AniEvHorseRun():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C5 offset: 0x16030
@scena.Code('AniEvHorseStop')
def AniEvHorseStop():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C6 offset: 0x1609C
@scena.Code('AniEvHorseTurnRight')
def AniEvHorseTurnRight():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C7 offset: 0x1610C
@scena.Code('AniEvHorseTurnLeft')
def AniEvHorseTurnLeft():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00C8 offset: 0x1617C
@scena.Code('AniEvHorseDash')
def AniEvHorseDash():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C9 offset: 0x161C4
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CA offset: 0x16230
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CB offset: 0x1629C
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CC offset: 0x16308
@scena.Code('AniEvCraft02b')
def AniEvCraft02b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT02', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, 104.367, 104.367, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CD offset: 0x16334
@scena.Code('AniEvSCraft01')
def AniEvSCraft01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x163AC
@scena.Code('AniEvSCraft01_02')
def AniEvSCraft01_02():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CF offset: 0x163E8
@scena.Code('AniEvSCraft01_03')
def AniEvSCraft01_03():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_05', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x16460
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D1 offset: 0x1649C
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D2 offset: 0x16500
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x00D3 offset: 0x1653C
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D4 offset: 0x16574
@scena.Code('AniEvUdegumi')
def AniEvUdegumi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_16643',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_16781')

    def _loc_16643(): pass

    label('loc_16643')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_166E8',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMI', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_16781')

    def _loc_166E8(): pass

    label('loc_166E8')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_16781(): pass

    label('loc_16781')

    Return()

# id: 0x00D5 offset: 0x16784
@scena.Code('AniEvUdegumiTeburi')
def AniEvUdegumiTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMI_t', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D6 offset: 0x16848
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x17B0), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D7 offset: 0x169C4
@scena.Code('AniEv40050')
def AniEv40050():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev40050', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D8 offset: 0x169F8
@scena.Code('AniEv40055')
def AniEv40055():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev40055', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev40055a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x16A60
@scena.Code('AniEv45010')
def AniEv45010():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45010', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev45010a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00DA offset: 0x16ABC
@scena.Code('AniEv45010a')
def AniEv45010a():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45010a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DB offset: 0x16AF0
@scena.Code('AniEv45015')
def AniEv45015():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45015', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00DC offset: 0x16B4C
@scena.Code('AniEv45020')
def AniEv45020():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45020', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev45020a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00DD offset: 0x16BA8
@scena.Code('AniEv45020a')
def AniEv45020a():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45020a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x16BDC
@scena.Code('AniEv45085')
def AniEv45085():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV45085', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x16C30
@scena.Code('AniEv45090')
def AniEv45090():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev45090', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E0 offset: 0x16C64
@scena.Code('AniAttachEQU437')
def AniAttachEQU437():
    LoadAsset('C_EQU437')
    AttachEquip(0xFFFE, 'C_EQU437', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00E1 offset: 0x16CFC
@scena.Code('AniDetachEQU437')
def AniDetachEQU437():
    ReleaseAsset('C_EQU437')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x00E2 offset: 0x16D48
@scena.Code('AniEv53550')
def AniEv53550():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53550', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E3 offset: 0x16DAC
@scena.Code('AniEv53550w')
def AniEv53550w():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53550w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E4 offset: 0x16E10
@scena.Code('AniEv53555')
def AniEv53555():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53555', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev53555a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E5 offset: 0x16EA4
@scena.Code('AniEv53560')
def AniEv53560():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53560', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E6 offset: 0x16ED8
@scena.Code('AniEv53561')
def AniEv53561():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53561', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev53561a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E7 offset: 0x16F6C
@scena.Code('AniEv53561a')
def AniEv53561a():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev53561', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.8, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev53561a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x16FD4
@scena.Code('AniEv70120')
def AniEv70120():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70120', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E9 offset: 0x17008
@scena.Code('AniAttachEQU172')
def AniAttachEQU172():
    LoadAsset('C_EQU172')
    AttachEquip(0xFFFE, 'C_EQU172', 'head_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'head_point', 0x01)

    Return()

# id: 0x00EA offset: 0x17070
@scena.Code('AniDetachEQU172')
def AniDetachEQU172():
    ReleaseAsset('C_EQU172')
    DeatchEquip(0xFFFE, 'head_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00EB offset: 0x170C0
@scena.Code('AniEv70125')
def AniEv70125():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70125', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EC offset: 0x17114
@scena.Code('AniEv74195')
def AniEv74195():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74195', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00ED offset: 0x17148
@scena.Code('AniEv74310')
def AniEv74310():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74310', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EE offset: 0x1719C
@scena.Code('AniEv79290')
def AniEv79290():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79290', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79290a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x17204
@scena.Code('AniEv79291')
def AniEv79291():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79291', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79291a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x1726C
@scena.Code('AniEv79292')
def AniEv79292():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79292', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79292a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x172D4
@scena.Code('AniEv79293')
def AniEv79293():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79293', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79293a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F2 offset: 0x1733C
@scena.Code('AniEv79294')
def AniEv79294():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79294', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79294a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F3 offset: 0x173A4
@scena.Code('AniEv79295')
def AniEv79295():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79295', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79295a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F4 offset: 0x1740C
@scena.Code('AniEv79296')
def AniEv79296():
    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79296', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'Ev79296a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F5 offset: 0x17474
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR019_EV', 'ev35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk019.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk019_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x24, 'battle/atk019_a1.eff', 0x00000000)

    Return()

# id: 0x00F6 offset: 0x174F4
@scena.Code('AniCvRelease')
def AniCvRelease():
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'ev35000')
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)

    Return()

# id: 0x00F7 offset: 0x17540
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x175A8
@scena.Code('AniCvIdle')
def AniCvIdle():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
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
        'loc_1765E',
    )

    OP_3B(0x32, ParamInt(0x1D98), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_176B3')

    def _loc_1765E(): pass

    label('loc_1765E')

    OP_3B(0x32, ParamInt(0x1D99), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_176B3(): pass

    label('loc_176B3')

    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    SetChrFace(0x03, PseudoChrId.Self, '1', '', '', '#b', '0')
    Sleep(1333)

    Call(ScriptId.Current, 'DefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x00F9 offset: 0x17748
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_3B(0x00, ParamInt(0x17B0), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_forearm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FA offset: 0x178F4
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

    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1DC9), ParamInt(0x1DCA), ParamInt(0), ParamInt(0))
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17A1A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0.04), ParamFloat(0.06), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_17A1A(): pass

    label('loc_17A1A')

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x1104), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    Sleep(166)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FB offset: 0x17AF8
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

    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    SetChrFace(0x03, PseudoChrId.Self, '3', '6[autoM6]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 76.6667, 77.0667, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D54), ParamInt(0x1D55), ParamInt(0), ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 77.1, 78.6667, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FE6), ParamFloat(1.2), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    Sleep(5)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17DAB',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0), ParamFloat(0.85), ParamFloat(0.75), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_17DAB(): pass

    label('loc_17DAB')

    OP_3B(0x00, ParamInt(0x1059), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, ParamInt(0x1059), ParamInt(1500), 0xFFFF)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    Sleep(666)

    Call(ScriptId.Current, 'BtlDefaultFace')
    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    OP_41(0xFFFE, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.3, 6.66667, 6.66667, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FC offset: 0x17ECC
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_forearm_point', 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    Sleep(233)

    OP_3B(0x00, ParamInt(0x1781), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    Call(ScriptId.Current, 'EraseEquip')
    SetEndhookFunction('EraseEquip', 0x000B)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FD offset: 0x180A0
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_180C5',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_180C5(): pass

    label('loc_180C5')

    Return()

# id: 0x00FE offset: 0x180C8
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1812A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_1812A(): pass

    label('loc_1812A')

    Return()

# id: 0x00FF offset: 0x1812C
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_181AF',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_18292')

    def _loc_181AF(): pass

    label('loc_181AF')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D5F), ParamInt(0x1D60), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_18292(): pass

    label('loc_18292')

    Return()

# id: 0x0100 offset: 0x18294
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x1D61), ParamInt(0x1D62), ParamInt(0), ParamInt(0))
    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Sleep(500)

    BattleCmd(0x05, 0x00, '')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)
    Sleep(300)

    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0101 offset: 0x184C0
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(100)

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_185C5',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    OP_3B(0x32, ParamInt(0x1D78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '4', '', '#b', '0')

    Jump('loc_185D2')

    def _loc_185C5(): pass

    label('loc_185C5')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_185D2(): pass

    label('loc_185D2')

    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '3', '5554', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '4', '', '#b', '0')
    Sleep(500)

    SetChrFace(0x03, PseudoChrId.Self, '', '[autoM4]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x0102 offset: 0x18670
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_R2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_L2',
        ),
    )

# id: 0x0103 offset: 0x18740
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0104 offset: 0x187F0
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4E,
            name   = '',
        ),
    )

# id: 0x0105 offset: 0x188A0
@scena.AnimeClips('_AniAttachEQU072')
def _AniAttachEQU072():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_R2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU072_L2',
        ),
    )

# id: 0x0106 offset: 0x18970
@scena.AnimeClips('_AniAttachPhone')
def _AniAttachPhone():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320_C04',
        ),
    )

# id: 0x0107 offset: 0x189D0
@scena.AnimeClips('_AniEv02050')
def _AniEv02050():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev02050',
        ),
    )

# id: 0x0108 offset: 0x18A30
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

# id: 0x0109 offset: 0x18A90
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

# id: 0x010A offset: 0x18AF0
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

# id: 0x010B offset: 0x18B50
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

# id: 0x010C offset: 0x18BB0
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

# id: 0x010D offset: 0x18C10
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

# id: 0x010E offset: 0x18C90
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

# id: 0x010F offset: 0x18D10
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

# id: 0x0110 offset: 0x18D90
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

# id: 0x0111 offset: 0x18DF0
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

# id: 0x0112 offset: 0x18E50
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

# id: 0x0113 offset: 0x18EB0
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

# id: 0x0114 offset: 0x18F10
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

# id: 0x0115 offset: 0x18F70
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

# id: 0x0116 offset: 0x18FF0
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

# id: 0x0117 offset: 0x19050
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

# id: 0x0118 offset: 0x190B0
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

# id: 0x0119 offset: 0x19180
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

# id: 0x011A offset: 0x19280
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

# id: 0x011B offset: 0x192E0
@scena.AnimeClips('_AniLand')
def _AniLand():
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
            name   = 'LAND',
        ),
    )

# id: 0x011C offset: 0x19360
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

# id: 0x011D offset: 0x19640
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

# id: 0x011E offset: 0x19710
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

# id: 0x011F offset: 0x19790
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

# id: 0x0120 offset: 0x19810
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

# id: 0x0121 offset: 0x19870
@scena.AnimeClips('_AniDamage')
def _AniDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D63,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0122 offset: 0x198F0
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D98,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D99,
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

# id: 0x0123 offset: 0x199C0
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
            dword4 = 0x00001DC9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0124 offset: 0x19AC0
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0125 offset: 0x19BC0
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
            name   = 'BTL_WAIT',
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
            dword4 = 0x00001D54,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D55,
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
            dword4 = 0x00000FE6,
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0126 offset: 0x19D60
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
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0127 offset: 0x19E30
@scena.AnimeClips('_AniFieldAttackEnd_endHook')
def _AniFieldAttackEnd_endHook():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001781,
            name   = '',
        ),
    )

# id: 0x0128 offset: 0x19E90
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
            dword4 = 0x00001781,
            name   = '',
        ),
    )

# id: 0x0129 offset: 0x19F10
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

# id: 0x012A offset: 0x19F70
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

# id: 0x012B offset: 0x19FD0
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU172',
        ),
    )

# id: 0x012C offset: 0x1A030
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D71,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D74,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D6F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D70,
            name   = '',
        ),
    )

# id: 0x012D offset: 0x1A130
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D50,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D4E,
            name   = '',
        ),
    )

# id: 0x012E offset: 0x1A230
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D73,
            name   = '',
        ),
    )

# id: 0x012F offset: 0x1A290
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

# id: 0x0130 offset: 0x1A2F0
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

# id: 0x0131 offset: 0x1A370
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
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D51,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D52,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D53,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DC9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCB,
            name   = '',
        ),
    )

# id: 0x0132 offset: 0x1A560
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D67,
            name   = '',
        ),
    )

# id: 0x0133 offset: 0x1A5C0
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

# id: 0x0134 offset: 0x1A640
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D63,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D64,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D65,
            name   = '',
        ),
    )

# id: 0x0135 offset: 0x1A6F0
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

# id: 0x0136 offset: 0x1A7A0
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

# id: 0x0137 offset: 0x1A800
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
            dword4 = 0x00001D66,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0138 offset: 0x1A8B0
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
            dword4 = 0x00001D61,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D62,
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

# id: 0x0139 offset: 0x1A9D0
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
            dword4 = 0x00001D61,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D62,
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

# id: 0x013A offset: 0x1AAD0
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

# id: 0x013B offset: 0x1AB30
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D6C,
            name   = '',
        ),
    )

# id: 0x013C offset: 0x1AB90
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D6D,
            name   = '',
        ),
    )

# id: 0x013D offset: 0x1ABF0
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D6E,
            name   = '',
        ),
    )

# id: 0x013E offset: 0x1AC50
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D79,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D7A,
            name   = '',
        ),
    )

# id: 0x013F offset: 0x1ACD0
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
    return ScenaAnimeClips(
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
            dword4 = 0x00001D8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D89,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D89,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D7B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
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

# id: 0x0140 offset: 0x1B160
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

# id: 0x0141 offset: 0x1B1C0
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

# id: 0x0142 offset: 0x1B220
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
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DBF,
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
            name   = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0143 offset: 0x1B4B0
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

# id: 0x0144 offset: 0x1B510
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5E,
            name   = '',
        ),
    )

# id: 0x0145 offset: 0x1B590
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

# id: 0x0146 offset: 0x1B5F0
@scena.AnimeClips('_AniBtlValiantArts_Aria')
def _AniBtlValiantArts_Aria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_V_ARIA',
        ),
    )

# id: 0x0147 offset: 0x1B670
@scena.AnimeClips('_AniBtlValiantArts_Support')
def _AniBtlValiantArts_Support():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_V_ARIA',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7F,
            name   = '',
        ),
    )

# id: 0x0148 offset: 0x1B6F0
@scena.AnimeClips('_AniBtlValiantHeal_Aria')
def _AniBtlValiantHeal_Aria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_V_ARIA',
        ),
    )

# id: 0x0149 offset: 0x1B750
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
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D59,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F38,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x014A offset: 0x1B940
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D76,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D75,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D76,
            name   = '',
        ),
    )

# id: 0x014B offset: 0x1B9F0
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
            dword4 = 0x000077D0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x014C offset: 0x1BAA0
@scena.AnimeClips('_AniBtlWinKnuckleL')
def _AniBtlWinKnuckleL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_KNUCKLE_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x014D offset: 0x1BB20
@scena.AnimeClips('_AniBtlWinBackknuckleL')
def _AniBtlWinBackknuckleL():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x014E offset: 0x1BBA0
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

# id: 0x014F offset: 0x1BC20
@scena.AnimeClips('_AniBtlWinBackknuckleR2')
def _AniBtlWinBackknuckleR2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN_BACKKNUCKLE_R2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0150 offset: 0x1BCA0
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
            dword4 = 0x000077D0,
            name   = '',
        ),
    )

# id: 0x0151 offset: 0x1BD20
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
            dword4 = 0x00001D77,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000077D0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0152 offset: 0x1BDF0
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

# id: 0x0153 offset: 0x1BE50
@scena.AnimeClips('_AniLvup')
def _AniLvup():
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

# id: 0x0154 offset: 0x1BED0
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
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
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0155 offset: 0x1BFD0
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D78,
            name   = '',
        ),
    )

# id: 0x0156 offset: 0x1C050
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0157 offset: 0x1C100
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D56,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000104A,
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE6,
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
            name   = 'BTL_CRAFT00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0158 offset: 0x1C310
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D57,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001046,
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
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
            name   = 'BTL_CRAFT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FE3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001042,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0159 offset: 0x1C5C0
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr019_02_0.eff',
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
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D59,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001067,
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
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x015A offset: 0x1C7B0
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc019_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc019_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc019_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc019_00_5.eff',
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
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
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
            dword4 = 0x00001047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001062,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
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
            dword4 = 0x000010ED,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5C,
            name   = '',
        ),
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
            name   = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001059,
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_05',
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
            dword4 = 0x00001066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000014BF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001059,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000105D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F52,
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
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x015B offset: 0x1CDB0
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

# id: 0x015C offset: 0x1CE10
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

# id: 0x015D offset: 0x1CE70
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

# id: 0x015E offset: 0x1CED0
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

# id: 0x015F offset: 0x1CF30
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

# id: 0x0160 offset: 0x1D030
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

# id: 0x0161 offset: 0x1D090
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

# id: 0x0162 offset: 0x1D110
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

# id: 0x0163 offset: 0x1D190
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

# id: 0x0164 offset: 0x1D1F0
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

# id: 0x0165 offset: 0x1D250
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

# id: 0x0166 offset: 0x1D2B0
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

# id: 0x0167 offset: 0x1D310
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
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0168 offset: 0x1D390
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

# id: 0x0169 offset: 0x1D410
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

# id: 0x016A offset: 0x1D490
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

# id: 0x016B offset: 0x1D510
@scena.AnimeClips('_AniEvGuard')
def _AniEvGuard():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_GUARD',
        ),
    )

# id: 0x016C offset: 0x1D570
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

# id: 0x016D offset: 0x1D5D0
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

# id: 0x016E offset: 0x1D650
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

# id: 0x016F offset: 0x1D6D0
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

# id: 0x0170 offset: 0x1D750
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

# id: 0x0171 offset: 0x1D7D0
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

# id: 0x0172 offset: 0x1D830
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

# id: 0x0173 offset: 0x1D8B0
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

# id: 0x0174 offset: 0x1D910
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

# id: 0x0175 offset: 0x1D990
@scena.AnimeClips('_AniEvWinA')
def _AniEvWinA():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0176 offset: 0x1D9F0
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

# id: 0x0177 offset: 0x1DA70
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0178 offset: 0x1DAF0
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

# id: 0x0179 offset: 0x1DB50
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

# id: 0x017A offset: 0x1DBB0
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

# id: 0x017B offset: 0x1DC10
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

# id: 0x017C offset: 0x1DC90
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

# id: 0x017D offset: 0x1DD10
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

# id: 0x017E offset: 0x1DD90
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

# id: 0x017F offset: 0x1DDF0
@scena.AnimeClips('_AniEvCraft00')
def _AniEvCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0180 offset: 0x1DE70
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0181 offset: 0x1DEF0
@scena.AnimeClips('_AniEvCraft02')
def _AniEvCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0182 offset: 0x1DF70
@scena.AnimeClips('_AniEvCraft02b')
def _AniEvCraft02b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02',
        ),
    )

# id: 0x0183 offset: 0x1DFD0
@scena.AnimeClips('_AniEvSCraft01')
def _AniEvSCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_02',
        ),
    )

# id: 0x0184 offset: 0x1E050
@scena.AnimeClips('_AniEvSCraft01_02')
def _AniEvSCraft01_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_03',
        ),
    )

# id: 0x0185 offset: 0x1E0B0
@scena.AnimeClips('_AniEvSCraft01_03')
def _AniEvSCraft01_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_05',
        ),
    )

# id: 0x0186 offset: 0x1E130
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

# id: 0x0187 offset: 0x1E190
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

# id: 0x0188 offset: 0x1E1F0
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

# id: 0x0189 offset: 0x1E250
@scena.AnimeClips('_AniEvUdegumi')
def _AniEvUdegumi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIa',
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
            name   = 'EV_UDEGUMI',
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
            name   = 'EV_UDEGUMI',
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
            name   = 'EV_UDEGUMIa',
        ),
    )

# id: 0x018A offset: 0x1E3C0
@scena.AnimeClips('_AniEvUdegumiTeburi')
def _AniEvUdegumiTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_t',
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
            name   = 'EV_UDEGUMIa',
        ),
    )

# id: 0x018B offset: 0x1E470
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
            dword4 = 0x000017B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x018C offset: 0x1E520
@scena.AnimeClips('_AniEv40050')
def _AniEv40050():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev40050',
        ),
    )

# id: 0x018D offset: 0x1E580
@scena.AnimeClips('_AniEv40055')
def _AniEv40055():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev40055',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev40055a',
        ),
    )

# id: 0x018E offset: 0x1E600
@scena.AnimeClips('_AniEv45010')
def _AniEv45010():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45010',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45010a',
        ),
    )

# id: 0x018F offset: 0x1E680
@scena.AnimeClips('_AniEv45010a')
def _AniEv45010a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45010a',
        ),
    )

# id: 0x0190 offset: 0x1E6E0
@scena.AnimeClips('_AniEv45015')
def _AniEv45015():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45015',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BIKE_RUN',
        ),
    )

# id: 0x0191 offset: 0x1E760
@scena.AnimeClips('_AniEv45020')
def _AniEv45020():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45020',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45020a',
        ),
    )

# id: 0x0192 offset: 0x1E7E0
@scena.AnimeClips('_AniEv45020a')
def _AniEv45020a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45020a',
        ),
    )

# id: 0x0193 offset: 0x1E840
@scena.AnimeClips('_AniEv45085')
def _AniEv45085():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV45085',
        ),
    )

# id: 0x0194 offset: 0x1E8A0
@scena.AnimeClips('_AniEv45090')
def _AniEv45090():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45090',
        ),
    )

# id: 0x0195 offset: 0x1E900
@scena.AnimeClips('_AniAttachEQU437')
def _AniAttachEQU437():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU437',
        ),
    )

# id: 0x0196 offset: 0x1E960
@scena.AnimeClips('_AniEv53550')
def _AniEv53550():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53550',
        ),
    )

# id: 0x0197 offset: 0x1E9C0
@scena.AnimeClips('_AniEv53550w')
def _AniEv53550w():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53550w',
        ),
    )

# id: 0x0198 offset: 0x1EA20
@scena.AnimeClips('_AniEv53555')
def _AniEv53555():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53555',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53555a',
        ),
    )

# id: 0x0199 offset: 0x1EAA0
@scena.AnimeClips('_AniEv53560')
def _AniEv53560():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53560',
        ),
    )

# id: 0x019A offset: 0x1EB00
@scena.AnimeClips('_AniEv53561')
def _AniEv53561():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53561',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53561a',
        ),
    )

# id: 0x019B offset: 0x1EB80
@scena.AnimeClips('_AniEv53561a')
def _AniEv53561a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53561',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev53561a',
        ),
    )

# id: 0x019C offset: 0x1EC00
@scena.AnimeClips('_AniEv70120')
def _AniEv70120():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70120',
        ),
    )

# id: 0x019D offset: 0x1EC60
@scena.AnimeClips('_AniAttachEQU172')
def _AniAttachEQU172():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU172',
        ),
    )

# id: 0x019E offset: 0x1ECC0
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

# id: 0x019F offset: 0x1ED20
@scena.AnimeClips('_AniEv74195')
def _AniEv74195():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV74195',
        ),
    )

# id: 0x01A0 offset: 0x1ED80
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

# id: 0x01A1 offset: 0x1EDE0
@scena.AnimeClips('_AniEv79290')
def _AniEv79290():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79290',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79290a',
        ),
    )

# id: 0x01A2 offset: 0x1EE60
@scena.AnimeClips('_AniEv79291')
def _AniEv79291():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79291',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79291a',
        ),
    )

# id: 0x01A3 offset: 0x1EEE0
@scena.AnimeClips('_AniEv79292')
def _AniEv79292():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79292',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79292a',
        ),
    )

# id: 0x01A4 offset: 0x1EF60
@scena.AnimeClips('_AniEv79293')
def _AniEv79293():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79293',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79293a',
        ),
    )

# id: 0x01A5 offset: 0x1EFE0
@scena.AnimeClips('_AniEv79294')
def _AniEv79294():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79294',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79294a',
        ),
    )

# id: 0x01A6 offset: 0x1F060
@scena.AnimeClips('_AniEv79295')
def _AniEv79295():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79295',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79295a',
        ),
    )

# id: 0x01A7 offset: 0x1F0E0
@scena.AnimeClips('_AniEv79296')
def _AniEv79296():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79296',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'Ev79296a',
        ),
    )

# id: 0x01A8 offset: 0x1F160
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk019.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk019_a0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk019_a1.eff',
        ),
    )

# id: 0x01A9 offset: 0x1F210
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

# id: 0x01AA offset: 0x1F270
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D98,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D99,
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

# id: 0x01AB offset: 0x1F340
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
            dword4 = 0x000017B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AC offset: 0x1F3F0
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
            dword4 = 0x00001DC9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001DCA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001104,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AD offset: 0x1F4F0
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
            name   = 'BTL_WAIT',
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
            dword4 = 0x00001D54,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D55,
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
            dword4 = 0x00000FE6,
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01AE offset: 0x1F690
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
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001781,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01AF offset: 0x1F760
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
            dword4 = 0x00001D5F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x01B0 offset: 0x1F860
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
            dword4 = 0x00001D61,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D62,
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

# id: 0x01B1 offset: 0x1F9B0
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001D78,
            name   = '',
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
