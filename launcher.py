import tkinter as tk
from tkinter import filedialog
import os
import subprocess, sys #--> for Mac system

opener ="open" if sys.platform == "darwin" else "xdg-open" #--> For Mac system

root=tk.Tk()
apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt','r',) as f:
        tempapps=f.read()
        tempapps = tempapps.split(',')
        apps=[x for x in tempapps if x.strip()]
        
def AddApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    
    filename=filedialog.askopenfilename(initialdir='/',title='select file',
                                        filetypes=(("executables","*.*"),("all files",'*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg='blue')
        label.pack()    
        
def  runapps():
    for app in apps:
        #os.startfile(app)--> for windows system
        subprocess.call([opener, app])# --> for mac system
        
    
canvas=tk.Canvas(root,height=700,width=700,bg='#0FA6AB')
canvas.pack()
frame =tk.Frame(root,bg='white')
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openfile=tk.Button(root,text='Open File',padx=10,pady=5,fg='black',bg='#0FA6AB',command=AddApp)
openfile.pack()
runApps=tk.Button(root,text='Run Apps',padx=10,pady=5,fg='black',bg='#0FA6AB',command=runapps)
runApps.pack()

for app in apps:
    label=tk.Label(frame,text=app)
    label.pack

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
