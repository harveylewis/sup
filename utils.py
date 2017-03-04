import os
import random
import sys
import time

class Color:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    white = '\033[1m\033[37m'



def p_(*args):
    """
    Color for general values
    """
    input_string = ' '.join(map(str, args))
    return Color.purple+ str(input_string) + Color.reset

def x_(*args):
    """
    Color for exceptions
    """
    input_string = ' '.join(map(str, args))
    return '{0}[{1:^21}]{2}'.format(
        Color.lightcyan,
        input_string,
        Color.reset,
    )


def z_(*args):
    """
    Color for debugging
    """
    input_string = ' '.join(map(str, args))
    return '{0}[{1:^21}]{2}'.format(
        Color.orange,
        input_string,
        Color.reset,
    )


def grey_(*args):
    """
    Colorize text with lightcyan
    """
    input_string = ' '.join(map(str, args))
    return Color.lightgrey + str(input_string) + Color.reset

def lb_(*args):
    """
    Colorize text with lightcyan
    """
    input_string = ' '.join(map(str, args))
    return Color.lightcyan + str(input_string) + Color.reset


def r_(*args):
    """
    Colorize text with red
    """
    input_string = ' '.join(map(str, args))
    return Color.red + str(input_string) + Color.reset


def y_(*args):
    """
    Colorize text with yellow
    """
    input_string = ' '.join(map(str, args))
    return Color.yellow + str(input_string) + Color.reset


def Y_(*args):
    """
    Color for yellow title
    """
    input_string = ' '.join(map(str, args))
    return '{0}[{1:^21}]{2}'.format(
        Color.yellow,
        input_string,
        Color.reset,
    )



def o_(*args):
    """
    Colorize text with orange
    """
    input_string = ' '.join(map(str, args))
    return Color.orange + str(input_string) + Color.reset


def g_(*args):
    """
    Colorize text with green
    """
    input_string = ' '.join(map(str, args))
    return Color.green + str(input_string) + Color.reset

def b_(*args):
    """
    Colorize text with yellow
    """
    input_string = ' '.join(map(str, args))
    return Color.blue + str(input_string) + Color.reset

def w_(*args):
    """
    Colorize text with yellow
    """
    input_string = ' '.join(map(str, args))
    return Color.white + str(input_string) + Color.reset




def GMT():
    return (time.strftime("%H:%M:%S") + ' :: ')


def new_line():
    return w_(("---------------------------------------------------------------------------------"))
    