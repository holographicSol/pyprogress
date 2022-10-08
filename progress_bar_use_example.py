import pyprogress

print('\n\n')
print('Example 1:')
whole = 10000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            size=5)
print('\n\n')

print('\nExample 2:')
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
                            size=10)
print('\n\n')

print('Example 3:')
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
                            size=20)
print('\n\n')

print('Example 4:')
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
                            size=25)
print('\n\n')

print('Example 5:')
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
                            size=50)
print('\n\n')

print('Example 6:')
whole = 10000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=False,
                            color='YELLOW',
                            pre_append='[PROGRESS] ',
                            progress_char='_',
                            size=100,
                            encapsulate_l='<',
                            encapsulate_r='>',
                            append=str(' ' + str(part)))
print('\n\n')
