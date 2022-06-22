from elements import *
import markdown
import xml.etree.ElementTree as ET

def markdownToObject(markdown_text):
    html = "<body>" + markdown.markdown(markdown_text) + "</body>"
    print(html)
    root = ET.fromstring(html)
    return root

def initial_boilerplate(document_object):
    boilerplate = ""
    with open("boilerplate.txt") as f:
        boilerplate += f.read()
    boilerplate += document_object[0].text
    boilerplate += "]\n"
    return boilerplate

# assumes that document_object[0] is the h1 title
def objectExceptTitleToPug(document_object):
    pass #TODO next

def objectToPug(document_object):
    pug_text = ""
    pug_text += initial_boilerplate(document_object)
    pug_text += objectExceptTitleToPug(document_object)
    return pug_text

def readFile(filename):
    with open(filename) as f:
        text = f.read()
    return text

def writeFile(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

def convert():
    markdown_text = readFile("in.md")
    document_object = markdownToObject(markdown_text)
    pug_text = objectToPug(document_object)
    # writeFile(pug_text, "out.pug")

if __name__ == "__main__":
    convert()
