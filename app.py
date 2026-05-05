import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="AlphaInsight Dashboard", layout="wide")

st.title("🚀 AlphaInsight: Agent 协作监控仪表盘")

# 模拟实时数据
st.sidebar.header("系统实时状态")
st.sidebar.metric("今日 Token 消耗", "135,402,810", "+15.2%")
st.sidebar.metric("当前 QPS", "45", "Peak")

tab1, tab2 = st.tabs(["Agent 协作日志", "Token 消耗分析"])

with tab1:
    st.subheader("🤖 多 Agent 异步博弈监控")
    log_area = st.empty()
    logs = [
        "[Perception] 正在解析 2024 半导体行业趋势 PDF (150 pages)...",
        "[Reasoning] 识别到 12 处逻辑潜在关联点...",
        "[Bull Agent] 提出：AI 算力侧毛利具有极强防御性。",
        "[Bear Agent] 质疑：推理侧竞争加剧，逻辑不成立。",
        "[System] 触发第 2 轮递归校准，调用历史数据对比...",
        "[Auditor] 正在融合最终深度决策报告..."
    ]
    current_logs = ""
    for log in logs:
        current_logs += log + "\n"
        log_area.code(current_logs)
        time.sleep(0.8)

with tab2:
    st.subheader("📊 Token 消耗分布 (by Component)")
    chart_data = pd.DataFrame({
        'Component': ['长文本解析', '多 Agent 博弈', '实时监控', '报告生成'],
        'Percentage': [45, 35, 15, 5]
    })
    st.bar_chart(chart_data.set_index('Component'))
    st.info("注：由于采用了 3 轮递归博弈机制，博弈环节 Token 消耗量较常规单 Agent 提升了 400%。")
