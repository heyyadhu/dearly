"""
Sentiment Tracker Agent

Monitors emotional tone in both user and agent messages.
Logs shifts over time for observability and insight.
"""

class EmotionAgent:
    """Agent responsible for tracking emotional sentiment in conversations"""
    
    def __init__(self):
        """Initialize the emotion tracker"""
        self.emotional_log = []
        self.sentiment_history = []
        self.emotional_shifts = []
    
    def analyze_sentiment(self, message, sender="user"):
        """
        Analyze the sentiment of a message
        
        Args:
            message (str): The message to analyze
            sender (str): Who sent the message ("user" or "companion")
            
        Returns:
            dict: Sentiment analysis results
        """
        # Placeholder for actual sentiment analysis
        # In a full implementation, this would use NLP techniques
        sentiment_data = {
            "sender": sender,
            "message": message,
            "sentiment": self._detect_sentiment(message),
            "confidence": 0.75,
            "emotional_tone": self._detect_emotional_tone(message),
            "timestamp": self._get_current_timestamp()
        }
        
        # Log the sentiment analysis
        self.emotional_log.append(sentiment_data)
        self.sentiment_history.append(sentiment_data)
        
        # Check for emotional shifts
        self._check_for_emotional_shifts(sentiment_data)
        
        return sentiment_data
    
    def _detect_sentiment(self, message):
        """
        Detect sentiment in a message
        
        Args:
            message (str): The message to analyze
            
        Returns:
            str: Detected sentiment ("positive", "negative", "neutral")
        """
        # Placeholder implementation
        # A real implementation would use NLP libraries like VADER, TextBlob, etc.
        return "neutral"
    
    def _detect_emotional_tone(self, message):
        """
        Detect emotional tone in a message
        
        Args:
            message (str): The message to analyze
            
        Returns:
            list: Emotional tones detected
        """
        # Placeholder implementation
        return ["neutral"]
    
    def _check_for_emotional_shifts(self, current_sentiment):
        """
        Check for emotional shifts and log them
        
        Args:
            current_sentiment (dict): Current sentiment data
        """
        if len(self.sentiment_history) > 1:
            previous_sentiment = self.sentiment_history[-2]
            if previous_sentiment["sentiment"] != current_sentiment["sentiment"]:
                shift_data = {
                    "from": previous_sentiment["sentiment"],
                    "to": current_sentiment["sentiment"],
                    "timestamp": current_sentiment["timestamp"]
                }
                self.emotional_shifts.append(shift_data)
    
    def get_emotional_summary(self):
        """
        Get a summary of emotional trends
        
        Returns:
            dict: Emotional trend summary
        """
        if not self.sentiment_history:
            return {"overall_trend": "neutral", "shifts_count": 0}
        
        # Simple summary calculation
        sentiments = [entry["sentiment"] for entry in self.sentiment_history]
        positive_count = sentiments.count("positive")
        negative_count = sentiments.count("negative")
        neutral_count = sentiments.count("neutral")
        
        if positive_count > negative_count and positive_count > neutral_count:
            overall_trend = "positive"
        elif negative_count > positive_count and negative_count > neutral_count:
            overall_trend = "negative"
        else:
            overall_trend = "neutral"
        
        return {
            "overall_trend": overall_trend,
            "positive_count": positive_count,
            "negative_count": negative_count,
            "neutral_count": neutral_count,
            "shifts_count": len(self.emotional_shifts)
        }
    
    def get_emotional_log(self):
        """
        Get the full emotional log
        
        Returns:
            list: Full emotional log
        """
        return self.emotional_log.copy()
    
    def _get_current_timestamp(self):
        """
        Get current timestamp
        
        Returns:
            str: Current timestamp
        """
        from datetime import datetime
        return datetime.now().isoformat()