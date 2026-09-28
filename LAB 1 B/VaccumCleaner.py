# Vacuum Cleaner Problem

room = {
    'A': 'Dirty',
    'B': 'Dirty'
}

position = 'A'

while True:
    print("NAME : Shashank Shinde\nUSN : 1BF24CS277")
    print("\nCurrent position:", position)
    print("Room A:", room['A'])
    print("Room B:", room['B'])

    if room[position] == 'Dirty':
        print("Action: Suck")
        room[position] = 'Clean'

    else:
        if position == 'A':
            print("Action: Move Right")
            position = 'B'
        else:
            print("Action: Move Left")
            position = 'A'

    if room['A'] == 'Clean' and room['B'] == 'Clean':
        print("\nBoth rooms are clean!")
        break