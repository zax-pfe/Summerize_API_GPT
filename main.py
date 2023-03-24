# from textwrapper import TextWrapper


import openai
import os
from time import time,sleep
import textwrap
import re
import process_pdf


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
openai.api_key = open_file('openaiapikey.txt')

# a = open_file('openaiapikey.txt')


def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)




path_pdf = 'Liege_le_journal_de_7h30_152851880.mp3_transcript_fr.pdf'


if __name__ == '__main__':

    text_transcipted = process_pdf.extract_text_from_pdf(path_pdf)

    cleaned_text = process_pdf.clean_text(text_transcipted)

    trunked_text = process_pdf.trunk_text(cleaned_text)
    # for i in trunked_text:
    #     print(i)
    #     print("\n\n")


    # response = openai.Completion.create ( 
    #     model = 'text-davinci-003',
    #     prompt = 'Give me two reason to learn openai api with python',
    #     max_tokens = 500)
    

    # print(response['choices'][0]['text'])

    result = list()
    count = 0
    for trunk in trunked_text:
        prompt = open_file('prompt.txt').replace('<<SUMMARY>>', trunk)
        print(prompt)
        break



    #     prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    #     summary = gpt3_completion(prompt)
    #     print('\n\n\n', count, 'of', len(chunks), ' - ', summary)
    #     result.append(summary)
    # save_file('\n\n'.join(result), 'output_%s.txt' % time())




    
        


