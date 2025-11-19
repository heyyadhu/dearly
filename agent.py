"""
Utility Agent for Dearly - A Memory-Pattern Companion

Google ADK agent definition for the utils module
"""

from google.adk.agents import Agent

# Define the root agent
root_agent = Agent(
    name="utils_agent",
    model="gemini-2.5-flash",
    description="Utility agent for Dearly that provides helper functions",
    instruction="""
    You are a utility agent for Dearly, a memory-pattern companion application.
    
    Your role is to provide helper functions and utilities for the main Dearly agent.
    You can help with file operations, data processing, and other utility tasks.
    
    Always be helpful and efficient in your responses.
    """
)