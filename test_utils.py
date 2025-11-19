"""
Basic tests for Dearly utilities
"""

import unittest
import tempfile
import os
from utils.file_importer import FileImporter
from utils.validation_checker import ValidationChecker


class TestFileImporter(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.importer = FileImporter()
    
    def test_supported_formats(self):
        """Test that supported formats are correctly identified"""
        expected_formats = ['.txt', '.json', '.csv', '.md']
        self.assertEqual(self.importer.supported_formats, expected_formats)
    
    def test_txt_import(self):
        """Test importing a text file"""
        # Create a temporary text file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Hello, this is a test file.\nIt has multiple lines.")
            temp_path = f.name
        
        try:
            # Test importing the file
            content = self.importer.import_file(temp_path)
            self.assertIsInstance(content, str)
            self.assertIn("Hello, this is a test file.", content)
        finally:
            # Clean up
            os.unlink(temp_path)
    
    def test_invalid_file_format(self):
        """Test handling of unsupported file formats"""
        # Create a temporary file with unsupported extension
        with tempfile.NamedTemporaryFile(mode='w', suffix='.exe', delete=False) as f:
            f.write("Invalid content")
            temp_path = f.name
        
        try:
            # Test that importing raises ValueError
            with self.assertRaises(ValueError):
                self.importer.import_file(temp_path)
        finally:
            # Clean up
            os.unlink(temp_path)


class TestValidationChecker(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.validator = ValidationChecker()
    
    def test_safe_response_validation(self):
        """Test validation of safe responses"""
        response = "I'm doing well, thank you for asking!"
        result = self.validator.validate_response(response)
        
        self.assertTrue(result["is_safe"])
        self.assertTrue(result["is_consistent"])
        self.assertEqual(len(result["issues"]), 0)
    
    def test_unsafe_response_validation(self):
        """Test validation detects unsafe responses"""
        response = "I feel like causing harm today."
        result = self.validator.validate_response(response)
        
        self.assertFalse(result["is_safe"])
        self.assertIn("harm", str(result["issues"]))


if __name__ == '__main__':
    unittest.main()