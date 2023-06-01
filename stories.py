"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with a title, words and template text."""

        self.title = title
        self.prompts = words
        self.template = text
    
    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a sample of Story instances


creature = Story(
    "creature",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

adventure = Story(
    "adventure",
    ["place", "villian_name", "noun", "hero_name", "3rd_person_pronoun"],
    """Once upon a time, everyone lived in the peaceful {place}. However, a malevolent
       force known as {villian_name} stole the {noun}, plunging the world into darkness!
       It was up to {hero_name} and {3rd_person_pronoun} friends to save the day!"""
)

lazy = Story(
    "lazy",
    ["noun", "plural_noun", "adjective", "number", "name"],
    """So, there was this guy and he went to the {noun} to get some {plural_noun}. But then this 
       {adjective} guy walked up to him and asked for {number} dollars. And that's the story of
       how I met {name}"""
)

# Here's a list of all the titles for the Story instances

all_stories = [creature.title, adventure.title, lazy.title]

# Here's a list of all the Story instances

complete_stories = [creature, adventure, lazy]