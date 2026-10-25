"""
Akıllı Kariyer Asistanı - Streamlit sürümü

Kurulum:   pip install streamlit anthropic
Çalıştır:  streamlit run app.py

Yapay zeka mentor için ANTHROPIC_API_KEY ortam değişkenini ayarla
(veya .streamlit/secrets.toml içine ANTHROPIC_API_KEY = "..." yaz).
Anahtar yoksa uygulama yine çalışır, sadece mentor sekmesi devre dışı kalır.
"""

import os

import streamlit as st

st.set_page_config(page_title="Akıllı Kariyer Asistanı", page_icon="🧭", layout="centered")

# ---------------------------------------------------------------- tema (mat palet)
st.markdown(
    """
    <style>
    .stApp { background-color: #F4F4F2; color: #333333; }
    h1, h2, h3 { color: #2C3E50; }
    div[data-testid="stCheckbox"] { background: #E8E8E4; padding: 6px 12px; border-radius: 8px; margin-bottom: 6px; }
    .kart { background: #E8E8E4; padding: 14px 16px; border-radius: 8px; margin-bottom: 10px; }
    .etiket { background: #7D8C7A; color: #F4F4F2; padding: 2px 8px; border-radius: 99px; font-size: 0.8rem; margin-left: 6px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- veri
VERI = {
    ("onlisans", "bilgisayar programcılığı"): {
        "ad": "Bilgisayar Programcılığı",
        "yol": [
            ("1. Sınıf Güz", [
                "Temel Git/GitHub öğren ve ilk reposunu oluştur",
                "Bir programlama dilinde günlük küçük alıştırmalar yap",
            ]),
            ("1. Sınıf Bahar", [
                "Bir yazılım topluluğuna (örn. GDG) üye ol ve etkinliklerine katıl",
                "İlk küçük projeni GitHub üzerinde yayınla",
            ]),
            ("Yaz Dönemi", [
                "En az 20 günlük zorunlu staj yeri bul",
                "LinkedIn üzerinden 10 sektör profesyoneliyle bağlantı kur",
            ]),
            ("2. Sınıf Güz", [
                "Veritabanı ve API temellerini bir projede uygula",
                "Portföy sayfanı oluştur",
            ]),
            ("2. Sınıf Bahar", [
                "CV ve LinkedIn profilini güncelle",
                "Dikey geçiş ve iş başvurusu seçeneklerini karşılaştır",
            ]),
        ],
        "takip": [
            ("Yazılım LinkedIn liderleri", "LinkedIn",
             "Sektörde işe alım ve kariyer yolları hakkında güncel paylaşımlar yapar.",
             "Staj ve ilk iş sürecini gerçek örneklerle görürsün."),
            ("Türkçe yazılım YouTube kanalları", "YouTube",
             "Sıfırdan proje geliştirmeyi adım adım anlatır.",
             "Derste öğrenmediğin pratik becerileri kazanırsın."),
            ("Açık kaynak geliştiriciler", "GitHub",
             "Gerçek projelerde kod yazım ve katkı süreçlerini gösterir.",
             "Kendi depolarını nasıl düzenleyeceğini öğrenirsin."),
        ],
    },
    ("lisans", "işletme"): {
        "ad": "İşletme",
        "yol": [
            ("1. Sınıf", ["Bir öğrenci kulübüne katıl", "Excel temellerini öğren"]),
            ("2. Sınıf", ["Kısa dönem staj yap", "Bir sertifika programı seç (örn. dijital pazarlama veya finans)"]),
            ("3. Sınıf", ["Uzun dönem staj başvurularını yap", "LinkedIn profilini kur ve sektör insanlarını takip et"]),
            ("4. Sınıf", ["CV ve mülakat provası yap", "Yüksek lisans ve doğrudan işe giriş seçeneklerini karşılaştır"]),
        ],
        "takip": [
            ("İşletme ve finans yazarları", "Medium",
             "Pazar ve şirket analizleri paylaşır.", "Sektör diline hâkim olursun."),
            ("Kariyer koçları", "LinkedIn",
             "CV, mülakat ve ilk iş süreçleri üzerine içerik üretir.", "Başvurularını güçlendirirsin."),
        ],
    },
}

GENEL = {
    "onlisans": [
        ("1. Sınıf Güz", ["Bölümünle ilgili temel araçları belirle ve öğrenmeye başla", "Bir öğrenci topluluğuna katıl"]),
        ("Yaz Dönemi", ["Zorunlu stajın için yerleri araştır", "LinkedIn profilini oluştur"]),
        ("2. Sınıf", ["Bir proje veya portföy parçası hazırla", "Dikey geçiş ve iş seçeneklerini karşılaştır"]),
    ],
    "lisans": [
        ("1. Sınıf", ["Topluluk ve kulüplere katıl", "Bölümünün sektör haritasını çıkar"]),
        ("2. Sınıf", ["İlk stajını yap", "Bir sertifika seç"]),
        ("3. Sınıf", ["Uzun dönem staj bul", "Sektör profesyonellerini takip et"]),
        ("4. Sınıf", ["CV ve mülakat hazırlığı yap", "Yüksek lisans ve işe giriş seçeneklerini değerlendir"]),
    ],
}


def api_anahtari():
    anahtar = os.environ.get("ANTHROPIC_API_KEY")
    if anahtar:
        return anahtar
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:
        return None


def mentora_sor(soru, bolum, derece):
    import anthropic

    istemci = anthropic.Anthropic(api_key=api_anahtari())
    sistem = (
        f"Sen bir üniversite kariyer koçusun. Öğrenci {bolum} bölümünde {derece} "
        "eğitimi alıyor veya almak istiyor. Türkçe, sade ve uygulanabilir tavsiyeler ver. "
        "Kısa tut (en fazla 200 kelime). Kesin iş garantisi verme, emin olmadığın yerde bunu söyle."
    )
    yanit = istemci.messages.create(
        model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
        max_tokens=600,
        system=sistem,
        messages=[{"role": "user", "content": soru}],
    )
    return "".join(p.text for p in yanit.content if p.type == "text")


# ---------------------------------------------------------------- arayüz
st.title("Akıllı Kariyer Asistanı")
st.write(
    "Diplomadan sonra ne yapacağını bilmek için bölümünü seç. "
    "Dönem dönem yol haritanı ve takip etmen gereken kişileri gör."
)

with st.form("secim"):
    sutun1, sutun2 = st.columns([1, 2])
    derece_etiket = sutun1.selectbox("Eğitim düzeyi", ["Önlisans (2 yıl)", "Lisans (4 yıl)"])
    bolum_girdi = sutun2.text_input("Bölümün", placeholder="Örn. Bilgisayar Programcılığı")
    gonder = st.form_submit_button("Koçluk ekranını aç")

if gonder and bolum_girdi.strip():
    st.session_state["derece"] = "onlisans" if derece_etiket.startswith("Önlisans") else "lisans"
    st.session_state["bolum"] = bolum_girdi.strip()

if "bolum" not in st.session_state:
    st.info("Başlamak için bölümünü yaz. Örnek veri: Bilgisayar Programcılığı (önlisans), İşletme (lisans).")
    st.stop()

derece = st.session_state["derece"]
bolum = st.session_state["bolum"]
kayit = VERI.get((derece, bolum.lower()))
bolum_adi = kayit["ad"] if kayit else bolum
yol = kayit["yol"] if kayit else GENEL[derece]
takip = kayit["takip"] if kayit else None

st.header(bolum_adi)
st.caption("Lisans (4 yıl)" if derece == "lisans" else "Önlisans (2 yıl)")

sekme_yol, sekme_takip, sekme_mentor = st.tabs(["Yol Haritası", "Kimi Takip Etmeli?", "Yapay Zeka Mentor"])

with sekme_yol:
    adimlar = [(d, a) for d, liste in yol for a in liste]
    isaretli = sum(1 for i in range(len(adimlar)) if st.session_state.get(f"adim_{derece}_{bolum_adi}_{i}"))
    st.write(f"{isaretli}/{len(adimlar)} adım tamamlandı")
    st.progress(isaretli / len(adimlar) if adimlar else 0.0)

    sayac = 0
    for donem, liste in yol:
        st.subheader(donem)
        for adim in liste:
            st.checkbox(adim, key=f"adim_{derece}_{bolum_adi}_{sayac}")
            sayac += 1

with sekme_takip:
    if not takip:
        st.info("Bu bölüm için henüz küratörlü liste yok. Katkı yaparak ilk listeyi sen oluşturabilirsin.")
    else:
        for isim, platform, neden, katki in takip:
            st.markdown(
                f'<div class="kart"><b>{isim}</b><span class="etiket">{platform}</span>'
                f"<p>Neden takip etmelisin? {neden}</p>"
                f"<p>Sana ne katar? {katki}</p></div>",
                unsafe_allow_html=True,
            )

with sekme_mentor:
    if not api_anahtari():
        st.warning(
            "Yapay zeka mentor için ANTHROPIC_API_KEY tanımlı değil. "
            "Ortam değişkeni olarak ayarla veya .streamlit/secrets.toml dosyasına ekle."
        )
    else:
        soru = st.text_area(
            "Sorun",
            max_chars=1000,
            placeholder="Örn. Dikey geçiş mi yapmalıyım, direkt işe mi girmeliyim?",
        )
        if st.button("Mentora sor") and soru.strip():
            with st.spinner("Yanıt hazırlanıyor..."):
                try:
                    st.markdown(mentora_sor(soru.strip(), bolum_adi, derece))
                except Exception as hata:
                    st.error(f"Yapay zeka şu an yanıt veremiyor: {hata}")
