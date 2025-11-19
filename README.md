# Dearly - A Memory-Pattern Companion

*Bringing cherished messages back to life, one text at a time.*

## Project Overview

Dearly is a multi-agent system designed to provide comfort, companionship, and emotional support by recreating text conversations with loved ones who are no longer present. Users securely upload messages, letters, or emails from the person they miss. The agents analyze tone, style, vocabulary, and sentiment to generate context-aware responses, maintaining continuity and emotional authenticity. This creates a private, interactive companion that feels like chatting with someone you love and trust—a safe space for nostalgia, reflection, and emotional healing.

## Problem Statement

Grief, loneliness, and nostalgia are universal human experiences. People often wish they could interact again with someone they've lost, but text messages, emails, and letters only allow passive revisiting. There's no ethical, private way to recreate the presence of loved ones through real-time text interaction, leaving a gap in emotional support for those struggling with loss.

## Solution Statement

Dearly addresses this by:

* **Analyzing personality and tone:** Multi-agent system trains on uploaded texts to capture humor, phrasing, sentiment, and style.
* **Generating memory-driven responses:** Produces context-aware text messages that reflect the personality of the loved one.
* **Maintaining continuity:** Session memory keeps track of past conversations to provide coherent, emotionally consistent responses.
* **Tracking emotional impact:** Sentiment analysis and observability logs allow users to monitor emotional shifts and reflect on conversations safely.

The result is a comforting, interactive chat experience, turning static memories into living, supportive interactions.

## Architecture

### Core Agent
* **dearly_agent** – Orchestrates sub-agents, manages memory, and generates responses using Google ADK.

### Sub-Agents

1. **Personality Analyzer (personality_agent)**
   * Extracts tone, humor, and sentiment patterns from user-uploaded text.
   * Builds a "memory profile" for the agent.
   * Implemented as a LoopAgent to improve accuracy iteratively.

2. **Memory Manager (memory_agent)**
   * Handles session and long-term memory using ADK's Memory Bank and InMemorySessionService.
   * Stores conversation history, recurring phrases, and emotional context.

3. **Message Generator (response_agent)**
   * Produces responses that reflect the style and personality of the loved one.
   * Checks context, sentiment, and conversation continuity using Context Engineering.

4. **Sentiment Tracker (emotion_agent)**
   * Monitors emotional tone in both user and agent messages.
   * Logs shifts over time for observability and insight.

### Tools & Utilities

* **File Importer:** Securely uploads messages, emails, and letters.
* **Validation Checker:** Ensures generated messages remain contextually consistent and emotionally safe.
* **Memory Inspector:** Lets users review and optionally edit stored memories.

## Implementation

* **Language:** Python
* **Framework:** Google Agent Development Kit (ADK)
* **Key Concepts Applied:** Multi-agent system, Memory & Sessions, Observability, Context Engineering, Loop Agents
* **Demo/Deployment:** Kaggle Notebook or Colab showing sample interactions.

## Getting Started

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your Google API key:
   ```
   echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Or run with ADK CLI:
   ```
   adk run .
   ```

## Project Structure

```
dearly/
├── agent.py               # ADK agent definition
├── app.py                 # Main application entry point
├── adk.yaml               # ADK configuration
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── architecture.md       # Architecture diagram
├── agents/               # Agent implementations
│   ├── __init__.py
│   ├── dearly_agent.py   # Core orchestrator
│   ├── personality_agent.py
│   ├── memory_agent.py
│   ├── response_agent.py
│   └── emotion_agent.py
├── utils/                # Utility functions
│   ├── __init__.py
│   ├── file_importer.py
│   ├── validation_checker.py
│   └── memory_inspector.py
└── tests/                # Test suite
    ├── __init__.py
    ├── test_agents.py
    └── test_utils.py
```

## Value Statement

Dearly transforms passive memory browsing into active emotional support. By enabling personalized, text-based interaction with loved ones, it helps users cope with grief, feel companionship, and cherish memories safely. This project combines technical depth with human-centered design—making it both innovative and deeply meaningful.