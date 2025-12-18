import streamlit as st
import random
import time

def generate_tree(height):
    # 树顶
    tree_str = " " * (height - 1) + "⭐" + "\n"
    
    # 树身
    for i in range(height):
        # 每一行随机加入一些装饰物
        row = ""
        for _ in range(2 * i + 1):
            if random.random() < 0.2:
                row += random.choice(["🔴", "🟡", "🔵", "❄️"])
            else:
                row += "🎄"
        tree_str += " " * (height - i - 1) + row + "\n"
    
    # 树干
    trunk_width = height // 3 if height > 3 else 1
    for _ in range(2):
        tree_str += " " * (height - trunk_width // 2 - 1) + "🪵" * trunk_width + "\n"
    
    return tree_str

# Streamlit 网页设置
st.set_page_config(page_title="我的 Python 圣诞树", page_icon="🎄")
st.title("🎄 程序员的圣诞礼遇")

# 侧边栏交互
height = st.sidebar.slider("选择圣诞树的高度", 5, 20, 10)
speed = st.sidebar.slider("彩灯闪烁速度 (秒)", 0.5, 3.0, 1.0)

# 动态刷新容器
placeholder = st.empty()

st.balloons() # 撒花特效

# 模拟动态闪烁
while True:
    with placeholder.container():
        tree = generate_tree(height)
        st.code(tree, language=None)
        st.caption("提示：每隔几秒，树上的装饰会自动更换位置哦！")
    time.sleep(speed)
