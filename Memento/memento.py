class Memento:
    """
    Memento
    - Stores the internal state (content) of the Originator.
    - Protects the state from external modifications.
    """

    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content
