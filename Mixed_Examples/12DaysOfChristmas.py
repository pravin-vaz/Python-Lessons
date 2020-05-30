#Code found on Twitter, Credit @mberry
#I just made it like a follow along lyrics using time.sleep

#Challenge students to make a sing along lyric video like this, which can be simple (chorus and verse) or complex like this using for loops and a list.



import time
presents = [('first', 'a partridge in a pear tree. \n'),
            ('second','two turtle doves and '),
            ('third', 'three french hens,'),
            ('fourth', 'four calling birds,'),
            ('fifth', 'five golden rings,'),
            ('sixth','six geese a laying,'),
            ('seventh','seven swans a swimming,'),
            ('eighth', 'eight maids a milking,'),
            ('ninth', 'nine ladies dancing,'),
            ('tenth', 'ten lords a leaping,'),
            ('eleventh','eleven pipers piping,'),
            ('twelfth','twelve drummers drumming,')]

total = 0

for i in range (12):
    print('On  the '+ presents[i][0]+ ' day of Christmas my true love sent to me:')
    time.sleep(2)
    for j in range(i, -1,-1):
        print(presents[j][1])
        time.sleep(2)
        total += j+1

print(total)
