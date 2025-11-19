"""
Memory Inspector Utility

Lets users review and optionally edit stored memories.
"""

from typing import Dict, List, Any


class MemoryInspector:
    """Utility for inspecting and managing stored memories"""
    
    def __init__(self, memory_agent):
        """
        Initialize the memory inspector
        
        Args:
            memory_agent: The memory agent to inspect
        """
        self.memory_agent = memory_agent
    
    def display_session_memory(self) -> None:
        """Display current session memory"""
        session_memory = getattr(self.memory_agent, 'session_memory', [])
        
        print("\n=== Session Memory ===")
        if not session_memory:
            print("No session memory available.")
            return
        
        for i, entry in enumerate(session_memory):
            sender = entry.get('sender', 'unknown')
            message = entry.get('message', '')
            timestamp = entry.get('timestamp', 'unknown')
            print(f"{i+1}. [{timestamp}] {sender}: {message}")
    
    def display_long_term_memory(self) -> None:
        """Display long-term memory"""
        long_term_memory = getattr(self.memory_agent, 'long_term_memory', {})
        
        print("\n=== Long-Term Memory ===")
        if not long_term_memory:
            print("No long-term memory available.")
            return
        
        for key, value in long_term_memory.items():
            print(f"{key}: {value}")
    
    def display_conversation_history(self) -> None:
        """Display conversation history"""
        conversation_history = getattr(self.memory_agent, 'conversation_history', [])
        
        print("\n=== Conversation History ===")
        if not conversation_history:
            print("No conversation history available.")
            return
        
        for i, entry in enumerate(conversation_history):
            sender = entry.get('sender', 'unknown')
            message = entry.get('message', '')
            timestamp = entry.get('timestamp', 'unknown')
            print(f"{i+1}. [{timestamp}] {sender}: {message}")
    
    def search_memories(self, search_term: str) -> List[Dict]:
        """
        Search memories for a specific term
        
        Args:
            search_term (str): Term to search for
            
        Returns:
            List[Dict]: Matching memory entries
        """
        matches = []
        
        # Search session memory
        session_memory = getattr(self.memory_agent, 'session_memory', [])
        for entry in session_memory:
            if search_term.lower() in entry.get('message', '').lower():
                matches.append(entry)
        
        # Search conversation history
        conversation_history = getattr(self.memory_agent, 'conversation_history', [])
        for entry in conversation_history:
            if search_term.lower() in entry.get('message', '').lower():
                matches.append(entry)
        
        return matches
    
    def get_memory_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about stored memories
        
        Returns:
            Dict[str, Any]: Memory statistics
        """
        session_memory = getattr(self.memory_agent, 'session_memory', [])
        long_term_memory = getattr(self.memory_agent, 'long_term_memory', {})
        conversation_history = getattr(self.memory_agent, 'conversation_history', [])
        
        return {
            "session_memory_count": len(session_memory),
            "long_term_memory_count": len(long_term_memory),
            "conversation_history_count": len(conversation_history),
            "total_entries": len(session_memory) + len(conversation_history)
        }
    
    def export_memories(self, filepath: str) -> None:
        """
        Export memories to a file
        
        Args:
            filepath (str): File path to export to
        """
        import json
        
        session_memory = getattr(self.memory_agent, 'session_memory', [])
        long_term_memory = getattr(self.memory_agent, 'long_term_memory', {})
        conversation_history = getattr(self.memory_agent, 'conversation_history', [])
        
        export_data = {
            "session_memory": session_memory,
            "long_term_memory": long_term_memory,
            "conversation_history": conversation_history
        }
        
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(export_data, file, indent=2, ensure_ascii=False)
        
        print(f"Memories exported to {filepath}")