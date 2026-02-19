import streamlit as st
import base64
import os
import requests  # <--- 用來傳送資料給 Google Apps Script

# --- 1. 網頁基礎配置 ---
st.set_page_config(
    page_title="柴寶手作 | 一口甜甜．財運連連",
    page_icon="🍬",
    layout="centered"
)

# --- 2. 圖片處理函數 ---
def get_base64_image(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- 3. CSS 視覺樣式 (包含第一頁排版、手機修復、深色模式修復) ---
st.markdown("""
    <style>
    /* 1. 全站背景 */
    .stApp { background-color: #FFFDF5; }
    
    /* 2. 強制全站字體 */
    html, body, p, div, span, h1, h2, h3, h4, h5, h6, label, input, textarea { 
        font-family: 'Microsoft JhengHei', '微軟正黑體', sans-serif !important; 
    }

    /* === 強制所有文字顯色 (無視深色模式) === */
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, div {
        color: #4E342E !important;
    }

    /* === 輸入框大修復：強制白底黑字 === */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #D7CCC8 !important;
    }
    .stTextInput label, .stNumberInput label, .stTextArea label, .stRadio label {
        color: #3E2723 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
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

    /* === 第一頁樣式 (確認找回來的完美版) === */
    .mom-box { 
        background-color: #FAFAFA; border: 2px dashed #BCAAA4; padding: 30px; 
        border-radius: 20px; margin-bottom: 30px; 
    }
    .story-box { 
        background-color: rgba(255, 255, 255, 0.9); padding: 25px; 
        border-radius: 15px; border-left: 8px solid #FFB300; margin: 20px 0; 
    }
    .five-elements { 
        background-color: #FFF8E1; padding: 30px; border-radius: 20px; 
        border: 2px dashed #FFB74D; margin-top: 30px; text-align: center; 
    }
    .story-text { 
        font-size: 19px !important; line-height: 1.8 !important; 
        color: #5D4037 !important; 
    }

    /* === 第二頁：橘色卡片 === */
    .orange-card {
        background-color: #FFCC80;
        border-radius: 30px; padding: 25px; margin-bottom: 40px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.15); border: 2px solid #FFA726;
        color: #3E2723; text-align: center;
    }
    .card-title { font-size: 28px !important; font-weight: 900 !important; margin-bottom: 15px; letter-spacing: 2px; color: #000000 !important; }
    .spotlight-box {
        background: radial-gradient(circle, #FFFFFF 30%, #E0E0E0 100%);
        padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 20px;
        border: 1px solid #B0BEC5;
    }
    .product-img { width: 100%; max-width: 300px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    .card-desc { font-size: 18px; line-height: 1.7; margin-bottom: 15px; font-weight: 500; text-align: justify; padding: 0 10px; color: #3E2723 !important; }
    .card-poem { font-size: 20px; font-weight: 900; line-height: 1.6; color: #1A237E !important; margin-top: 10px; }

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
st.markdown("<h3 style='text-align: center; color: #8D6E63; margin-top: -10px;'>✨ 一口甜甜．財運連連 ✨</h3>", unsafe_allow_html=True)

# --- 5. 三大分頁 ---
tab1, tab2, tab3 = st.tabs(["📖 關於柴寶", "🛒 美味下單", "💬 暖心留言"])

# ==========================================
# 分頁 1：品牌故事 (完整補回取名故事！)
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
    
    # --- 這裡完美補回您遺失的重要標題 ---
    st.markdown("### 🐾 取名故事：兩位毛孩的溫柔守護")
    st.markdown("<p class='story-text' style='margin-bottom: 20px;'>「柴寶」這個名字，這不是一個隨機的名字，而是我們家兩位「小小守護神」——黑柴「福祿」與喜鵲「喜寶」的縮寫。」。</p>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #8D6E63; margin-top: 10px;'>🐶 巷弄小太陽：福祿 (Lulu)</h4>", unsafe_allow_html=True)
    lc1, lc2 = st.columns(2)
    with lc1:
        try: st.image("lulu_q.png", caption="Q版可愛的祿祿", use_container_width=True)
        except: st.info("缺少 lulu_q.png")
    with lc2:
        try: st.image("lulu_real.png", caption="帥氣英俊的祿祿", use_container_width=True)
        except: st.info("缺少 lulu_real.png")
    
    st.markdown("""
    <div class="story-box">
        <h4 style="color: #E65100; margin-bottom: 10px;">☀️ 溫暖的天使柴</h4>
        <p class="story-text">
            鄰居們常說：<b>「看到祿祿，心情就好了一半。」</b><br>
            他是大家公認的「天使柴」。脾氣好到不可思議。每當有人經過，他總是瞇著眼、開著飛機耳，用全身力氣搖著尾巴迎接，彷彿在熱情地說：「歡迎來我們家玩！」。那種純真無邪的笑容，有一種讓人<b>瞬間忘記煩惱的魔力</b>。
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #8D6E63; margin-top: 20px;'>🐦 因愛重生的孩子：喜寶 (Bobo)</h4>", unsafe_allow_html=True)
    bc1, bc2 = st.columns(2)
    with bc1:
        try: st.image("bobo_q.png", caption="Q版可愛的喜寶", use_container_width=True)
        except: st.info("缺少 bobo_q.png")
    with bc2:
        try: st.image("bobo_real.png", caption="霸氣傲嬌的喜寶", use_container_width=True)
        except: st.info("缺少 bobo_real.png")

    st.markdown("""
    <div class="story-box" style="border-left: 8px solid #8D6E63;">
        <h4 style="color: #6D4C41; margin-bottom: 10px;">🐦 用愛灌溉的奇蹟</h4>
        <p class="story-text">
            喜寶的故事，是從一個鳥販擁擠的籠子裡開始的。當時牠還很小，腳受了傷，縮在角落瑟瑟發抖。媽媽看了心疼，心想：「這孩子如果野放，肯定活不了。」便毅然決然把牠帶回家照顧。或許是知道自己被救贖了，這個原本孤僻的小傢伙，把所有的溫柔都留給了媽媽。<br>
            當媽媽在廚房忙碌時，牠會在一旁發出軟糯的**「咪～（媽咪）」撒嬌討肉吃；每當傍晚媽媽下班，只要「喀啦」**一聲鋁門打開，喜寶一定會第一個大叫迎接。牠的叫聲，是我們家最安心的信號。</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="five-elements">
        <h4 style="color: #E65100; font-size: 24px;">✨ 五行相生．財運滾滾</h4>
        <p class="story-text">
            黑柴屬水，水生木（柴），木生火（手作），火生土（財庫），土生金（財寶）。<br>
            福祿的笑容帶來了「人氣」，喜寶的重生帶來了「福氣」。<br>
            這就是<b>【柴寶手作】</b>的初心——我們賣的不只是甜點，更是一份被愛包圍的幸福好運。
        </p>
    </div>
    """, unsafe_allow_html=True)
# ==========================================
# 分頁 2：美味下單 (使用確認好的 GAS 連線)
# ==========================================
with tab2:
    st.markdown("### ✨ 暖心甜點系列")
    st.write("每一份點心，皆含有一份人生的祝福。")

    img_sesame = get_base64_image("sesame.png")
    img_matcha = get_base64_image("matcha.png")
    img_strawberry = get_base64_image("strawberry.png")

    # 卡片 1
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">墨玉生輝 - 麥芽芝麻糖</div>
        <div class="spotlight-box"><img src="data:image/png;base64,{img_sesame}" class="product-img"></div>
        <div class="card-desc">麥芽與黑糖，混合著芝麻，枸杞，腰果與核桃仁，在恰當的火候上細心慢熬，猶如寒冬熬骨。<br>完成後芝麻裹著糖衣，變成了發亮的墨玉，如同酷寒過後的梅花，耀眼綻放。</div>
        <div class="card-poem">"酸甜苦辣人生路，運程總有起伏時。"<br>"願以糖衣化心苦，望爾莫忘初心路。"</div>
    </div>
    """, unsafe_allow_html=True)

    # 卡片 2
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">靜谷尋心 - 抹茶雪Q餅</div>
        <div class="spotlight-box"><img src="data:image/png;base64,{img_matcha}" class="product-img"></div>
        <div class="card-desc">棉花糖的甜，中和了抹茶中些許的苦澀，清香又清甜。入口的甜，舌上的清香，喉中的回甘。猶如身在森林中，放鬆緊張的心情，讓自己短暫的休息。迎接接下來的挑戰。</div>
        <div class="card-poem">"忙忙碌碌過甲子，記家記外獨忘己。"<br>"願將此品送爾心，暫停世俗品香茗。"</div>
    </div>
    """, unsafe_allow_html=True)

    # 卡片 3
    st.markdown(f"""
    <div class="orange-card">
        <div class="card-title">方寸留憶 - 草莓雪Q餅</div>
        <div class="spotlight-box"><img src="data:image/png;base64,{img_strawberry}" class="product-img"></div>
        <div class="card-desc">棉花糖的甜，加上了草莓的酸甜，雖甜卻不膩。入口的酸甜，不停留在喉間，甜中的後韻，只留存心中。猶如初戀的酸甜美好，或許不是陪伴一生的佳人，但是卻是人生中最難忘的相遇，最美好的回憶。</div>
        <div class="card-poem">"相逢初在束髮年，臉羞耳紅意綿綿。"<br>"雖伴老年不是君，初憶願留此心間。"</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 📝 福氣訂購單")
    
    with st.form("order_form"):
        f1, f2 = st.columns(2)
        with f1: name = st.text_input("怎麼稱呼您？(必填)")
        with f2: phone = st.text_input("福氣專線 (電話)")
        
        line_id = st.text_input("Line ID (方便我們聯繫您)")
        
        st.markdown("**🛒 選擇祝福份數**")
        c1, c2, c3 = st.columns(3)
        q1 = c1.number_input("🖤 墨玉生輝 (1袋6入 / NT$50)", min_value=0)
        q2 = c2.number_input("🌿 靜谷尋心 (1袋5入 / NT$60)", min_value=0)
        q3 = c3.number_input("🌸 方寸留憶 (1袋5入 / NT$60)", min_value=0)
        
        delivery = st.radio("🚚 取貨方式", ("7-11 店到店", "全家 店到店", "面交自取"))
        notes = st.text_area("想對媽媽說的悄悄話...")
        
        submit = st.form_submit_button("🚀 確認送出祝福訂單")
        
        # --- 按下送出後的邏輯 (您剛剛確認成功的版本) ---
        if submit:
            if not name or not phone:
                st.error("❌ 請記得填寫「稱呼」與「電話」，不然找不到人喔！")
            else:
                total_price = (q1 * 50) + (q2 * 60) + (q3 * 60)
                
                order_data = {
                    "name": name,
                    "phone": phone,
                    "line_id": line_id,
                    "qty_moyu": q1,       # 墨玉生輝
                    "qty_jinggu": q2,     # 靜谷尋心
                    "qty_fangcun": q3,    # 方寸留憶
                    "total_price": total_price,
                    "notes": notes,
                    "delivery": delivery
                }                
                with st.spinner("📦 正在把訂單傳送給柴寶店長..."):
                    try:
                        # 您的 Apps Script 網址
                        gas_url = "https://script.google.com/macros/s/AKfycbzcSRl5tRsNqRvXhrtwFfT3ebS23AsouM2WIKW1EZhROWdFgmCr_N4mywo9rV_1ap8/exec" 
                        response = requests.post(gas_url, json=order_data)
                        
                        if response.status_code == 200:
                            st.balloons()
                            st.success(f"✅ 訂單已送出！謝謝 {name} 的支持！")
                            st.markdown(f"### 💰 預計總金額：NT$ {total_price}")
                            st.info("我們將會盡快透過電話或 LINE 與您聯繫出貨事宜。")
                        else:
                            st.error("連線發生錯誤，請截圖此畫面傳給我們！")
                    except Exception as e:
                        st.error(f"傳送失敗，請檢查網路或是稍後再試：{e}")

# ==========================================
# 分頁 3：暖心留言 (表單在上，留言在下版！)
# ==========================================
with tab3:
    st.markdown("### 💌 柴寶暖心留言牆")
    
    # 您的專屬留言板網址 
    msg_gas_url = "https://script.google.com/macros/s/AKfycbyZnAfV_8JX1sEgWQhkgKrkgU3UmllmJKTuC_LbBJ12ZdholFOI72lID17Ffr59Q-fMAA/exec"
    
    # 預先讀取 Q 版圖片
    img_mom_base64 = get_base64_image("mom_q.png")
    img_lubo_base64 = get_base64_image("lubo_q.png")
    
    # 產生圖片的 HTML (設定為絕對位置，貼在角落)
    mom_html = f'<img src="data:image/png;base64,{img_mom_base64}" style="position: absolute; top: 15px; right: 15px; width: 85px; z-index: 0; opacity: 0.95;">' if img_mom_base64 else ''
    lubo_html = f'<img src="data:image/png;base64,{img_lubo_base64}" style="position: absolute; bottom: 10px; left: 10px; width: 110px; z-index: 0; opacity: 0.95;">' if img_lubo_base64 else ''

    # --- 1. 溫馨介紹區塊 ---
    st.markdown("""
    <div style="background-color: #FFF3E0; border-radius: 20px; padding: 20px; border: 2px dashed #FFB74D; text-align: center; margin-bottom: 30px;">
        <h4 style="color: #E65100; margin-bottom: 5px;">💬 大家的溫暖鼓勵</h4>
        <p style="color: #5D4037; font-size: 16px;">不管是對媽媽手藝的稱讚、還是想對祿祿喜寶說說話，每一則留言都是我們前進的動力！</p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- 2. 新增留言表單 (移到上面來囉！) ---
    st.markdown("### ✍️ 寫下您的悄悄話")
    with st.form("msg_form"):
        m_name = st.text_input("您的暱稱 (怎麼稱呼您？)")
        m_msg = st.text_area("想對媽媽、福祿或喜寶說的話...", height=100)
        
        submit_msg = st.form_submit_button("💌 送出留言")
        
        if submit_msg:
            if not m_msg:
                st.warning("📭 信紙是空的喔！寫點什麼吧～")
            else:
                msg_data = {
                    "name": m_name if m_name else "善心人士",
                    "message": m_msg
                }
                with st.spinner("把您的心意傳送中..."):
                    try:
                        post_res = requests.post(msg_gas_url, json=msg_data)
                        if post_res.status_code == 200:
                            st.balloons()
                            st.success("✨ 收到您的溫暖留言了！")
                            # 提示文字改成「往下看」，因為留言會自動出現！
                            st.markdown("""
                            <div style="background-color:#E8F5E9; padding:15px; border-radius:10px; border:1px solid #4CAF50; text-align:center; margin-bottom:20px;">
                                <h4 style="color:#2E7D32;">感謝您的鼓勵！</h4>
                                <p style="color:#2E7D32; margin-bottom:0;">(往下滑，您的留言已經熱騰騰地上牆囉！)</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error("傳送失敗，請稍後再試！")
                    except Exception as e:
                        st.error(f"連線發生問題：{e}")

    st.write("---")
    
    # --- 3. 顯示歷史留言牆 (移到下方！) ---
    st.markdown("<h4 style='color: #8D6E63;'>✨ 柴寶歷史留言牆</h4>", unsafe_allow_html=True)
    
    with st.spinner("正在為您讀取留言牆..."):
        try:
            res = requests.get(msg_gas_url)
            if res.status_code == 200:
                messages = res.json()
                
                if isinstance(messages, list) and len(messages) > 0:
                    for msg in reversed(messages):
                        st.markdown(f"""
                        <div style="position: relative; background-color: #FDF8E7; border: 1px solid #EEDEA8; border-radius: 5px; padding: 20px; box-shadow: 3px 4px 8px rgba(0,0,0,0.08); margin-bottom: 25px; min-height: 200px; overflow: hidden;">
                            {mom_html}
                            {lubo_html}
                            <div style="color: #5D4037; font-weight: bold; font-size: 17px; position: relative; z-index: 1;">留言者：{msg.get('name', '神秘客')}</div>
                            <div style="color: #4E342E; font-size: 18px; line-height: 1.6; text-align: center; margin: 30px 90px 40px 110px; position: relative; z-index: 1; min-height: 60px; white-space: pre-wrap;">{msg.get('message', '')}</div>
                            <div style="color: #8D6E63; font-size: 14px; position: absolute; bottom: 15px; right: 20px; z-index: 1;">日期：{msg.get('time', '')[:10]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("目前還沒有留言喔！快來當第一個留言的人吧！✨")
        except Exception as e:
            st.warning("目前暫時無法載入留言牆，請稍後再試。")