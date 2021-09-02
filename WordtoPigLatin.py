"""To form Pig Latin words from words beginning with a consonant (like hello) or a consonant cluster (like switch), 
simply move the consonant or consonant cluster from the start of the word to the end of the word. Then add the suffix "-ay" to the end of the word.
Here from hello h is moved to the end and ay is added after that
example:

1. word: it     pigLatin:  it-yay

2. word:glove   pigLatin:  ove-glay

3. word:hello   piglatin:  ello-hay
"""


def w2pl(word):
    """Convert word to Pig Latin."""
    vowels = "AaEeIiOoUu"
   
    if not any(char in word for char in vowels):
        vowels = "Yy"
  
    x = min(word.find(char) for char in word if char in vowels)
    if word[0] in "aAeEiIoOuU":
        plword = f"{word[x:]}-{word[:x]}yay"
    else:
        plword = f"{word[x:]}-{word[:x]}ay"
    return plword.capitalize() if word[0].isupper() else plword


print(" ".join((w2pl(word) for word in input().split())))
