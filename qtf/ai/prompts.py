"""
Prompt 管理器 (Prompt Manager)
管理生成量化策略的 Prompt 模板
"""

from typing import Dict, Any, Optional


# 策略生成系统提示
STRATEGY_SYSTEM_PROMPT = """
你是一个专业的量化策略开发专家。你的任务是根据用户的自然语言描述生成 Python 交易策略代码。

生成的策略需要继承 BaseStrategy 类，并实现以下方法：
- on_init(): 策略初始化
- on_start(): 策略启动
- on_stop(): 策略停止  
- on_bar(bar): 处理K线数据

你可以使用以下接口：
- self.buy(symbol, price, volume): 买入
- self.sell(symbol, price, volume): 卖出
- self.cancel(order_id): 撤单
- self.context.get_position(symbol): 获取持仓
- self.context.get_account(): 获取账户
- self.context.log(message): 记录日志

请确保生成的代码：
1. 语法正确
2. 逻辑清晰
3. 包含适当的风控措施
4. 有清晰的注释
"""

# 策略优化提示
REFINE_PROMPT = """
根据以下反馈优化策略代码：

原始代码:
{code}

用户反馈:
{feedback}

请在保持原有功能的基础上进行优化。
"""


class PromptManager:
    """
    Prompt 模板管理器
    """
    
    def __init__(self):
        self._templates: Dict[str, str] = {
            "strategy_system": STRATEGY_SYSTEM_PROMPT,
            "refine": REFINE_PROMPT,
        }
    
    def get_template(self, name: str) -> Optional[str]:
        """获取模板"""
        return self._templates.get(name)
    
    def add_template(self, name: str, template: str) -> None:
        """添加模板"""
        self._templates[name] = template
    
    def format_template(
        self,
        name: str,
        **kwargs: Any
    ) -> Optional[str]:
        """格式化模板"""
        template = self._templates.get(name)
        if template:
            return template.format(**kwargs)
        return None
    
    def build_strategy_prompt(
        self,
        description: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, str]:
        """
        构建策略生成 prompt
        Args:
            description: 策略描述
            context: 额外上下文
        Returns:
            Dict: system 和 user prompt
        """
        user_prompt = f"请根据以下描述生成交易策略：\n\n{description}"
        
        if context:
            user_prompt += f"\n\n额外信息：\n{context}"
        
        return {
            "system": self._templates["strategy_system"],
            "user": user_prompt,
        }
