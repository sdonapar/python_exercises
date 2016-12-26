
""""99 Bottles of Beer" is a traditional song in the United States and Canada.
It is popular to sing on long trips, as it has a very repetitive format which
is easy to memorize, and can take a long time to sing. The song's simple
lyrics are as follows:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.
The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers
reach zero."""

def sing_song(num=99):
    verse = """{0} bottles of beer on the wall, {1} bottles of beer.
Take one down, pass it around, {2} bottles of beer on the wall.\n"""
    for i in range(num,0,-1):
        print(verse.format(i,i,i-1))

if __name__ == '__main__':
    sing_song()
