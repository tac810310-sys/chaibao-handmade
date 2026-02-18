import streamlit as st
import base64
import os

# --- 1. 網頁基礎配置 ---
st.set_page_config(
    page_title="柴寶手作 | 一口甜甜．財寶連連",
    page_icon="🐕",
    layout="centered"
)

# --- 2. 圖片處理函數 ---
def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 3. 視覺樣式 (輸入框白底修復版) ---
st.markdown("""
    <style>
    /* 1. 全站背景 */
    .stApp { background-color: #FFFDF5; }
    
    /* 2. 強制全站字體 */
    html, body, p, div, span, h1, h2, h3, h4, h5, h6, label, input, textarea { 
        font-family: 'Microsoft JhengHei', '微軟正黑體', sans-serif !important; 
    }

    /* === 關鍵修復：強制所有文字顯色 (無視深色模式) === */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, div {
        color: #4E342E !important;
    }

    /* === 🌟 輸入框大修復：強制背景變白，文字變黑 🌟 === */
    /* 針對 單行輸入框(TextInput) 與 數字輸入框(NumberInput) 與 多行輸入(TextArea) */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        background-color: #FFFFFF !important; /* 強制背景白色 */
        color: #000000 !important;            /* 強制文字黑色 */
        border: 1px solid #D7CCC8 !important; /* 加個邊框比較明顯 */
    }
    
    /* 針對 輸入框的標題 (Label) */
    .stTextInput label, .stNumberInput label, .stTextArea label, .stRadio label {
        color: #3E2723 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* 針對 選項按鈕 (Radio Button) */
    .stRadio div[role='radiogroup'] label div p {
        color: #4E342E !important;
        font-size: 16px !important;
    }

    /* === 分頁標籤 === */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; width: 100%; }
    .stTabs [data-baseweb="tab"] {
        height: 70px; font-size: 20px !important; font-weight: bold; flex: 1;
        background-color: #FFF3E0; border-radius: 15px 15px 0 0; 
        color: #5D4037 !important;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #FF9800 !important; color: white !important; 
    }

    /* === 第一頁樣式 === */
    .mom-box { background-color: #FAFAFA; border: 2px dashed #BCAAA4; padding: 30px; border-radius: 20px; margin-bottom: 30px; }
    .story-box { background-color: rgba(255, 255, 255, 0.9); padding: 25px; border-radius: 15px; border-left: 8px solid #FFB300; margin: 20px 0; }
    .five-elements { background-color: #FFF8E1; padding: 30px; border-radius: 20px; border: 2px dashed #FFB74D; margin-top: 30px; text-align: center; }
    .story-text { font-size: 19px !important; line-height: 1.8 !important; color: #5D4037 !important; }

    /* === 第二頁：橘色卡片 === */
    .orange-card {
        background-color: #FFCC80;
        border-radius: 30px;
        padding: 25px;
        margin-bottom: 40px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border: 2px solid #FFA726;
        color: #3E2723;
        text-align: center;
    }
    .card-title { font-size: 28px !important; font-weight: 900 !important; margin-bottom: 15px; letter-spacing: 2px; color: #000000 !important; }
    .spotlight-box {
        background: radial-gradient(circle, #FFFFFF 30%, #E0E0E0 100%);
        padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 20px;
        border: 1px solid #B0BEC5;
    }
    .product-img { width: 100%; max-width: 300px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    .card-desc { font-size: 18px; line-height: 1.7; margin-bottom: 15px; font-weight: 500; text-align: justify; padding: 0 10px; color: #3E2723 !important; }
    
    /* 詩句樣式 */
    .card-poem { font-size: 20px; font-weight: 900; line-height: 1.6; color: #1A237E !important; margin-top: 10px; }

    /* 手機版調整 */
    @media (max-width: 768px) {
        .card-poem { font-size: 16px !important; line-height: 1.5 !important; }
        .card-desc { font-size: 16px !important; }
        .card-title { font-size: 24px !important; }
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. 頁首 Logo ---
col_l, col_m, col_r = st.columns([1, 4, 1])
with col_m:
    try: st.image("logo.png", use_container_width=True)
    except: st.title("🐕 柴寶手作")

st.markdown("<h3 style='text-align: center; color: #8D6E63; margin-top: -10px;'>✨ 一口甜甜．財寶連連 ✨</h3>", unsafe_allow_html=True)

# --- 5. 三大分頁 ---
tab1, tab2, tab3 = st.tabs(["📖 品牌故事", "🛒 美味下單", "💬 暖心留言"])

# ==========================================
# 分頁 1：品牌故事
# ==========================================
with tab1:
    st.markdown("### 👩‍🍳 柴寶緣起：媽媽的私房手藝")
    st.markdown("""
    <div class="mom-box">
        <h4 style="color: #5D4037; text-align: center; font-size: 26px; margin-bottom: 10px;">從替家人把關，到大家的口耳相傳</h4>
        <hr style="border: 0.5px solid #E0E0E0;">
        <p class="story-text">
            起初，這只是一份媽媽對家人的私房愛。<br><br>
            因為覺得外面的糖果價格不斐，成分又標示不清，熱愛料理的媽媽心想：<b>「既然家人愛吃，那就自己動手做吧！用最好的料，吃得才安心。」</b><br><br>
            當第一鍋「黑芝麻糖」出爐，那股濃郁的香氣立刻征服了左鄰右舍。大家一吃成主顧，紛紛驚呼：「這比外面的還好吃！」在親友的熱情推坑下，<b>【柴寶手作】</b>就這樣在大家的期待與祝福中，溫馨誕生了。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🐶 巷弄小太陽：福祿 (Lulu)")
    lc1, lc2 = st.columns(2)
    with lc1:
        try: st.image("lulu_q.png", caption="Q版店長祿祿", use_container_width=True)
        except: st.info("缺少 lulu_q.png")
    with lc2:
        try: st.image("lulu_real.png", caption="帥氣祿祿本尊", use_container_width=True)
        except: st.info("缺少 lulu_real.png")
    
    st.markdown("""
    <div class="story-box">
        <h4 style="color: #E65100; margin-bottom: 10px;">☀️ 溫暖的天使柴</h4>
        <p class="story-text">
            鄰居們常說：<b>「看到祿祿，心情就好了一半。」</b><br>
            他是大家公認的「天使柴」。每當有人經過，他總是瞇著眼、開著飛機耳，用全身力氣搖著尾巴迎接。那種純真無邪的笑容，有一種讓人<b>瞬間忘記煩惱的魔力</b>。
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🐦 用愛重生：喜寶 (Bobo)")
    bc1, bc2 = st.columns(2)
    with bc1:
        try: st.image("bobo_q.png", caption="Q版喜寶", use_container_width=True)
        except: st.info("缺少 bobo_q.png")
    with bc2:
        try: st.image("bobo_real.png", caption="喜寶本尊", use_container_width=True)
        except: st.info("缺少 bobo_real.png")

    st.markdown("""
    <div class="story-box" style="border-left: 8px solid #8D6E63;">
        <h4 style="color: #6D4C41; margin-bottom: 10px;">🐦 用愛灌溉的奇蹟</h4>
        <p class="story-text">
            喜寶是媽媽從鳥販手中救下的孩子。當時牠受了傷，瑟瑟發抖。媽媽心疼收編後，這個孤僻的小傢伙把所有的溫柔都留給了媽媽。<br>
            廚房忙時，牠會撒嬌叫<b>「咪～」</b>；聽到媽媽回家，牠總是第一個大叫迎接。<b>牠的叫聲，是我們家最安心的信號。</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="five-elements">
        <h4 style="color: #E65100; font-size: 24px;">✨ 五行相生．財寶滾滾</h4>
        <p class="story-text">
            黑柴屬水，水生木（柴），木生火（手作），火生土（財庫），土生金（財寶）。<br>
            福祿的笑容帶來了「人氣」，喜寶的重生帶來了「福氣」。<br>
            這就是<b>【柴寶手作】</b>的初心——我們賣的不只是甜點，更是一份被愛包圍的幸福好運。
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 分頁 2：美味下單
# ==========================================
with tab2:
    st.markdown("### ✨ 心靈祝禱系列")
    st.write("每一份點心，皆含有一份人生的祝福。")

    img_sesame = get_base64_image("sesame.png")
    img_matcha = get_base64_image("matcha.png")
    img_strawberry = get_base64_image("strawberry.png")

    # --- 1. 墨玉生輝 ---
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">寒梅破曙 - 墨玉生輝</div>
        <div class="spotlight-box">
            <img src="data:image/png;base64,{img_sesame}" class="product-img" alt="墨玉生輝">
        </div>
        <div class="card-desc">
            麥芽與黑糖，混合著芝麻，枸杞，腰果與核桃仁，在恰當的火候上細心慢熬，猶如寒冬熬骨。<br>
            完成後芝麻裹著糖衣，變成了發亮的墨玉，如同酷寒過後的梅花，耀眼綻放。
        </div>
        <div class="card-poem">
            "酸甜苦辣人生路，運程總有起伏時。"<br>
            "願以糖衣化心苦，望爾莫忘初心路。"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. 靜谷尋心 ---
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">幽靜鳥語 - 靜谷尋心</div>
        <div class="spotlight-box">
            <img src="data:image/png;base64,{img_matcha}" class="product-img" alt="靜谷尋心">
        </div>
        <div class="card-desc">
            棉花糖的甜，中和了抹茶中些許的苦澀，清香又清甜。入口的甜，舌上的清香，喉中的回甘。猶如身在森林中，放鬆緊張的心情，讓自己短暫的休息。迎接接下來的挑戰。
        </div>
        <div class="card-poem">
            "忙忙碌碌過甲子，記家記外獨忘己。"<br>
            "願將此品送爾心，暫停世俗品香茗。"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3. 方寸留憶 ---
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">緋紅初見 - 方寸留憶</div>
        <div class="spotlight-box">
            <img src="data:image/png;base64,{img_strawberry}" class="product-img" alt="方寸留憶">
        </div>
        <div class="card-desc">
            棉花糖的甜，加上了草莓的酸甜，雖甜卻不膩。入口的酸甜，不停留在喉間，甜中的後韻，只留存心中。猶如初戀的酸甜美好，或許不是陪伴一生的佳人，但是卻是人生中最難忘的相遇，最美好的回憶。
        </div>
        <div class="card-poem">
            "相逢初在束髮年，臉羞耳紅意綿綿。"<br>
            "雖伴老年不是君，初憶願留此心間。"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 訂購單 ---
    st.write("---")
    st.markdown("### 📝 福氣訂購單")
    
    with st.form("order_form"):
        # 這些文字標籤已被強制修復為深色
        name = st.text_input("怎麼稱呼您？(必填)")
        phone = st.text_input("福氣專線 (電話)")
        
        st.markdown("**🛒 選擇祝福份數**")
        c1, c2, c3 = st.columns(3)
        q1 = c1.number_input("🖤 墨玉生輝", min_value=0)
        q2 = c2.number_input("🌿 靜谷尋心", min_value=0)
        q3 = c3.number_input("🌸 方寸留憶", min_value=0)
        
        delivery = st.radio("🚚 取貨方式", ("7-11 店到店", "全家 店到店", "面交自取"))
        notes = st.text_area("想對媽媽說的悄悄話...")
        
        submit = st.form_submit_button("🚀 確認送出祝福訂單")
        
        if submit:
            if not name or not phone:
                st.error("❌ 請記得留下稱呼與電話喔！")
            else:
                total = (q1*200) + (q2*180) + (q3*180)
                st.balloons()
                st.success(f"✅ 訂單已送出！總金額：NT$ {total}")
                st.info("您的福氣已發貨，請靜待好事發生。")

# ==========================================
# 分頁 3：暖心留言
# ==========================================
with tab3:
    st.markdown("### 💬 暖心留言板")
    st.write("歡迎留下您對媽媽、福祿或喜寶的悄悄話。")
    with st.form("msg_form"):
        m_name = st.text_input("您的暱稱")
        m_msg = st.text_area("想說的話...")
        if st.form_submit_button("💌 送出留言"):
            st.success("收到您的溫暖留言了！✨")