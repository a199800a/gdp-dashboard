import streamlit as st

st.title("🚦 红绿灯最简工具")

st.write("上传截图 → 自动输出固定模板")

img = st.file_uploader("上传图片")

if img:
    st.image(img)

    st.markdown("## 🚦 红绿灯")
    st.write("🟡 黄灯（震荡结构）")

    st.markdown("## 🧠 状态")
    st.write("热度：中高")
    st.write("结构：小单偏强")
    st.write("阶段：震荡期")

    st.markdown("## 🎯 三选结构")
    st.write("1️⃣ 小单")
    st.write("2️⃣ 小双")
    st.write("3️⃣ 大单")

    st.markdown("## 💡 一句话总结")
    st.write("当前为小结构主导震荡")
