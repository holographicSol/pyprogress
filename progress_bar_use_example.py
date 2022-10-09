import pyprogress

print('\n\n')
print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            factor=5)
print('\n\n')

print('\nExample:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            color='MAGENTA',
                            pre_append='[DOWNLOADING] ',
                            encapsulate_l='[',
                            encapsulate_r=']',
                            progress_char='_',
                            factor=10)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color='WHITE',
                            pre_append='[SEARCHING] ',
                            progress_char=' ',
                            factor=20)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            color='CYAN',
                            pre_append='[PROGRESS] ',
                            progress_char='|',
                            factor=25)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color='GREEN',
                            pre_append='[PROGRESS] ',
                            progress_char=' ',
                            encapsulate_l='|',
                            encapsulate_r='|',
                            encapsulate_l_color='LIGHTMAGENTA_EX',
                            encapsulate_r_color='LIGHTMAGENTA_EX',
                            factor=50)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color='GREEN',
                            pre_append='[PROGRESS] ',
                            progress_char=' ',
                            encapsulate_l='|',
                            encapsulate_r='|',
                            encapsulate_l_color='LIGHTBLUE_EX',
                            encapsulate_r_color='LIGHTBLUE_EX',
                            factor=50)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color='GREEN',
                            pre_append='[PROGRESS] ',
                            progress_char=' ',
                            encapsulate_l='|',
                            encapsulate_r='|',
                            encapsulate_l_color='LIGHTCYAN_EX',
                            encapsulate_r_color='LIGHTCYAN_EX',
                            factor=50)
print('\n\n')

print('Example:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=False,
                            color='YELLOW',
                            pre_append='[PROGRESS] ',
                            progress_char='_',
                            factor=100,
                            encapsulate_l='<',
                            encapsulate_r='>',
                            append=str(' ' + str(part)))
print('\n\n')

print('Example :')
whole = 10000
part = 0
bg_i = 0
while part < whole:
    part += 1

    if bg_i < len(pyprogress.bg_color_):
        for index, key in enumerate(pyprogress.bg_color_):
            if index == bg_i:
                if 'WHITE' not in key:
                    bg = key
    else:
        bg_i = 0
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color=bg,
                            pre_append='[PROGRESS NEON FLASH] ',
                            progress_char=' ',
                            factor=100,
                            encapsulate_l='|',
                            encapsulate_r='|',
                            append=str(' ' + str(part)))
    bg_i += 1
print('\n\n')
