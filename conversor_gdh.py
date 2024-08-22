import tkinter as tk
from tkinter import filedialog as fd     # from tkinter import Tk and filedialogfor Python 3.x
import pandas as pd
from bs4 import BeautifulSoup
from ics import Calendar, Event #Ics.py is a pythonic iCalendar library
from ics.grammar.parse import ContentLine
from tkcalendar import DateEntry 
import arrow

my_w = tk.Tk()
my_w.geometry("300x300")  
my_w.title("Conversor Grades de Horarios UFSC")

l0=tk.Label(my_w, text='Selecione as datas de inicio e fim das aulas')
l0.grid(row=1,column=1,columnspan=4,padx=20,pady=20)
 
cal_1=DateEntry(my_w,selectmode='day')
cal_1.grid(row=2,column=1,columnspan=2, rowspan=3,padx=20)

cal_2=DateEntry(my_w,selectmode='day')
cal_2.grid(row=2,column=3,columnspan=2, rowspan=3,padx=20)

l1=tk.Label(my_w,text='inicio')  # Label to display date 
l1.grid(row=5,column=1,columnspan=2, rowspan=1)

l2=tk.Label(my_w,text='fim')  # Label to display date 
l2.grid(row=5,column=3,columnspan=2, rowspan=1)

def open_file():
    global filename
    filename = fd.askopenfilename(filetypes=(("HTML Files",("*.htm", "*.html")),))
    l3.config(text=filename,bg='green')

def close():
    global begin, end
    begin = arrow.get(cal_1.get_date()).replace(tzinfo='-03:00')
    end = arrow.get(cal_2.get_date()).replace(tzinfo='-03:00')
    my_w.destroy()

b3=tk.Button(my_w,text='Selecione arquivo HTML da grade de horarios', command=lambda:open_file())
b3.grid(row=6,column=1, columnspan=4, padx=20, pady=30)

l3=tk.Label(my_w,text='Selecione um arquivo',bg='yellow',wraplength=250,justify='center')
l3.grid(row=7,column=1,columnspan=5)

b4=tk.Button(my_w,text='Gerar ICS', command=close)
b4.grid(row=8,column=1, columnspan=4, padx=20, pady=30)

my_w.mainloop()

c=Calendar()

# Read the HTML file into a Pandas dataframe
with open(filename) as file:
    soup = BeautifulSoup(file, 'html.parser')
tables = pd.read_html(str(soup))

Timetable = tables[1] #select second table in the file
Timetable = Timetable.set_index('Unnamed: 0')
print(Timetable)

Subjects =  tables[2]
Subjects = Subjects.rename(columns=Subjects.iloc[0])
Subjects = Subjects.drop([0])
Subjects = Subjects.set_index(Subjects.columns[0])
print(Subjects)

for i in range(Timetable.shape[1]):
    j = 0
    while j in range(Timetable.shape[0]):
        if pd.notna(Timetable.index[j]) and pd.notna(Timetable.iloc[j,i]):
            print('Event!')
            e = Event()
            e.name = str(Subjects['NOME DA DISCIPLINA'].get(str(Timetable.iloc[j,i])[:7]))+' - '+str(Timetable.iloc[j,i])[:7]
            time = arrow.get(str(Timetable.index[j])[:5],'HH:mm').shift(minutes=20).time() #create an arrow object for the start time
            e.begin = begin.replace(hour=time.hour, minute=time.minute).shift(days=i)
            for k in range (12):
                if Timetable.iloc[j+k,i] != Timetable.iloc[j,i]: 
                    time = arrow.get(str(Timetable.index[j+k-1]),'HH:mm').shift(minutes=70).time()
                    e.end = begin.replace(hour=time.hour, minute=time.minute).shift(days=i)
                    e.location = str(Timetable.iloc[j,i])[-8:]
                    e.description = 'Turma: ' + str(Subjects['TURMA'].get(str(Timetable.iloc[j,i])[:7]))+' | Professor: ' + str(Subjects['PROFESSOR'].get(str(Timetable.iloc[j,i])[:7]))
                    e.extra.append(ContentLine('RRULE', {}, f"FREQ=WEEKLY;UNTIL={str(end.format('YYYYMMDD[T]HHmm[00]'))}"))
                    j = j + k - 1
                    break
            print(e.serialize())
            c.events.add(e)
        j = j + 1    
    
with fd.asksaveasfile(initialfile = 'AulasUFSC.ics', defaultextension=".ics",filetypes=[("Calendar","*.ics"),("All Files","*.*")]) as f:
    f.writelines(c.serialize())

print('\n\n\nSuccess!\n\n\n')