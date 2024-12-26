from tkinter import filedialog
from docx import Document
from docx.shared import Pt
import customtkinter as ctk
from PyPDF2 import PdfReader
import tkinter.messagebox as popup

mode = 'dark'
ctk.set_appearance_mode(mode)
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.title('PDF converter')
root.geometry('800x640')

pdf_file = None


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


def show_text():
    read_pdf(pdf_file)
    text_area.insert('1.0', read_pdf(pdf_file))


def clear_text():
    text_area.delete('1.0', 'end')


def convert_pdf_to_docx():
    extracted_text = text_area.get('1.0', 'end')
    if extracted_text.strip() == '':
        popup.showinfo('Внимание!', 'Липсва текст за конвертиране')
    else:
        document = Document()
        paragraph = document.add_paragraph(extracted_text)

        for run in paragraph.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)

        filepath = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
        document.save(filepath)


def read_pdf(pdf_file_path):
    reader = PdfReader(pdf_file_path)
    page = reader.pages[0]
    text = page.extract_text()

    return text


top_frame = ctk.CTkFrame(root)
top_frame.pack(side='top', pady=20)

browse_pdf_label = ctk.CTkLabel(top_frame, text='Не е избран PDF файл')
browse_pdf_label.pack(side='left', padx=15, pady=20)

browse_button = ctk.CTkButton(top_frame, text='Избери PDF документ', command=browse_for_pdf)
browse_button.pack(side='left', padx=15, pady=20)

show_text_button = ctk.CTkButton(top_frame, text='Покажи текст', state='disabled', command=show_text)
show_text_button.pack(side='left', padx=15, pady=20)

text_area = ctk.CTkTextbox(root, width=750, height=400)
text_area.pack(pady=10)

bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(side='bottom', pady=10)

clear_button = ctk.CTkButton(bottom_frame, text='Изчисти текста', command=clear_text)
clear_button.pack(side='left', padx=15, pady=20)

save_button = ctk.CTkButton(bottom_frame, text='Запази като', state='disabled', command=convert_pdf_to_docx)
save_button.pack(side='left', padx=15, pady=20)

root.mainloop()
