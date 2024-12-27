from tkinter import filedialog
from docx import Document
from docx.shared import Pt
import customtkinter as ctk
from PyPDF2 import PdfReader
import tkinter.messagebox as popup
import json

# Default language
current_language = 'bg'

# Opens language json. If it doesn't exist, it sets the default language to English
try:
    with open('language.json', 'r', encoding='utf-8') as file:
        translations = json.load(file)
except FileNotFoundError:
    popup.showerror("Error", "Translations file not found. The language is set to English.")
    translations = {"en": {
        "title": "PDF Converter",
        "no_pdf_selected": "No PDF file selected",
        "select_pdf": "Select PDF Document",
        "show_text": "Show Text",
        "clear_text": "Clear Text",
        "save_as": "Save As",
        "warning": "Warning!",
        "no_text_to_convert": "No text to convert"
    }}
    current_language = 'en'

# Sets default appearance as dark and default theme to dark blue
mode = 'dark'
ctk.set_appearance_mode(mode)
ctk.set_default_color_theme('dark-blue')

# Creates the main window
root = ctk.CTk()
root.title('PDF converter')
root.geometry('800x640')

pdf_file = None


# Updates the UI language when the app is started or when the language is changed by the user
def update_language(lang):
    global current_language
    current_language = lang

    root.title(translations[lang]["title"])
    browse_pdf_label.configure(text=translations[lang]["no_pdf_selected"])
    browse_button.configure(text=translations[lang]["select_pdf"])
    show_text_button.configure(text=translations[lang]["show_text"])
    clear_button.configure(text=translations[lang]["clear_text"])
    save_button.configure(text=translations[lang]["save_as"])

    # Changes the color of the language buttons after the language is changed
    if current_language == 'en':
        english_button.configure(fg_color='#1f538d')
        bulgarian_button.configure(fg_color='#212121')
    elif current_language == 'bg':
        english_button.configure(fg_color='#212121')
        bulgarian_button.configure(fg_color='#1f538d')


def switch_language(lang):
    update_language(lang)


# Opens a file dialog to select a PDF file
def browse_for_pdf():
    global pdf_file

    filename = ctk.filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    pdf_file = filename

    if not filename:
        browse_pdf_label.configure(text='Не е избран PDF файл')
        show_text_button.configure(state='disabled')
        save_button.configure(state='disabled')
    else:
        browse_pdf_label.configure(text=filename.split('/')[-1])

        show_text_button.configure(state='normal')
        save_button.configure(state='normal')


# Reads the PDF file and displays the text in the text area
def show_text():
    read_pdf(pdf_file)
    text_area.insert('1.0', read_pdf(pdf_file))


# Clears the text in the text area
def clear_text():
    text_area.delete('1.0', 'end')


# Converts the text in the text area to a Word document and sets default font and size
def convert_pdf_to_docx():
    extracted_text = text_area.get('1.0', 'end')
    if extracted_text.strip() == '':
        popup.showinfo(translations[current_language]["warning"], translations[current_language]["no_text_to_convert"])
    else:
        document = Document()
        paragraph = document.add_paragraph(extracted_text)

        for run in paragraph.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)

        filepath = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
        document.save(filepath)


# Reads the PDF file and returns the text
def read_pdf(pdf_file_path):
    reader = PdfReader(pdf_file_path)
    number_of_pages = len(reader.pages)
    pages = reader.pages[0:number_of_pages]

    text = ''
    for pages in pages:
        text += pages.extract_text()

    return text


#######################################################################################################################
# UI                                                                                                                  #
#######################################################################################################################
top_frame = ctk.CTkFrame(root)
top_frame.pack(side='top', pady=20)
english_button = ctk.CTkButton(top_frame,
                               width=35,
                               height=25,
                               text="En",
                               fg_color='#212121',
                               command=lambda: switch_language("en"))
english_button.pack(side='right', anchor='ne', padx=5)

bulgarian_button = ctk.CTkButton(top_frame,
                                 width=35,
                                 height=25,
                                 text="Bg",
                                 fg_color='#212121',
                                 command=lambda: switch_language("bg"))
bulgarian_button.pack(side='right', anchor='ne')

language_icon = ctk.CTkLabel(top_frame, text='🌐', font=('Arial', 18))
language_icon.pack(side='right', anchor='ne', padx=(50, 5))

browse_pdf_label = ctk.CTkLabel(top_frame, text='Не е избран PDF файл')
browse_pdf_label.pack(side='left', padx=15, pady=20)

browse_button = ctk.CTkButton(top_frame, text='Избери PDF документ', command=browse_for_pdf)
browse_button.pack(side='left', padx=15, pady=20)

show_text_button = ctk.CTkButton(top_frame, text='Покажи текст', state='disabled', command=show_text)
show_text_button.pack(side='left', padx=15, pady=20)

text_area = ctk.CTkTextbox(root)
text_area.pack(pady=10, padx=40, expand=True, fill='both')

bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side='bottom', pady=10)

clear_button = ctk.CTkButton(bottom_frame, text='Изчисти текста', command=clear_text)
clear_button.pack(side='left', padx=15, pady=20)

save_button = ctk.CTkButton(bottom_frame, text='Запази като', state='disabled', command=convert_pdf_to_docx)
save_button.pack(side='left', padx=15, pady=20)
#######################################################################################################################

# Updates the UI language on the start of the app
update_language(current_language)

root.mainloop()
