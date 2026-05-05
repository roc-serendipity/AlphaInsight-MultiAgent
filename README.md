# AlphaInsight-MultiAgent
# AlphaInsight: Multi-Agent Financial Intelligence & Decision System

AlphaInsight 是一款基于 **Multi-Agent Debate (多 Agent 博弈)** 架构的深度金融投研决策系统。它通过多维度的感知 Agents 和递归式的逻辑校准环，将非结构化市场数据转化为高置信度的投资洞察。

## 🌟 核心痛点解决
- **信息噪音过滤**: 处理全球多语种、多模态（PDF/图表/语音）数据，实现信息无损转化。
- **消除模型偏见**: 通过“看多-看空”双向 Agent 辩论机制，最大限度降低单一 LLM 的幻觉与预设偏见。
- **长链逻辑推演**: 针对复杂指令（如：地缘政治对特定供应链的影响）进行 5-10 步的深度推理。

## 🧠 技术架构与 Token 消耗模型
本项目为了追求极致的逻辑严密性，设计了高强度的计算链路，这也是系统 Token 需求量大的核心原因：
1. **Long-Context Scanning (128K+)**: 每次分析任务都会全量扫描数千份行业文档，确保不遗漏关键脚注细节。
2. **Recursive Debate Loop (递归博弈)**: 激进与保守 Agent 针对同一结论进行 3-5 轮对抗，每一轮都会调用历史数据进行 CoT（思维链）回溯，单次分析任务的推理步数显著超过常规聊天机器人。
3. **High-Frequency Monitoring**: 7x24 小时高并发扫描全球 API，日均处理数据吞吐量支撑起 **1.2 亿+ Token** 的消耗规模。

## 🛠️ 快速开始
1. 安装依赖: `pip install -r requirements.txt`
2. 运行演示看板: `streamlit run app.py`
