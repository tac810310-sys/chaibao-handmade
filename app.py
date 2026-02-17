import streamlit as st
from PIL import Image
import requests

# --- 1. 網頁設定 (Page Config) ---
st.set_page_config(
    page_title="柴寶手作 | 招財甜點專賣",
    page_icon="🍬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. 視覺美化 CSS (裝修工程) ---
st.markdown("""
    <style>
    /* 全站背景：淡奶油色，看了就想吃甜點 */
    .stApp {
        background-color: #FFFDF5;
        background-image: radial-gradient(#FFE0B2 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* 隱藏預設選單 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 標題樣式：深咖啡色，圓潤感 */
    h1 {
        color: #5D4037 !important;
        font-family: 'Microsoft JhengHei', sans-serif;
        text-align: center;
        font-weight: 800;
        text-shadow: 2px 2px 0px #FFCC80;
    }
    
    /* 副標題樣式 */
    h2, h3 {
        color: #E65100 !important;
        font-family: 'Microsoft JhengHei', sans-serif;
        font-weight: 600;
    }
    
    /* 商品卡片：加上陰影和圓角，像張精緻的菜單 */
    .product-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 2px solid #FFECB3;
        text-align: center;
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        border-color: #FF9800;
    }
    
    /* 按鈕美化：漸層橘色，像金元寶一樣亮眼 */
    div.stButton > button {
        background: linear-gradient(to bottom, #FF9800 5%, #F57C00 100%);
        background-color: #FF9800;
        border-radius: 20px;
        border: 2px solid #E65100;
        display: inline-block;
        cursor: pointer;
        color: #ffffff;
        font-family: 'Microsoft JhengHei', sans-serif;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 24px;
        text-decoration: none;
        width: 100%;
        box-shadow: 0px 4px 0px #BF360C;
    }
    div.stButton > button:active {
        position: relative;
        top: 4px;
        box-shadow: 0px 0px 0px #BF360C;
    }
    
    /* 輸入框美化 */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #FFCC80;
    }
    
    /* 成功訊息背景 */
    .stSuccess {
        background-color: #E8F5E9;
        border-left: 5px solid #2E7D32;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 頂部 Hero Section (LOGO 與 標語) ---
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    try:
        # 顯示你的 LOGO
        image = Image.open("logo.png") 
        st.image(image, use_container_width=True) 
    except:
        st.header("🐕 柴寶手作") # 如果找不到圖的備案

st.markdown("<h3 style='text-align: center; margin-top: -20px; color: #8D6E63 !important;'>✨ 一口甜甜．財運連連 ✨</h3>", unsafe_allow_html=True)

st.write("") # 空行
st.markdown("---") # 分隔線

# --- 4. 品牌故事 (Story) ---
st.markdown("### 🐕 關於柴寶手作")
st.info(
    """
    這是一個由 **黑柴「福祿」** 與 **喜鵲「喜寶」** 共同守護的美味小舖。
    
    媽媽堅持純手工製作，嚴選天然麥芽與黑糖，慢火熬煮，不添加化學成分。
    每一口都是家的味道，每一口都帶著滿滿的財氣與祝福。
    
    **「用最好的食材，款待最重要的人。」**
    """
)

st.write("") 

# --- 5. 美味展示區 (Products - Card Style) ---
st.markdown("### 🍬 熱銷財寶 (點心介紹)")

c1, c2 = st.columns(2)

with c1:
    # 使用 HTML 語法來做漂亮的卡片
    st.markdown("""
    <div class="product-card">
        <div style="font-size: 50px;">🥜</div>
        <h4>麥芽芝麻糖</h4>
        <p style="color: #666; font-size: 14px;">嚴選黑芝麻 x 不黏牙麥芽<br>香氣濃郁，長輩最愛</p>
        <h3 style="color: #D84315 !important;">NT$ 200</h3>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="product-card">
        <div style="font-size: 50px;">☁️</div>
        <h4>好運雪Q餅</h4>
        <p style="color: #666; font-size: 14px;">像雲朵般的綿密口感<br>鹹甜交織，一口接一口</p>
        <h3 style="color: #D84315 !important;">NT$ 180</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

# --- 6. 訂購表單 (Order Form) ---
st.markdown("### 📝 立即把財寶帶回家")
st.write("👇 請填寫下方訂購單，媽媽收到後會盡快與您聯繫確認！")

with st.form(key='order_form'):
    # 分欄位讓表單看起來比較整齊
    f1, f2 = st.columns(2)
    with f1:
        name = st.text_input("您的稱呼 (必填)", placeholder="例如：王小明")
    with f2:
        phone = st.text_input("聯絡電話 (必填)", placeholder="例如：0912-345-678")
    
    line_id = st.text_input("LINE ID (選填，方便聯繫)")
    
    st.markdown("**🛒 選擇商品數量**")
    
    q1, q2 = st.columns(2)
    with q1:
        qty_sesame = st.number_input("🥜 麥芽芝麻糖 (包)", min_value=0, value=1, step=1)
    with q2:
        qty_cookie = st.number_input("☁️ 好運雪Q餅 (包)", min_value=0, value=0, step=1)
    
    delivery_method = st.radio(
        "🚚 取貨方式：",
        ("7-11 店到店 (+60元)", "全家 店到店 (+60元)", "面交自取 (台南)")
    )
    
    notes = st.text_area("備註事項", placeholder="例如：我要送禮，請幫我附提袋...")
    
    # 送出按鈕 (CSS 已經幫它美化過了)
    submit_button = st.form_submit_button(label='🚀 確認訂單')

# --- 7. 送出後的邏輯 ---
if submit_button:
    if not name or not phone:
        st.error("❌ 請記得填寫「稱呼」與「電話」，不然找不到人喔！")
    else:
        total_price = (qty_sesame * 200) + (qty_cookie * 180)
        
        order_data = {
            "name": name,
            "phone": phone,
            "line_id": line_id,
            "qty_sesame": qty_sesame,
            "qty_cookie": qty_cookie,
            "total_price": total_price,
            "notes": notes,
            "delivery": delivery_method
        }
        
        with st.spinner("📦 正在把訂單傳送給柴寶店長..."):
            try:
                # 你的 Apps Script 網址
                gas_url = "https://script.google.com/macros/s/AKfycbzcSRl5tRsNqRvXhrtwFfT3ebS23AsouM2WIKW1EZhROWdFgmCr_N4mywo9rV_1ap8/exec" 
                
                response = requests.post(gas_url, json=order_data)
                
                if response.status_code == 200:
                    st.success(f"✅ 訂單已送出！謝謝 {name} 的支持！")
                    st.balloons()
                    
                    st.markdown("""
                    <div style="background-color: #FFF; padding: 20px; border-radius: 10px; border: 2px dashed #FF9800;">
                        <h3 style="text-align: center;">📜 訂單明細</h3>
                        <ul>
                            <li><b>麥芽芝麻糖：</b> {} 包</li>
                            <li><b>好運雪Q餅：</b> {} 包</li>
                        </ul>
                        <hr>
                        <h2 style="text-align: center; color: #D32F2F;">💰 總金額：NT$ {}</h2>
                        <p style="text-align: center; color: #666;">我們將盡快透過電話或 LINE 聯繫您出貨！</p>
                    </div>
                    """.format(qty_sesame, qty_cookie, total_price), unsafe_allow_html=True)
                    
                else:
                    st.error("連線發生錯誤，請截圖此畫面傳給我們！")
            except Exception as e:
                st.error(f"傳送失敗：{e}")