import streamlit as st
from PIL import Image
import requests

# --- 1. 網頁設定 (Page Config) ---
st.set_page_config(
    page_title="柴寶手作 | 招財甜點專賣",
    page_icon="🍬",  # 之後可以換成你的 LOGO 小圖
    layout="centered", # 手機版用 centered 比較好看，不會太寬
    initial_sidebar_state="collapsed"
)

# --- 2. 自訂 CSS 樣式 (讓介面更漂亮) ---
# 隱藏 Streamlit 預設選單和 Footer，並調整字體大小
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 自訂標題樣式 */
    .title-text {
        font-size: 40px !important;
        font-weight: bold;
        color: #D35400; /* 暖橘色，呼應品牌色 */
        text-align: center;
        margin-bottom: 0px;
    }
    .slogan-text {
        font-size: 20px !important;
        color: #555555;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 20px;
        font-style: italic;
    }
    .product-card {
        background-color: #FEF9E7; /* 淡黃色背景 */
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #F5CBA7;
        text-align: center;
    }
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# --- 3. 頂部 Hero Section (LOGO 與 標語) ---
col1, col2, col3 = st.columns([1, 2, 1]) # 置中排版技巧

with col2:
    # 這裡預設會找一張叫 logo.png 的圖，如果找不到會顯示提示
    try:
        #image = Image.open("logo.png") 
        #st.image(image, use_column_width=True) # 實際上線請解開這兩行
        st.header("🖼️ (LOGO圖片區)") # 測試用佔位符
    except:
        st.warning("請在資料夾中放入 logo.png")

st.markdown('<p class="title-text">柴寶手作</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan-text">✨ 一口甜甜．財運連連 ✨</p>', unsafe_allow_html=True)

st.divider() # 分隔線

# --- 4. 品牌故事 (Story) ---
st.subheader("🐕 關於柴寶手作")
st.write(
    """
    這是一個由 **黑柴「福祿」** 與 **喜鵲「喜寶」** 共同守護的美味小舖。
    
    媽媽堅持純手工製作，嚴選天然麥芽與黑糖，慢火熬煮，不添加化學成分。
    每一口都是家的味道，每一口都帶著滿滿的財氣與祝福。
    
    **「用最好的食材，款待最重要的人。」**
    """
)

st.info("💡 **開幕慶！** 現在訂購滿 500 元，加送「招財試吃包」一份！")

st.divider()

# --- 5. 美味展示區 (Products) ---
st.subheader("🍬 熱銷財寶")

# 使用 Columns 建立並排的商品卡片
c1, c2 = st.columns(2)

with c1:
    # 商品 A
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.write("### 🥜 麥芽芝麻糖")
    st.caption("香濃芝麻 x 不黏牙麥芽")
    st.write("NT$ 200 / 包")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    # 商品 B
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.write("### ☁️ 好運雪Q餅")
    st.caption("像雲朵般的綿密口感")
    st.write("NT$ 180 / 包")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 6. 訂購表單 (Order Form) ---
st.subheader("📝 立即把財寶帶回家")
st.write("請填寫下方訂購單，媽媽收到後會盡快與您聯繫確認！")

with st.form(key='order_form'):
    # 客戶資料
    st.markdown("**1. 聯絡資訊**")
    name = st.text_input("您的稱呼 (必填)", placeholder="例如：王小明")
    phone = st.text_input("聯絡電話 (必填)", placeholder="例如：0912-345-678")
    line_id = st.text_input("LINE ID (選填，方便聯繫)")
    
    # 訂購數量
    st.markdown("**2. 選擇商品數量**")
    qty_sesame = st.number_input("🥜 麥芽芝麻糖 (包)", min_value=0, value=1, step=1)
    qty_cookie = st.number_input("☁️ 好運雪Q餅 (包)", min_value=0, value=0, step=1)
    
    # 取貨方式
    st.markdown("**3. 取貨方式**")
    delivery_method = st.radio(
        "請選擇：",
        ("7-11 店到店 (+60元)", "全家 店到店 (+60元)", "面交自取 (台南)")
    )
    
    notes = st.text_area("備註事項", placeholder="例如：送禮用紙袋、不喜歡太甜...")
    
    # 送出按鈕
    submit_button = st.form_submit_button(label='🚀 確認送出訂單')

# --- 7. 送出後的邏輯 (正式串接 Google Sheets) ---
if submit_button:
    if not name or not phone:
        st.error("❌ 請記得填寫「稱呼」與「電話」，不然找不到人喔！")
    else:
        # 計算總金額
        total_price = (qty_sesame * 200) + (qty_cookie * 180)
        
        # 準備要傳送的資料 (JSON 格式)
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
        
        # 顯示處理中... (給客人一點儀式感)
        with st.spinner("📦 正在把訂單傳送給柴寶店長..."):
            try:
                # 這是你剛剛做好的 Apps Script 網址
                gas_url = "https://script.google.com/macros/s/AKfycbzcSRl5tRsNqRvXhrtwFfT3ebS23AsouM2WIKW1EZhROWdFgmCr_N4mywo9rV_1ap8/exec" 
                
                # 發送 POST 請求
                response = requests.post(gas_url, json=order_data)
                
                # 判斷是否成功
                if response.status_code == 200:
                    st.success(f"✅ 訂單已送出！謝謝 {name} 的支持！")
                    st.balloons() # 放氣球慶祝！
                    
                    st.write("---")
                    st.markdown(f"**訂單摘要：**")
                    st.write(f"- 麥芽芝麻糖：{qty_sesame} 包")
                    st.write(f"- 好運雪Q餅：{qty_cookie} 包")
                    st.markdown(f"### 💰 預計總金額：NT$ {total_price}")
                    st.write("我們將會盡快透過電話或 LINE 與您聯繫出貨事宜。")
                else:
                    st.error("連線發生錯誤，請截圖此畫面傳給我們！")
            except Exception as e:
                st.error(f"傳送失敗，請檢查網路或是稍後再試：{e}")