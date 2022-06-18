import unittest, sys
sys.path.append("/home/ginger/workspace/md2pug/src/main") #TODO: change this before uploading
import converter, elements, assets.markdownToObjectTest_assets

class TestConverter(unittest.TestCase):
    
    def markdownToObjectTest(self):
        markdown_text = assets.markdownToObjectTest_assets.markdown_text
        
        obtained_object = converter.markdownToObject(markdown_text)
        
        expected_object = assets.markdownToObjectTest_assets.expected_object
        self.assertEqual(obtained_object, expected_object)


if __name__ == "__main__":
    unittest.main()