import tkinter as tk
from tkinter import filedialog, END
from tkinter import messagebox
import socket
import nmap

# Object
scanner = nmap.PortScanner()


class Window(tk.Tk):

    def __init__(self):
        """
            Fonction d'initialisation des widgets
        """
        tk.Tk.__init__(self)
        # Main Title
        self.label = tk.Label(self, text="Enter hostname : ")
        # Input User
        self.entry = tk.Entry(self)
        # Text Area
        self.text_result = tk.Text(self, height=20, width=90, bg="#d6d6d6")
        # Quit BTN
        self.quit_btn = tk.Button(self, text="Quitter", command=self.quit)
        # Ip Resolver BTN
        self.port_scanner = tk.Button(self, text="Port Scanner", command=self.port_scanner)
        # Save As BTN
        self.save_as = tk.Button(self, text="Save As...", command=self.save_as)
        # Widgets Packing
        self.pack_widgets()

    def pack_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.port_scanner.pack()
        self.text_result.pack()
        self.save_as.pack()
        self.quit_btn.pack()

    def save_as(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text_to_save = self.text_result.get(1.0, END)
        file.write(text_to_save)
        file.close()

    def port_scanner(self):
        hostname = self.entry.get()
        try:
            ipv4 = socket.gethostbyname(hostname)
            self.text_result.insert("1.0", hostname + " : " + ipv4 + "\n")
            scanner.scan(ipv4, arguments='-F')
            for port in scanner[ipv4]['tcp']:
                port_data = scanner[ipv4]['tcp'][port]
                self.text_result.insert("2.0", 'Port {0} Service : {1} \n'.format(port, port_data.get('name')))
        except socket.gaierror:
            tk.messagebox.showerror(title="Erreur ! ", message="Nom de domaine introuvable")


if __name__ == "__main__":
    fen = Window()
    fen.title("TCP/IP Scanner in python")
    fen.geometry("500x500")
    fen.resizable(False, False)
    fen.mainloop()
