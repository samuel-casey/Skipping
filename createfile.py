def createfile(text, name='name.txt'):
    text_flie = open(name,'w')
    text_flie.write(text)
    text_flie.close