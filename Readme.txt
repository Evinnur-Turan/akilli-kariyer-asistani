# 🧭 Akıllı Kariyer Asistanı

**Akıllı Kariyer Asistanı**, üniversite öğrencilerinin (önlisans ve lisans) ve yeni mezunların *"Diplomayı alacağım ama şimdi ne yapacağım, sektöre nasıl adım atacağım?"* sorusuna yanıt arayan, kâr amacı gütmeyen, topluluk odaklı ve **açık kaynaklı bir dijital kariyer koçu** projesidir.

İş ilanı listeleyen siteler yerine öğrenciyi merkeze alır: bölümüne özel yol haritası, takip edilecek kişiler ve bir yapay zeka mentor sunar.

---

## ✨ Özellikler

Uygulama 3 sekmeden oluşan bir koçluk ekranı sunar:

| Sekme | Ne yapar? |
|---|---|
| **Yol Haritası** | 1. sınıftan mezuniyete dönem dönem yapılacaklar. Check-list olarak işaretlenir, ilerleme çubuğu güncellenir. |
| **Kimi Takip Etmeli?** | Bölüme göre LinkedIn, YouTube, Medium ve GitHub kaynakları. Her biri için "Neden takip etmelisin?" ve "Sana ne katar?" açıklaması. |
| **Yapay Zeka Mentor** | "Dikey geçiş mi yapmalıyım, direkt işe mi girmeliyim?" gibi sorulara Claude ile yanıt verir. |

Önlisans (2 yıl) ve lisans (4 yıl) için ayrı akışlar vardır.

---

## 🖥️ Hızlı Başlangıç (Streamlit sürümü)

Gereksinimler: Python 3.9+

```bash
git clone https://github.com/KULLANICI_ADIN/kariyer-asistani.git
cd kariyer-asistani
pip install streamlit anthropic
streamlit run app.py
```

Tarayıcıda uygulama otomatik açılır. Bölüm olarak **Bilgisayar Programcılığı** (önlisans) veya **İşletme** (lisans) yazarak örnek içerikleri görebilirsin. Başka bir bölüm yazarsan genel bir plan gösterilir.

### Yapay zeka mentoru etkinleştirme

Mentor sekmesi için bir Claude API anahtarı gerekir. Anahtar yoksa uygulamanın geri kalanı yine çalışır.

```bash
# Mac / Linux
export ANTHROPIC_API_KEY="anahtarin"

# Windows (cmd)
set ANTHROPIC_API_KEY=anahtarin
```

Alternatif olarak `.streamlit/secrets.toml` dosyasına şunu yaz:

```toml
ANTHROPIC_API_KEY = "anahtarin"
```

> ⚠️ API anahtarını asla GitHub'a gönderme. `.streamlit/secrets.toml` dosyasını `.gitignore` içine ekle.

İstersen kullanılacak modeli `CLAUDE_MODEL` ortam değişkeniyle değiştirebilirsin.

---

## 🎨 Tasarım

Gözü yormayan, mat bir renk paleti kullanılır:

| Kullanım | Renk |
|---|---|
| Arka plan | `#F4F4F2` |
| Birincil (gece mavisi) | `#2C3E50` |
| İkincil (adaçayı yeşili) | `#7D8C7A` |
| Metin | `#333333` |
| Kartlar | `#E8E8E4` |

---

## 🗂️ Proje Yapısı

```
kariyer-asistani/
├── app.py            # Streamlit uygulaması (çalışan sürüm)
├── kurulum.py        # Next.js + Supabase iskeletini oluşturan betik (planlanan sürüm)
└── README.md
```

`kurulum.py`, ileride web sürümüne geçmek için Next.js, Supabase ve SQL şeması dosyalarını üretir. Önce `npx create-next-app@latest` ile bir Next.js projesi oluşturup betiği o klasörde çalıştırman gerekir.

---

## 🤝 Katkıda Bulunma

Projeye en kolay katkı, yeni bir bölümün içeriğini eklemektir. `app.py` içindeki `VERI` sözlüğüne şu biçimde yeni bir kayıt ekle:

```python
("lisans", "psikoloji"): {
    "ad": "Psikoloji",
    "yol": [
        ("1. Sınıf", ["Bir öğrenci topluluğuna katıl", "..."]),
        # diğer dönemler
    ],
    "takip": [
        ("Kaynak adı", "LinkedIn", "Neden takip etmeli?", "Sana ne katar?"),
    ],
},
```

Anahtarın ilk kısmı `"onlisans"` veya `"lisans"`, ikinci kısmı **küçük harfle** bölüm adıdır.

**Takip listesi için kurallar:**
- Gerçek kişileri listelerken mümkünse önce kendilerinden izin al.
- Kısa ve gerekçeli açıklama yaz, kesin iş garantisi veya abartılı vaat içeren ifadelerden kaçın.
- Sadece herkese açık, güvenilir profil ve kanalları ekle.

**Adımlar:**
1. Depoyu forklayın.
2. Yeni bir branch açın: `git checkout -b feature/YeniBolumEkleme`
3. Değişikliklerinizi commit edin: `git commit -m "Eklendi: Psikoloji yol haritası"`
4. Branch'inizi push edin: `git push origin feature/YeniBolumEkleme`
5. Bir **Pull Request** açın.

---

## 🛣️ Yol Haritası

- [x] Streamlit ile çalışan prototip
- [x] Önlisans / lisans ayrımı
- [x] Yapay zeka mentor (Claude API)
- [ ] Verilerin koddan ayrılıp veritabanına (Supabase / PostgreSQL) taşınması
- [ ] Kullanıcı girişi ve kalıcı ilerleme kaydı
- [ ] En çok tercih edilen 20 önlisans ve 20 lisans bölümünün içeriği
- [ ] Bölümlere özel, aranabilir rehber sayfaları (SEO)
- [ ] Next.js web sürümü

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. MIT lisansı ticari kullanımı da kapsar. Projenin ticari kullanıma kapalı olmasını istiyorsan lisansı değiştirmen gerekir.

Depoya bir `LICENSE` dosyası eklemeyi unutma. GitHub'da **Add file → Create new file** ile dosya adına `LICENSE` yazınca şablon seçeneği çıkar.
