""" PyProgress - Written By Benjamin Jack Cullen """

import colorama

colorama.init()

color_ = {'BLACK': colorama.Fore.BLACK,
          'RED': colorama.Fore.RED,
          'GREEN': colorama.Fore.GREEN,
          'YELLOW': colorama.Fore.YELLOW,
          'BLUE': colorama.Fore.BLUE,
          'MAGENTA': colorama.Fore.MAGENTA,
          'CYAN': colorama.Fore.CYAN,
          'WHITE': colorama.Fore.WHITE,
          'LIGHTBLACK_EX': colorama.Fore.LIGHTBLACK_EX,
          'LIGHTRED_EX': colorama.Fore.LIGHTRED_EX,
          'LIGHTGREEN_EX': colorama.Fore.LIGHTGREEN_EX,
          'LIGHTYELLOW_EX': colorama.Fore.LIGHTYELLOW_EX,
          'LIGHTBLUE_EX': colorama.Fore.LIGHTBLUE_EX,
          'LIGHTMAGENTA_EX': colorama.Fore.LIGHTMAGENTA_EX,
          'LIGHTCYAN_EX': colorama.Fore.LIGHTCYAN_EX,
          'LIGHTWHITE_EX': colorama.Fore.LIGHTWHITE_EX
          }

bg_color_ = {'BLACK': colorama.Back.BLACK,
          'RED': colorama.Back.RED,
          'GREEN': colorama.Back.GREEN,
          'YELLOW': colorama.Back.YELLOW,
          'BLUE': colorama.Back.BLUE,
          'MAGENTA': colorama.Back.MAGENTA,
          'CYAN': colorama.Back.CYAN,
          'WHITE': colorama.Back.WHITE,
          'LIGHTBLACK_EX': colorama.Back.LIGHTBLACK_EX,
          'LIGHTRED_EX': colorama.Back.LIGHTRED_EX,
          'LIGHTGREEN_EX': colorama.Back.LIGHTGREEN_EX,
          'LIGHTYELLOW_EX': colorama.Back.LIGHTYELLOW_EX,
          'LIGHTBLUE_EX': colorama.Back.LIGHTBLUE_EX,
          'LIGHTMAGENTA_EX': colorama.Back.LIGHTMAGENTA_EX,
          'LIGHTCYAN_EX': colorama.Back.LIGHTCYAN_EX,
          'LIGHTWHITE_EX': colorama.Back.LIGHTWHITE_EX
          }


def pr_technical_data(technical_data):
    """ clears console line and then prints """

    print(technical_data, end='\r', flush=True)


def progress_bar(part, whole, percent=True, color='', bg_color='', pre_append='', encapsule_l='', encapsule_r='', progress_char=''):
    """ part=int, whole=int, color=str, pre_append=str, percent=bool, encapsule_l=str, encapsule_r=str, progress_char=str"""

    prc = int(100 * float((float(part) / whole)))

    if color and bg_color == '':
        if percent is True:
            pr_data = colorama.Style.BRIGHT + color_[color] + str(prc * progress_char) + colorama.Style.RESET_ALL
        else:
            pr_data = colorama.Style.BRIGHT + color_[color] + str(prc * progress_char) + colorama.Style.RESET_ALL

    elif color and bg_color:
        if percent is True:
            pr_data = bg_color_[bg_color] + colorama.Style.BRIGHT + color_[color] + str(prc * progress_char) + colorama.Style.RESET_ALL
        else:
            pr_data = bg_color_[bg_color] + colorama.Style.BRIGHT + color_[color] + str(prc * progress_char) + colorama.Style.RESET_ALL

    elif bg_color and color == '':
        if percent is True:
            pr_data = bg_color_[bg_color] + str(prc * progress_char) + colorama.Style.RESET_ALL
        else:
            pr_data = bg_color_[bg_color] + str(prc * progress_char) + colorama.Style.RESET_ALL

    else:
        if percent is True:
            pr_data = str(prc * progress_char)
        else:
            pr_data = str(prc * progress_char)

    if encapsule_l and encapsule_r:
        pr_data = encapsule_l + pr_data + encapsule_r
    if percent is True:
        pr_data = str(prc) + '% ' + pr_data

    if pre_append:
        pr_data = pre_append + pr_data

    pr_technical_data(technical_data=pr_data)


def display_color_options():
    return color_.keys()
