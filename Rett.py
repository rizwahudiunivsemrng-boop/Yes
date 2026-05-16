import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Analisis Nilai UAS",
    page_icon="📊",
    layout="wide"
)

# --- STYLE CSS TINGKAT TINGGI (GARANSI PRESISI TOTAL) ---
st.markdown("""
    <style>
    /* Mengatur grid agar 3 kotak Matkul tingginya selalu sama rata air */
    .wadah-grid-Matkul {
        display: flex;
        gap: 15px;
        justify-content: space-between;
        align-items: stretch;
        width: 100%;
    }

    /* Desain Kotak Matkul Presisi */
    .kotak-Matkul {
        background-color: #f8f9fa;
        padding: 15px 10px;
        border-radius: 12px;
        border-top: 5px solid #764ba2;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        text-align: center;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: all 0.3s ease-in-out;
        min-width: 0;
    }
    
    /* Efek Hover Melayang */
    .kotak-Matkul:hover {
        transform: translateY(-8px);
        background-color: #ffffff;
        border-top: 5px solid #667eea;
        box-shadow: 0 12px 24px rgba(118, 75, 162, 0.2);
    }
    
    /* Memaksa nama Matkul tetap 1 baris */
    .judul-Matkul {
        margin: 0px 0px 6px 0px !important; 
        font-size: 0.95rem; 
        font-weight: 700; 
        color: #764ba2;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    
    /* Angka nilai dibuat jauh lebih besar dan tebal */
    .angka-nilai {
        margin: 0px !important; 
        font-size: 2.2rem; 
        font-weight: 800;
        color: #1e2024;
        line-height: 1.1;
    }
    
    /* Penyesuaian saat laptop menggunakan Tema Dark Mode */
    @media (prefers-color-scheme: dark) {
        .kotak-Matkul {
            background-color: #1e2024;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .kotak-Matkul:hover {
            background-color: #25282f;
            box-shadow: 0 12px 24px rgba(118, 75, 162, 0.4);
        }
        .angka-nilai {
            color: #ffffff;
        }
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNGSI UNTUK MENGAMBIL ANIMASI SECARA ONLINE ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Mengambil link animasi Lottie
lottie_welcome = load_lottieurl("https://lottie.host/81180bba-1b9c-48c0-bc6d-a6007ec124fa/7IOnbI8WqW.json")
lottie_success = load_lottieurl("https://lottie.host/7ca6ba10-09fa-4bfa-97b7-7ff72a15c8e3/w885N8g90v.json")

# --- TAMPILAN HEADER ---
st.markdown("<h1 style='text-align: center; color: #764ba2;'>PROGRAM ANALISIS NILAI UAS</h1>", unsafe_allow_html=True)

if lottie_welcome:
    st_lottie(lottie_welcome, speed=1, height=180, key="welcome_anim")

st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #6e7e8c;'>Selamat! Hasil UAS sudah keluar. Silakan masukkan data di sidebar samping.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR INPUT DATA (FORM) ---
with st.sidebar:
    with st.form(key="my_form"):
        st.header("👤 Input Identitas")
        Nama = st.text_input("Nama:")
        Umur = st.number_input("Umur:", min_value=0, step=1, value=0)
        Alamat = st.text_input("Alamat:")
        Sekolah = st.text_input("Fakultas:")
        
        st.markdown("---")
        st.header("📚 Input Matkul & Nilai")
        
        # Di sini perbaikannya: value diubah menjadi 0.0 (desimal) agar aplikasi tidak error
        Matkul1 = st.text_input("Matkul 1:", value="")
        Nilai1 = st.number_input(f"Nilai {Matkul1}:", min_value=0.0, max_value=100.0, step=0.5, key="n1", value=0.0)
        
        Matkul2 = st.text_input("Matkul 2:", value="")
        Nilai2 = st.number_input(f"Nilai {Matkul2}:", min_value=0.0, max_value=100.0, step=0.5, key="n2", value=0.0)
        
        Matkul3 = st.text_input("Matkul 3:", value="")
        Nilai3 = st.number_input(f"Nilai {Matkul3}:", min_value=0.0, max_value=100.0, step=0.5, key="n3", value=0.0)
        
        proses = st.form_submit_button("🚀 Analisis Sekarang", use_container_width=True)

# --- LOGIKA KETIKA TOMBOL DIKLIK ---
if proses:
    st.snow()
    
    # BAGIAN 1: DATA IDENTITAS
    st.subheader("📋 Ringkasan Identitas")
    id_col1, id_col2, id_col3, id_col4 = st.columns(4)
    
    with id_col1:
        st.metric(label="Nama Mahasiswa", value=Nama if Nama.strip() != "" else "Belum Diisi")
    with id_col2:
        st.metric(label="Usia", value=f"{Umur} Tahun")
    with id_col3:
        st.metric(label="Asal Institusi", value=Sekolah if Sekolah.strip() != "" else "Belum Diisi")
    with id_col4:
        st.metric(label="Alamat", value=Alamat if Alamat.strip() != "" else "Belum Diisi")
        
    st.markdown("---")
    
    # BAGIAN 2: DETAIL NILAI & EVALUASI
    main_col1, main_col2 = st.columns(2, gap="large")
    
    # Kolom Kiri: Dipecah pakai 3 kolom murni Streamlit (Anti Gantung / Anti Tumpuk)
    with main_col1:
        st.subheader("📚 Nilai Per Mata Kuliah")
        Matkul1_col1, Matkul2_col2, Matkul3_col3 = st.columns(3, gap="small")
        
        with Matkul1_col1:
            st.markdown(f"""
                <div class="kotak-Matkul 1-baru">
                    <p class="judul-Matkul 1-baru" title="{Matkul1}">{Matkul1}</p>
                    <p class="angka-nilai-baru">{Nilai1}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with Matkul2_col2:
            st.markdown(f"""
                <div class="kotak-Matkul 2-baru">
                    <p class="judul-Matkul2-baru" title="{Matkul2}">{Matkul2}</p>
                    <p class="angka-nilai-baru">{Nilai2}</p>
                </div>
            """, unsafe_allow_html=True)
            
        with Matkul3_col3:
            st.markdown(f"""
                <div class="kotak-Matkul 3-baru">
                    <p class="judul-Matkul3-baru" title="{Matkul3}">{Matkul3}</p>
                    <p class="angka-nilai-baru">{Nilai3}</p>
                </div>
            """, unsafe_allow_html=True)
            
    # Kolom Kanan: Hasil Analisis & Kesimpulan Akhir
    with main_col2:
        st.subheader("🏁 Hasil Kelulusan")
        
        rata_rata = (Nilai1 + Nilai2 + Nilai3) / 3
        
        res_col1, res_col2 = st.columns([1, 1])
        with res_col1:
            st.metric(label="Total Rata-rata", value=f"{rata_rata:.2f}")
            
            if rata_rata >= 75.0:
                st.success("Dinyatakan Lulus")
            else:
                st.error("Remedial Diperlukan")
                
        with res_col2:
            if rata_rata >= 75.0 and lottie_success:
                st_lottie(lottie_success, speed=1, height=120, key="success_anim")
        
        st.markdown("**💡 Kesimpulan Akhir:**")
        if Umur >= 18 and rata_rata >= 75:
            st.success("Kualifikasi Terpenuhi! Usia matang dan nilai memenuhi syarat kelulusan.")
        elif Umur < 18 and rata_rata >= 75:
            st.warning("Nilai mencukupi, namun status usia masih masuk kategori pengembangan (Remaja).")
        elif Umur >= 18 and rata_rata < 75:
            st.error("Sudah masuk usia dewasa, tetapi harus ditingkatkan lagi karena nilai di bawah standar 75.")
        else:
            st.error("Nilai belum cukup dan usia masih muda. Direkomendasikan untuk bimbingan khusus.")