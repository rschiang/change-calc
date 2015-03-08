s = ''

units = [1000, 500, 100, 50, 10, 5, 1]
total = 0
total_changes = { unit : 0 for unit in units }

while s.lower() != 'end':
    try:
        num = int(s.strip())
    except ValueError:
        try:
            s = input('>>> ')
        except EOFError:
            print('')
            break
        continue

    changes = {}
    remaining = num
    for unit in units:
        change = remaining // unit
        remaining = remaining % unit

        if change > 0:
            changes[unit] = change

        if remaining == 0:
            break

    print(num, '=', ' + '.join(['{0} x {1}'.format(unit, changes[unit]) for unit in units if unit in changes]))

    total += num
    for unit, change in changes.items():
        total_changes[unit] += change

    try:
        s = input('>>> ')
    except EOFError:
        print('')
        break

print('Total:', total)
for unit in units:
    print(unit, 'x', total_changes[unit])
