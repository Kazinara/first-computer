from gtts import gTTS
import pdfplumber
file_path="text.pdf"
with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
    pages = ''.join([page.extract_text() for page in pdf_file.pages]).replace('\n',' ')
    def get_txt():
        pdf_file_ = pages    
        return pdf_file_
    
    text_one = get_txt()
    print(text_one)


    def get_sound(txt):
        language = 'ru'
        voiced_txt = gTTS(text=txt, lang=language, slow=False)
        voiced_txt.save('voiced_text.mp3')


def main():
    get_txt()
    get_sound(text_one)


if __name__ =='__main__':
    main()




    

