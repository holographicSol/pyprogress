import pyprogress

print('\nExample 1:')
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
print('\n\n')

print('Example 2:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=True,
                            bg_color='WHITE',
                            pre_append='[SEARCHING] ')
print('\n\n')

print('Example 3:')
whole = 1000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole,
                            percent=False,
                            color='CYAN',
                            pre_append='[PROGRESS] ',
                            progress_char='|')
print('\n\n')

print('Example 4:')
whole = 10000
part = 0
while part < whole:
    part += 1
    pyprogress.progress_bar(part=part,
                            whole=whole)
print('\n\n')