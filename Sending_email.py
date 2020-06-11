import os
import smtplib
# import model
import random
from credentials import host, port
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = os.getenv("App_Address")
passwrd = os.getenv("App_Password")
to_email = os.getenv("App_email_to")


quote_file = open('model.txt','r')
line_list = quote_file.read().split('\n') #read the file however you'd like to read it.
quote_file.close()

class Quote_email():

    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

    def email_message(self):
        s = '"%s" -%s' %(self.message,self.author)
        quotelist = []
        for line in linelist:
            split = line.split()
            quote = Quote_email(split[0],split[1]) 
        quote_list.append(quote)
        quote_choice = random.choice(quote_list)
        # print (quotechoice)

    def get_contacts(self, file_name,names , emails):
        self.file_name = filename
        self.names = []
        self.emails = []
        with open(filename, mode='mode', encoding='encoding') as my_contacts_file:
            for contact in my_contacts_file:
                self.names.append(contact.split()[0])
                self.emails.append(contact.split()[1])
        return self.names, self.emails

    def read_template(self):
        with open(filename, 'mode', encoding='encoding') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def main(self):
        self.names, self.emails = get_contacts('my_contacts.txt') # read contacts
        message_template = read_template('model.txt')
        try:
            server = smtplib.SMTP(host='host', port=port)
            server.ehlo()
            server.starttls()
            sever.login(user,passwrd)
            msg = f'Subject:{author}\n\n{msg}'
            server.sendmail(user,passwrd)
            return 'successful:email sent'
        except:
            return 'email failed'
        finally:
            server.quit()
     
        msg['From']=user
        msg['To']=to_email
        msg['Subject']="Review project"

# email_sent = Quote_email(quote,author)
# print(email_sent.main())         
     

  
     



