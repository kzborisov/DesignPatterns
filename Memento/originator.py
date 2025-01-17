from memento import Memento

class Editor:
    """
    Originator
    - Manages the internal state (content) of our text editor.
    - Can create and restore Memento objects.
    """

    def __init__(self):
        self._content = ""

    def type(self, text):
        self._content += text

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()

    def get_content(self):
        return self._content
