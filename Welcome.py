import os
try:
    import tkinter as tk
except ImportError:  # the toolkit is optional: the greeting is the contract
    tk = None

GREETING = "Welcome to Blitzy"
HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(HERE, "dummy.png")
FALLBACK_SIZE = (400, 150)


def main():
    """Print the greeting, then show it over the image in one window."""
    print(GREETING)
    if tk is None:
        return
    try:
        root = tk.Tk()
        root.title(GREETING)
        try:
            photo = tk.PhotoImage(file=IMAGE_PATH)
        except tk.TclError:  # missing, unreadable or not decodable
            photo = None
        size = (photo.width(), photo.height()) if photo else FALLBACK_SIZE
        centre = (size[0] // 2, size[1] // 2)
        font_size = max(4, min(24, (size[0] - 8) // 16, (size[1] - 8) // 2))
        root.geometry("%dx%d" % size)  # wm calls precede the canvas (Tk 9.1)
        root.resizable(False, False)
        canvas = tk.Canvas(root, width=size[0], height=size[1],
                           highlightthickness=0, bd=0)
        canvas.pack(fill="both", expand=True)
        if photo is not None:
            canvas.image = photo  # Tk keeps no reference of its own
            canvas.create_image(*centre, image=photo)
        canvas.create_text(*centre, text=GREETING, fill="black",
                           font=("TkDefaultFont", font_size))
        root.mainloop()
    except Exception:  # no display or no toolkit window: report nothing
        pass


if __name__ == "__main__":
    main()
