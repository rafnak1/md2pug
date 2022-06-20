from elements import *
import markdown
import xml.etree.ElementTree as ET

def markdownToObject(markdown_text):
    html = markdown.markdown(markdown_text)
    root = ET.fromstring(html)
    return root

def initial_boilerplate(document_object):
    boilerplate = ""
    with open("boilerplate.txt") as f:
        boilerplate += f.read()
    boilerplate += document_object[0].text
    boilerplate += "]\n"
    return boilerplate

def incomplete_objectToPug():
    pass

def objectToPug(document_object):
    pug_text = ""
    pug_text += initial_boilerplate(document_object)
    pug_text += incomplete_objectToPug(document_object)
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
