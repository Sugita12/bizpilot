import streamlit as st

st.title("BizPilot - 経営ナビ")

data = {
    "売上": 1200000,
    "利益率": 0.18,
    "現預金": 5000000,
    "新患者数": 45,
    "リピート率": 0.72
}

st.header("📊 経営ダッシュボード")
st.write(data)

st.header("🤖 AI経営コメント")

if st.button("分析する"):
    st.write("総合評価：B")
    st.write("良い点：売上は安定しています")
    st.write("課題：リピート率改善余地あり")
    st.write("施策：再診フォロー強化")

st.header("💬 経営相談")

q = st.text_input("相談してください")

if q:
    st.write("この内容はKPIに基づき検討が必要です")
