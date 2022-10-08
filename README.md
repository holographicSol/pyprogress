# pyprogress
A simple and customizable coloured progress bar module for cli applications.

Simple Example:

import pyprogress

whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            color='MAGENTA',
                            pre_append='[DOWNLOADING] ',
                            encapsule_l='[',
                            encapsule_r=']',
                            progress_char='_')
print('')



A list of available color's can be returned using:
pyprogress.display_color_options()

Requirements:
Written with python 3.10.1 on Windows 10.
pip install colorama.
