"""
Basic tests for Dearly agents
"""

import unittest
from agents.dearly_agent import DearlyAgent
from agents.personality_agent import PersonalityAgent
from agents.memory_agent import MemoryAgent
from agents.response_agent import ResponseAgent
from agents.emotion_agent import EmotionAgent


class TestDearlyAgents(unittest.TestCase):
    
    def test_dearly_agent_initialization(self):
        """Test that DearlyAgent initializes all sub-agents"""
        agent = DearlyAgent()
        
        self.assertIsNotNone(agent.personality_agent)
        self.assertIsNotNone(agent.memory_agent)
        self.assertIsNotNone(agent.response_agent)
        self.assertIsNotNone(agent.emotion_agent)
        
        # Check that sub-agents are of the correct types
        self.assertIsInstance(agent.personality_agent, PersonalityAgent)
        self.assertIsInstance(agent.memory_agent, MemoryAgent)
        self.assertIsInstance(agent.response_agent, ResponseAgent)
        self.assertIsInstance(agent.emotion_agent, EmotionAgent)
    
    def test_personality_agent_analysis(self):
        """Test personality agent analysis functionality"""
        agent = PersonalityAgent()
        
        # Test with sample text
        sample_text = "Hello there! How are you doing today? I hope you're having a wonderful day!"
        results = agent.analyze_text(sample_text)
        
        # Check that we get results
        self.assertIsInstance(results, dict)
        self.assertIn("tone", results)
        self.assertIn("humor", results)
        self.assertIn("sentiment", results)
        
        # Check that memory profile is updated
        profile = agent.get_memory_profile()
        self.assertIsInstance(profile, dict)
    
    def test_memory_agent_storage(self):
        """Test memory agent storage functionality"""
        agent = MemoryAgent()
        
        # Test storing a message
        agent.store_message("user", "Hello, how are you?")
        
        # Check that message is stored
        recent_context = agent.get_recent_context(1)
        self.assertEqual(len(recent_context), 1)
        self.assertEqual(recent_context[0]["sender"], "user")
        self.assertEqual(recent_context[0]["message"], "Hello, how are you?")
        
        # Test long-term memory
        agent.store_long_term_memory("name", "John")
        retrieved = agent.retrieve_memory("name")
        self.assertEqual(retrieved, "John")
    
    def test_response_agent_generation(self):
        """Test response agent generation functionality"""
        agent = ResponseAgent()
        
        # Test generating a response
        response = agent.generate_response("Hello there!")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
    
    def test_emotion_agent_analysis(self):
        """Test emotion agent analysis functionality"""
        agent = EmotionAgent()
        
        # Test sentiment analysis
        result = agent.analyze_sentiment("I'm feeling great today!", "user")
        
        # Check result structure
        self.assertIsInstance(result, dict)
        self.assertIn("sender", result)
        self.assertIn("message", result)
        self.assertIn("sentiment", result)
        self.assertIn("emotional_tone", result)
        
        # Test emotional summary
        summary = agent.get_emotional_summary()
        self.assertIsInstance(summary, dict)
        self.assertIn("overall_trend", summary)


if __name__ == '__main__':
    unittest.main()