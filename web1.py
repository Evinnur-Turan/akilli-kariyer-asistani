import streamlit as st
import pypdf

# 1. WEB SİTESİNİN GENEL AYARLARI
st.set_page_config(
    page_title="Genç Kariyer Asistanı AI", 
    page_icon="🧠", 
    layout="centered"
)

# HAFIZA (SESSION STATE) TANIMLAMALARI
if "arama_yapildi" not in st.session_state:
    st.session_state.arama_yapildi = False

# 2. ŞIK VE MODERN KARŞILAMA PANELİ
st.markdown("""
    <div style="background-color:#f0f2f6; padding:25px; border-radius:15px; margin-bottom:25px; border-left: 5px solid #1E3A8A;">
        <h1 style="color:#1E3A8A; text-align:center; margin:0; font-size:28px;">🧠 Genç Kariyer Asistanı AI</h1>
        <p style="color:#4B5563; text-align:center; font-size:15px; margin-top:8px; line-height:1.5;">
            Yapay zeka desteğiyle özgeçmişinizi (CV) analiz edin, bölgenizdeki en uygun iş fırsatlarını ve mülakat tüyolarını anında yakalayın!
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. İŞ İLANLARI VERİTABANIMIZ
IS_BANKASI = [
    {
        "unvan": "Genç Yazılımcı (Python)", "sehir": "İstanbul",
        "yetenekler": ["python", "kodlama", "yazilim"], "firma": "Vairosoft Bilgi Teknolojileri",
        "tuyp": "🎯 Şirket Kültürü: GitHub linkine inanılmaz önem veriyorlar! Projelerini eklemeyi unutma.",
        "link": "https://www.kariyer.net/is-ilanlari/istanbul-python" 
    },
    {
        "unvan": "Python Backend Developer", "sehir": "İstanbul",
        "yetenekler": ["seo", "reklam", "analiz", "pazarlama", "python"], "firma": "Arman Yazılım",
        "tuyp": "🎯 Şirket Kültürü: Mülakatta geçmişte yazdığın backend algoritmalarından bahset.",
        "link": "https://www.kariyer.net/is-ilanlari/istanbul-yazilim-gelistirme" 
    },
    {
        "unvan": "Sosyal Medya Stajyeri", "sehir": "İzmir",
        "yetenekler": ["tasarim", "instagram", "video", "pazarlama"], "firma": "Yaratıcı Medya Ajansı",
        "tuyp": "🎯 Şirket Kültürü: Instagram'da yaptığın eski tasarımları veya videoları mülakatta mutlaka göster.",
        "link": "https://www.kariyer.net/is-ilanlari/izmir-stajyer"
    }
]

# TÜRKİYE'NİN 81 İLİ
SEHIRLER_81 = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin", 
    "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", 
    "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", 
    "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "İstanbul", 
    "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli", 
    "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş", 
    "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Şanlıurfa", "Siirt", "Sinop", 
    "Sivas", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"
]

# 4. YARDIMCI FONKSİYONLAR
def metni_temizle(metin):
    return metin.lower().replace('ı', 'i').replace('ş', 's').replace('ğ', 'g').replace('ç', 'c').replace('ö', 'o').replace('ü', 'u')

def pdf_metnini_oku(yuklenen_dosya):
    okuyucu = pypdf.PdfReader(yuklenen_dosya)
    tum_yazilar = ""
    for sayfa in okuyucu.pages:
        yazi = sayfa.extract_text()
        if yazi: tum_yazilar += yazi + "\n"
    return tum_yazilar

# 5. SOL MENÜ (SIDEBAR) TASARIMI
st.sidebar.markdown("<h1 style='text-align: center;'>📑</h1>", unsafe_allow_html=True)
st.sidebar.header("📍 Arama Ayarları")
sehir_secimi = st.sidebar.selectbox("Çalışmak İstediğiniz Şehir:", SEHIRLER_81)

st.sidebar.markdown("---")
st.sidebar.write("💡 *Tüyo: CV'nizde ne kadar çok anahtar kelime (Python, SEO, Yazılım vb.) varsa, eşleşme o kadar güçlü olur!*")

# 6. ANA EKRAN DOSYA YÜKLEME ALANI
st.subheader("📂 Özgeçmişinizi Yükleyin")
yuklenen_dosya = st.file_uploader("", type=["pdf"])

# Dosya değişirse veya kaldırılırsa aramayı sıfırla
if yuklenen_dosya is None:
    st.session_state.arama_yapildi = False

# 7. AKILLI EŞLEŞTİRME MOTORU
if yuklenen_dosya is not None:
    st.success("🎉 CV Başarıyla Sisteme Yüklendi!")
    
    # Arama butonu hafızayı tetikler
    if st.button("🚀 UYGUN İLANLARI VE ÖN YAZIMI LİSTELE", use_container_width=True):
        st.session_state.arama_yapildi = True

    # Eğer butona basıldıysa veya hafızada arama yapıldı görünüyorsa sonuçları göster
    if st.session_state.arama_yapildi:
        cv_metni = pdf_metnini_oku(yuklenen_dosya)
        temiz_cv = metni_temizle(cv_metni)
        temiz_sehir = metni_temizle(sehir_secimi)
        
        st.markdown("### 🔎 Sizin İçin Listelenen Fırsatlar")
        
        bulundu_mu = False
        for ilan in IS_BANKASI:
            if metni_temizle(ilan["sehir"]) == temiz_sehir:
                eslesenler = [y for y in ilan["yetenekler"] if y in temiz_cv]
                
                if eslesenler:
                    bulundu_mu = True
                    
                    with st.expander(f"💼 {ilan['unvan']} — {ilan['firma']}", expanded=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**📍 Konum:** {ilan['sehir']}")
                            st.write(f"**✅ Eşleşen Yetenekleriniz:** {', '.join(eslesenler).upper()}")
                            st.markdown("<span style='background-color:#D1FAE5; color:#065F46; padding:4px 8px; border-radius:12px; font-size:12px; font-weight:bold;'>✨ Genç Dostu Firma</span>", unsafe_allow_html=True)
                        with col2:
                            link_kodu = f"""
                                <a href="{ilan['link']}" target="_blank" style="text-decoration: none;">
                                    <div style="background-color: #1E3A8A; color: white; padding: 10px 12px; text-align: center; border-radius: 6px; font-weight: bold; font-size: 14px; margin-top: 15px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                                        🔗 İlanları Listele
                                    </div>
                                </a>
                            """
                            st.markdown(link_kodu, unsafe_allow_html=True)
                        
                        st.info(ilan["tuyp"])
                        
                        st.write("📝 **Size Özel Hazırlanan Başvuru Mektubu:**")
                        mektup = f"Sayın {ilan['firma']} İşe Alım Ekibi,\n\n{sehir_secimi} bölgesindeki '{ilan['unvan']}' ilanınızı büyük bir heyecanla inceledim. CV'mde de görebileceğiniz üzere, şirketinizin aradığı kriterlerle yeteneklerim birebir uyuşmaktadır...\n\nSaygılarımla,\nİş Arayan Genç"
                        
                        # Benzersiz key ekleyerek çakışmaları önlüyoruz
                        st.text_area("Kopyalamak için kutunun içine tıklayın:", mektup, height=120, key=f"mektup_{ilan['unvan']}")
                        
        if not bulundu_mu:
            st.warning(f"Seçtiğiniz {sehir_secimi} şehrinde veya CV içeriğinize uygun bir ilan şimdilik bulunamadı.")

# 8. SIKÇA SORULAN SORULAR BÖLÜMÜ
st.markdown("<br><br>", unsafe_allow_html=True)
with st.container():
    st.info("💡 **Yol Gösterici Bilgiler Paneli**")
    with st.expander("❓ Sitedeki İlanlar Güncel mi?"):
        st.write("Evet! Sistemimizdeki bağlantılar Kariyer.net üzerindeki anlık, canlı ve başvuruya açık ilan arama motorlarına bağlanmıştır.")
    with st.expander("❓ Başvuru Mektubunu Nasıl Kullanmalıyım?"):
        st.write("Yapay zekanın sizin için hazırladığı mektubu kopyalayarak şirketlerin İK e-postalarına veya kariyer sitelerindeki 'Ön Yazı' kısmına yapıştırarak fark yaratabilirsiniz.")
