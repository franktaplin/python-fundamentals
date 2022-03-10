# the bottles of beer soneg
# this demonstartes looping and conditional statements

def beer_song():
    bottles_of_beer = 99
    word = 'bottles'

    while bottles_of_beer > 0:
        if bottles_of_beer == 1:
            word = 'bottle'

        print('{0} {1} of beer on the wall.'.format(bottles_of_beer, word))
        print('{0} {1} of beer.'.format(bottles_of_beer, word))
        print('Take one down')
        print('Pass it around')

        bottles_of_beer -= 1
        # bottles_of_beer = bottles_of_beer - 1

        if bottles_of_beer > 0:
            print('{0} {1} of beer on the wall.'.format(bottles_of_beer, word))
            print('')
        else:
            print('')
            print('No more bottles of beer on the wall.')


beer_song()