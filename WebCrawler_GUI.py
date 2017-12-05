from tkinter import *
# http://usingpython.com/using-tkinter/
url = ''
seeds = []
ALLOWED_DOMAINS = ['.com','.edu','.gov','.net','.org']
keywords = []
termination = []

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("WebCrawler")
        self.pack(fill=BOTH,expand=1)
        #self.configure(background="black")

        lbl = Label(self, text = 'welcome label')
        lbl.pack()
        #lbl.place(x=150,y=5)

        self.ent = Entry(self)
        self.ent.pack()
        #self.ent.place(x=150,y=25)

        self.btn_enter = Button(self, text='enter',command=self.get_seeds)
        self.btn_enter.pack()
        #btn.place(x=150,y=45)

        self.btn_next = Button(self, text='next',command=self.keywords,state=DISABLED)
        self.btn_next.pack()
        
        self.lbl_msg = Label(self, text = 'enter seed(s) in box above')
        self.lbl_msg.pack()

        # define dropdown menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #file button & exit
        file = Menu(menu)
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='Menu',menu=file)

    def client_exit(self):
        exit()

    def showTxt(self):
        text = Label(self, text='Hello there')
        text.place(x=100,y=100)

    def get_seeds(self):
        global url
        global seeds
        url = self.ent.get().lower()
        self.ent.delete(0,'end')
        if check_domain(url):
            self.lbl_msg.config(text = url + ' added to seeds\nAdd another seed or next to continue')
            self.lbl_msg.pack()
            seeds.append(url)
            self.btn_next.config(text='next',command=self.keywords,state='normal')
            self.btn_next.pack()
        elif len(seeds) == 0 and url == '':
            self.lbl_msg.config(text = 'Error: must have at least one nonempty seed')
            self.lbl_msg.pack()
        else:
            self.lbl_msg.config(text = "Enter URL that contains .com, .edu, .gov, .net, .org")
            self.lbl_msg.pack()

    def get_keywords(self):
        global keywords
        
        keyword = self.ent.get()
        self.ent.delete(0,'end')

        if keyword == '':
            self.lbl_msg.config(text = 'Insert nonempty keyword value')
        else:
            self.btn_next.config(state='normal')
            keywords.append(keyword)
            self.lbl_msg.config(text = keyword + ' added to keywords\nAdd another keyword or next to continue')
            self.lbl_msg.pack()
            
    def check_termination_value(self):
        #print("check_termination_value")
        global termination

        value = self.ent.get()
        self.ent.delete(0,'end')
        #print(value)
        if termination[-1] == '1':
            try:
                value = int(value)
                termination.append(value)
                self.done()
            except:
                self.lbl_msg.config(text = "Error: Invalid number of seconds\nEnter the number of seconds you want the program to run for ")
                self.lbl_msg.pack()
        elif termination[-1] == '2':
            try:
                value = int(value)
                termination.append(value)
                self.done()
            except:
                self.lbl_msg.config(text = "Error: Invalid number of pages\nEnter the number of seconds you want the program to run for ")
                self.lbl_msg.pack()
        elif termination[-1] == '4':
            try:
                value = int(value)
                termination.append(value)
                self.done()
            except:
                self.lbl_msg.config(text = "Error: Invalid number of jobs\nEnter the number of seconds you want the program to run for ")
                self.lbl_msg.pack()
        
        
    def get_termination_value(self):
        #print("get_termination_value")
        global termination
        self.btn_enter.config(command=self.check_termination_value)
        self.btn_enter.pack()
        if termination[-1] == '1':
            self.lbl_msg.config(text = "Enter the number of seconds you want the program to run for ")
            self.lbl_msg.pack()
        elif termination[-1] == '2':
            self.lbl_msg.config(text = "Enter the number of pages you want the program to run for ")
            self.lbl_msg.pack()
        elif termination[-1] == '4':
            self.lbl_msg.config(text = "Enter the number of jobs you want the program to run for ")
            self.lbl_msg.pack()
        
    def get_termination(self):
        #print("get_termination")
        global termination
        choice = self.ent.get()
        self.ent.delete(0,'end')
        #print(choice)
        if choice == '1' or choice == '2' or choice == '4':
            # time limit or number of pages or number of jobs
            termination.append(choice)
            self.get_termination_value()
        elif choice == '3':
            # until list is out of pages
            termination = ['3',seeds]
            self.done()
        else:
            #print("Error: Insert valid termination condition")
            self.lbl_msg.config(text = 'Error: Insert valid termination condition\nEnter the number cooresponding to your termination choice:\n1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs')
            self.lbl_msg.pack()
        
    def keywords(self):
        #print('in keywords')
        self.btn_next.config(text='next',command=self.termination,state=DISABLED)
        self.btn_next.pack()
        self.lbl_msg.config(text = 'Insert keyword(s) to search for')# = Label(self, text = url + ' added')
        self.lbl_msg.pack()
        self.btn_enter.config(text='enter',command=self.get_keywords)
        self.btn_enter.pack()


    def termination(self):
        #print('in termination')
        self.btn_next.pack_forget()
        self.lbl_msg.config(text = 'Enter the number cooresponding to your termination choice:\n1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs')
        self.lbl_msg.pack()
        
        self.btn_enter.config(text='enter',command=self.get_termination)
        self.btn_enter.pack()

    def done(self):
        #print("start web scraping")
        self.lbl_msg.pack()
        self.btn_enter.config(state=DISABLED)
        self.btn_enter.pack()
        
        self.destroy()

        self.lbl_msg1 = Label(text = 'Seeds, keywords and termination accepted\nClose this window to run program')
        self.lbl_msg1.pack()
        self.destroy()

        
        
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
root.geometry("500x200")
app = Window(root)

root.mainloop()
print(seeds)
print(keywords)
print(termination)
