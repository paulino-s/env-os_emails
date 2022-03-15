from dotenv import load_dotenv

from src.email import Email

html_format='''  
                   
                   
                 Envio de mail formateado en HTML  
                   
                   
                     h2 {font-size:14px;margin: 2px;}  
                     h3 {font-size:12px;margin: 2px;}  
                     p {font-size:10px; margin: 2px;}  
                     td {border: 1px outset}  
                   
                   
                 ''' 

def main():
    name = input('What is your name? ')
    email = Email()
    email.send_email([''], 'Probando env[ios de emails', message_format=html_format.format(name), format='html')

if __name__ == '__name__':
    load_dotenv()
    main()