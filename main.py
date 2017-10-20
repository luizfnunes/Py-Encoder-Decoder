from tkinter import *
from tkinter import messagebox

import base64, hashlib,os

class Encoder:
    def __init__(self):
        """ Criar a janela """
        self.window = Tk()
        x = (self.window.winfo_screenwidth() / 2) - (400 / 2)
        y = (self.window.winfo_screenheight() / 2) - (500 / 2)
        self.window.title("Encoder/Decoder")
        self.window.geometry("400x500+{}+{}".format(int(x),int(y)))
        self.window.resizable(False,False)
        if os.path.isfile("icon.ico"):
            self.window.iconbitmap(bitmap="icon.ico")
        """Cria os widgets"""
        self.create_widgets()
        """Criar o Loop """
        self.window.mainloop()

    def create_widgets(self):
        """ Cria o menu inicial """
        self.create_menu()
        """ Cria a area de input """
        self.create_input()
        """ Cria a area de output"""
        self.create_output()
        """ Cria Popup Menu para Output """
        self.create_popup()
        """ Cria a area de radio buttons"""
        self.create_radios()
        """ Cria a area de botoes"""
        self.create_buttons()

    def create_menu(self):
        self.menubar = Menu(self.window)
        self.menubar.add_command(label="About",command=self.command_about)
        self.menubar.add_command(label="Quit",command=self.command_quit)
        self.window["menu"] = self.menubar

    def create_input(self):
        self.containerInput = Frame(self.window,padx=5,pady=5)
        self.containerInput.grid()
        self.labelInput = Label(self.containerInput,text="Input:  ")
        self.labelInput.grid(row=0,column=0)
        self.textInput = Text(self.containerInput,width=40,height=10)
        self.textInput.grid(row=1,column=1)

    def create_output(self):
        self.containerOutput = Frame(self.window, padx=5, pady=5)
        self.containerOutput.grid()
        self.labelOutput = Label(self.containerOutput,text="Output:")
        self.labelOutput.grid(row=0,column=0)
        self.textOutput = Text(self.containerOutput,width=40,height=10,state=DISABLED)
        self.textOutput.bind("<Button-3>",self.show_popup)
        self.textOutput.grid(row=1,column=1)

    def create_popup(self):
        self.popmenu = Menu(self.containerOutput, tearoff=0)
        self.popmenu.add_command(label="Copy",command=self.copy_output)
    
    def show_popup(self,event):
        self.popmenu.post(event.x_root,event.y_root)

    def copy_output(self):
        content = self.textOutput.get(1.0,END)
        self.window.clipboard_clear()
        self.window.clipboard_append(content)

    def create_radios(self):
        """ Seta o modo de codificação """
        self.encode_mode = IntVar()
        self.encode_mode.set(0)
        self.containerRadios = Frame(self.window, padx=5, pady=5)
        self.containerRadios.grid()
        self.radioButtonBase64 = Radiobutton(self.containerRadios,text="Base64", variable=self.encode_mode, value=0,\
        command=self.command_active_decoder)
        self.radioButtonBase64.grid(row=0,column=0)
        self.radioButtonBase64.select()
        self.radioButtonMd5 = Radiobutton(self.containerRadios,text="MD5", variable=self.encode_mode, value=1,\
        command=self.command_desactive_decoder)
        self.radioButtonMd5.grid(row=0,column=1)
        self.radioButtonSHA1 = Radiobutton(self.containerRadios,text="SHA1",variable=self.encode_mode, value=2,\
        command=self.command_desactive_decoder)
        self.radioButtonSHA1.grid(row=0,column=2)
    
    def create_buttons(self):
        self.containerButtons = Frame(self.window,padx=5, pady=5)
        self.containerButtons.grid()
        self.buttonEncode = Button(self.containerButtons,text="Encode",command=self.command_encode)
        self.buttonEncode.grid(row=0,column=0,padx=5,pady=5)
        self.buttonDecode = Button(self.containerButtons,text="Decode",command=self.command_decode)
        self.buttonDecode.grid(row=0,column=1,padx=5,pady=5)

    def command_about(self):
        messagebox.showinfo("Encode/Decode",\
        "Single encoder/decoder from strings.\nCreated by luizfnunes in 2017\nwith Python3 and Tkinter")
    def command_quit(self):
        self.window.quit()

    def command_active_decoder(self):
        self.buttonDecode["state"] = NORMAL

    def command_desactive_decoder(self):
        self.buttonDecode["state"] = DISABLED

    def command_encode(self):
        mode = self.encode_mode.get()
        text = self.textInput.get(1.0,END)
        crypt = ""
        if mode == 0:
            try:
                crypt = base64.b64encode(text.encode())
            except Exception as e:
                messagebox.showwarning("Error","Error found: \n {}".format(str(e)))
        if mode == 1:
            objcrypt = hashlib.md5(text.encode())
            crypt = objcrypt.hexdigest()
        if mode == 2:
            objcrypt = hashlib.sha1(text.encode())
            crypt = objcrypt.hexdigest()
        
        self.textOutput["state"] = NORMAL
        self.textOutput.delete(1.0,END)
        self.textOutput.insert(END, crypt)
        self.textOutput["state"] = DISABLED
        
    def command_decode(self):
        mode = self.encode_mode.get()
        text = self.textInput.get(1.0,END)
        crypt = ""
        try:
            crypt = base64.b64decode(text.encode())
        except Exception as e:
            messagebox.showwarning("Error","Error found: \n {}".format(str(e)))
        self.textOutput["state"] = NORMAL
        self.textOutput.delete(1.0,END)
        self.textOutput.insert(END, crypt)
        self.textOutput["state"] = DISABLED

if __name__=="__main__":
    App = Encoder()