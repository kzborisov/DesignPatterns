from originator import Editor
from caretaker import Caretaker


if __name__ == "__main__":
    editor = Editor()  # Originator
    caretaker = Caretaker()

    caretaker.save(editor)
    editor.type("Hello, ")
    caretaker.save(editor)

    editor.type("World!")

    print("Current content:", editor.get_content())

    caretaker.undo(editor)
    print("After 1st undo:", editor.get_content())
    caretaker.undo(editor)
    print("After 2nd undo:", editor.get_content())
