import os
import smtplib
from http import HTTPStatus
import random
from credentials import host, port
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = os.getenv("App_Address")
passwrd = os.getenv("App_Password")
to_email = os.getenv("App_email_to")
quote_file = open('model.txt','r')
line_list = quote_file.read().split('\n')
quote_file.close()

class Random_message():

    def __init__(self,random_message,author):
        self.random_message = random_message
        self.author = author

    def __str__(self): #string method
        s = '"%s" -%s' %(self.random_message,self.author)
        message_list = []
        for line in line_list:
            split_quote = line.split()
            quote = __str__(split_quote[0],split_quote[1]) 
        message_list.append(quote)
        quote_choice = random.choice(message_list)
        return quote_choice

    def extract_contacts(self, filename,names ,emails):
        self.filename = filename
        self.names = []
        self.emails = []
        with open(filename, mode='mode', encoding='utf-8') as my_contacts_file:
            for contact in my_contacts_file:
                self.names.append(contact.split()[0])
                self.emails.append(contact.split()[1])
        return self.names, self.emails

    def read_model_template(self):
        with open(self.filename,'mode', encoding='utf-8') as model_file:
            model_file_content = model_file.read()
        return Template(model_file_content)

    def sending_mail(self, extract_contacts, read_model_template):
        self.names, self.emails = extract_contacts('my_contacts.txt') # read contacts
        message_template = read_model_template('model.txt')
        try:
            server = smtplib.SMTP(host='host', port=port)
            server.ehlo()
            server.starttls()
            sever.login(user,passwrd)
            for self.names, self.emails in zip(self.name, self.email):
                msg = MIMEMultipart()
                random_message = message_template.substitute(SUBJECT_NAME=name.title())
                print(random_message)
                msg = f'Subject:{author}\n\n{msg}'
                msg['From']=user
                msg['To']=to_email
                msg['Subject']="Review project"
                body = f'This is a test message sent to {to_email}'
                msg.attach(MIMEText(random_message, 'plain'))
                server.sendmail(random_message)
                print('successful: <200>')
        except:
                print('email failed: <404>')
        finally:
            server.quit()


if __name__ == "__main__":
    email_sent = Random_message("A verbal contract is not worth the paper it's written on.","Samuel Goldwyn")



      
 
     



  
     



