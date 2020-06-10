import random


quote_file = open('model.txt','r')
line_list = quotefile.read().split('\n') #read the file however you'd like, this is just how i sometimes do it
quote_file.close()

class Quote:
    def __init__(self,quote,author):
        self.quote = quote
        self.author = author

    def __str__(self):
        s = '"%s" -%s' %(self.quote,self.author)
        quotelist = []
        for line in linelist:
            thesplit = line.split()
            quote = Quote(thesplit[0],thesplit[1]) 
        quotelist.append(quote)
        quotechoice = random.choice(quotelist)
        print (quotechoice)

