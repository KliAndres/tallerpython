GIFTS = {1: 'a Partridge in a Pear Tree', 2: 'two Turtle Doves', 3: 'three French Hens',
        4: 'four Calling Birds', 5: 'five Gold Rings', 6: 'six Geese-a-Laying',
        7: 'seven Swans-a-Swimming', 8: 'eight Maids-a-Milking', 9: 'nine Ladies Dancing',
        10: 'ten Lords-a-Leaping', 11: 'eleven Pipers Piping', 12: 'twelve Drummers Drumming'}

DAYS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
        'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

def recite(start_verse, end_verse):
    lyrics = []
    for day in range(start_verse, end_verse + 1):
        verse = f'On the {DAYS[day-1]} day of Christmas my true love gave to me: '
        for gift in range(day, 0, -1):
            verse = verse + ('and ' if (gift == 1 and day > 1) else '')
            verse = verse + GIFTS[gift]
            verse = verse + ('.' if gift == 1 else ', ')
        lyrics.append(verse)
    return lyrics