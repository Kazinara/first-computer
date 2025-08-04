from gtts import gTTS
import pdfplumber


def get_txt():
    file_path="text.pdf"
    with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
        pages = ''.join([page.extract_text() for page in pdf_file.pages]).replace('\n',' ')
    return pages
    
    
def get_sound(txt):
    language = 'ru'
    voiced_txt = gTTS(text=txt, lang=language, slow=False)
    voiced_txt.save('voiced_text.mp3')


def main():
    pdf_text = get_txt()
    print(pdf_text)
    get_sound(pdf_text)


if __name__ =='__main__':
    main()




    

