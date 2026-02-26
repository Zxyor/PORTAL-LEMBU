import streamlit as st
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Portal LEMBU",
    page_icon="lembu.png",
    layout="centered"
)

URL_VIDEO_PC = "https://github.com/Zxyor/PORTAL-LEMBU/raw/refs/heads/main/PT.%20Mahakam%20Lembu%20Mulawarman.mp4"
URL_VIDEO_HP = "https://github.com/Zxyor/PORTAL-LEMBU/raw/refs/heads/main/mobile_bg.mp4"

# =========================================================================

# --- INJEKSI CSS & HTML (STREAMING LANGSUNG - TANPA PYTHON BASE64) ---
video_html = f"""
<style>
    /* 1. BACKGROUND ANIMASI (STANDBY SAAT VIDEO BUFFERING) */
    .animated-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -100;
        background: linear-gradient(-45deg, #000000, #1a0b2e, #0f204b, #020a1a);
        background-size: 400% 400%;
        animation: bgFlow 10s ease infinite;
    }}
    @keyframes bgFlow {{
        0%   {{ background-position: 0% 50%; }}
        50%  {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* 2. PENGATURAN VIDEO (AKAN MENIMPA ANIMASI JIKA SUDAH JALAN) */
    .bg-video {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -99; 
        object-fit: fill; 
        will-change: transform; 
    }}
    
    /* 3. LAPISAN HITAM TRANSPARAN OVERLAY */
    .video-overlay {{
        position: fixed;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.6); 
        z-index: -98;
    }}

    .stApp {{ background: transparent; }}
    header {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    /* MEDIA QUERY TAMPILAN */
    #videoDesktop {{ display: block; }}
    #videoMobile {{ display: none; }}

    @media (max-width: 768px) {{
        #videoDesktop {{ display: none; }}
        #videoMobile {{ display: block; }}
    }}
</style>

<div class="animated-bg"></div>

<video id="videoDesktop" class="bg-video" autoplay loop muted playsinline>
    <source src="{URL_VIDEO_PC}" type="video/mp4">
</video>

<video id="videoMobile" class="bg-video" autoplay loop muted playsinline>
    <source src="{URL_VIDEO_HP}" type="video/mp4">
</video>

<div class="video-overlay"></div>
"""
st.markdown(video_html, unsafe_allow_html=True)


# --- 2. CSS KUSTOM (KOTAK KACA & TOMBOL) ---
st.markdown("""
<style>
    /* --- KOTAK KACA --- */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(20, 30, 50, 0.65) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"] hr {
        border-color: rgba(255,255,255, 0.2) !important;
    }

    /* --- LOGO & TEKS --- */
    img {
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.5);
        display: block;
        margin-left: auto;
        margin-right: auto;
        transition: transform 0.3s ease;
    }
    img:hover { transform: scale(1.05); }

    h1 {
        color: #FFFFFF;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 800;
        text-shadow: 0 0 20px rgba(0,0,0,0.8);
        text-align: center;
        margin-bottom: 5px;
    }

    p {
        color: #d1d5db;
        text-align: center;
        font-size: 1.1rem;
    }
    
    h3 {
        color: #38bdf8 !important;
        text-align: center;
        font-weight: 700;
        text-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
    }
    
    .caption-text {
        font-size: 0.9rem;
        color: #9ca3af;
        text-align: center;
        margin-bottom: 15px;
        display: block;
    }

    /* --- ANIMASI TOMBOL --- */
    @keyframes btnFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    div.stButton > button, div.stDownloadButton > button, .stLinkButton a {
        width: 100%;
        background: linear-gradient(90deg, #0f172a, #2563eb, #7c3aed);
        background-size: 200% 200%;
        animation: btnFlow 4s ease infinite;
        
        color: white !important;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 0.8rem 1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-decoration: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .stLinkButton { width: 100%; }

    div.stButton > button:hover, div.stDownloadButton > button:hover, .stLinkButton a:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(37, 99, 235, 0.6);
        border-color: #38bdf8;
    }

</style>
""", unsafe_allow_html=True)

# --- 3. TAMPILAN UTAMA (UI) ---

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("lembu.png"):
        st.image("lembu.png", use_container_width=True)

st.title("Web Portal LEMBU")
st.markdown("Selamat datang. Silakan pilih Aplikasi Apa Yang Ingin Anda Akses.")

with st.container(border=True):
    st.markdown("---") 
    
    st.subheader("🌐 Aplikasi Laporan BBM")
    st.markdown('<span class="caption-text">Klik tombol di bawah untuk membuka aplikasi.</span>', unsafe_allow_html=True)
    
    target_url = "https://bbm-lembu.streamlit.app/" 
    st.link_button("🚀 KUNJUNGI APLIKASI", target_url, use_container_width=True)

    st.subheader("📂 Buku Panduan")
    st.markdown('<span class="caption-text">Unduh panduan penggunaan lengkap (PDF).</span>', unsafe_allow_html=True)

    pdf_path = "manualbook/BUKU PANDUAN PENGGUNA APLIKASI LAPORAN BBM.pdf"

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            pdf_byte = pdf_file.read()
            
        st.download_button(
            label="DOWNLOAD PANDUAN (PDF) 📥",
            data=pdf_byte,
            file_name="BUKU_PANDUAN_PENGGUNA_BBM.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("⚠️ File PDF belum tersedia di folder manualbook.")

    st.markdown("---") 

st.markdown(
    """
    <div style='text-align: center; color: #fff; margin-top: 30px; font-size: 0.8rem; font-family: monospace; opacity: 0.7;'>
        © 2026 Web Portal LEMBU | All Rights Reserved
    </div>
    """, 
    unsafe_allow_html=True
)