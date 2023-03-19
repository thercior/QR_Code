import qrcode
from tkinter import Tk, Entry, Button, Label, messagebox
import os

def qr_code_generator():
    url = site_entry.get()
    
    if len(url) == 0:
        messagebox.showerror(
            title="Error!", 
            message="Por favor, insira uma URL válida")
    else:
        escolha = messagebox.askokcancel(
            title="QR Code Generator", 
            message=f"O endereço url é: \n"
                    f"{url}\n"
                    f"Deseja gerar o código QR e salvar?"
        )
        
        if escolha:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            pasta = "./qrcode"
            if os.path.exists(pasta):
                print('Pasta existente')
            else:
                os.mkdir(pasta)
            
            img.save(pasta+"/qrcode.png")
            messagebox.showinfo(
                    title="QR Code Generator", 
                    message=f"O código QR é: \n"
                            f"{img}\n"
                            f"Salvo com sucesso!"
                )

if __name__ == "__main__":
    # Criação da janela
    window = Tk()
    window.title("QR Code Generator")
    window.geometry("500x300")
    window.resizable(False, False)
    window.config(padx=10,pady=100)
    
    #Label
    site_label = Label(text="URL: ")
    site_label.grid(row=2,column=0)
    
    #Entrada
    site_entry = Entry(width=40)
    site_entry.grid(row=2,column=1, columnspan=2)
    site_entry.focus()
    botao = Button(text="Gerar QR Code", width=40, command=qr_code_generator)
    botao.grid(row=4,column=1, columnspan=2)
    
    window.mainloop()
    
    
    