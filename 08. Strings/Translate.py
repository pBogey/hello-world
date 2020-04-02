"""
26.12.2018 22:06
String translate method
Bogdan Prădatu
"""

t = """It has been over eleven years since the bubble peak.
In the Case-Shiller release this morning, the seasonally adjusted
National Index (SA), was reported as being 11.4% above the previous
bubble peak. However, in real terms, the National index (SA) is still
about 8.9% below the bubble peak (and historically there has been an
upward slope to real house prices).  The composite 20, in real terms,
is still 12.4% below the bubble peak."""

def translate_text(text):
    """Return cleaned text"""
    #Create filtering table for translate method
    flt = text.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’",
        "abcdefghijklmnopqrstuvwxyz                                         ")
    #filters must be of equal length
    cleaned_text = text.translate(flt)
    words = cleaned_text.split()
    return words
    
print(t)
print("**********************************************")
print(translate_text(t))
