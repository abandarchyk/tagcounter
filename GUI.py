from tkinter import *
from tkinter.ttk import Combobox


def go_click():
    entered_text = enter_site.get()
    if len(entered_text) is 0:
        url_error_label['text'] = 'Err!'
    parsing_info_text.insert(INSERT, chars=entered_text)


window = Tk()
window.title('TagCounter by Aliaksandr_Bandarchyk@epam.com')


Label(window, text='Available\nSites').grid(row=0, column=0)


listbox = Combobox(window, values=['A', 'B', 'C'], state='readonly')

listbox.grid(row=0, column=1, sticky=W)

select_btn = Button(window, text='Select', width=10)
select_btn.grid(row=0, column=2)

Label(window, text='Enter site url').grid(row=1, column=0)
enter_site = Entry(window, width=20)
enter_site.grid(row=1, column=1, sticky=W)

go_btn = Button(window, text='Go', command=go_click, width=10)
go_btn.grid(row=1, column=2)

url_error_label = Label(window, text='WTF?!')
url_error_label.grid(row=2, column=1)

parsing_info_text = Text(window, width=35, height=20, wrap=WORD)
parsing_info_text.grid(row=3, column=0, columnspan=3, pady=100)

window.mainloop()
