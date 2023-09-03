import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr034_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr034.dat')

# id: 0x0000 offset: 0x1F0C
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'FATTACK1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR034_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WIN1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_WIN1a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR034_BT1',
            symbol     = 'BTL_CRAFT12_04a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_15',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_16',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR034_SC1',
            symbol     = 'BTL_S_CRAFT01_17',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'WAIT1_U',
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
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHR034_EV',
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
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHR034_EV',
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
            symbol     = 'EV_FUANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_sb',
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
            symbol     = 'EV_INORI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_JUMP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_JUMPa',
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
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            symbol     = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE_sb',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_ATAMA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
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
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_SQUATa',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
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
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
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
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
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
            asset      = 'C_CHR034_EV',
            symbol     = 'EV00380',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV00380a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev03515',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev03515a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev04000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev04000a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV04060',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV04060a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV04550',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV30005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV30005a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV30065',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev30065r',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev30065w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV31030',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV31030a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV75550',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV75550a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV75551',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV75551a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV86045',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR034_EV',
            symbol     = 'EV86050',
        ),
    )

# id: 0x0001 offset: 0x9FE8
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0xA008
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0xA020
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_A063',
    )

    AnimeClipCmd(0x0C, PseudoChrId.Self, 'C_CHR034_C00_FC1', '')

    Jump('loc_A06D')

    def _loc_A063(): pass

    label('loc_A063')

    AnimeClipCmd(0x0C, PseudoChrId.Self, '', '')

    def _loc_A06D(): pass

    label('loc_A06D')

    Return()

# id: 0x0004 offset: 0xA070
@scena.Code('Init')
def Init():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR034_BT1')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_A0BC',
    )

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A0C9')

    def _loc_A0BC(): pass

    label('loc_A0BC')

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_A0C9(): pass

    label('loc_A0C9')

    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'EraseEquip')
    LoadEffect(0xFFFE, 0x24, 'battle/atk034_2.eff', 0x00000000)

    Return()

# id: 0x0005 offset: 0xA138
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0006 offset: 0xA160
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0007 offset: 0xA18C
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0008 offset: 0xA198
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x0009 offset: 0xA1A8
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x000A offset: 0xA1B8
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    Return()

# id: 0x000B offset: 0xA1BC
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000C offset: 0xA1CC
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000004)

    Return()

# id: 0x000D offset: 0xA1DC
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000E offset: 0xA1EC
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000F offset: 0xA204
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    Return()

# id: 0x0010 offset: 0xA208
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xA220
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000004)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0012 offset: 0xA238
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Return()

# id: 0x0013 offset: 0xA23C
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    Return()

# id: 0x0014 offset: 0xA240
@scena.Code('AniReset')
def AniReset():
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'EraseEquip')

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

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0xA2B0
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0xA2C0
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

# id: 0x0017 offset: 0xA2D0
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0018 offset: 0xA2FC
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_A316',
    )

    Jump('loc_A344')

    def _loc_A316(): pass

    label('loc_A316')

    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_A344(): pass

    label('loc_A344')

    Return()

# id: 0x0019 offset: 0xA348
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    ModelCmd(0x0B, 0xFFFE)

    If(
        (
            (Expr.Eval, "EquipCmd(0x03, 0xFFFE, '', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)"),
            (Expr.PushLong, 0x270F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A41E',
    )

    If(
        (
            (Expr.Eval, "IsAssetLoaded('C_EQU309')"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3C5',
    )

    LoadAsset('C_EQU309')

    def _loc_A3C5(): pass

    label('loc_A3C5')

    EquipCmd(0x05, 0xFFFE, 'C_EQU309', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)

    def _loc_A41E(): pass

    label('loc_A41E')

    Return()

# id: 0x001A offset: 0xA420
@scena.Code('OnCampIn')
def OnCampIn():
    ExecExpressionWithReg(
        0x01,
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

# id: 0x001B offset: 0xA488
@scena.Code('OnCostumeIn')
def OnCostumeIn():
    ExecExpressionWithReg(
        0x01,
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
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x001C offset: 0xA4EC
@scena.Code('OnCostumeIn1')
def OnCostumeIn1():
    ExecExpressionWithReg(
        0x01,
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

# id: 0x001D offset: 0xA564
@scena.Code('OnCostumeIn2')
def OnCostumeIn2():
    ExecExpressionWithReg(
        0x01,
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

# id: 0x001E offset: 0xA5D4
@scena.Code('OnCostumeIn3')
def OnCostumeIn3():
    ExecExpressionWithReg(
        0x01,
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

# id: 0x001F offset: 0xA66C
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0020 offset: 0xA6C8
@scena.Code('AniFieldChange')
def AniFieldChange():
    ExecExpressionWithReg(
        0x01,
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

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28C8), ParamInt(0x28C9), ParamInt(0x28CA), ParamInt(0))

    Return()

# id: 0x0021 offset: 0xA704
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0022 offset: 0xA71C
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x0023 offset: 0xA734
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB05', 0.2)

    Return()

# id: 0x0024 offset: 0xA890
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB05', 0.2)

    Return()

# id: 0x0025 offset: 0xA9EC
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0026 offset: 0xA9F0
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x0027 offset: 0xA9F4
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x0028 offset: 0xA9F8
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x0029 offset: 0xA9FC
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AAAC',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA7F',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_AAA3')

    def _loc_AA7F(): pass

    label('loc_AA7F')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_AAA3(): pass

    label('loc_AAA3')

    Jump('loc_AE85')

    def _loc_AAAC(): pass

    label('loc_AAAC')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_AC54',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB05',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_AB05(): pass

    label('loc_AB05')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AB94',
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

    Jump('loc_AC4B')

    def _loc_AB94(): pass

    label('loc_AB94')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC24',
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

    Jump('loc_AC4B')

    def _loc_AC24(): pass

    label('loc_AC24')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_AC4B(): pass

    label('loc_AC4B')

    Jump('loc_AE85')

    def _loc_AC54(): pass

    label('loc_AC54')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_ACB0',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_AE85')

    def _loc_ACB0(): pass

    label('loc_ACB0')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD49',
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

    Jump('loc_AE85')

    def _loc_AD49(): pass

    label('loc_AD49')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADDB',
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

    Jump('loc_AE85')

    def _loc_ADDB(): pass

    label('loc_ADDB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE59',
    )

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_AE85')

    def _loc_AE59(): pass

    label('loc_AE59')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_AE85(): pass

    label('loc_AE85')

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002A offset: 0xAEAC
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
        'loc_AF6D',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AF3D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_AF3D(): pass

    label('loc_AF3D')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_AFE4')

    def _loc_AF6D(): pass

    label('loc_AF6D')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AFC1',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_AFC1(): pass

    label('loc_AFC1')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_AFE4(): pass

    label('loc_AFE4')

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
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002B offset: 0xB014
@scena.Code('AniBack')
def AniBack():
    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002C offset: 0xB054
@scena.Code('AniRun')
def AniRun():
    OP_80(0.2)

    ExecExpressionWithReg(
        0x01,
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
        'loc_B0B7',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B0D9')

    def _loc_B0B7(): pass

    label('loc_B0B7')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B0D9(): pass

    label('loc_B0D9')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0F8',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B0F8(): pass

    label('loc_B0F8')

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

# id: 0x002D offset: 0xB11C
@scena.Code('AniDash')
def AniDash():
    ExecExpressionWithReg(
        0x01,
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
        'loc_B17F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B1A2')

    def _loc_B17F(): pass

    label('loc_B17F')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B1A2(): pass

    label('loc_B1A2')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1C1',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B1C1(): pass

    label('loc_B1C1')

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

# id: 0x002E offset: 0xB1E4
@scena.Code('AniSitWait')
def AniSitWait():
    OP_80(0.0)
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    ReleaseEffect(0xFFFE, 0x30)
    LoadEffect(0xFFFE, 0x30, 'system/maskBox.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.4), 0xFF)

    Return()

# id: 0x002F offset: 0xB298
@scena.Code('AniWait1')
def AniWait1():
    OP_80(0.2)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0030 offset: 0xB2D8
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x01,
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
        'loc_B3A3',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B357',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B39A')

    def _loc_B357(): pass

    label('loc_B357')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B39A',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B39A(): pass

    label('loc_B39A')

    Jump('loc_B431')

    def _loc_B3A3(): pass

    label('loc_B3A3')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B3EE',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B431')

    def _loc_B3EE(): pass

    label('loc_B3EE')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B431',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B431(): pass

    label('loc_B431')

    OP_3F(PseudoChrId.Self, 0x00000000)
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0031 offset: 0xB450
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
        'loc_B4AE',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B597')

    def _loc_B4AE(): pass

    label('loc_B4AE')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_B539',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_B597')

    def _loc_B539(): pass

    label('loc_B539')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B597(): pass

    label('loc_B597')

    Return()

# id: 0x0032 offset: 0xB598
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xB5D4
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
        'loc_B62D',
    )

    Sleep(500)

    Jump('loc_B639')

    def _loc_B62D(): pass

    label('loc_B62D')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_B639(): pass

    label('loc_B639')

    ExecExpressionWithReg(
        0x01,
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

# id: 0x0034 offset: 0xB670
@scena.Code('AniIdle')
def AniIdle():
    ExecExpressionWithReg(
        0x01,
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
        'loc_B705',
    )

    OP_3B(0x32, ParamInt(0x291C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_B75A')

    def _loc_B705(): pass

    label('loc_B705')

    OP_3B(0x32, ParamInt(0x291D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_B75A(): pass

    label('loc_B75A')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#66wE#156w9#86w0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0035 offset: 0xB7F4
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk034_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x27, 'battle/atk034_3.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_B86E',
    )

    LoadEffect(0xFFFE, 0x25, 'battle/atk034_a0.eff', 0x00000000)

    def _loc_B86E(): pass

    label('loc_B86E')

    Return()

# id: 0x0036 offset: 0xB870
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x27)
    ReleaseEffect(0xFFFE, 0x25)

    Return()

# id: 0x0037 offset: 0xB88C
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
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    EffectCmd(0x17, 0xFFFE, 0x07, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0027), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x07)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28CD), ParamInt(0x28CE), ParamInt(0x28CF), ParamInt(0))
    Sleep(500)

    CameraCmd(0x0A, 0.0, 0.05, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x108B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    CameraCmd(0x0A, 0.15, 0.15, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_AD(0x01, 0x01)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0038 offset: 0xBAFC
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
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'open_s', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Call(ScriptId.Current, 'SpringOff')
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 3.33333, 5.03333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 3.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR034', ScriptId.Sound2, ParamInt(0x0014))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28D0), ParamInt(0x28D1), ParamInt(0), ParamInt(0))
    Sleep(400)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 5.06667, 6.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(333)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x0039 offset: 0xBDFC
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

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003A offset: 0xBEBC
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x003B offset: 0xBEF0
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
    Sleep(533)

    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x003C offset: 0xBF9C
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x003D offset: 0xBFC8
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x003E offset: 0xBFE0
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C09E',
    )

    LoadEffect(0xFFFE, 0x22, 'battle/atk034_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/cr034_19_0.eff', 0x00000000)
    Call(ScriptId.Current, 'AniDetachEQU309')

    Jump('loc_C0E2')

    def _loc_C09E(): pass

    label('loc_C09E')

    LoadEffect(0xFFFE, 0x22, 'battle/atk034_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/cr034_00_1.eff', 0x00000000)

    def _loc_C0E2(): pass

    label('loc_C0E2')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000023, ParamStr('NODE_CENTER'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x03)

    Return()

# id: 0x003F offset: 0xC138
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x0040 offset: 0xC150
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
    Sleep(433)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C23C',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x296A), ParamInt(0x297D), ParamInt(0), ParamInt(0))

    Jump('loc_C25C')

    def _loc_C23C(): pass

    label('loc_C23C')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28CD), ParamInt(0x28E2), ParamInt(0), ParamInt(0))

    def _loc_C25C(): pass

    label('loc_C25C')

    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)

    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)

    Return()

# id: 0x0041 offset: 0xC36C
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_C40A',
    )

    ChrSetPhysicsFlags(0x0BCC, 0x00000080)
    OP_3B(0x32, ParamInt(0x293A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    OP_3B(0x39, 0xFFFE)
    ChrClearPhysicsFlags(0x0BCC, 0x00000080)

    Jump('loc_C654')

    def _loc_C40A(): pass

    label('loc_C40A')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C480',
    )

    OP_3B(0x32, ParamInt(0x28F3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C654')

    def _loc_C480(): pass

    label('loc_C480')

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
        'loc_C514',
    )

    OP_3B(0x32, ParamInt(0x28F2), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C654')

    def _loc_C514(): pass

    label('loc_C514')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C58A',
    )

    OP_3B(0x32, ParamInt(0x28F5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C654')

    def _loc_C58A(): pass

    label('loc_C58A')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C5FF',
    )

    OP_3B(0x32, ParamInt(0x28F0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C654')

    def _loc_C5FF(): pass

    label('loc_C5FF')

    OP_3B(0x32, ParamInt(0x28F1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_C654(): pass

    label('loc_C654')

    Return()

# id: 0x0042 offset: 0xC658
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_C6DE',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C6B5',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(10600), ParamInt(0x2969), ParamInt(0), ParamInt(0))

    Jump('loc_C6D5')

    def _loc_C6B5(): pass

    label('loc_C6B5')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28CB), ParamInt(0x28CC), ParamInt(0), ParamInt(0))

    def _loc_C6D5(): pass

    label('loc_C6D5')

    Jump('loc_C747')

    def _loc_C6DE(): pass

    label('loc_C6DE')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C727',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(10600), ParamInt(0x2969), ParamInt(0), ParamInt(0))

    Jump('loc_C747')

    def _loc_C727(): pass

    label('loc_C727')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28C8), ParamInt(0x28C9), ParamInt(0x28CA), ParamInt(0))

    def _loc_C747(): pass

    label('loc_C747')

    Return()

# id: 0x0043 offset: 0xC748
@scena.Code('AniBtlChain')
def AniBtlChain():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C7C6',
    )

    OP_3B(0x32, ParamInt(0x298B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C81B')

    def _loc_C7C6(): pass

    label('loc_C7C6')

    OP_3B(0x32, ParamInt(0x28F4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_C81B(): pass

    label('loc_C81B')

    Return()

# id: 0x0044 offset: 0xC81C
@scena.Code('AniBtlWait')
def AniBtlWait():
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0045 offset: 0xC86C
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleMoveToTarget()

    Return()

# id: 0x0046 offset: 0xC8D4
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0047 offset: 0xC8FC
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C93F',
    )

    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x2987))

    Jump('loc_C959')

    def _loc_C93F(): pass

    label('loc_C93F')

    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x28EC))

    def _loc_C959(): pass

    label('loc_C959')

    Return()

# id: 0x0048 offset: 0xC95C
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_C9A0',
    )

    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x2986))

    Jump('loc_C9BB')

    def _loc_C9A0(): pass

    label('loc_C9A0')

    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x28EB))

    def _loc_C9BB(): pass

    label('loc_C9BB')

    Return()

# id: 0x0049 offset: 0xC9BC
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleMoveToTarget()
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x02)
    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(133)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB87',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_CB67',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x296A), ParamInt(0x296B), ParamInt(0x296C), ParamInt(0))

    Jump('loc_CB87')

    def _loc_CB67(): pass

    label('loc_CB67')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28CD), ParamInt(0x28CE), ParamInt(0x28CF), ParamInt(0))

    def _loc_CB87(): pass

    label('loc_CB87')

    Sleep(666)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    CameraCmd(0x09, 0.15, 0.15, 0.3)
    OP_3B(0x00, ParamInt(0x108B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(133)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(333)

    OP_3B(0x00, ParamInt(0x107B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlAttack_Damage', ScriptId.Current)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Sleep(666)

    WaitEffect(0xFFFE, 0x0022, 0x00)
    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Return()

# id: 0x004A offset: 0xCCD8
@scena.Code('AniBtlAttack_Damage')
def AniBtlAttack_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_CCE8(): pass

    label('loc_CCE8')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_CD8C',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.8), ParamFloat(0.8), ParamFloat(0.8), 0xFF)
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

    Jump('loc_CCE8')

    def _loc_CD8C(): pass

    label('loc_CD8C')

    Return()

# id: 0x004B offset: 0xCD90
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_CE0E',
    )

    OP_3B(0x32, ParamInt(0x2983), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_CE63')

    def _loc_CE0E(): pass

    label('loc_CE0E')

    OP_3B(0x32, ParamInt(0x28E8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_CE63(): pass

    label('loc_CE63')

    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x004C offset: 0xCE7C
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
        'loc_CEDD',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_CF06')

    def _loc_CEDD(): pass

    label('loc_CEDD')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_CF06(): pass

    label('loc_CF06')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0xCF14
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_CFE2',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_CFB9',
    )

    OP_3B(0x32, ParamInt(0x2981), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_CFD9')

    def _loc_CFB9(): pass

    label('loc_CFB9')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x297F), ParamInt(0x2980), ParamInt(0x2981), ParamInt(0))

    def _loc_CFD9(): pass

    label('loc_CFD9')

    Jump('loc_D087')

    def _loc_CFE2(): pass

    label('loc_CFE2')

    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_D067',
    )

    OP_3B(0x32, ParamInt(0x28E6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D087')

    def _loc_D067(): pass

    label('loc_D067')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28E4), ParamInt(0x28E5), ParamInt(0x28E6), ParamInt(0))

    def _loc_D087(): pass

    label('loc_D087')

    Return()

# id: 0x004E offset: 0xD088
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_D106',
    )

    OP_3B(0x32, ParamInt(0x2939), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D106')

    def _loc_D106(): pass

    label('loc_D106')

    Return()

# id: 0x004F offset: 0xD108
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
        'loc_D16A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_D1CE')

    def _loc_D16A(): pass

    label('loc_D16A')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_D1CE(): pass

    label('loc_D1CE')

    Return()

# id: 0x0050 offset: 0xD1D0
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0051 offset: 0xD21C
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr034_03_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr034_03_1.eff', 0x00000000)
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '4[autoM4]', '5', '7', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraCmd(0x0A, 0.01, 0.01, 0.0, 100, 5000, 100, 0, 0, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x8F39), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F78), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.28, 0.2, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 0.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCmd(0x0B, 0x03, 42.0, 0x0000)
    CameraCmd(0x0C, 0x03, 0.0, -0.15, 0.0, 8000)
    CameraCmd(0x11, 0x03, -5.0, 22.0, 0.0, 0x1F40, 0x01)
    CameraSetHeight(0x03, -0.5, 1000)
    CameraCmd(0x0B, 0x03, 38.0, 0x0BB8)
    BattleCmd(0x4B, 0x1F40, 0x03)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_D527',
    )

    OP_3B(0x32, ParamInt(0x2938), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_D527')

    def _loc_D527(): pass

    label('loc_D527')

    OP_3B(0xFF, 0.3, 0.4, 0.6)
    Sleep(533)

    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)
    Sleep(133)

    OP_6C(PseudoChrId.Self, 0.25, 0xFFFFFFFF)
    Sleep(100)

    OP_6C(PseudoChrId.Self, 0.7, 0xFFFFFFFF)
    OP_5E(0x00, 0x0002, 0.5, 200, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(33)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '2', '', '0', '2', '0')
    CameraCmd(0x0A, 0.008, 0.008, 0.0, 1000, 1000, 500, 0, 0, 0x00)
    Sleep(133)

    OP_5E(0x00, 0x0002, 0.5, 200, 400, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(333)

    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.0, 1.22, 0.2, 150)
    CameraRotateByTarget(0xFFFE, '', 0x02, 9.0, 0.0, 6.0, 150, 0x01)
    CameraSetDistance(0x02, 2.5, 150)
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(1), ParamInt(0x0064), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.6, 0.8, 0.25)
    CameraCmd(0x0B, 0x03, 45.0, 0x0064)
    Sleep(133)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.01, 0.1, 0.0, 100, 300, 100, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x8FA8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(133)

    CameraSetHeight(0x03, 2.25, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    CameraCmd(0x11, 0x00, 0.0, 30.0, 0.0, 0x2710, 0x01)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(1333)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x0052 offset: 0xD888
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x0053 offset: 0xD8A4
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
        'loc_DAA6',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.5, 0xFFFFFFFF)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_DA62',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0xDD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D98F',
    )

    OP_3B(0x32, ParamInt(0x293C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_DA62')

    def _loc_D98F(): pass

    label('loc_D98F')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_DA0D',
    )

    OP_3B(0x32, ParamInt(0x2982), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_DA62')

    def _loc_DA0D(): pass

    label('loc_DA0D')

    OP_3B(0x32, ParamInt(0x28E7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_DA62(): pass

    label('loc_DA62')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Jump('loc_DBD4')

    def _loc_DAA6(): pass

    label('loc_DAA6')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_DB4B',
    )

    OP_3B(0x32, ParamInt(0x2982), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_DBA0')

    def _loc_DB4B(): pass

    label('loc_DB4B')

    OP_3B(0x32, ParamInt(0x28E7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_DBA0(): pass

    label('loc_DBA0')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_DBD4(): pass

    label('loc_DBD4')

    Call(ScriptId.Current, 'AniBtlDead_ResetHair')

    Return()

# id: 0x0054 offset: 0xDBF4
@scena.Code('AniBtlAria')
def AniBtlAria():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_DC94',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x44C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC61',
    )

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x2937), ParamInt(0), ParamFloat(-1), ParamFloat(0))

    Jump('loc_DC8B')

    def _loc_DC61(): pass

    label('loc_DC61')

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x297B), ParamInt(0x297C), ParamFloat(-1), ParamFloat(0))

    def _loc_DC8B(): pass

    label('loc_DC8B')

    Jump('loc_DCBE')

    def _loc_DC94(): pass

    label('loc_DC94')

    Call(ScriptId.BtlCom, 'AniBtlAria', ParamInt(0x28E0), ParamInt(0x28E1), ParamFloat(-1), ParamFloat(0))

    def _loc_DCBE(): pass

    label('loc_DCBE')

    Return()

# id: 0x0055 offset: 0xDCC0
@scena.Code('AniBtlArts')
def AniBtlArts():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_DF3E',
    )

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x18),
            Expr.Equ,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x19),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x1A),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x1B),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x27),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x29),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2B),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2C),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x36),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x37),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x38),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x39),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x46),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x47),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x48),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x53),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x55),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x62),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x63),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x71),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x73),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x7E),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x84),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x7F),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x85),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_DF0A',
    )

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0x297D), ParamInt(0x297D), ParamStr('NODE_L_HAND'))

    Jump('loc_DF35')

    def _loc_DF0A(): pass

    label('loc_DF0A')

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0x297D), ParamInt(0x297E), ParamStr('NODE_L_HAND'))

    def _loc_DF35(): pass

    label('loc_DF35')

    Jump('loc_E193')

    def _loc_DF3E(): pass

    label('loc_DF3E')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x18),
            Expr.Equ,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x19),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x1A),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x1B),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x27),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x29),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2B),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x2C),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x36),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x37),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x38),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x39),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x46),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x47),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x48),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x53),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x55),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x62),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x63),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x71),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x73),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x7E),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x84),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x7F),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0B)"),
            (Expr.PushLong, 0x85),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_E168',
    )

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0x28E2), ParamInt(0x28E2), ParamStr('NODE_L_HAND'))

    Jump('loc_E193')

    def _loc_E168(): pass

    label('loc_E168')

    Call(ScriptId.BtlCom, 'AniBtlArts', ParamInt(0x28E2), ParamInt(0x28E3), ParamStr('NODE_L_HAND'))

    def _loc_E193(): pass

    label('loc_E193')

    Return()

# id: 0x0056 offset: 0xE194
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0xDD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E1C0',
    )

    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0x293C))

    def _loc_E1C0(): pass

    label('loc_E1C0')

    Return()

# id: 0x0057 offset: 0xE1C4
@scena.Code('AniBtlFrontstep')
def AniBtlFrontstep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0058 offset: 0xE224
@scena.Code('AniBtlBackstep')
def AniBtlBackstep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0059 offset: 0xE284
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    Call(ScriptId.BtlCom, 'AniBtlBluff')

    Return()

# id: 0x005A offset: 0xE298
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, ParamInt(0x293B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x005B offset: 0xE300
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E37E',
    )

    OP_3B(0x32, ParamInt(0x2988), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E3D3')

    def _loc_E37E(): pass

    label('loc_E37E')

    OP_3B(0x32, ParamInt(0x28ED), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E3D3(): pass

    label('loc_E3D3')

    Return()

# id: 0x005C offset: 0xE3D4
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E452',
    )

    OP_3B(0x32, ParamInt(0x2989), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E4A7')

    def _loc_E452(): pass

    label('loc_E452')

    OP_3B(0x32, ParamInt(0x28EE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E4A7(): pass

    label('loc_E4A7')

    Return()

# id: 0x005D offset: 0xE4A8
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E526',
    )

    OP_3B(0x32, ParamInt(0x298A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E57B')

    def _loc_E526(): pass

    label('loc_E526')

    OP_3B(0x32, ParamInt(0x28EF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E57B(): pass

    label('loc_E57B')

    Return()

# id: 0x005E offset: 0xE57C
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E5C5',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x298C), ParamInt(0x298D), ParamInt(0), ParamInt(0))

    Jump('loc_E5E5')

    def _loc_E5C5(): pass

    label('loc_E5C5')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x28FB), ParamInt(0x28FC), ParamInt(0), ParamInt(0))

    def _loc_E5E5(): pass

    label('loc_E5E5')

    Return()

# id: 0x005F offset: 0xE5E8
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E7E0',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E782',
    )

    OP_3B(0x32, ParamInt(0x299C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E7D7')

    def _loc_E782(): pass

    label('loc_E782')

    OP_3B(0x32, ParamInt(0x290B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E7D7(): pass

    label('loc_E7D7')

    Jump('loc_EB92')

    def _loc_E7E0(): pass

    label('loc_E7E0')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E8D5',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E877',
    )

    OP_3B(0x32, ParamInt(0x299C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E8CC')

    def _loc_E877(): pass

    label('loc_E877')

    OP_3B(0x32, ParamInt(0x290B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E8CC(): pass

    label('loc_E8CC')

    Jump('loc_EB92')

    def _loc_E8D5(): pass

    label('loc_E8D5')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x3C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E9CA',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_E96C',
    )

    OP_3B(0x32, ParamInt(0x299D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E9C1')

    def _loc_E96C(): pass

    label('loc_E96C')

    OP_3B(0x32, ParamInt(0x290C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E9C1(): pass

    label('loc_E9C1')

    Jump('loc_EB92')

    def _loc_E9CA(): pass

    label('loc_E9CA')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EABF',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_EA61',
    )

    OP_3B(0x32, ParamInt(0x299D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EAB6')

    def _loc_EA61(): pass

    label('loc_EA61')

    OP_3B(0x32, ParamInt(0x290C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_EAB6(): pass

    label('loc_EAB6')

    Jump('loc_EB92')

    def _loc_EABF(): pass

    label('loc_EABF')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_EB3D',
    )

    OP_3B(0x32, ParamInt(0x298E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_EB92')

    def _loc_EB3D(): pass

    label('loc_EB3D')

    OP_3B(0x32, ParamInt(0x28FD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_EB92(): pass

    label('loc_EB92')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x02)
    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(800)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    CameraCmd(0x09, 0.15, 0.15, 0.3)
    OP_3B(0x00, ParamInt(0x108B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(133)

    Sleep(333)

    OP_3B(0x00, ParamInt(0x107B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x2A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EE46',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F12A')

    def _loc_EE46(): pass

    label('loc_EE46')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x3C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EF48',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FB), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.1), ParamFloat(1.1), ParamFloat(1.1), 0xFF)
    CameraCmd(0x09, 0.075, 0.075, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F12A')

    def _loc_EF48(): pass

    label('loc_EF48')

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F04A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.05, 0.05, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0x0001))
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F12A')

    def _loc_F04A(): pass

    label('loc_F04A')

    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, ParamInt(0x8BF0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))

    def _loc_F12A(): pass

    label('loc_F12A')

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

# id: 0x0060 offset: 0xF218
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0061 offset: 0xF25C
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0062 offset: 0xF284
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
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x02)
    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(800)

    SetChrFace(0x03, PseudoChrId.Self, '2', '2', '', '#b', '0')
    CameraCmd(0x09, 0.15, 0.15, 0.3)
    OP_3B(0x00, ParamInt(0x108B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_F517',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x29A3), ParamInt(0x29A4), ParamInt(0x29A5), ParamInt(0))

    Jump('loc_F537')

    def _loc_F517(): pass

    label('loc_F517')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x294A), ParamInt(0x294B), ParamInt(0x294C), ParamInt(0))

    def _loc_F537(): pass

    label('loc_F537')

    Sleep(133)

    Sleep(333)

    OP_3B(0x00, ParamInt(0x107B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0063 offset: 0xF69C
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0064 offset: 0xF6B4
@scena.Code('AniBtlLinkUltimateAttack')
def AniBtlLinkUltimateAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0065 offset: 0xF6CC
@scena.Code('AniBtlLinkRageCounter')
def AniBtlLinkRageCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0066 offset: 0xF6E4
@scena.Code('AniBtlLinkSuperCounter')
def AniBtlLinkSuperCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0067 offset: 0xF6FC
@scena.Code('AniBtlLinkHeavyRage')
def AniBtlLinkHeavyRage():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_F741',
    )

    Call(ScriptId.BtlCom, 'AniBtlLinkRage', ParamInt(0x299E))

    Jump('loc_F75D')

    def _loc_F741(): pass

    label('loc_F741')

    Call(ScriptId.BtlCom, 'AniBtlLinkRage', ParamInt(0x290D))

    def _loc_F75D(): pass

    label('loc_F75D')

    Return()

# id: 0x0068 offset: 0xF760
@scena.Code('AniBtlLinkSuperRage')
def AniBtlLinkSuperRage():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_F7A5',
    )

    Call(ScriptId.BtlCom, 'AniBtlLinkRage', ParamInt(0x299E))

    Jump('loc_F7C1')

    def _loc_F7A5(): pass

    label('loc_F7A5')

    Call(ScriptId.BtlCom, 'AniBtlLinkRage', ParamInt(0x290D))

    def _loc_F7C1(): pass

    label('loc_F7C1')

    Return()

# id: 0x0069 offset: 0xF7C4
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x006A offset: 0xF7E4
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x006B offset: 0xF800
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    BattleTurnChrDirection(0xFFFE, 0xFFFE, -20.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '777776', '[autoM6]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006C offset: 0xF864
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_F8D5',
    )

    OP_3B(0x32, ParamInt(0x28DF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F9A8')

    def _loc_F8D5(): pass

    label('loc_F8D5')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_F953',
    )

    OP_3B(0x32, ParamInt(0x297A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_F9A8')

    def _loc_F953(): pass

    label('loc_F953')

    OP_3B(0x32, ParamInt(0x28DE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_F9A8(): pass

    label('loc_F9A8')

    Return()

# id: 0x006D offset: 0xF9AC
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.0666667, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.4, 0xFFFFFFFF)
    Sleep(266)

    OP_6C(PseudoChrId.Self, 0.9, 0xFFFFFFFF)

    Return()

# id: 0x006E offset: 0xFA14
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x006F offset: 0xFA2C
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x0070 offset: 0xFA50
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x0071 offset: 0xFA54
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x0072 offset: 0xFA74
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x297D), ParamInt(0x297E))

    Return()

# id: 0x0073 offset: 0xFAA0
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x0074 offset: 0xFAC4
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x0075 offset: 0xFAE4
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x0076 offset: 0xFB04
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0077 offset: 0xFB40
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0078 offset: 0xFBA4
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x0079 offset: 0xFBE0
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x007A offset: 0xFC18
@scena.Code('VoiceWin_select')
def VoiceWin_select():
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
        'loc_FC57',
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_FC8C')

    def _loc_FC57(): pass

    label('loc_FC57')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_FC7F',
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_FC8C')

    def _loc_FC7F(): pass

    label('loc_FC7F')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FC8C(): pass

    label('loc_FC8C')

    Return()

# id: 0x007B offset: 0xFC90
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FD00',
    )

    OP_3B(0x32, ParamInt(0x28F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FDC5')

    def _loc_FD00(): pass

    label('loc_FD00')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FD70',
    )

    OP_3B(0x32, ParamInt(0x28F6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FDC5')

    def _loc_FD70(): pass

    label('loc_FD70')

    OP_3B(0x32, ParamInt(0x28F7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_FDC5(): pass

    label('loc_FDC5')

    Return()

# id: 0x007C offset: 0xFDC8
@scena.Code('AniBtlWin')
def AniBtlWin():
    CameraCmd(0x00)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x12)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FFC2',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '227#46wB#126w7776[autoE6]', '4[autoM4]', '0[autoB0]', '#b', '0')
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_0', ScriptId.Current)
    Sleep(800)

    OP_3B(0x32, ParamInt(0x28F8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8C3D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_3B(0x39, 0xFFFE)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(800)

    Jump('loc_10087')

    def _loc_FFC2(): pass

    label('loc_FFC2')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, 'A#196w9#136wA', '2[autoM2]', '0[autoB0]', '#b', '0')
    CreateThread(PseudoChrId.Self, 0x02, '_Lambda_1', ScriptId.Current)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28F6), ParamInt(0x28F7), ParamInt(0), ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(800)

    def _loc_10087(): pass

    label('loc_10087')

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)

    Return()

# id: 0x007D offset: 0x100EC
@scena.Code('_Lambda_0')
def _Lambda_0():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.15, 1.46, 0.05, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 8.61, -18.71, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.58, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.13, 1.51, 0.07, 2933)
    CameraRotateByTarget(0xFFFE, '', 0x03, -11.19, 30.44, 0.0, 2933, 0x01)
    CameraSetDistance(0x03, 0.93, 2933)
    BattleCmd(0x4B, 0x0B75, 0x03)
    Sleep(2933)

    Return()

# id: 0x007E offset: 0x10190
@scena.Code('_Lambda_1')
def _Lambda_1():
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.11, 1.39, 0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.67, -25.12, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.41, 0)
    CameraCmd(0x0B, 0x03, 42.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.09, 1.52, 0.1, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.66, 27.33, 0.0, 3000, 0x01)
    CameraSetDistance(0x03, 0.94, 3000)
    BattleCmd(0x4B, 0x0BB8, 0x03)
    Sleep(3000)

    Return()

# id: 0x007F offset: 0x10234
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '23A#146w3#76w0[autoE0]', '228[autoM8]', '0[autoB0]', '#b', '0')
    Sleep(800)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0080 offset: 0x10330
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'DefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '23A#146w3#76w0[autoE0]', '228[autoM8]', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x28F9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(800)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN1a', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0081 offset: 0x10488
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0082 offset: 0x104C8
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_END', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEvYareyare', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEvYareyare')
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x0083 offset: 0x10550
@scena.Code('AniBtlWinWait_END')
def AniBtlWinWait_END():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x0084 offset: 0x1055C
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    SetEndhookFunction('AniBtlWin_eraseEquip_END', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.4, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '3332#80w33332[autoE2]', '0#44w4[autoM4]', '5#193w0[autoB0]', '#b', '0')
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x00000103, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(166)

    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.7), ParamInt(0x0064), 0.0, ParamFloat(-5), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '', '', '', '#b', '0')
    Sleep(100)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    WaitEffect(0xFFFE, 0x0024, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x0085 offset: 0x10714
@scena.Code('AniBtlWin_eraseEquip_END')
def AniBtlWin_eraseEquip_END():
    EffectCmd(0x0F, 0xFFFE, 0x0024, 0x01)

    Return()

# id: 0x0086 offset: 0x10720
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1078D',
    )

    OP_3B(0x32, ParamInt(0x28FA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_107E2')

    def _loc_1078D(): pass

    label('loc_1078D')

    OP_3B(0x32, ParamInt(0x28FA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_107E2(): pass

    label('loc_107E2')

    Return()

# id: 0x0087 offset: 0x107E4
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtLevelUp_Call', ScriptId.Current)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.28, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x11, 0x03, 5.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.4, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '22332222#80w3#36w2[autoE2]', '4[autoM4]', '0005#166w0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x28FA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x00000103, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(266)

    OP_3B(0x00, ParamInt(6100), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0088 offset: 0x10A60
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x0089 offset: 0x10A84
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B1A',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cr034_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr034_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr034_00_13.eff', 0x00000000)

    def _loc_10B1A(): pass

    label('loc_10B1A')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B95',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cr034_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr034_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr034_00_3.eff', 0x00000000)

    def _loc_10B95(): pass

    label('loc_10B95')

    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.2, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 1.0, 10.0, -5.0, 0, 0x01)
    CameraSetDistance(0x00, 3.6, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.85, -0.2, 1000)
    CameraCmd(0x11, 0x03, -2.0, -45.0, -6.0, 0x03E8, 0x01)
    CameraSetDistance(0x03, 2.2, 1000)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0[autoM0]', '5', '7', '0')
    OP_6C(PseudoChrId.Self, 0.4, 0xFFFFFFFF)
    OP_43(0xFF, 0, 0x0000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_10D2E',
    )

    OP_3B(0x32, ParamInt(0x296F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10D83')

    def _loc_10D2E(): pass

    label('loc_10D2E')

    OP_3B(0x32, ParamInt(0x28D2), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10D83(): pass

    label('loc_10D83')

    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x107D), ParamFloat(0.8), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1048), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    CameraSetPosByTarget(0x02, 0xFFFE, '', -0.0, 0.95, -0.3, 1600)
    CameraCmd(0x11, 0x02, -2.0, -50.0, 0.0, 0x0640, 0x01)
    CameraSetDistance(0x02, 2.0, 1600)
    Sleep(500)

    OP_4E(0.4, 0.0, 0x03, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '', '2', '6', '0')
    Sleep(200)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    Sleep(100)

    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(166)

    OP_3B(0xFF, 0.6, 0.8, 0.15)
    OP_3B(0x00, ParamInt(0x10CE), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10D9), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    CameraCmd(0x0A, 0.35, 0.1, 0.0, 100, 500, 100, 0, 0, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '', '', '0', '6', '0')
    Sleep(66)

    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 1.75, 0.0, 700)
    CameraCmd(0x11, 0x03, -5.0, -105.0, 0.0, 0x02BC, 0x01)
    CameraSetDistance(0x03, 6.2, 700)
    Sleep(300)

    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFF3, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x10BB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(1.5), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1800), ParamInt(300), 0x0000, 0x0708, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x07, 0x00BF)
    CameraCmd(0x09, 0.125, 0.125, 1.0)
    CameraSetPosByTarget(0x00, 0xFFFB, '', 0.0, 2.5, 0.0, 500)
    CameraSetDistance(0x03, 9.2, 500)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(300)

    CameraSetPosByTarget(0x00, 0xFFFB, '', 0.0, 3.2, 0.0, 2500)
    CameraCmd(0x11, 0x00, -2.0, -15.0, 0.0, 0x09C4, 0x01)
    CameraSetDistance(0x03, 11.75, 2500)
    CameraCmd(0x09, 0.055, 0.055, 3.0)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft00_Damage', ScriptId.Current)
    Sleep(800)

    OP_5E(0x01, 0x04B0)
    Sleep(1300)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.Current, 'SpringOn')
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x38)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')

    Return()

# id: 0x008A offset: 0x11374
@scena.Code('AniBtlCraft00_Damage')
def AniBtlCraft00_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_11384(): pass

    label('loc_11384')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_11428',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
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

    Jump('loc_11384')

    def _loc_11428(): pass

    label('loc_11428')

    Return()

# id: 0x008B offset: 0x1142C
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_114C2',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cr034_01_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr034_01_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr034_01_12.eff', 0x00000000)

    def _loc_114C2(): pass

    label('loc_114C2')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1153D',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cr034_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr034_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/cr034_01_2.eff', 0x00000000)

    def _loc_1153D(): pass

    label('loc_1153D')

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, 'G', '4[autoM4]', '6', 'G', '0')
    Sleep(1)

    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.01, 1.4, 0.27, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 26.0, 12.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_11673',
    )

    OP_3B(0x32, ParamInt(0x2970), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_116C8')

    def _loc_11673(): pass

    label('loc_11673')

    OP_3B(0x32, ParamInt(0x28D3), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_116C8(): pass

    label('loc_116C8')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x107D), ParamFloat(0.8), ParamInt(200), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1048), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.05, 1.23, -0.67, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.0, -2.0, 9.0, 700, 0x01)
    CameraSetDistance(0x03, 2.0, 700)
    CameraCmd(0x0B, 0x03, 40.0, 0x02BC)
    Sleep(333)

    SetChrFace(0x03, PseudoChrId.Self, '7', '', '5', '7', '0')
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '6', '', '3', '6', '0')
    CameraSetHeight(0x03, -2.0, 3000)
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '6', '', '8', '6', '0')
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '', '8', '6', '0')
    Sleep(66)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.06, 0.92, 1.98, 500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, 11.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 7.4, 500)
    Sleep(33)

    CameraCmd(0x09, 0.09, 0.125, 1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.5, 0.7, 0.15)
    Sleep(200)

    ReleaseEffect(0xFFFE, 0x38)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    Sleep(166)

    CameraSetHeight(0x00, 5.0, 5000)
    CameraCmd(0x0B, 0x03, 35.0, 0x1388)
    OP_3B(0x00, ParamInt(0x14BF), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10E8), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_4E(0.1, 0.0, 0x03, 0x00)
    Sleep(66)

    OP_4E(0.25, 0.0, 0x03, 0x00)
    Sleep(33)

    OP_4E(0.5, 0.0, 0x03, 0x00)
    Sleep(33)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    Sleep(166)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.2, 1.4, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 2.0, 160.0, 0.0, 0, 0x01)
    CameraSetDistance(0x00, 4.3, 0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.4, 1.2, 2.0, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, 170.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x00, 3.3, 3000)
    CameraCmd(0x09, 0.055, 0.075, 2.0)
    OP_43(0xFF, 0, 0x0000)
    OP_5E(0x00, 0x0002, 0.4, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(350)

    OP_5E(0x01, 0x0258)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft01_Damage', ScriptId.Current)
    Sleep(1000)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    SetChrFace(0x03, PseudoChrId.Self, 'P', '0', '', '#b', '0')

    Return()

# id: 0x008C offset: 0x11CD4
@scena.Code('AniBtlCraft01_Damage')
def AniBtlCraft01_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_11CE4(): pass

    label('loc_11CE4')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_11D88',
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

    Jump('loc_11CE4')

    def _loc_11D88(): pass

    label('loc_11D88')

    Return()

# id: 0x008D offset: 0x11D8C
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr034_20_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr034_20_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr034_03_0.eff', 0x00000000)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6#36w3#120w6[autoE6]', '2#36w9#120w7', '0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x28D7), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR034', ScriptId.Sound2, ParamInt(0x0082))
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetDistance(0x03, 3.1, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.0, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, 0.0, 0.0, 0, 0x01)
    CameraSetHeight(0x03, -1.5, 3000)
    CameraCmd(0x0C, 0x03, 0.0, 0.3, 0.0, 3000)
    BattleCmd(0x4B, 0x0000, 0x03)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(500)

    OP_6C(PseudoChrId.Self, 0.25, 0xFFFFFFFF)
    Sleep(1333)

    OP_6C(PseudoChrId.Self, 0.7, 0xFFFFFFFF)
    OP_5E(0x00, 0x0002, 0.5, 200, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(166)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    Sleep(0)

    OP_5E(0x00, 0x0002, 0.5, 30, 1200, 500, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraSetHeight(0x03, 1.0, 500)
    OP_3B(0xFF, 0.7, 0.9, 0.8)
    OP_3B(0x32, ParamInt(0x28D8), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x0A, 0.15, 0.1, 0.01, 30, 1400, 700, 0, 0, 0x00)
    OP_43(0x03, 250, 1.0, 0)
    Sleep(400)

    CameraSetHeight(0x03, 0.75, 3000)
    Call(ScriptId.Current, 'AniChangeHair')
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    OP_43(0x67, 500, 1.0, 0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '7', '0', '#b', '0')
    Sleep(2000)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x008E offset: 0x12208
@scena.Code('AniBtlResetHair')
def AniBtlResetHair():
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    Sleep(1)

    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_CENTER', 0.0, 0.2, 0.0, 0)
    CameraCmd(0x11, 0x03, 0.0, 5.0, 0.0, 0x0BB8, 0x01)
    CameraSetHeight(0x03, 1.0, 3000)
    OP_43(0xFF, 0, 0x0000)
    Sleep(400)

    OP_43(0x03, 400, 1.0, 0)
    OP_3B(0x00, ParamInt(0x1018), ParamFloat(1), ParamInt(400), 0.0, ParamInt(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0xFF, 0, 0x0000)
    Call(ScriptId.Current, 'AniResetHair')
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(100)

    OP_43(0x67, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    CameraCmd(0x07, 0x00BF)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x008F offset: 0x1239C
@scena.Code('AniChangeHair')
def AniChangeHair():
    SetScenaFlags(ScenaFlag(0x009E, 5, 0x4F5))

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR034_C00')

    If(
        (
            (Expr.Eval, "EquipCmd(0x03, 0xFFFE, '', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)"),
            (Expr.PushLong, 0x270F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1245E',
    )

    DeatchEquip(0xFFFE, 'C_EQU309', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x00)

    def _loc_1245E(): pass

    label('loc_1245E')

    Call(ScriptId.Current, 'AniBtlLoadBeastAnimeclip')
    BattleCmd(0xC6, 0xFFFE)
    Sleep(0)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    LoadEffect(0xFFFE, 0x22, 'battle/atk034_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/cr034_19_0.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000023, ParamStr('NODE_CENTER'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x03)

    Return()

# id: 0x0090 offset: 0x125B4
@scena.Code('AniResetHair')
def AniResetHair():
    ClearScenaFlags(ScenaFlag(0x009E, 5, 0x4F5))

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AnimeClipChangeSkin(PseudoChrId.Self, '')

    If(
        (
            (Expr.Eval, "EquipCmd(0x03, 0xFFFE, '', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)"),
            (Expr.PushLong, 0x270F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12676',
    )

    EquipCmd(0x05, 0xFFFE, 'C_EQU309', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)

    def _loc_12676(): pass

    label('loc_12676')

    Call(ScriptId.Current, 'AniBtlLoadBeastAnimeclip')
    BattleCmd(0xC6, 0xFFFE)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    LoadEffect(0xFFFE, 0x22, 'battle/atk034_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/cr034_00_1.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000023, ParamStr('NODE_CENTER'), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x03)

    Return()

# id: 0x0091 offset: 0x12770
@scena.Code('AniBtlDead_ResetHair')
def AniBtlDead_ResetHair():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x009E, 5, 0x4F5)),
            Expr.Return,
        ),
        'loc_12850',
    )

    SetEndhookFunction('AniResetHair', 0x000B)
    OP_3B(0x00, ParamInt(0x1018), ParamFloat(1), ParamInt(400), 0.0, ParamInt(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0x03, 0, 1.0, 0)
    OP_43(0x67, 600, 1.0, 0)
    Call(ScriptId.Current, 'AniResetHair')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetEndhookFunction('', 0x000B)
    OP_43(0xFF, 0, 0x0000)

    def _loc_12850(): pass

    label('loc_12850')

    Return()

# id: 0x0092 offset: 0x12854
@scena.Code('AniBtlLoadBeastAnimeclip')
def AniBtlLoadBeastAnimeclip():
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR034_BT1')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR034_EV')

    Return()

# id: 0x0093 offset: 0x12880
@scena.Code('AniBtlCraft12')
def AniBtlCraft12():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr034_12_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr034_12_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr034_12_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr034_12_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr034_12_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/cr034_12_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/cr034_12_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/cr034_12_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/cr034_12_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'system/maskBox.eff', 0x00000000)
    BattleCreateChrDummy(0xFFFE, 0x00000000)
    LoadEffect(0x0B86, 0x3A, 'battle/cr034_12_10.eff', 0x00000000)
    LoadEffect(0x0B86, 0x3B, 'battle/cr034_12_10.eff', 0x00000000)
    LoadEffect(0x0B86, 0x3C, 'battle/cr034_12_10.eff', 0x00000000)
    LoadEffect(0x0B86, 0x3D, 'battle/cr034_12_10.eff', 0x00000000)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B86, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTargetsIterInit(0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    Sleep(1)

    SetChrFace(0x03, PseudoChrId.Self, '6', '4[autoM4]', '0', '6', '0')
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.06, 1.05, 0.22, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 12.0, -40.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 3.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.06, 1.05, 0.22, 2800)
    CameraRotateByTarget(0xFFFE, '', 0x03, 31.0, -95.0, 4.0, 2800, 0x01)
    CameraSetHeight(0x03, -1.25, 2000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.17), ParamFloat(1.45), ParamFloat(0.725), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(933)

    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.02, 1.39, 0.85, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 12.0, -150.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetHeight(0x03, -0.5, 2400)
    Sleep(1000)

    OP_3B(0x00, ParamInt(0x10FE), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x107B), ParamFloat(1.3), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1333)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(33)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.05, 1.46, 0.78, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -166.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCmd(0x0B, 0x03, 33.1, 0x0000)
    SetChrFace(0x03, PseudoChrId.Self, '2', '4[autoM4]', '0', '2', '0')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_12F4F',
    )

    OP_3B(0x32, ParamInt(0x2971), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_12FA4')

    def _loc_12F4F(): pass

    label('loc_12F4F')

    OP_3B(0x32, ParamInt(0x28D4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12FA4(): pass

    label('loc_12FA4')

    Sleep(333)

    CameraCmd(0x0A, 0.01, 0.01, 0.0, 100, 400, 100, 0, 0, 0x00)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.22), ParamFloat(1.4), ParamFloat(0.625), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_3B(0x00, ParamInt(0x1054), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.6, 0.2)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.191), ParamFloat(1.354), ParamFloat(2.378), 0.0, 0.0, 0.0, ParamFloat(0.264), ParamFloat(0.891), ParamFloat(2.676), 0xFF)
    Sleep(266)

    Sleep(600)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.12, 1.44, 0.78, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -100.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.2, 0)
    CameraCmd(0x0B, 0x03, 35.0, 0x0000)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft12_Equip1', ScriptId.Current)
    CameraCmd(0x0A, 0.1, 0.05, 0.0, 100, 250, 100, 0, 0, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.5, 0.6, 0.2)
    Sleep(333)

    EffectCmd(0x0E, 0xFFFE, 0x02, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '4[autoM4]', '5', '7', '0')
    Sleep(333)

    CameraCmd(0x0A, 0.25, 0.05, 0.0, 100, 250, 100, 0, 0, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.08, 1.68, -0.23, 600)
    CameraRotateByTarget(0xFFFE, '', 0x03, -19.0, -7.0, 0.0, 600, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCmd(0x0B, 0x03, 45.0, 0x0000)
    OP_3B(0x00, ParamInt(0x8F07), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.7, 0.5)
    Sleep(866)

    SetChrFace(0x03, PseudoChrId.Self, '6', '4[autoM4]', '1', '6', '0')
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x05)
    Sleep(66)

    CameraCmd(0x0A, 0.15, 0.15, 0.0, 100, 200, 100, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x8F78), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F71), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0002, 0.35, 100, 300, 150, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.5, 0.75, -0.01, 400)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, -12.0, 7.0, 400, 0x01)
    CameraSetDistance(0x03, 2.0, 400)
    CameraCmd(0x0B, 0x03, 50.2, 0x0190)
    OP_3B(0xFF, 0.5, 0.6, 0.2)
    Sleep(100)

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft12_Equip1_Detach', ScriptId.Current)
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft12_Equip2', ScriptId.Current)
    Sleep(133)

    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.5, 0.75, -0.01, 6000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, -10.0, 3.0, 6000, 0x01)
    CameraSetDistance(0x03, 2.8, 6000)
    CameraCmd(0x0B, 0x03, 50.2, 0x1770)
    ReleaseEffect(0xFFFE, 0x3A)
    Sleep(1266)

    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    OP_43(0x65, 400, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.0, 1.4, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 15.0, 15.0, 0.0, 0, 0x01)
    CameraSetHeight(0x03, 1.25, 5000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '1', '2', '0')
    Sleep(666)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_13790',
    )

    OP_3B(0x32, ParamInt(0x2972), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_137E5')

    def _loc_13790(): pass

    label('loc_13790')

    OP_3B(0x32, ParamInt(0x28D5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_137E5(): pass

    label('loc_137E5')

    Sleep(433)

    OP_3B(0x00, ParamInt(0x8F07), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(133)

    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.175, 6.0, 15.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    OP_5E(0x00, 0x0002, 0.35, 200, 500, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    OP_3B(0x00, ParamInt(0x10F0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1398B(): pass

    label('loc_1398B')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_13B71',
    )

    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13A02',
    )

    PlayEffect(0x0B86, ParamInt(0x003A), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0C)

    def _loc_13A02(): pass

    label('loc_13A02')

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13A5B',
    )

    PlayEffect(0x0B86, ParamInt(0x003B), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0D)

    def _loc_13A5B(): pass

    label('loc_13A5B')

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13AB4',
    )

    PlayEffect(0x0B86, ParamInt(0x003C), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0E)

    def _loc_13AB4(): pass

    label('loc_13AB4')

    If(
        (
            (Expr.PushReg, 0x9),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13B0D',
    )

    PlayEffect(0x0B86, ParamInt(0x003D), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0F)

    def _loc_13B0D(): pass

    label('loc_13B0D')

    BattleSetChrPosAsync(0x0B86, 0xFFFB, 0.0, 0.0, 0.0, 6.0, 0x00, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    BattleCmd(0x3F, 0x0B86)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x09,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_1398B')

    def _loc_13B71(): pass

    label('loc_13B71')

    Sleep(333)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.16, 1.43, -0.14, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 21.0, -27.0, 1.0, 0, 0x01)
    CameraSetDistance(0x03, 7.2, 0)
    CameraCmd(0x0B, 0x03, 52.0, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(266)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    OP_3B(0x00, ParamInt(0x8F27), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F01), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1064), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetHeight(0x03, -5.05, 1100)
    CameraCmd(0x0B, 0x03, 37.0, 0x0960)
    OP_5E(0x00, 0x0002, 0.25, 200, 750, 400, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    EffectCmd(0x0E, 0x0B86, 0x0C, 0x00)
    EffectCmd(0x0E, 0x0B86, 0x0D, 0x00)
    EffectCmd(0x0E, 0x0B86, 0x0E, 0x00)
    EffectCmd(0x0E, 0x0B86, 0x0F, 0x00)
    BattleCmd(0x3C, 0xFFFE, 0xFFF9, 7.5, 0x02BC)
    OP_4E(0.6, 0.0, 0x03, 0x00)
    Sleep(100)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    OP_43(0x65, 350, 1.0, 0)
    OP_43(0xFE, 0)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_13EA7',
    )

    OP_3B(0x32, ParamInt(0x2973), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_13EFC')

    def _loc_13EA7(): pass

    label('loc_13EA7')

    OP_3B(0x32, ParamInt(0x28D6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_13EFC(): pass

    label('loc_13EFC')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.21, 1.1, -0.58, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 19.0, -49.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCmd(0x0B, 0x03, 45.0, 0x0000)
    CameraSetHeight(0x02, -0.65, 1700)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.21, 1.1, -0.58, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 8.0, -43.0, 0.0, 1000, 0x01)
    Sleep(266)

    SetChrFace(0x03, PseudoChrId.Self, '6', '5', '3', '6', '0')
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_6C(PseudoChrId.Self, 0.35, 0xFFFFFFFF)
    Sleep(433)

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.265, 1.01, -0.62, 800)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.0, -4.0, 6.0, 800, 0x01)
    CameraSetDistance(0x03, 1.65, 1100)
    CameraCmd(0x0B, 0x03, 45.0, 0x0320)
    Sleep(100)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '5', '6', '6', '0')
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.75), ParamFloat(0.5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0B)
    Sleep(166)

    LoadEffect(0xFFFE, 0x30, 'battle/cr034_12_11.eff', 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    EffectCmd(0x0E, 0xFFFE, 0x0B, 0x00)
    Sleep(33)

    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.02, 0.52, -0.1, 500)
    CameraRotateByTarget(0xFFFE, '', 0x02, 17.0, 11.0, 4.0, 500, 0x01)
    CameraSetDistance(0x02, 10.5, 500)
    CameraCmd(0x0B, 0x02, 50.2, 0x01F4)
    CameraCmd(0x0A, 0.3, 0.2, 0.0, 100, 500, 100, 0, 0, 0x00)
    OP_3B(0xFF, 0.7, 0.9, 0.25)

    ExecExpressionWithReg(
        0x0C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_141EF(): pass

    label('loc_141EF')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1423A',
    )

    If(
        (
            (Expr.GetChrWork, 0xFFFB, 0x3),
            (Expr.PushLong, 0x1B58),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1421C',
    )

    ExecExpressionWithReg(
        0x0C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1421C(): pass

    label('loc_1421C')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_141EF')

    def _loc_1423A(): pass

    label('loc_1423A')

    EffectCmd(0x0E, 0xFFFE, 0x04, 0x00)

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_142A6',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(-0.5), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.75), ParamFloat(1.75), ParamFloat(1.75), 0x07)

    Jump('loc_142FF')

    def _loc_142A6(): pass

    label('loc_142A6')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_142FF',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x07)

    def _loc_142FF(): pass

    label('loc_142FF')

    OP_3B(0x00, ParamInt(0x8F07), ParamFloat(0.9), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x8F51), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Sleep(333)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.3, 6.0, 15.0)
    BattleTargetsIterInit(0x05)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_143FA(): pass

    label('loc_143FA')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_144F0',
    )

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(2.5), ParamFloat(0.5), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Target, 0x00000009, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
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

    Jump('loc_143FA')

    def _loc_144F0(): pass

    label('loc_144F0')

    OP_4E(0.3, 0.0, 0x03, 0x00)
    CameraCmd(0x0A, 0.05, 0.05, 0.0, 100, 5000, 100, 0, 0, 0x00)
    Sleep(200)

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1457D',
    )

    BattleCmd(0x47)
    CameraSetHeight(0x03, 3.0, 5000)
    CameraCmd(0x0B, 0x03, 52.0, 0x1388)
    CameraCmd(0x11, 0x00, -6.0, 80.0, 0.0, 0x2710, 0x01)
    BattleCmd(0x4B, 0x2710, 0x00)

    Jump('loc_145CE')

    def _loc_1457D(): pass

    label('loc_1457D')

    If(
        (
            (Expr.PushReg, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_145CE',
    )

    BattleCmd(0x47)
    CameraSetHeight(0x03, 3.0, 5000)
    CameraCmd(0x0B, 0x03, 52.0, 0x1388)
    CameraCmd(0x11, 0x00, -6.0, 80.0, 0.0, 0x2710, 0x01)
    BattleCmd(0x4B, 0x2710, 0x00)

    def _loc_145CE(): pass

    label('loc_145CE')

    Sleep(333)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    OP_43(0x00, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x00FF)
    BattleDeleteChrDummy()
    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlCraft12_Equip2_Detach', ScriptId.Current)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    WaitForThreadExit(PseudoChrId.Self, 0x03)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    Return()

# id: 0x0094 offset: 0x146C0
@scena.Code('AniBtlCraft12_Equip1')
def AniBtlCraft12_Equip1():
    LoadAsset('C_EQU091')
    AttachEquip(0xFFFE, 'C_EQU091', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'noaura', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0095 offset: 0x14758
@scena.Code('AniBtlCraft12_Equip1_Detach')
def AniBtlCraft12_Equip1_Detach():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0096 offset: 0x147AC
@scena.Code('AniBtlCraft12_Equip2')
def AniBtlCraft12_Equip2():
    LoadAsset('C_EQU091_00')
    AttachEquip(0xFFFE, 'C_EQU091_00', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0097 offset: 0x1481C
@scena.Code('AniBtlCraft12_Equip2_Detach')
def AniBtlCraft12_Equip2_Detach():
    ReleaseAsset('C_EQU091_00')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0098 offset: 0x14874
@scena.Code('AniBtlCraft12_Damage')
def AniBtlCraft12_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_14884(): pass

    label('loc_14884')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_14928',
    )

    BattleDamage(0xFFF9, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFF9, ParamFloat(10), ParamFloat(0.5), 0x01)
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

    Jump('loc_14884')

    def _loc_14928(): pass

    label('loc_14928')

    Return()

# id: 0x0099 offset: 0x1492C
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR034_SC1')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14AAF',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cic034_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc034_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc034_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc034_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc034_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc034_00_14.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc034_00_15.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3F, 'battle/sc034_00_16.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc034_00_17.eff', 0x00000000)

    def _loc_14AAF(): pass

    label('loc_14AAF')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14BFA',
    )

    LoadEffect(0xFFFE, 0x38, 'battle/cic034_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc034_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc034_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc034_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc034_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc034_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc034_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3F, 'battle/sc034_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc034_00_7.eff', 0x00000000)

    def _loc_14BFA(): pass

    label('loc_14BFA')

    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000001, 0x000005DC, 0x00000000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    SetChrPos(PseudoChrId.Self, 0.0, 0.0, 60.0, 0.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(60), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlTurnToThis')
    BattleTurnChrDirection(0xFFFE, 0xFFFF, 180.0, -1.0)
    SetChrFace(0x03, PseudoChrId.Self, '6', '4[autoM4]', '0', '6', '0')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Sleep(0)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.1, 1.25, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x00, 0.0, -6.0, 2.0, 0, 0x01)
    CameraSetDistance(0x00, 2.2, 0)
    OP_C0(0x0001, 0x3FD33333)
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.2, 1.35, 0.05, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x03, -12.0, -13.0, 5.0, 1200, 0x01)
    CameraSetDistance(0x03, 1.8, 1200)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_14EBE',
    )

    OP_3B(0x32, ParamInt(0x2976), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_14F13')

    def _loc_14EBE(): pass

    label('loc_14EBE')

    OP_3B(0x32, ParamInt(0x28D9), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_14F13(): pass

    label('loc_14F13')

    Sleep(700)

    Sleep(400)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8F2E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '7', '', '5', '7', '0')
    Sleep(366)

    SetChrFace(0x03, PseudoChrId.Self, '6', '', '2', '6', '0')
    Sleep(700)

    OP_3B(0x00, ParamInt(0x8F2F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0000, 0.8, 150, 250, 200, 1.0, 0xF016, '', 0.0, 1.0, 0.0)
    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.24, 0.96, 0.11, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x02, -3.0, -16.0, 6.0, 1000, 0x01)
    CameraSetDistance(0x02, 1.6, 1000)
    SetChrFace(0x03, PseudoChrId.Self, '', '', '0', '', '0')
    Sleep(900)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.0, 1.0, 600)
    CameraCmd(0x11, 0x03, -1.0, -2.0, 1.0, 0x0258, 0x01)
    CameraSetDistance(0x03, 2.0, 600)
    OP_3B(0xFF, 0.5, 0.6, 0.7)
    CameraCmd(0x09, 0.0125, 0.016, 0.4)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(0.9), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(0.6), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1000), ParamInt(300), 0x0000, 0x03E8, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(100)

    CameraCmd(0x09, 0.02, 0.03, 0.7)
    Sleep(400)

    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.25, 1.3, 1.5, 1800)
    CameraCmd(0x11, 0x00, 2.0, -10.0, 1.0, 0x0708, 0x01)
    CameraSetDistance(0x00, 2.9, 1800)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_07', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.5, 1.1, 0.0, 600)
    CameraRotateByTarget(0xFFFE, '', 0x03, -3.0, -55.0, -5.0, 600, 0x01)
    CameraSetDistance(0x03, 1.0, 600)
    Sleep(266)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.6, 1.2, 0.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -4.0, -60.0, -5.0, 1000, 0x01)
    CameraSetDistance(0x00, 2.0, 1000)
    Sleep(66)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.35, 2.75, 800)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, -31.0, -10.0, 800, 0x01)
    CameraSetDistance(0x03, 4.6, 800)
    CameraCmd(0x0B, 0x03, 55.0, 0x0708)
    Sleep(200)

    Sleep(233)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_15493',
    )

    OP_3B(0x32, ParamInt(0x2977), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_154E8')

    def _loc_15493(): pass

    label('loc_15493')

    OP_3B(0x32, ParamInt(0x28DB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_154E8(): pass

    label('loc_154E8')

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    CameraCmd(0x09, 0.07, 0.07, 0.5)
    OP_3B(0x00, ParamInt(0x0FAB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_08', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x00, 0xFFFE, '', 0.2, 1.35, 4.0, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, -10.0, -25.0, -12.0, 1000, 0x01)
    CameraSetDistance(0x00, 5.6, 1000)
    Sleep(150)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.4, 1.35, 0.55, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, 210.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.0, 0)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.1, 1.35, 0.85, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x00, 0.0, 205.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x00, 4.0, 1000)
    EffectCmd(0x0F, 0xFFFE, 0x003B, 0x01)
    Sleep(100)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_09', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -1.4, 1.35, 4.0, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 190.0, 0.0, 1200, 0x01)
    CameraSetDistance(0x03, 6.0, 1200)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x0FAB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.07, 0.07, 0.5)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_10', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.05, -0.3, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 5.0, 60.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.0, 0)
    EffectCmd(0x0F, 0xFFFE, 0x003B, 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_11', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.35, 4.2, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 40.0, 0.0, 1200, 0x01)
    CameraSetDistance(0x03, 6.0, 1200)
    Sleep(100)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.07, 0.07, 0.5)
    OP_3B(0x00, ParamInt(0x0FAB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_12', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 2.05, 25.0, 0)
    CameraRotate(0x03, 7.0, -10.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 14.0, 0)
    EffectCmd(0x0F, 0xFFFE, 0x003B, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x003A, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPos(0x03, 0.0, 0.1, 1.0, 2100)
    CameraRotate(0x03, 2.0, 2.0, 5.0, 2100, 0x01)
    CameraSetDistance(0x03, 10.6, 2200)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1063), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x09, 0.06, 0.06, 2.0)
    Sleep(1900)

    CameraCmd(0x09, 0.35, 0.35, 1.0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-6), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x10BB), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    CameraCmd(0x09, 0.275, 0.275, 4.0)
    OP_5E(0x00, 0x0002, 0.8, 0, 0, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, ParamInt(0x10E8), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetPos(0x03, 0.0, 2.0, 0.0, 500)
    CameraRotate(0x03, 1.0, 11.0, 5.0, 500, 0x01)
    CameraSetDistance(0x03, 9.0, 500)
    Sleep(500)

    CameraSetPos(0x03, 0.0, 3.0, 0.0, 2500)
    CameraRotate(0x03, 2.0, 45.0, 5.0, 2500, 0x01)
    CameraSetDistance(0x03, 11.0, 2500)
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft01_Damage', ScriptId.Current)
    Sleep(1000)

    OP_5E(0x01, 0x0514)
    Sleep(1300)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ReleaseEffect(0xFFFE, 0x3B)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_15E5C',
    )

    OP_3B(0x32, ParamInt(0x2978), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_15EB1')

    def _loc_15E5C(): pass

    label('loc_15E5C')

    OP_3B(0x32, ParamInt(0x28DC), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_15EB1(): pass

    label('loc_15EB1')

    CreateThread(PseudoChrId.Self, 0x01, 'AniBtlSCraft00_Mouth02', ScriptId.Current)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.0, 0.45, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -15.0, -10.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.325, 1.2, 0.35, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x03, -15.0, -13.0, -4.0, 1500, 0x01)
    CameraSetDistance(0x03, 1.1, 1500)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_43(0xFF, 0, 0x0000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_HAND'), ParamFloat(0.2), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x107B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.35, 1.25, 0.3, 650)
    CameraRotateByTarget(0xFFFE, '', 0x00, -15.5, -15.0, -4.5, 650, 0x01)
    CameraSetDistance(0x00, 1.0, 650)
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.2, 1.4, -0.95, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, -15.0, 80.0, -4.0, 700, 0x01)
    CameraSetDistance(0x03, 1.45, 700)
    OP_5E(0x00, 0x0000, 0.75, 100, 500, 150, 0.5, 0xFFFB, '', 0.0, 1.0, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x0FC2), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_15', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.2, 1.4, -1.15, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x00, -15.0, 85.0, -4.0, 1200, 0x01)
    CameraSetDistance(0x00, 1.75, 1200)
    Sleep(600)

    OP_3B(0x00, ParamInt(0x1067), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.0, -0.75, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -15.0, -145.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.2, 1.25, -1.15, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -16.0, -150.0, -4.0, 1000, 0x01)
    CameraSetDistance(0x03, 1.45, 1000)
    Sleep(1000)

    CameraSetPosByTarget(0x00, 0xFFFE, '', -0.2, 1.28, -1.2, 1600)
    CameraRotateByTarget(0xFFFE, '', 0x00, -17.0, -152.0, -5.0, 1600, 0x01)
    CameraSetDistance(0x00, 1.0, 2000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), PseudoChrId.Self, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1600)

    Sleep(400)

    WaitForThreadExit(PseudoChrId.Self, 0x01)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR034_C00')"),
            Expr.Return,
        ),
        'loc_164C4',
    )

    OP_3B(0x32, ParamInt(0x2979), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_16519')

    def _loc_164C4(): pass

    label('loc_164C4')

    OP_3B(0x32, ParamInt(0x28DD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_16519(): pass

    label('loc_16519')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_16', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    OP_5E(0x00, 0x0003, 0.8, 150, 250, 200, 1.0, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraSetPosByTarget(0x02, 0xFFFE, '', -0.01, 1.03, 1.26, 300)
    CameraRotateByTarget(0xFFFE, '', 0x02, -3.0, -161.0, -4.0, 300, 0x01)
    CameraSetDistance(0x02, 3.2, 300)
    Sleep(233)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.55), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x01, ParamInt(0x1012), ParamInt(0x0064), 0xFFFF)
    OP_3B(0x00, ParamInt(0x10C6), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1066), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.7, 0.9, 0.2)
    Sleep(220)

    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.6, 1.25, 5.2, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.0, -170.0, -5.0, 2000, 0x01)
    CameraSetDistance(0x03, 5.5, 2000)
    Sleep(1000)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    EffectCmd(0x0F, 0xFFFE, 0x003B, 0x01)
    CameraCmd(0x00)
    CameraSetPos(0x03, 1.0, 4.0, 29.0, 0)
    CameraRotate(0x03, -5.0, -120.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 3.4, 0)
    CameraCmd(0x0B, 0x03, 38.0, 0x0000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(4), ParamFloat(30), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x11A4), ParamFloat(1), ParamInt(1000), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(400), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_17', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPos(0x03, -1.0, 4.0, 30.7, 1000)
    CameraRotate(0x03, -2.0, -105.0, -3.5, 1000, 0x01)
    CameraSetDistance(0x03, 3.4, 1000)
    OP_43(0xFF, 0, 0x0000)
    Sleep(1000)

    CameraSetDistance(0x00, 5.4, 2000)
    CameraRotate(0x00, 3.0, -95.0, -3.5, 2000, 0x01)
    Sleep(300)

    OP_3B(0x00, ParamInt(0x1034), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    OP_3B(0x00, ParamInt(0x10BC), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraSetDistance(0x00, 4.4, 2000)
    Sleep(1000)

    CameraSetDistance(0x03, 8.4, 2000)
    CameraCmd(0x0B, 0x03, 56.0, 0x07D0)
    OP_5E(0x00, 0x0002, 0.75, 2000, 3000, 200, 1.0, 0xF016, '', 0.0, 1.0, 0.0)
    Sleep(1300)

    OP_3B(0x00, ParamInt(0x1033), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x07, 0x00BF)
    OP_43(0x65, 300, 1.0, 0)
    OP_43(0xFE, 0)
    OP_5E(0x01, 0x00C8)
    CameraCmd(0x00)
    CameraSetPos(0x03, 0.0, 2.0, 6.0, 0)
    CameraRotate(0x03, -2.5, 190.0, -10.0, 0, 0x01)
    CameraSetDistance(0x03, 12.0, 0)
    CameraSetPos(0x03, 0.0, 2.0, -1.0, 3000)
    CameraRotate(0x03, -2.5, 180.0, -10.0, 3000, 0x01)
    CameraCmd(0x09, 0.05, 0.065, 3.0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(150)

    OP_4E(0.5, 0.0, 0x03, 0x00)
    Sleep(100)

    Sleep(200)

    Sleep(100)

    OP_4E(1.0, 0.0, 0x03, 0x00)
    Sleep(50)

    OP_5E(0x00, 0x0002, 0.75, 0, 500, 0, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(800)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFFF, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.35, 0.35, 0.8)
    OP_3B(0x01, ParamInt(0x11A4), ParamInt(300), 0xFFFF)
    OP_3B(0x00, ParamInt(0x10BB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    StopEffect(0xFFFE, 0x02, 0x01)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPos(0x00, 0.0, 0.0, 0.0, 300)
    CameraRotate(0x00, 5.5, -65.0, -4.0, 300, 0x01)
    CameraSetDistance(0x00, 9.0, 300)
    Sleep(300)

    CreateThread(PseudoChrId.Self, 0x02, 'AniBtlSCraft01_Damage', ScriptId.Current)
    CameraCmd(0x09, 0.095, 0.095, 3.0)
    OP_3B(0x00, ParamInt(0x113A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetDistance(0x03, 8.0, 2500)
    Sleep(1000)

    Sleep(1500)

    CameraSetDistance(0x03, 18.0, 2000)
    CameraCmd(0x09, 0.5, 0.5, 3.0)
    OP_3B(0x00, ParamInt(0x0FC5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x1146), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x8F4B), ParamFloat(2), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(800)

    OP_43(0x03, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)
    CameraCmd(0x0B, 0x03, 38.0, 0x0000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000080)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000200)
    ChrClearPhysicsFlags(0xFFF9, 0x00000080)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000200)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    Call(ScriptId.Current, 'SpringOn')
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_5E(0x01, 0x0064)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x009A offset: 0x17038
@scena.Code('AniBtlSCraft01_Damage')
def AniBtlSCraft01_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_17048(): pass

    label('loc_17048')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1708E',
    )

    BattleDamageAnime(0xFFFB, ParamFloat(0.5), ParamFloat(0.8), 0x01)
    Sleep(50)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_17048')

    def _loc_1708E(): pass

    label('loc_1708E')

    Return()

# id: 0x009B offset: 0x17090
@scena.Code('AniBtlSCraft00_Mouth01')
def AniBtlSCraft00_Mouth01():
    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')
    Sleep(1350)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'C', '', '#b', '0')
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(180)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')

    Return()

# id: 0x009C offset: 0x1724C
@scena.Code('AniBtlSCraft00_Mouth02')
def AniBtlSCraft00_Mouth02():
    SetChrFace(0x03, PseudoChrId.Self, '7', '9', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '7', 'C', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '7', '2', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '6', '3', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '1', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '8', '', '#b', '0')
    Sleep(120)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'A', '', '#b', '0')

    Return()

# id: 0x009D offset: 0x1738C
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x009E offset: 0x173F8
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x009F offset: 0x1744C
@scena.Code('AniDisarm')
def AniDisarm():
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00A0 offset: 0x174A4
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A1 offset: 0x174EC
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A2 offset: 0x1753C
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A3 offset: 0x175C8
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A4 offset: 0x17648
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A5 offset: 0x176D8
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A6 offset: 0x1770C
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A7 offset: 0x17774
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A8 offset: 0x177C8
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A9 offset: 0x177FC
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AA offset: 0x1786C
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00AB offset: 0x178F0
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AC offset: 0x1797C
@scena.Code('AniEvDeada')
def AniEvDeada():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AD offset: 0x179D4
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AE offset: 0x17A2C
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00AF offset: 0x17A8C
@scena.Code('AniEvCraft00_01')
def AniEvCraft00_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B0 offset: 0x17B00
@scena.Code('AniEvCraft01_01')
def AniEvCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B1 offset: 0x17B74
@scena.Code('AniEvSCraft01_01')
def AniEvSCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B2 offset: 0x17BB0
@scena.Code('AniEvSCraft01_02')
def AniEvSCraft01_02():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B3 offset: 0x17C48
@scena.Code('AniEvSCraft01_04')
def AniEvSCraft01_04():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_05', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B4 offset: 0x17CE0
@scena.Code('AniEvSCraft01_06')
def AniEvSCraft01_06():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_06', 0x01, 0x01, 0x00, 0x01, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B5 offset: 0x17D1C
@scena.Code('AniEvSCraft01_07')
def AniEvSCraft01_07():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_08', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B6 offset: 0x17D94
@scena.Code('AniEvSCraft01_09')
def AniEvSCraft01_09():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_10', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B7 offset: 0x17E0C
@scena.Code('AniEvSCraft01_11')
def AniEvSCraft01_11():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_12', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B8 offset: 0x17E84
@scena.Code('AniEvSCraft01_13')
def AniEvSCraft01_13():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_13', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B9 offset: 0x17EC0
@scena.Code('AniEvSCraft01_14')
def AniEvSCraft01_14():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_15', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BA offset: 0x17F38
@scena.Code('AniEvSCraft01_16')
def AniEvSCraft01_16():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_16', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT01_17', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BB offset: 0x17FD0
@scena.Code('AniEvAttachMainWeapon')
def AniEvAttachMainWeapon():
    Call(ScriptId.Current, 'AniEvDetachMainWeapon')
    LoadAsset('C_EQU091')
    AttachEquip(0xFFFE, 'C_EQU091', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x00BC offset: 0x18058
@scena.Code('AniEvDetachMainWeapon')
def AniEvDetachMainWeapon():
    ReleaseAsset('C_EQU091')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x00BD offset: 0x180A4
@scena.Code('AniEvCraft12')
def AniEvCraft12():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_00', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BE offset: 0x18114
@scena.Code('AniEvCraft12_1')
def AniEvCraft12_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    ReleaseEffect(0xFFFE, 0x30)
    LoadEffect(0xFFFE, 0x30, 'system/maskBox.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.191), ParamFloat(1.354), ParamFloat(2.378), 0.0, 0.0, 0.0, ParamFloat(0.264), ParamFloat(0.891), ParamFloat(2.676), 0xFF)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(833)

    Call(ScriptId.Current, 'AniEvAttachMainWeapon')
    Sleep(1666)

    ReleaseEffect(0xFFFE, 0x30)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BF offset: 0x18228
@scena.Code('AniEvCraft12_1b')
def AniEvCraft12_1b():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_01', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 143.0, 144.133, -1.0, 0x00, 0x00)
    Sleep(833)

    Sleep(1666)

    ReleaseEffect(0xFFFE, 0x30)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C0 offset: 0x1827C
@scena.Code('AniEvCraft12_1a')
def AniEvCraft12_1a():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_01a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C1 offset: 0x182B8
@scena.Code('AniEvCraft12_2')
def AniEvCraft12_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C2 offset: 0x18350
@scena.Code('AniEvCraft12_2a')
def AniEvCraft12_2a():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_02a', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C3 offset: 0x183AC
@scena.Code('AniEvCraft12_3')
def AniEvCraft12_3():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C4 offset: 0x18444
@scena.Code('AniEvCraft12_4')
def AniEvCraft12_4():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT12_04a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C5 offset: 0x184DC
@scena.Code('AniEvUdegumi')
def AniEvUdegumi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_185AD',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_18763')

    def _loc_185AD(): pass

    label('loc_185AD')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_186CA',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMI', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_1866F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_186C1')

    def _loc_1866F(): pass

    label('loc_1866F')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_186C1(): pass

    label('loc_186C1')

    Jump('loc_18763')

    def _loc_186CA(): pass

    label('loc_186CA')

    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_UDEGUMIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_18763(): pass

    label('loc_18763')

    Return()

# id: 0x00C6 offset: 0x18764
@scena.Code('AniEvByeWalk')
def AniEvByeWalk():
    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "IsAnimeClipEqualTo(PseudoChrId.Self, 'WALK')"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_187BF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, '_end_loop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_187BF(): pass

    label('loc_187BF')

    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_BYE_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x00C7 offset: 0x18844
@scena.Code('AniEvRyoteKosi')
def AniEvRyoteKosi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_18974',
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
        'loc_18922',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x03)

    Jump('loc_1895F')

    def _loc_18922(): pass

    label('loc_18922')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_1895F(): pass

    label('loc_1895F')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_18D91')

    def _loc_18974(): pass

    label('loc_18974')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_18C4E',
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_18B05',
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
        'loc_18AFC',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18AA4',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_18A70(): pass

    label('loc_18A70')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_18A9D',
    )

    Sleep(10)

    Jump('loc_18A70')

    def _loc_18A9D(): pass

    label('loc_18A9D')

    Sleep(300)

    def _loc_18AA4(): pass

    label('loc_18AA4')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT_U', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_18AFC(): pass

    label('loc_18AFC')

    Jump('loc_18C45')

    def _loc_18B05(): pass

    label('loc_18B05')

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
        'loc_18C45',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18BEF',
    )

    ChrSetPhysicsFlags(PseudoChrId.Self, 0x10000000)

    def _loc_18BBB(): pass

    label('loc_18BBB')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10000000),
            Expr.And,
            Expr.Return,
        ),
        'loc_18BE8',
    )

    Sleep(10)

    Jump('loc_18BBB')

    def _loc_18BE8(): pass

    label('loc_18BE8')

    Sleep(300)

    def _loc_18BEF(): pass

    label('loc_18BEF')

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_18C45(): pass

    label('loc_18C45')

    Jump('loc_18D91')

    def _loc_18C4E(): pass

    label('loc_18C4E')

    OP_80(0.4)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_18D10',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_18D91')

    def _loc_18D10(): pass

    label('loc_18D10')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_18D91(): pass

    label('loc_18D91')

    Return()

# id: 0x00C8 offset: 0x18D94
@scena.Code('AniEvRyoteKosiTeburi')
def AniEvRyoteKosiTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_80(0.4)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_18E7F',
    )

    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI_t_U', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa_U', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_18F02')

    def _loc_18E7F(): pass

    label('loc_18E7F')

    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSI_t', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTE_KOSIa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_18F02(): pass

    label('loc_18F02')

    Return()

# id: 0x00C9 offset: 0x18F04
@scena.Code('AniEv00380')
def AniEv00380():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV00380', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV00380a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CA offset: 0x18F6C
@scena.Code('AniEv03515')
def AniEv03515():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03515', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev03515a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CB offset: 0x18FD4
@scena.Code('AniEv04000')
def AniEv04000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev04000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev04000a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CC offset: 0x1905C
@scena.Code('AniEv04060')
def AniEv04060():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV04060', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV04060a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CD offset: 0x190C4
@scena.Code('AniEv04550')
def AniEv04550():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV04550', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x190F8
@scena.Code('AniEv30005')
def AniEv30005():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV30005', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(600)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV30005a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CF offset: 0x19194
@scena.Code('AniEv30065')
def AniEv30065():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV30065', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x191C8
@scena.Code('AniEv30065r')
def AniEv30065r():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30065r', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D1 offset: 0x19220
@scena.Code('AniEv30065w')
def AniEv30065w():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30065w', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D2 offset: 0x19278
@scena.Code('AniEv31030')
def AniEv31030():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV31030', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV31030a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D3 offset: 0x192E0
@scena.Code('AniEv35000')
def AniEv35000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D4 offset: 0x19368
@scena.Code('AniAttachEQU091')
def AniAttachEQU091():
    LoadAsset('C_EQU091')
    AttachEquip(0xFFFE, 'C_EQU091', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00D5 offset: 0x19400
@scena.Code('AniDetachEQU091')
def AniDetachEQU091():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU091')
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00D6 offset: 0x19454
@scena.Code('AniEv75550')
def AniEv75550():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV75550', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV75550a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D7 offset: 0x194DC
@scena.Code('AniEv75551')
def AniEv75551():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV75551', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV75551a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D8 offset: 0x19564
@scena.Code('AniEv86045')
def AniEv86045():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('ShowEquip', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV86045', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x195BC
@scena.Code('AniAttachEQU309')
def AniAttachEQU309():
    LoadAsset('C_EQU309')
    AttachEquip(0xFFFE, 'C_EQU309', 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)

    Return()

# id: 0x00DA offset: 0x19628
@scena.Code('AniDetachEQU309')
def AniDetachEQU309():
    ReleaseAsset('C_EQU309')
    DeatchEquip(0xFFFE, 'megane_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00DB offset: 0x1967C
@scena.Code('AniEv86050')
def AniEv86050():
    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV86050', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(1333)

    OP_2A(0x00, 0xFFFE, '', 'megane_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00DC offset: 0x19754
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR034_EV', 'ev35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk034_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/atk034_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk034_a0.eff', 0x00000000)

    Return()

# id: 0x00DD offset: 0x197D8
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'ev35000')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x25)

    Return()

# id: 0x00DE offset: 0x19824
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'EraseEquip')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x1988C
@scena.Code('AniCvIdle')
def AniCvIdle():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')

    ExecExpressionWithReg(
        0x01,
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
        'loc_1994F',
    )

    OP_3B(0x32, ParamInt(0x291C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_199A4')

    def _loc_1994F(): pass

    label('loc_1994F')

    OP_3B(0x32, ParamInt(0x291D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_199A4(): pass

    label('loc_199A4')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#66w3#226w0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00E0 offset: 0x19A38
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('ShowEquip', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(1333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E1 offset: 0x19B0C
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
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    EffectCmd(0x17, 0xFFFE, 0x03, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C19',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamInt(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.9), ParamFloat(0.9), ParamFloat(0.9), 0x03)

    def _loc_19C19(): pass

    label('loc_19C19')

    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_3B(0x00, ParamInt(0x108F), ParamFloat(0.8), ParamInt(0x0064), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28CD), ParamInt(0x28CE), ParamInt(0x28CF), ParamInt(0))
    Sleep(500)

    CameraCmd(0x0A, 0.0, 0.1, 1.0, 0, 100, 0, 0, 0, 0x00)
    OP_3B(0x00, ParamInt(0x108B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    OP_AD(0x01, 0x01)
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '2', '6[autoM6]', '', '#b', '0')
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00E2 offset: 0x19D80
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
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'open_s', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Call(ScriptId.Current, 'SpringOff')
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 3.33333, 5.03333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 3.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR034', ScriptId.Sound2, ParamInt(0x0014))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28D0), ParamInt(0x28D1), ParamInt(0), ParamInt(0))
    Sleep(400)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19FA5',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0.6), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_19FA5(): pass

    label('loc_19FA5')

    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(166)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 5.06667, 6.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(333)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x00E3 offset: 0x1A0A0
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(500)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00E4 offset: 0x1A180
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A1A5',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_1A1A5(): pass

    label('loc_1A1A5')

    Return()

# id: 0x00E5 offset: 0x1A1A8
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A20A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_1A20A(): pass

    label('loc_1A20A')

    Return()

# id: 0x00E6 offset: 0x1A20C
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_1A28F',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_1A372')

    def _loc_1A28F(): pass

    label('loc_1A28F')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28E0), ParamInt(0x28E1), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_1A372(): pass

    label('loc_1A372')

    Return()

# id: 0x00E7 offset: 0x1A374
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x28E2), ParamInt(0x28E3), ParamInt(0), ParamInt(0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0xF54),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A4A4',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), 0xFFE0, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    Jump('loc_1A4F6')

    def _loc_1A4A4(): pass

    label('loc_1A4A4')

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_1A4F6(): pass

    label('loc_1A4F6')

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

# id: 0x00E8 offset: 0x1A610
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_3B(0x32, ParamInt(0x28FA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.4, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3332#156w33332[autoE2]', '0#44w4[autoM4]', '5#193w0[autoB0]', '#b', '0')
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0024), PseudoChrId.Self, 0x00000103, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A802',
    )

    Sleep(266)

    OP_3B(0x00, ParamInt(6100), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '', '1944434134', '', '#b', '0')

    Jump('loc_1A886')

    def _loc_1A802(): pass

    label('loc_1A802')

    Sleep(266)

    OP_3B(0x00, ParamInt(6100), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(233)

    SetChrFace(0x03, PseudoChrId.Self, '', '1944434134', '', '#b', '0')
    Sleep(100)

    def _loc_1A886(): pass

    label('loc_1A886')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Sleep(500)

    Return()

# id: 0x00E9 offset: 0x1A8E0
@scena.AnimeClips('_OnChangeAttach')
def _OnChangeAttach():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU309',
        ),
    )

# id: 0x00EA offset: 0x1A940
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

# id: 0x00EB offset: 0x1A9C0
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028C8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028C9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CA,
            name   = '',
        ),
    )

# id: 0x00EC offset: 0x1AA70
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

# id: 0x00ED offset: 0x1AD00
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

# id: 0x00EE offset: 0x1ADD0
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

# id: 0x00EF offset: 0x1AE30
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

# id: 0x00F0 offset: 0x1AEB0
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

# id: 0x00F1 offset: 0x1AF30
@scena.AnimeClips('_AniSitWait')
def _AniSitWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'system/maskBox.eff',
        ),
    )

# id: 0x00F2 offset: 0x1AFB0
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

# id: 0x00F3 offset: 0x1B010
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

# id: 0x00F4 offset: 0x1B0E0
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

# id: 0x00F5 offset: 0x1B1E0
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

# id: 0x00F6 offset: 0x1B240
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

# id: 0x00F7 offset: 0x1B2A0
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000291C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000291D,
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

# id: 0x00F8 offset: 0x1B370
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x00F9 offset: 0x1B4C0
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D1,
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

# id: 0x00FA offset: 0x1B5E0
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
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00FB offset: 0x1B660
@scena.AnimeClips('_AniFieldAttackEndShort')
def _AniFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
    )

# id: 0x00FC offset: 0x1B6C0
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_19_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_1.eff',
        ),
    )

# id: 0x00FD offset: 0x1B790
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
            dword4 = 0x0000296A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000297D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E2,
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

# id: 0x00FE offset: 0x1B8E0
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000293A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F1,
            name   = '',
        ),
    )

# id: 0x00FF offset: 0x1BA00
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002968,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002969,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002968,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002969,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028C8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028C9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CA,
            name   = '',
        ),
    )

# id: 0x0100 offset: 0x1BBA0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000298B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F4,
            name   = '',
        ),
    )

# id: 0x0101 offset: 0x1BC20
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

# id: 0x0102 offset: 0x1BC80
@scena.AnimeClips('_AniBtlMove')
def _AniBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x0103 offset: 0x1BCE0
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x0104 offset: 0x1BD40
@scena.AnimeClips('_AniBtlAttack')
def _AniBtlAttack():
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
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000296A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000296B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000296C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107B,
            name   = '',
        ),
    )

# id: 0x0105 offset: 0x1BF30
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002983,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E8,
            name   = '',
        ),
    )

# id: 0x0106 offset: 0x1BFB0
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

# id: 0x0107 offset: 0x1C030
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002981,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000297F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002980,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002981,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E6,
            name   = '',
        ),
    )

# id: 0x0108 offset: 0x1C1A0
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002939,
            name   = '',
        ),
    )

# id: 0x0109 offset: 0x1C200
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

# id: 0x010A offset: 0x1C2B0
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

# id: 0x010B offset: 0x1C310
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
            name   = 'battle/cr034_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_03_1.eff',
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
            dword4 = 0x00008F39,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002938,
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
            dword4 = 0x00008FA8,
            name   = '',
        ),
    )

# id: 0x010C offset: 0x1C4B0
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
            dword4 = 0x0000293C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002982,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E7,
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
            dword4 = 0x00002982,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x010D offset: 0x1C650
@scena.AnimeClips('_AniBtlFrontstep')
def _AniBtlFrontstep():
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

# id: 0x010E offset: 0x1C6D0
@scena.AnimeClips('_AniBtlBackstep')
def _AniBtlBackstep():
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

# id: 0x010F offset: 0x1C750
@scena.AnimeClips('_AniBtlBluffVoice')
def _AniBtlBluffVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000293B,
            name   = '',
        ),
    )

# id: 0x0110 offset: 0x1C7B0
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002988,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028ED,
            name   = '',
        ),
    )

# id: 0x0111 offset: 0x1C830
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002989,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028EE,
            name   = '',
        ),
    )

# id: 0x0112 offset: 0x1C8B0
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000298A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028EF,
            name   = '',
        ),
    )

# id: 0x0113 offset: 0x1C930
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000298C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000298D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FC,
            name   = '',
        ),
    )

# id: 0x0114 offset: 0x1CA00
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
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
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000299C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000290B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000299C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000290B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000299D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000290C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000299D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000290C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000298E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107B,
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

# id: 0x0115 offset: 0x1CD50
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

# id: 0x0116 offset: 0x1CDB0
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

# id: 0x0117 offset: 0x1CE10
@scena.AnimeClips('_AniBtlLinkRush')
def _AniBtlLinkRush():
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
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000029A3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000029A4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000029A5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000294A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000294B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000294C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107B,
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

# id: 0x0118 offset: 0x1D050
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

# id: 0x0119 offset: 0x1D0B0
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028DF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000297A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028DE,
            name   = '',
        ),
    )

# id: 0x011A offset: 0x1D160
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

# id: 0x011B offset: 0x1D1C0
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

# id: 0x011C offset: 0x1D220
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

# id: 0x011D offset: 0x1D280
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

# id: 0x011E offset: 0x1D2E0
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F7,
            name   = '',
        ),
    )

# id: 0x011F offset: 0x1D390
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008C3D,
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1a',
        ),
    )

# id: 0x0120 offset: 0x1D500
@scena.AnimeClips('_AniBtlWin_link')
def _AniBtlWin_link():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1a',
        ),
    )

# id: 0x0121 offset: 0x1D580
@scena.AnimeClips('_AniBtlWin_burst')
def _AniBtlWin_burst():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028F9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN1a',
        ),
    )

# id: 0x0122 offset: 0x1D630
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

# id: 0x0123 offset: 0x1D690
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0124 offset: 0x1D740
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FA,
            name   = '',
        ),
    )

# id: 0x0125 offset: 0x1D7C0
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
            dword4 = 0x000028FA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000017D4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0126 offset: 0x1D890
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000296F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D2,
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
            dword4 = 0x0000107D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001048,
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
            dword4 = 0x000010D9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BB,
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
            name   = 'BTL_CRAFT00_02',
        ),
    )

# id: 0x0127 offset: 0x1DB40
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002970,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D3,
            name   = '',
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
            dword4 = 0x0000107D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001048,
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
            dword4 = 0x000014BF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_02',
        ),
    )

# id: 0x0128 offset: 0x1DDD0
@scena.AnimeClips('_AniBtlCraft03')
def _AniBtlCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_20_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_20_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D8,
            name   = '',
        ),
    )

# id: 0x0129 offset: 0x1DEF0
@scena.AnimeClips('_AniBtlResetHair')
def _AniBtlResetHair():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001018,
            name   = '',
        ),
    )

# id: 0x012A offset: 0x1DF50
@scena.AnimeClips('_AniChangeHair')
def _AniChangeHair():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_19_0.eff',
        ),
    )

# id: 0x012B offset: 0x1E000
@scena.AnimeClips('_AniBtlDead_ResetHair')
def _AniBtlDead_ResetHair():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001018,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x012C offset: 0x1E080
@scena.AnimeClips('_AniBtlCraft12')
def _AniBtlCraft12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'system/maskBox.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B86,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_00',
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
            dword4 = 0x000010FE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002971,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001054,
            name   = '',
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
            dword4 = 0x00008F78,
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
            name   = 'BTL_CRAFT12_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002972,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D5,
            name   = '',
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
            dword4 = 0x000010F0,
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
            name   = 'BTL_CRAFT12_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F27,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F01,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002973,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr034_12_11.eff',
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
            dword4 = 0x00008F51,
            name   = '',
        ),
    )

# id: 0x012D offset: 0x1E790
@scena.AnimeClips('_AniBtlCraft12_Equip1')
def _AniBtlCraft12_Equip1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU091',
        ),
    )

# id: 0x012E offset: 0x1E7F0
@scena.AnimeClips('_AniBtlCraft12_Equip2')
def _AniBtlCraft12_Equip2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU091_00',
        ),
    )

# id: 0x012F offset: 0x1E850
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic034_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_15.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_16.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_17.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic034_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc034_00_7.eff',
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
            name   = 'BTL_S_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002976,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D9,
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
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2F,
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
            dword4 = 0x00008F66,
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002977,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028DB,
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
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_09',
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
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_11',
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
            name   = 'BTL_S_CRAFT01_12',
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
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002978,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028DC,
            name   = '',
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
            dword4 = 0x0000107B,
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
            dword4 = 0x00000FC2,
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
            dword4 = 0x00001067,
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
            dword4 = 0x00002979,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028DD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_16',
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
            dword4 = 0x00001066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000011A4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_17',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001034,
            name   = '',
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
            dword4 = 0x00001033,
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
            dword4 = 0x000010BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000113A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001146,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F4B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0130 offset: 0x1F370
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

# id: 0x0131 offset: 0x1F3D0
@scena.AnimeClips('_AniDisarm')
def _AniDisarm():
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

# id: 0x0132 offset: 0x1F450
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

# id: 0x0133 offset: 0x1F4B0
@scena.AnimeClips('_AniEvBtlMove')
def _AniEvBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x0134 offset: 0x1F510
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

# id: 0x0135 offset: 0x1F590
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

# id: 0x0136 offset: 0x1F610
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

# id: 0x0137 offset: 0x1F690
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

# id: 0x0138 offset: 0x1F6F0
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

# id: 0x0139 offset: 0x1F770
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x013A offset: 0x1F7D0
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

# id: 0x013B offset: 0x1F830
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

# id: 0x013C offset: 0x1F8B0
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

# id: 0x013D offset: 0x1F930
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

# id: 0x013E offset: 0x1F9B0
@scena.AnimeClips('_AniEvDeada')
def _AniEvDeada():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x013F offset: 0x1FA10
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

# id: 0x0140 offset: 0x1FA70
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

# id: 0x0141 offset: 0x1FAF0
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

# id: 0x0142 offset: 0x1FB70
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
            name   = 'BTL_CRAFT01_02',
        ),
    )

# id: 0x0143 offset: 0x1FBF0
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

# id: 0x0144 offset: 0x1FC50
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
    )

# id: 0x0145 offset: 0x1FCD0
@scena.AnimeClips('_AniEvSCraft01_04')
def _AniEvSCraft01_04():
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

# id: 0x0146 offset: 0x1FD50
@scena.AnimeClips('_AniEvSCraft01_06')
def _AniEvSCraft01_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_06',
        ),
    )

# id: 0x0147 offset: 0x1FDB0
@scena.AnimeClips('_AniEvSCraft01_07')
def _AniEvSCraft01_07():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
    )

# id: 0x0148 offset: 0x1FE30
@scena.AnimeClips('_AniEvSCraft01_09')
def _AniEvSCraft01_09():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_09',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
    )

# id: 0x0149 offset: 0x1FEB0
@scena.AnimeClips('_AniEvSCraft01_11')
def _AniEvSCraft01_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_12',
        ),
    )

# id: 0x014A offset: 0x1FF30
@scena.AnimeClips('_AniEvSCraft01_13')
def _AniEvSCraft01_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
    )

# id: 0x014B offset: 0x1FF90
@scena.AnimeClips('_AniEvSCraft01_14')
def _AniEvSCraft01_14():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_14',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_15',
        ),
    )

# id: 0x014C offset: 0x20010
@scena.AnimeClips('_AniEvSCraft01_16')
def _AniEvSCraft01_16():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_16',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_17',
        ),
    )

# id: 0x014D offset: 0x20090
@scena.AnimeClips('_AniEvAttachMainWeapon')
def _AniEvAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU091',
        ),
    )

# id: 0x014E offset: 0x200F0
@scena.AnimeClips('_AniEvCraft12')
def _AniEvCraft12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_00',
        ),
    )

# id: 0x014F offset: 0x20150
@scena.AnimeClips('_AniEvCraft12_1')
def _AniEvCraft12_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'system/maskBox.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_01',
        ),
    )

# id: 0x0150 offset: 0x201D0
@scena.AnimeClips('_AniEvCraft12_1b')
def _AniEvCraft12_1b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_01',
        ),
    )

# id: 0x0151 offset: 0x20230
@scena.AnimeClips('_AniEvCraft12_1a')
def _AniEvCraft12_1a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_01a',
        ),
    )

# id: 0x0152 offset: 0x20290
@scena.AnimeClips('_AniEvCraft12_2')
def _AniEvCraft12_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_02a',
        ),
    )

# id: 0x0153 offset: 0x20310
@scena.AnimeClips('_AniEvCraft12_2a')
def _AniEvCraft12_2a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_02a',
        ),
    )

# id: 0x0154 offset: 0x20370
@scena.AnimeClips('_AniEvCraft12_3')
def _AniEvCraft12_3():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_03a',
        ),
    )

# id: 0x0155 offset: 0x203F0
@scena.AnimeClips('_AniEvCraft12_4')
def _AniEvCraft12_4():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT12_04a',
        ),
    )

# id: 0x0156 offset: 0x20470
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
            name   = 'WAIT',
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

# id: 0x0157 offset: 0x20630
@scena.AnimeClips('_AniEvByeWalk')
def _AniEvByeWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x0158 offset: 0x206B0
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

# id: 0x0159 offset: 0x20990
@scena.AnimeClips('_AniEvRyoteKosiTeburi')
def _AniEvRyoteKosiTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSI_t_U',
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
            name   = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_RYOTE_KOSIa',
        ),
    )

# id: 0x015A offset: 0x20A90
@scena.AnimeClips('_AniEv00380')
def _AniEv00380():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00380',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00380a',
        ),
    )

# id: 0x015B offset: 0x20B10
@scena.AnimeClips('_AniEv03515')
def _AniEv03515():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03515',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03515a',
        ),
    )

# id: 0x015C offset: 0x20B90
@scena.AnimeClips('_AniEv04000')
def _AniEv04000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev04000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev04000a',
        ),
    )

# id: 0x015D offset: 0x20C10
@scena.AnimeClips('_AniEv04060')
def _AniEv04060():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV04060',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV04060a',
        ),
    )

# id: 0x015E offset: 0x20C90
@scena.AnimeClips('_AniEv04550')
def _AniEv04550():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV04550',
        ),
    )

# id: 0x015F offset: 0x20CF0
@scena.AnimeClips('_AniEv30005')
def _AniEv30005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV30005',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV30005a',
        ),
    )

# id: 0x0160 offset: 0x20D70
@scena.AnimeClips('_AniEv30065')
def _AniEv30065():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV30065',
        ),
    )

# id: 0x0161 offset: 0x20DD0
@scena.AnimeClips('_AniEv30065r')
def _AniEv30065r():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30065r',
        ),
    )

# id: 0x0162 offset: 0x20E30
@scena.AnimeClips('_AniEv30065w')
def _AniEv30065w():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30065w',
        ),
    )

# id: 0x0163 offset: 0x20E90
@scena.AnimeClips('_AniEv31030')
def _AniEv31030():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31030',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV31030a',
        ),
    )

# id: 0x0164 offset: 0x20F10
@scena.AnimeClips('_AniEv35000')
def _AniEv35000():
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0165 offset: 0x20F90
@scena.AnimeClips('_AniAttachEQU091')
def _AniAttachEQU091():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU091',
        ),
    )

# id: 0x0166 offset: 0x20FF0
@scena.AnimeClips('_AniEv75550')
def _AniEv75550():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV75550',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV75550a',
        ),
    )

# id: 0x0167 offset: 0x21070
@scena.AnimeClips('_AniEv75551')
def _AniEv75551():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV75551',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV75551a',
        ),
    )

# id: 0x0168 offset: 0x210F0
@scena.AnimeClips('_AniEv86045')
def _AniEv86045():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV86045',
        ),
    )

# id: 0x0169 offset: 0x21150
@scena.AnimeClips('_AniAttachEQU309')
def _AniAttachEQU309():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU309',
        ),
    )

# id: 0x016A offset: 0x211B0
@scena.AnimeClips('_AniEv86050')
def _AniEv86050():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV86050',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x016B offset: 0x21230
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk034_a0.eff',
        ),
    )

# id: 0x016C offset: 0x212E0
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

# id: 0x016D offset: 0x21340
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000291C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000291D,
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

# id: 0x016E offset: 0x21410
@scena.AnimeClips('_AniCvBtlWait')
def _AniCvBtlWait():
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x016F offset: 0x21490
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028CF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0170 offset: 0x215E0
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
            dword4 = 0x000028D0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028D1,
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

# id: 0x0171 offset: 0x21700
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
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0172 offset: 0x21780
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
            dword4 = 0x000028E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x0173 offset: 0x21880
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
            dword4 = 0x000028E2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028E3,
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

# id: 0x0174 offset: 0x219D0
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000028FA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000017D4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000017D4,
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
