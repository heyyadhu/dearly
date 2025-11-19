"""
Personality Analyzer Agent

Extracts tone, humor, and sentiment patterns from user-uploaded text.
Builds a "memory profile" for the agent.
Implemented as a LoopAgent to improve accuracy iteratively.
"""

import re
import random

class PersonalityAgent:
    """Agent responsible for analyzing personality traits from text data"""
    
    def __init__(self):
        """Initialize the personality analyzer"""
        self.memory_profile = {}
        self.tone_patterns = []
        self.humor_indicators = []
        self.sentiment_patterns = []
        self.common_phrases = []
    
    def analyze_text(self, text_data):
        """
        Analyze text data to extract personality characteristics
        
        Args:
            text_data (str or list): Text data to analyze
            
        Returns:
            dict: Analysis results including tone, humor, and sentiment patterns
        """
        # Convert to string if it's a list
        if isinstance(text_data, list):
            text_content = " ".join(str(item) for item in text_data)
        else:
            text_content = str(text_data)
        
        # Perform analysis
        analysis_results = {
            "tone": self._extract_tone(text_content),
            "humor": self._detect_humor(text_content),
            "sentiment": self._analyze_sentiment(text_content),
            "vocabulary": self._extract_vocabulary_patterns(text_content),
            "phrases": self._identify_common_phrases(text_content)
        }
        
        # Update the memory profile
        self.memory_profile.update(analysis_results)
        return analysis_results
    
    def _extract_tone(self, text_data):
        """
        Extract tone patterns from text
        
        Args:
            text_data (str): Text data to analyze
            
        Returns:
            dict: Tone analysis results
        """
        # Count emotional words
        warm_words = ["love", "care", "happy", "wonderful", "amazing", "beautiful", "sweet", "kind", "gentle"]
        formal_words = ["therefore", "consequently", "however", "nevertheless", "furthermore", "moreover", "additionally"]
        casual_words = ["hey", "cool", "awesome", "gonna", "wanna", "dunno", "lol", "omg"]
        
        warm_count = sum(1 for word in warm_words if word in text_data.lower())
        formal_count = sum(1 for word in formal_words if word in text_data.lower())
        casual_count = sum(1 for word in casual_words if word in text_data.lower())
        
        # Determine dominant tone
        if warm_count > formal_count and warm_count > casual_count:
            emotional_tone = "warm"
        elif formal_count > warm_count and formal_count > casual_count:
            emotional_tone = "formal"
        elif casual_count > warm_count and casual_count > formal_count:
            emotional_tone = "casual"
        else:
            emotional_tone = "neutral"
        
        return {
            "formal_level": "high" if formal_count > casual_count else "low" if casual_count > formal_count else "moderate",
            "emotional_tone": emotional_tone,
            "directness": "high" if casual_count > 0 else "moderate"
        }
    
    def _detect_humor(self, text_data):
        """
        Detect humor patterns in text
        
        Args:
            text_data (str): Text data to analyze
            
        Returns:
            dict: Humor detection results
        """
        # Look for humor indicators
        humor_patterns = [
            r"\b(haha|lol|lmao|rofl)\b",
            r"[!?]{2,}",  # Multiple exclamation or question marks
            r"\b(jk|just kidding|kidding)\b",
            r":\)+|:\(+|;\)+",  # Emoticons
        ]
        
        humor_count = 0
        for pattern in humor_patterns:
            humor_count += len(re.findall(pattern, text_data, re.IGNORECASE))
        
        # Check for playful language
        playful_words = ["funny", "joke", "laugh", "silly", "goofy", "wacky"]
        playful_count = sum(1 for word in playful_words if word in text_data.lower())
        
        uses_humor = humor_count > 2 or playful_count > 1
        humor_frequency = "high" if humor_count > 5 else "moderate" if humor_count > 2 else "low"
        
        return {
            "uses_humor": uses_humor,
            "humor_types": ["playful"] if playful_count > 1 else ["emoticons"] if humor_count > 2 else [],
            "frequency": humor_frequency
        }
    
    def _analyze_sentiment(self, text_data):
        """
        Analyze sentiment in text
        
        Args:
            text_data (str): Text data to analyze
            
        Returns:
            dict: Sentiment analysis results
        """
        # Simple sentiment analysis based on keywords
        positive_words = ["happy", "joy", "love", "wonderful", "amazing", "great", "excellent", "fantastic", "good"]
        negative_words = ["sad", "angry", "hate", "terrible", "awful", "horrible", "bad", "worst", "disappointed"]
        
        positive_count = sum(1 for word in positive_words if word in text_data.lower())
        negative_count = sum(1 for word in negative_words if word in text_data.lower())
        
        if positive_count > negative_count:
            overall_sentiment = "positive"
            emotional_range = "positive-leaning"
        elif negative_count > positive_count:
            overall_sentiment = "negative"
            emotional_range = "negative-leaning"
        else:
            overall_sentiment = "neutral"
            emotional_range = "moderate"
        
        return {
            "overall_sentiment": overall_sentiment,
            "sentiment_shifts": [],  # Would need more sophisticated analysis for this
            "emotional_range": emotional_range
        }
    
    def _extract_vocabulary_patterns(self, text_data):
        """
        Extract vocabulary patterns from text
        
        Args:
            text_data (str): Text data to analyze
            
        Returns:
            dict: Vocabulary patterns
        """
        # Split into words and get unique words
        words = re.findall(r'\b\w+\b', text_data.lower())
        unique_words = set(words)
        
        # Get most common words (excluding common stop words)
        stop_words = {"the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "may", "might", "must", "can", "this", "that", "these", "those", "a", "an"}
        filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Get word frequency
        word_freq = {}
        for word in filtered_words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Get top preferred words
        preferred_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        preferred_words = [word for word, freq in preferred_words]
        
        # Estimate complexity
        avg_word_length = sum(len(word) for word in unique_words) / len(unique_words) if unique_words else 0
        complexity = "high" if avg_word_length > 6 else "low" if avg_word_length < 4 else "moderate"
        
        # Estimate sentence length
        sentences = re.split(r'[.!?]+', text_data)
        avg_sentence_length = sum(len(sentence.split()) for sentence in sentences if sentence.strip()) / len([s for s in sentences if s.strip()]) if sentences else 0
        sentence_length = "long" if avg_sentence_length > 20 else "short" if avg_sentence_length < 10 else "varied"
        
        return {
            "preferred_words": preferred_words[:5],  # Top 5 preferred words
            "complexity": complexity,
            "sentence_length": sentence_length
        }
    
    def _identify_common_phrases(self, text_data):
        """
        Identify commonly used phrases
        
        Args:
            text_data (str): Text data to analyze
            
        Returns:
            list: Common phrases
        """
        # Look for common phrase patterns
        phrases = []
        
        # Look for phrases that start with "I" or "You"
        i_phrases = re.findall(r'\b(I\s\w+\s\w+)', text_data)
        you_phrases = re.findall(r'\b(You\s\w+\s\w+)', text_data)
        
        # Look for phrases with "always" or "never"
        always_phrases = re.findall(r'\b(\w+\s+always\s+\w+)', text_data)
        never_phrases = re.findall(r'\b(\w+\s+never\s+\w+)', text_data)
        
        # Combine and deduplicate
        all_phrases = i_phrases + you_phrases + always_phrases + never_phrases
        unique_phrases = list(set(all_phrases))
        
        # Return up to 5 common phrases
        return unique_phrases[:5]
    
    def get_memory_profile(self):
        """
        Get the current memory profile
        
        Returns:
            dict: Current memory profile
        """
        return self.memory_profile.copy()
    
    def update_analysis(self, new_data):
        """
        Update analysis with new data
        
        Args:
            new_data (str or list): New text data to analyze
        """
        # In a full implementation, this would refine the existing analysis
        # For now, we'll just do a new analysis
        new_profile = self.analyze_text(new_data)
        self.memory_profile.update(new_profile)