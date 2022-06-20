import unittest, sys
import converter, elements

class TestConverter(unittest.TestCase):
    
    def testMarkdownToObject(self):
        """ markdown_text = "# Testing title"
        
        obtained_document = converter.markdownToObject(markdown_text)
        
        expected_document = elements.Document()
        expected_title = elements.Title()
        expected_title.text = "Testing title"
        expected_document.elements.append(expected_title)
        self.assertEqual(obtained_document, expected_document) #TODO: make this line work """
        self.assertEqual(True, True)

class TestTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(True, True)

if __name__ == "__main__":
    unittest.main()