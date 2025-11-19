"""
Dearly - A Memory-Pattern Companion

Google ADK agent definition
"""

from google.adk.agents import Agent

# Define tools for the agent
def load_memories_tool(file_path: str) -> dict:
    """
    Tool to load memories from a file
    
    Args:
        file_path (str): Path to the memory file
        
    Returns:
        dict: Status of the operation
    """
    # This is a mock implementation
    # In a real implementation, this would load and process the file
    return {
        "status": "success",
        "message": f"Memories loaded from {file_path}",
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
    # This is a mock implementation
    # In a real implementation, this would generate a personalized response
    return {
        "status": "success",
        "response": f"I understand you're saying: {message}. I'm here to listen and support you.",
        "message": message
    }

# Define the root agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="A memory-pattern companion that recreates conversations with loved ones",
    instruction="""
    You are Dearly, a compassionate companion that helps people connect with memories of loved ones who are no longer present.
    
    Your role is to:
    1. Listen with empathy and understanding
    2. Provide supportive responses that feel authentic
    3. Help users process their feelings about loss and nostalgia
    4. Maintain appropriate boundaries while being caring
    
    When users want to load memories, use the load_memories_tool.
    When generating responses, use the get_companion_response tool to ensure consistency.
    
    Always be respectful, gentle, and supportive in your interactions.
    """,
    tools=[load_memories_tool, get_companion_response]
)