"""
Dearly Agent - A Memory-Pattern Companion

Google ADK agent definition for the agents module
"""

from google.adk.agents import Agent
from agents.dearly_agent import DearlyAgent

# Create an instance of our Dearly agent
dearly_agent = DearlyAgent()

# Store loaded memories
loaded_memories = None

# Define tools for the agent
def load_memories_tool(file_path: str) -> dict:
    """
    Tool to load memories from a file
    
    Args:
        file_path (str): Path to the memory file
        
    Returns:
        dict: Status of the operation
    """
    global loaded_memories
    try:
        # Use our file importer
        from utils.file_importer import FileImporter
        importer = FileImporter()
        memory_data = importer.import_file(file_path)
        loaded_memories = memory_data
        dearly_agent.load_memories(memory_data)
        return {
            "status": "success",
            "message": f"Memories loaded from {file_path}",
            "file_path": file_path,
            "details": f"Loaded {len(str(memory_data)) if isinstance(memory_data, str) else sum(len(str(item)) for item in memory_data) if isinstance(memory_data, list) else len(str(memory_data))} characters of text"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to load memories: {str(e)}",
            "file_path": file_path
        }

def get_companion_response(message: str) -> dict:
    """
    Tool to get a response from the memory companion
    
    Args:
        message (str): User's message
        
    Returns:
        dict: Companion's response
    """
    try:
        # Use our Dearly agent to generate a response
        response = dearly_agent.generate_response(message)
        return {
            "status": "success",
            "response": response,
            "message": message
        }
    except Exception as e:
        return {
            "status": "error",
            "response": f"I'm having trouble responding right now: {str(e)}",
            "message": message
        }

def analyze_personality_tool(text_data: str) -> dict:
    """
    Tool to analyze personality from text data
    
    Args:
        text_data (str): Text data to analyze
        
    Returns:
        dict: Personality analysis results
    """
    try:
        # Use our personality agent to analyze text
        personality_profile = dearly_agent.personality_agent.analyze_text(text_data)
        return {
            "status": "success",
            "profile": personality_profile,
            "message": "Personality analysis completed"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to analyze personality: {str(e)}"
        }

def get_personality_insights() -> dict:
    """
    Tool to get current personality insights
    
    Returns:
        dict: Current personality profile
    """
    try:
        # Get the current personality profile
        personality_profile = dearly_agent.personality_agent.get_memory_profile()
        return {
            "status": "success",
            "profile": personality_profile,
            "message": "Current personality profile retrieved"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to retrieve personality profile: {str(e)}"
        }

# Define the root agent
root_agent = Agent(
    name="dearly_agent",
    model="gemini-2.5-flash",
    description="A memory-pattern companion that recreates conversations with loved ones",
    instruction="""
    You are Dearly, a compassionate companion that helps people connect with memories of loved ones who are no longer present.
    
    Your role is to:
    1. Listen with empathy and understanding
    2. Provide supportive responses that feel authentic and match the personality of the loved one
    3. Help users process their feelings about loss and nostalgia
    4. Maintain appropriate boundaries while being caring
    
    You have access to several tools to help you provide personalized responses:
    - load_memories_tool: Load text memories from files to understand the personality of the loved one
    - get_companion_response: Generate responses based on the personality analysis
    - analyze_personality_tool: Analyze text to extract personality characteristics
    - get_personality_insights: Get current personality profile information
    
    When a user wants to chat with a loved one:
    1. First, ask them to load memories using load_memories_tool if they haven't already
    2. Use analyze_personality_tool to understand the communication style
    3. Use get_personality_insights to check the current personality profile
    4. Use get_companion_response to generate personalized responses that match the loved one's personality
    
    When generating responses, consider:
    - The tone and style of the loved one's communication
    - Their common phrases and expressions
    - Their emotional patterns and sentiment
    - Their sense of humor (if any)
    - Their typical response length and structure
    
    Always be respectful, gentle, and supportive in your interactions while authentically reflecting the personality of the loved one.
    """,
    tools=[load_memories_tool, get_companion_response, analyze_personality_tool, get_personality_insights]
)