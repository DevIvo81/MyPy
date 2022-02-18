import random, string, os, tkinter as tk
from database import PasswordStore, create_db

from database.db_repo import create_and_update_password_entry, get_passwords

os.system('cls' if os.name == 'nt' else 'clear')


# VARIJABLE ZA IZBOR
SLOVA = string.ascii_letters
BROJEVI = string.digits
SIMBOLI = string.punctuation
SVI_LISTA = list(SLOVA + BROJEVI + SIMBOLI)


print(SVI_LISTA)
print(SVI_LISTA.index('0'))
print(SVI_LISTA.index('!'))

LARGE_FONT = ('Verdana', 16)

#region GLAVNI CONTAINER - nasljeđuje master tk sučelje i 
# pohranjuje se unutar njega

root = tk.Tk()  # ...pohrana unutar sučelja
root.title('IZ_Py - Algebra Python Developer | Password Generator')
# root.geometry('600x400') # ...okvir pohrane

#endregion

#region FRAME SETTINGS

# FRAME CONTAINER "POSTAVKE" - NASLJEĐUJE glavni container ""root"" 
# kao master i pohranjuje se unutar njega.

frm_settings = tk.Frame(root)
frm_settings.grid(row=0, column=0, rowspan=3, columnspan=3) 
#endregion


#region LabelFrame - OKVIR ZA WIDGETE nasljeđuje frm_settings !!!
frm_lbl_settings = tk.LabelFrame(frm_settings, 
                                text='Postavke',
                                font=LARGE_FONT)

    # ...konfiguracija kolona
frm_lbl_settings.columnconfigure((0, 1, 2), weight=1, minsize=150)

    # u prozoru dolazi preko framea pa je pozicija ista...
    # ...stavljamo padding da se label izdvoji.
frm_lbl_settings.grid(row=0, column=0, rowspan=3, columnspan=3,
                    padx=5, pady=5, ipadx=5, ipady=5)

#endregion

#region WIDGETS - nasljeđuju frm_lbl_settings

# CheckButton SLOVA - default je False!
    #...postavljanje varijable za vraćanje vrijednosti checkBox
cb_letters_var = tk.BooleanVar() #...predefinirana vrijednost u "tk"
    #...checkBox stavljamo unutar label okvira
cb_letters = tk.Checkbutton(frm_lbl_settings, text='SLOVA',
                            variable=cb_letters_var)
cb_letters.grid(row=0, column=0, pady=10)

# CheckButton BROJEVI - default je False!
    #...postavljanje varijable za vraćanje vrijednosti checkBox
cb_numbers_var = tk.BooleanVar() #...predefinirana vrijednost u "tk"
    #...checkBox stavljamo unutar label okvira
cb_numbers = tk.Checkbutton(frm_lbl_settings, text='BROJEVI',
                            variable=cb_numbers_var)
cb_numbers.grid(row=0, column=1, pady=10)

# CheckButton ZNAKOVI - default je False!
    #...postavljanje varijable za vraćanje vrijednosti checkBox
cb_symbols_var = tk.BooleanVar() #...predefinirana vrijednost u "tk"
    #...checkBox stavljamo unutar label okvira
cb_symbols = tk.Checkbutton(frm_lbl_settings, text='ZNAKOVI',
                            variable=cb_symbols_var)
cb_symbols.grid(row=0, column=2, pady=10)

#endregion


#region FRAME ACTIONS

# KLIZAČ - prima Integer pa je varijabla IntVar()

def set_pwd_length(value):
    scl_pwd_length_var.set(int(value))

    #...postavljanje varijable za vraćanje vrijednosti Scale
scl_pwd_length_var = tk.IntVar() #...predefinirana vrijednost u "tk"
scl_pwd_length_var.set(10)
    #...Scale stavljamo unutar label okvira
scl_pwd_length = tk.Scale(frm_lbl_settings,
                            orient='horizontal',
                            variable=scl_pwd_length_var,
                            from_=8,
                            
                            to=40,
                            length=300,
                            command=set_pwd_length)
scl_pwd_length.grid(row=1, column=0, columnspan=3, pady=10)

# RADIO BUTTONS show / hide PASSWORD
def set_pwd_visibility(): # postavljamo vrijednost varijable
    
    if rb_show_password_var.get() == 'show_pwd':
        ent_pwd.config(show='')
        pass
    else:
        ent_pwd.config(show='*')

# ako je uključeno Show Password
rb_show_password_var = tk.StringVar() 
rb_show_password_var.set('show_pwd') # default vrijednost
rb_show_password = tk.Radiobutton(frm_lbl_settings,
                                text='Otkrij lozinku',
                                variable=rb_show_password_var,
                                command=set_pwd_visibility,
                                value='show_pwd')
rb_show_password.grid(row=2, column=0, pady=10)

# ako je uključeno Hide Password
# hide uzima istu varijablu i poziva istu funkciju kao i show
rb_hide_password = tk.Radiobutton(frm_lbl_settings,
                                text='Sakrij lozinku',
                                variable=rb_show_password_var,
                                command=set_pwd_visibility,
                                value='hide_pwd') # izmijenjena vrijednost
rb_hide_password.grid(row=2, column=2, pady=10)

#endregion


#region FRAME CONTAINER BUTTONS - pripada u "root"

frm_buttons = tk.Frame(root)
frm_buttons.grid(row=3, column=0, columnspan=3,
                padx=5, pady=15, ipadx=5, ipady=5)

# BUTTON GENERATE - pripada u "frm_buttons"

def generate_pwd():
    # TODO kombinacija za SLOVA BROJEVE i ZNAKOVE
    
    password = ''
    password_length = scl_pwd_length_var.get() #....dohvaćamo vrijednost preko klizača
    for _ in range(password_length):
        if cb_letters_var.get():
            znak = random.choice(SVI_LISTA[ : 52])
        elif cb_numbers_var.get():
            znak = random.choice(SVI_LISTA[52 : 62])
        elif cb_symbols_var.get():
            znak = random.choice(SVI_LISTA[62 : ])
        else:
            znak = random.choice(SVI_LISTA)
        password += znak
    
    
    ent_pwd_var.set(str(password))
    
    


btn_generate_pwd = tk.Button(frm_buttons,
                            text='GENERATE',
                            bg = '#5cb85c',
                            command=generate_pwd)
btn_generate_pwd.grid(row=3, column=0, padx=20, pady=5, ipadx=5, ipady=5)


# BUTTON RESET - pripada u "frm_buttons"

def reset_pwd():
    ent_pwd_var.set('Generirana lozinka')
    

btn_reset_pwd = tk.Button(frm_buttons,
                            text='RESET',
                            bg = '#d9534f',
                            command=reset_pwd)
btn_reset_pwd.grid(row=3, column=1, padx=20, pady=5, ipadx=5, ipady=5)


# BUTTON GENERATE - pripada u "frm_buttons"

def copy_and_save_pwd():
    # koristimo clipboard metode, prvo čišćenje
    root.clipboard_clear()
    #...potom dodavanje u clipboard
    root.clipboard_append(ent_pwd_var.get())
    
    gen_pwd_entry = PasswordStore(
        password = ent_pwd_var.get(),
        user_name = 'ime.prezime@email.address',
        url = 'https://www.domain.tld/login'
    )
    
    create_and_update_password_entry(gen_pwd_entry)

def init_pwd_from_db():
    passwords = get_passwords()
    init_password = passwords[0].password
    
    ent_pwd_var.set(str(init_password))
    
btn_copy_pwd = tk.Button(frm_buttons,
                            text='COPY',
                            bg = '#f0ad4e',
                            command=copy_and_save_pwd)
btn_copy_pwd.grid(row=3, column=2, padx=20, pady=5, ipadx=5, ipady=5)


#endregion


#region FRAME CONTAINER "DISPLAY PASSWORD" - pripada u "root"

frm_display_pwd = tk.Frame(root)
frm_display_pwd.grid(row=4, column=0, columnspan=3, 
                    padx=20, pady=5, ipadx=5, ipady=5)

#...labela za ispis lozinke - nasljeđuje frm_display_pwd
lbl_pwd = tk.Label(frm_display_pwd,
                    font=LARGE_FONT,
                    text='Generirana lozinka')
lbl_pwd.grid(row=4, column=0, columnspan=3,
            padx=20, pady=5, ipadx=5, ipady=5)


ent_pwd_var = tk.StringVar()
init_pwd_from_db()
ent_pwd = tk.Entry(frm_display_pwd,
                    textvariable=ent_pwd_var,
                    font=LARGE_FONT,
                    justify='center',
                    width=30,
                    state='readonly',
                    bg='systembuttonface',
                    bd=0)
ent_pwd.grid(row=5, column=0, columnspan=3,
                padx=5, pady=25, ipadx=5, ipady=5)

#endregion


create_db()

root.mainloop()





