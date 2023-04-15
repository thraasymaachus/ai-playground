import requests
import hashlib
import time
import tkinter as tk
from tkinter import messagebox

class WebsiteChangeDetector:
    def __init__(self, url, interval):
        self.url = url
        self.interval = interval
        self.previous_hash = None

    def get_site_content(self):
        response = requests.get(self.url)
        return response.text

    def has_changed(self):
        current_content = self.get_site_content()
        current_hash = hashlib.sha256(current_content.encode('utf-8')).hexdigest()

        if self.previous_hash is None:
            self.previous_hash = current_hash
            return False

        if self.previous_hash == current_hash:
            return False

        self.previous_hash = current_hash
        return True

    def monitor(self):
        while True:
            if self.has_changed():
                messagebox.showinfo("Website Change Alert", f"The content of {self.url} has changed!")
            time.sleep(self.interval)

def start_monitoring():
    url = url_entry.get()
    interval = int(interval_entry.get())
    detector = WebsiteChangeDetector(url, interval)
    detector.monitor()

app = tk.Tk()
app.title("Website Change Detector")

url_label = tk.Label(app, text="Website URL:")
url_label.grid(row=0, column=0)
url_entry = tk.Entry(app)
url_entry.grid(row=0, column=1)

interval_label = tk.Label(app, text="Check interval (seconds):")
interval_label.grid(row=1, column=0)
interval_entry = tk.Entry(app)
interval_entry.grid(row=1, column=1)

start_button = tk.Button(app, text="Start Monitoring", command=start_monitoring)
start_button.grid(row=2, column=0, columnspan=2)

app.mainloop()
