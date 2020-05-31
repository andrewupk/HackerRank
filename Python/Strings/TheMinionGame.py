def minion_game(string):
    # your code goes here
    stuart = 0  #consonants
    kevin = 0   #vowels     AEIOU

    consonants = []
    vowels = []

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowels.append(i)
        else:
            consonants.append(i)

    print('Vowels: {0}'.format(vowels))
    print('Consonants: {0}'.format(consonants))

    for i in consonants:
        stuart += len(string) - i

    for i in vowels:
        kevin += len(string) - i

    if stuart > kevin:
        print('Stuart {0}'.format(stuart))
    if kevin > stuart:
        print('Kevin {0}'.format(kevin))
    if stuart == kevin:
        print('Draw')




if __name__ == '__main__':
    s = input()
    minion_game(s)