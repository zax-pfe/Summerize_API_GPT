import PyPDF2


def extract_text_from_pdf(pdf_file : str):
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict = False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text
    
def trunk_text(text, page_nb = 3):
    temp_text = ''
    page_count = 1
    trunked_file = []

    # create trunk of n page per n pages 
    for i,page  in enumerate(text):
        temp_text = temp_text + page
        
        if page_count == page_nb:
            trunked_file.append(temp_text)
            page_count = 0
            temp_text=''

        page_count = page_count+1

    if temp_text:
            trunked_file.append(temp_text)
    return trunked_file

def clean_text(text_transcipted):
    text_without_timestamp_all = []

    
    for text in text_transcipted:
        text = text.replace('\t', ' ')
        text_list = text.split('\n')
        text_without_timestamp_list = []

        for line in text_list:
            if '00:' not in line:
                line = line+'\n'
                text_without_timestamp_list.append(line)

        text_without_timestamp = ''.join([str(element) for element in text_without_timestamp_list])
        text_without_timestamp_all.append(text_without_timestamp)

    return text_without_timestamp_all
