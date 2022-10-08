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


def check_factor(size):
    allow_bool = False
    if size in factor_100:
        allow_bool = True
    return allow_bool


def clear_console_line(char_limit):
    """ clear n chars from console """

    print(' '*char_limit, end='\r', flush=True)


def pr_technical_data(technical_data):
    """ clears console line and then prints """

    print(technical_data, end='\r', flush=True)


def progress_bar(part, whole, percent=True, color='', bg_color='', pre_append='', append='', encapsulate_l='', encapsulate_r='', progress_char='', size=100):
    """
    part=int, whole=int, percent=bool,
    color=str, bg_color=str
    pre_append=str, append=str,
    encapsulate_l=str, encapsule_r=str,
    progress_char=str,
    size=int (factor of 100:  1, 2, 4, 5, 10, 20, 25, 50, and 100)
    """
    if check_factor(size) is True:
        prc = int(int(size) * float((float(part) / whole)))

        offset = int(prc * int((100 / size)))

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
            pr_data = encapsulate_l + pr_data + str(' ' * int(int(size)-prc)) + encapsulate_r
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
