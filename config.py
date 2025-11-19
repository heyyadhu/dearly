"""
Configuration file for Dearly - A Memory-Pattern Companion
"""

import os

class Config:
    """Configuration class for Dearly"""
    
    # Project information
    PROJECT_NAME = "Dearly"
    VERSION = "0.1.0"
    DESCRIPTION = "A Memory-Pattern Companion"
    
    # Directory paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    AGENTS_DIR = os.path.join(BASE_DIR, "agents")
    UTILS_DIR = os.path.join(BASE_DIR, "utils")
    TESTS_DIR = os.path.join(BASE_DIR, "tests")
    
    # Memory settings
    MAX_SESSION_MEMORY = 100
    MEMORY_SAVE_INTERVAL = 10  # Save memory every 10 interactions
    
    # Response settings
    MAX_RESPONSE_LENGTH = 500
    DEFAULT_RESPONSE_TIMEOUT = 30  # seconds
    
    # Safety settings
    ENABLE_SAFETY_CHECKS = True
    BLOCK_INAPPROPRIATE_CONTENT = True
    
    # Emotional tracking
    ENABLE_SENTIMENT_ANALYSIS = True
    EMOTION_LOGGING = True
    
    # File import settings
    SUPPORTED_FILE_FORMATS = [".txt", ".json", ".csv", ".md"]
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    
    # Demo settings
    DEMO_MODE = False
    SAMPLE_RESPONSES = [
        "I've been thinking about what you said.",
        "That's an interesting point.",
        "I understand how you feel.",
        "Thank you for sharing that with me.",
        "I appreciate you telling me about this."
    ]


# Global configuration instance
config = Config()