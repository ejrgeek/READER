from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from extract_text import ext_text
from play_text import play


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("READER")
        self.minsize(640, 400)

        self.labelFrame = ttk.Labelframe(self, text="Abrir imagem")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)

        self.button()

    def button(self):
        self.buttonBrowser = ttk.Button(self.labelFrame, text="Procurar Imagem", command=self.fileDialog)
        self.buttonBrowser.grid(column=1, row=1)

    def button_reader(self):
        self.buttonReader = ttk.Button(self.labelFrame, text="Tocar Audio", command=self.play_text_in_image)
        self.buttonReader.grid(column=2, row=2)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Selecione uma imagem",
                                                   filetypes=(("jpeg", "*.jpg"), ("png", "*.png")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.path_image = self.filename
        self.image = PhotoImage(file=self.path_image)
        try:
            self.label.configure(image=self.image)
        except Exception as e:
            pass
        finally:
            self.button_reader()

    def play_text_in_image(self):
        text = ext_text(self.filename)
        play(text)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
