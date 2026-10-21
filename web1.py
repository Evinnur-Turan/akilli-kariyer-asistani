# --- ADIM 5: PROJENİN WEB SİTESİ (STREAMLIT) KODU ---
# Not: Bu kod bir web sitesi tasarımı olduğu için normal Python gibi değil, 
# Streamlit kütüphanesiyle çalışır.

# Önce web sitesi kütüphanesini Kaggle'a tanıtıyoruz (Çalıştırmadan önce en üstte dursun)
# !pip install streamlit pypdf -q

import streamlit as st
import pypdf

# 1. WEB SİTESİNİN BAŞLIĞI VE LOGOSU
st.set_page_config(page_title="Genç İş Bulucu", page_icon="🌟", layout="centered")

st.title("🌟 Gençler İçin Akıllı İş Bulucu Asistanı 🌟")
st.write("CV'nizi yükleyin, çalışmak istediğiniz şehri seçin ve size özel kariyer fırsatlarını anında görün!")

# 2. İŞ İLANLARI VERİTABANIMIZ
IS_BANKASI = [
    {
        "unvan": "Genç Yazılımcı (Python)", "sehir": "Istanbul",
        "yetenekler": ["python", "kodlama", "yazilim"], "firma": "Gelecek Teknoloji",
        "tuyp": "💡 TÜYO: GitHub linkine önem veriyorlar! Projelerini ekle."
    },
    {
        "unvan": "Dijital Pazarlama Uzmanı", "sehir": "Istanbul",
        "yetenekler": ["seo", "reklam", "analiz", "pazarlama"], "firma": "MedyaKüp Ajans",
        "tuyp": "💡 TÜYO: Mülakatta bütçe yönetimi tecrübelerinden bahset."
    }
]

# 3. YARDIMCI FONKSİYONLAR (Harf temizleme ve PDF okuma)
def metni_temizle(metin):
    return metin.lower().replace('ı', 'i').replace('ş', 's').replace('ğ', 'g').replace('ç', 'c').replace('ö', 'o').replace('ü', 'u')

def pdf_metnini_oku(yuklenen_dosya):
    okuyucu = pypdf.PdfReader(yuklenen_dosya)
    tum_yazilar = ""
    for sayfa in okuyucu.pages:
        yazi = sayfa.extract_text()
        if yazi: tum_yazilar += yazi + "\n"
    return tum_yazilar

# 4. WEB SİTESİ ARAYÜZ ELEMANLARI (Kutular, Butonlar)
st.subheader("1) Bilgilerinizi Girin")

# Şehir seçme kutusu
sehir_secimi = st.selectbox("Çalışmak İstediğiniz Şehir:", ["Istanbul", "Izmir", "Ankara"])

# Dosya yükleme kutusu (Sürükle-Bırak)
yuklenen_dosya = st.file_uploader("CV'nizi PDF formatında yükleyin:", type=["pdf"])

# 5. EŞLEŞTİRME VE BUTON MOTORU
if yuklenen_dosya is not None:
    st.success("🎉 CV Başarıyla Yüklendi!")
    
    # Kullanıcı butona bastığında oyun başlasın
    if st.button("🚀 Bana En Uygun İşleri Bul ve Ön Yazımı Hazırla"):
        
        # PDF'i arka planda okuyoruz
        cv_metni = pdf_metnini_oku(yuklenen_dosya)
        temiz_cv = metni_metni_temizle(cv_metni)
        temiz_sehir = metni_temizle(sehir_secimi)
        
        st.subheader("🔎 Bulunan Uygun İş İlanları")
        
        # İlanları dönüp eşleşen var mı bakıyoruz
        bulundu_mu = False
        for ilan in IS_BANKASI:
            if metni_temizle(ilan["sehir"]) == temiz_sehir:
                # Yetenek kontrolü
                eslesenler = [y for y in ilan["yetenekler"] if y in temiz_cv]
                
                if eslesenler:
                    bulundu_mu = True
                    # Ekranda şık bir bilgi kutusu açıyoruz
                    with st.expander(f"💼 {ilan['unvan']} - {ilan['firma']}"):
                        st.write(f"**📍 Konum:** {ilan['sehir']}")
                        st.write(f"**✅ Eşleşen Yetenekleriniz:** {', '.join(eslesenler)}")
                        st.info(ilan["tuyp"])
                        
                        # Otomatik Ön Yazı Kısmı
                        st.write("**📝 Sizin İçin Hazırlanan Başvuru Mektubu:**")
                        mektup = f"Sayın {ilan['firma']} Yetkilisi,\n\n{sehir_secimi} bölgesindeki {ilan['unvan']} ilanınızla ilgileniyorum. CV'mde belirttiğim yeteneklerimle şirketinize değer katabileceğime inanıyorum...\n\nSaygılarımla,\nİş Arayan Genç"
                        st.text_area("Kopyalamak için tıklayın:", mektup, height=150)
                        
        if not bulundu_mu:
            st.warning("Bu şehirde veya bu CV içeriğine uygun bir ilan şimdilik bulunamadı.")
