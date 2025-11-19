"""
Dearly Agent - Core orchestrator for the memory-pattern companion

This agent coordinates all sub-agents to provide a cohesive experience.
"""

from google.adk.agents import Agent
from .personality_agent import PersonalityAgent
from .memory_agent import MemoryAgent
from .response_agent import ResponseAgent
from .emotion_agent import EmotionAgent


class DearlyAgent:
    """Main orchestrator agent for Dearly using Google ADK"""
    
    def __init__(self):
        """Initialize the Dearly agent and all sub-agents"""
        # Initialize all sub-agents
        self.personality_agent = PersonalityAgent()
        self.memory_agent = MemoryAgent()
        self.response_agent = ResponseAgent()
        self.emotion_agent = EmotionAgent()
        
        # Store personality profile
        self.personality_profile = {}
    
    def start_conversation(self):
        """Start the conversation loop with the user"""
        print("Starting conversation with your memory companion...")
        print("Type 'quit' to exit the conversation.\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! Take care.")
                break
            
            response = self.generate_response(user_input)
            print(f"Companion: {response}")
    
    def generate_response(self, user_input):
        """
        Generate a response based on user input
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The companion's response
        """
        # Store user message in memory
        self.memory_agent.store_message("user", user_input)
        
        # Analyze sentiment of user input
        user_sentiment = self.emotion_agent.analyze_sentiment(user_input, "user")
        
        # Generate response using response agent with personality context
        context = self.memory_agent.get_recent_context()
        
        # Enhance response with personality profile
        if self.personality_profile:
            # Pass personality profile to response agent
            self.response_agent.set_personality_profile(self.personality_profile)
        
        response = self.response_agent.generate_response(user_input, context)
        
        # Store companion response in memory
        self.memory_agent.store_message("companion", response)
        
        # Analyze sentiment of companion response
        companion_sentiment = self.emotion_agent.analyze_sentiment(response, "companion")
        
        return response
    
    def load_memories(self, memory_data):
        """
        Load memory data for the companion
        
        Args:
            memory_data (dict): The memory data to load
        """
        # Analyze personality from memory data
        personality_profile = self.personality_agent.analyze_text(memory_data)
        
        # Store personality profile
        self.personality_profile = personality_profile
        
        # Set personality profile in response agent
        self.response_agent.set_personality_profile(personality_profile)
        
        # Store in long-term memory
        self.memory_agent.store_long_term_memory("personality_profile", personality_profile)
        
        return personality_profile