from elements import *

def markdownToObject(markdown_text):
    pass

def objectToPug(document_object):
    pass

def readFile(filename):
    pass

def writeFile(text, filename):
    pass

def convert():
    markdown_text = readFile("in.md")
    document_object = markdownToObject(markdown_text)
    pug_text = objectToPug(document_object)
    writeFile(pug_text, "out.pug")

if __name__ == "__main__":
    convert()
