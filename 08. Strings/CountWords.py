"""
Count Words in given text
02.11.2018 21:10
Bogdan Prădatu
"""

test_text = """
By taking a shape, by having a visible plan, you open yourself to attack. Instead of taking a form
for your enemy to grasp keep yourself adaptable and on the move. Accept the fact that nothing is certain
and no law is fixed. The best way to protect yourself is to be as fluid and formless as water; never bet
on stability or lasting order. Everything changes.

The way of the world 
· In the face of the world's harshness and danger, organisms of any kind develop protection—a coat of armor,
a rigid system, a comforting ritual. 
· For the short term it may work, but for the long term it spells disaster. 
· People weighed down by a system and inflexible ways of doing things cannot move fast, cannot sense or adapt
to change. 
· People lumber around more and more slowly until they go the way of the brontosaurus. 
· Learn to move fast and adapt or you will be eaten.
· The best way to avoid this fate is to assume formlessness. 
· No predator alive can attack what it cannot see. 
Value Movement over Position 
· Your speed and mobility make it impossible to predict your moves
· Unable to understand you, your enemy can form no strategy to defeat you. 
· Instead of fixing on particular spots, this indirect form of warfare spreads out, just as you can use the large
and disconnected nature of the real world to your advantage. 
· Be like a vapor. Do not give your opponents anything solid to attack; watch as they exhaust themselves pursuing
you, trying to cope with your elusiveness. 
· Only formlessness allows you to truly surprise your enemies.
· By the time they figure out where you are and what you are up to, it is too late. 

10 Reasons to Emulate the Powerful 
1. The powerful are often people who in their youth have shown immense creativity in expressing something new through
a new form. 
2. Society grants them power because it hungers for and rewards this sort of newness. 
3. Power can only thrive if it is flexible in its forms. 
4. To be formless is not to be amorphous; everything has a form—it is impossible to avoid. 
5. The formlessness of power is more like that of water, or mercury, taking the form of whatever is around it. 
6. Changing constantly, it is never predictable. 
7. The powerful are constantly creating form. 
8. Their power comes from the rapidity with which they can change. 
9. Formlessness is in the eye of the enemy who cannot see what they are up to and so has nothing solid to attack. 
10. This is the premier pose of power: ungraspable, as elusive and swift as the god Mercury, who could take any form
he pleased and used this ability to wreak havoc on Mount Olympus. 
WARNINGS 
· The first psychological requirement of formlessness is to train yourself to take nothing personally. 
· Never show any defensiveness. 
· When you act defensive, you show your emotions, revealing a clear form. 
· Your opponents will realize they have hit a nerve, an Achilles' heel. And they will hit it again and again. 
· Never let anyone get your back up. 
· Be like a slippery ball that cannot be held.
· Let no one know what gets to you, or where your weaknesses are. 
· Make your face a formless mask and you will infuriate and disorient your scheming colleagues and opponents.

Formlessness makes your enemies hunt all over for you, scattering their own forces, mental as well as physical.
When you play with formlessness, keep on top of the process, and keep your long-term strategy in mind. When you
assume a form and go on the attack, use concentration, speed, and power."""

punctuation = "~!@#$%^&*()_-=+[{]}\\|'\";:,<.>/?"


def remove_punctuation(text):
    text_wo_punctuation = ""
    for word in text:
        if word not in punctuation:
            text_wo_punctuation += word
    return text_wo_punctuation


def count_words(text):
    words = remove_punctuation(text).lower().split()
    word_no = 0
    for word in words:
        word_no += 1
    return word_no


def count_words_e(text):
    words = remove_punctuation(text).lower().split()
    word_no_e = 0
    for word in words:
        if "e" in word:
            word_no_e += 1
        else:
            continue
    return word_no_e    


print(
    "Your text contains", count_words(remove_punctuation(test_text)),
    "words, of which", count_words_e(remove_punctuation(test_text)),
    "contain the letter 'e'.")


