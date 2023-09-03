import sys
sys.path.append(r'C:\Users\hecky\AppData\Local\Temp\_MEI519402')

from Falcom.ED85.Parser.scena_writer_helper import *
try:
    import chr067_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr067.dat')

# id: 0x0000 offset: 0x22BC
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'FATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_POSE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR067_DF1',
            symbol     = 'BTL_ASSAULT01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_POWERUP_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_POWERUP_01_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_POWERUP_02_GS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR067_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR067_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'WAIT1_U',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_INORI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MEGANE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_NORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_NORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_NORIDASIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIANF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIANF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_SIANF_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
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
            asset      = 'C_CHR067_EV',
            symbol     = 'ev00150',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev00150a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev00200',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV00340',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV00340a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV02031',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV02031a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev03005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev03010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev30190',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev30190a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev30215',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev33005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev33005a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev33010',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev33010a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev51045_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev56020',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'ev56020a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV70115',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV70115a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV74310',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV79250',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV79251',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR067_EV',
            symbol     = 'EV79251a',
        ),
    )

# id: 0x0001 offset: 0xA178
@scena.Code('PreInit')
def PreInit():
    AnimeClipCmd(0x0D, PseudoChrId.Self)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 7, 0x34F)),
            Expr.Return,
        ),
        'loc_A279',
    )

    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'PRE_WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'TURN_LEFT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'TURN_RIGHT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'WAIT_D')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_C00_DF1', 'PRE_WAIT_U')

    Jump('loc_A342')

    def _loc_A279(): pass

    label('loc_A279')

    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_DF1', 'WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_DF1', 'PRE_WAIT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_DF1', 'TURN_LEFT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_DF1', 'TURN_RIGHT')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_EV', 'WAIT_D')
    AnimeClipCmd(0x0E, PseudoChrId.Self, 0x00000001, 'C_CHR067_EV', 'PRE_WAIT_U')

    def _loc_A342(): pass

    label('loc_A342')

    Return()

# id: 0x0002 offset: 0xA344
@scena.Code('Init')
def Init():
    Call(ScriptId.Current, 'PlayFakeEffect')
    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'DefaultFace')
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0003 offset: 0xA3B4
@scena.Code('PlayFakeEffect')
def PlayFakeEffect():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_A443',
    )

    LoadEffect(0xFFFE, 0x2F, 'system/shadow_chr_aura.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x002F), PseudoChrId.Self, 0x00000023, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    def _loc_A443(): pass

    label('loc_A443')

    Return()

# id: 0x0004 offset: 0xA444
@scena.Code('ReInit')
def ReInit():
    Call(ScriptId.Current, 'OnChangeAttach')
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0005 offset: 0xA46C
@scena.Code('ResetModel1')
def ResetModel1():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    Call(ScriptId.Current, 'ResetModel2')

    Return()

# id: 0x0006 offset: 0xA498
@scena.Code('ResetModel2')
def ResetModel2():
    AnimeClipChangeSkin(PseudoChrId.Self, '')

    Return()

# id: 0x0007 offset: 0xA4A4
@scena.Code('DefaultFace')
def DefaultFace():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_A4F8',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Jump('loc_A523')

    def _loc_A4F8(): pass

    label('loc_A4F8')

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    def _loc_A523(): pass

    label('loc_A523')

    Return()

# id: 0x0008 offset: 0xA524
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "ModelCmd(0x27)"),
            Expr.Return,
        ),
        'loc_A53E',
    )

    Jump('loc_A56C')

    def _loc_A53E(): pass

    label('loc_A53E')

    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_A56C(): pass

    label('loc_A56C')

    Return()

# id: 0x0009 offset: 0xA570
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x20),
            Expr.Equ,
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_A595',
    )

    ModelCmd(0x0B, 0xFFFE)

    def _loc_A595(): pass

    label('loc_A595')

    Call(ScriptId.Current, 'AniKibaOff')

    Return()

# id: 0x000A offset: 0xA5A8
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000B offset: 0xA5B8
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x000C offset: 0xA5C8
@scena.Code('Ani_BT3_Load')
def Ani_BT3_Load():
    Return()

# id: 0x000D offset: 0xA5CC
@scena.Code('Ani_SC1_Load')
def Ani_SC1_Load():
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x000E offset: 0xA5DC
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000002)

    Return()

# id: 0x000F offset: 0xA5EC
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0010 offset: 0xA604
@scena.Code('Ani_BT3_Release')
def Ani_BT3_Release():
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0011 offset: 0xA610
@scena.Code('Ani_SC1_Release')
def Ani_SC1_Release():
    AnimeClipReleaseByCatalog(PseudoChrId.Self, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0012 offset: 0xA628
@scena.Code('AniFieldAttack_Load')
def AniFieldAttack_Load():
    LoadEffect(0xFFFE, 0x22, 'battle/atk067.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/disarm067.eff', 0x00000000)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_A6C3',
    )

    LoadEffect(0xFFFE, 0x25, 'battle/atk067_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk067_a1.eff', 0x00000000)

    def _loc_A6C3(): pass

    label('loc_A6C3')

    Return()

# id: 0x0013 offset: 0xA6C4
@scena.Code('AniFieldAttack_Release')
def AniFieldAttack_Release():
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x0014 offset: 0xA6EC
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    LoadAsset('C_EQU095_C00')
    AttachEquip(0xFFFE, 'C_EQU095_C00', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x0015 offset: 0xA778
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ReleaseAsset('C_EQU095_C00')

    Return()

# id: 0x0016 offset: 0xA7C8
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

# id: 0x0017 offset: 0xA7D8
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

# id: 0x0018 offset: 0xA7E8
@scena.Code('AniReset')
def AniReset():
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0019 offset: 0xA82C
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x001A offset: 0xA844
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)

    Return()

# id: 0x001B offset: 0xA85C
@scena.Code('AniKibaOn')
def AniKibaOn():
    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5D(0xFFFE, 'Kiba', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x00, 0x01)

    Return()

# id: 0x001C offset: 0xA8A0
@scena.Code('AniKibaOff')
def AniKibaOff():
    ExecExpressionWithReg(
        0x0A,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5D(0xFFFE, 'Kiba', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0x0000, 0x00, 0x01)

    Return()

# id: 0x001D offset: 0xA8E4
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH06', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH06', 0.2)

    Return()

# id: 0x001E offset: 0xAB8C
@scena.Code('SpringOn2')
def SpringOn2():
    OP_8A(0xFE, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB05', 0.2)

    Return()

# id: 0x001F offset: 0xACF8
@scena.Code('SpringOn3')
def SpringOn3():
    OP_8A(0xFE, 0xFFFE, 'Tai01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Left_ring', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_ring', 0.2)

    Return()

# id: 0x0020 offset: 0xAD38
@scena.Code('SpringOn4')
def SpringOn4():
    OP_8A(0xFE, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH06', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightFH06', 0.2)

    Return()

# id: 0x0021 offset: 0xAE78
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH06', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH06', 0.2)

    Return()

# id: 0x0022 offset: 0xB120
@scena.Code('SpringOff2')
def SpringOff2():
    OP_8A(0xFF, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB05', 0.2)

    Return()

# id: 0x0023 offset: 0xB28C
@scena.Code('SpringOff3')
def SpringOff3():
    OP_8A(0xFF, 0xFFFE, 'Tai01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Left_ring', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_ring', 0.2)

    Return()

# id: 0x0024 offset: 0xB2CC
@scena.Code('SpringOff4')
def SpringOff4():
    OP_8A(0xFF, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH06', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightFH06', 0.2)

    Return()

# id: 0x0025 offset: 0xB40C
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0026 offset: 0xB410
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x0027 offset: 0xB414
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

# id: 0x0028 offset: 0xB47C
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
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x0029 offset: 0xB4E0
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
    SetChrAniFunction(PseudoChrId.Self, 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)

    Return()

# id: 0x002A offset: 0xB558
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

    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'OnCostumeIn2_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    Call(ScriptId.Current, 'EraseEquip')
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn2_2')

    Return()

# id: 0x002B offset: 0xB5DC
@scena.Code('OnCostumeIn2_2')
def OnCostumeIn2_2():
    OP_3B(0x32, ParamInt(0x2192), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4[autoM4]', '', '#b', '0')
    Sleep(900)

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '13434#70s134#100s4', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x002C offset: 0xB6E0
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
    OP_38(PseudoChrId.Self, 0x01, 0x00, '')
    OP_38(PseudoChrId.Self, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x002D offset: 0xB764
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    SetChrFace(0x03, PseudoChrId.Self, 'E,', '5,', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '', '4[autoM4]', '', '#b', '0')
    OP_3B(0x32, ParamInt(0x218F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, 'E', '', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', 'BBA[autoMA]', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '#20s1', '', '', '#b', '0')
    Sleep(600)

    SetChrFace(0x03, PseudoChrId.Self, '#40s0#100s0', '', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', 'A[autoMA]', '', '#b', '0')

    Return()

# id: 0x002E offset: 0xB8B4
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

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2166), ParamInt(0x2167), ParamInt(0x2168), ParamInt(0))

    Return()

# id: 0x002F offset: 0xB8F0
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
        'loc_B9E5',
    )

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B984',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnL')

    Jump('loc_B9DC')

    def _loc_B984(): pass

    label('loc_B984')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B9DC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlTurnR')

    def _loc_B9DC(): pass

    label('loc_B9DC')

    Jump('loc_BA73')

    def _loc_B9E5(): pass

    label('loc_B9E5')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BA30',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_BA73')

    def _loc_BA30(): pass

    label('loc_BA30')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_BA73',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_BA73(): pass

    label('loc_BA73')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_38(PseudoChrId.Self, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0030 offset: 0xBA94
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
        'loc_BB54',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB27',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_BB4B')

    def _loc_BB27(): pass

    label('loc_BB27')

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_BB4B(): pass

    label('loc_BB4B')

    Jump('loc_BF1B')

    def _loc_BB54(): pass

    label('loc_BB54')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_BCEA',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BBAD',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_BBAD(): pass

    label('loc_BBAD')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC33',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.15, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_BCE1')

    def _loc_BC33(): pass

    label('loc_BC33')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCBA',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_BCE1')

    def _loc_BCBA(): pass

    label('loc_BCBA')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_BCE1(): pass

    label('loc_BCE1')

    Jump('loc_BF1B')

    def _loc_BCEA(): pass

    label('loc_BCEA')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_BD46',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_BF1B')

    def _loc_BD46(): pass

    label('loc_BD46')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BDDF',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_BF1B')

    def _loc_BDDF(): pass

    label('loc_BDDF')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE71',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_BF1B')

    def _loc_BE71(): pass

    label('loc_BE71')

    If(
        (
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BEEF',
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

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_BF1B')

    def _loc_BEEF(): pass

    label('loc_BEEF')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_BF1B(): pass

    label('loc_BF1B')

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

# id: 0x0031 offset: 0xBF44
@scena.Code('AniWalk')
def AniWalk():
    Call(ScriptId.Current, 'ResetModel1')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_C026',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BFF6',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_BFF6(): pass

    label('loc_BFF6')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C09D')

    def _loc_C026(): pass

    label('loc_C026')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C07A',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.1)

    def _loc_C07A(): pass

    label('loc_C07A')

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C09D(): pass

    label('loc_C09D')

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

# id: 0x0032 offset: 0xC0CC
@scena.Code('AniBack')
def AniBack():
    ExecExpressionWithReg(
        0x07,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xC10C
@scena.Code('AniRun')
def AniRun():
    Call(ScriptId.Current, 'SpringOff2')
    SetEndhookFunction('SpringOn2', 0x000B)
    Call(ScriptId.Current, 'SpringOff4')
    SetEndhookFunction('SpringOn4', 0x000B)

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
        'loc_C1AC',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C1CE')

    def _loc_C1AC(): pass

    label('loc_C1AC')

    PlayChrAnimeClip(PseudoChrId.Self, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C1CE(): pass

    label('loc_C1CE')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C1ED',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C1ED(): pass

    label('loc_C1ED')

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

# id: 0x0034 offset: 0xC210
@scena.Code('AniDash')
def AniDash():
    Call(ScriptId.Current, 'SpringOff3')
    SetEndhookFunction('SpringOn3', 0x000B)

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
        'loc_C2AA',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_38(0x0BCC, 0x00, 0x00, 'AniBtlDash')

    Jump('loc_C2CD')

    def _loc_C2AA(): pass

    label('loc_C2AA')

    PlayChrAnimeClip(PseudoChrId.Self, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C2CD(): pass

    label('loc_C2CD')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C2EC',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_C2EC(): pass

    label('loc_C2EC')

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

# id: 0x0035 offset: 0xC310
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    ReleaseEffect(0xFFFE, 0x30)
    LoadEffect(0xFFFE, 0x30, 'system/maskBox.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.25), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.3), ParamFloat(0.4), ParamFloat(0.3), 0xFF)

    Return()

# id: 0x0036 offset: 0xC3C4
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0037 offset: 0xC3FC
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
        'loc_C45A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_C543')

    def _loc_C45A(): pass

    label('loc_C45A')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_C4E5',
    )

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_C543')

    def _loc_C4E5(): pass

    label('loc_C4E5')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_C543(): pass

    label('loc_C543')

    Return()

# id: 0x0038 offset: 0xC544
@scena.Code('AniFall')
def AniFall():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'SpringOff3')
    SetEndhookFunction('SpringOn3', 0x000B)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0039 offset: 0xC5C0
@scena.Code('AniLand')
def AniLand():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'SpringOff3')
    SetEndhookFunction('SpringOn3', 0x000B)
    OP_80(0.05)
    PlayChrAnimeClip(PseudoChrId.Self, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, PseudoChrId.Self, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_C64D',
    )

    Sleep(500)

    Jump('loc_C659')

    def _loc_C64D(): pass

    label('loc_C64D')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_C659(): pass

    label('loc_C659')

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

# id: 0x003A offset: 0xC690
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
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C7BD',
    )

    SetChrFace(0x03, PseudoChrId.Self, '01AA1G#86wD#376wHHHHGGGAH#66w10[autoE0]', '00ICEEI#56w37#356w1100CE2666CCEE226[autoM6]', '#0e0[autoB0]', '#b', '0')
    Sleep(1666)

    OP_3B(0x32, ParamInt(0x21B0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_C881')

    def _loc_C7BD(): pass

    label('loc_C7BD')

    SetChrFace(0x03, PseudoChrId.Self, '01AA1G#86wD#376wH#46wGGH#66w10[autoE0]', '00BBEEHHHBBJJ37#356w1100CE2666CCEE226[autoM6]', '#0e0[autoB0]', '#b', '0')
    OP_3B(0x32, ParamInt(0x21B1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_C881(): pass

    label('loc_C881')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x003B offset: 0xC8B4
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

    Call(ScriptId.Current, 'SpringOff3')
    SetEndhookFunction('SpringOn3', 0x000B)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.2, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', 'A[autoMA]', '', '#b', '0')
    Sleep(200)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x216B), ParamInt(0x216C), ParamInt(0x216D), ParamInt(0))
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0.074), ParamFloat(0.951), ParamFloat(0.633), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x0FB5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    OP_3B(0x00, ParamInt(0x0FBA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    Sleep(500)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '', '0', '', '#b', '0')
    Sleep(166)

    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003C offset: 0xCAFC
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
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 23.3333, 25.8, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR067', ScriptId.Sound2, ParamInt(0x0014))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x216E), ParamInt(0x216F), ParamInt(0), ParamInt(0))
    Sleep(533)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.203), ParamFloat(1.203), ParamFloat(0.237), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(500)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0xFF)
    Sleep(233)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 25.8333, 26.3333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(333)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x003D offset: 0xCE44
@scena.Code('SubAttackEnd')
def SubAttackEnd():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'DefaultFace')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(466)

    OP_AD(0x00, 0x01)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    SetChrFace(0x03, PseudoChrId.Self, '1', '0', '', '#b', '0')
    Sleep(600)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003E offset: 0xCF5C
@scena.Code('SubAttackEndEV')
def SubAttackEndEV():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(466)

    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'Left_SB_point', 0x00)
    Sleep(433)

    OP_3B(0x00, ParamInt(0x7536), ParamFloat(0.4), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x7533), ParamFloat(0.4), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(533)

    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x00)
    Sleep(33)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x003F offset: 0xD168
@scena.Code('AniSubAttackEndEV')
def AniSubAttackEndEV():
    OP_04(0x0B, 'SubAttackEndEV')

    Return()

# id: 0x0040 offset: 0xD17C
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
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.11), ParamFloat(1.79), ParamFloat(-0.032), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x10)
    Sleep(166)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(833)

    OP_3B(0x00, ParamInt(0x10B9), ParamFloat(0.6), ParamInt(0x015E), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0041 offset: 0xD328
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    EffectCmd(0x0E, 0xFFFE, 0x10, 0x00)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)

    Return()

# id: 0x0042 offset: 0xD364
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
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.11), ParamFloat(1.79), ParamFloat(-0.032), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x0064)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    Sleep(933)

    OP_3B(0x00, ParamInt(0x10B9), ParamFloat(0.6), ParamInt(0x015E), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0043 offset: 0xD4E8
@scena.Code('AniHorseVoice')
def AniHorseVoice():
    Return()

# id: 0x0044 offset: 0xD4EC
@scena.Code('AniHorseDashVoice')
def AniHorseDashVoice():
    Return()

# id: 0x0045 offset: 0xD4F0
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0046 offset: 0xD528
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0047 offset: 0xD568
@scena.Code('AniHorseRun')
def AniHorseRun():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0048 offset: 0xD5A8
@scena.Code('AniHorseDash')
def AniHorseDash():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0049 offset: 0xD5E8
@scena.Code('AniHorseStop')
def AniHorseStop():
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004A offset: 0xD628
@scena.Code('AniHorseTurnRight')
def AniHorseTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004B offset: 0xD684
@scena.Code('AniHorseTurnLeft')
def AniHorseTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004C offset: 0xD6E0
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
        'loc_D7F2',
    )

    OP_5C(0xFFFE, 0x00, 'RightArm')
    OP_5C(0xFFFE, 0x00, 'LeftArm')
    OP_5C(0xFFFE, 0x00, 'up_point')
    OP_5D(0xFFFE, 'RightArm', 0.0, 0.0, 0.0, 8.0, 9.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'LeftArm', 0.0, 0.0, 0.0, 8.0, -6.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    OP_5D(0xFFFE, 'up_point', 0.0, 0.0, -0.02, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)

    def _loc_D7F2(): pass

    label('loc_D7F2')

    OP_80(0.0)
    OP_04(0x0B, 'AniHorseRearWait')

    Return()

# id: 0x004D offset: 0xD810
@scena.Code('AniHorseRearEnd')
def AniHorseRearEnd():
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'RightArm')
    OP_5C(0xFFFE, 0x01, 'LeftArm')
    OP_5C(0xFFFE, 0x01, 'up_point')

    Return()

# id: 0x004E offset: 0xD854
@scena.Code('AniHorseRearWait')
def AniHorseRearWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0xD88C
@scena.Code('AniHorseRearWalk')
def AniHorseRearWalk():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xD8C8
@scena.Code('AniHorseRearRun')
def AniHorseRearRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0051 offset: 0xD904
@scena.Code('AniHorseRearStop')
def AniHorseRearStop():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0052 offset: 0xD968
@scena.Code('AniHorseRearTurnRight')
def AniHorseRearTurnRight():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0053 offset: 0xD9D0
@scena.Code('AniHorseRearTurnLeft')
def AniHorseRearTurnLeft():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0054 offset: 0xDA38
@scena.Code('AniHorseRearDash')
def AniHorseRearDash():
    PlayChrAnimeClip(PseudoChrId.Self, 'HORSE_REAR_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0xDA74
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
        'loc_DACF',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_BACK_END', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_DACF(): pass

    label('loc_DACF')

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

# id: 0x0056 offset: 0xDB14
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

# id: 0x0057 offset: 0xDB6C
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

# id: 0x0058 offset: 0xDBC0
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

# id: 0x0059 offset: 0xDC14
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

# id: 0x005A offset: 0xDC6C
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

# id: 0x005B offset: 0xDCC4
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

# id: 0x005C offset: 0xDD54
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

# id: 0x005D offset: 0xDDB0
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

# id: 0x005E offset: 0xDE08
@scena.Code('AniBikeRearWait')
def AniBikeRearWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0xDE54
@scena.Code('AniBikeRearRun')
def AniBikeRearRun():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0xDEA0
@scena.Code('AniBikeRearTilt')
def AniBikeRearTilt():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0061 offset: 0xDEEC
@scena.Code('AniBikeRearBack')
def AniBikeRearBack():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_BACK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0062 offset: 0xDF38
@scena.Code('AniBikeRearHandleWait')
def AniBikeRearHandleWait():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_HANDLE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0063 offset: 0xDF8C
@scena.Code('AniBikeRearTiltL')
def AniBikeRearTiltL():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_L', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0064 offset: 0xDFDC
@scena.Code('AniBikeRearTiltR')
def AniBikeRearTiltR():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_REAR_TILT_R', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0065 offset: 0xE02C
@scena.Code('AniBikeSideWait')
def AniBikeSideWait():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0066 offset: 0xE068
@scena.Code('AniBikeSideRun')
def AniBikeSideRun():
    PlayChrAnimeClip(PseudoChrId.Self, 'BIKE_SIDE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0067 offset: 0xE0A4
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_E0F8',
    )

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Jump('loc_E123')

    def _loc_E0F8(): pass

    label('loc_E0F8')

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    def _loc_E123(): pass

    label('loc_E123')

    Return()

# id: 0x0068 offset: 0xE124
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    AnimeClipChangeSkin(PseudoChrId.Self, 'PLACEHOLDER_REPLACE')
    AnimeClipLoadByCatalog(PseudoChrId.Self, 0x00000100)

    Return()

# id: 0x0069 offset: 0xE13C
@scena.Code('AniBtlInit')
def AniBtlInit():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')

    If(
        (
            (Expr.Eval, "BattleCmd(0x87)"),
            Expr.Return,
        ),
        'loc_E164',
    )

    Return()

    def _loc_E164(): pass

    label('loc_E164')

    Call(ScriptId.Current, 'AniBtlChangeChild')
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x22)
    LoadEffect(0xFFFE, 0x22, 'battle/atk067.eff', 0x00000000)
    Call(ScriptId.Current, 'PlayFakeEffect')

    Return()

# id: 0x006A offset: 0xE1D0
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    Call(ScriptId.BtlCom, 'AniBtlRelease')

    Return()

# id: 0x006B offset: 0xE1E8
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_E209',
    )

    Return()

    def _loc_E209(): pass

    label('loc_E209')

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_E28F',
    )

    OP_3B(0x32, ParamInt(0x21BB), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    OP_3B(0x39, 0xFFFE)

    Jump('loc_E4D9')

    def _loc_E28F(): pass

    label('loc_E28F')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E305',
    )

    OP_3B(0x32, ParamInt(0x218C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E4D9')

    def _loc_E305(): pass

    label('loc_E305')

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
        'loc_E399',
    )

    OP_3B(0x32, ParamInt(0x218B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E4D9')

    def _loc_E399(): pass

    label('loc_E399')

    If(
        (
            (Expr.Eval, "BattleCmd(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E40F',
    )

    OP_3B(0x32, ParamInt(0x218E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E4D9')

    def _loc_E40F(): pass

    label('loc_E40F')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E484',
    )

    OP_3B(0x32, ParamInt(0x2189), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_E4D9')

    def _loc_E484(): pass

    label('loc_E484')

    OP_3B(0x32, ParamInt(0x2189), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_E4D9(): pass

    label('loc_E4D9')

    Return()

# id: 0x006C offset: 0xE4DC
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_E519',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2169), ParamInt(0x216A), ParamInt(0), ParamInt(0))

    Jump('loc_E539')

    def _loc_E519(): pass

    label('loc_E519')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2166), ParamInt(0x2167), ParamInt(0x2168), ParamInt(0))

    def _loc_E539(): pass

    label('loc_E539')

    Return()

# id: 0x006D offset: 0xE53C
@scena.Code('AniBtlKisinReady')
def AniBtlKisinReady():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_E579',
    )

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2169), ParamInt(0x216A), ParamInt(0), ParamInt(0))

    Jump('loc_E599')

    def _loc_E579(): pass

    label('loc_E579')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2166), ParamInt(0x2167), ParamInt(0x2168), ParamInt(0))

    def _loc_E599(): pass

    label('loc_E599')

    Return()

# id: 0x006E offset: 0xE59C
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, ParamInt(0x218D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x006F offset: 0xE5F4
@scena.Code('AniBtlWait')
def AniBtlWait():
    OP_80(0.2)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0070 offset: 0xE64C
@scena.Code('AniBtlMove')
def AniBtlMove():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)

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
        'loc_E710',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)

    Jump('loc_E737')

    def _loc_E710(): pass

    label('loc_E710')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_E737(): pass

    label('loc_E737')

    BattleMoveToTarget()
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')

    Return()

# id: 0x0071 offset: 0xE750
@scena.Code('AniBtlAria')
def AniBtlAria():
    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_E7FF',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_E970')

    def _loc_E7FF(): pass

    label('loc_E7FF')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_E8FE',
    )

    Jump('loc_E91E')

    def _loc_E8FE(): pass

    label('loc_E8FE')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x2179), ParamInt(0x217A), ParamInt(0), ParamInt(0))

    def _loc_E91E(): pass

    label('loc_E91E')

    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_E970(): pass

    label('loc_E970')

    Return()

# id: 0x0072 offset: 0xE974
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

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_EA20',
    )

    Jump('loc_EA40')

    def _loc_EA20(): pass

    label('loc_EA20')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x217B), ParamInt(0x217C), ParamInt(0), ParamInt(0))

    def _loc_EA40(): pass

    label('loc_EA40')

    Sleep(800)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSb', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x0073 offset: 0xEB98
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', ParamInt(0x2184))

    Return()

# id: 0x0074 offset: 0xEBB4
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', ParamInt(0x2185))

    Return()

# id: 0x0075 offset: 0xEBD0
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(660)

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ECB9',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_EC99',
    )

    Jump('loc_ECB9')

    def _loc_EC99(): pass

    label('loc_EC99')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x216B), ParamInt(0x216C), ParamInt(0x216D), ParamInt(0))

    def _loc_ECB9(): pass

    label('loc_ECB9')

    Sleep(225)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(50)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0.074), ParamFloat(0.951), ParamFloat(0.633), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x0FB5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    OP_3B(0x00, ParamInt(0x0FBA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(450)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCmd(0x46, 0.25, 6.0, 15.0)

    def _loc_EE0A(): pass

    label('loc_EE0A')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_EEAE',
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

    Jump('loc_EE0A')

    def _loc_EEAE(): pass

    label('loc_EEAE')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'AniBtlWait')

    Return()

# id: 0x0076 offset: 0xEED0
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_EEF9',
    )

    Jump('loc_EF4E')

    def _loc_EEF9(): pass

    label('loc_EEF9')

    OP_3B(0x32, ParamInt(0x2181), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_EF4E(): pass

    label('loc_EF4E')

    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0077 offset: 0xEF64
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
        'loc_EFC5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_EFEE')

    def _loc_EFC5(): pass

    label('loc_EFC5')

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_EFEE(): pass

    label('loc_EFEE')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0078 offset: 0xEFFC
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_F025',
    )

    Jump('loc_F045')

    def _loc_F025(): pass

    label('loc_F025')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x217D), ParamInt(0x217E), ParamInt(0x217F), ParamInt(0))

    def _loc_F045(): pass

    label('loc_F045')

    Return()

# id: 0x0079 offset: 0xF048
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    OP_3B(0x32, ParamInt(0x217F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007A offset: 0xF0A0
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x007B offset: 0xF0BC
@scena.Code('AniBtlDead')
def AniBtlDead():
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_F1AA',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_F149',
    )

    Jump('loc_F1AA')

    def _loc_F149(): pass

    label('loc_F149')

    OP_3B(0x32, ParamInt(0x2180), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x34, ParamInt(0x2180))

    def _loc_F1AA(): pass

    label('loc_F1AA')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x007C offset: 0xF1E0
@scena.Code('AniBtlItem')
def AniBtlItem():
    BattleTargetsIterReset(0xFF, 0xFFFE)
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.Current, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ITEM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    SetChrFace(0x03, PseudoChrId.Self, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x217B), ParamInt(0x217C), ParamInt(0), ParamInt(0))
    Sleep(400)

    PlayEffect(PseudoChrId.Self, ParamInt(0x03F9), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B80), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x03F9)

    Return()

# id: 0x007D offset: 0xF3B0
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, ParamInt(0x2186), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007E offset: 0xF408
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, ParamInt(0x2187), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x007F offset: 0xF460
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, ParamInt(0x2188), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0080 offset: 0xF4B8
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
        'loc_F51A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_F57E')

    def _loc_F51A(): pass

    label('loc_F51A')

    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_F57E(): pass

    label('loc_F57E')

    Return()

# id: 0x0081 offset: 0xF580
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    Call(ScriptId.BtlCom, 'AniBtlEscape', ParamInt(0))

    Return()

# id: 0x0082 offset: 0xF59C
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    Call(ScriptId.BtlCom, 'AniBtlBluff')

    Return()

# id: 0x0083 offset: 0xF5B0
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, ParamInt(0x2168), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0084 offset: 0xF618
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_F659',
    )

    Call(ScriptId.BtlCom, 'AniBtlTensionMax')

    Jump('loc_FB1E')

    def _loc_F659(): pass

    label('loc_F659')

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
    OP_CE(0x0005, 0xFFFE, 'BTL_POWERUP_01_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos0', 0x00)
    OP_CE(0x0004, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    OP_CE(0x0002, 'BTL_POWERUP_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_F', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '00003', '2[autoM2]', '0[autoB0]', '#b', '0')
    WeatherCmd(3000, 2.0, 0.5, 0x0000, 0.2)
    OP_43(0xFF, 0, 0x0000)
    OP_3B(0x32, ParamInt(0x2179), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.5), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.75), ParamFloat(0.75), ParamFloat(0.75), 0xFF)
    CameraCmd(0x0A, 0.015, 0.015, 0.0, 500, 2000, 500, 0, 0, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    OP_CE(0x0002, 'BTL_POWERUP_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '225', '0[autoB0]', '#b', '0')
    Sleep(266)

    WaitEffect(0xFFFE, 0x0031, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(1), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.6), ParamFloat(0.6), ParamFloat(0.6), 0xFF)
    CameraCmd(0x0A, 0.2, 0.1, 0.0, 100, 1000, 500, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 100, 1500, 400, 0.5, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.6, 0.8, 0.4)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_CE(0x0003, 0x00)
    OP_CE(0x0001, 0x00000000, 0x00)
    BattleCmd(0x47)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(833)

    SetChrFace(0x03, PseudoChrId.Self, '2', '0', '', '#b', '0')
    WeatherCmd(3000, 0.0, 0.0, 0x0000, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))

    def _loc_FB1E(): pass

    label('loc_FB1E')

    Return()

# id: 0x0085 offset: 0xFB20
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0086 offset: 0xFB48
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    SetChrFace(0x03, PseudoChrId.Self, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0087 offset: 0xFB84
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0088 offset: 0xFBC0
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(PseudoChrId.Self, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0089 offset: 0xFC24
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)

    Return()

# id: 0x008A offset: 0xFC60
@scena.Code('AniBtlDownHill')
def AniBtlDownHill():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DOWNHILL', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008B offset: 0xFC98
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2193), ParamInt(0x2194), ParamInt(0), ParamInt(0))

    Return()

# id: 0x008C offset: 0xFCBC
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

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '6', '0', '', '#b', '0')
    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    Sleep(327)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.2), ParamFloat(0.85), ParamFloat(1.1), -60.0, -25.0, -65.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    If(
        (
            (Expr.Eval, "BattleCmd(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1E),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FEAA',
    )

    OP_3B(0x32, ParamInt(0x21A0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_FF28')

    def _loc_FEAA(): pass

    label('loc_FEAA')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_FED3',
    )

    Jump('loc_FF28')

    def _loc_FED3(): pass

    label('loc_FED3')

    OP_3B(0x32, ParamInt(0x2195), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_FF28(): pass

    label('loc_FF28')

    Sleep(225)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0.074), ParamFloat(0.951), ParamFloat(0.633), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x0FB5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    OP_3B(0x00, ParamInt(0x0FBA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(450)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, ParamFloat(0), ParamFloat(0), 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x03FA), PseudoChrId.Target, 0x0000000C, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', ParamInt(0))
    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(933)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)

    BattleCmd(0x3F, 0xFFFE)
    EffectCmd(0x12, 0xFFFE, 0x03FA)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x008D offset: 0x101D8
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
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(660)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_1032B',
    )

    Jump('loc_1034B')

    def _loc_1032B(): pass

    label('loc_1032B')

    OP_3B(0x3A, 0xFFFE, ParamInt(0x21D4), ParamInt(0x21D5), ParamInt(0x21D6), ParamInt(0))

    def _loc_1034B(): pass

    label('loc_1034B')

    Sleep(225)

    Sleep(50)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0.074), ParamFloat(0.951), ParamFloat(0.633), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    OP_3B(0x00, ParamInt(0x0FB5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    OP_3B(0x00, ParamInt(0x0FBA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(450)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    Sleep(666)

    WaitForThreadExit(PseudoChrId.Self, 0x02)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008E offset: 0x10550
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, PseudoChrId.Self, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008F offset: 0x10594
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0090 offset: 0x105BC
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x0091 offset: 0x105D4
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0092 offset: 0x105EC
@scena.Code('AniBtlLinkQuickCharge')
def AniBtlLinkQuickCharge():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x21A1), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x0093 offset: 0x10618
@scena.Code('AniBtlLinkQuickCharge2')
def AniBtlLinkQuickCharge2():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x21A1), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x0094 offset: 0x10644
@scena.Code('AniBtlLinkQuickCharge3')
def AniBtlLinkQuickCharge3():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x21A1), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x0095 offset: 0x10670
@scena.Code('AniBtlLinkQuickCharge4')
def AniBtlLinkQuickCharge4():
    Call(ScriptId.BtlCom, 'AniBtlLinkHeal', ParamInt(0x21A1), ParamStr('NODE_L_HAND'))

    Return()

# id: 0x0096 offset: 0x1069C
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x0097 offset: 0x106BC
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x0098 offset: 0x106D8
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    SetChrFace(0x03, PseudoChrId.Self, '777776', '', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 49.3333, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.1, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.25, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1333)

    Return()

# id: 0x0099 offset: 0x10760
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.Eval, "CraftCmd(0x0E, 0xFFFF)"),
            Expr.Return,
        ),
        'loc_107D1',
    )

    OP_3B(0x32, ParamInt(0x2178), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10826')

    def _loc_107D1(): pass

    label('loc_107D1')

    OP_3B(0x32, ParamInt(0x2177), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10826(): pass

    label('loc_10826')

    Return()

# id: 0x009A offset: 0x10828
@scena.Code('AniBtlValiantAttack_Start')
def AniBtlValiantAttack_Start():
    SetChrFace(0x03, PseudoChrId.Self, '6', '0[autoM0]', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009B offset: 0x1086C
@scena.Code('AniBtlValiantAttack')
def AniBtlValiantAttack():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x009C offset: 0x10884
@scena.Code('AniBtlValiantAttack_Move')
def AniBtlValiantAttack_Move():
    Call(ScriptId.BtlCom, 'AniBtlValiantAttack_Move')

    Return()

# id: 0x009D offset: 0x108A8
@scena.Code('AniBtlValiantArts_Wait')
def AniBtlValiantArts_Wait():
    Return()

# id: 0x009E offset: 0x108AC
@scena.Code('AniBtlValiantArts_Aria')
def AniBtlValiantArts_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Aria')

    Return()

# id: 0x009F offset: 0x108CC
@scena.Code('AniBtlValiantArts_Arts')
def AniBtlValiantArts_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Arts', ParamInt(0x217B), ParamInt(0x217C))

    Return()

# id: 0x00A0 offset: 0x108F8
@scena.Code('AniBtlValiantArts_Support')
def AniBtlValiantArts_Support():
    Call(ScriptId.BtlCom, 'AniBtlValiantArts_Support')

    Return()

# id: 0x00A1 offset: 0x1091C
@scena.Code('AniBtlValiantHeal_Aria')
def AniBtlValiantHeal_Aria():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Aria')

    Return()

# id: 0x00A2 offset: 0x1093C
@scena.Code('AniBtlValiantHeal_Arts')
def AniBtlValiantHeal_Arts():
    Call(ScriptId.BtlCom, 'AniBtlValiantHeal_Arts')

    Return()

# id: 0x00A3 offset: 0x1095C
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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_109A0',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_109AD')

    def _loc_109A0(): pass

    label('loc_109A0')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_109AD(): pass

    label('loc_109AD')

    Return()

# id: 0x00A4 offset: 0x109B0
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10A20',
    )

    OP_3B(0x32, ParamInt(0x218F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_10A75')

    def _loc_10A20(): pass

    label('loc_10A20')

    OP_3B(0x32, ParamInt(0x2190), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_10A75(): pass

    label('loc_10A75')

    Return()

# id: 0x00A5 offset: 0x10A78
@scena.Code('AniBtlWin')
def AniBtlWin():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.02, 1.2, 0.08, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -1.0, -28.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x02, 0xFFFE, '', -0.04, 1.1, 0.14, 2500)
    CameraRotateByTarget(0xFFFE, '', 0x02, 0.0, 8.0, 0.0, 2500, 0x01)
    CameraSetDistance(0x02, 1.5, 2500)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10CA7',
    )

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '4[autoM4]', '', '#b', '0')
    Sleep(300)

    OP_3B(0x00, ParamInt(0x1088), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    Call(ScriptId.Current, 'VoiceWin_play')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, 'E', '', '', '#b', '0')

    Jump('loc_10D52')

    def _loc_10CA7(): pass

    label('loc_10CA7')

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '8[autoM8]', '', '#b', '0')
    Sleep(300)

    OP_3B(0x00, ParamInt(0x1088), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'VoiceWin_play')
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, '2', '', '', '#b', '0')

    def _loc_10D52(): pass

    label('loc_10D52')

    CameraSetPosByTarget(0x02, 0xFFFE, '', -0.0, 1.17, 0.07, 2500)
    CameraRotateByTarget(0xFFFE, '', 0x02, -2.0, 13.0, 0.0, 2500, 0x01)
    CameraSetDistance(0x02, 1.2, 2500)
    CameraCmd(0x0B, 0x02, 40.0, 0x09C4)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10E01',
    )

    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', 'BBA[autoMA]', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '', '', '#b', '0')
    Sleep(600)

    Jump('loc_10E5D')

    def _loc_10E01(): pass

    label('loc_10E01')

    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', 'BBA[autoMA]', '', '#b', '0')
    Sleep(650)

    SetChrFace(0x03, PseudoChrId.Self, '#75s8#100s8[autoE8]', '', '', '#b', '0')
    Sleep(650)

    def _loc_10E5D(): pass

    label('loc_10E5D')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)
    Sleep(600)

    OP_43(0x65, 250, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F3D',
    )

    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', 'A[autoMA]', '', '#b', '0')

    Jump('loc_10F5F')

    def _loc_10F3D(): pass

    label('loc_10F3D')

    SetChrFace(0x03, PseudoChrId.Self, '8[autoE8]', 'A[autoMA]', '', '#b', '0')

    def _loc_10F5F(): pass

    label('loc_10F5F')

    Sleep(1000)

    Return()

# id: 0x00A6 offset: 0x10F68
@scena.Code('AniBtlWin_link')
def AniBtlWin_link():
    SetChrFace(0x03, PseudoChrId.Self, '0', '0', '', '#b', '0')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2', '8', '', '#b', '0')
    Sleep(300)

    OP_3B(0x00, ParamInt(0x1088), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(150)

    SetChrFace(0x03, PseudoChrId.Self, '1', '1', '', '#b', '0')
    Sleep(900)

    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '', '0', '', '#b', '0')
    Sleep(800)

    SetChrFace(0x03, PseudoChrId.Self, '0000110', '', '', '#b', '0')
    Sleep(1000)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '', '', '#b', '0')

    Return()

# id: 0x00A7 offset: 0x110F8
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, ParamInt(0x2191), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    OP_6C(PseudoChrId.Self, 0.8, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '', '4', '', '#b', '0')
    Sleep(300)

    OP_3B(0x00, ParamInt(0x1088), ParamFloat(0.7), ParamInt(200), 0.0, ParamFloat(-3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(300)

    SetChrFace(0x03, PseudoChrId.Self, 'E', '', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, PseudoChrId.Self, '', 'BBA[autoMA]', '', '#b', '0')
    Sleep(700)

    SetChrFace(0x03, PseudoChrId.Self, '0', '', '', '#b', '0')
    Sleep(600)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0[autoE0]', 'A[autoMA]', '0[autoB0]', '#b', '0')
    OP_3B(0x34, ParamInt(0x2191))

    Return()

# id: 0x00A8 offset: 0x112E8
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    SetEndhookFunction('AniBtlWinWait_sub', 0x000B)
    AnimeClipLoadMultiple(PseudoChrId.Self, 0x00, 'AniEv00200', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(PseudoChrId.Self, 0x00, 0x01, 'AniEv00200')
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    OP_60(0xFFFE, 0x01, '')

    Return()

# id: 0x00A9 offset: 0x11378
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCmd(0x09, PseudoChrId.Self, 0x00)

    Return()

# id: 0x00AA offset: 0x11384
@scena.Code('AniBtlWinWait_burst')
def AniBtlWinWait_burst():
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AB offset: 0x113D4
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    LoadEffect(0xFFFE, 0x31, 'battle/disarm067.eff', 0x00000000)
    SetChrFace(0x03, PseudoChrId.Self, '0', '0[autoM0]', '', '#b', '0')
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.11), ParamFloat(1.79), ParamFloat(-0.032), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)
    Sleep(833)

    OP_3B(0x00, ParamInt(0x10B9), ParamFloat(0.6), ParamInt(0x015E), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', '', '', '#b', '0')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    EffectCmd(0x11, 0xFFFE, 0x02)
    ReleaseEffect(0xFFFE, 0x31)

    Return()

# id: 0x00AC offset: 0x115A0
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)

    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x00AD offset: 0x115C4
@scena.Code('AniBtlLevelUpVoice')
def AniBtlLevelUpVoice():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_11631',
    )

    OP_3B(0x32, ParamInt(0x2192), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_11686')

    def _loc_11631(): pass

    label('loc_11631')

    OP_3B(0x32, ParamInt(0x2192), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11686(): pass

    label('loc_11686')

    Return()

# id: 0x00AE offset: 0x11688
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(PseudoChrId.Self, 0x02, 'AniBtLevelUp_Call', ScriptId.Current)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.16, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x11, 0x03, 5.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x2192), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4[autoM4]', '', '#b', '0')
    Sleep(900)

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '13434#70s134#100s4', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00AF offset: 0x1188C
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    BattleCmd(0x12, 0x01)
    LoadEffect(0xFFFE, 0x30, 'battle/cr067_00_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr067_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr067_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/cr067_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/cr067_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/ryu2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/gra00.eff', 0x00000000)
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
    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    BattleSetChrPos(0x0B86, 0xFFFE, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(0x0B86, 0x00000040)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.19, 0.09, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -1.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCmd(0x0B, 0x03, 2.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.19, 0.09, 833)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -1.0, 0.0, 833, 0x01)
    CameraSetDistance(0x03, 1.5, 833)
    CameraCmd(0x0B, 0x03, 2.8, 0x0341)
    BattleCmd(0x4B, 0x0341, 0x03)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    OP_46(0x06, PseudoChrId.Self, 0xFFFF, 0x0000)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniKibaOn')
    SetChrFace(0x03, PseudoChrId.Self, '3,32[autoE2]', '0,0K#80w0', '0[autoB0]', '#b', '0')
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('NODE_L_HAND'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0D)
    EffectSetRGBA(0xFFFE, 0x0D, 0.5, 0.1, 0.1, 1.0, 0, 0x03)
    OP_6C(PseudoChrId.Self, 1.25, 0xFFFFFFFF)
    Sleep(666)

    CameraSetPosByTarget(0x02, 0xFFFE, '', 0.02, 1.21, 0.08, 932)
    CameraRotateByTarget(0xFFFE, '', 0x02, 1.0, 0.0, 0.0, 932, 0x01)
    CameraSetDistance(0x02, 2.0, 932)
    CameraCmd(0x0B, 0x02, 14.8, 0x03A4)
    BattleCmd(0x4B, 0x03A4, 0x02)
    OP_3B(0x00, ParamInt(0x8FB4), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_11D4F',
    )

    Jump('loc_11DA4')

    def _loc_11D4F(): pass

    label('loc_11D4F')

    OP_3B(0x32, ParamInt(0x2170), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_11DA4(): pass

    label('loc_11DA4')

    SetChrFace(0x03, PseudoChrId.Self, '', '0[autoM0]', '', '#b', '0')
    Sleep(933)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.11, 1.21, 0.08, 532)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 0.0, 0.0, 532, 0x01)
    CameraSetDistance(0x03, 2.2, 532)
    CameraCmd(0x0B, 0x03, 14.8, 0x0214)
    BattleCmd(0x4B, 0x0214, 0x03)
    OP_3B(0x00, ParamInt(0xFFFF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(533)

    ChrClearPhysicsFlags(0x0B86, 0x00000040)
    ChrSetRGBA(0x0B86, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    Sleep(34)

    BattleCmd(0x6E, 0x0B86, 0x0B86, 0.0, 0.0, 5.0, 0.0)
    BattleSetChrPos(0x0B86, 0xFFEF, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 0.0, -1.0)
    OP_3B(0x00, ParamInt(0x8F6A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(34)

    CameraSetPosByTarget(0x03, 0x0B86, '', -0.04, 0.79, 1.27, 300)
    CameraRotateByTarget(0x0B86, '', 0x03, 3.0, 163.0, 0.0, 300, 0x01)
    CameraSetDistance(0x03, 4.0, 300)
    CameraCmd(0x0B, 0x03, 40.0, 0x012C)
    BattleCmd(0x4B, 0x012C, 0x03)
    EffectSetRGBA(0xFFFE, 0x0D, 0.0, 0.0, 0.0, 0.0, 300, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 110.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0E)
    EffectSetRGBA(0xFFFE, 0x0E, 0.5, 0.1, 0.1, 0.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0E, 0.5, 0.1, 0.1, 1.0, 500, 0x03)
    Sleep(166)

    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(0.15), ParamFloat(1.116), ParamFloat(0.496), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.2), ParamFloat(0.2), ParamFloat(0.2), 0x0C)
    EffectSetRGBA(0xFFFE, 0x0C, 0.5, 0.1, 0.1, 1.0, 0, 0x03)
    Sleep(500)

    EffectCmd(0x0F, 0xFFFE, 0x0031, 0x01)
    StopEffect(0xFFFE, 0x0D, 0x01)
    StopEffect(0xFFFE, 0x0E, 0x01)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Sleep(34)

    ChrSetPhysicsFlags(0x0B86, 0x00000020)
    BattleSetChrPos(0x0B86, 0xFFF5, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B86, 0xFFFE, 180.0, -1.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(2), 0.0, 0.0, 0.0, ParamFloat(7), ParamFloat(7), ParamFloat(7), 0xFF)
    Sleep(34)

    CameraCmd(0x00)
    CameraSetPosByTarget(0x00, 0x0B86, '', 0.0, 1.0, 0.0, 0)
    CameraRotateByTarget(0x0B86, '', 0x03, 4.0, -10.0, 0.0, 0, 0x01)
    BattleCmd(0x4B, 0x0000, 0x00)
    Sleep(34)

    OP_34(0x00, 0.0, 0.0, 0.0, 0.0, 0x0000)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x48, 0x0B86, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x012C, 0x03)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetHeight(0x03, 1.5, 500)
    BattleCmd(0x4B, 0x01F4, 0x03)
    Sleep(333)

    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    BattleCmd(0xC5, 0xFFFE, 0x00000002, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    OP_3B(0x00, ParamInt(0x8F66), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_1239E(): pass

    label('loc_1239E')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_123E6',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_123C8',
    )

    Jump('loc_123E6')

    def _loc_123C8(): pass

    label('loc_123C8')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_1239E')

    def _loc_123E6(): pass

    label('loc_123E6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1293F',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B86, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0x05)
    OP_3B(0xFF, 0.6, 0.6, 0.5)
    OP_5E(0x00, 0x0002, 0.35, 60, 800, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(200)

    CameraSetPosByTarget(0x03, 0x0B86, '', -0.0, 3.6, 0.01, 1200)
    CameraRotateByTarget(0x0B86, '', 0x03, -20.0, -24.0, 0.0, 1200, 0x01)
    CameraSetDistance(0x03, 9.0, 1200)
    CameraCmd(0x0B, 0x03, 40.0, 0x04B0)
    BattleCmd(0x4B, 0x04B0, 0x03)
    OP_3B(0x00, ParamInt(0x8F39), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(600)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, 180.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0E)
    EffectSetRGBA(0xFFFE, 0x0E, 1.0, 0.0, 0.0, 0.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0E, 1.0, 0.3, 0.0, 0.5, 1300, 0x03)

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_125BD(): pass

    label('loc_125BD')

    If(
        (
            (Expr.PushReg, 0x8),
            (Expr.PushLong, 0xB),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12633',
    )

    CameraSetPosByTarget(0x00, 0x0B86, '', -0.0, 3.6, 0.01, 600)
    CameraRotateByTarget(0x0B86, '', 0x00, -20.0, -24.0, 0.0, 600, 0x01)
    CameraSetDistance(0x00, 9.0, 600)
    BattleCmd(0x4B, 0x0258, 0x00)

    ExecExpressionWithReg(
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(100)

    Jump('loc_125BD')

    def _loc_12633(): pass

    label('loc_12633')

    BattleCmd(0x12, 0x00, 'PM', 0x001F, -1.0, -1.0)
    BattleCmd(0xC5, 0xFFFE, 0x00000083, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    StopEffect(0xFFFE, 0x0C, 0x01)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    CameraCmd(0x00)
    CameraRotateByTarget(0x0B86, '', 0x03, 10.0, 180.0, 0.0, 0, 0x01)
    ChrSetPhysicsFlags(0x0B86, 0x00000200)
    BattleSetChrPos(0x0B86, 0x0B86, 0.0, 8.0, 0.0, 0.0, 0x00, 0x00)
    Sleep(0)

    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x48, 0x0B86, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x4B, 0x0000, 0x03)
    BattleCmd(0x47)
    CameraSetHeight(0x03, 1.5, 100)
    BattleCmd(0x4B, 0x0064, 0x03)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_1276D',
    )

    Jump('loc_127C2')

    def _loc_1276D(): pass

    label('loc_1276D')

    OP_3B(0x32, ParamInt(0x2171), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_127C2(): pass

    label('loc_127C2')

    EffectCmd(0x13, 0xFFFE, 0x05, 0x01F4)
    Sleep(400)

    OP_5E(0x00, 0x0003, 0.75, 1000, 1000, 1000, 0.1, 0x0B86, '', 0.0, 1.0, 0.0)
    Sleep(100)

    OP_3B(0x00, ParamInt(0x0FBD), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(1), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1200), ParamInt(400), 0x0000, 0x04B0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    CameraRotateByTarget(0x0B86, '', 0x03, 10.0, 160.0, 0.0, 4000, 0x01)
    CameraSetHeight(0x03, 2.5, 4000)
    BattleCmd(0x4B, 0x0FA0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0E, 0.0, 0.8, 1.0, 1.0, 1000, 0x03)
    Sleep(400)

    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_128B0(): pass

    label('loc_128B0')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_1292D',
    )

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x01)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), PseudoChrId.Target, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x06)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_128B0')

    def _loc_1292D(): pass

    label('loc_1292D')

    EffectCmd(0x11, 0xFFFE, 0x06)

    Jump('loc_12946')

    def _loc_1293F(): pass

    label('loc_1293F')

    Sleep(2000)

    def _loc_12946(): pass

    label('loc_12946')

    Call(ScriptId.Current, 'SpringOn')
    OP_46(0x07, PseudoChrId.Self, 0xFFFF, 0x0000)
    BattleCmd(0x12, 0x02)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'AniKibaOff')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    OP_34(0x02, 0.0, 0.0, 0.0, 0.0, 0x0000)
    BattleDeleteChrDummy()

    Return()

# id: 0x00B0 offset: 0x129F8
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr067_01_0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x31, 'battle/cr067_01_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/cr067_01_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/gra00.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/ryu2.eff', 0x00000000)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(PseudoChrId.Self, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, PseudoChrId.Self, 0xFFFF, 0x0000)
    BattleSaveChrPosition(0xFFFE, 0x00000000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_12B41(): pass

    label('loc_12B41')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_12B71',
    )

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_12B41')

    def _loc_12B71(): pass

    label('loc_12B71')

    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    Call(ScriptId.BtlCom, 'SET_MOVE_SPEED', ParamFloat(6))
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.08, 0.72, -0.14, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 11.0, -2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.08, 0.72, -0.14, 666)
    CameraRotateByTarget(0xFFFE, '', 0x03, 11.0, -2.0, 0.0, 666, 0x01)
    CameraSetDistance(0x03, 2.6, 666)
    CameraCmd(0x0B, 0x03, 40.0, 0x029A)
    BattleCmd(0x4B, 0x029A, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '3#66w6', '2#66w7#66w2', '0#66w1[autoB1]', '#b', '0')
    Sleep(666)

    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.08, 1.97, -0.14, 400)
    CameraRotateByTarget(0xFFFE, '', 0x03, -20.0, 23.0, -49.0, 400, 0x01)
    CameraSetDistance(0x03, 2.6, 400)
    CameraCmd(0x0B, 0x03, 40.0, 0x0190)
    BattleCmd(0x4B, 0x0190, 0x03)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_12D33',
    )

    Jump('loc_12D88')

    def _loc_12D33(): pass

    label('loc_12D33')

    OP_3B(0x32, ParamInt(0x2172), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_12D88(): pass

    label('loc_12D88')

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, -165.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0C)
    EffectSetRGBA(0xFFFE, 0x0C, 1.0, 0.3, 5.0, 0.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0C, 1.0, 0.3, 5.0, 0.5, 500, 0x03)
    Sleep(166)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x1056), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FB9), ParamFloat(0.8), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(666)

    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.53, 1.15, 1.22, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -5.0, -30.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.8, 0)
    CameraCmd(0x0B, 0x03, 14.8, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.54, 1.15, 1.15, 1666)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, -40.0, 0.0, 1666, 0x01)
    CameraSetDistance(0x03, 2.1, 1666)
    CameraCmd(0x0B, 0x03, 14.8, 0x0682)
    BattleCmd(0x4B, 0x0682, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2#66w76', '6[autoM6]', '1[autoB1]', '#b', '0')
    Sleep(1000)

    EffectCmd(0x0F, 0xFFFE, 0x003A, 0x01)
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.16, 0.78, -0.13, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -35.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.21, 0.78, 0.03, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -72.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 2.6, 1000)
    CameraCmd(0x0B, 0x03, 40.0, 0x03E8)
    BattleCmd(0x4B, 0x03E8, 0x03)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 1.33333, 0x00, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(540), ParamFloat(0), 0.0, 0.0, -100.0, ParamFloat(2), ParamFloat(1), ParamFloat(1), 0x0C)
    EffectSetRGBA(0xFFFE, 0x0C, 1.0, 0.2, 5.0, 0.0, 0, 0x03)
    EffectSetRGBA(0xFFFE, 0x0C, 1.0, 0.2, 5.0, 0.3, 500, 0x03)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_13201',
    )

    Jump('loc_13256')

    def _loc_13201(): pass

    label('loc_13201')

    OP_3B(0x32, ParamInt(0x2173), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_13256(): pass

    label('loc_13256')

    BattleSaveChrPosition(0xFFFE, 0x00000000)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, -2.0, -1.0, 0x00, 0x00)
    Sleep(333)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, 0.3, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 0.75, 0xFFFFFFFF)
    Sleep(733)

    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.52, 0.78, 0.48, 300)
    CameraRotateByTarget(0xFFFE, '', 0x03, 1.0, -149.0, 0.0, 300, 0x01)
    CameraSetDistance(0x03, 2.6, 300)
    CameraCmd(0x0B, 0x03, 40.0, 0x012C)
    BattleCmd(0x4B, 0x012C, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), PseudoChrId.Self, 0x0200000C, ParamStr(''), ParamFloat(-0.203), ParamFloat(1.203), ParamFloat(0.237), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x03)
    OP_3B(0x00, ParamInt(0x8F6C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x0FAF), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    Sleep(300)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x0D)
    EffectSetRGBA(0xFFFE, 0x0D, 1.0, 0.2, 5.0, 0.5, 0, 0x03)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_13491(): pass

    label('loc_13491')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_134D9',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0A, 0xFFFE, 0xFFFB)"),
            Expr.Return,
        ),
        'loc_134BB',
    )

    Jump('loc_134D9')

    def _loc_134BB(): pass

    label('loc_134BB')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_13491')

    def _loc_134D9(): pass

    label('loc_134D9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_13508',
    )

    CameraCmd(0x0A, 0.07, 0.07, 0.01, 100, 900, 1200, 0, 0, 0x00)

    def _loc_13508(): pass

    label('loc_13508')

    OP_5E(0x00, 0x0002, 0.35, 60, 1400, 800, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.3, 6.0, 15.0)
    BattleCmd(0x4B, 0x012C, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x0032), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0003), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))
    Sleep(300)

    BattleCmd(0x47)
    Sleep(1200)

    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish', ParamInt(0x0001))
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    Call(ScriptId.BtlCom, 'RESET_MOVE_SPEED')

    Return()

# id: 0x00B1 offset: 0x13660
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipAddAsset(PseudoChrId.Self, 'C_CHR067_SC1')

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_136D9',
    )

    LoadEffect(0xFFFE, 0x30, 'battle/cic067_9.eff', 0x00000000)

    Jump('loc_136E2')

    def _loc_136D9(): pass

    label('loc_136D9')

    BattleCmd(0x52, 0xFFFE, 0x30)

    def _loc_136E2(): pass

    label('loc_136E2')

    LoadEffect(0xFFFE, 0x31, 'battle/sc067_00_1.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x32, 'battle/sc067_00_2.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x33, 'battle/sc067_00_3.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x34, 'battle/sc067_00_4.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x35, 'battle/sc067_00_5.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x36, 'battle/sc067_00_6.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x37, 'battle/sc067_00_7.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x38, 'battle/sc067_00_8.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x39, 'battle/sc067_00_9.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3A, 'battle/sc067_00_10.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3B, 'battle/sc067_00_11.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3C, 'battle/sc067_00_12.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3D, 'battle/sc067_00_13.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3E, 'battle/sc067_00_14.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x3F, 'battle/sc067_00_15.eff', 0x00000000)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000040)
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHR099', 'chr099')
    AnimeClipAddAsset(0x0B68, 'C_CHR099_SC1')
    ChrSetPhysicsFlags(0x0B68, 0x000003A0)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, 50.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000FA0, 0x00000000)

    def _loc_139CF(): pass

    label('loc_139CF')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_13A12',
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

    Jump('loc_139CF')

    def _loc_13A12(): pass

    label('loc_13A12')

    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'EraseEquip')
    OP_C0(0x0001, 0x40400000)
    OP_CE(0x0005, 0x0B68, 'BTL_S_CRAFT00_00_GS', 0x00)
    OP_CE(0x000A, 'gameCamera', 0x00)
    OP_CE(0x0014, 0x0B68, 'gamePos0', 0x00)
    OP_CE(0x0014, 0xFFFE, 'gamePos1', 0x00)
    OP_CE(0x0004, 0xFFFF, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    OP_43(0x64, 1000, 1.0, 0)
    OP_4E(0.75, 0.0, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0031), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), PseudoChrId.Self, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(4), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003C), PseudoChrId.Self, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0038), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_6B(0x06, 0x0000, 0x0000, 0.0, 0x00000000, 0x00000028)
    OP_CE(0x0002, 'BTL_S_CRAFT00_00_GS', 0x40555555, 0x40A55555, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 3.33333, 5.16667, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 3.33333, 5.16667, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '0#76w1#86w0[autoE0]', '0', '3#176w0[autoB0]', '#b', '0')
    ChrSetRGBA(PseudoChrId.Self, 0.3, 0.15, 0.15, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B68, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    OP_3B(0x00, ParamInt(0x1012), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_13D8B',
    )

    Jump('loc_13DE0')

    def _loc_13D8B(): pass

    label('loc_13D8B')

    OP_3B(0x32, ParamInt(0x2174), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_13DE0(): pass

    label('loc_13DE0')

    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), 0xFFFF, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7D), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_CE(0x0002, 'BTL_S_CRAFT00_00_GS', 0x40A66666, 0x40E00000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 5.2, 7.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 5.2, 7.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0x0B68, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    ChrSetRGBA(0x0B68, 0.3, 0.15, 0.15, 1.0, 100, 0x03)
    OP_5E(0x00, 0x0002, 0.7, 60, 1000, 500, 0.0, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_43(0x03, 200, 1.0, 0)
    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003E), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    ChrSetRGBA(PseudoChrId.Self, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    Sleep(100)

    OP_43(0x67, 200, 1.0, 0)
    OP_63(0xFFFE, 0x00)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0032, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x003C, 0x01)
    OP_C0(0x0001, 0x40800000)
    OP_4E(1.2, 0.0, 0x03, 0x00)
    OP_CE(0x0002, 'BTL_S_CRAFT00_01_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, ParamInt(0x8FA7), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_2A(0x00, 0x0B68, '', 'R_hand_point', 0x01)
    ChrSetPhysicsFlags(PseudoChrId.Self, 0x00000040)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0032), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(7), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1.2), ParamFloat(1.2), ParamFloat(1.2), 0xFF)
    OP_CE(0x0003, 0x00)
    OP_4E(1.0, 0.0, 0x03, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0038, 0x01)
    OP_6B(0x06, 0x0000, 0x0000, 0.0, 0x0000000F, 0xFFFFFFF1)
    OP_CE(0x0002, 'BTL_S_CRAFT00_02_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayChrAnimeClip(0x0B68, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0x0B68, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')
    ChrSetRGBA(0x0B68, 0.6, 0.3, 0.4, 1.0, 1000, 0x03)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003D), 0x0B68, 0x00000003, ParamStr('MEGANE_POINT'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8FA7), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(66)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B68, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(0.8), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0033), 0x0B68, 0x00000003, ParamStr('R_hand_point:NODE_EFFECT01'), ParamFloat(0), ParamFloat(0), ParamFloat(-0.5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)
    Sleep(266)

    CreateThread(0x0B68, 0x01, 'AniBtlSCraft00_Mouth00', ScriptId.Current)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_1446D',
    )

    Jump('loc_144C2')

    def _loc_1446D(): pass

    label('loc_1446D')

    OP_3B(0x32, ParamInt(0x2175), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_144C2(): pass

    label('loc_144C2')

    Sleep(2666)

    OP_3B(0x00, ParamInt(0x101B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x105A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_5E(0x00, 0x0002, 0.3, 200, 500, 200, 0.4, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(12), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(4), ParamFloat(11), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(5), ParamFloat(7), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(4), ParamFloat(3), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(-5), ParamFloat(7), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(-4), ParamFloat(11), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(-4), ParamFloat(3), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0034), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(2), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0037), 0x0B68, 0x00000001, ParamStr(''), ParamFloat(0), ParamFloat(7), ParamFloat(-5), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    ChrSetRGBA(0x0B68, 0.0, 0.0, 0.0, 1.0, 2000, 0x03)
    EffectSetRGBA(0x0B68, 0x02, 0.0, 0.0, 0.0, 0.0, 2000, 0x03)
    Sleep(1833)

    OP_63(0xFFFE, 0x00)
    OP_CE(0x0003, 0x00)
    WaitForThreadExit(0x0B68, 0x01)

    OP_CE(0x0002, 'BTL_S_CRAFT00_03_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    OP_6B(0x07, 0x0000, 0x0000, 0.0, 0x00000000, 0x00000000)
    EffectCmd(0x0F, 0xFFFE, 0x0038, 0x01)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0033, 0x01)
    ChrSetPhysicsFlags(0x0B68, 0x00000040)
    ChrSetPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    EffectCmd(0x0F, 0xFFFE, 0x0034, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_04_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0035), 0xFFEA, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x101B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x105A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.5, 0.0, 0.5)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0035, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_05_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0036), 0xFFEA, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x101B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x105A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0xFF, 0.0, 0.5, 0.5)
    OP_CE(0x0003, 0x00)
    OP_C0(0x0001, 0x3FD33333)
    EffectCmd(0x0F, 0xFFFE, 0x0030, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0034, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0035, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0037, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    OP_CE(0x0002, 'BTL_S_CRAFT00_06_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003A), 0xFFEA, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(20), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0039), 0xFFEA, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(15), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(PseudoChrId.Self, 'C_CHR067_C70')"),
            Expr.Return,
        ),
        'loc_14CB2',
    )

    Jump('loc_14D07')

    def _loc_14CB2(): pass

    label('loc_14CB2')

    OP_3B(0x32, ParamInt(0x2176), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_14D07(): pass

    label('loc_14D07')

    OP_3B(0x00, ParamInt(0x101B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x105A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1000)

    OP_3B(0x00, ParamInt(0x1065), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1833)

    OP_5E(0x00, 0x0002, 0.5, 100, 2000, 500, 0.4, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    CameraCmd(0x0A, 2.0, 3.0, 0.6, 100, 3000, 300, 0, 30, 0x00)
    OP_3B(0xFF, 0.7, 0.7, 3.0)
    OP_3B(0x00, ParamInt(0x3E5C), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, ParamInt(0x103A), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(1600), ParamInt(400), 0x0000, 0x0640, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    Sleep(1666)

    Sleep(833)

    PlayEffect(PseudoChrId.Self, ParamInt(0x003B), 0xFFFF, 0x00000000, ParamStr('scrn'), ParamFloat(960), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8F4B), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_63(0xFFFE, 0x00)
    OP_CE(0x0003, 0x00)
    EffectCmd(0x0F, 0xFFFE, 0x0039, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x003A, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x003B, 0x01)
    OP_CE(0x0002, 'BTL_S_CRAFT00_09_GS', 0xBF800000, 0xBF800000, 0xBF800000, 0x00000000, 0x00)
    PlayEffect(PseudoChrId.Self, ParamInt(0x003F), 0xFFEA, 0x00000000, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x113B), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(2000), ParamInt(500), 0x0000, 0x07D0, 0x0001, 0xFFFE, 0x0000, 0x0000, 0.0)
    ChrSetRGBA(0xFFF9, 0.7, 0.1, 0.1, 1.0, 0, 0x03)
    CameraCmd(0x0A, 0.5, 0.5, 0.6, 500, 3000, 300, 0, 30, 0x00)
    OP_3B(0xFF, 0.3, 0.3, 3.0)
    Sleep(1000)

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)

    def _loc_15119(): pass

    label('loc_15119')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_15164',
    )

    ChrSetRGBA(PseudoChrId.Target, 0.3, 0.1, 0.1, 1.0, 1000, 0x03)
    Sleep(33)

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_15119')

    def _loc_15164(): pass

    label('loc_15164')

    Sleep(1566)

    OP_3B(0x00, ParamInt(0x88E1), ParamFloat(1), ParamInt(300), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_43(0x03, 2000, 1.0, 0)
    OP_CE(0x0003, 0x00)
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR740_C00')
    OP_04(0x0B, 'AniBtlSCraft00_Finish')

    Return()

# id: 0x00B2 offset: 0x15208
@scena.Code('AniBtlSCraft00_Finish')
def AniBtlSCraft00_Finish():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    WaitForThreadExit(PseudoChrId.Self, 0x02)

    OP_CE(0x0001, 0x00000000, 0x00)
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR067_SC1')
    AnimeClipRemoveAsset(PseudoChrId.Self, 'C_CHR099_SC1')
    ChrClearPhysicsFlags(PseudoChrId.Self, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    BattleDeleteTempChar(0xFFFF)
    ChrSetRGBA(PseudoChrId.Self, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_43(0xFF, 0, 0x0000)
    ReleaseEffect(0xFFFE, 0x30)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x37)
    ReleaseEffect(0xFFFE, 0x38)
    ReleaseEffect(0xFFFE, 0x3A)
    ReleaseEffect(0xFFFE, 0x3B)
    ReleaseEffect(0xFFFE, 0x3C)
    ReleaseEffect(0xFFFE, 0x3D)
    ReleaseEffect(0xFFFE, 0x3E)
    ReleaseEffect(0xFFFE, 0x3F)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x00B3 offset: 0x153B0
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', ParamInt(0x03FA), ParamStr('NODE_CENTER'), ParamFloat(1), ParamInt(0x0001), ParamInt(0xFFFF), ParamFloat(0.5), ParamFloat(0))

    Return()

# id: 0x00B4 offset: 0x15400
@scena.Code('AniBtlSCraft00_Mouth00')
def AniBtlSCraft00_Mouth00():
    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '1', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0x0B68, '2', '0', '', '#b', '0')
    Sleep(800)

    Return()

# id: 0x00B5 offset: 0x15640
@scena.Code('AniBtlChangeAdult')
def AniBtlChangeAdult():
    AnimeClipChangeSkin(PseudoChrId.Self, 'C_CHR099')

    Return()

# id: 0x00B6 offset: 0x15654
@scena.Code('AniBtlChangeChild')
def AniBtlChangeChild():
    AnimeClipChangeSkin(PseudoChrId.Self, '')
    Call(ScriptId.Current, 'Ani_BT1_Load')

    Return()

# id: 0x00B7 offset: 0x15674
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B8 offset: 0x156E0
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B9 offset: 0x15728
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BA offset: 0x15780
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BB offset: 0x157D8
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.5, 0xFFFFFFFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BC offset: 0x1583C
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BD offset: 0x15870
@scena.Code('AniEvArts')
def AniEvArts():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BE offset: 0x158FC
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_BACKSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BF offset: 0x15968
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C0 offset: 0x159D4
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C1 offset: 0x15A60
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C2 offset: 0x15AB8
@scena.Code('AniEvDead2')
def AniEvDead2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C3 offset: 0x15B10
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C4 offset: 0x15B7C
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(433)

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.11), ParamFloat(1.79), ParamFloat(-0.032), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x10)
    Sleep(166)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    Sleep(833)

    OP_3B(0x00, ParamInt(0x10B9), ParamFloat(0.6), ParamInt(0x015E), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00C5 offset: 0x15CD8
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP_F', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C6 offset: 0x15DA0
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C7 offset: 0x15DF8
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C8 offset: 0x15E88
@scena.Code('AniEvBtlAria')
def AniEvBtlAria():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C9 offset: 0x15EE0
@scena.Code('AniEvBtlArts')
def AniEvBtlArts():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CA offset: 0x15F6C
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CB offset: 0x15FD4
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00CC offset: 0x16038
@scena.Code('AniEvCraft01_01')
def AniEvCraft01_01():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CD offset: 0x160AC
@scena.Code('AniEvCraft01_00')
def AniEvCraft01_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x16120
@scena.Code('AniEvCraft00_00')
def AniEvCraft00_00():
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CF offset: 0x16194
@scena.Code('AniEvSCraft00_00')
def AniEvSCraft00_00():
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x161E4
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

# id: 0x00D1 offset: 0x16298
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

# id: 0x00D2 offset: 0x16348
@scena.Code('AniEvTeburi')
def AniEvTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_TEBURI', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D3 offset: 0x163F8
@scena.Code('AniEvRyoteburi')
def AniEvRyoteburi():
    Call(ScriptId.CurrentCharacter, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000F)
    OP_80(0.4)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_RYOTEBURI', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D4 offset: 0x164AC
@scena.Code('AniEvDesk')
def AniEvDesk():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)
    OP_80(0.0)

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16542',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK-2', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_166AA')

    def _loc_16542(): pass

    label('loc_16542')

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1658D',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK-1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_166AA')

    def _loc_1658D(): pass

    label('loc_1658D')

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_165D5',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_166AA')

    def _loc_165D5(): pass

    label('loc_165D5')

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1661F',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK+1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_166AA')

    def _loc_1661F(): pass

    label('loc_1661F')

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16669',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK+2', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Jump('loc_166AA')

    def _loc_16669(): pass

    label('loc_16669')

    If(
        (
            (Expr.Eval, "OP_B6(0xFFFE, 0x01)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_166AA',
    )

    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK+3', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    def _loc_166AA(): pass

    label('loc_166AA')

    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D5 offset: 0x166E0
@scena.Code('AniEvDesk_p1')
def AniEvDesk_p1():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0, 0x0000, 0x0003)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000F)
    OP_80(0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV_DESK+1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D6 offset: 0x1678C
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x00D7 offset: 0x167F8
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00D8 offset: 0x1684C
@scena.Code('AniEv00150')
def AniEv00150():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev00150', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev00150a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x168B4
@scena.Code('AniEv00200')
def AniEv00200():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev00200', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00DA offset: 0x1690C
@scena.Code('AniEv00340')
def AniEv00340():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV00340', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV00340a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DB offset: 0x16974
@scena.Code('AniEv02031')
def AniEv02031():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV02031', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV02031a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DC offset: 0x169DC
@scena.Code('AniEv03005')
def AniEv03005():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03005', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DD offset: 0x16A10
@scena.Code('AniEv03010')
def AniEv03010():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev03010', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DE offset: 0x16A44
@scena.Code('AniEv30190')
def AniEv30190():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30190', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev30190a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00DF offset: 0x16ACC
@scena.Code('AniEv30215')
def AniEv30215():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev30215', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1033)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00E0 offset: 0x16B78
@scena.Code('AniEv33005')
def AniEv33005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev33005', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev33005a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E1 offset: 0x16C00
@scena.Code('AniEv33010')
def AniEv33010():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev33010', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev33010a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E2 offset: 0x16C88
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(633)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(40)

    OP_3B(0x00, ParamInt(0x7538), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00E3 offset: 0x16D74
@scena.Code('AniAttachS50KMO33')
def AniAttachS50KMO33():
    LoadAsset('O_S50KMO33')
    AttachEquip(0xFFFE, 'O_S50KMO33', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00E4 offset: 0x16E10
@scena.Code('AniDetachS50KMO33')
def AniDetachS50KMO33():
    ReleaseAsset('O_S50KMO33')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00E5 offset: 0x16E64
@scena.Code('AniAttachS50KMO41')
def AniAttachS50KMO41():
    LoadAsset('O_S50KMO41')
    AttachEquip(0xFFFE, 'O_S50KMO41', 'R_hand_point', 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00E6 offset: 0x16F00
@scena.Code('AniDetachS50KMO41')
def AniDetachS50KMO41():
    ReleaseAsset('O_S50KMO33')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00E7 offset: 0x16F54
@scena.Code('AniEv51045_2')
def AniEv51045_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    ReleaseEffect(0xFFFE, 0x30)
    LoadEffect(0xFFFE, 0x30, 'system/maskBox.eff', 0x00000000)
    PlayEffect(PseudoChrId.Self, ParamInt(0x0030), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0), ParamFloat(0.125), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.4), ParamFloat(0.4), ParamFloat(0.3), 0xFF)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev51045_2', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00E8 offset: 0x1701C
@scena.Code('AniAttachEQU461')
def AniAttachEQU461():
    LoadAsset('C_EQU461')
    AttachEquip(0xFFFE, 'C_EQU461', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00E9 offset: 0x170B4
@scena.Code('AniDetachEQU461')
def AniDetachEQU461():
    ReleaseAsset('C_EQU461')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00EA offset: 0x17108
@scena.Code('AniEv56020')
def AniEv56020():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev56020', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1366)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'ev56020a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00EB offset: 0x17198
@scena.Code('AniEv56020a')
def AniEv56020a():
    PlayChrAnimeClip(PseudoChrId.Self, 'ev56020a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EC offset: 0x171CC
@scena.Code('AniEv70115')
def AniEv70115():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV70115', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV70115a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00ED offset: 0x17234
@scena.Code('AniEv74310')
def AniEv74310():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV74310', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EE offset: 0x17288
@scena.Code('AniEv79250')
def AniEv79250():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79250', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00EF offset: 0x172DC
@scena.Code('AniEv79251')
def AniEv79251():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79251', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'EV79251a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F0 offset: 0x17364
@scena.Code('AniEv79251a')
def AniEv79251a():
    PlayChrAnimeClip(PseudoChrId.Self, 'EV79251a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F1 offset: 0x17398
@scena.Code('AniAttachEQU465')
def AniAttachEQU465():
    LoadAsset('C_EQU465')
    AttachEquip(0xFFFE, 'C_EQU465', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00F2 offset: 0x17430
@scena.Code('AniDetachEQU465')
def AniDetachEQU465():
    ReleaseAsset('C_EQU465')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00F3 offset: 0x17484
@scena.Code('AniAttachEQU095')
def AniAttachEQU095():
    LoadAsset('C_EQU095')
    AttachEquip(0xFFFE, 'C_EQU095', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x00F4 offset: 0x1751C
@scena.Code('AniDetachEQU095')
def AniDetachEQU095():
    ReleaseAsset('C_EQU095')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x00F5 offset: 0x17570
@scena.Code('AniCvInit')
def AniCvInit():
    AnimeClipAddSymbol(PseudoChrId.Self, 'C_CHR067_EV', 'ev35000')
    LoadEffect(0xFFFE, 0x22, 'battle/atk067.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x23, 'battle/disarm067.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x25, 'battle/atk067_a0.eff', 0x00000000)
    LoadEffect(0xFFFE, 0x26, 'battle/atk067_a1.eff', 0x00000000)

    Return()

# id: 0x00F6 offset: 0x17614
@scena.Code('AniCvRelease')
def AniCvRelease():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    AnimeClipRemoveSymbol(PseudoChrId.Self, 'ev35000')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x25)
    ReleaseEffect(0xFFFE, 0x26)

    Return()

# id: 0x00F7 offset: 0x17668
@scena.Code('AniCvWait')
def AniCvWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'EraseEquip')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00F8 offset: 0x176E0
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
    PlayChrAnimeClip(PseudoChrId.Self, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '01AA1G#86wD#376wHHHHGGGAH#66w10[autoE0]', '0[autoM0]', '#0e0[autoB0]', '#b', '0')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_17812',
    )

    OP_3B(0x32, ParamInt(0x21B0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_17867')

    def _loc_17812(): pass

    label('loc_17812')

    OP_3B(0x32, ParamInt(0x21B1), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_17867(): pass

    label('loc_17867')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00F9 offset: 0x17898
@scena.Code('AniCvBtlWait')
def AniCvBtlWait():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'ShowEquip')
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(PseudoChrId.Self, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(633)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(40)

    OP_3B(0x00, ParamInt(0x7538), ParamFloat(0.7), ParamInt(0), 0.0, ParamFloat(-2), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FA offset: 0x179C8
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

    Call(ScriptId.Current, 'SpringOff3')
    SetEndhookFunction('SpringOn3', 0x000B)
    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'FATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.2, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '2[autoE2]', 'A[autoMA]', '', '#b', '0')
    Sleep(200)

    OP_3B(0x3A, 0xFFFE, ParamInt(0x216B), ParamInt(0x216C), ParamInt(0x216D), ParamInt(0))
    Sleep(166)

    SetChrFace(0x03, PseudoChrId.Self, '', '6[autoM6]', '', '#b', '0')
    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17B39',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0022), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(0.074), ParamFloat(0.951), ParamFloat(0.633), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_17B39(): pass

    label('loc_17B39')

    OP_3B(0x00, ParamInt(0x0FB5), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1)

    OP_3B(0x00, ParamInt(0x0FBA), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(50)

    Sleep(500)

    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    SetChrFace(0x03, PseudoChrId.Self, '', '0', '', '#b', '0')
    Sleep(166)

    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00FB offset: 0x17C34
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
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, ParamInt(0x0FC0), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamInt(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_80(0.1)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 23.3333, 25.8, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 2.0, 0xFFFFFFFF)
    SetChrFace(0x03, PseudoChrId.Self, '6', '6[autoM6]', '', '#b', '0')
    CreateThread(0xFFFF, 0x04, 'SE_BTL_CHR067', ScriptId.Sound2, ParamInt(0x0014))
    OP_3B(0x3A, 0xFFFE, ParamInt(0x216E), ParamInt(0x216F), ParamInt(0), ParamInt(0))
    Sleep(533)

    EffectCmd(0x17, 0xFFFE, 0x02, 8.0)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17E1B',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0025), PseudoChrId.Self, 0x0000000C, ParamStr(''), ParamFloat(-0.203), ParamFloat(1.203), ParamFloat(0.237), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x02)

    def _loc_17E1B(): pass

    label('loc_17E1B')

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_5E(0x00, 0x0003, 0.75, 60, 1, 300, 0.2, 0xFFFE, '', 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 60, 1, 400, 0, 0, 0x00)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17EDE',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0026), PseudoChrId.Self, 0x00000003, ParamStr('NODE_R_ARM'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(0.7), ParamFloat(0.7), ParamFloat(0.7), 0xFF)

    def _loc_17EDE(): pass

    label('loc_17EDE')

    Sleep(233)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ASSAULT01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 25.8333, 26.3333, -1.0, 0x00, 0x00)
    OP_6C(PseudoChrId.Self, 1.0, 0xFFFFFFFF)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    Sleep(333)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.5, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.Current, 'SpringOn')
    OP_41(0xFFFE, 0x01)

    Return()

# id: 0x00FC offset: 0x17FA0
@scena.Code('AniCvFieldAttackEnd')
def AniCvFieldAttackEnd():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(PseudoChrId.Self, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(PseudoChrId.Self, 'R_hand_point', 'disarm_eq', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    Sleep(433)

    If(
        (
            (Expr.Eval, "OP_D9(0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1809E',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x0023), PseudoChrId.Self, 0x00000003, ParamStr(''), ParamFloat(-0.11), ParamFloat(1.79), ParamFloat(-0.032), 0.0, 0.0, 0.0, ParamFloat(0.5), ParamFloat(0.5), ParamFloat(0.5), 0x02)

    def _loc_1809E(): pass

    label('loc_1809E')

    Sleep(166)

    ChrClearPhysicsFlags(PseudoChrId.Self, 0x00000010)
    OP_AD(0x00, 0x01)
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)
    Sleep(833)

    OP_3B(0x00, ParamInt(0x10B9), ParamFloat(0.6), ParamInt(0x015E), 0.0, ParamFloat(3), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00FD offset: 0x18180
@scena.Code('AniCvAria_stopEffect')
def AniCvAria_stopEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_181A5',
    )

    EffectCmd(0x0E, 0xFFFE, 0x00, 0x00)

    def _loc_181A5(): pass

    label('loc_181A5')

    Return()

# id: 0x00FE offset: 0x181A8
@scena.Code('AniCvAria_PlayEffect')
def AniCvAria_PlayEffect():
    If(
        (
            (Expr.Eval, "EffectCmd(0x1F, 0xFFFE, 0x07D9)"),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1820A',
    )

    PlayEffect(PseudoChrId.Self, ParamInt(0x07D9), PseudoChrId.Self, 0x00000021, ParamStr(''), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0x00)

    def _loc_1820A(): pass

    label('loc_1820A')

    Return()

# id: 0x00FF offset: 0x1820C
@scena.Code('AniCvAria')
def AniCvAria():
    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "BattleGetChrStatus(0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_1828F',
    )

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    Jump('loc_18372')

    def _loc_1828F(): pass

    label('loc_1828F')

    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    OP_3B(0x00, ParamInt(0x8B7E), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, ParamInt(0x2179), ParamInt(0x217A), ParamInt(0), ParamInt(0))
    SetChrFace(0x03, PseudoChrId.Self, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, PseudoChrId.Self, '7', '0', '', '#b', '0')

    def _loc_18372(): pass

    label('loc_18372')

    Return()

# id: 0x0100 offset: 0x18374
@scena.Code('AniCvArts')
def AniCvArts():
    Call(ScriptId.Current, 'AniCvAria_PlayEffect')
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(200)

    SetChrFace(0x03, PseudoChrId.Self, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, ParamInt(0x217B), ParamInt(0x217C), ParamInt(0), ParamInt(0))
    Sleep(800)

    PlayEffect(PseudoChrId.Self, ParamInt(0x07DB), PseudoChrId.Self, 0x00000003, ParamStr('NODE_CENTER'), ParamFloat(0), ParamFloat(0), ParamFloat(0), 0.0, 0.0, 0.0, ParamFloat(1), ParamFloat(1), ParamFloat(1), 0xFF)
    OP_3B(0x00, ParamInt(0x8B7F), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
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

# id: 0x0101 offset: 0x185A8
@scena.Code('AniCvLevelUp')
def AniCvLevelUp():
    Call(ScriptId.Current, 'AniCvAria_stopEffect')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, ParamInt(0x2192), ParamFloat(1), ParamInt(0), 0.0, ParamFloat(0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, ParamFloat(0), '', ParamInt(0), ParamInt(0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, PseudoChrId.Self, '5', '4[autoM4]', '', '#b', '0')
    Sleep(900)

    SetChrFace(0x03, PseudoChrId.Self, '4[autoE4]', '13434#70s134#100s4', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(PseudoChrId.Self, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    Return()

# id: 0x0102 offset: 0x18730
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

# id: 0x0103 offset: 0x18790
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU095_C00',
        ),
    )

# id: 0x0104 offset: 0x187F0
@scena.AnimeClips('_OnCostumeIn2_2')
def _OnCostumeIn2_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002192,
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

# id: 0x0105 offset: 0x188A0
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218F,
            name   = '',
        ),
    )

# id: 0x0106 offset: 0x18920
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002166,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002167,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002168,
            name   = '',
        ),
    )

# id: 0x0107 offset: 0x189D0
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

# id: 0x0108 offset: 0x18AA0
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

# id: 0x0109 offset: 0x18D30
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

# id: 0x010A offset: 0x18E00
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

# id: 0x010B offset: 0x18E60
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

# id: 0x010C offset: 0x18EE0
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

# id: 0x010D offset: 0x18F60
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

# id: 0x010E offset: 0x18FE0
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

# id: 0x010F offset: 0x19040
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

# id: 0x0110 offset: 0x19140
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

# id: 0x0111 offset: 0x191A0
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

# id: 0x0112 offset: 0x19200
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021B1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0113 offset: 0x192D0
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
            dword4 = 0x0000216B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBA,
            name   = '',
        ),
    )

# id: 0x0114 offset: 0x193F0
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
            dword4 = 0x0000216E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216F,
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

# id: 0x0115 offset: 0x19510
@scena.AnimeClips('_SubAttackEnd')
def _SubAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
    )

# id: 0x0116 offset: 0x19570
@scena.AnimeClips('_SubAttackEndEV')
def _SubAttackEndEV():
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007533,
            name   = '',
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
    )

# id: 0x0117 offset: 0x19670
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
            dword4 = 0x000010B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0118 offset: 0x19720
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
            dword4 = 0x000010B9,
            name   = '',
        ),
    )

# id: 0x0119 offset: 0x197A0
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

# id: 0x011A offset: 0x19800
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

# id: 0x011B offset: 0x19860
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

# id: 0x011C offset: 0x198C0
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

# id: 0x011D offset: 0x19920
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

# id: 0x011E offset: 0x19980
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

# id: 0x011F offset: 0x19A00
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

# id: 0x0120 offset: 0x19A80
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

# id: 0x0121 offset: 0x19AE0
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

# id: 0x0122 offset: 0x19B40
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

# id: 0x0123 offset: 0x19BA0
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

# id: 0x0124 offset: 0x19C20
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

# id: 0x0125 offset: 0x19CA0
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

# id: 0x0126 offset: 0x19D20
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

# id: 0x0127 offset: 0x19D80
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

# id: 0x0128 offset: 0x19E00
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

# id: 0x0129 offset: 0x19E60
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

# id: 0x012A offset: 0x19EC0
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

# id: 0x012B offset: 0x19F20
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

# id: 0x012C offset: 0x19F80
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

# id: 0x012D offset: 0x19FE0
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

# id: 0x012E offset: 0x1A060
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

# id: 0x012F offset: 0x1A0C0
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

# id: 0x0130 offset: 0x1A120
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

# id: 0x0131 offset: 0x1A180
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

# id: 0x0132 offset: 0x1A1E0
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

# id: 0x0133 offset: 0x1A240
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

# id: 0x0134 offset: 0x1A2A0
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

# id: 0x0135 offset: 0x1A300
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

# id: 0x0136 offset: 0x1A360
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

# id: 0x0137 offset: 0x1A3C0
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

# id: 0x0138 offset: 0x1A420
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

# id: 0x0139 offset: 0x1A480
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk067.eff',
        ),
    )

# id: 0x013A offset: 0x1A4E0
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002189,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002189,
            name   = '',
        ),
    )

# id: 0x013B offset: 0x1A600
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002169,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002166,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002167,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002168,
            name   = '',
        ),
    )

# id: 0x013C offset: 0x1A700
@scena.AnimeClips('_AniBtlKisinReady')
def _AniBtlKisinReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002169,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002166,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002167,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002168,
            name   = '',
        ),
    )

# id: 0x013D offset: 0x1A800
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218D,
            name   = '',
        ),
    )

# id: 0x013E offset: 0x1A860
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

# id: 0x013F offset: 0x1A8C0
@scena.AnimeClips('_AniBtlMove')
def _AniBtlMove():
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
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x0140 offset: 0x1A940
@scena.AnimeClips('_AniBtlAria')
def _AniBtlAria():
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
            dword4 = 0x00002179,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x0141 offset: 0x1AA40
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
            dword4 = 0x0000217B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217C,
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

# id: 0x0142 offset: 0x1AB60
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
            dword4 = 0x0000216B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBA,
            name   = '',
        ),
    )

# id: 0x0143 offset: 0x1AC80
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002181,
            name   = '',
        ),
    )

# id: 0x0144 offset: 0x1ACE0
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

# id: 0x0145 offset: 0x1AD60
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217F,
            name   = '',
        ),
    )

# id: 0x0146 offset: 0x1AE10
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217F,
            name   = '',
        ),
    )

# id: 0x0147 offset: 0x1AE70
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
            dword4 = 0x00002180,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0148 offset: 0x1AF20
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
            dword4 = 0x0000217B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217C,
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

# id: 0x0149 offset: 0x1B020
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002186,
            name   = '',
        ),
    )

# id: 0x014A offset: 0x1B080
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002187,
            name   = '',
        ),
    )

# id: 0x014B offset: 0x1B0E0
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002188,
            name   = '',
        ),
    )

# id: 0x014C offset: 0x1B140
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

# id: 0x014D offset: 0x1B1F0
@scena.AnimeClips('_AniBtlBluffVoice')
def _AniBtlBluffVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002168,
            name   = '',
        ),
    )

# id: 0x014E offset: 0x1B250
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
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_01_GS',
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
            dword4 = 0x00002179,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_02_GS',
        ),
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
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x014F offset: 0x1B3F0
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

# id: 0x0150 offset: 0x1B450
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

# id: 0x0151 offset: 0x1B4B0
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

# id: 0x0152 offset: 0x1B510
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

# id: 0x0153 offset: 0x1B570
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

# id: 0x0154 offset: 0x1B5D0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002193,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002194,
            name   = '',
        ),
    )

# id: 0x0155 offset: 0x1B650
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
            dword4 = 0x000021A0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002195,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
    )

# id: 0x0156 offset: 0x1B7A0
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
            dword4 = 0x000021D4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021D5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021D6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBA,
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

# id: 0x0157 offset: 0x1B940
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

# id: 0x0158 offset: 0x1B9A0
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

# id: 0x0159 offset: 0x1BA00
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

# id: 0x015A offset: 0x1BA80
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002178,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002177,
            name   = '',
        ),
    )

# id: 0x015B offset: 0x1BB00
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

# id: 0x015C offset: 0x1BB60
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000218F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002190,
            name   = '',
        ),
    )

# id: 0x015D offset: 0x1BBE0
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
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001088,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001088,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x015E offset: 0x1BCE0
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
            dword4 = 0x00001088,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x015F offset: 0x1BD90
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
            dword4 = 0x00002191,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001088,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0160 offset: 0x1BE60
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

# id: 0x0161 offset: 0x1BEC0
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/disarm067.eff',
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
            dword4 = 0x000010B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0162 offset: 0x1BF90
@scena.AnimeClips('_AniBtlLevelUpVoice')
def _AniBtlLevelUpVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002192,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002192,
            name   = '',
        ),
    )

# id: 0x0163 offset: 0x1C010
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002192,
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

# id: 0x0164 offset: 0x1C0C0
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/ryu2.eff',
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
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002170,
            name   = '',
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
            dword4 = 0x00008F6A,
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
            dword4 = 0x00008F39,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002171,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0165 offset: 0x1C3A0
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr067_01_2.eff',
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
            name   = 'battle/ryu2.eff',
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
            dword4 = 0x00002172,
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
            dword4 = 0x00000FB9,
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
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002173,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FAF,
            name   = '',
        ),
    )

# id: 0x0166 offset: 0x1C600
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic067_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc067_00_15.eff',
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
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
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
            dword4 = 0x00002174,
            name   = '',
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
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001065,
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
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA7,
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
            type2  = 0x0B68,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002175,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000101B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000105A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000101B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000105A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000101B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000105A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06_GS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002176,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000101B,
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
            dword4 = 0x00001065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00003E5C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000103A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F4B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x000A,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09_GS',
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
            dword4 = 0x000088E1,
            name   = '',
        ),
    )

# id: 0x0167 offset: 0x1CE80
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

# id: 0x0168 offset: 0x1CEE0
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

# id: 0x0169 offset: 0x1CF60
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

# id: 0x016A offset: 0x1CFC0
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

# id: 0x016B offset: 0x1D020
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

# id: 0x016C offset: 0x1D080
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

# id: 0x016D offset: 0x1D0E0
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

# id: 0x016E offset: 0x1D140
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

# id: 0x016F offset: 0x1D1C0
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

# id: 0x0170 offset: 0x1D240
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

# id: 0x0171 offset: 0x1D2C0
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

# id: 0x0172 offset: 0x1D340
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

# id: 0x0173 offset: 0x1D3A0
@scena.AnimeClips('_AniEvDead2')
def _AniEvDead2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0174 offset: 0x1D400
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

# id: 0x0175 offset: 0x1D480
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
            dword4 = 0x000010B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0176 offset: 0x1D530
@scena.AnimeClips('_AniEvPowerUp')
def _AniEvPowerUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_F',
        ),
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

# id: 0x0177 offset: 0x1D5E0
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

# id: 0x0178 offset: 0x1D640
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

# id: 0x0179 offset: 0x1D6C0
@scena.AnimeClips('_AniEvBtlAria')
def _AniEvBtlAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x017A offset: 0x1D720
@scena.AnimeClips('_AniEvBtlArts')
def _AniEvBtlArts():
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

# id: 0x017B offset: 0x1D7A0
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

# id: 0x017C offset: 0x1D820
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

# id: 0x017D offset: 0x1D8A0
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

# id: 0x017E offset: 0x1D920
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

# id: 0x017F offset: 0x1D9A0
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

# id: 0x0180 offset: 0x1DA20
@scena.AnimeClips('_AniEvSCraft00_00')
def _AniEvSCraft00_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
    )

# id: 0x0181 offset: 0x1DA80
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

# id: 0x0182 offset: 0x1DB30
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

# id: 0x0183 offset: 0x1DBE0
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

# id: 0x0184 offset: 0x1DC90
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

# id: 0x0185 offset: 0x1DD40
@scena.AnimeClips('_AniEvDesk')
def _AniEvDesk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK-2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK-1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK+1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK+2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK+3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
    )

# id: 0x0186 offset: 0x1DE90
@scena.AnimeClips('_AniEvDesk_p1')
def _AniEvDesk_p1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DESK+1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
    )

# id: 0x0187 offset: 0x1DF10
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

# id: 0x0188 offset: 0x1DF70
@scena.AnimeClips('_AniEv00150')
def _AniEv00150():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00150',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00150a',
        ),
    )

# id: 0x0189 offset: 0x1DFF0
@scena.AnimeClips('_AniEv00200')
def _AniEv00200():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00200',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x018A offset: 0x1E070
@scena.AnimeClips('_AniEv00340')
def _AniEv00340():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00340',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV00340a',
        ),
    )

# id: 0x018B offset: 0x1E0F0
@scena.AnimeClips('_AniEv02031')
def _AniEv02031():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02031',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02031a',
        ),
    )

# id: 0x018C offset: 0x1E170
@scena.AnimeClips('_AniEv03005')
def _AniEv03005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03005',
        ),
    )

# id: 0x018D offset: 0x1E1D0
@scena.AnimeClips('_AniEv03010')
def _AniEv03010():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03010',
        ),
    )

# id: 0x018E offset: 0x1E230
@scena.AnimeClips('_AniEv30190')
def _AniEv30190():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30190',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30190a',
        ),
    )

# id: 0x018F offset: 0x1E2B0
@scena.AnimeClips('_AniEv30215')
def _AniEv30215():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30215',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0190 offset: 0x1E330
@scena.AnimeClips('_AniEv33005')
def _AniEv33005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33005',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33005a',
        ),
    )

# id: 0x0191 offset: 0x1E3B0
@scena.AnimeClips('_AniEv33010')
def _AniEv33010():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33010',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33010a',
        ),
    )

# id: 0x0192 offset: 0x1E430
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
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0193 offset: 0x1E4E0
@scena.AnimeClips('_AniAttachS50KMO33')
def _AniAttachS50KMO33():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'O_S50KMO33',
        ),
    )

# id: 0x0194 offset: 0x1E540
@scena.AnimeClips('_AniAttachS50KMO41')
def _AniAttachS50KMO41():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'O_S50KMO41',
        ),
    )

# id: 0x0195 offset: 0x1E5A0
@scena.AnimeClips('_AniEv51045_2')
def _AniEv51045_2():
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
            name   = 'ev51045_2',
        ),
    )

# id: 0x0196 offset: 0x1E620
@scena.AnimeClips('_AniAttachEQU461')
def _AniAttachEQU461():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU461',
        ),
    )

# id: 0x0197 offset: 0x1E680
@scena.AnimeClips('_AniEv56020')
def _AniEv56020():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev56020',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev56020a',
        ),
    )

# id: 0x0198 offset: 0x1E700
@scena.AnimeClips('_AniEv56020a')
def _AniEv56020a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev56020a',
        ),
    )

# id: 0x0199 offset: 0x1E760
@scena.AnimeClips('_AniEv70115')
def _AniEv70115():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70115',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV70115a',
        ),
    )

# id: 0x019A offset: 0x1E7E0
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

# id: 0x019B offset: 0x1E840
@scena.AnimeClips('_AniEv79250')
def _AniEv79250():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79250',
        ),
    )

# id: 0x019C offset: 0x1E8A0
@scena.AnimeClips('_AniEv79251')
def _AniEv79251():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79251',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79251a',
        ),
    )

# id: 0x019D offset: 0x1E920
@scena.AnimeClips('_AniEv79251a')
def _AniEv79251a():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV79251a',
        ),
    )

# id: 0x019E offset: 0x1E980
@scena.AnimeClips('_AniAttachEQU465')
def _AniAttachEQU465():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU465',
        ),
    )

# id: 0x019F offset: 0x1E9E0
@scena.AnimeClips('_AniAttachEQU095')
def _AniAttachEQU095():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU095',
        ),
    )

# id: 0x01A0 offset: 0x1EA40
@scena.AnimeClips('_AniCvInit')
def _AniCvInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk067.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/disarm067.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk067_a0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk067_a1.eff',
        ),
    )

# id: 0x01A1 offset: 0x1EB10
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

# id: 0x01A2 offset: 0x1EB70
@scena.AnimeClips('_AniCvIdle')
def _AniCvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x000021B1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01A3 offset: 0x1EC40
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
            dword4 = 0x00007538,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x01A4 offset: 0x1ECF0
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
            dword4 = 0x0000216B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FB5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FBA,
            name   = '',
        ),
    )

# id: 0x01A5 offset: 0x1EE10
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
            dword4 = 0x0000216E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000216F,
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

# id: 0x01A6 offset: 0x1EF30
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
            dword4 = 0x000010B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x01A7 offset: 0x1EFE0
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
            dword4 = 0x00002179,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x01A8 offset: 0x1F0E0
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
            dword4 = 0x0000217B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000217C,
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

# id: 0x01A9 offset: 0x1F230
@scena.AnimeClips('_AniCvLevelUp')
def _AniCvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00002192,
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
