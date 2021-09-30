def equalsTen(x):
    if x == 10:
        return "x equals 10!!!!!!!"

    elif x > 10:
        return "x is greater than 10"

    else:
        return "x is not equal to 10"

print(equalsTen(10))

def favColor(color):
    if color == "red":
        return "your favorite color is red"

    else:
        return "your favorite color is not red"

print(favColor("red"))

def define(word):
    if word.lower() == "hey":
        return "(used as an exclamation to call attention or to express pleasure, surprise, bewilderment, etc.)"

    elif word.lower() == "horse":
        return "a large, solid-hoofed, herbivorous quadruped, Equus caballus, domesticated since prehistoric times, bred in a number of varieties, and used for carrying or pulling loads, for riding, and for racing."

    elif word.lower() == "turtle":
        return "any reptile of the order Testudines, comprising aquatic and terrestrial species having the trunk enclosed in a shell consisting of a dorsal carapace and a ventral plastron."

    elif word.lower() == "mammal":
        return "any vertebrate of the class Mammalia, having the body more or less covered with hair, nourishing the young with milk from the mammary glands, and, with the exception of the egg-laying monotremes, giving birth to live young."

    elif word.lower() == "dictionary":
        return "a book giving information on particular subjects or on a particular class of words, names, or facts, usually arranged alphabetically:"

    elif word.lower() == "synonym":
        return "a word having the same or nearly the same meaning as another in the language, as happy, joyful, elated. A dictionary of synonyms and antonyms (or opposites), such as Thesaurus.com, is called a thesaurus."

    elif word.lower() == "leg":
        return "either of the two lower limbs of a biped, as a human being, or any of the paired limbs of an animal, arthropod, etc., that support and move the body."

    elif word.lower() == "massive":
        return "large in scale, amount, or degree"

    elif word.lower() == "cow":
        return "the mature female of a bovine animal, especially of the genus Bos."

    elif word.lower() == "capable":
        return "having power and ability; efficient; competent"

    else:
        return "I dont know"

print(define("leg"))

print(99 % 100) 