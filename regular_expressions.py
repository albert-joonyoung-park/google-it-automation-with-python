import re


# Simple Matching

result = re.search(r"aza", "plaza")  # always use raw string 'r'
print(result)  # <re.Match object; span=(2, 5), match='aza'>
result = re.search(r"aza", "bazaar")
print(result)  # <re.Match object; span=(1, 4), match='aza'>
result = re.search(r"aza", "maze")
print(result)  # None

# ^: circumflex any leading char with...
print(re.search(r"^x", "xenon"))  # <re.Match object; span=(0, 1), match='x'>
# .: any single character
print(re.search(r"p.ng", "penguin"))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "clapping"))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "sponge"))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "sponGe", re.IGNORECASE))  # <re.Match object; span=(1, 5), match='ponG'>

# Question:
# Check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None, result  # True if match found, and Match object

print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True


# Wildcards and Character Classes, regexes used in [] for matching

# Character Classes
print(re.search(r"[Pp]ython", "Python")) # match the word 'Python' or 'python'

# [a-z], any lowercase letter
print(re.search(r"[a-z]way", "The end of the highway"))  # <re.Match object; span=(18, 22), match='hway'>
print(re.search(r"[a-z]way", "What a way to go"))  # <re.Match object; span=(18, 22), match='hway'>

# [A-Z], [0-9], any uppercase letter, any number
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))  # <re.Match object; span=(0, 6), match='cloudy'>
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))  # <re.Match object; span=(0, 6), match='cloud9'>

# Question:
# Check if  the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
def check_punctuation (text):
    result = re.search(r"[,.:;?!]", text)
    return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True

# ^ as Negation, [^a-zA-Z]: Any character that are NOT lowercase or uppercase letter
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))  # <re.Match object; span=(4, 5), match=' '>
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))  # <re.Match object; span=(30, 31), match='.'>

# |(pipe) to match either This of That expressions
print(re.search(r"cat|dog", "I like cats."))  # <re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs."))  # <re.Match object; span=(7, 10), match='dog'>

