from tkinter import *

import random,operator

#List of PLayers

class Application(Frame):

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.FORWARDS={"Sagar":10,"Ashwin":10,"Jollu":6,"Siddesh":8,"SUdeep":9,"Modi":6,"Jibril":10}
        self.MID={"Aayush":9,"Sachin":10,"Supreeth":10,"Jathin":9,"Anand":7,"Vatsa":9}
        self.DEFENCE={"Baby":9,"Sajjan":9,"Prem":9,"Uttam":8,"KatHle":7,"Pratham":9,"Shravanth":9,"Zahesh":8}
        self.GK={"Chenga":7,"Bharath":9}
        self.AMBIGUOUS={"Mama":6,"Nithin":6}

        self.FORWARDS_d={"Sagar":10,"Ashwin":10,"Jollu":6,"Siddesh":8,"SUdeep":9,"Modi":6,"Jibril":10}
        self.MID_d={"Aayush":9,"Sachin":10,"Supreeth":10,"Jathin":9,"Anand":7,"Vatsa":9}
        self.DEFENCE_d={"Baby":9,"Sajjan":9,"Prem":9,"Uttam":8,"KatHle":7,"Pratham":9,"Shravanth":9,"Zahesh":8}
        self.GK_d={"Chenga":7,"Bharath":9}
        self.AMBIGUOUS_d={"Mama":6,"Nithin":6}


        self.FORWARDS_={}
        self.MID_={}
        self.DEFENCE_={}

        self.TEAM_A=[]
        self.TEAM_B=[]


        Label(self,text="WELCOME",font="Impact").grid(row=0,column=1,sticky=N)
        Label(self,text="Select PLayers:").grid(row=3,column=0,sticky=W)

        Label(self,text="FORWARDS").grid(row=4,column=0,sticky=W)
        Label(self,text="DEFENCE").grid(row=4,column=2,sticky=W)
        Label(self,text="MID").grid(row=4,column=1,sticky=W)

        #Display list
        
        i=7
        for player in self.FORWARDS:
            self.FORWARDS_d[player]=BooleanVar()
            Checkbutton(self,text=player,variable=self.FORWARDS_d[player]).grid(row=i,column=0,columnspan=1,sticky=W)
            i=i+1


        i=7    
        for player in self.MID:
            self.MID_d[player]=BooleanVar()
            Checkbutton(self,text=player,variable=self.MID_d[player]).grid(row=i,column=1,columnspan=1,sticky=W)
            i=i+1
        
        i=7    
        for player in self.DEFENCE:
            self.DEFENCE_d[player]=BooleanVar()
            Checkbutton(self,text=player,variable=self.DEFENCE_d[player]).grid(row=i,column=2,columnspan=1,sticky=W)
            i=i+1

        Button(self,text="Submit",command=self.display_team).grid(row=18,column=0,sticky=W)
        Button(self,text="Clear",command=self.clear).grid(row=18,column=1,sticky=W)
        self.results_A=Text(self, height=15,width=20,wrap=WORD)
        self.results_A.grid(row=20,column=0,columnspan=1,sticky=W)
        self.results_B=Text(self,height=16,width=20,wrap=WORD)
        self.results_B.grid(row=20,column=1,columnspan=1,sticky=W)
    
    def clear(self):

        self.results_A.delete(0.0,END)
        self.results_B.delete(0.0,END)
        self.TEAM_A=[]
        self.TEAM_B=[]
        self.FORWARDS_={}
        self.MID_={}
        self.DEFENCE_={}

        for player in self.FORWARDS:
            self.FORWARDS_d[player].set(0)

        for player in self.MID:
            self.MID_d[player].set(0)

        for player in self.DEFENCE:
            self.DEFENCE_d[player].set(0)

    def display_team(self):

        for player in self.FORWARDS:
            if self.FORWARDS_d[player].get():
                self.FORWARDS_[player]=self.FORWARDS[player]

        for player in self.MID:
            if self.MID_d[player].get():
                self.MID_[player]=self.MID[player]

        for player in self.DEFENCE:
            if self.DEFENCE_d[player].get():
                self.DEFENCE_[player]=self.DEFENCE[player]

        self.FORWARDS_=self.sort_position(self.FORWARDS_)
        self.MID_=self.sort_position(self.MID_)
        self.DEFENCE_=self.sort_position(self.DEFENCE_)

        self.split_into(self.FORWARDS_)
        self.split_into(self.MID_)
        self.split_into(self.DEFENCE_)

        for x in self.TEAM_A:
            self.results_A.insert(0.0,x+"\n")

        for x in self.TEAM_B:
            self.results_B.insert(0.0,x+"\n")

    def sort_position(self,position):
        sorted_team=sorted(position,key=position.__getitem__,reverse=True)
        return list(sorted_team)
          
    def split_into(self,position):

        if len(self.TEAM_A)<=len(self.TEAM_B):
            for ele in position:
                if position.index(ele) in (0,3,4,7,8,11):
                    self.TEAM_A.append(ele)
                else:
                    self.TEAM_B.append(ele)           
                
        else:
            for ele in position:
                if position.index(ele) in (0,3,4,7,8,11):
                    self.TEAM_B.append(ele)
                else:
                    self.TEAM_A.append(ele)                    
#main
root=Tk()
root.title("Don't Panic")
root.geometry("640x500")

app=Application(root)
root.mainloop()




