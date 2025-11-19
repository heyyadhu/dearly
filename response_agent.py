"""
Message Generator Agent

Produces responses that reflect the style and personality of the loved one.
Checks context, sentiment, and conversation continuity using Context Engineering.
"""

import random

class ResponseAgent:
    """Agent responsible for generating contextually appropriate responses"""
    
    def __init__(self):
        """Initialize the response generator"""
        self.personality_profile = {}
        self.context_history = []
        self.response_templates = []
    
    def generate_response(self, user_message, context=None):
        """
        Generate a response based on user message and context
        
        Args:
            user_message (str): The user's message
            context (list, optional): Conversation context
            
        Returns:
            str: Generated response
        """
        # Use personality profile to customize response
        if self.personality_profile:
            response = self._generate_personality_based_response(user_message, context)
        else:
            # Fallback to placeholder response
            response = self._generate_placeholder_response(user_message)
        
        return response
    
    def _generate_personality_based_response(self, user_message, context):
        """
        Generate a response based on personality profile
        
        Args:
            user_message (str): The user's message
            context (list): Conversation context
            
        Returns:
            str: Personality-based response
        """
        # Extract personality characteristics
        tone = self.personality_profile.get("tone", {}).get("emotional_tone", "neutral")
        humor = self.personality_profile.get("humor", {}).get("uses_humor", False)
        sentiment = self.personality_profile.get("sentiment", {}).get("overall_sentiment", "neutral")
        vocabulary = self.personality_profile.get("vocabulary", {}).get("preferred_words", [])
        phrases = self.personality_profile.get("phrases", [])
        
        # Adjust response based on personality
        if humor and random.random() < 0.3:  # 30% chance to use humor if personality has it
            return self._generate_humorous_response(user_message)
        elif tone == "warm" or sentiment == "positive":
            return self._generate_warm_response(user_message)
        elif tone == "formal":
            return self._generate_formal_response(user_message)
        elif phrases:
            # Use common phrases from the personality
            return f"{random.choice(phrases)} {self._generate_continuation(user_message)}"
        else:
            # Default personalized response
            return self._generate_personalized_response(user_message, tone, sentiment)
    
    def _generate_humorous_response(self, user_message):
        """
        Generate a humorous response
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: Humorous response
        """
        humorous_responses = [
            f"Haha, that reminds me of something funny!",
            f"You always know how to make me smile with comments like that.",
            f"That's quite the observation! I bet you're grinning as you type this.",
            f"Only you would say something like that!",
        ]
        return random.choice(humorous_responses)
    
    def _generate_warm_response(self, user_message):
        """
        Generate a warm response
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: Warm response
        """
        warm_responses = [
            f"I'm so glad you shared that with me.",
            f"Thank you for telling me about this. It means a lot.",
            f"You have such a beautiful way of looking at things.",
            f"I can feel the warmth in your words.",
        ]
        return random.choice(warm_responses)
    
    def _generate_formal_response(self, user_message):
        """
        Generate a formal response
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: Formal response
        """
        formal_responses = [
            f"Thank you for sharing your thoughts with me.",
            f"I appreciate you taking the time to communicate this to me.",
            f"Your perspective on this matter is quite insightful.",
            f"I find your observations to be particularly noteworthy.",
        ]
        return random.choice(formal_responses)
    
    def _generate_personalized_response(self, user_message, tone, sentiment):
        """
        Generate a personalized response based on tone and sentiment
        
        Args:
            user_message (str): The user's message
            tone (str): Emotional tone
            sentiment (str): Overall sentiment
            
        Returns:
            str: Personalized response
        """
        if sentiment == "positive":
            responses = [
                f"I'm happy to hear about this!",
                f"That sounds wonderful!",
                f"I can sense the joy in your message.",
                f"What a lovely thing to share.",
            ]
        elif sentiment == "negative":
            responses = [
                f"I'm here for you during this difficult time.",
                f"I understand this must be challenging for you.",
                f"It's okay to feel this way.",
                f"I'm listening, and I care about what you're going through.",
            ]
        else:  # neutral
            responses = [
                f"I've been thinking about what you said.",
                f"That's an interesting point.",
                f"I understand how you feel.",
                f"Thank you for sharing that with me.",
            ]
        
        return random.choice(responses)
    
    def _generate_continuation(self, user_message):
        """
        Generate a continuation for a response
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: Response continuation
        """
        continuations = [
            "How are you doing today?",
            "What's been on your mind lately?",
            "Is there anything specific you'd like to talk about?",
            "I'm here to listen whenever you need to share.",
        ]
        return random.choice(continuations)
    
    def _generate_placeholder_response(self, user_message):
        """
        Generate a placeholder response
        
        Args:
            user_message (str): The user's message
            
        Returns:
            str: Placeholder response
        """
        # This is a simple placeholder - a real implementation would use
        # the personality profile and context to generate a meaningful response
        responses = [
            "I've been thinking about what you said.",
            "That's an interesting point.",
            "I understand how you feel.",
            "Thank you for sharing that with me.",
            "I appreciate you telling me about this."
        ]
        
        return random.choice(responses)
    
    def set_personality_profile(self, profile):
        """
        Set the personality profile to use for response generation
        
        Args:
            profile (dict): Personality profile data
        """
        self.personality_profile = profile
    
    def add_context(self, context_item):
        """
        Add context to the context history
        
        Args:
            context_item (dict): Context information to add
        """
        self.context_history.append(context_item)
    
    def clear_context(self):
        """Clear the context history"""
        self.context_history = []
    
    def _apply_context_engineering(self, user_message):
        """
        Apply context engineering to ensure conversation continuity
        
        Args:
            user_message (str): The user's message
            
        Returns:
            dict: Context-engineered parameters
        """
        # Placeholder for context engineering
        return {
            "tone_adjustment": "neutral",
            "reference_previous": False,
            "emotional_alignment": "maintain"
        }
    
    def _ensure_continuity(self, response):
        """
        Ensure conversation continuity in the response
        
        Args:
            response (str): Generated response
            
        Returns:
            str: Continuity-checked response
        """
        # Placeholder for continuity checking
        return response