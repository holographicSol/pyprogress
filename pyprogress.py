""" PyProgress - Written By Benjamin Jack Cullen """

import colorama

colorama.init()

factor_100 = [1, 2, 4, 5, 10, 20, 25, 50, 100]

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


def check_factor(factor):
    allow_bool = False
    if factor in factor_100:
        allow_bool = True
    return allow_bool


def clear_console_line(char_limit):
    """ clear n chars from console """

    print(' '*char_limit, end='\r', flush=True)


def pr_technical_data(technical_data):
    """ clears console line and then prints """

    print(technical_data, end='\r', flush=True)


def progress_bar(part, whole, percent=True, color='', bg_color='', encapsulate_l_color='', encapsulate_r_color='', pre_append='', append='', encapsulate_l='', encapsulate_r='', progress_char='', factor=100):
    """
    part=int, whole=int, percent=bool,
    color=str, bg_color=str
    encapsulate_l_color=str
    encapsulate_r_color=str
    pre_append=str, append=str,
    encapsulate_l=str, encapsulate_r=str,
    progress_char=str,
    factor=int (factor of 100:  1, 2, 4, 5, 10, 20, 25, 50, and 100)

    Note: extremely customizable. The only required values are part=int and whole=int. Set other values as desired/necessary.

    factor_100 = [1, 2, 4, 5, 10, 20, 25, 50, 100]

    Use a factors inverse factor as a multiplier for an offset percentage independent of the progress bar.
        Example: if factor=100 then multiplier=1
        Example: factor=10 then multiplier=10 (has no opposing factor because 10 is in the middle).

    """

    if check_factor(factor) is True:
        prc = int(int(factor) * float((float(part) / whole)))

        if factor == 100:
            multiplier = 1
        elif factor == 50:
            multiplier = 2
        elif factor == 25:
            multiplier = 4
        elif factor == 20:
            multiplier = 5
        elif factor == 10:
            multiplier = 10
        elif factor == 5:
            multiplier = 20
        elif factor == 4:
            multiplier = 25
        elif factor == 2:
            multiplier = 50
        elif factor == 1:
            multiplier = 100

        offset = float(int(factor) * float((float(part) / whole))) * multiplier
        offset = int(offset)

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

        if encapsulate_l and encapsulate_r:
            if encapsulate_l_color and encapsulate_r_color:
                pr_data = color_[encapsulate_l_color] + encapsulate_l + colorama.Style.RESET_ALL + pr_data + str(' ' * int(int(factor) - prc)) + color_[encapsulate_r_color] + encapsulate_r + colorama.Style.RESET_ALL
            else:
                pr_data = encapsulate_l + pr_data + str(' ' * int(int(factor)-prc)) + encapsulate_r
        if percent is True:
            pr_data = str(offset) + '% ' + pr_data

        if pre_append:
            pr_data = pre_append + pr_data
        if append:
            pr_data = pr_data + append

        clear_console_line(char_limit=int(len(pr_data)))

        pr_technical_data(technical_data=pr_data)

    else:
        return False


def display_color_options():
    return color_.keys()
