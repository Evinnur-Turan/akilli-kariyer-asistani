import streamlit as st

# Sayfa Genişliği ve Başlık Ayarı
st.set_page_config(
    page_title="Kariyer & Gelişim Asistanı",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Göz yormayan, mat ve modern premium renk paleti için CSS Enjeksiyonu
st.markdown("""
    <style>
    /* Ana Arka Plan ve Yazı Tipi */
    .stApp {
        background-color: #f4f6f8;
        color: #2d3748;
    }
    
    /* Başlık Alanı Tasarımı */
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Ortak Kart Alanları */
    .section-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #34495e;
        border-bottom: 2px solid #edf2f7;
        padding-bottom: 8px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .section-body {
        font-size: 0.95rem;
        color: #4a5568;
        line-height: 1.6;
        text-align: justify;
    }
    
    /* Bilgi Kutusu Tasarımları */
    .meta-box {
        background-color: #fafbfc;
        border-left: 4px solid #7f8c8d;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        margin-bottom: 10px;
    }
    
    .meta-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 6px;
        font-size: 0.95rem;
    }
    
    .meta-item {
        font-size: 0.9rem;
        color: #5a6578;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Başlık Bölümü
st.markdown('<div class="main-title">🎯 Kariyer & Gelişim Yol Gösterici Asistanı</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Göz yormayan mat tonlarla tasarlanmış akıllı mesleki gelişim rehberi</div>', unsafe_allow_html=True)

# 30 Bölümün Detaylı Veri Seti
data = {
    # --- LİSANS BÖLÜMLERİ ---
    "Tıp (Doktorluk)": {
        "type": "Lisans",
        "student": "Temel tıp bilimleri (Anatomi, Fizyoloji) süresince ezber yerine mantık kurun. Klinik yıllarda (4-5-6) olabildiğince çok hasta çeşitliliği görün ve anamnez alma becerinizi kusursuzlaştırın.",
        "grad": "Zorunlu hizmet süreçlerini ve TUS (Tıpta Uzmanlık Sınavı) hedefinizi netleştirin. İlgi duyduğunuz branşların nöbet ve çalışma şartlarını hastanelerde bizzat asistanlardan öğrenin.",
        "seeker": "Kamu atamalarını beklerken veya özel hastane zincirlerine başvururken klinik ilgi alanlarınızı ve aldığınız spesifik sertifikaları ('örneğin kupa terapisi, akupunktur vb. yan dallar') vurgulayın.",
        "follow": ["Türk Tabipleri Birliği (TTB)", "Medscape Medical News", "Doç. Dr. Muhammed Keskin"],
        "videos": ["TUS Derece Yapanların Çalışma Metotları", "Klinik Vaka Analizleri ve Anamnez Teknikleri"]
    },
    "Hukuk (Avukatlık)": {
        "type": "Lisans",
        "student": "Kanun maddelerini ezberlemek yerine gerekçelerini ve mantığını kavrayın. Güncel Yargıtay kararlarını düzenli okuyun ve kurgusal duruşma kulüplerinde aktif görev alın.",
        "grad": "Yasal staj döneminizde sadece tek bir alana sıkışmamak için genel dava yükü olan prestijli hukuk bürolarını tercih edin. İleride uzmanlaşacağınız dalı (Bilişim, Ceza, Ticaret) seçin.",
        "seeker": "Baro levhasına kaydınızı takiben, kurumsal şirketlerin hukuk departmanlarını veya spesifik alanlarda (örneğin KVKK, Deniz Ticareti) uzmanlaşmış niş büroları hedefleyen CV'ler hazırlayın.",
        "follow": ["Prof. Dr. Kemal Gözler", "Hukuk Gündemi", "Türkiye Barolar Birliği"],
        "videos": ["Hukukta Uzmanlık Alanı Nasıl Seçilir?", "Etkili Dava Dosyası İnceleme Yöntemleri"]
    },
    "Gastronomi ve Mutfak Sanatları (Aşçılık)": {
        "type": "Lisans",
        "student": "Temel Fransız kesim tekniklerini, sos reçetelerini ve mutfakta hijyen/sanitasyon kurallarını refleks haline getirin. Okul dışı zamanlarda otel ve restoran mutfaklarında gönüllü çalışın.",
        "grad": "Mutfak hiyerarşisinde 'Commis' (çırak) olarak başlamaya zihnen hazırlanın. İstasyon rotasyonlarına (sıcak, soğuk, pastane) sadık kalarak her alanda temel pratik kazanın.",
        "seeker": "Özgün bir portfolyo oluşturun (hazırladığınız tabakların profesyonel fotoğrafları ve reçete detayları). Fine-dining restoranlar, lüks oteller ve kurumsal catering şirketlerine doğrudan mutfak mülakatı talep ederek başvurun.",
        "follow": ["Mutfak Sanatları Akademisi (MSA)", "Chef's Table", "Şef Mehmet Yalçınkaya"],
        "videos": ["Profesyonel Mutfakta İstasyon Yönetimi", "Temel Fransız Soslarının Yapılışı ve Püf Noktaları"]
    },
    "Diş Hekimliği": {
        "type": "Lisans",
        "student": "Preklinik derslerinde el becerinizi geliştirmek için maksimum zaman harcayın. Fantom laboratuvar çalışmalarını ciddiye alın ve klinik stajlarda hastalarla iletişim psikolojisini gözlemleyin.",
        "grad": "DUS (Diş Hekimliğinde Uzmanlık Sınavı) rotasını çizip çizmeme kararını verin. Güncel estetik kompozit ve implantoloji kurslarını yakından takip edin.",
        "seeker": "Özel diş poliklinikleri ve estetik merkezlerine başvuru yaparken, okulda yaptığınız başarılı protetik ve endodontik tedavilerin görsellerinden oluşan bir mini portfolyo sunun.",
        "follow": ["Türk Dişhekimleri Birliği (TDB)", "Dental Tribune Türkiye", "Dr. Diş Hekimi Ortodontist Hesapları"],
        "videos": ["Endodontide Kanala Şekil Verme Teknikleri", "Estetik Kompozit Dolgu Uygulamaları"]
    },
    "Eczacılık": {
        "type": "Lisans",
        "student": "Farmakoloji, farmasötik kimya ve botanik derslerine odaklanın. İlaç etkileşimlerini ve etken maddelerin kimyasal yapılarını çok iyi kavrayın.",
        "grad": "Serbest eczane açma, endüstriyel eczacılık (ilaç firmalarında AR-GE, ruhsatlandırma) veya hastane eczacılığı arasında stratejik bir seçim yapın.",
        "seeker": "Global ilaç firmalarının 'Medical Advisor' veya ruhsatlandırma departmanlarındaki ilanlarına başvurun. Serbest eczane için bölge analizleri gerçekleştirin.",
        "follow": ["Türk Eczacıları Birliği (TEB)", "RxMediaPharma", "İlaç Endüstrisi İşverenler Sendikası"],
        "videos": ["İlaç Sektöründe Eczacı Olmak: AR-GE ve Ruhsatlandırma", "Eczane Yönetimi ve Finansal Süreçler"]
    },
    "Mimarlık": {
        "type": "Lisans",
        "student": "Tasarım stüdyolarında yapıcı eleştirileri sindirmeyi öğrenin. Revit, AutoCAD, Rhino ve Photoshop yazılımlarını profesyonel düzeyde kullanacak şekilde kendinizi eğitin.",
        "grad": "Özgün mimari dilinizi ve teknik çizim yeteneğinizi yansıtan şık bir dijital portfolyo (Behance veya Issuu üzerinden) oluşturun. Ulusal yarışmalara katılın.",
        "seeker": "Tasarım ofisleri ve şantiyelerin ilgili departmanlarına hazırladığınız özel tasarım kitabıyla başvurun. Görüşmelerde projelerinizin hikayesini ön plana çıkarın.",
        "follow": ["Mimarlık Arşivi", "Arkitera", "Tasarım Günlüğü"],
        "videos": ["Sıfırdan Etkili Mimari Portfolyo Hazırlama", "Revit ile Detaylı Proje Modelleme Adımları"]
    },
    "Psikoloji": {
        "type": "Lisans",
        "student": "İstatistik ve araştırma yöntemleri derslerini hafife almayın. Klinik, gelişim, sosyal veya endüstriyel psikoloji gibi alt dalların makalelerini düzenli tarayın.",
        "grad": "Klinik psikolog olmak istiyorsanız akredite bir yüksek lisans programına kabul edilmek için hazırlık yapın. Geçerliliği olan ölçek ve test eğitimlerini (MMPI vb.) edinin.",
        "seeker": "Rehabilitasyon merkezleri, özel klinikler, anaokulları veya kurumsal şirketlerin insan kaynakları (işe alım/organizasyonel gelişim) departmanlarını hedefleyin.",
        "follow": ["Prof. Dr. Acar Baltaş", "Beyhan Budak", "Türk Psikologlar Derneği"],
        "videos": ["Psikolojide Ekol Seçimi ve Terapi Yaklaşımları", "Etkili Seans Yönetimi ve Etik Kurallar"]
    },
    "PDR (Psikolojik Danışmanlık ve Rehberlik)": {
        "type": "Lisans",
        "student": "Okullarda yapılan gözlem stajlarını çok verimli geçirin. Çocuk ve ergen psikolojisi, aile danışmanlığı yaklaşımları üzerine ek okumalar yapın.",
        "grad": "MEB atamaları için KPSS çalışmalarına başlayın. Özel sektör düşünülüyorsa, çocuk merkezli oyun terapisi veya çözüm odaklı kısa süreli terapi eğitimleri alın.",
        "seeker": "Özel kolejler, rehberlik ve araştırma merkezleri (RAM) ile kurumsal etüt merkezlerine başvurun. Eğitim teknolojilerine ve mentörlük programlarına hakimiyetinizi gösterin.",
        "follow": ["PDR Derneği", "Eğitim Ajansı", "Pedagog/Danışman Hesapları"],
        "videos": ["Okullarda Kriz Yönetimi ve Psikolojik Danışmanlık", "Çözüm Odaklı Kısa Süreli Terapi Teknikleri"]
    },
    "İşletme": {
        "type": "Lisans",
        "student": "Pazarlama, finans, muhasebe ve İK gibi tüm kurumsal departmanları tanıyın. Sunum yapma becerinizi üst seviyeye taşımak için vaka analiz kulüplerine girin.",
        "grad": "Uzmanlaşmak istediğiniz departmanı seçip kurumsal şirketlerin 'Management Trainee' (MT) sınav ve mülakat süreçlerine hazırlanın. İleri düzey Excel öğrenin.",
        "seeker": "LinkedIn profilinizi optimize edin. Şirketlerin başlangıç pozisyonlarına (Analist, Uzman Yardımcısı) başvururken staj projelerinizdeki sayısal başarılarınızı (örn: %10 maliyet tasarrufu sağlandı) belirtin.",
        "follow": ["Hakan Selahi", "Pazarlama Türkiye", "Harvard Business Review Türkiye"],
        "videos": ["Management Trainee (MT) Mülakatlarına Nasıl Hazırlanılır?", "Sıfırdan Kurumsal Finansal Okuryazarlık"]
    },
    "İktisat (Ekonomi)": {
        "type": "Lisans",
        "student": "Ekonometri ve veri analizi yazılımlarına (R, Python, Stata) yatırım yapın. Makroekonomik gelişmeleri dünya ölçeğinde analiz etme alışkanlığı edinin.",
        "grad": "Bankacılık, finansal danışmanlık, SPK lisanslama süreçleri veya kamu müfettiş yardımcılığı sınavları arasından kariyer yolunuzu netleştirin.",
        "seeker": "Aracı kurumlar, bankalar, denetim firmaları (Big Four) ve araştırma departmanlarına başvurun. Finansal modelleme yeteneğinizi CV'nizde öne çıkarın.",
        "follow": ["Dr. Mahfi Eğilmez", "Prof. Dr. Özgür Demirtaş", "Bloomberg HT"],
        "videos": ["Ekonometrik Modelleme ve Veri Analizi Giriş", "Dünya Ekonomisi ve Finansal Piyasaları Okuma Hizası"]
    },
    "Uluslararası İlişkiler": {
        "type": "Lisans",
        "student": "Siyasi tarih ve küresel diplomasi teorilerini derinlemesine okuyun. En az iki yabancı dili çok iyi derecede (C1/C2) konuşup yazacak seviyeye gelin.",
        "grad": "Dışişleri Bakanlığı aday meslek memurluğu sınavlarını, Avrupa Birliği projelerini ve uluslararası sivil toplum kuruluşlarının (STK) fon yapılarını araştırın.",
        "seeker": "Çok uluslu şirketlerin dış ticaret, kurumsal iletişim, sürdürülebilirlik departmanlarına veya düşünce kuruluşlarına (think-tank) analist olarak başvurun.",
        "follow": ["İlber Ortaylı", "T.C. Dışişleri Bakanlığı", "Foreign Affairs Türkiye Analizleri"],
        "videos": ["Konsolosluk ve Diplomatlık Sınavları Hazırlık Süreci", "Uluslararası STK'larda Proje Yönetimi"]
    },
    "Hemşirelik": {
        "type": "Lisans",
        "student": "Anatomi, farmakoloji ve temel cerrahi esasları derslerinin laboratuvar pratiklerine eksiksiz katılın. Klinik stajlarda el becerinizi geliştirmek için inisiyatif alın.",
        "grad": "Yoğun Bakım Hemşireliği, Ameliyathane Hemşireliği veya Yenidoğan Hemşireliği gibi spesifik alan sertifikasyon programlarına katılarak uzmanlaşın.",
        "seeker": "Devlet atamaları için KPSS'ye hazırlanın. Özel hastane zincirlerinin mülakatlarında kriz anı yönetimi, sabır ve yüksek iletişim becerilerinizi somut örneklerle aktarın.",
        "follow": ["Türk Hemşireler Derneği", "Hemşirelik Akademisi", "Sağlık Bakanlığı Duyuruları"],
        "videos": ["Temel Klinik Müdahaleler ve Hasta Bakım Esasları", "Yoğun Bakım Ünitelerinde Kritik Hasta Takibi"]
    },
    "Beslenme ve Diyetetik (Diyetisyenlik)": {
        "type": "Lisans",
        "student": "Besin kimyası, biyokimya ve hastalıklarda diyet tedavisi derslerini çok iyi öğrenin. Güncel uluslararası beslenme kılavuzlarını (ESPEN, ASPEN) takip edin.",
        "grad": "Hastanelerin klinik beslenme birimlerinde veya bariatrik cerrahi merkezlerinde gönüllü staj sürelerinizi uzatın. Sosyal medyada bilimsel ve etik içerik üretmeye başlayın.",
        "seeker": "Diyet klinikleri, spor salonları, catering/toplu beslenme firmalarına başvurun veya kendi online/yüz yüze danışmanlık merkezinizi açmak için bir iş planı oluşturun.",
        "follow": ["Diyetisyen Dünyası", "Türkiye Diyetisyenler Derneği", "Klinik Beslenme Hesapları"],
        "videos": ["Klinik Beslenmede Güncel Vaka Analizleri", "Diyetisyenler İçin Dijital Markalaşma ve Danışan Yönetimi"]
    },
    "Fizyoterapi ve Rehabilitasyon (FTR)": {
        "type": "Lisans",
        "student": "Kinezyoloji, anatomi ve nörolojik rehabilitasyon derslerinin pratik uygulamalarında yetkinleşin. Manuel terapi tekniklerini yakından inceleyin.",
        "grad": "Pediatrik, ortopedik veya sporcu fizyoterapistliği alanlarından birini seçin. Uluslararası geçerliliği olan osteopati veya kuru iğneleme gibi ek eğitimleri araştırın.",
        "seeker": "Fizik tedavi merkezleri, kaplıcalar, spor kulüpleri ve özel eğitim rehabilitasyon merkezlerinin ilanlarına odaklanarak pratik uygulama tecrübelerinizi aktarın.",
        "follow": ["Türkiye Fizyoterapistler Derneği", "Physiopedia", "Sporcu Sağlığı Portalları"],
        "videos": ["Ortopedik Rehabilitasyonda Manuel Terapi Teknikleri", "Sporcu Yaralanmalarında Güncel Dönüş Protokolleri"]
    },
    "Veteriner Hekimlik": {
        "type": "Lisans",
        "student": "Küçük ve büyük baş hayvan anatomisini, fizyolojisini ve farmakolojisini iyi kıyaslayın. Cerrahi ve iç hastalıkları klinik saatlerini verimli geçirin.",
        "grad": "Pet klinisyenliği (kedi-köpek) mi, çiftlik hayvanları mı yoksa gıda hijyeni/endüstrisi alanına mı yöneleceğinize karar verip klinik vizyonunuzu netleştirin.",
        "seeker": "Hayvan hastanelerine, veteriner polikliniklerine veya tarım/hayvancılık entegre tesislerine başvurun. Operasyonel cerrahi özgüveninizi mülakatlarda yansıtın.",
        "follow": ["Türk Veteriner Hekimleri Birliği", "Veteriner Cerrahi Derneği", "Pet Sağlığı Platformları"],
        "videos": ["Kedi ve Köpeklerde Temel Cerrahi Yaklaşımlar", "Büyükbaş Hayvanlarda Sık Görülen İç Hastalıkları Tanısı"]
    },
    "Moleküler Biyoloji ve Genetik": {
        "type": "Lisans",
        "student": "Hücre kültürü, PCR, jel elektroforezi ve DNA/RNA izolasyon tekniklerini laboratuvarda bizzat uygulayarak öğrenin. İngilizce makale tarama hızınızı artırın.",
        "grad": "Akademik kariyer için yüksek lisans/doktora başvuruları (ALES, YDS, TOEFL) yapın. Endüstri düşünülüyorsa, Python/R ile biyoenformatik araçlarını öğrenin.",
        "seeker": "Biyoteknoloji girişimleri, tüp bebek merkezleri, ilaç AR-GE laboratuvarları ve genetik tanı merkezlerindeki araştırmacı/teknisyen ilanlarına başvurun.",
        "follow": ["Evrim Ağacı", "Geleceğin Bilimi Platformu", "Nature Genetics"],
        "videos": ["Biyoenformatik Analiz Araçları ve R Kullanımı", "CRISPR-Cas9 Gen Düzenleme Teknolojisi Detayları"]
    },
    "Grafik Tasarım": {
        "type": "Lisans",
        "student": "Tipografi, renk teorisi, kompozisyon görsel dilini özümseyin. Adobe Photoshop, Illustrator ve InDesign programlarına tamamen hakim olun.",
        "grad": "Behance ve Dribbble profillerinizi en iyi işlerinizle güncelleyin. Trend olan UI/UX tasarımı veya 3D modelleme/illüstrasyon alanlarında kendinizi geliştirin.",
        "seeker": "Reklam ajansları, kurumsal markaların pazarlama departmanları ve e-ticaret şirketlerine güncel tasarım portfolyonuzun yer aldığı dijital link ile başvurun.",
        "follow": ["Tasarımcı Dayı", "Afgan Rasulov", "Behance Featured"],
        "videos": ["Sıfırdan Marka Kimliği ve Logo Tasarım Süreçleri", "Göz Alıcı Dijital Portfolyo Nasıl Tasarlanır?"]
    },
    "Yeni Medya ve İletişim": {
        "type": "Lisans",
        "student": "Dijital yayıncılık, sosyal medya algoritmaları, kriz iletişimi ve temel video kurgu programlarını (Adobe Premiere, After Effects) öğrenin.",
        "grad": "Google Analytics, Meta Ads Manager ve SEO (Arama Motoru Optimizasyonu) araçlarında uzmanlaşarak saygın kurumlardan sertifikalar edinin.",
        "seeker": "Dijital reklam ajansları, medya kuruluşları ve şirketlerin kurumsal iletişim birimlerinde 'Sosyal Medya Yöneticisi' veya 'İçerik Stratejisti' olarak iş arayın.",
        "follow": ["Pazarlamasyon", "Ecehan Ersöz", "Dijital Medya Araştırmaları"],
        "videos": ["Sıfırdan Profesyonel Google Ads Reklam Yönetimi", "SEO Uyumlu İçerik Yazarlığı ve Stratejisi"]
    },
    "İngiliz Dili ve Edebiyatı": {
        "type": "Lisans",
        "student": "Klasik ve modern dönem edebi metinlerini eleştirel analiz yöntemleriyle okuyun. Dil yetkinliğinizi akademik yazım (Academic Writing) seviyesine taşıyın.",
        "grad": "Formasyon alarak öğretmenliğe geçebilir veya simultane çeviri, teknik metin yazarlığı, içerik editörlüğü sertifikalarına yönelebilirsiniz.",
        "seeker": "Özel kolejler, dil kursları, çeviri büroları, yayınevleri ve dış ticaret şirketlerinin uluslararası operasyon/yazışma pozisyonlarına müracaat edin.",
        "follow": ["British Council Turkey", "Akademik Dil Portalı", "Literature Hub"],
        "videos": ["Simultane ve Ardıl Çeviri Teknikleri Eğitimi", "Metin Yazarlığı ve İçerik Editörlüğüne Giriş"]
    },
    "Sınıf Öğretmenliği": {
        "type": "Lisans",
        "student": "Çocuk psikolojisi, oyun temelli öğrenme modelleri ve sınıf yönetimi teorilerini öğrenin. Eğitici materyal geliştirme süreçlerinde yaratıcı olun.",
        "grad": "MEB güncel ilkokul müfredatını hatasız inceleyin. KPSS Eğitim Bilimleri, Genel Kültür-Genel Yetenek ve ÖABT (Alan Sınavı) hazırlıklarına odaklanın.",
        "seeker": "Devlet kadroları için atama süreçlerini takip edin. Özel ilkokullar ve kolej mülakatları için yaratıcı bir 'Örnek Demo Ders Anlatımı' tasarlayarak başvurun.",
        "follow": ["Eğitim Bilişim Ağı (EBA)", "Milli Eğitim Bakanlığı (MEB)", "Eğitim Dünyası Platformları"],
        "videos": ["İlk Okuma Yazma Öğretimi Aşamaları ve Teknikleri", "İlkokulda İnteraktif Sınıf Yönetimi Stratejileri"]
    },

    # --- ÖNLİSANS BÖLÜMLERİ ---
    "Bilgisayar Programcılığı": {
        "type": "Önlisans",
        "student": "Algoritma mantığını oturtun, veri tabanı mimarilerini (SQL) öğrenin. DGS (Dikey Geçiş Sınavı) planınız varsa matematik temeli kurun.",
        "grad": "Web geliştirme (HTML, CSS, JavaScript) veya mobil programlama alanında pratik 3-4 projeyi uçtan uca tamamlayıp GitHub profilinizde yayınlayın.",
        "seeker": "Junior Front-End/Back-End Developer ilanlarını tarayın. Teknik mülakatlarda kodlama hızınızı ve problem çözme mantığınızı açıkça sergileyin.",
        "follow": ["Sadık Turan", "Murat Yücedağ", "Yazılım Bilimi"],
        "videos": ["Sıfırdan Komple Web Geliştirme Yol Haritası", "İleri Düzey SQL Sorgulama ve Veri Tabanı Tasarımı"]
    },
    "Bilişim Güvenliği Teknolojisi": {
        "type": "Önlisans",
        "student": "Ağ temellerini (TCP/IP, OSI katmanları), Linux işletim sistemi yönetimini ve siber güvenlik temel kavramlarını (SIEM, Güvenlik Duvarı) hatasız öğrenin.",
        "grad": "TryHackMe ve HackTheBox gibi pratik lab platformlarında aktif hacking/savunma senaryoları çözün. Siber güvenlik sertifikalarını (CEH, Security+) inceleyin.",
        "seeker": "Şirketlerin Güvenlik Operasyon Merkezlerinde (SOC) 'Giriş Seviyesi Siber Güvenlik Analisti' veya sızma testi ekiplerinde asistan rollerine başvurun.",
        "follow": ["Can Değer", "Siber Güvenlik Kümelenmesi", "Gökhan Muharremoğlu"],
        "videos": ["Sıfırdan Siber Güvenlik ve Pentest Yol Haritası", "Sistem Yönetimi İçin Temel Linux Komut Satırı Eğitimi"]
    },
    "Mekatronik": {
        "type": "Önlisans",
        "student": "PLC programlama (Siemens vb.), endüstriyel otomasyon sistemleri ve hidrolik-pnömatik sistem devre şemalarını okumayı çok iyi öğrenin.",
        "grad": "Otomasyon atölyelerinde veya üretim hatlarında pratik saha deneyimi kazanın. Arduino ve Raspberry Pi ile mikrodenetleyici projeleri geliştirin.",
        "seeker": "Organize sanayi bölgelerindeki fabrikaların bakım-onarım, otomasyon teknikeri veya AR-GE teknisyeni açık pozisyonlarına doğrudan başvurun.",
        "follow": ["Robotistan", "Otomasyon Merkezi Dünyası", "Endüstri 4.0 Platformları"],
        "videos": ["Sıfırdan Endüstriyel PLC Programlama Dersleri", "Fabrika Otomasyon Hatları ve Mekanik Bakım Esasları"]
    },
    "Anestezi": {
        "type": "Önlisans",
        "student": "Anestezi cihazlarının iç yapısını, gaz sistemlerini ve operasyonel farmakolojik ilaç dozajlama hesaplamalarını hatasız yapmayı öğrenin.",
        "grad": "Hastanelerin yoğun cerrahi operasyon yapılan ameliyathanelerinde gönüllü stajyerlik yaparak hız, soğukkanlılık ve vaka deneyimi edinin.",
        "seeker": "Kamu atamaları için KPSS önlisans sınavına girin. Özel hastanelerin ameliyathane koordinatörlüklerine başvurarak pratik cihaz bilginizi vurgulayın.",
        "follow": ["Anestezi Teknisyenleri ve Teknikerleri Derneği", "Sağlık Platformları"],
        "videos": ["Anestezi Cihazı Kurulumu ve Kontrol Adımları", "Ameliyathane Rutininde Entübasyon ve Monitorizasyon"]
    },
    "İlk ve Acil Yardım (Paramedik)": {
        "type": "Önlisans",
        "student": "İleri yaşam desteği protokollerini, EKG okuma tekniklerini, travmalı hastaya ilk müdahale adımlarını kusursuz öğrenin. Kondisyonunuzu yüksek tutun.",
        "grad": "Ambulans Sürüş Teknikleri (ASTE) eğitim modüllerini inceleyin. Stres altında anlık doğru kararlar verme simülasyonları yapın.",
        "seeker": "112 Acil Sağlık Hizmetleri istasyonları, özel ambulans şirketleri ve özel hastanelerin acil servis kadrolarına başvuruda bulunun.",
        "follow": ["Paramedik Derneği (PARDER)", "Acil Tıp Teknikerleri Platformu"],
        "videos": ["Kritik Hastada Temel ve İleri Yaşam Desteği (CPR)", "Ambulans İçi Tıbbi Ekipmanların Fonksiyonel Kullanımı"]
    },
    "Grafik Tasarımı (Önlisans)": {
        "type": "Önlisans",
        "student": "2 yıllık kısıtlı sürede hızla portfolyo biriktirmeye bakın. Adobe Photoshop ve Illustrator kısayollarına ve baskı hazırlık süreçlerine odaklanın.",
        "grad": "Matbaa teknikleri, kurumsal kimlik paketleri ve e-ticaret siteleri için banner/sosyal medya görsel üretim süreçlerinde hız kazanın.",
        "seeker": "Yerel reklam ajansları, dijital baskı merkezleri, tekstil desen stüdyoları ve e-ticaret firmalarının kreatif ekiplerine başvurun.",
        "follow": ["Tasarım Fikirleri", "Grafikerler Kulübü Platformu"],
        "videos": ["Photoshop Hızlı Görsel Manipülasyon ve Dekupe Teknikleri", "Matbaa İçin Baskıya Hazır Dosya Çıkışı Hazırlama"]
    },
    "Dış Ticaret": {
        "type": "Önlisans",
        "student": "Gümrük mevzuatını, uluslararası teslim şekillerini (Incoterms 2020) ve akreditifli ödeme yöntemlerinin operasyonel işleyişini kavrayın.",
        "grad": "Mesleki dış ticaret İngilizcesi ve ticari yazışma dil kurallarını öğrenin. İthalat/ihracat beyannamelerini okuma pratikleri yapın.",
        "seeker": "Gümrük müşavirlikleri, lojistik firmaları ve üretim yapıp yurt dışına ihracat gerçekleştiren şirketlerin operasyon ekiplerine başvurun.",
        "follow": ["Gümrük TV", "Dış Ticaret Enstitüsü Portalı", "İhracatçılar Birlikleri"],
        "videos": ["Incoterms 2020 Teslim Şekilleri Detaylı Anlatım", "Gümrük Beyannamesi Nasıl Doldurulur ve Okunur?"]
    },
        "Lojistik": {
        "tür": "Önlisans",
        "öğrenci": "Tedarik zinciri yönetimi, depo yerleşim düzeni, stok kontrol sistemleri ve ERP/WMS (Depo Yönetim Sistemleri) yazılımlarının mantığını öğrenin.",
        "mezun": "Gümrüklü antrepo süreçlerini ve küresel taşımacılık (denizyolu, havayolu, demiryolu) rotasyon planlama araçlarını öğrenerek pratik kazanın.",
        "iş_arayan": "Uluslararası kargo şirketleri, liman işletmeleri, dağıtım merkezleri ve büyük perakende markalarının lojistik/depo operasyon sorumluluğu ilanlarına başvurun.",
        "takip": ["Lojistik Derneği (LODER)", "Lojistik Dünyası Yayınları"],
        "video": ["Depo Yönetim Sistemleri (WMS) Program Kullanımı", "Uluslararası Nakliye ve Rota Optimizasyonu Nasıl Yapılır?"]
    },
    "Makine Mühendisliği": {
        "tür": "Lisans",
        "öğrenci": "SolidWorks, AutoCAD veya CATIA gibi CAD programlarını ileri düzeyde öğrenin. Termodinamik, akışkanlar mekaniği temellerini sağlam tutun.",
        "mezun": "Üretim, AR-GE, bakım-onarım veya kalite kontrol alanlarından birini seçin. Ansys veya HyperMesh ile sonlu elemanlar analizine (FEA) giriş yapın.",
        "iş_arayan": "Otomotiv, beyaz eşya, savunma sanayisi ve üretim fabrikalarındaki açık pozisyonları inceleyin. Tasarım portfolyonuzu PDF/görsel olarak sunun.",
        "takip": ["Makine Mühendisi TV", "CadCam Hocası YouTube", "TMMOB Makina Mühendisleri Odası"],
        "video": ["SolidWorks Sıfordan Parça Modelleme", "Makine Mühendisleri İçin AR-GE Tasarım Stratejileri"]
    },
    "Mekatronik Teknikerliği": {
        "tür": "Önlisans",
        "öğrenci": "PLC programlama, endüstriyel otomasyon, Arduino/Raspberry Pi uygulamaları ve temel elektrik-mekanik şemalarını hatasız okumayı öğrenin.",
        "mezun": "Fabrika otomasyon sistemleri, hidrolik-pnömatik sistemler and robotik kollarla ilgili pratik saha bakım bilgilerini edinmeye çalışın.",
        "iş_arayan": "Bakım onarım teknisyeni, otomasyon teknikeri pozisyonları için organize sanayi bölgelerindeki fabrikaların ilanlarını tarayın.",
        "takip": ["Robotistan", "Otomasyon Merkezi Kulübü"],
        "video": ["Sıfırdan PLC Programlama Temelleri", "Endüstriyel Robotik Sistemler ve Bakım Esasları"]
    },
    "Mimarlık": {
        "tür": "Lisans",
        "öğrenci": "Estetik ve mekânsal algınızı besleyin. Revit, Rhino, AutoCAD, Photoshop ve 3ds Max gibi tasarım ve 3D görselleştirme araçlarına hakim olun.",
        "mezun": "Özgün mimari dilinizi ve teknik çizim yeteneğinizi yansıtan şık bir dijital portfolyo (Behance veya Issuu üzerinden) hazırlayın.",
        "iş_arayan": "Mimarlık ve tasarım ofislerine, şantiyelere başvurun. Portfolyonuzu yüz yüze mülakatlarda konsept hikayeleriyle anlatın.",
        "takip": ["Mimarlık Arşivi", "Arkitera", "Tasarım Günlüğü"],
        "video": ["Profesyonel Mimari Portfolyo Nasıl Hazırlanır?", "Revit ile BIM Tabanlı Modelleme Esasları"]
    },
    "Moleküler Biyoloji ve Genetik": {
        "tür": "Lisans",
        "öğrenci": "Laboratuvar tekniklerini (PCR, jel elektroforezi, klonlama) çok iyi öğrenin. İngilizce makale tarama ve literatür okuma becerinizi geliştirin.",
        "mezun": "Yurt içi/yurt dışı akademik laboratuvarlara staj başvurusu yapın. Biyoenformatik veri analiz araçlarını (Python, R, BLAST) öğrenmeye başlayın.",
        "iş_arayan": "Biyoteknoloji Ar-Ge firmaları, tüp bebek merkezleri, ilaç şirketleri ve tanı laboratuvarlarındaki araştırmacı pozisyonlarına müracaat edin.",
        "takip": ["Evrim Ağacı", "Geleceğin Bilimi Topluluğu", "Nature Genetics"],
        "video": ["Biyoenformatik Dünyasına ve Kodlamaya Giriş", "CRISPR Teknolojisi ve Laboratuvar Uygulama Rutinleri"]
    },
    "Psikoloji": {
        "tür": "Lisans",
        "öğrenci": "Teorik altyapıyı sağlam kurun. Klinik, endüstriyel, gelişim veya sosyal psikoloji gibi alt alanlardan hangisine ilginiz olduğunu keşfedin.",
        "mezun": "Klinik hedefliyorsanız yüksek lisans (Master) rotanızı hemen çizin. Gönüllü projelerde yer alın ve akredite kurumlardan test eğitimleri alın.",
        "iş_arayan": "Özel klinikler, danışmanlık merkezleri, hastaneler, anaokulları veya kurumsal şirketlerin insan kaynakları (İK) departmanlarını hedefleyin.",
        "takip": ["Acar Baltaş", "Beyhan Budak", "Türk Psikologlar Derneği"],
        "video": ["Psikolojide Ekol Seçimi ve Eğitim Süreçleri", "Etkili İletişim ve Aktif Dinleme Teknikleri"]
    },
    "Sınıf Öğretmenliği": {
        "tür": "Lisans",
        "öğrenci": "Çocuk psikolojisi, pedagoji ve alternatif eğitim modellerini (Montessori, Waldorf) araştırın. İlkokul materyal geliştirme becerisi edinin.",
        "mezun": "Milli Eğitim Bakanlığı (MEB) güncel müfredatını derinlemesine inceleyin. KPSS eğitim bilimleri ve ÖABT (Alan Sınavı) hazırlıklarına odaklanın.",
        "iş_arayan": "Devlet kadroları için KPSS'ye girin; özel okullar, etüt merkezleri ve kolejlerin mülakatları için etkili örnek (demo) dersler hazırlayın.",
        "takip": ["Eğitim Bilişim Ağı (EBA)", "Öğretmenler Sitesi", "Milli Eğitim Bakanlığı"],
        "video": ["İlkokulda İlk Okuma Yazma Öğretimi Teknikleri", "Sınıf Yönetimi ve Pozitif Disiplin Stratejileri"]
    },
    "Yeni Medya ve İletişim": {
        "tür": "Lisans",
        "öğrenci": "Sosyal medya algoritmalarını, dijital pazarlamayı, kriz yönetimini ve temel video kurgu programlarını (Adobe Premiere, CapCut) öğrenin.",
        "mezun": "SEO, Google Analytics ve Meta Ads panellerini kullanmayı öğrenerek global geçerliliği olan sertifikalar alın. Kendi dijital içerik markanızı yaratın.",
        "iş_arayan": "Dijital reklam ajanslarında Sosyal Medya Yöneticisi, İçerik Üreticisi, SEO Uzman Yardımcısı veya Dijital İletişim Sorumlusu olarak iş arayın.",
        "takip": ["Pazarlamasyon", "Ecehan Ersöz", "Dijital Pazarlama Okulu"],
        "video": ["Google Ads Reklam Kurulumu ve Strateji Rehberi", "Sıfırdan SEO (Arama Motoru Optimizasyonu) Temelleri"]
    }
}

# Şık Bölüm Seçim Kutusu (Arama Özellikli)
seçilen_bölüm = st.selectbox(
    "💡 Tavsiyelerini görmek istediğiniz bölümü seçin:",
    options=["-- Bölüm Seçiniz --"] + list(data.keys()),
    index=0
)

# Seçim Yapıldığında Dinamik İçerik Gösterimi
if seçilen_bölüm != "-- Bölüm Seçiniz --":
    veri = data[seçilen_bölüm]
    
    st.write(f"**Eğitim Seviyesi:** `{veri['tür']}`")
    st.markdown("<hr style='margin-top: 10px; margin-bottom: 20px; border-color: #e9ecef;'>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="info-card">
            <div class="card-heading">👨‍🎓 Öğrenci İçin Yol Haritası</div>
            <div class="card-text">{veri['öğrenci']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="info-card">
            <div class="card-heading">🎓 Yeni Mezun İçin Stratejiler</div>
            <div class="card-text">{veri['mezun']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="info-card">
            <div class="card-heading">💼 İş Arayan İçin İpuçları</div>
            <div class="card-text">{veri['iş_arayan']}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='meta-box'>", unsafe_allow_html=True)
    st.markdown("<div class='meta-title'>🔍 Kimleri / Hangi Kurumları Takip Etmeli?</div>", unsafe_allow_html=True)
    for t in veri['takip']:
        st.markdown(f"<div class='meta-item'>• {t}</div>", unsafe_allow_html=True)
        
    st.markdown("<div class='meta-title' style='margin-top:12px;'>📺 YouTube'da Hangi Konuları Araştırmalı?</div>", unsafe_allow_html=True)
    for v in veri['video']:
        st.markdown(f"<div class='meta-item'>• {v}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Lütfen asistanın tavsiyelerini, takip listelerini ve video önerilerini görüntülemek için yukarıdaki menüden bir meslek/bölüm seçiniz.")
