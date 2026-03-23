Why we need AI Agent Framework -
    - AI agents are LLM (Large Language Model) powered applications that perceive tasks, reason, and act autonomously toward completing goals.
    - Building such agents from scratch is possible but time-consuming and complex; hence, frameworks exist to ease the development.
    - Frameworks handle crucial functionalities like prompting, memory management, tool integration, and monitoring.

Categories of Agent Frameworks: - 

    Coding based Frameworks: Require developers to write code for agent development - 

        LangChain: Simple, open-source, ideal for single-agent workflows and simple tasks. Supports multi-LLMs and tool integration.

        LangGraph: Built on LangChain, supports complex, multi-agent workflows with graph-based control flow, scheduling, and memory capabilities.

        Crew AI: Focused on multi-agent architectures working as a team to achieve shared goals.

        Google ADK: Modular and model-agnostic framework tightly integrated with Google ecosystem and Gemini LLM.

        Autogen (Microsoft): Multi-agent AI apps with autonomous and human collaboration, best suited for Microsoft ecosystem.

        Versal AI SDK: A TypeScript-based software development kit ideal for building AI agents in web applications.




No-Code/Low-Code Frameworks: Allow creating agents through configuration without coding - 

    N8N: Popular for automation workflows in sales, marketing, and business operations. Supports human-in-the-loop feedback, ideal for non-technical users to build visual workflows.


Framework Selection Guidelines -

    Use LangChain for simpler, single-agent applications requiring fewer steps.
    
    Choose LangGraph, Crew AI, or Autogen for multi-agent, complex, and production-grade workflows with advanced autonomous functionalities.
    
    For business and tool automation with minimal coding, use N8N.
    
    Pick Google ADK if operating heavily within the Google ecosystem, and Autogen if you are using Microsoft services.
    
    Select Versal AI SDK for TypeScript-based web applications requiring agentic AI.