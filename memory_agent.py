"""
Memory Manager Agent

Handles session and long-term memory using ADK's Memory Bank and InMemorySessionService.
Stores conversation history, recurring phrases, and emotional context.
"""

class MemoryAgent:
    """Agent responsible for managing memories and conversation history"""
    
    def __init__(self):
        """Initialize the memory manager"""
        self.session_memory = []
        self.long_term_memory = {}
        self.conversation_history = []
        self.recurring_phrases = []
        self.emotional_context = {}
    
    def store_message(self, sender, message, timestamp=None):
        """
        Store a message in session memory
        
        Args:
            sender (str): Who sent the message ("user" or "companion")
            message (str): The message content
            timestamp (datetime, optional): When the message was sent
        """
        memory_entry = {
            "sender": sender,
            "message": message,
            "timestamp": timestamp or self._get_current_timestamp()
        }
        
        self.session_memory.append(memory_entry)
        self.conversation_history.append(memory_entry)
    
    def store_long_term_memory(self, key, value):
        """
        Store information in long-term memory
        
        Args:
            key (str): The memory key
            value (any): The memory value
        """
        self.long_term_memory[key] = value
    
    def retrieve_memory(self, key):
        """
        Retrieve information from long-term memory
        
        Args:
            key (str): The memory key to retrieve
            
        Returns:
            any: The memory value or None if not found
        """
        return self.long_term_memory.get(key)
    
    def get_recent_context(self, num_messages=5):
        """
        Get recent conversation context
        
        Args:
            num_messages (int): Number of recent messages to retrieve
            
        Returns:
            list: Recent messages
        """
        return self.conversation_history[-num_messages:] if self.conversation_history else []
    
    def update_emotional_context(self, context_data):
        """
        Update emotional context
        
        Args:
            context_data (dict): Emotional context data
        """
        self.emotional_context.update(context_data)
    
    def get_emotional_context(self):
        """
        Get current emotional context
        
        Returns:
            dict: Current emotional context
        """
        return self.emotional_context.copy()
    
    def clear_session_memory(self):
        """Clear session memory"""
        self.session_memory = []
    
    def save_conversation(self, filename):
        """
        Save conversation to a file
        
        Args:
            filename (str): File to save conversation to
        """
        # Placeholder for saving conversation
        pass
    
    def load_conversation(self, filename):
        """
        Load conversation from a file
        
        Args:
            filename (str): File to load conversation from
        """
        # Placeholder for loading conversation
        pass
    
    def _get_current_timestamp(self):
        """
        Get current timestamp
        
        Returns:
            str: Current timestamp
        """
        from datetime import datetime
        return datetime.now().isoformat()