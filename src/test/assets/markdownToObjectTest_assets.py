from elements import *

markdown_text = "# title\n\n\n## subtitle1\n text element `code element` \n\ntext element2 \n## subtitle2\n```code element 2```"

expected_object = Document()

title = Title()
expected_object.elements.append(Title())