from tkinter import *
from tkinter.ttk import Combobox
import tagcounter_config
import results_processor


class MainForm:
    def __init__(self, master):
        self.master = master
        master.title('TagCounter by Aliaksandr_Bandarchyk')

        Label(master, text='Select URL').grid(row=0, column=0)

        predefined_sites = Combobox(master, values=['http://yandex.by', 'b', 'c'])
        predefined_sites.grid(row=0, column=1, sticky=W)

        Label(master, text='Or').grid(row=1, column=0)

        Label(master, text='Enter URL manually').grid(row=2, column=0)

        enter_site = Entry(master, width=20)
        enter_site.grid(row=2, column=1)

        def on_parse_click():
            selected_host = predefined_sites.get()
            print('Selected host: ' + selected_host)
            # OR
            entered_text = enter_site.get()
            print(entered_text)
            # assert

            page = results_processor.process(selected_host)

            #show method with format
            parsing_info_text.insert(INSERT, chars=page.tags_dict)

        go_btn = Button(master, text='Parse', command=on_parse_click, width=10)
        go_btn.grid(row=2, column=2)

        # Previous results block
        results_history_label = Label(master, text='Results history')
        results_history_label.grid(row=3, column=0)

        listbox = Combobox(master, values=['filename_1', 'filename_2', 'filename_3'])
        listbox.grid(row=3, column=1, sticky=W)

        go_btn = Button(master, text='Load', width=10)
        go_btn.grid(row=3, column=2)

        log_label = Label(master, text='LOG:')
        log_label.grid(row=4, column=0, columnspan=1, sticky=S)

        parsing_info_text = Text(master, width=35, height=20, wrap=WORD)
        parsing_info_text.grid(row=5, column=0, columnspan=3, pady=10)


def run():
    print('Loading GUI')
    window = Tk()
    window.geometry('1000x1000')
    MainForm(window)
    window.mainloop()


if __name__ == '__main__':
    run()
