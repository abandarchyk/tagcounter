from tkinter import *
from tkinter.ttk import Combobox
import config
import results_processor


def on_parse_click():
    selected_host = predefined_sites.get()
    print('Selected host:' + selected_host)
    # OR
    entered_text = enter_site.get()
    print(entered_text)
    # assert
    page = results_processor.process(config.get_site(selected_host))
    parsing_info_text.insert(INSERT, chars=page.tags_dict)


window = Tk()
window.title('TagCounter by Aliaksandr_Bandarchyk')


Label(window, text='Check from available sites').grid(row=0, column=0)


predefined_sites = Combobox(window, values=config.get_hosts(), state='readonly')
predefined_sites.grid(row=0, column=1, sticky=W)

Label(window, text='Or').grid(row=1, column=0)

Label(window, text='Enter url manually').grid(row=2, column=0)

enter_site = Entry(window, width=20)
enter_site.grid(row=2, column=1)

go_btn = Button(window, text='Parse', command=on_parse_click, width=10)
go_btn.grid(row=2, column=2)

# Previous results block
results_history_label = Label(window, text='Results history')
results_history_label.grid(row=3, column=0)

listbox = Combobox(window, values=['filename_1', 'filename_2', 'filename_3'])
listbox.grid(row=3, column=1, sticky=W)

go_btn = Button(window, text='Load', width=10)
go_btn.grid(row=3, column=2)


log_label = Label(window, text='LOG:')
log_label.grid(row=4, column=0, columnspan=1, sticky=S)

parsing_info_text = Text(window, width=35, height=20, wrap=WORD)
parsing_info_text.grid(row=5, column=0, columnspan=3, pady=10)

window.mainloop()



