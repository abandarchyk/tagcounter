from tkinter import *
from tkinter.ttk import Combobox


def go_click():
    entered_text = enter_site.get()
    parsing_info_text.insert(INSERT, chars=entered_text)


window = Tk()
window.title('TagCounter by Aliaksandr_Bandarchyk')


Label(window, text='Available\nSites').grid(row=0, column=0)


predefined_sites = Combobox(window, values=['A', 'B', 'C'], state='readonly')
predefined_sites.grid(row=0, column=1, sticky=W)

select_btn = Button(window, text='Select', width=10)
select_btn.grid(row=0, column=2)

Label(window, text='Enter site url').grid(row=1, column=0)
enter_site = Entry(window, width=20)
enter_site.grid(row=1, column=1, sticky=W)

go_btn = Button(window, text='Parse', command=go_click, width=10)
go_btn.grid(row=1, column=2)

# Previous results block
results_history_label = Label(window, text='Results history')
results_history_label.grid(row=2, column=0)

listbox = Combobox(window, values=['filename_1', 'filename_2', 'filename_3'])
listbox.grid(row=2, column=1, sticky=W)

go_btn = Button(window, text='Load', width=10)
go_btn.grid(row=2, column=2)


log_label = Label(window, text='LOG:')
log_label.grid(row=4, column=0, columnspan=1, sticky=S)

parsing_info_text = Text(window, width=35, height=20, wrap=WORD)
parsing_info_text.grid(row=5, column=0, columnspan=3, pady=10)

window.mainloop()
