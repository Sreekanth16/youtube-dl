import tkinter as tk 
from tkinter import messagebox
import webbrowser
import os


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Youtube Video Downloader", font=45)
        label.pack(pady=10,padx=10)

        link1 = tk.Label(self, text="Download by URL", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: controller.show_frame(PageUrl))
        
        link2 = tk.Label(self, text="Advanced Download", fg="blue", cursor="hand2")
        link2.pack()
        link2.bind("<Button-1>", lambda e: controller.show_frame(PageAdvanced))
        

class PageUrl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Download by URL", font=22)
        label.pack(pady=10,padx=10)
        
        l = tk.Label(self, text="Video Hyperlink")
        l.pack()
        
        E1 = tk.Entry(self, bd =20)
        E1.pack()
        
        button = tk.Button(self, text='Download', width=50, command=lambda:self.action1(E1.get()))
        button.pack()
        
        button1 = tk.Button(self, text="Back to Home",command=lambda:controller.show_frame(HomePage))
        button1.pack()

        button2 = tk.Button(self, text="Advanced download",command=lambda: controller.show_frame(PageAdvanced))
        button2.pack()

    def action1(self,str):
        print("Link: %s"%str)
        cmd = "youtube-dl "+ str
        print(cmd)
        status = os.system(cmd)
        print(status)
        if status == 256:
            messagebox.showinfo("Error", "Video cannot be Downloaded")
        elif status == 0:
            messagebox.showinfo("Success", "Video Downloaded")
        
                    
class PageAdvanced(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Advanced download", font=22)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.pack()
        button2 = tk.Button(self, text="Download by URL",command=lambda: controller.show_frame(PageUrl))
        button2.pack()
        
class youtube_dl(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (HomePage, PageUrl, PageAdvanced):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
            self.show_frame(HomePage)
            
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
if __name__ == "__main__":
    root = youtube_dl()
    root.mainloop()
