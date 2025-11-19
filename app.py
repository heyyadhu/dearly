#!/usr/bin/env python3
"""
Dearly - A Memory-Pattern Companion

Main application entry point using Google ADK
"""

import sys
from agents.dearly_agent import DearlyAgent
from utils.file_importer import FileImporter
from config import config


def main():
    """Main application entry point"""
    print(f"Welcome to {config.PROJECT_NAME} v{config.VERSION}")
    print(config.DESCRIPTION)
    print("Bringing cherished messages back to life, one text at a time.\n")
    
    # Initialize the core agent
    dearly = DearlyAgent()
    
    # Show initial options
    show_options()
    
    while True:
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            # Start conversation
            dearly.start_conversation()
        elif choice == '2':
            # Load memories
            load_memories(dearly)
        elif choice == '3':
            # Show options again
            show_options()
        elif choice == '4':
            # Exit
            print("Thank you for using Dearly. Take care!")
            break
        else:
            print("Invalid option. Please select 1-4.")


def show_options():
    """Display available options"""
    print("\nOptions:")
    print("1. Start conversation with your memory companion")
    print("2. Load memories from text files")
    print("3. Show options again")
    print("4. Exit")


def load_memories(dearly_agent):
    """
    Load memories from files
    
    Args:
        dearly_agent: The DearlyAgent instance
    """
    print("\nLoading memories...")
    print(f"Supported formats: {', '.join(config.SUPPORTED_FILE_FORMATS)}")
    
    file_path = input("Enter path to memory file (or 'cancel' to go back): ").strip()
    
    if file_path.lower() == 'cancel':
        return
    
    try:
        importer = FileImporter()
        memory_data = importer.import_file(file_path)
        dearly_agent.load_memories(memory_data)
        print("Memories loaded successfully!")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except ValueError as e:
        print(f"Error loading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()