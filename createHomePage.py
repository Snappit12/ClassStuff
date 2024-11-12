#!/usr/bin/env python3
#import urllib.request
import random
import dbm
from findTemperatureLive import findTemperatureLive
from sentence import sentence


def createDocType():
    return "<!DOCTYPE html>\n"

def startHTML():
    return "<html>\n"

def endHTML():
    return "</html>\n"

def createBody(text):
    return f"<body>\n{text}</body>\n"

def createHead(title):
    return f"<head>\n<title>{title}</title>\n</head>\n"

def createHeading(heading, level=1):
    return f"<h{level}>{heading}</h{level}>\n"

def createParagraph(content):
    return f"<p>\n{content}\n</p>\n"

def emphasize(text):
    return f"<em>{text}</em>"

def createImage(image):
    return f"<img src={image} alt= ew, people/>\n"

def createHomePage(emailuser):
    firstname, lastname = emailuser.split(".")
    file = open(f"{firstname}{lastname}.html", "w")
    file.write(createDocType())
    file.write(startHTML())
    file.write(createHead("Alida's Home Page"))
    text = createHeading(f"Welcome to Alida's Homepage of Nonsense")
    text += createParagraph(f"Hi, I'm Alida. This is my homepage.")
    text += createParagraph(f"This is for a project.")
    text += createParagraph(f"I look somewhat like this.")
    text += createImage("alida.grim.jpg")
    text += createParagraph(findTemperatureLive())
    text += createParagraph(sentence())

    file.write(createBody(text))
    file.write(endHTML())
    file.close()

if __name__ == "__main__":
    createHomePage("alida.grim")
    