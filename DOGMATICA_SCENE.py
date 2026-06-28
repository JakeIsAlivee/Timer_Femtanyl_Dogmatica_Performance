#I LOOOOVE FOURTH WALL BREAKSSSS

#im NOT proud of the code but AM proud of the final product

import os
import time

import pygame

import random

import math

songSTARTtime = 0
songpos = 0

DOGMATICAlyricnum = 0

DOGMATICArenderednum = -1

BE_AMCSLASH = ["    \n",                     #0
               "    \n",                     #1
               "    \n",                     #2
               "    .s5SSSs.  .s5SSSs.  \n", #3
               "          SS.       SS. \n", #4
               "    sS    S%S sS    `:; \n", #5
               "    SS    S%S SS        \n", #6
               "    SS .sSSS  SSSs.     \n", #7
               "    SS    S%S SS        \n", #8
               "    SS    `:; SS        \n", #9
               "    SS    ;,. SS    ;,. \n", #10
               "    `:;;;;;:' `:;;;;;:' \n", #11
               "    \n",                     #12
               "    \n",                     #13
               "    \n",]                    #14
BE_AMCSLASH_str = ''
for i in BE_AMCSLASH:
    BE_AMCSLASH_str+=i


BE_AMCAAA01 = ["     .S_SSSs      sSSs  \n", #0
               "    .SS~SSSSS    d%%SP  \n", #1
               "    S%S   SSSS  d%S'    \n", #2
               "    S%S    S%S  S%S     \n", #3
               "    S%S SSSS%P  S&S     \n", #4
               "    S&S  SSSY   S&S_Ss  \n", #5
               "    S&S    S&S  S&S~SP  \n", #6
               "    S&S    S&S  S&S~SP  \n", #7
               "    S&S    S&S  S&S     \n", #8
               "    S*S    S&S  S*b     \n", #9
               "    S*S    S*S  S*S.    \n", #10
               "    S*S SSSSP    SSSbs  \n", #11
               "    S*S  SSY      YSSP  \n", #12
               "    SP                  \n", #13
               "    Y                   \n",]#14
BE_AMCAAA01_str = ''
for i in BE_AMCAAA01:
    BE_AMCAAA01_str+=i

KEEP_AMCAAA01 = ["     .S    S.     sSSs    sSSs   .S_sSSs    \n", #0                 
                 "    .SS    SS.   d%%SP   d%%SP  .SS~YS%%b   \n", #1
                 "    S%S    S&S  d%S'    d%S'    S%S   `S%b  \n", #2
                 "    S%S    d*S  S%S     S%S     S%S    S%S  \n", #3
                 "    S&S   .S*S  S&S     S&S     S%S    d*S  \n", #4
                 "    S&S_sdSSS   S&S_Ss  S&S_Ss  S&S   .S*S  \n", #5
                 "    S&S~YSSY%b  S&S~SP  S&S~SP  S&S_sdSSS   \n", #6
                 "    S&S    `S%  S&S     S&S     S&S~YSSY    \n", #7
                 "    S*S     S%  S*b     S*b     S*S         \n", #8
                 "    S*S     S&  S*S.    S*S.    S*S         \n", #9
                 "    S*S     S&   SSSbs   SSSbs  S*S         \n", #10
                 "    S*S     SS    YSSP    YSSP  S*S         \n", #11
                 "    SP                          SP          \n", #12
                 "    Y                           Y           \n",]#13
KEEP_AMCAAA01_str = ''
for i in KEEP_AMCAAA01:
    KEEP_AMCAAA01_str+=i

BEFORE_BLURVISIONASCII = [
    "░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░ \n", #0
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n", #1
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n", #2
    "░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░   \n", #3
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n", #4
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n", #5
    "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ \n", #6
]
BEFORE_BLURVISIONASCII_str = ''
for i in BEFORE_BLURVISIONASCII:
    BEFORE_BLURVISIONASCII_str+=i

OH_ANSIREGULAR = [
    "     ██████  ██   ██ \n", #0
    "    ██    ██ ██   ██ \n", #1
    "    ██    ██ ███████ \n", #2
    "    ██    ██ ██   ██ \n", #3
    "     ██████  ██   ██ \n", #4
]
OH_ANSIREGULAR_str = ''
for i in OH_ANSIREGULAR:
    OH_ANSIREGULAR_str+=i

MY_ANSIREGULAR = [
    "    ███    ███ ██    ██ \n", #0
    "    ████  ████  ██  ██  \n", #1
    "    ██ ████ ██   ████   \n", #2
    "    ██  ██  ██    ██    \n", #3
    "    ██      ██    ██    \n", #4
]
MY_ANSIREGULAR_str = ''
for i in MY_ANSIREGULAR:
    MY_ANSIREGULAR_str+=i

GOD_ANSIREGULAR = [
    "     ██████   ██████  ██████  \n", #0
    "    ██       ██    ██ ██   ██ \n", #1
    "    ██   ███ ██    ██ ██   ██ \n", #2
    "    ██    ██ ██    ██ ██   ██ \n", #3
    "     ██████   ██████  ██████  \n", #4
]
GOD_ANSIREGULAR_str = ''
for i in GOD_ANSIREGULAR:
    GOD_ANSIREGULAR_str+=i

SHUT_THEEDGE = [
    "       ▄▄▄▄▄    ▄  █   ▄     ▄▄▄▄▀ \n", #0
    "      █     ▀▄ █   █    █ ▀▀▀ █    \n", #1
    "    ▄  ▀▀▀▀▄   ██▀▀█ █   █    █    \n", #2
    "     ▀▄▄▄▄▀    █   █ █   █   █     \n", #3
    "                  █  █▄ ▄█  ▀      \n", #4
    "                 ▀    ▀▀▀          \n", #5
]
SHUT_THEEDGE_str = ''
for i in SHUT_THEEDGE:
    SHUT_THEEDGE_str+=i

THE_THIS = [
    "     ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄ \n", #0
    "    █    █  ▐ █  █   ▄▀ ▐  ▄▀   ▐ \n", #1
    "    ▐   █     ▐  █▄▄▄█    █▄▄▄▄▄  \n", #2
    "       █         █   █    █    ▌  \n", #3
    "     ▄▀         ▄▀  ▄▀   ▄▀▄▄▄▄   \n", #4
    "    █          █   █     █    ▐   \n", #5
    "    ▐          ▐   ▐     ▐        \n", #6
]
THE_THIS_str = ''
for i in THE_THIS:
    THE_THIS_str+=i

FUCK_THIS = [
    "     ▄▀▀▀█▄    ▄▀▀▄ ▄▀▀▄  ▄▀▄▄▄▄   ▄▀▀▄ █ \n", #0
    "    █  ▄▀  ▀▄ █   █    █ █ █    ▌ █  █ ▄▀ \n", #1
    "    ▐ █▄▄▄▄   ▐  █    █  ▐ █      ▐  █▀▄  \n", #2
    "     █    ▐     █    █     █        █   █ \n", #3
    "     █           ▀▄▄▄▄▀   ▄▀▄▄▄▄▀ ▄▀   █  \n", #4
    "    █                    █     ▐  █    ▐  \n", #5
    "    ▐                    ▐        ▐       \n", #6
]
FUCK_THIS_str=''
for i in FUCK_THIS:
    FUCK_THIS_str += i

UP_BLOODY = [
    "     █    ██  ██▓███   ▐██▌ \n", #0
    "     ██  ▓██▒▓██░  ██▒ ▐██▌ \n", #1
    "    ▓██  ▒██░▓██░ ██▓▒ ▐██▌ \n", #2
    "    ▓▓█  ░██░▒██▄█▓▒ ▒ ▓██▒ \n", #3
    "    ▒▒█████▓ ▒██▒ ░  ░ ▒▄▄  \n", #4
    "    ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░ ░▀▀▒ \n", #5
    "    ░░▒░ ░ ░ ░▒ ░      ░  ░ \n", #6
    "     ░░░ ░ ░ ░░           ░ \n", #7
    "       ░               ░    \n", #8
]
UP_BLOODY_str=''
for i in UP_BLOODY:
    UP_BLOODY_str+=i

TWICE_BLOODY = [
    "▄▄▄█████▓ █     █░ ██▓ ▄████▄  ▓█████ \n", #0
    "▓  ██▒ ▓▒▓█░ █ ░█░▓██▒▒██▀ ▀█  ▓█   ▀ \n", #1
    "▒ ▓██░ ▒░▒█░ █ ░█ ▒██▒▒▓█    ▄ ▒███   \n", #2
    "░ ▓██▓ ░ ░█░ █ ░█ ░██░▒▓▓▄ ▄██▒▒▓█  ▄ \n", #3
    "  ▒██▒ ░ ░░██▒██▓ ░██░▒ ▓███▀ ░░▒████▒\n", #4
    "  ▒ ░░   ░ ▓░▒ ▒  ░▓  ░ ░▒ ▒  ░░░ ▒░ ░\n", #5
    "  ▒ ░░   ░ ▓░▒ ▒  ░▓  ░ ░▒ ▒  ░░░ ▒░ ░\n", #6
    "    ░      ▒ ░ ░   ▒ ░  ░  ▒    ░ ░  ░\n", #7
    "  ░        ░   ░   ▒ ░░           ░   \n", #8
    "             ░     ░  ░ ░         ░  ░\n", #9
    "                      ░               \n", #10
]
TWICE_BLOODY_str = ''
for i in TWICE_BLOODY:
    TWICE_BLOODY_str+=i

TONIGHT_BLOODY = [
    "▄▄▄█████▓ ▒█████   ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓\n", #0
    "▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒\n", #1
    "▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░\n", #2
    "░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ \n", #3
    "  ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ \n", #4
    "  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   \n", #5
    "    ░      ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    \n", #6
    "  ░      ░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      \n", #7
    "             ░ ░           ░  ░        ░  ░  ░  ░         \n", #8
]
TONIGHT_BLOODY_str = ''
for i in TONIGHT_BLOODY:
    TONIGHT_BLOODY_str+=i

SO_THEEDGE = [
    "   ▄▄▄▄▄   ████▄\n", #0
    "  █     ▀▄ █   █\n", #1
    "▄  ▀▀▀▀▄   █   █\n", #2
    " ▀▄▄▄▄▀    ▀████\n", #3
    "                \n", #4
    "                \n", #5
    "                \n", #6
]
SO_THEEDGE_str =''
for i in SO_THEEDGE:
    SO_THEEDGE_str+=i

PLEASE_THEEDGE = [
    "█ ▄▄  █     ▄███▄   ██      ▄▄▄▄▄   ▄███▄  \n", #0
    "█   █ █     █▀   ▀  █ █    █     ▀▄ █▀   ▀ \n", #1
    "█▀▀▀  █     ██▄▄    █▄▄█ ▄  ▀▀▀▀▄   ██▄▄   \n", #2
    "█     ███▄  █▄   ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀\n", #3
    " █        ▀ ▀███▀      █            ▀███▀  \n", #4
    "  ▀                   █                    \n", #5
    "                     ▀                     \n", #6
]
PLEASE_THEEDGE_str = ''
for i in PLEASE_THEEDGE:
    PLEASE_THEEDGE_str+=i

JUST_THEEDGE = [
    "  ▄▄▄▄▄ ▄      ▄▄▄▄▄      ▄▄▄▄▀\n", #0
    "▄▀  █    █    █     ▀▄ ▀▀▀ █   \n", #1
    "    █ █   █ ▄  ▀▀▀▀▄       █   \n", #2
    " ▄ █  █   █  ▀▄▄▄▄▀       █    \n", #3
    "  ▀   █▄ ▄█              ▀     \n", #4
    "       ▀▀▀                     \n", #5
    "                               \n", #6
]
JUST_THEEDGE_str=''
for i in JUST_THEEDGE:
    JUST_THEEDGE_str+=i

HOLD_THEEDGE = [
    " ▄  █ ████▄ █     ██▄  \n", #0
    "█   █ █   █ █     █  █ \n", #1
    "██▀▀█ █   █ █     █   █\n", #2
    "█   █ ▀████ ███▄  █  █ \n", #3
    "   █            ▀ ███▀ \n", #4
    "  ▀                    \n", #5
    "                       \n", #6
]
HOLD_THEEDGE_str = ''
for i in HOLD_THEEDGE:
    HOLD_THEEDGE_str+=i

ME_THEEDGE = [
    "█▀▄▀█ ▄███▄  \n", #0
    "█ █ █ █▀   ▀ \n", #1
    "█ ▄ █ ██▄▄   \n", #2
    "█   █ █▄   ▄▀\n", #3
    "   █  ▀███▀  \n", #4
    "  ▀          \n", #5
    "             \n", #6
]
ME_THEEDGE_str = ''
for i in ME_THEEDGE:
    ME_THEEDGE_str+=i

ONE_THEEDGE = [
    "████▄    ▄   ▄███▄  \n", #0
    "█   █     █  █▀   ▀ \n", #1
    "█   █ ██   █ ██▄▄   \n", #2
    "▀████ █ █  █ █▄   ▄▀\n", #3
    "      █  █ █ ▀███▀  \n", #4
    "      █   ██        \n", #5
    "                    \n", #6
]
ONE_THEEDGE_str = ''
for i in ONE_THEEDGE:
    ONE_THEEDGE_str+=i

LAST_THEEDGE = [
    "█    ██      ▄▄▄▄▄      ▄▄▄▄▀ \n", #0
    "█    █ █    █     ▀▄ ▀▀▀ █    \n", #1
    "█    █▄▄█ ▄  ▀▀▀▀▄       █    \n", #2
    "███▄ █  █  ▀▄▄▄▄▀       █     \n", #3
    "    ▀   █              ▀      \n", #4
    "       █                      \n", #5
    "      ▀                       \n", #6
]
LAST_THEEDGE_str = ''
for i in LAST_THEEDGE:
    LAST_THEEDGE_str+=i

TIME_BLOODY = [
    "▄▄▄█████▓ ██▓ ███▄ ▄███▓▓█████ \n", #0
    "▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▓█   ▀ \n", #1
    "▒ ▓██░ ▒░▒██▒▓██    ▓██░▒███   \n", #2
    "░ ▓██▓ ░ ░██░▒██    ▒██ ▒▓█  ▄ \n", #3
    "  ▒██▒ ░ ░██░▒██▒   ░██▒░▒████▒\n", #4
    "  ▒ ░░   ░▓  ░ ▒░   ░  ░░░ ▒░ ░\n", #5
    "    ░     ▒ ░░  ░      ░ ░ ░  ░\n", #6
    "  ░       ▒ ░░      ░      ░   \n", #7
    "          ░         ░      ░  ░\n", #8
]
TIME_BLOODY_str = ''
for i in TIME_BLOODY:
    TIME_BLOODY_str+=i

GOODBYE_BLOODY = [
    "  ▄████  ▒█████   ▒█████  ▓█████▄  ▄▄▄▄ ▓██   ██▓▓█████ \n", #0
    " ██▒ ▀█▒▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█████▄▒██  ██▒▓█   ▀ \n", #1
    "▒██░▄▄▄░▒██░  ██▒▒██░  ██▒░██   █▌▒██▒ ▄██▒██ ██░▒███   \n", #2
    "░▓█  ██▓▒██   ██░▒██   ██░░▓█▄   ▌▒██░█▀  ░ ▐██▓░▒▓█  ▄ \n", #3
    "░▒▓███▀▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▓█  ▀█▓░ ██▒▓░░▒████▒\n", #4
    " ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░\n", #5
    "  ░   ░   ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▒░▒   ░▓██ ░▒░  ░ ░  ░\n", #6
    "░ ░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░  ░    ░▒ ▒ ░░     ░   \n", #7
    "      ░     ░ ░      ░ ░     ░     ░     ░ ░        ░  ░\n", #8
    "                           ░            ░░ ░            \n", #9
]
GOODBYE_BLOODY_str = ''
for i in GOODBYE_BLOODY:
    GOODBYE_BLOODY_str+=i

AAH_BLOODY = [
    " ▄▄▄      ▄▄▄       ██░ ██  ▐██▌ \n", #0
    "▒████▄   ▒████▄    ▓██░ ██▒ ▐██▌ \n", #1
    "▒██  ▀█▄ ▒██  ▀█▄  ▒██▀▀██░ ▐██▌ \n", #2
    "░██▄▄▄▄██░██▄▄▄▄██ ░▓█ ░██  ▓██▒ \n", #3
    " ▓█   ▓██▒▓█   ▓██▒░▓█▒░██▓ ▒▄▄  \n", #4
    " ▒▒   ▓▒█░▒▒   ▓▒█░ ▒ ░░▒░▒ ░▀▀▒ \n", #5
    "  ░   ▒    ░   ▒    ░  ░░ ░    ░ \n", #6
    "      ░  ░     ░  ░ ░  ░  ░ ░    \n", #7
]
AAH_BLOODY_str = ''
for i in AAH_BLOODY:
    AAH_BLOODY_str+=i
































I_BIG = [
    "     _____      \n", #0
    "    |_   _|     \n", #1
    "      | |______ \n", #2
    "      | |______|\n", #3
    "     _| |_      \n", #4
    "    |_____|     \n", #5
]
DONT_BIG = [
    "     _____   ____  _   _ _______     \n", #0
    "    |  __ \\ / __ \\| \\ | |__   __|    \n", #1
    "    | |  | | |  | |  \\| |  | |______ \n", #2
    "    | |  | | |  | | . ` |  | |______|\n", #3
    "    | |__| | |__| | |\\  |  | |       \n", #4
    "    |_____/ \\____/|_| \\_|  |_|       \n", #5
]
HAVE_BIG = [
    "     _    _     __      ________      \n", #0
    "    | |  | |   /\\ \\    / /  ____|     \n", #1
    "    | |__| |  /  \\ \\  / /| |__ ______ \n", #2
    "    |  __  | / /\\ \\ \\/ / |  __|______|\n", #3
    "    | |  | |/ ____ \\  /  | |____      \n", #4
    "    |_|  |_/_/    \\_\\/   |______|     \n", #5
]
A_BIG = [
    "                   \n", #0
    "        /\\         \n", #1
    "       /  \\ ______ \n", #2
    "      / /\\ \\______|\n", #3
    "     / ____ \\      \n", #4
    "    /_/    \\_\\     \n", #5
]





I_SBLOOD = [
    "    @@@         \n", #0
    "    @@!         \n", #1
    "    !!@ @!@!@!@!\n", #2
    "    !!:         \n", #3
    "    :           \n", #4
]
DONT_SBLOOD = [
    "    @@@@@@@   @@@@@@  @@@  @@@ @@@@@@@         \n", #0
    "    @@!  @@@ @@!  @@@ @@!@!@@@   @@!           \n", #1
    "    @!@  !@! @!@  !@! @!@@!!@!   @!!   @!@!@!@!\n", #2
    "    !!:  !!! !!:  !!! !!:  !!!   !!:           \n", #3
    "    :: :  :   : :. :  ::    :     :            \n", #4
]
HAVE_SBLOOD = [
    "    @@@  @@@  @@@@@@  @@@  @@@ @@@@@@@@         \n", #0
    "    @@!  @@@ @@!  @@@ @@!  @@@ @@!              \n", #1
    "    @!@!@!@! @!@!@!@! @!@  !@! @!!!:!   @!@!@!@!\n", #2
    "    !!:  !!! !!:  !!!  !: .:!  !!:              \n", #3
    "     :   : :  :   : :    ::    : :: :::         \n", #4
]
A_SBLOOD = [
    "     @@@@@@          \n", #0
    "    @@!  @@@         \n", #1
    "    @!@!@!@! @!@!@!@!\n", #2
    "    !!:  !!!         \n", #3
    "     :   : :         \n", #4
]





I_ANSIREGULAR = [
    "    ██       \n", #0
    "    ██       \n", #1
    "    ██ █████ \n", #2
    "    ██       \n", #3
    "    ██       \n", #4
]
DONT_ANSIREGULAR = [
    "    ██████   ██████  ███    ██ ████████       \n", #0
    "    ██   ██ ██    ██ ████   ██    ██          \n", #1
    "    ██   ██ ██    ██ ██ ██  ██    ██    █████ \n", #2
    "    ██   ██ ██    ██ ██  ██ ██    ██          \n", #3
    "    ██████   ██████  ██   ████    ██          \n", #4
]
HAVE_ANSIREGULAR = [
    "    ██   ██  █████  ██    ██ ███████       \n", #0
    "    ██   ██ ██   ██ ██    ██ ██            \n", #1
    "    ███████ ███████ ██    ██ █████   █████ \n", #2
    "    ██   ██ ██   ██  ██  ██  ██            \n", #3
    "    ██   ██ ██   ██   ████   ███████       \n", #4
]
A_ANSIREGULAR = [
    "     █████        \n", #0
    "    ██   ██       \n", #1
    "    ███████ █████ \n", #2
    "    ██   ██       \n", #3
    "    ██   ██       \n", #4
]





I_THEEDGE = [
    "    ▄█ \n", #0
    "    ██ \n", #1
    "    ██ \n", #2
    "    ▐█ \n", #3
    "     ▐ \n", #4
    "\n",        #5
    "\n",        #6
]
DONT_THEEDGE = [
    "    ██▄   ████▄    ▄     ▄▄▄▄▀ \n", #0
    "    █  █  █   █     █ ▀▀▀ █    \n", #1
    "    █   █ █   █ ██   █    █    \n", #2
    "    █  █  ▀████ █ █  █   █     \n", #3
    "    ███▀        █  █ █  ▀      \n", #4
    "                █   ██         \n", #5
    "\n",                                #6
]
HAVE_THEEDGE = [
    "     ▄  █ ██       ▄   ▄███▄   \n", #0
    "    █   █ █ █       █  █▀   ▀  \n", #1
    "    ██▀▀█ █▄▄█ █     █ ██▄▄    \n", #2
    "    █   █ █  █  █    █ █▄   ▄▀ \n", #3
    "       █     █   █  █  ▀███▀   \n", #4
    "      ▀     █     █▐           \n", #5
    "           ▀      ▐            \n", #6
]
A_THEEDGE = [
    "    ██   \n", #0
    "    █ █  \n", #1
    "    █▄▄█ \n", #2
    "    █  █ \n", #3
    "       █ \n", #4
    "      █  \n", #5
    "     ▀   \n", #6
]





I_AMCSlash = [
    "    s.  \n", #0
    "    SS. \n", #1
    "    S%S \n", #2
    "    S%S \n", #3
    "    S%S \n", #4
    "    S%S \n", #5
    "    `:; \n", #6
    "    ;,. \n", #7
    "    ;:' \n", #8
]
DONT_AMCSlash = [
    "    .s5SSSs.  .s5SSSs.  .s    s.  .s5SSSSs. \n", #0
    "          SS.       SS.       SS.    SSS    \n", #1
    "    sS    S%S sS    S%S sSs.  S%S    S%S    \n", #2
    "    SS    S%S SS    S%S SS`S. S%S    S%S    \n", #3
    "    SS    S%S SS    S%S SS `S.S%S    S%S    \n", #4
    "    SS    S%S SS    S%S SS  `sS%S    S%S    \n", #5
    "    SS    `:; SS    `:; SS    `:;    `:;    \n", #6
    "    SS    ;,. SS    ;,. SS    ;,.    ;,.    \n", #7
    "    ;;;;;;;:' `:;;;;;:' :;    ;:'    ;:'    \n", #8
]
HAVE_AMCSlash = [
    "    .s    s.  .s5SSSs.  .s    s.  .s5SSSs.  \n", #0
    "          SS.       SS.       SS.       SS. \n", #1
    "    sS    S%S sS    S%S sS    S%S sS    `:; \n", #2
    "    SS    S%S SS    S%S SS    S%S SS        \n", #3
    "    SSSs. S%S SSSs. S%S SS    S%S SSSs.     \n", #4
    "    SS    S%S SS    S%S  SS   S%S SS        \n", #5
    "    SS    `:; SS    `:;  SS   `:; SS        \n", #6
    "    SS    ;,. SS    ;,.   SS  ;,. SS    ;,. \n", #7
    "    :;    ;:' :;    ;:'    `:;;:' `:;;;;;:' \n", #8
]
A_AMCSlash = [
    "    .s5SSSs.  \n", #0
    "          SS. \n", #1
    "    sS    S%S \n", #2
    "    SS    S%S \n", #3
    "    SSSs. S%S \n", #4
    "    SS    S%S \n", #5
    "    SS    `:; \n", #6
    "    SS    ;,. \n", #7
    "    :;    ;:' \n", #8
]





I_DeltaCorpsPriest1 = [
    "     ▄█  \n", #0
    "    ███  \n", #1
    "    ███▌ \n", #2
    "    ███▌ \n", #3
    "    ███▌ \n", #4
    "    ███  \n", #5
    "    ███  \n", #6
    "    █▀   \n", #7
]
DONT_DeltaCorpsPriest1 = [
    "    ████████▄   ▄██████▄  ███▄▄▄▄       ███     \n", #0
    "    ███   ▀███ ███    ███ ███▀▀▀██▄ ▀█████████▄ \n", #1
    "    ███    ███ ███    ███ ███   ███    ▀███▀▀██ \n", #2
    "    ███    ███ ███    ███ ███   ███     ███   ▀ \n", #3
    "    ███    ███ ███    ███ ███   ███     ███     \n", #4
    "    ███    ███ ███    ███ ███   ███     ███     \n", #5
    "    ███   ▄███ ███    ███ ███   ███     ███     \n", #6
    "    ████████▀   ▀██████▀   ▀█   █▀     ▄████▀   \n", #7
]
HAVE_DeltaCorpsPriest1 = [
    "       ▄█    █▄       ▄████████  ▄█    █▄     ▄████████ \n", #0
    "      ███    ███     ███    ███ ███    ███   ███    ███ \n", #1
    "      ███    ███     ███    ███ ███    ███   ███    █▀  \n", #2
    "     ▄███▄▄▄▄███▄▄   ███    ███ ███    ███  ▄███▄▄▄     \n", #3
    "    ▀▀███▀▀▀▀███▀  ▀███████████ ███    ███ ▀▀███▀▀▀     \n", #4
    "      ███    ███     ███    ███ ███    ███   ███    █▄  \n", #5
    "      ███    ███     ███    ███ ███    ███   ███    ███ \n", #6
    "      ███    █▀      ███    █▀   ▀██████▀    ██████████ \n", #7
]
A_DeltaCorpsPriest1 = [
    "       ▄████████ \n", #0
    "      ███    ███ \n", #1
    "      ███    ███ \n", #2
    "      ███    ███ \n", #3
    "    ▀███████████ \n", #4
    "      ███    ███ \n", #5
    "      ███    ███ \n", #6
    "      ███    █▀  \n", #7
]





I_BlurVisionASCII = [
    "    ░▒▓█▓▒░ \n", #0
    "    ░▒▓█▓▒░ \n", #1
    "    ░▒▓█▓▒░ \n", #2
    "    ░▒▓█▓▒░ \n", #3
    "    ░▒▓█▓▒░ \n", #4
    "    ░▒▓█▓▒░ \n", #5
    "    ░▒▓█▓▒░ \n", #6
]
DONT_BlurVisionASCII = [
    "    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░ \n", #0
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #1
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #2
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #3
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #4
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #5
    "    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     \n", #6
]
HAVE_BlurVisionASCII = [
    "    ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ \n", #0
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        \n", #1
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░        \n", #2
    "    ░▒▓████████▓▒░▒▓████████▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░   \n", #3
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        \n", #4
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░        \n", #5
    "    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░ \n", #6
]
A_BlurVisionASCII = [
    "     ░▒▓██████▓▒░  \n", #0
    "    ░▒▓█▓▒░░▒▓█▓▒░ \n", #1
    "    ░▒▓█▓▒░░▒▓█▓▒░ \n", #2
    "    ░▒▓████████▓▒░ \n", #3
    "    ░▒▓█▓▒░░▒▓█▓▒░ \n", #4
    "    ░▒▓█▓▒░░▒▓█▓▒░ \n", #5
    "    ░▒▓█▓▒░░▒▓█▓▒░ \n", #6
]





I_THIS = [
    "     ▄▀▀█▀▄   \n", #0
    "    █   █  █  \n", #1
    "    ▐   █  ▐  \n", #2
    "        █     \n", #3
    "     ▄▀▀▀▀▀▄  \n", #4
    "    █       █ \n", #5
    "    ▐       ▐ \n", #6
]
DONT_THIS = [
    "     ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄ \n", #0
    "    █ ▄▀   █ █      █ █  █ █ █ █    █  ▐ \n", #1
    "    ▐ █    █ █      █ ▐  █  ▀█ ▐   █     \n", #2
    "      █    █ ▀▄    ▄▀   █   █     █      \n", #3
    "     ▄▀▄▄▄▄▀   ▀▀▀▀   ▄▀   █    ▄▀       \n", #4
    "    █     ▐           █    ▐   █         \n", #5
    "    ▐                 ▐        ▐         \n", #6
]
HAVE_THIS = [
    "     ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄ \n", #0
    "    █  █   ▄▀ ▐ ▄▀ ▀▄ █   █    █ ▐  ▄▀   ▐ \n", #1
    "    ▐  █▄▄▄█    █▄▄▄█ ▐  █    █    █▄▄▄▄▄  \n", #2
    "       █   █   ▄▀   █    █   ▄▀    █    ▌  \n", #3
    "      ▄▀  ▄▀  █   ▄▀      ▀▄▀     ▄▀▄▄▄▄   \n", #4
    "     █   █    ▐   ▐               █    ▐   \n", #5
    "     ▐   ▐                        ▐        \n", #6
]
A_THIS = [
    "     ▄▀▀█▄  \n", #0
    "    ▐ ▄▀ ▀▄ \n", #1
    "      █▄▄▄█ \n", #2
    "     ▄▀   █ \n", #3
    "    █   ▄▀  \n", #4
    "    ▐   ▐   \n", #5
    "            \n", #6
]

        















































dogmaticalyric_nums = {
    0: ' ',

    3:  'FINAL.\n',
    12: 'FINAL.\nFINAL.',
    
    22: 'WE\n',
    23: 'WE HAVE,\n',
    28: 'WE HAVE, 12\n',
    30: 'WE HAVE, 12 HOURS\n',
    32: 'WE HAVE, 12 HOURS LEFT.\n',
    
    40: 'WE HAVE, 12 HOURS LEFT.\nWE',
    41: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE,',
    46: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12',
    48: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12 HOURS',
    50: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12 HOURS LEFT.',
    
    61: 'FINAL.\n',
    70: 'FINAL.\nFINAL.',
    
    80: 'WE\n',
    81: 'WE HAVE,\n',
    86: 'WE HAVE, 12\n',
    88: 'WE HAVE, 12 HOURS\n',
    90: 'WE HAVE, 12 HOURS LEFT.\n',
    
    98: 'WE HAVE, 12 HOURS LEFT.\nWE',
    99: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE,',
    104: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12',
    106: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12 HOURS',
    108: 'WE HAVE, 12 HOURS LEFT.\nWE HAVE, 12 HOURS LEFT.',
    
    116: 'Hey!\n',
    120: 'Hey!\nHey!',
    
    125: 'Hey!\n',
    129: 'Hey!\nHEY!',

    133: 'HEY!\n',
    137: 'HEY!\nHEY!',

    141: 'HEY!\n',
    145: 'HEY!\nHEY!',


    150: 'HE-\n',
    151: 'HE-HE-\n',
    152: 'HE-HE-EY!\n',

    154: 'HE-HE-EY!\nHE-',
    155: 'HE-HE-EY!\nHE-HE',
    156: 'HE-HE-EY!\nHE-HE-EY!',

    158: 'HE-\n',
    159: 'HE-HE-\n',
    160: 'HE-HE-EY!\n',

    162: 'HE-HE-EY!\nHE-',
    163: 'HE-HE-EY!\nHE-HE',
    164: 'HE-HE-EY!\nHE-HE-EY!',

    166: 'HE-\n',
    167: 'HE-HE-\n',
    168: 'HE-HE-EY!\n',

    170: 'HE-HE-EY!\nHE-',
    171: 'HE-HE-EY!\nHE-HE',
    172: 'HE-HE-EY!\nHE-HE-EY!',

    174: 'HE-\n',
    175: 'HE-HE-\n',
    176: 'HE-HE-EY!\n',

    178: 'HE-HE-EY!\nHE-',
    179: 'HE-HE-EY!\nHE-HE',
    180: 'HE-HE-EY!\nHE-HE-EY!',

    183: 'HE-\n',
    184: 'HE-HE-\n',
    185: 'HE-HE-EY!\n',

    187: 'HE-HE-EY!\nHE-',
    188: 'HE-HE-EY!\nHE-HE',
    189: 'HE-HE-EY!\nHE-HE-EY!',

    192: 'HE-\n',
    193: 'HE-HE-\n',
    194: 'HE-HE-EY!\n',

    196: 'HE-HE-EY!\nHE-',
    197: 'HE-HE-EY!\nHE-HE',
    198: 'HE-HE-EY!\nHE-HE-EY!',

    200: "CORPSE\n",
    201: "CORPSE LOCKED\n",
    202: "CORPSE LOCKED IN\n",
    203: "CORPSE LOCKED IN MY\n",
    204: "CORPSE LOCKED IN MY BATH-\n",
    205: "CORPSE LOCKED IN MY BATHROOM",

    207: "CORPSE LOCKED IN MY BATHROOM\nBLOOD",
    208: "CORPSE LOCKED IN MY BATHROOM\nBLOOD IS",
    209: "CORPSE LOCKED IN MY BATHROOM\nBLOOD IS IN-",
    210: "CORPSE LOCKED IN MY BATHROOM\nBLOOD IS INSIDE",
    211: "CORPSE LOCKED IN MY BATHROOM\nBLOOD IS INSIDE MY",
    212: "CORPSE LOCKED IN MY BATHROOM\nBLOOD IS INSIDE MY SINK",

    213: "I\n",
    214: "I WAN-\n",
    215: "I WANNA\n",
    216: BE_AMCSLASH_str,
    217: BE_AMCAAA01_str,
    219: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CA-\n",
    220: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATA-\n",
    221: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATO-\n",
    222: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\n",
    223: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE",
    224: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-",
    225: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-I",
    226: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-I CANT",
    227: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-I CANT E-",
    228: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-I CANT EVEN",
    229: "I WANNA B̴̲̗̫̱͆Ė̵̩̳̹͘͜͠ CATATONIC\nWHERE I-I CANT EVEN THINK",

    230: "BLEE-\n",

    231: "BLEE-BLEED-\n",
    232: "BLEE-BLEEDING\n",
    233: "BLEE-BLEEDING OUT\n",
    234: "BLEE-BLEEDING OUT IN-\n",
    235: "BLEE-BLEEDING OUT INSIDE\n",
    236: "BLEE-BLEEDING OUT INSIDE MY\n",
    237: "BLEE-BLEEDING OUT INSIDE MY CLO-\n",
    238: "BLEE-BLEEDING OUT INSIDE MY CLOSET\n",
    239: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE",
    240: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE SE-",
    241: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE SECRETS,",
    243: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE SECRETS, THAT",
    244: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE SECRETS, THAT I",
    245: "BLEE-BLEEDING OUT INSIDE MY CLOSET\nTHE SECRETS, THAT I WILL",
    246: KEEP_AMCAAA01_str,

    248: " WORTH-\n",
    249: "  WORTHLESS\n",
    250: "   WORTHLESS FUCK-\n",
    251: "    WORTHLESS FUCKING\n",
    252: "     WORTHLESS FUCKING CUM\n",
    253: "      WORTHLESS FUCKING CUM DE-\n",
    254: "       WORTHLESS FUCKING CUM DEPO-\n",
    255: "        WORTHLESS FUCKING CUM DEPOSIT\n",
    256: "         WORTHLESS FUCKING CUM DEPOSIT\n",
    257: "          WORTHLESS FUCKING CUM DEPOSIT\n          I-",
    258: "           WORTHLESS FUCKING CUM DEPOSIT\n           I-I",
    259: "            WORTHLESS FUCKING CUM DEPOSIT\n            I-I DON'T",
    260: "             WORTHLESS FUCKING CUM DEPOSIT\n             I-I DON'T E-",
    261: "             WORTHLESS FUCKING CUM DEPOSIT\n             I-I DON'T EVER",
    262: "ME-          WORTHLESS FUCKING CUM DEPOSIT\n             I-I DON'T EVER SLEEP",
    263: "ME-ME-       WORTHLESS FUCKING CUM DEPOSIT\n             I-I DON'T EVER SLEEP",
    264: "ME-ME-ME-    WORTHLESS FUCKING CUM DEPOSIT\n             I-I DON'T EVER SLEEP",

    265: "ME-ME-ME-   MEN-\n",
    266: "ME-ME-ME-  MENTAL\n",
    267: "ME-ME-ME  MENTAL SHARDS\n",
    268: "ME-ME-M  MENTAL SHARDS IN-\n",
    269: "ME-ME-  MENTAL SHARDS INSIDE\n",
    270: "ME-ME  MENTAL SHARDS INSIDE MY\n",
    271: "ME-M  MENTAL SHARDS INSIDE MY VO-\n",
    272: "ME-  MENTAL SHARDS INSIDE MY VOMIT\n",
    273: "M  MENTAL SHARDS INSIDE MY VOMIT\n",
    274: "  MENTAL SHARDS INSIDE MY VOMIT\n  GUN",
    275: " MENTAL SHARDS INSIDE MY VOMIT\n GUN",
    276: "MENTAL SHARDS INSIDE MY VOMIT\nGUN SHOTS",
    277: "MENTAL SHARDS INSIDE MY VOMIT\nGUN SHOTS THROUGH",
    278: "MENTAL SHARDS INSIDE MY VOMIT\nGUN SHOTS THROUGH THE",
    279: "MENTAL SHARDS INSIDE MY VOMIT\nGUN SHOTS THROUGH THE DOOR",

    281: "I",
    282: "I CAN",
    283: "I CAN TAKE",
    284: "I CAN TAKE JUST",
    285: "I CAN TAKE JUST WHAT",
    286: "I CAN TAKE JUST WHAT I",
    287: "I CAN TAKE JUST WHAT I WAN-",
    288: "I CAN TAKE JUST WHAT I WANTED",

    289: "WHEN",
    290: "WHEN I-",
    291: "WHEN I-I",
    292: "WHEN I-I SET-",
    293: "WHEN I-I SETTLE",
    294: "WHEN I-I SETTLE THE",
    295: "WHEN I-I SETTLE THE SCORE",

    296: "CU-\n",
    297: "CU-CUT\n",
    298: "CU-CUT MY-\n",
    299: "CU-CUT MYSELF\n",
    300: "CU-CUT MYSELF UP\n",
    301: "CU-CUT MYSELF UP IN\n", 
    302: "CU-CUT MYSELF UP IN A\n",
    303: "CU-CUT MYSELF UP IN A RIB-\n",
    304: "CU-CUT MYSELF UP IN A RIBBONS\n",

    307: "CU-CUT MYSELF UP IN A RIBBONS\nALL-",
    308: "CU-CUT MYSELF UP IN A RIBBONS\nALL-ALL",
    309: "CU-CUT MYSELF UP IN A RIBBONS\nALL-ALL O-",
    310: "CU-CUT MYSELF UP IN A RIBBONS\nALL-ALL OVER",
    311: "CU-CUT MYSELF UP IN A RIBBONS\nALL-ALL OVER THE",
    312: "CU-CUT MYSELF UP IN A RIBBONS\nALL-ALL OVER THE FLOOR",

    314: "I",
    315: "I GOT",
    316: "I GOT BITE",
    317: "I GOT BITE MARKS",
    318: "I GOT BITE MARKS ON",
    319: "I GOT BITE MARKS ON MY",
    320: "I GOT BITE MARKS ON MY STO-",
    321: "I GOT BITE MARKS ON MY STOMACH\n",
    322: "I GOT BITE MARKS ON MY STOMACH\nTHAT",
    323: "I GOT BITE MARKS ON MY STOMACH\nTHAT WERE-",
    324: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T",

    327: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE",
    328: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE BE-",
    329: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE BEFORE\n"+BEFORE_BLURVISIONASCII_str,
    330: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE BEFORE\n"+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str,
    331: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE BEFORE\n"+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str,
    332: "I GOT BITE MARKS ON MY STOMACH\nTHAT WEREN'T HERE BEFORE\n"+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str+BEFORE_BLURVISIONASCII_str,


    333: "BLOOD",

    336: "BLOOD BE-",
    337: "BLOOD BEHIND", 
    338: "BLOOD BEHIND MY",

    339: "BLOOD BEHIND MY EYES",
    340: "BLOOD BEHIND MY EYES WHEN",

    342: "BLOOD BEHIND MY EYES WHEN\nI",
    343: "BLOOD BEHIND MY EYES WHEN\nI TRY",
    344: "BLOOD BEHIND MY EYES WHEN\nI TRY TO", 
    345: "BLOOD BEHIND MY EYES WHEN\nI TRY TO SLEEP",
    346: "BLOOD BEHIND MY EYES WHEN\nI TRY TO SLEEP AT",
    347: "BLOOD BEHIND MY EYES WHEN\nI TRY TO SLEEP AT NIGHT",


    349: "GO-",

    351: "GOING",

    354: "GOING MISS-",
    355: "GOING MISSING", 
    356: "GOING MISSING WHEN\n",
    357: "GOING MISSING WHEN\nMY",

    359: "GOING MISSING WHEN\nMY MIND",

    361: "GOING MISSING WHEN\nMY MIND TURNS", 
    362: "GOING MISSING WHEN\nMY MIND TURNS OUT",
    363: "GOING MISSING WHEN\nMY MIND TURNS OUT THE",
    364: "GOING MISSING WHEN\nMY MIND TURNS OUT THE LIGHTS",

    367: I_BIG[0]+I_BIG[1]+I_BIG[2]+I_BIG[3]+I_BIG[4]+I_BIG[5], 
    368: DONT_BIG[0]+DONT_BIG[1]+DONT_BIG[2]+DONT_BIG[3]+DONT_BIG[4]+DONT_BIG[5],
    369: HAVE_BIG[0]+HAVE_BIG[1]+HAVE_BIG[2]+HAVE_BIG[3]+HAVE_BIG[4]+HAVE_BIG[5],
    370: A_BIG[0]+A_BIG[1]+A_BIG[2]+A_BIG[3]+A_BIG[4]+A_BIG[5],
    371: I_SBLOOD[0]+I_SBLOOD[1]+I_SBLOOD[2]+I_SBLOOD[3]+I_SBLOOD[4], 
    372: DONT_SBLOOD[0]+DONT_SBLOOD[1]+DONT_SBLOOD[2]+DONT_SBLOOD[3]+DONT_SBLOOD[4], 
    373: HAVE_SBLOOD[0]+HAVE_SBLOOD[1]+HAVE_SBLOOD[2]+HAVE_SBLOOD[3]+HAVE_SBLOOD[4],
    374: A_SBLOOD[0]+A_SBLOOD[1]+A_SBLOOD[2]+A_SBLOOD[3]+A_SBLOOD[4],
    375: I_ANSIREGULAR[0]+I_ANSIREGULAR[1]+I_ANSIREGULAR[2]+I_ANSIREGULAR[3]+I_ANSIREGULAR[4],
    376: DONT_ANSIREGULAR[0]+DONT_ANSIREGULAR[1]+DONT_ANSIREGULAR[2]+DONT_ANSIREGULAR[3]+DONT_ANSIREGULAR[4],
    377: HAVE_ANSIREGULAR[0]+HAVE_ANSIREGULAR[1]+HAVE_ANSIREGULAR[2]+HAVE_ANSIREGULAR[3]+HAVE_ANSIREGULAR[4],
    378: A_ANSIREGULAR[0]+A_ANSIREGULAR[1]+A_ANSIREGULAR[2]+A_ANSIREGULAR[3]+A_ANSIREGULAR[4],
    379: I_THEEDGE[0]+I_THEEDGE[1]+I_THEEDGE[2]+I_THEEDGE[3]+I_THEEDGE[4]+I_THEEDGE[5]+I_THEEDGE[6],  
    380: DONT_THEEDGE[0]+DONT_THEEDGE[1]+DONT_THEEDGE[2]+DONT_THEEDGE[3]+DONT_THEEDGE[4]+DONT_THEEDGE[5]+DONT_THEEDGE[6],
    381: HAVE_THEEDGE[0]+HAVE_THEEDGE[1]+HAVE_THEEDGE[2]+HAVE_THEEDGE[3]+HAVE_THEEDGE[4]+HAVE_THEEDGE[5]+HAVE_THEEDGE[6],
    382: A_THEEDGE[0]+A_THEEDGE[1]+A_THEEDGE[2]+A_THEEDGE[3]+A_THEEDGE[4]+A_THEEDGE[5]+A_THEEDGE[6],
    383: I_AMCSlash[0]+I_AMCSlash[1]+I_AMCSlash[2]+I_AMCSlash[3]+I_AMCSlash[4]+I_AMCSlash[5]+I_AMCSlash[6]+I_AMCSlash[7]+I_AMCSlash[8],
    384: DONT_AMCSlash[0]+DONT_AMCSlash[1]+DONT_AMCSlash[2]+DONT_AMCSlash[3]+DONT_AMCSlash[4]+DONT_AMCSlash[5]+DONT_AMCSlash[6]+DONT_AMCSlash[7]+DONT_AMCSlash[8], 
    385: HAVE_AMCSlash[0]+HAVE_AMCSlash[1]+HAVE_AMCSlash[2]+HAVE_AMCSlash[3]+HAVE_AMCSlash[4]+HAVE_AMCSlash[5]+HAVE_AMCSlash[6]+HAVE_AMCSlash[7]+HAVE_AMCSlash[8], 
    386: A_AMCSlash[0]+A_AMCSlash[1]+A_AMCSlash[2]+A_AMCSlash[3]+A_AMCSlash[4]+A_AMCSlash[5]+A_AMCSlash[6]+A_AMCSlash[7]+A_AMCSlash[8], 
    387: I_DeltaCorpsPriest1[0]+I_DeltaCorpsPriest1[1]+I_DeltaCorpsPriest1[2]+I_DeltaCorpsPriest1[3]+I_DeltaCorpsPriest1[4]+I_DeltaCorpsPriest1[5]+I_DeltaCorpsPriest1[6]+I_DeltaCorpsPriest1[7], 
    388: DONT_DeltaCorpsPriest1[0]+DONT_DeltaCorpsPriest1[1]+DONT_DeltaCorpsPriest1[2]+DONT_DeltaCorpsPriest1[3]+DONT_DeltaCorpsPriest1[4]+DONT_DeltaCorpsPriest1[5]+DONT_DeltaCorpsPriest1[6]+DONT_DeltaCorpsPriest1[7], 
    389: HAVE_DeltaCorpsPriest1[0]+HAVE_DeltaCorpsPriest1[1]+HAVE_DeltaCorpsPriest1[2]+HAVE_DeltaCorpsPriest1[3]+HAVE_DeltaCorpsPriest1[4]+HAVE_DeltaCorpsPriest1[5]+HAVE_DeltaCorpsPriest1[6]+HAVE_DeltaCorpsPriest1[7],
    390: A_DeltaCorpsPriest1[0]+A_DeltaCorpsPriest1[1]+A_DeltaCorpsPriest1[2]+A_DeltaCorpsPriest1[3]+A_DeltaCorpsPriest1[4]+A_DeltaCorpsPriest1[5]+A_DeltaCorpsPriest1[6]+A_DeltaCorpsPriest1[7], 
    391: I_BlurVisionASCII[0]+I_BlurVisionASCII[1]+I_BlurVisionASCII[2]+I_BlurVisionASCII[3]+I_BlurVisionASCII[4]+I_BlurVisionASCII[5]+I_BlurVisionASCII[6], 
    392: DONT_BlurVisionASCII[0]+DONT_BlurVisionASCII[1]+DONT_BlurVisionASCII[2]+DONT_BlurVisionASCII[3]+DONT_BlurVisionASCII[4]+DONT_BlurVisionASCII[5]+DONT_BlurVisionASCII[6], 
    393: HAVE_BlurVisionASCII[0]+HAVE_BlurVisionASCII[1]+HAVE_BlurVisionASCII[2]+HAVE_BlurVisionASCII[3]+HAVE_BlurVisionASCII[4]+HAVE_BlurVisionASCII[5]+HAVE_BlurVisionASCII[6], 
    394: A_BlurVisionASCII[0]+A_BlurVisionASCII[1]+A_BlurVisionASCII[2]+A_BlurVisionASCII[3]+A_BlurVisionASCII[4]+A_BlurVisionASCII[5]+A_BlurVisionASCII[6], 
    395: I_THIS[0]+I_THIS[1]+I_THIS[2]+I_THIS[3]+I_THIS[4]+I_THIS[5]+I_THIS[6], 
    396: DONT_THIS[0]+DONT_THIS[1]+DONT_THIS[2]+DONT_THIS[3]+DONT_THIS[4]+DONT_THIS[5]+DONT_THIS[6], 
    397: HAVE_THIS[0]+HAVE_THIS[1]+HAVE_THIS[2]+HAVE_THIS[3]+HAVE_THIS[4]+HAVE_THIS[5]+HAVE_THIS[6], 
    398: A_THIS[0]+A_THIS[1]+A_THIS[2]+A_THIS[3]+A_THIS[4]+A_THIS[5]+A_THIS[6], 

    402: OH_ANSIREGULAR_str,
    403: MY_ANSIREGULAR_str,
    405: GOD_ANSIREGULAR_str,

    407: SHUT_THEEDGE_str,
    409: THE_THIS_str,
    410: FUCK_THIS_str,
    412: UP_BLOODY_str,


    416: 'budubudum',
    421: 'budubudumx2',
    425: 'budubudumx3',
    429: 'budubudumx4',
    433: 'budu',

    435: 'THINK',
    437: 'THINK TWICE',
    439: 'THINK TWICE\nTHINK',
    441: 'THINK TWICE\nTHINK TWICE',

    443: 'THINK',
    445: 'THINK TWICE',
    448: 'THINK TWICE\nTHINK',
    450: TWICE_BLOODY_str,
    451: TWICE_BLOODY_str+TWICE_BLOODY_str,
    452: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,
    453: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,
    454: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,
    455: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,
    456: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,
    457: TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str+TWICE_BLOODY_str,

    468: 'I-',
    469: 'I-I',
    470: 'I-I WILL',
    471: 'I-I WILL BE',
    472: 'I-I WILL BE IN',
    473: 'I-I WILL BE IN LOVE',
    474: 'I-I WILL BE IN LOVE FOR-',
    475: 'I-I WILL BE IN LOVE FORE-',
    476: 'I-I WILL BE IN LOVE FOREVER',

    477: 'CUZ',
    478: 'CUZ IM',
    479: 'CUZ IM GON-',
    480: 'CUZ IM GONNA',
    481: 'CUZ IM GONNA DIE',
    482: 'CUZ IM GONNA DIE TO-',
    483: TONIGHT_BLOODY_str,


    496: TONIGHT_BLOODY_str+TONIGHT_BLOODY_str,
    497: TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str,
    498: TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str,
    499: TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str+TONIGHT_BLOODY_str,

    502: SO_THEEDGE_str,
    504: PLEASE_THEEDGE_str,
    506: JUST_THEEDGE_str,
    508: HOLD_THEEDGE_str,
    510: ME_THEEDGE_str,
    513: ONE_THEEDGE_str,
    515: LAST_THEEDGE_str,

    517: TIME_BLOODY_str,

    518: TIME_BLOODY_str+TIME_BLOODY_str,
    519: TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str,
    520: TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str,
    521: TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str,
    522: TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str,
    523: TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str+TIME_BLOODY_str,

    
    535: "BE-\n",
    536: "BEFORE\n",
    537: "BEFORE I\n",
    538: "BEFORE I BLOOM\n",
    539: "BEFORE I BLOOM IN-\n",
    540: "BEFORE I BLOOM INTO\n",
    541: "BEFORE I BLOOM INTO A\n",
    542: "BEFORE I BLOOM INTO A FLO-\n",
    543: "BEFORE I BLOOM INTO A FLOWER\n",
    544: "BEFORE I BLOOM INTO A FLOWER\nFIRST",
    545: "BEFORE I BLOOM INTO A FLOWER\nFIRST I",
    546: "BEFORE I BLOOM INTO A FLOWER\nFIRST I WAN-",
    547: "BEFORE I BLOOM INTO A FLOWER\nFIRST I WANNA",
    548: "BEFORE I BLOOM INTO A FLOWER\nFIRST I WANNA SAY",
    549: "BEFORE I BLOOM INTO A FLOWER\nFIRST I WANNA SAY GOOD-",
    550: GOODBYE_BLOODY_str,
    
    562: AAH_BLOODY_str,
    566: 'aaahhh',

    608: 'bleahhhx1',
    609: 'bleahhhx2',
    610: 'bleahhhx3',
    611: 'bleahhhx4',

    612: 'bleahhhx5',
    613: 'bleahhhx6',
    614: 'bleahhhx7',
    615: 'bleahhhx8',

    642: 'bleahhh x1',
    643: 'bleahhh x2',
    644: 'bleahhh x3',
    645: 'bleahhh x4',

    646: 'bleahhh x5',
    647: 'bleahhh x6',
    648: 'bleahhh x7',
    649: 'bleahhh x8',

    675: 'bleahhh  x1',
    676: 'bleahhh  x2',
    677: 'bleahhh  x3',
    678: 'bleahhh  x4',

    679: 'bleahhh  x5',
    680: 'bleahhh  x6',
    681: 'bleahhh  x7',
    682: 'bleahhh  x8',

    689: 'Trans-',
    692: 'Transfor-',
    693: 'Transforma-',
    694: 'Transformation',

    }

asd = {







   

    
    #Transformation complete You are now, as you once were. Beautiful. You are Dogmatica
    
#   _____ _    _ _    _ _______ 
#  / ____| |  | | |  | |__   __|
# | (___ | |__| | |  | |  | |   
#  \___ \|  __  | |  | |  | |      Font Name: Big
#  ____) | |  | | |__| |  | |   
# |_____/|_|  |_|\____/   |_|   

# ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
# ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░       Font Name: BlurVision ASCII
#       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
#       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░     
#░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░     

#   SSSSSSSSSSSSSSS HHHHHHHHH     HHHHHHHHHUUUUUUUU     UUUUUUUUTTTTTTTTTTTTTTTTTTTTTTT
# SS:::::::::::::::SH:::::::H     H:::::::HU::::::U     U::::::UT:::::::::::::::::::::T
#S:::::SSSSSS::::::SH:::::::H     H:::::::HU::::::U     U::::::UT:::::::::::::::::::::T
#S:::::S     SSSSSSSHH::::::H     H::::::HHUU:::::U     U:::::UUT:::::TT:::::::TT:::::T
#S:::::S              H:::::H     H:::::H   U:::::U     U:::::U TTTTTT  T:::::T  TTTTTT
#S:::::S              H:::::H     H:::::H   U:::::D     D:::::U         T:::::T        
# S::::SSSS           H::::::HHHHH::::::H   U:::::D     D:::::U         T:::::T        
#  SS::::::SSSSS      H:::::::::::::::::H   U:::::D     D:::::U         T:::::T            Font Name: Doh
#    SSS::::::::SS    H:::::::::::::::::H   U:::::D     D:::::U         T:::::T        
#       SSSSSS::::S   H::::::HHHHH::::::H   U:::::D     D:::::U         T:::::T        
#            S:::::S  H:::::H     H:::::H   U:::::D     D:::::U         T:::::T        
#            S:::::S  H:::::H     H:::::H   U::::::U   U::::::U         T:::::T        
#SSSSSSS     S:::::SHH::::::H     H::::::HH U:::::::UUU:::::::U       TT:::::::TT      
#S::::::SSSSSS:::::SH:::::::H     H:::::::H  UU:::::::::::::UU        T:::::::::T      
#S:::::::::::::::SS H:::::::H     H:::::::H    UU:::::::::UU          T:::::::::T      
# SSSSSSSSSSSSSSS   HHHHHHHHH     HHHHHHHHH      UUUUUUUUU            TTTTTTTTTTT      

#███████ ██   ██ ██    ██ ████████ 
#██      ██   ██ ██    ██    ██    
#███████ ███████ ██    ██    ██      Font Name: ANSI Regular
#     ██ ██   ██ ██    ██    ██    
#███████ ██   ██  ██████     ██    





#  ██████  ██░ ██  █    ██ ▄▄▄█████▓
#▒██    ▒ ▓██░ ██▒ ██  ▓██▒▓  ██▒ ▓▒
#░ ▓██▄   ▒██▀▀██░▓██  ▒██░▒ ▓██░ ▒░   Font Name: Bloody
#  ▒   ██▒░▓█ ░██ ▓▓█  ░██░░ ▓██▓ ░ 
#▒██████▒▒░▓█▒░██▓▒▒█████▓   ▒██▒ ░ 
#▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▒▓▒ ▒ ▒   ▒ ░░   
#░ ░▒  ░ ░ ▒ ░▒░ ░░░▒░ ░ ░     ░    
#░  ░  ░   ░  ░░ ░ ░░░ ░ ░   ░      
#      ░   ░  ░  ░   ░              
#                                   





#   ▄████████    ▄█    █▄    ███    █▄      ███     
#  ███    ███   ███    ███   ███    ███ ▀█████████▄ 
#  ███    █▀    ███    ███   ███    ███    ▀███▀▀██ 
#  ███         ▄███▄▄▄▄███▄▄ ███    ███     ███   ▀ 
#▀███████████ ▀▀███▀▀▀▀███▀  ███    ███     ███        Font Name: Delta Corps Priest 1
#         ███   ███    ███   ███    ███     ███     
#   ▄█    ███   ███    ███   ███    ███     ███     
# ▄████████▀    ███    █▀    ████████▀     ▄████▀   

# ▄▀▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀█▀▀▄ 
#█ █   ▐ █  █   ▄▀ █   █    █ █    █  ▐ 
#   ▀▄   ▐  █▄▄▄█  ▐  █    █  ▐   █     
#▀▄   █     █   █    █    █      █          Font Name: THIS
# █▀▀▀     ▄▀  ▄▀     ▀▄▄▄▄▀   ▄▀       
# ▐       █   █               █         
#        ▐   ▐               ▐         

#   ▄▄▄▄▄    ▄  █   ▄     ▄▄▄▄▀ 
#  █     ▀▄ █   █    █ ▀▀▀ █    
#▄  ▀▀▀▀▄   ██▀▀█ █   █    █       Font Name: The Edge
# ▀▄▄▄▄▀    █   █ █   █   █     
#              █  █▄ ▄█  ▀      
#             ▀    ▀▀▀          

#  @@@@@@ @@@  @@@ @@@  @@@ @@@@@@@
# !@@     @@!  @@@ @@!  @@@   @@!  
#  !@@!!  @!@!@!@! @!@  !@!   @!!       Font Name: S Blood
#     !:! !!:  !!! !!:  !!!   !!:  
# ::.: :   :   : :  :.:: :     :   





#   sSSs   .S    S.    .S       S.   sdSS_SSSSSSbs  
#  d%%SP  .SS    SS.  .SS       SS.  YSSS~S%SSSSSP  
# d%S'    S%S    S%S  S%S       S%S       S%S       
# S%|     S%S    S%S  S%S       S%S       S%S       
# S&S     S%S SSSS%S  S&S       S&S       S&S       
# Y&Ss    S&S  SSS&S  S&S       S&S       S&S            Font Name: AMC AAA01
# `S&&S   S&S    S&S  S&S       S&S       S&S       
#   `S*S  S&S    S&S  S&S       S&S       S&S       
#    l*S  S*S    S*S  S*b       d*S       S*S       
#   .S*P  S*S    S*S  S*S.     .S*S       S*S       
# sSS*S   S*S    S*S   SSSbs_sdSSS        S*S       
# YSS'    SSS    S*S    YSSP~YSSY         S*S       
#                SP                       SP        
#                Y                        Y         

#.s5SSSs.  .s    s.  .s    s.  .s5SSSSs. 
#      SS.       SS.       SS.    SSS    
#sS    `:; sS    S%S sS    S%S    S%S    
#SS        SS    S%S SS    S%S    S%S    
#`:;;;;.   SSSs. S%S SS    S%S    S%S       Font Name: AMC Slash
#      ;;. SS    S%S SS    S%S    S%S    
#      `:; SS    `:; SS    `:;    `:;    
#.,;   ;,. SS    ;,. SS    ;,.    ;,.    
#`:;;;;;:' :;    ;:' `:;;;;;:'    ;:'    




  






















}













cinemapart = False



dir_to_file_FOLDER = os.path.dirname(os.path.realpath(__file__)).replace('/','\\')
files = {
'icon': dir_to_file_FOLDER+'\\Data\\tokegotchi ico.jpg',

'song': dir_to_file_FOLDER+'\\Data\\DOGMATICA.wav',
'paw': dir_to_file_FOLDER+'\\Data\\dogmatica paw (i cant draw bro waaah waaaaah).png',
'pawmirror': dir_to_file_FOLDER+'\\Data\\dogmatica paw (i cant draw bro waaah waaaaah) mirrored.png',

'facebase': dir_to_file_FOLDER+'\\Data\\dogmatica face base+eyes.png',
'faceeyesdetail': dir_to_file_FOLDER+'\\Data\\dogmatica face eyes detail.png',
'facemouthclosed': dir_to_file_FOLDER+'\\Data\\dogmatica face mouth closed.png',
'facemouthopened': dir_to_file_FOLDER+'\\Data\\dogmatica face mouth opened.png',
    }
    
    

pygame.mixer.init()

pygame.display.init()

pygame.font.init()

desktopres = pygame.display.get_desktop_sizes()[0]
standardres = (1920,1080)
desktopscale = (standardres[0]/desktopres[0],standardres[1]/desktopres[1])

windowmain = pygame.Window('windowmain',desktopres,(0,0),
                            borderless=True,
                            resizable=False,
                            always_on_top=True) 
#pygame-ce exclusive, may be buggy
windowmain.hide()
windowmainsurface = windowmain.get_surface()
windowmainsurface.fill((0,255,0))
windowmain.flip()


icon = pygame.image.load(files['icon'])
windowmain.set_icon(icon)


import win32api
import win32con
import win32gui
windowmaininfo = win32gui.FindWindowEx(None, None, None, 'windowmain')

win32gui.SetWindowLong(windowmaininfo, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(windowmaininfo, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(windowmaininfo, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)

windowmain.title = ' '


pawsurface = pygame.transform.scale(pygame.image.load(files['paw']),(desktopres[1],desktopres[1]))
pawmirrorsurface = pygame.transform.scale(pygame.image.load(files['pawmirror']),(desktopres[1],desktopres[1]))
facebasesurface = pygame.image.load(files['facebase'])
faceeyesdetailsurface = pygame.image.load(files['faceeyesdetail'])
facemouthclosedsurface = pygame.image.load(files['facemouthclosed'])
facemouthopenedsurface = pygame.image.load(files['facemouthopened'])



def fonts_faith_collapsing(size):
    return pygame.Font(dir_to_file_FOLDER+'\\Data\\fonts\\faith_collapsing\\Faith Collapsing.ttf',size)

def fonts_ithorn(size):
    return pygame.Font(dir_to_file_FOLDER+'\\Data\\fonts\\IthornЙt.otf',size)

def fonts_unifont(size):
    return pygame.Font(dir_to_file_FOLDER+'\\Data\\fonts\\unifont-17.0.04.otf',size)


window1 = pygame.Window('window1',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window1.set_icon(icon)
window1surface = window1.get_surface()
window1surface.fill((0,255,0))
window1.flip()
window1info = win32gui.FindWindowEx(None, None, None, 'window1')
win32gui.SetWindowLong(window1info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window1info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window1info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window1.title = ' '
window1.hide()

window2 = pygame.Window('window2',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window2.set_icon(icon)
window2surface = window2.get_surface()
window2surface.fill((0,255,0))
window2.flip()
window2info = win32gui.FindWindowEx(None, None, None, 'window2')
win32gui.SetWindowLong(window2info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window2info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window2info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window2.title = ' '
window2.hide()

window3 = pygame.Window('window3',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window3.set_icon(icon)
window3surface = window3.get_surface()
window3surface.fill((0,255,0))
window3.flip()
window3info = win32gui.FindWindowEx(None, None, None, 'window3')
win32gui.SetWindowLong(window3info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window3info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window3info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window3.title = ' '
window3.hide()

window4 = pygame.Window('window4',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window4.set_icon(icon)
window4surface = window4.get_surface()
window4surface.fill((0,255,0))
window4.flip()
window4info = win32gui.FindWindowEx(None, None, None, 'window4')
win32gui.SetWindowLong(window4info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window4info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window4info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window4.title = ' '
window4.hide()

window5 = pygame.Window('window5',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window5.set_icon(icon)
window5surface = window5.get_surface()
window5surface.fill((0,255,0))
window5.flip()
window5info = win32gui.FindWindowEx(None, None, None, 'window5')
win32gui.SetWindowLong(window5info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window5info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window5info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window5.title = ' '
window5.hide()

window6 = pygame.Window('window6',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window6.set_icon(icon)
window6surface = window6.get_surface()
window6surface.fill((0,255,0))
window6.flip()
window6info = win32gui.FindWindowEx(None, None, None, 'window6')
win32gui.SetWindowLong(window6info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window6info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window6info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window6.title = ' '
window6.hide()

window7 = pygame.Window('window7',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window7.set_icon(icon)
window7surface = window7.get_surface()
window7surface.fill((0,255,0))
window7.flip()
window7info = win32gui.FindWindowEx(None, None, None, 'window7')
win32gui.SetWindowLong(window7info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window7info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window7info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window7.title = ' '
window7.hide()

window8 = pygame.Window('window8',(1,1),(-100,-100),
                        resizable=False,
                        always_on_top=True,
                        utility=True)
window8.set_icon(icon)
window8surface = window8.get_surface()
window8surface.fill((0,255,0))
window8.flip()
window8info = win32gui.FindWindowEx(None, None, None, 'window8')
win32gui.SetWindowLong(window8info, 
                       win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(window8info, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(window8info, win32api.RGB(*(0,255,0)), 0, win32con.LWA_COLORKEY)
window8.title = ' '
window8.hide()

windows_list = [windowmain,
                window1,
                window2,
                window3,
                window4,
                window5,
                window6,
                window7,
                window8,]
windowsurfaces_list = [windowmainsurface,
                       window1surface,
                       window2surface,
                       window3surface,
                       window4surface,
                       window5surface,
                       window6surface,
                       window7surface,
                       window8surface,]
windowcurrent = 0



facebasesurface_scales_prerender = []
faceeyesdetailsurface_scales_prerender = []
facemouthclosedsurface_scales_prerender = []
facemouthopenedsurface_scales_prerender = []
num = 10
while num <= 30:
    facebasesurface_scales_prerender.append(pygame.transform.scale(facebasesurface,(256*(num/10),256*(num/10))))
    faceeyesdetailsurface_scales_prerender.append(pygame.transform.scale(faceeyesdetailsurface,(256*(num/10),256*(num/10))))
    facemouthclosedsurface_scales_prerender.append(pygame.transform.scale(facemouthclosedsurface,(256*(num/10),256*(num/10))))
    facemouthopenedsurface_scales_prerender.append(pygame.transform.scale(facemouthopenedsurface,(256*(num/10),256*(num/10))))

    num += 1



CLOCK = pygame.Clock()

def fourthwallbreak(Startingtime):

    global windows_list
    global windowsurfaces_list
    global windowcurrent

    windows_list[windowcurrent].show()
    windows_list[windowcurrent].set_icon(icon)
    
    global facebasesurface
    global faceeyesdetailsurface
    
    eyedetailstate = False

    shakeface = 0
    shakemouth = 0
    facezoom = 1

    animtime = 0

    facemouthsurface_changed = facemouthclosedsurface

    #код говнище. похуй.
    while animtime < 3.840:
        try:
            animtime = time.perf_counter() - Startingtime

            animtimems = int(animtime*1000)


            if animtimems in range(800,2560): #clearing screen
                windowsurfaces_list[windowcurrent].fill((0,255,0))

            if animtimems in range(1120,2560): #paw 1 appear
                pawshake = 0
                if animtimems-1120 <= 160:
                    pawshake = abs((animtimems-1280) / 160)
                windowsurfaces_list[windowcurrent].blit(pawsurface,(0-(pawsurface.get_width()//2)+((pawsurface.get_width()//16)*((1-(random.random()*2))*pawshake))+((256*facezoom)//16)*((1-(random.random()*2)*shakeface)),
                                                                    0+((pawsurface.get_height()//16)*((1-(random.random()*2))*pawshake))+((256*facezoom)//16)*((1-(random.random()*2)*shakeface))))
                
            if animtimems in range(1600,2560): #paw 2 appear
                pawshake = 0
                if animtimems-1600 <= 160:
                    pawshake = abs((animtimems-1760) / 160)
                windowsurfaces_list[windowcurrent].blit(pawmirrorsurface,(desktopres[0]-(pawsurface.get_width()//2)+((pawsurface.get_width()//16)*((1-(random.random()*2))*pawshake))+((256*facezoom)//16)*((1-(random.random()*2)*shakeface)),
                                                                          0+((pawsurface.get_height()//16)*((1-(random.random()*2))*pawshake))+((256*facezoom)//16)*((1-(random.random()*2)*shakeface))))

            if animtimems in range(160,640): #rolling in dogmatica face render
                rollingin = (animtimems-160) / 480 * 10

                wholefacex = (desktopres[0]//2)-(facebasesurface.get_width()//2+110)+((desktopres[0]//2)/rollingin)
                wholefacey = (desktopres[1]//2)-(facebasesurface.get_height()//2)+((facebasesurface.get_height()//8)*(1-(random.random()*2)))
                
                windowsurfaces_list[windowcurrent].blit(facebasesurface,(wholefacex,
                                                                                wholefacey))

                windowsurfaces_list[windowcurrent].blit(facemouthsurface_changed,(wholefacex,
                                                                                  wholefacey))

                    
            if animtimems in range(640,2560): #staying still dogmatica face render
                
                wholefacex = (desktopres[0]//2)-((facebasesurface.get_width())//2)+((facemouthopenedsurface.get_height())//16)*((1-(random.random()*2)*shakeface))
                wholefacey = (desktopres[1]//2)-((facebasesurface.get_height())//2)+((facemouthopenedsurface.get_height())//16)*((1-(random.random()*2)*shakeface))
                
                windowsurfaces_list[windowcurrent].blit(facebasesurface,(wholefacex,
                                                                         wholefacey))

                if eyedetailstate:
                    windowsurfaces_list[windowcurrent].blit(faceeyesdetailsurface,(wholefacex,
                                                                                   wholefacey))

                windowsurfaces_list[windowcurrent].blit(facemouthsurface_changed,(wholefacex+((256*facezoom)//16)*((1-(random.random()*2)*shakemouth)),
                                                                                  wholefacey+((256*facezoom)//16)*((1-(random.random()*2)*shakemouth))))
                

            if animtimems in range(320,480): #OH
                if animtimems >= 420:
                    facemouthsurface_changed = facemouthclosedsurface
                else: 
                    facemouthsurface_changed = facemouthopenedsurface
            if animtimems in range(480,800): #MY
                if animtimems >= 720:
                    facemouthsurface_changed = facemouthclosedsurface
                else: 
                    facemouthsurface_changed = facemouthopenedsurface
            if animtimems in range(800,1120): #GOD
                shakemouth = abs((animtimems-1120) / 320)

                if animtimems >= 1040:
                    facemouthsurface_changed = facemouthclosedsurface
                else: 
                    facemouthsurface_changed = facemouthopenedsurface
            if animtimems in range(1120,1440): #SHUT
                facezoom = round(1+((animtimems-1120)/320*2),1)
                #^^^ this bullshit causes a massive fps drop but only when RENDERED, not when we are creating surfaces like below
                #i have NO IDEA how to optimize this shit, ive tried EVERYTHING I COULD THINK OF FOR 2 HOURS STRAIGHT

                facebasesurface = facebasesurface_scales_prerender[int((facezoom-1)*10)]
                faceeyesdetailsurface = faceeyesdetailsurface_scales_prerender[int((facezoom-1)*10)]
                facemouthsurface_changed = facemouthopenedsurface_scales_prerender[int((facezoom-1)*10)]

                shakemouth = 1
                
                eyedetailstate = True

                if animtimems >= 1280:
                    facemouthsurface_changed = facemouthclosedsurface_scales_prerender[int((facezoom-1)*10)]
                else: 
                    facemouthsurface_changed = facemouthopenedsurface_scales_prerender[int((facezoom-1)*10)]
            if animtimems in range(1440,1600): #THE
                shakemouth = 1
                if animtimems >= 1520:
                    facemouthsurface_changed = facemouthclosedsurface_scales_prerender[int((facezoom-1)*10)]
                else: 
                    facemouthsurface_changed = facemouthopenedsurface_scales_prerender[int((facezoom-1)*10)]
            if animtimems in range(1600,1920): #FUCK
                shakeface = abs((animtimems-1600) / 320)
                shakemouth = 2
                if animtimems >= 1840:
                    facemouthsurface_changed = facemouthclosedsurface_scales_prerender[int((facezoom-1)*10)]
                else: 
                    facemouthsurface_changed = facemouthopenedsurface_scales_prerender[int((facezoom-1)*10)]
            if animtimems in range(1920,2100): #UP!
                shakeface = 2
                shakemouth = 3
                facemouthsurface_changed = facemouthopenedsurface_scales_prerender[int((facezoom-1)*10)]
            
            if animtimems in range(2560,3840): # transition
                num = 0
                while num < 30:
                    x = random.randint(0,desktopres[0])
                    y = random.randint(0,desktopres[1])
                    pygame.draw.line(windowmainsurface,(0,0,0),(x-200,y),
                                                       (x+200,y),3)
                    num += 1

            

            windows_list[windowcurrent].flip()

            for event in pygame.event.get():
                pass
            

        except ZeroDivisionError:
            continue

def fadein1600ms(Startingtime):
    global windows_list
    global windowsurfaces_list
    global windowcurrent

    
    windows_list[windowcurrent].borderless = False
    windows_list[windowcurrent].set_icon(icon)

    windowsurfaces_list[windowcurrent].fill((0,0,0))
    windows_list[windowcurrent].flip()

    animtime = 0

    windowmovingmult = [0,0]
    mult_of_a_windowmovingmult = 4

    nuhuhtime = 0

    while animtime <= 1.600:

        animtime = time.perf_counter() - Startingtime

        animtimems = int(animtime*1000)

        
        if animtimems in range(0,640):
            num = 0
            while num < 10:
                x = random.randint(0,desktopres[0])
                y = random.randint(0,desktopres[1])
                pygame.draw.line(windowsurfaces_list[windowcurrent],(0,255,0),(x,y-100),
                                                                              (x,y+100),1)
                num += 1

                
        if animtimems in range(640,1600):

            windowscale = abs((animtimems-1600)/960)

            #500x250 new window
            x = desktopres[0]-500
            y = desktopres[1]-250

            windowres = [int(500+(x*windowscale)),int(250+(y*windowscale))]

            lastsurface = pygame.transform.scale(windowmainsurface,(windowres[0],windowres[1]))

            windows_list[windowcurrent].size = (windowres[0],windowres[1])
            windowsurfaces_list[windowcurrent].fill((0,255,0))
            windowsurfaces_list[windowcurrent].blit(lastsurface)

            num = 0
            while num < 10:
                x = random.randint(0,windows_list[windowcurrent].size[0])
                y = random.randint(0,windows_list[windowcurrent].size[1])
                pygame.draw.line(windowsurfaces_list[windowcurrent],(0,255,0),(x,y-100),
                                                                              (x,y+100),1)
                num += 1

            pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
        

        animtime = time.perf_counter() - Startingtime

        animtimems = int(animtime*1000)
        

        x = (desktopres[0]//2)-(windows_list[windowcurrent].size[0]//2)-((windowmovingmult[0]*mult_of_a_windowmovingmult)*((desktopres[0]//2)-(windows_list[windowcurrent].size[0]//2)))
        y = (desktopres[1]//2)-(windows_list[windowcurrent].size[1]//2)-((windowmovingmult[1]*mult_of_a_windowmovingmult)*((desktopres[1]//2)-(windows_list[windowcurrent].size[1]//2)))
        windows_list[windowcurrent].position = (x,y)
        
        #infinity pattern
        #right side
        if animtimems in range(640,960):
            windowmovingmult[0] = -0.2*((animtimems-640) / 320)
            windowmovingmult[1] =  0.2*((animtimems-640) / 320)
        if animtimems in range(960,1280):
            angle = ((animtimems-960) / 320) * 180
            radian = (angle+90)*(math.pi/180)
            circleradius = 0.2
            xs = -0.2
            ys = 0
            x = xs+circleradius * math.cos(radian)
            y = ys+circleradius * math.sin(radian)
            windowmovingmult[0] = x
            windowmovingmult[1] = y
        if animtimems in range(1280,1600):
            windowmovingmult[0] = -0.2+(0.2*((animtimems-1280) / 320))
            windowmovingmult[1] = -0.2+(0.2*((animtimems-1280) / 320))


        if nuhuhtime+1.6 > time.perf_counter():
            nuhuh = fonts_unifont(100).render('No :3',False,(0,0,0))
            windowsurfaces_list[windowcurrent].blit(nuhuh,((windows_list[windowcurrent].size[0]//2)-(nuhuh.get_width() //2),
                                                           (windows_list[windowcurrent].size[1]//2)-(nuhuh.get_height()//2)))
            
        windows_list[windowcurrent].flip()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                nuhuhtime = time.perf_counter()
            if event.type == pygame.WINDOWMINIMIZED:
                windows_list[event.window.id-1].restore()
                
        


def windowtextanim(Startingtime):
    global windows_list
    global windowsurfaces_list
    global windowcurrent

    animtime = 0


    mult_of_a_windowmovingmult = 1
    windowmovingmult = [0,0]
    windowcycle = True

    windowcycletimemult = 1
    windowcycletime = 0 #0 - 2560

    shakeintensity = 0

    nuhuhtime = 0
    nuhuh_id = 0

    while animtime <= 20.64:

        animtime = time.perf_counter() - Startingtime

        animtimems = int(animtime*1000)

        firstparttime = animtimems-40
        secondparttime = animtimems-5400
        thirdparttime = animtimems-10400

        x = (desktopres[0]//2)-(windows_list[windowcurrent].size[0]//2)-((windowmovingmult[0]*mult_of_a_windowmovingmult)*((desktopres[0]//2)-(windows_list[windowcurrent].size[0]//2)))+(random.randint(-50,50)*shakeintensity)
        y = (desktopres[1]//2)-(windows_list[windowcurrent].size[1]//2)-((windowmovingmult[1]*mult_of_a_windowmovingmult)*((desktopres[1]//2)-(windows_list[windowcurrent].size[1]//2)))+(random.randint(-50,50)*shakeintensity)
        windows_list[windowcurrent].position = (x,y)

        if windowcycle:
            windowcycletime = (animtimems*windowcycletimemult) % 2560

            #infinity pattern

            #left side
            if windowcycletime in range(0,320):
                windowmovingmult[0] = 0.3*(windowcycletime / 320)
                windowmovingmult[1] = 0.3*(windowcycletime / 320)
            if windowcycletime in range(320,960):
                angle = abs((windowcycletime-960) / 640) * 180
                radian = (angle-90)*(math.pi/180)

                circleradius = 0.3
                xs = 0.3
                ys = 0
                x = xs+circleradius * math.cos(radian)
                y = ys+circleradius * math.sin(radian)
                windowmovingmult[0] = x
                windowmovingmult[1] = y
            if windowcycletime in range(960,1280):
                windowmovingmult[0] =  0.3-(0.3*((windowcycletime-960) / 320))
                windowmovingmult[1] = -0.3+(0.3*((windowcycletime-960) / 320))
            

            #right side
            if windowcycletime in range(1280,1600):
                windowmovingmult[0] = -0.3*((windowcycletime-1280) / 320)
                windowmovingmult[1] =  0.3*((windowcycletime-1280) / 320)
            if windowcycletime in range(1600,2240):
                angle = ((windowcycletime-1600) / 640) * 180
                radian = (angle+90)*(math.pi/180)

                circleradius = 0.3
                xs = -0.3
                ys = 0
                x = xs+circleradius * math.cos(radian)
                y = ys+circleradius * math.sin(radian)
                windowmovingmult[0] = x
                windowmovingmult[1] = y
            if windowcycletime in range(2240,2560):
                windowmovingmult[0] = -0.3+(0.3*((windowcycletime-2240) / 320))
                windowmovingmult[1] = -0.3+(0.3*((windowcycletime-2240) / 320))
        

        #этот код просто пизда
        #я сын яндередева блять
        if firstparttime in range(160,480): #THINK
            shakeintensity = abs((firstparttime-480)/320)

            if (firstparttime-160) in range(0,10):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,0,0))
                windowtextanim_windowsetmode(text,'THINK',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-160) in range(80,90):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if firstparttime in range(480,800): #TWICE
            shakeintensity = abs((firstparttime-800)/320)

            if (firstparttime-480) in range(0,10):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-480) in range(80,90):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
          

        if firstparttime in range(800,1120): #THINK x2
            shakeintensity = abs((firstparttime-1120)/320)

            if (firstparttime-800) in range(0,10):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,0,0))
                windowtextanim_windowsetmode(text,'THINK',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-800) in range(80,90):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(1120,1440): #TWICE x2
            shakeintensity = abs((firstparttime-1440)/320)

            if (firstparttime-1120) in range(0,10):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-1120) in range(80,90):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()


        if firstparttime in range(1460,1780): #THINK x3
            shakeintensity = abs((firstparttime-1780)/320)

            if (firstparttime-1460) in range(0,10):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,0,0))
                windowtextanim_windowsetmode(text,'THINK',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-1460) in range(80,90):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(1780,2100): #TWICE x3
            shakeintensity = abs((firstparttime-2100)/320)

            if (firstparttime-1780) in range(0,10):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-1780) in range(80,90):
                text = fonts_faith_collapsing(200).render('TWICE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
            

        if firstparttime in range(2100,2420): #THINK TW- x4
            shakeintensity = abs((firstparttime-2420)/320)
            if (firstparttime-2100) in range(0,10):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,0,0))
                windowtextanim_windowsetmode(text,'THINK',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-2100) in range(80,90):
                text = fonts_faith_collapsing(200).render('THINK',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
            
    

        if firstparttime in range(2440,2600): #ice x1
            windowcurrent = 8
            shakeintensity = 2
            if (firstparttime-2440) < 10:
                windows_list[0].hide()
                windowcycle = True
                windowcycletimemult = 2
                mult_of_a_windowmovingmult = 1.5
            else:
                windowcycle = False

            if (firstparttime-2440) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-2440) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(2600,2760): #ice x2
            windowcurrent = 7
            if (firstparttime-2600) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-2600) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-2600) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(2760,2920): #ice x3
            windowcurrent = 6
            if (firstparttime-2760) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-2760) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-2760) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(2940,3100): #ice x4
            windowcurrent = 5
            if (firstparttime-2940) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-2940) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-2940) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(3100,3260): #ice x5
            windowcurrent = 4
            if (firstparttime-3100) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-3100) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-3100) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(3260,3420): #ice x6
            windowcurrent = 3
            if (firstparttime-3260) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-3260) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-3260) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(3420,3580): #ice x7
            windowcurrent = 2
            if (firstparttime-3420) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-3420) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-3420) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if firstparttime in range(3580,3740): #ice x8
            windowcurrent = 1
            if (firstparttime-3580) < 10:
                windowcycle = True
            else:
                windowcycle = False

            if (firstparttime-3580) in range(0,10):
                windows_list[windowcurrent].show()
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (firstparttime-3580) in range(80,90):
                text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        
        #23 beat 
        if firstparttime in range(3740,3750):
            windows_list[8].size = (1,1)
            windows_list[8].position = (-100,-100)
            windows_list[8].hide()

            shakeintensity = 0 
            windowcycle = True
            windowcycletimemult = 1
            mult_of_a_windowmovingmult = 1

            windowcurrent = 0
            windows_list[0].show()
            text = fonts_faith_collapsing(150).render('TWICE',False,(255,255,255))
            text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
            windowtextanim_windowsetmode(text,'TWICE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])

        if firstparttime in range(3900,3910):
            windows_list[7].size = (1,1)
            windows_list[7].position = (-100,-100)
            windows_list[7].hide()
        if firstparttime in range(4060,4070):
            windows_list[6].size = (1,1)
            windows_list[6].position = (-100,-100)
            windows_list[6].hide()
        if firstparttime in range(4220,4230):
            windows_list[5].size = (1,1)
            windows_list[5].position = (-100,-100)
            windows_list[5].hide()
        if firstparttime in range(4380,4390):
            windows_list[4].size = (1,1)
            windows_list[4].position = (-100,-100)
            windows_list[4].hide()
        if firstparttime in range(4540,4550):
            windows_list[3].size = (1,1)
            windows_list[3].position = (-100,-100)
            windows_list[3].hide()
        if firstparttime in range(4700,4710):
            windows_list[2].size = (1,1)
            windows_list[2].position = (-100,-100)
            windows_list[2].hide()
        if firstparttime in range(4860,4870):
            windows_list[1].size = (1,1)
            windows_list[1].position = (-100,-100)
            windows_list[1].hide()


        if secondparttime in range(0,160): #I-
            shakeintensity = abs((secondparttime-160)/160) / 4
            if (secondparttime) in range(0,10):
                text = fonts_ithorn(200).render('I-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'I-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime) in range(80,90):
                text = fonts_ithorn(200).render('I-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
                
        if secondparttime in range(160,320): #I
            shakeintensity = abs((secondparttime-320)/160) / 4
            if (secondparttime-160) in range(0,10):
                text = fonts_ithorn(200).render('I',False,(255,0,0))
                windowtextanim_windowsetmode(text,'I',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-160) in range(80,90):
                text = fonts_ithorn(200).render('I',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(320,480): #WILL
            shakeintensity = abs((secondparttime-480)/160) / 4
            if (secondparttime-320) in range(0,10):
                text = fonts_ithorn(200).render('WILL',False,(255,0,0))
                windowtextanim_windowsetmode(text,'WILL',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-320) in range(80,90):
                text = fonts_ithorn(200).render('WILL',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(480,640): #BE
            shakeintensity = abs((secondparttime-640)/160) / 4
            if (secondparttime-480) in range(0,10):
                text = fonts_ithorn(200).render('BE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'BE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-480) in range(80,90):
                text = fonts_ithorn(200).render('BE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(640,800): #IN
            shakeintensity = abs((secondparttime-800)/160) / 4
            if (secondparttime-640) in range(0,10):
                text = fonts_ithorn(200).render('IN',False,(255,0,0))
                windowtextanim_windowsetmode(text,'IN',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-640) in range(80,90):
                text = fonts_ithorn(200).render('IN',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(800,960): #LOVE
            shakeintensity = abs((secondparttime-960)/160) / 4
            if (secondparttime-800) in range(0,10):
                text = fonts_ithorn(200).render('LOVE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'LOVE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-800) in range(80,90):
                text = fonts_ithorn(200).render('LOVE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(960,1120): #FOR-
            shakeintensity = abs((secondparttime-1120)/160) / 4
            if (secondparttime-960) in range(0,10):
                text = fonts_ithorn(200).render('FOR-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FOR-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-960) in range(80,90):
                text = fonts_ithorn(200).render('FOR-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(1120,1280): #FORE-
            shakeintensity = abs((secondparttime-1280)/160) / 4
            if (secondparttime-1120) in range(0,10):
                text = fonts_ithorn(200).render('FORE-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FORE-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1120) in range(80,90):
                text = fonts_ithorn(200).render('FORE-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(1280,1440): #FOREVER
            shakeintensity = abs((secondparttime-1440)/160) / 4
            if (secondparttime-1280) in range(0,10):
                text = fonts_ithorn(200).render('FOREVER',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FOREVER',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1280) in range(80,90):
                text = fonts_ithorn(200).render('FOREVER',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        
        if secondparttime in range(1440,1600): #CUZ
            shakeintensity = abs((secondparttime-1600)/160) / 4
            if (secondparttime-1440) in range(0,10):
                text = fonts_ithorn(200).render('CUZ',False,(255,0,0))
                windowtextanim_windowsetmode(text,'CUZ',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1440) in range(80,90):
                text = fonts_ithorn(200).render('CUZ',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(1600,1760): #I'M
            shakeintensity = abs((secondparttime-1760)/160) / 4
            if (secondparttime-1600) in range(0,10):
                text = fonts_ithorn(200).render("I'M",False,(255,0,0))
                windowtextanim_windowsetmode(text,"I'M",windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1600) in range(80,90):
                text = fonts_ithorn(200).render("I'M",False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(1760,1920): #GON-
            shakeintensity = abs((secondparttime-1920)/160) / 4
            if (secondparttime-1760) in range(0,10):
                text = fonts_ithorn(200).render('GON-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'GON-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1760) in range(80,90):
                text = fonts_ithorn(200).render('GON-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(1920,2080): #GONNA
            shakeintensity = abs((secondparttime-2080)/160) / 4
            if (secondparttime-1920) in range(0,10):
                text = fonts_ithorn(200).render('GONNA',False,(255,0,0))
                windowtextanim_windowsetmode(text,'GONNA',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-1920) in range(80,90):
                text = fonts_ithorn(200).render('GONNA',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(2080,2240): #DIE
            shakeintensity = abs((secondparttime-2240)/160) / 4
            if (secondparttime-2080) in range(0,10):
                text = fonts_ithorn(200).render('DIE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'DIE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-2080) in range(80,90):
                text = fonts_ithorn(200).render('DIE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(2240,2400): #TO-
            shakeintensity = abs((secondparttime-2400)/160) / 4
            if (secondparttime-2240) in range(0,10):
                text = fonts_faith_collapsing(150).render('TO-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'TO-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (secondparttime-2240) in range(80,90):
                text = fonts_faith_collapsing(150).render('TO-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()



        if secondparttime in range(2400,2560): #TONIGHT

            
            windowcycle = False
            if windowmovingmult[0] > 0:
                windowmovingmult[0] -= 0.005
            if windowmovingmult[1] > 0:
                windowmovingmult[1] -= 0.005
            shakeintensity = abs((secondparttime-2560)/160) * 2
            if (secondparttime-2400) in range(0,10):
                text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,0,0))
                windowtextanim_windowsetmode(text,'TONIGHT',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
                windows_list[1].hide()
                windows_list[2].hide()
                windows_list[3].hide()
                windows_list[4].hide()
                windowtextanim_windowsetmode(text,'TONIGHT',windows_list[1],windowsurfaces_list[1])
                windowtextanim_windowsetmode(text,'TONIGHT',windows_list[2],windowsurfaces_list[2])
                windowtextanim_windowsetmode(text,'TONIGHT',windows_list[3],windowsurfaces_list[3])
                windowtextanim_windowsetmode(text,'TONIGHT',windows_list[4],windowsurfaces_list[4])
                windows_list[1].position = (random.randint(0,desktopres[0]-windows_list[1].size[0]),
                                            random.randint(0,desktopres[1]-windows_list[1].size[1]))
                windows_list[2].position = (random.randint(0,desktopres[0]-windows_list[2].size[0]),
                                            random.randint(0,desktopres[1]-windows_list[2].size[1]))
                windows_list[3].position = (random.randint(0,desktopres[0]-windows_list[3].size[0]),
                                            random.randint(0,desktopres[1]-windows_list[3].size[1]))
                windows_list[4].position = (random.randint(0,desktopres[0]-windows_list[4].size[0]),
                                            random.randint(0,desktopres[1]-windows_list[4].size[1]))
                windows_startingpos = [windows_list[1].position,
                                       windows_list[2].position,
                                       windows_list[3].position,
                                       windows_list[4].position]
            if (secondparttime-2400) in range(80,90):
                text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()

        if secondparttime in range(4480,5120): #tonights' shake
            windows_list[1].position = (windows_startingpos[0][0]+random.randint(-10,10),
                                        windows_startingpos[0][1]+random.randint(-10,10))
            windows_list[2].position = (windows_startingpos[1][0]+random.randint(-10,10),
                                        windows_startingpos[1][1]+random.randint(-10,10))
            windows_list[3].position = (windows_startingpos[2][0]+random.randint(-10,10),
                                        windows_startingpos[2][1]+random.randint(-10,10))
            windows_list[4].position = (windows_startingpos[3][0]+random.randint(-10,10),
                                        windows_startingpos[3][1]+random.randint(-10,10))
            
        if secondparttime in range(4480,4490): #TONIGHT x2
            windows_list[1].show()
            text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,255,255))
            windowsurfaces_list[1].fill((0,255,0))
            windowsurfaces_list[1].blit(text)
            pygame.draw.lines(windowsurfaces_list[1],(128,128,128),False,[(0,0),(windows_list[1].size[0]-1,0),(windows_list[1].size[0]-1,windows_list[1].size[1]-1),(0,windows_list[1].size[1]-1),(0,0)])
            windows_list[1].flip()
        if secondparttime in range(4640,4650): #TONIGHT x3
            windows_list[2].show()
            text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,255,255))
            windowsurfaces_list[2].fill((0,255,0))
            windowsurfaces_list[2].blit(text)
            pygame.draw.lines(windowsurfaces_list[2],(128,128,128),False,[(0,0),(windows_list[2].size[0]-1,0),(windows_list[2].size[0]-1,windows_list[2].size[1]-1),(0,windows_list[2].size[1]-1),(0,0)])
            windows_list[2].flip()
        if secondparttime in range(4800,4810): #TONIGHT x4
            windows_list[3].show()
            text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,255,255))
            windowsurfaces_list[3].fill((0,255,0))
            windowsurfaces_list[3].blit(text)
            pygame.draw.lines(windowsurfaces_list[3],(128,128,128),False,[(0,0),(windows_list[3].size[0]-1,0),(windows_list[3].size[0]-1,windows_list[3].size[1]-1),(0,windows_list[3].size[1]-1),(0,0)])
            windows_list[3].flip()
        if secondparttime in range(4960,4970): #TONIGHT x5
            windows_list[4].show()
            text = fonts_faith_collapsing(200).render('TONIGHT',False,(255,255,255))
            windowsurfaces_list[4].fill((0,255,0))
            windowsurfaces_list[4].blit(text)
            pygame.draw.lines(windowsurfaces_list[4],(128,128,128),False,[(0,0),(windows_list[4].size[0]-1,0),(windows_list[4].size[0]-1,windows_list[4].size[1]-1),(0,windows_list[4].size[1]-1),(0,0)])
            windows_list[4].flip()



        if thirdparttime in range(0,480):
            if thirdparttime in range(0,10):
                shakeintensity = 0
                windows_list[1].hide()
                windows_list[2].hide()
                windows_list[3].hide()
                windows_list[4].hide()
                for i in windows_list:
                    i.borderless = False
                windows_list[windowcurrent].borderless = True
                    
            sizemult = 1+((thirdparttime-480)/320)
            sizemult = 1-(sizemult-1)**2                                  #fucking around in desmos helped #sizemult is x in this equasion

            if thirdparttime in range(0,160):
                windows_list[windowcurrent].position = (0,0)
                windows_list[windowcurrent].size = desktopres
                windowsurfaces_list[windowcurrent].fill((255,0,0))
                windows_list[windowcurrent].flip()
            if thirdparttime in range(160,480):
                windows_list[windowcurrent].position = (((desktopres[0]-500)//2)*sizemult,
                                                        ((desktopres[1]-250)//2)*sizemult)
                windows_list[windowcurrent].size = (desktopres[0]-((desktopres[0]-500)*sizemult),
                                                    desktopres[1]-((desktopres[1]-250)*sizemult))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()


        if thirdparttime in range(480,2720):
            if thirdparttime % 16 == 0:
                randomx = random.randint(-10,10)
                randomy = random.randint(-10,10)
                windows_list[7].position = (50+randomx, 
                                            50+randomy) #so
                
                windows_list[6].position = (50+randomx,
                                            (desktopres[1]//2)-(windows_list[6].size[1]//2)+randomy) #please
                windows_list[5].position = (50+randomx,
                                            desktopres[1]-windows_list[5].size[1]-50+randomy) #just
                
                windows_list[4].position = ((desktopres[0]-50-windows_list[4].size[0])+randomx,
                                            50+randomy) #hold
                windows_list[3].position = ((desktopres[0]-50-windows_list[3].size[0])+randomx,
                                            desktopres[1]-windows_list[3].size[1]-50+randomy) #me
                
                windows_list[2].position = ((desktopres[0]//2)-(windows_list[2].size[0]//2)+randomx,
                                            50+randomy) #one
                windows_list[1].position = ((desktopres[0]//2)-(windows_list[1].size[0]//2)+randomx,
                                            (desktopres[1]-50-windows_list[1].size[1])+randomy) #last




        if thirdparttime in range(480,800): #SO
            if (thirdparttime-480) in range(0,10):
                windows_list[7].show()
                text = fonts_faith_collapsing(150).render('SO',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*2,text.get_height()))
                windowtextanim_windowsetmode(text,'SO',windows_list[7],windowsurfaces_list[7])
            if (thirdparttime-480) in range(40,50):
                text = fonts_faith_collapsing(150).render('SO',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'SO',windows_list[7],windowsurfaces_list[7])
            if (thirdparttime-480) in range(80,90):
                text = fonts_faith_collapsing(150).render('SO',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*2))
                windowtextanim_windowsetmode(text,'SO',windows_list[7],windowsurfaces_list[7])

        if thirdparttime in range(800,1120): #PLEASE
            if (thirdparttime-800) in range(0,10):
                windows_list[6].show()
                text = fonts_faith_collapsing(150).render('PLEASE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()//2,text.get_height()))
                windowtextanim_windowsetmode(text,'PLEASE',windows_list[6],windowsurfaces_list[6])
            if (thirdparttime-800) in range(40,50):
                text = fonts_faith_collapsing(150).render('PLEASE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'PLEASE',windows_list[6],windowsurfaces_list[6])
            if (thirdparttime-800) in range(80,90):
                text = fonts_faith_collapsing(150).render('PLEASE',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()//2))
                windowtextanim_windowsetmode(text,'PLEASE',windows_list[6],windowsurfaces_list[6])

        if thirdparttime in range(1120,1440): #JUST
            if (thirdparttime-1120) in range(0,10):
                windows_list[5].show()
                text = fonts_faith_collapsing(150).render('JUST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*2,text.get_height()))
                windowtextanim_windowsetmode(text,'JUST',windows_list[5],windowsurfaces_list[5])
            if (thirdparttime-1120) in range(40,50):
                text = fonts_faith_collapsing(150).render('JUST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'JUST',windows_list[5],windowsurfaces_list[5])
            if (thirdparttime-1120) in range(80,90):
                text = fonts_faith_collapsing(150).render('JUST',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'JUST',windows_list[5],windowsurfaces_list[5])
        
        if thirdparttime in range(1440,1760): #HOLD
            if (thirdparttime-1440) in range(0,10):
                windows_list[4].show()
                text = fonts_faith_collapsing(150).render('HOLD',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()//2,text.get_height()))
                windowtextanim_windowsetmode(text,'HOLD',windows_list[4],windowsurfaces_list[4])
            if (thirdparttime-1440) in range(40,50):
                text = fonts_faith_collapsing(150).render('HOLD',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'HOLD',windows_list[4],windowsurfaces_list[4])
            if (thirdparttime-1440) in range(80,90):
                text = fonts_faith_collapsing(150).render('HOLD',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'HOLD',windows_list[4],windowsurfaces_list[4])
        
        if thirdparttime in range(1760,2080): #ME
            if (thirdparttime-1760) in range(0,10):
                windows_list[3].show()
                text = fonts_faith_collapsing(150).render('ME',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*2))
                windowtextanim_windowsetmode(text,'ME',windows_list[3],windowsurfaces_list[3])
            if (thirdparttime-1760) in range(40,50):
                text = fonts_faith_collapsing(150).render('ME',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'ME',windows_list[3],windowsurfaces_list[3])
            if (thirdparttime-1760) in range(80,90):
                text = fonts_faith_collapsing(150).render('ME',False,(255,255,255))
                text = pygame.transform.scale(text,(text.get_width()*2,text.get_height()))
                windowtextanim_windowsetmode(text,'ME',windows_list[3],windowsurfaces_list[3])
        
        if thirdparttime in range(2080,2400): #ONE
            if (thirdparttime-2080) in range(0,10):
                windows_list[2].show()
                text = fonts_faith_collapsing(150).render('ONE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*3,text.get_height()))
                windowtextanim_windowsetmode(text,'ONE',windows_list[2],windowsurfaces_list[2])
            if (thirdparttime-2080) in range(40,50):
                text = fonts_faith_collapsing(150).render('ONE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'ONE',windows_list[2],windowsurfaces_list[2])
            if (thirdparttime-2080) in range(80,90):
                text = fonts_faith_collapsing(150).render('ONE',False,(255,200,200))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'ONE',windows_list[2],windowsurfaces_list[2])
        
        if thirdparttime in range(2400,2720): #LAST
            if (thirdparttime-2400) in range(0,10):
                windows_list[1].show()
                text = fonts_faith_collapsing(150).render('LAST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*3,text.get_height()))
                windowtextanim_windowsetmode(text,'LAST',windows_list[1],windowsurfaces_list[1])
            if (thirdparttime-2400) in range(40,50):
                text = fonts_faith_collapsing(150).render('LAST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'LAST',windows_list[1],windowsurfaces_list[1])
            if (thirdparttime-2400) in range(80,90):
                text = fonts_faith_collapsing(150).render('LAST',False,(255,200,200))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*3))
                windowtextanim_windowsetmode(text,'LAST',windows_list[1],windowsurfaces_list[1])
        



        if thirdparttime in range(2720,4960):
            if thirdparttime-2720 in range(0,10):
                textbleh = fonts_faith_collapsing(150).render('TIME',False,(255,0,0))
                text1 = fonts_faith_collapsing(150).render('TIME',False,(255,255,255))
                text2 = fonts_faith_collapsing(150).render('TIME',False,(255,0,0))
                text3 = fonts_faith_collapsing(150).render('TIME',False,(255,255,255))
                text4 = fonts_faith_collapsing(150).render('TIME',False,(255,0,0))
                text5 = fonts_faith_collapsing(150).render('TIME',False,(255,255,255))
                text6 = fonts_faith_collapsing(150).render('TIME',False,(255,0,0))
                text7 = fonts_faith_collapsing(150).render('TIME',False,(255,255,255))
                textwidth = textbleh.get_width()
                textheight = textbleh.get_height()
                textoutline = fonts_faith_collapsing(154).render('TIME',False,(0,0,0))
            wholesurface = pygame.Surface((textwidth+200,textheight+200),pygame.SRCALPHA)

        if thirdparttime in range(2720,4000): #TIME X1
            if (thirdparttime-2720) in range(0,10):
                text = fonts_faith_collapsing(150).render('SO',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'SO',windows_list[7],windowsurfaces_list[7])
            if (thirdparttime-2720) in range(40,50):
                text = fonts_faith_collapsing(150).render('SO',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*2,text.get_height()))
                windowtextanim_windowsetmode(text,'SO',windows_list[7],windowsurfaces_list[7])
            if (thirdparttime-2720) in range(80,90):
                windows_list[7].hide()

            windowcycle = True
            timeeffect_scale = 1+(thirdparttime-3360)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text1,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
            
        if thirdparttime in range(2880,4160): #TIME X2

            if (thirdparttime-2880) in range(0,10):
                text = fonts_faith_collapsing(150).render('PLEASE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'PLEASE',windows_list[6],windowsurfaces_list[6])
            if (thirdparttime-2880) in range(40,50):
                text = fonts_faith_collapsing(150).render('PLEASE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()//2,text.get_height()))
                windowtextanim_windowsetmode(text,'PLEASE',windows_list[6],windowsurfaces_list[6])
            if (thirdparttime-2880) in range(80,90):
                windows_list[6].hide()

            timeeffect_scale = 1+(thirdparttime-3520)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            
            texteffect = pygame.transform.scale(text2,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))

        if thirdparttime in range(3040,4320): #TIME X3
            if (thirdparttime-3040) in range(0,10):
                text = fonts_faith_collapsing(150).render('JUST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'JUST',windows_list[5],windowsurfaces_list[5])
            if (thirdparttime-3040) in range(40,50):
                text = fonts_faith_collapsing(150).render('JUST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*2,text.get_height()))
                windowtextanim_windowsetmode(text,'JUST',windows_list[5],windowsurfaces_list[5])
            if (thirdparttime-3040) in range(80,90):
                windows_list[5].hide()

            timeeffect_scale = 1+(thirdparttime-3680)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text3,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
            
        if thirdparttime in range(3200,4480): #TIME X4
            if (thirdparttime-3200) in range(0,10):
                text = fonts_faith_collapsing(150).render('HOLD',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'HOLD',windows_list[4],windowsurfaces_list[4])
            if (thirdparttime-3200) in range(40,50):
                text = fonts_faith_collapsing(150).render('HOLD',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()//2,text.get_height()))
                windowtextanim_windowsetmode(text,'HOLD',windows_list[4],windowsurfaces_list[4])
            if (thirdparttime-3200) in range(80,90):
                windows_list[4].hide()

            timeeffect_scale = 1+(thirdparttime-3840)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text4,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
            
        if thirdparttime in range(3360,4640): #TIME X5
            if (thirdparttime-3360) in range(0,10):
                text = fonts_faith_collapsing(150).render('ME',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'ME',windows_list[3],windowsurfaces_list[3])
            if (thirdparttime-3360) in range(40,50):
                text = fonts_faith_collapsing(150).render('ME',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()*2))
                windowtextanim_windowsetmode(text,'ME',windows_list[3],windowsurfaces_list[3])
            if (thirdparttime-3360) in range(80,90):
                windows_list[3].hide()

            timeeffect_scale = 1+(thirdparttime-4000)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text5,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
            
        if thirdparttime in range(3520,4800): #TIME X6
            if (thirdparttime-3520) in range(0,10):
                text = fonts_faith_collapsing(150).render('ONE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'ONE',windows_list[2],windowsurfaces_list[2])
            if (thirdparttime-3520) in range(40,50):
                text = fonts_faith_collapsing(150).render('ONE',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*3,text.get_height()))
                windowtextanim_windowsetmode(text,'ONE',windows_list[2],windowsurfaces_list[2])
            if (thirdparttime-3520) in range(80,90):
                windows_list[2].hide()

            timeeffect_scale = 1+(thirdparttime-4160)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text6,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
            
        if thirdparttime in range(3680,4960): #TIME X7
            if (thirdparttime-3680) in range(0,10):
                text = fonts_faith_collapsing(150).render('LAST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width(),text.get_height()))
                windowtextanim_windowsetmode(text,'LAST',windows_list[1],windowsurfaces_list[1])
            if (thirdparttime-3680) in range(40,50):
                text = fonts_faith_collapsing(150).render('LAST',False,(255,0,0))
                text = pygame.transform.scale(text,(text.get_width()*3,text.get_height()))
                windowtextanim_windowsetmode(text,'LAST',windows_list[1],windowsurfaces_list[1])
            if (thirdparttime-3680) in range(80,90):
                windows_list[1].hide()

            timeeffect_scale = 1+(thirdparttime-4320)/640
            if timeeffect_scale > 0 and timeeffect_scale <= 1:
                timeeffect_scale = math.sqrt(timeeffect_scale)
            if timeeffect_scale > 1: #text popped out
                timeeffect_scale = 1 + (1-timeeffect_scale)
                timeeffect_scale = math.sqrt(timeeffect_scale)
            texteffect = pygame.transform.scale(text7,(textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)))
            wholesurface.blit(texteffect,(100-(100*timeeffect_scale),100-(100*timeeffect_scale)))
        
        if thirdparttime in range(2720,4960):
            wholesurface.blit(textoutline,(100-4,100-2))
            wholesurface.blit(textbleh,(100,100))
            windowtextanim_windowsetmode(wholesurface,'TIME',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
        
        if thirdparttime in range(4960,5280):
            timeeffect_scale = abs(1-(thirdparttime-4960)/320)
            if timeeffect_scale > 0:
                timeeffect_scale = timeeffect_scale**5

            wholesurface = pygame.Surface((textwidth+(200*timeeffect_scale),textheight+(200*timeeffect_scale)),pygame.SRCALPHA)

            text = fonts_faith_collapsing(150).render('TIME',False,(255,0,0))

            wholesurface.blit(textoutline,((100*timeeffect_scale)-4,(100*timeeffect_scale)-2))
            wholesurface.blit(textbleh,((100*timeeffect_scale),(100*timeeffect_scale)))
            windowtextanim_windowsetmode(wholesurface,'TIME',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])

        

        if thirdparttime in range(5600,5760): #BE-
            shakeintensity = abs((thirdparttime-5760)/160) / 8
            if (thirdparttime   -5600) in range(0,10):
                text = fonts_ithorn(200).render('BE-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'BE-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-5600) in range(80,90):
                text = fonts_ithorn(200).render('BE-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(5760,5920): #BEFORE
            shakeintensity = abs((thirdparttime-5920)/160) / 8
            if (thirdparttime-5760) in range(0,10):
                text = fonts_ithorn(200).render('BEFORE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'BEFORE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-5760) in range(80,90):
                text = fonts_ithorn(200).render('BEFORE',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(5920,6080): #I
            shakeintensity = abs((thirdparttime-6080)/160) / 8
            if (thirdparttime-5920) in range(0,10):
                text = fonts_ithorn(200).render('I',False,(255,0,0))
                windowtextanim_windowsetmode(text,'I',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-5920) in range(80,90):
                text = fonts_ithorn(200).render('I',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6080,6240): #BLOOM
            shakeintensity = abs((thirdparttime-6240)/160) / 8
            if (thirdparttime-6080) in range(0,10):
                text = fonts_ithorn(200).render('BLOOM',False,(255,0,0))
                windowtextanim_windowsetmode(text,'BLOOM',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6080) in range(80,90):
                text = fonts_ithorn(200).render('BLOOM',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6240,6400): #IN-
            shakeintensity = abs((thirdparttime-6400)/160) / 8
            if (thirdparttime-6240) in range(0,10):
                text = fonts_ithorn(200).render('IN-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'IN-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6240) in range(80,90):
                text = fonts_ithorn(200).render('IN-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6400,6560): #INTO
            shakeintensity = abs((thirdparttime-6560)/160) / 8
            if (thirdparttime-6400) in range(0,10):
                text = fonts_ithorn(200).render('INTO',False,(255,0,0))
                windowtextanim_windowsetmode(text,'INTO',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6400) in range(80,90):
                text = fonts_ithorn(200).render('INTO',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6560,6720): #A
            shakeintensity = abs((thirdparttime-6720)/160) / 8
            if (thirdparttime-6560) in range(0,10):
                text = fonts_ithorn(200).render('A',False,(255,0,0))
                windowtextanim_windowsetmode(text,'A',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6560) in range(80,90):
                text = fonts_ithorn(200).render('A',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6720,6880): #FLO-
            shakeintensity = abs((thirdparttime-6880)/160) / 8
            if (thirdparttime-6720) in range(0,10):
                text = fonts_ithorn(200).render('FLO-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FLO-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6720) in range(80,90):
                text = fonts_ithorn(200).render('FLO-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(6880,7040): #FLOWER
            shakeintensity = abs((thirdparttime-7040)/160) / 8
            if (thirdparttime-6880) in range(0,10):
                text = fonts_ithorn(200).render('FLOWER',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FLOWER',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-6880) in range(80,90):
                text = fonts_ithorn(200).render('FLOWER',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7040,7200): #FIRST
            shakeintensity = abs((thirdparttime-7200)/160) / 8
            if (thirdparttime-7040) in range(0,10):
                text = fonts_ithorn(200).render('FIRST',False,(255,0,0))
                windowtextanim_windowsetmode(text,'FIRST',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7040) in range(80,90):
                text = fonts_ithorn(200).render('FIRST',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7200,7360): #I
            shakeintensity = abs((thirdparttime-7360)/160) / 8
            if (thirdparttime-7200) in range(0,10):
                text = fonts_ithorn(200).render('I',False,(255,0,0))
                windowtextanim_windowsetmode(text,'I',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7200) in range(80,90):
                text = fonts_ithorn(200).render('I',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7360,7520): #WAN-
            shakeintensity = abs((thirdparttime-7520)/160) / 8
            if (thirdparttime-7360) in range(0,10):
                text = fonts_ithorn(200).render('WAN-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'WAN-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7360) in range(80,90):
                text = fonts_ithorn(200).render('WAN-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7520,7680): #WANNA
            shakeintensity = abs((thirdparttime-7680)/160) / 8
            if (thirdparttime-7520) in range(0,10):
                text = fonts_ithorn(200).render('WANNA',False,(255,0,0))
                windowtextanim_windowsetmode(text,'WANNA',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7520) in range(80,90):
                text = fonts_ithorn(200).render('WANNA',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7680,7840): #SAY
            shakeintensity = abs((thirdparttime-7840)/160) / 8
            if (thirdparttime-7680) in range(0,10):
                text = fonts_ithorn(200).render('SAY',False,(255,0,0))
                windowtextanim_windowsetmode(text,'SAY',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7680) in range(80,90):
                text = fonts_ithorn(200).render('SAY',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()
        if thirdparttime in range(7840,8000): #GOOD-
            shakeintensity = abs((thirdparttime-8000)/160) / 8
            if (thirdparttime-7840) in range(0,10):
                text = fonts_ithorn(200).render('GOOD-',False,(255,0,0))
                windowtextanim_windowsetmode(text,'GOOD-',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            if (thirdparttime-7840) in range(80,90):
                text = fonts_ithorn(200).render('GOOD-',False,(255,255,255))
                windowsurfaces_list[windowcurrent].fill((0,255,0))
                windowsurfaces_list[windowcurrent].blit(text)
                pygame.draw.lines(windowsurfaces_list[windowcurrent],(128,128,128),False,[(0,0),(windows_list[windowcurrent].size[0]-1,0),(windows_list[windowcurrent].size[0]-1,windows_list[windowcurrent].size[1]-1),(0,windows_list[windowcurrent].size[1]-1),(0,0)])
                windows_list[windowcurrent].flip()


        if thirdparttime in range(8000,9280): #GOODBYE
            windowcycle = False
            if windowmovingmult[0] > 0:
                windowmovingmult[0] -= 0.05
            if windowmovingmult[1] > 0:
                windowmovingmult[1] -= 0.05

            shakeintensity = 0.5
            if thirdparttime > 8640:
                shakeintensity = (thirdparttime-8000)/1280
                shakeintensity = (16*((shakeintensity-1)**4))/2

            textscale = (thirdparttime-8000)/640     #0 --> 2
            textscale = 1-((textscale-1)**2)

            if (thirdparttime-8000) in range(0,10):
                text = fonts_faith_collapsing(100+int(100*textscale)).render('GOODBYE',False,(255,0,0))
                windowtextanim_windowsetmode(text,'GOODBYE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])
            else:
                if (thirdparttime-8000) in range(640,1280):
                    text = fonts_faith_collapsing(int(200*textscale)).render('GOODBYE',False,(255,255,255))
                if (thirdparttime-8000) in range(0,640):
                    text = fonts_faith_collapsing(100+int(100*textscale)).render('GOODBYE',False,(255,255,255))
                windowtextanim_windowsetmode(text,'GOODBYE',windows_list[windowcurrent],windowsurfaces_list[windowcurrent])

        if thirdparttime in range(9280,9290):
            shakeintensity = 0
            windowsurfaces_list[windowcurrent].fill((0,255,0))
            windows_list[windowcurrent].position = (0,0)
            windows_list[windowcurrent].size = desktopres
            windowsurfaces_list[windowcurrent].fill((0,255,0))
            windows_list[windowcurrent].borderless = False
            windows_list[windowcurrent].title = '...'
            windows_list[windowcurrent].flip()
        



        if nuhuhtime+0.32 > time.perf_counter():
            nuhuh = fonts_unifont(100).render('No :3',False,(0,0,0))
            windowsurfaces_list[nuhuh_id-1].blit(nuhuh,((windows_list[nuhuh_id-1].size[0]//2)-(nuhuh.get_width() //2),
                                                        (windows_list[nuhuh_id-1].size[1]//2)-(nuhuh.get_height()//2)))
            windows_list[nuhuh_id-1].flip()

        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                nuhuhtime = time.perf_counter()
                nuhuh_id = event.window.id
            if event.type == pygame.WINDOWMINIMIZED:
                prevsurface = windowsurfaces_list[event.window.id-1].copy()
                windows_list[event.window.id-1].restore()
                windowsurfaces_list[event.window.id-1].blit(prevsurface)
                windows_list[event.window.id-1].flip()



def picturedas__perfect_part(Startingtime):
    global windows_list
    global windowsurfaces_list
    global windowcurrent

    global surfacepas_purple_noize
    global surfacepas_red_noize
    global surface_circle_layer

    animtime = 0

    nuhuhtime = 0
    nuhuh_id = 0

    textahh = fonts_faith_collapsing(200).render('AHH',False,(255,255,255))
    textahhoutline = fonts_faith_collapsing(204).render('AHH',False,(0,0,0))
    randomtextpos = [(random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     (random.randint(0,desktopres[0]-textahh.get_width()),random.randint(0,desktopres[1]-textahh.get_height())),
                     ]

    while animtime < 100:

        animtime = time.perf_counter() - Startingtime
        animtimems = int(animtime*1000)

        firsttimepart = animtimems

        if firsttimepart in range(0,640):
            textscale = firsttimepart/640
            if textscale <= 0.5:
                textscale = (4*((textscale-0.5)**3))+0.5
            if textscale > 0.5:
                textscale = (8*((textscale-0.5)**3))+0.5
            
            
            
            text = fonts_faith_collapsing(int(200*textscale)).render('AAH!',False,(255,255,255))
            textoutline = fonts_faith_collapsing(int(204*textscale)).render('AAH!',False,(0,0,0))
            pygame.draw.circle(surface_circle_layer,(0,0,255),(desktopres[0]//2,desktopres[1]//2),text.get_width()//2,100)

            for i in range(0,100):
                x = random.randint(desktopres[0]//2-text.get_width()//2,desktopres[0]//2+text.get_width()//2)
                y = random.randint(desktopres[1]//2-text.get_width()//2,desktopres[1]//2+text.get_width()//2)
                pygame.draw.line(surfacepas_red_noize,pas_colors[random.randint(0,2)],(x,y),(x,y))

            windowsurfaces_list[windowcurrent].blit(surfacepas_red_noize)
            windowsurfaces_list[windowcurrent].blit(surface_circle_layer)
            windowsurfaces_list[windowcurrent].blit(textoutline,((desktopres[0]//2-text.get_width()//2-4),(desktopres[1]//2-text.get_height()//2)-2))
            windowsurfaces_list[windowcurrent].blit(text,((desktopres[0]//2-text.get_width()//2),(desktopres[1]//2-text.get_height()//2)))
            windows_list[windowcurrent].flip()

        if firsttimepart in range(640,19200): #noize
            
            if firsttimepart-640 in range(0,40):
                windowsurfaces_list[windowcurrent].blit(surfacepas_purple_noize)
            else:
                windowsurfaces_list[windowcurrent].blit(surfacepas_red_noize)
                for i in range(0,1000):
                    x = random.randint(0,desktopres[0])
                    y = random.randint(0,desktopres[1])
                    pygame.draw.line(surfacepas_red_noize,pas_colors[random.randint(0,2)],(x,y),(x,y))

            windows_list[windowcurrent].flip()


        if firsttimepart in range(7360,8640): #ahh1 1-8  
            textposnum = int((firsttimepart-7360)/160)
            x = randomtextpos[textposnum][0]+random.randint(-50,50)
            y = randomtextpos[textposnum][1]+random.randint(-50,50)
            surfacepas_red_noize.blit(textahhoutline,(x-4,y-2))
            surfacepas_red_noize.blit(textahh,(x,y))
            








        if firsttimepart in range(19200,19210):
            windowsurfaces_list[windowcurrent].fill((0,255,0))
            windows_list[windowcurrent].flip()

            





        if nuhuhtime+0.32 > time.perf_counter():
            nuhuh = fonts_unifont(100).render('No :3',False,(0,0,0))
            windowsurfaces_list[nuhuh_id-1].blit(nuhuh,((windows_list[nuhuh_id-1].size[0]//2)-(nuhuh.get_width() //2),
                                                        (windows_list[nuhuh_id-1].size[1]//2)-(nuhuh.get_height()//2)))
            windows_list[nuhuh_id-1].flip()

        CLOCK.tick()
        for event in pygame.event.get():
            print(CLOCK.get_fps())
            if event.type == pygame.WINDOWCLOSE:
                nuhuhtime = time.perf_counter()
                nuhuh_id = event.window.id
            if event.type == pygame.WINDOWMINIMIZED:
                prevsurface = windowsurfaces_list[event.window.id-1].copy()
                windows_list[event.window.id-1].restore()
                windowsurfaces_list[event.window.id-1].blit(prevsurface)
                windows_list[event.window.id-1].flip()




def windowtextanim_windowsetmode(text_surface,text,
                                 window,windowsurface):

    window.size = (text_surface.get_width(),text_surface.get_height())

    window.title = text

    windowsurface.fill((0,255,0))

    windowsurface.blit(text_surface)
    pygame.draw.lines(windowsurface,(128,128,128),False,[(0,0),(window.size[0]-1,0),(window.size[0]-1,window.size[1]-1),(0,window.size[1]-1),(0,0)])
    
    window.flip()




pas_colors = [(255,0,0),(0,0,0),(255,255,255),(255,0,255)]
surfacepas_purple_noize = pygame.Surface(desktopres)
surfacepas_red_noize = pygame.Surface(desktopres)

surface_circle_layer = pygame.Surface(desktopres,pygame.SRCCOLORKEY)
surface_circle_layer.set_colorkey((0,0,255))
surface_circle_layer.fill((0,255,0))


def START(date_leftto_date1_print,time_leftto_date1_print,startoffsetsec):
    
    global pas_colors
    global surfacepas_purple_noize
    global surfacepas_red_noize
    xforsurfaces = 0
    yforsurfaces = 0
    surface_purple_done = False
    surface_red_done = False

    if __name__ == '__main__':
        for y in range(0,desktopres[1]):
            for x in range(0,desktopres[0]):
                pygame.draw.line(surfacepas_purple_noize,pas_colors[random.randint(1,3)],(x,y),(x,y))

        for y in range(0,desktopres[1]):
            for x in range(0,desktopres[0]):
                pygame.draw.line(surfacepas_red_noize,pas_colors[random.randint(0,2)],(x,y),(x,y))
        
        surfacepas_purple_done = True
        surface_red_done = True



    global DOGMATICArenderednum

    global windowmain
    global windowmainsurface

    global cinemapart

    pygame.mixer_music.load(files['song'])
    pygame.mixer_music.play()
    pygame.mixer_music.set_volume(0.5)
    pygame.mixer_music.set_pos(startoffsetsec)

    songSTARTtime = time.perf_counter() - startoffsetsec
            
    while True:
        #time.sleep(0.01)

        songpos = time.perf_counter() - songSTARTtime
        DOGMATICAlyricnum = int(songpos // 0.16)
        
        match cinemapart:
            case False:
                if DOGMATICAlyricnum >= 400:
                    cinemapart = True
                if DOGMATICAlyricnum != DOGMATICArenderednum:
                    try:
                        dogmaticalyric_nums[DOGMATICAlyricnum]
                        os.system('cls||clear')
                        print('Time left:\n'+date_leftto_date1_print+' '+time_leftto_date1_print)
                        print('\n')
                        print(dogmaticalyric_nums[DOGMATICAlyricnum])
                    except KeyError:
                        pass
                    DOGMATICArenderednum = DOGMATICAlyricnum
            case True:
                fourthwallbreak((DOGMATICAlyricnum*0.16)+songSTARTtime)
                fadein1600ms(((DOGMATICAlyricnum+24)*0.16)+songSTARTtime)
                windowtextanim(((DOGMATICAlyricnum+34)*0.16)+songSTARTtime)
                picturedas__perfect_part(((DOGMATICAlyricnum+163)*0.16)+songSTARTtime)
                pygame.quit()
                break

        #getting surfaces for picturedas__perfect_part ready cuz its lagging really bad when we do that on start
        
        if __name__ != '__main__':
            if (surface_red_done and surface_purple_done) != True:
                for i in range(0,desktopres[1]*2):
                    if not surface_purple_done:
                        if yforsurfaces >= desktopres[1]:
                            surface_purple_done = True
                            yforsurfaces = 0
                            xforsurfaces = 0
                        if xforsurfaces >= desktopres[0]:
                            yforsurfaces += 1
                            xforsurfaces = 0
                        pygame.draw.line(surfacepas_purple_noize,pas_colors[random.randint(1,3)],(xforsurfaces,yforsurfaces),(xforsurfaces,yforsurfaces))
                    else:
                        if yforsurfaces >= desktopres[1]:
                            surface_red_done = True
                            yforsurfaces = 0
                            xforsurfaces = 0
                        if xforsurfaces >= desktopres[0]:
                            yforsurfaces += 1
                            xforsurfaces = 0
                        pygame.draw.line(surfacepas_red_noize,pas_colors[random.randint(0,2)],(xforsurfaces,yforsurfaces),(xforsurfaces,yforsurfaces))
                    xforsurfaces += 1

        for event in pygame.event.get():
            pass

def error_funnies():
    global windows_list
    pygame.mixer.init()

    deltaruneboom = pygame.image.load_animation(dir_to_file_FOLDER+"\\Data\\funnies\\explosion_deltarune.gif")
    deltaruneboomscaled = []
    for i in deltaruneboom:
        deltaruneboomscaled.append(pygame.transform.scale(i[0],(desktopres[1]+(desktopres[1]//2),desktopres[1]+(desktopres[1]//2))))
    del deltaruneboom
    deltaruneboomsound = pygame.Sound(dir_to_file_FOLDER+"\\Data\\funnies\\deltarune-explosion.mp3")

    for i in windows_list:
        i.destroy()
    pygame.display.message_box('An error occured',"Oopsies, something went wrong :pp\nWe're blowing uuuuup :3\nblehhh :ppp",'error',
                               buttons=('boom','boom'))
    funnies = pygame.Window('boom',
                            (desktopres),(0,0),
                            borderless=True,
                            always_on_top=True,
                            utility=True)
    funniessurface = funnies.get_surface()
    funniesinfo = win32gui.FindWindowEx(None, None, None, 'boom')
    win32gui.SetWindowLong(funniesinfo, 
                           win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(funniesinfo, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(funniesinfo, win32api.RGB(*(0,0,0)), 0, win32con.LWA_COLORKEY)

    starttime = time.perf_counter()
    deltaruneboomsound.play()
    while time.perf_counter()-starttime <= 0.3:
        funniessurface.fill((0,0,0))

        currentframe = deltaruneboomscaled[int((time.perf_counter()-starttime)*20)]
        funniessurface.blit(currentframe,
                            ((desktopres[0]//2)-(currentframe.get_width() //2),
                             (desktopres[1]//2)-(currentframe.get_height()//2),))

        funnies.flip()

        for event in pygame.event.get():
            pass

    funnies.destroy()
    pygame.quit()
    quit()

if __name__ == '__main__':
    START('','',60)

