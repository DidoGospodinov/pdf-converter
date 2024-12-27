# pdf_converter
PDF Converter
A GUI application built with Python for converting PDF documents to Word (.docx) files. The application supports multi-language functionality (English and Bulgarian) and provides a user-friendly interface using the CustomTkinter library.
____________________________________________________________________________________________
Features

•	PDF to Word Conversion: Extracts text from PDF files and saves it as a Word document.

•	Multi-Language Support: Choose between English and Bulgarian for the application interface.

•	Text Display: View the extracted text in a text area before saving.

•	Dark Mode UI: Modern dark-themed interface powered by CustomTkinter.

•	File Selection: Easily browse and select PDF files through a file dialog.

____________________________________________________________________________________________
Prerequisites

• Ensure the required Python packages are listed in the requirements.txt file and can be installed with:

-     pip install -r requirements.txt
____________________________________________________________________________________________
Installation
1.	Clone the repository or download the source code:
   -     git clone https://github.com/DidoGospodinov/pdf-converter.git
2.	Navigate to the project directory.  
3.	Run the application script:
-     python main.py
____________________________________________________________________________________________
Usage
1.	Start the Application:
   
       • Launch the script.
   
2.	Select a Language:
   
       • Use the language buttons ("En" for English, "Bg" for Bulgarian) at the top right corner to set your preferred language.
   
3.	Select a PDF:
   
       • Click the "Select PDF Document" button to choose a PDF file.
   
4.	Display Text:
   
       • Click the "Show Text" button to view the text extracted from the PDF.
   
5.	Clear Text:
   
       • Use the "Clear Text" button to clear the text area.
   
6.	Save as Word:
    
       • Click the "Save As" button to convert the displayed text to a Word document.
____________________________________________________________________________________________
File Structure

•	main.py: Main application script.

•	language.json: Contains translations for supported languages.

•	requirements.txt: Lists all the necessary dependencies for the project.

____________________________________________________________________________________________
Translations

The application uses a language.json file to manage translations. The application will use it to load the translations for supported languages. You can modify this file to add more languages or customize translations.
