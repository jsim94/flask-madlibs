"""Madlibs Stories."""


# created new class to help add and manage stories during runtime without storage
class StoryList:
    def __init__(self):
        self.stories = {}
        self.chosen = None
        self.current_id = 0

    def add(self, name, prompts, template):
        self.stories[self.current_id] = Story(
            self.current_id, name, prompts, template)
        self.current_id += 1

    def get_chosen(self):
        return self.stories[self.chosen]


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

    def __init__(self, id, name, words, text):
        """Create story with words and template text."""
        self.id = id
        self.name = name
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        print(text)
        return text
