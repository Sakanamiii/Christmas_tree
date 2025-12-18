import streamlit as st
import random
import time

def generate_beautiful_tree(height, top_message=""):
    tree_lines = []

    # 树顶消息 (居中显示)
    if top_message:
        message_len = len(top_message)
        # 简单居中，考虑中文字符宽度
        padding = (2 * height - 1 - message_len * 2) // 2 # 估算中文占据2个英文字符宽度
        tree_lines.append(" " * max(0, padding) + top_message)
        tree_lines.append(" " * (height - 1) + "✨") # 在消息下加个星星
    else:
        tree_lines.append(" " * (height - 1) + "⭐") # 默认的树顶星星

    # 树身
    decorations = ["🔴", "🟡", "🔵", "🟣", "🟠", "🌟", "🔔", "🎁", "❄️", "✨"]
    
    for i in range(height):
        # 每一行加入更多“叶子”和随机装饰物
        row_content = ""
        for j in range(2 * i + 1):
            if random.random() < 0.25: # 增加装饰物密度
                row_content += random.choice(decorations)
            else:
                row_content += random.choice(["🌲", "🌳", "🌿"]) # 使用更多绿色系符号
        
        tree_lines.append(" " * (height - i - 1) + row_content)
    
    # 树干
    trunk_width = height // 4 if height > 4 else 2 # 调整树干宽度
    if trunk_width % 2 == 0: # 确保树干宽度为奇数或偶数都能居中
        trunk_width += 1 if height % 2 != 0 else 0 # 简单调整居中
    
    for _ in range(max(2, height // 5)): # 树干高度
        trunk_padding = (2 * height - 1 - trunk_width) // 2
        tree_lines.append(" " * trunk_padding + "🟫" * trunk_width) # 使用棕色方块表示树干
    
    return "\n".join(tree_lines)

# Streamlit 网页设置
st.set_page_config(page_title="🎄 余周周爱极点专属圣诞树 🎄", page_icon="💖")
st.title("💖 专属定制：余周周爱极点圣诞树 💖")
st.markdown("---")

# 侧边栏交互
height = st.sidebar.slider("选择圣诞树的高度", 8, 25, 15)
speed = st.sidebar.slider("彩灯闪烁速度 (秒)", 0.3, 2.0, 0.8)

st.sidebar.markdown("---")
st.sidebar.info("这是一棵为你和极点定制的圣诞树，快分享给TA吧！")

# 动态刷新容器
placeholder = st.empty()

st.balloons() # 撒花特效

# 模拟动态闪烁
while True:
    with placeholder.container():
        st.markdown(f"### ✨ `{random.choice(['余周周', '极点'])} 祝你圣诞快乐！` ✨") # 动态显示祝福
        tree = generate_beautiful_tree(height, top_message="余周周爱极点")
        st.code(tree, language=None)
        st.markdown("---")
        st.caption("🎅 愿你拥有一个充满爱与惊喜的节日！")
    time.sleep(speed)

