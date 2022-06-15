'''

Excercise 7

This exercise is meant to help you practice thinking in this way. Here, you’ll imple-
ment a translator from English into another secret children’s language, Ubbi Dubbi
(http://mng.bz/90zl)

In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub . Thus milk becomes
mubilk ( m-ub-ilk ) and program becomes prubogrubam ( prub-ogrub-am ). In theory,
you only put an ub before every vowel sound, rather than before each vowel. Given that
this is a book about Python and not linguistics, I hope that you’ll forgive this slight dif-
ference in definition.

For this exercise, you’ll write a function (called ubbi_dubbi ) that takes a single
word (string) as an argument. It returns a string, the word’s translation into Ubbi
Dubbi. So if the function is called with octopus , the function will return the string
uboctubopubus . And if the user passes the argument elephant , you’ll output
ubelubephubant.

'''

def ubbi_dubbi(word):
    letters = []
    new_list = []
    for letter in word:
        letters.append(letter)
    print(letters)
    for letter in letters:
        if letter in 'aeiou':
            new_list.append('ub')
        new_list.append(letter)
    return ''.join(new_list)
    
print(ubbi_dubbi('elephant'))
print(ubbi_dubbi('octopus'))
