"""
File Importer Utility

Securely uploads messages, emails, and letters.
"""

import os
import json
from typing import Union, List, Dict


class FileImporter:
    """Utility for importing various types of text files"""
    
    def __init__(self):
        """Initialize the file importer"""
        self.supported_formats = ['.txt', '.json', '.csv', '.md']
    
    def import_file(self, file_path: str) -> Union[str, List[str], Dict]:
        """
        Import a file and return its contents
        
        Args:
            file_path (str): Path to the file to import
            
        Returns:
            Union[str, List[str], Dict]: File contents in appropriate format
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is not supported
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        _, ext = os.path.splitext(file_path)
        
        if ext not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {ext}")
        
        if ext == '.txt':
            return self._import_txt(file_path)
        elif ext == '.json':
            return self._import_json(file_path)
        elif ext == '.csv':
            return self._import_csv(file_path)
        elif ext == '.md':
            return self._import_md(file_path)
        
        # Fallback - should not reach here due to validation above
        raise ValueError(f"Unsupported file format: {ext}")
    
    def _import_txt(self, file_path: str) -> str:
        """
        Import a text file
        
        Args:
            file_path (str): Path to the text file
            
        Returns:
            str: File contents as string
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def _import_json(self, file_path: str) -> Dict:
        """
        Import a JSON file
        
        Args:
            file_path (str): Path to the JSON file
            
        Returns:
            Dict: Parsed JSON data
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def _import_csv(self, file_path: str) -> List[str]:
        """
        Import a CSV file (returns list of lines)
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            List[str]: List of CSV lines
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    
    def _import_md(self, file_path: str) -> str:
        """
        Import a Markdown file
        
        Args:
            file_path (str): Path to the Markdown file
            
        Returns:
            str: File contents as string
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def batch_import(self, directory_path: str) -> Dict[str, Union[str, List[str], Dict]]:
        """
        Import all supported files from a directory
        
        Args:
            directory_path (str): Path to directory containing files
            
        Returns:
            Dict[str, Union[str, List[str], Dict]]: Dictionary mapping filenames to contents
        """
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        imported_files = {}
        
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                if ext in self.supported_formats:
                    try:
                        imported_files[filename] = self.import_file(file_path)
                    except Exception as e:
                        print(f"Warning: Could not import {filename}: {e}")
        
        return imported_files