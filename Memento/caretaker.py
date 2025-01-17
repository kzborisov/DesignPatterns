class Caretaker:
    """
    Memento
    - Stores the internal state (content) of the Originator.
    - Protects the state from external modifications.
    """

    def __init__(self):
        self._history = []

    def save(self, originator):
        memento = originator.save()
        self._history.append(memento)

    def undo(self, originator):
        if not self._history:
            return

        memento = self._history.pop()
        originator.restore(memento)
