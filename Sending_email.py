import os
import smtplib
# import model
import random
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = os.getenv("App_Address")
passwrd = os.getenv("App_Password")
to_email = os.getenv("App_email_to")


quote_file = open('model.txt','r')
line_list = quote_file.read().split('\n') 
quote_file.close()

class Quote_email():

    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

    def email_quote(self):
        s = '"%s" -%s' %(self.quote,self.author) # %s stands for string
        quotelist = []
        for line in linelist:
            thesplit = line.split()
            quote = Quote_email(thesplit[0],thesplit[1]) 
        quotelist.append(quote)
        quotechoice = random.choice(quotelist)
        # print (quotechoice)

    def get_contacts(self, file_name,names , emails):
        self.filename = file_name
        self.names = []
        self.emails = []
        with open(self.filename, mode='r', encoding='utf-8') as contacts_file:
            for contact in contacts_file:
                self.names.append(contact.split()[0])
                self.emails.append(contact.split()[1])
        return self.names, self.emails

    def read_template(self):
        with open(self.filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def main(self):
        self.names, self.emails = get_contacts('my_contacts.txt') # read contacts
        message_template = read_template('model.txt')
        try:
            server = smtplib.SMTP(host='smtp-relay.sendinblue.com', port=587)
            server.ehlo()
            server.starttls()
            sever.login(user,passwrd)
            msg = f'Subject:{author}\n\n{quote}'
            server.sendmail(user,passwrd)
            server.quit()
            return 'successful:email sent'
        except:
            return 'email failed'
     
        msg['From']=user
        msg['To']=to_email
        msg['Subject']="This is TEST"

# email_sent = Quote_email(quote,author)
# print(email_sent.main())         
     

