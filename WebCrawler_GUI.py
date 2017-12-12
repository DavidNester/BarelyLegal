from tkinter import *

url = ''
seeds = []
ALLOWED_DOMAINS = ['.com','.edu','.gov','.net','.org']

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    
    
    def init_window(self):

        self.master.title("WebCrawler")
        self.pack(fill=BOTH,expand=1)
        self.configure(background="black")
        #quitButton = Button(self,text='Quit', command=self.client_exit)
        #quitButton.place(x=69, y=69)

        lbl = Label(self, text = 'welcome label')
        lbl.pack()
        #lbl.place(x=150,y=5)

        

        self.ent = Entry(self)
        self.ent.pack()
        #self.ent.place(x=150,y=25)

        btn = Button(self, text='enter',command=self.seeds)
        btn.pack()
        #btn.place(x=150,y=45)

        if len(seeds) != 0:
            self.btn_next = Button(self, text='next',command=self.keywords)
            self.btn_next.pack()

        self.lbl_confirm = Label(self, text = 'enter seed(s) in box above')
        self.lbl_confirm.pack()

        
        # define menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #file button
        file = Menu(menu)
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='Menu',menu=file)

##        #edit button
##        edit = Menu(menu)
##        edit.add_command(label='ShowText', command=self.showTxt)
##        menu.add_cascade(label='Edit',menu=edit)
        

    def client_exit(self):
        exit()

    def showTxt(self):
        text = Label(self, text='Hello there')
        text.place(x=100,y=100)

    def seeds(self):
        global url
        global seeds
        url = self.ent.get()
        self.ent.delete(0,'end')
        if check_domain(url):
            self.lbl_confirm.config(text = url + ' added to seeds')# = Label(self, text = url + ' added')
            self.lbl_confirm.pack()
            seeds.append(url)
            self.btn_next = Button(self, text='next',command=self.keywords)
            self.btn_next.pack()
        elif len(seeds) == 0 and url == '':
            self.lbl_confirm.config(text = 'Error: must have at least one nonempty seed')# = Label(self, text = url + ' added')
            self.lbl_confirm.pack()
        else:
            self.lbl_confirm.config(text = "Enter URL that contains .com, .edu, .gov, .net, .org")# = Label(self, text = url + ' added')
            self.lbl_confirm.pack()
            
    def keywords(self):
        pass

def check_domain(address):
    '''
    checks given address to determine if it is valid
    returns True or False
    '''
    for i in ALLOWED_DOMAINS:
        if (str(i+'/') in address or address.endswith(i)) and len(address) >= 5:
            return True
    return False
        
    
root = Tk()
root.geometry("500x300")
app = Window(root)

root.mainloop()
