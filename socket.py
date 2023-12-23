import tkinter as tk
from socket import *
import time
from tkinter import scrolledtext

def scan_ports():
    target = entry.get()
    t_IP = gethostbyname(target)
    result_text.delete(1.0, tk.END)
    startTime=time.time()# Clear previous results

    for i in range(1, 10000):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            result_text.insert(tk.END, 'Port %d: OPEN\n' % (i,))
        s.close()

    result_text.insert(tk.END, 'Time taken: {:.2f} seconds'.format(time.time() - startTime))

# GUI setup
app = tk.Tk()
app.title("Port Scanner")

label = tk.Label(app, text="Enter the host to be scanned (use 'localhost' or '127.0.0.1' for your local machine):")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

scan_button = tk.Button(app, text="Scan Ports", command=scan_ports)
scan_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(app, width=40, height=10)
result_text.pack(pady=10)

app.mainloop()
