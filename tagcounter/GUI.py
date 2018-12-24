from tkinter import *
from tkinter import simpledialog
from tkinter.ttk import Combobox
from tagcounter import tagcounter_config as conf
from tagcounter import results_processor
from tagcounter import db_module


class MainForm:

    def __init__(self, master):
        self.site_data = None
        self.master = master
        master.title('TagCounter by Aliaksandr_Bandarchyk')

        Label(master, text='Select URL').grid(row=0, column=0)

        predefined_sites = Combobox(master, values=conf.get_sites_urls())
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

            site_data = results_processor.process_url(selected_host)
            self.site_data = site_data

            parsing_info_text.insert(INSERT, chars=site_data)

        def on_load_click():
            url = show_result_entry.get()
            page_data = results_processor.show_results(url)

            parsing_info_text.insert(INSERT, chars=page_data)

        def on_save_click():
            site_name = simpledialog.askstring("Site name", "Please enter site name", parent=master)
            site_data = self.site_data
            db_module.save_results(site_name, site_data.base_url, site_data.datetime_stamp, site_data.tags_dict)

        go_btn = Button(master, text='Parse', command=on_parse_click, width=10)
        go_btn.grid(row=2, column=2)

        show_result_label = Label(master, text='Show results for url')
        show_result_label.grid(row=3, column=0)

        show_result_entry = Entry(master, width=20)
        show_result_entry.grid(row=3, column=1)

        load_btn = Button(master, text='Load', command=on_load_click, width=10)
        load_btn.grid(row=3, column=2)

        log_label = Label(master, text='Tags dictionary:')
        log_label.grid(row=4, column=0, columnspan=1, sticky=S)

        parsing_info_text = Text(master, width=35, height=20, wrap=WORD)
        parsing_info_text.grid(row=5, column=0, columnspan=3, pady=10)

        save_btn = Button(master, text='Save', command=on_save_click, width=10)
        save_btn.grid(row=6, column=1)





def run():
    print('Loading GUI')
    window = Tk()
    window.geometry('700x700')
    MainForm(window)
    window.mainloop()


if __name__ == '__main__':
    run()
