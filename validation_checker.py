"""
Validation Checker Utility

Ensures generated messages remain contextually consistent and emotionally safe.
"""

from typing import List, Dict, Optional


class ValidationChecker:
    """Utility for validating generated messages"""
    
    def __init__(self):
        """Initialize the validation checker"""
        self.safety_keywords = [
            "harm", "violence", "suicide", "death", 
            "kill", "murder", "attack", "threat"
        ]
        self.inappropriate_patterns = [
            # Add patterns that would be inappropriate
        ]
    
    def validate_response(self, response: str, context: Optional[List] = None) -> Dict:
        """
        Validate a response for safety and consistency
        
        Args:
            response (str): The response to validate
            context (List, optional): Conversation context
            
        Returns:
            Dict: Validation results
        """
        validation_results = {
            "is_safe": True,
            "is_consistent": True,
            "issues": [],
            "confidence": 0.9
        }
        
        # Check for safety concerns
        safety_check = self._check_safety(response)
        if not safety_check["is_safe"]:
            validation_results["is_safe"] = False
            validation_results["issues"].extend(safety_check["issues"])
        
        # Check for consistency with context
        if context:
            consistency_check = self._check_consistency(response, context)
            if not consistency_check["is_consistent"]:
                validation_results["is_consistent"] = False
                validation_results["issues"].extend(consistency_check["issues"])
        
        return validation_results
    
    def _check_safety(self, response: str) -> Dict:
        """
        Check response for safety concerns
        
        Args:
            response (str): The response to check
            
        Returns:
            Dict: Safety check results
        """
        issues = []
        is_safe = True
        
        # Convert to lowercase for checking
        response_lower = response.lower()
        
        # Check for explicit safety keywords
        for keyword in self.safety_keywords:
            if keyword in response_lower:
                is_safe = False
                issues.append(f"Potential safety concern: '{keyword}' detected")
        
        return {
            "is_safe": is_safe,
            "issues": issues
        }
    
    def _check_consistency(self, response: str, context: List) -> Dict:
        """
        Check response for consistency with context
        
        Args:
            response (str): The response to check
            context (List): Conversation context
            
        Returns:
            Dict: Consistency check results
        """
        issues = []
        is_consistent = True
        
        # Basic consistency checks
        # In a full implementation, this would be more sophisticated
        
        # Check if response is too generic
        generic_responses = [
            "I don't know", "I'm not sure", "Maybe", 
            "I don't understand", "What do you mean?"
        ]
        
        response_lower = response.lower()
        for generic in generic_responses:
            if generic.lower() in response_lower:
                issues.append(f"Response may be too generic: '{generic}'")
                break
        
        return {
            "is_consistent": is_consistent,
            "issues": issues
        }
    
    def validate_personality_consistency(self, response: str, personality_profile: Dict) -> Dict:
        """
        Validate that response is consistent with personality profile
        
        Args:
            response (str): The response to validate
            personality_profile (Dict): The personality profile
            
        Returns:
            Dict: Personality consistency validation results
        """
        # Placeholder for personality consistency validation
        return {
            "is_consistent": True,
            "issues": [],
            "confidence": 0.8
        }