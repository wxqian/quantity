"""
QTF AI Integration Layer
AI Agent 层：LLM 集成和策略生成
"""

from qtf.ai.generator import CodeGenerator
from qtf.ai.prompts import PromptManager

__all__ = [
    "CodeGenerator",
    "PromptManager",
]
