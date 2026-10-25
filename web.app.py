"""
Akıllı Kariyer Asistanı - Kurulum Betiği

Kullanım:
  1) npx create-next-app@latest kariyer-asistani
     (TypeScript: Yes, ESLint: Yes, Tailwind: Yes, src/: No, App Router: Yes)
  2) Bu dosyayı kariyer-asistani klasörünün içine koy
  3) python kurulum.py

Betik, projenin tüm dosyalarını oluşturur ve @supabase/supabase-js paketini kurar.
"""

import subprocess
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent

DOSYALAR = {}

# ---------------------------------------------------------------- ortam
DOSYALAR[".env.example"] = r"""NEXT_PUBLIC_SUPABASE_URL=https://PROJE_ID.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=senin_anon_anahtarin
ANTHROPIC_API_KEY=senin_claude_api_anahtarin
# Istege bagli: kullanilacak model
# CLAUDE_MODEL=claude-sonnet-5-5
"""

# ---------------------------------------------------------------- supabase istemcisi
DOSYALAR["lib/supabase.ts"] = r"""import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);
"""

# ---------------------------------------------------------------- tema
DOSYALAR["app/globals.css"] = r"""@import "tailwindcss";

:root {
  --bg: #F4F4F2;
  --kart: #E8E8E4;
  --metin: #333333;
  --gece: #2C3E50;
  --adacayi: #7D8C7A;
}

body {
  background: var(--bg);
  color: var(--metin);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
"""

DOSYALAR["app/layout.tsx"] = r"""import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Akıllı Kariyer Asistanı",
  description:
    "Önlisans ve lisans öğrencileri için bölümüne özel yol haritası, takip listesi ve yapay zeka mentor.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="tr">
      <body>
        <main className="mx-auto max-w-3xl px-5 py-10">{children}</main>
      </body>
    </html>
  );
}
"""

# ---------------------------------------------------------------- ana sayfa
DOSYALAR["app/page.tsx"] = r"""
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  const [derece, setDerece] = useState("onlisans");
  const [bolum, setBolum] = useState("");

  function gonder(e: React.FormEvent) {
    e.preventDefault();
    if (!bolum.trim()) return;
    router.push(
      `/panel?derece=${derece}&bolum=${encodeURIComponent(bolum.trim())}`
    );
  }

  return (
    <div>
      <h1 className="mb-2 text-3xl font-bold text-[#2C3E50]">
        Akıllı Kariyer Asistanı
      </h1>
      <p className="mb-8 max-w-prose">
        Diplomadan sonra ne yapacağını bilmek için bölümünü seç. Dönem dönem
        yol haritanı ve takip etmen gereken kişileri gör.
      </p>

      <form
        onSubmit={gonder}
        className="grid gap-3 rounded-xl bg-[#E8E8E4] p-5"
      >
        <label className="grid gap-1 text-sm">
          Eğitim düzeyi
          <select
            value={derece}
            onChange={(e) => setDerece(e.target.value)}
            className="rounded-lg border border-[#cfcfc8] bg-[#F4F4F2] px-3 py-2 text-base"
          >
            <option value="onlisans">Önlisans (2 yıl)</option>
            <option value="lisans">Lisans (4 yıl)</option>
          </select>
        </label>

        <label className="grid gap-1 text-sm">
          Bölümün
          <input
            type="text"
            value={bolum}
            onChange={(e) => setBolum(e.target.value)}
            placeholder="Örn. Bilgisayar Programcılığı"
            className="rounded-lg border border-[#cfcfc8] bg-[#F4F4F2] px-3 py-2 text-base"
          />
        </label>

        <button
          type="submit"
          className="mt-2 rounded-lg bg-[#2C3E50] px-4 py-2 text-[#F4F4F2] hover:opacity-90"
        >
          Koçluk ekranını aç
        </button>
      </form>
    </div>
  );
}
"""

# ---------------------------------------------------------------- panel (sunucu)
DOSYALAR["app/panel/page.tsx"] = r"""
import Link from "next/link";
import { supabase } from "@/lib/supabase";
import Panel from "./Panel";

export const dynamic = "force-dynamic";

export default async function PanelSayfasi({
  searchParams,
}: {
  searchParams: Promise<{ derece?: string; bolum?: string }>;
}) {
  const { derece = "onlisans", bolum = "" } = await searchParams;

  const { data: bolumler } = await supabase
    .from("bolumler")
    .select("bolum_id, bolum_adi, derece_turu")
    .ilike("bolum_adi", bolum)
    .eq("derece_turu", derece)
    .limit(1);

  const kayit = bolumler?.[0];
  let adimlar = [];
  let mentorlar = [];

  if (kayit) {
    const { data: a } = await supabase
      .from("yol_haritasi_adimlari")
      .select("adim_id, donem, sira, aciklama")
      .eq("bolum_id", kayit.bolum_id)
      .order("sira");
    adimlar = a ?? [];

    const { data: m } = await supabase
      .from("bolum_mentor_baglantisi")
      .select(
        "takip_edilecekler(mentor_id, isim_unvan, platform, profil_linki, neden_takip_etmeli, sana_ne_katar)"
      )
      .eq("bolum_id", kayit.bolum_id);
    mentorlar = (m ?? []).flatMap((r) =>
      Array.isArray(r.takip_edilecekler)
        ? r.takip_edilecekler
        : [r.takip_edilecekler]
    );
  }

  return (
    <div>
      <Link href="/" className="text-sm underline">
        Bölümü değiştir
      </Link>
      <Panel
        bolumAdi={kayit?.bolum_adi ?? bolum}
        derece={derece}
        bulundu={!!kayit}
        adimlar={adimlar}
        mentorlar={mentorlar}
      />
    </div>
  );
}
"""

# ---------------------------------------------------------------- panel (istemci)
DOSYALAR["app/panel/Panel.tsx"] = r"""
"use client";

import { useEffect, useState } from "react";

type Adim = { adim_id: string; donem: string; sira: number; aciklama: string };
type Mentor = {
  mentor_id: string;
  isim_unvan: string;
  platform: string;
  profil_linki: string;
  neden_takip_etmeli: string;
  sana_ne_katar: string | null;
};
type Props = {
  bolumAdi: string;
  derece: string;
  bulundu: boolean;
  adimlar: Adim[];
  mentorlar: Mentor[];
};

const SEKMELER = [
  ["yol", "Yol Haritası"],
  ["takip", "Kimi Takip Etmeli?"],
  ["mentor", "Yapay Zeka Mentor"],
] as const;

export default function Panel({
  bolumAdi,
  derece,
  bulundu,
  adimlar,
  mentorlar,
}: Props) {
  const [sekme, setSekme] = useState<string>("yol");
  const [tamam, setTamam] = useState<Record<string, boolean>>({});
  const [soru, setSoru] = useState("");
  const [cevap, setCevap] = useState("");
  const [bekliyor, setBekliyor] = useState(false);

  const anahtar = `ka:${derece}:${bolumAdi}`;

  useEffect(() => {
    try {
      setTamam(JSON.parse(localStorage.getItem(anahtar) || "{}"));
    } catch {
      setTamam({});
    }
  }, [anahtar]);

  function isaretle(id: string, deger: boolean) {
    const yeni = { ...tamam, [id]: deger };
    setTamam(yeni);
    try {
      localStorage.setItem(anahtar, JSON.stringify(yeni));
    } catch {}
  }

  async function sor(e: React.FormEvent) {
    e.preventDefault();
    if (!soru.trim() || bekliyor) return;
    setBekliyor(true);
    setCevap("");
    try {
      const r = await fetch("/api/mentor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ soru, bolum: bolumAdi, derece }),
      });
      const veri = await r.json();
      setCevap(veri.cevap ?? "Cevap alınamadı.");
    } catch {
      setCevap("Bağlantı hatası. Lütfen tekrar dene.");
    }
    setBekliyor(false);
  }

  const gruplar: [string, Adim[]][] = [];
  for (const a of adimlar) {
    const son = gruplar[gruplar.length - 1];
    if (son && son[0] === a.donem) son[1].push(a);
    else gruplar.push([a.donem, [a]]);
  }
  const bitti = adimlar.filter((a) => tamam[a.adim_id]).length;

  return (
    <div>
      <h1 className="mt-4 text-2xl font-bold text-[#2C3E50]">{bolumAdi}</h1>
      <p className="mb-4 text-sm">
        {derece === "lisans" ? "Lisans (4 yıl)" : "Önlisans (2 yıl)"}
      </p>

      <div role="tablist" className="mb-5 flex gap-1 overflow-x-auto border-b border-[#cfcfc8]">
        {SEKMELER.map(([id, ad]) => (
          <button
            key={id}
            role="tab"
            aria-selected={sekme === id}
            onClick={() => setSekme(id)}
            className={`whitespace-nowrap border-b-4 px-4 py-2 text-sm ${
              sekme === id
                ? "border-[#7D8C7A] font-semibold text-[#2C3E50]"
                : "border-transparent"
            }`}
          >
            {ad}
          </button>
        ))}
      </div>

      {!bulundu && sekme !== "mentor" && (
        <p className="rounded-lg bg-[#E8E8E4] p-4">
          Bu bölüm için henüz içerik yok. Veritabanına katkı yaparak ilk
          yol haritasını sen ekleyebilirsin. Yapay zeka mentor sekmesi yine de
          çalışır.
        </p>
      )}

      {bulundu && sekme === "yol" && (
        <div>
          <p className="mb-2">
            {bitti}/{adimlar.length} adım tamamlandı
          </p>
          <div className="mb-6 h-2 overflow-hidden rounded bg-[#E8E8E4]">
            <div
              className="h-full bg-[#7D8C7A]"
              style={{ width: `${adimlar.length ? (bitti / adimlar.length) * 100 : 0}%` }}
            />
          </div>
          {gruplar.map(([donem, liste]) => (
            <div key={donem} className="mb-5">
              <h3 className="mb-2 font-semibold text-[#2C3E50]">{donem}</h3>
              {liste.map((a) => (
                <label
                  key={a.adim_id}
                  className="mb-2 flex items-start gap-3 rounded-lg bg-[#E8E8E4] p-3"
                >
                  <input
                    type="checkbox"
                    checked={!!tamam[a.adim_id]}
                    onChange={(e) => isaretle(a.adim_id, e.target.checked)}
                    className="mt-1 accent-[#7D8C7A]"
                  />
                  <span className={tamam[a.adim_id] ? "line-through opacity-60" : ""}>
                    {a.aciklama}
                  </span>
                </label>
              ))}
            </div>
          ))}
        </div>
      )}

      {bulundu && sekme === "takip" && (
        <div>
          {mentorlar.length === 0 && (
            <p className="rounded-lg bg-[#E8E8E4] p-4">
              Bu bölüm için takip listesi henüz boş.
            </p>
          )}
          {mentorlar.map((m) => (
            <div key={m.mentor_id} className="mb-3 rounded-lg bg-[#E8E8E4] p-4">
              <div className="font-semibold text-[#2C3E50]">
                {m.profil_linki.startsWith("https://") ? (
                  <a href={m.profil_linki} target="_blank" rel="noopener noreferrer" className="underline">
                    {m.isim_unvan}
                  </a>
                ) : (
                  m.isim_unvan
                )}
                <span className="ml-2 rounded-full bg-[#7D8C7A] px-2 py-0.5 text-xs text-[#F4F4F2]">
                  {m.platform}
                </span>
              </div>
              <p className="mt-2">Neden takip etmelisin? {m.neden_takip_etmeli}</p>
              {m.sana_ne_katar && <p className="mt-1 opacity-80">Sana ne katar? {m.sana_ne_katar}</p>}
            </div>
          ))}
        </div>
      )}

      {sekme === "mentor" && (
        <div>
          <form onSubmit={sor} className="grid gap-3">
            <textarea
              value={soru}
              onChange={(e) => setSoru(e.target.value)}
              maxLength={1000}
              rows={4}
              placeholder="Örn. Dikey geçiş mi yapmalıyım, direkt işe mi girmeliyim?"
              className="rounded-lg border border-[#cfcfc8] bg-[#F4F4F2] p-3"
            />
            <button
              type="submit"
              disabled={bekliyor}
              className="rounded-lg bg-[#2C3E50] px-4 py-2 text-[#F4F4F2] disabled:opacity-60"
            >
              {bekliyor ? "Yanıt hazırlanıyor..." : "Mentora sor"}
            </button>
          </form>
          {cevap && (
            <div className="mt-4 whitespace-pre-wrap rounded-lg bg-[#E8E8E4] p-4">{cevap}</div>
          )}
        </div>
      )}
    </div>
  );
}
"""

# ---------------------------------------------------------------- mentor API
DOSYALAR["app/api/mentor/route.ts"] = r"""
import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const { soru, bolum, derece } = await req.json();

  if (typeof soru !== "string" || !soru.trim() || soru.length > 1000) {
    return NextResponse.json(
      { cevap: "Sorun boş veya çok uzun (en fazla 1000 karakter)." },
      { status: 400 }
    );
  }

  const anahtar = process.env.ANTHROPIC_API_KEY;
  if (!anahtar) {
    return NextResponse.json(
      { cevap: "Sunucuda ANTHROPIC_API_KEY tanımlı değil." },
      { status: 500 }
    );
  }

  const bolumAdi = String(bolum ?? "").slice(0, 100);
  const dereceAdi = derece === "lisans" ? "lisans" : "önlisans";

  const sistem =
    `Sen bir üniversite kariyer koçusun. Öğrenci ${bolumAdi} bölümünde ${dereceAdi} ` +
    `eğitimi alıyor veya almak istiyor. Türkçe, sade ve uygulanabilir tavsiyeler ver. ` +
    `Kısa tut (en fazla 200 kelime). Kesin iş garantisi verme, emin olmadığın yerde bunu söyle.`;

  const yanit = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "x-api-key": anahtar,
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify({
      model: process.env.CLAUDE_MODEL ?? "claude-sonnet-5-5",
      max_tokens: 600,
      system: sistem,
      messages: [{ role: "user", content: soru }],
    }),
  });

  if (!yanit.ok) {
    return NextResponse.json(
      { cevap: "Yapay zeka şu an yanıt veremiyor. Biraz sonra tekrar dene." },
      { status: 502 }
    );
  }

  const veri = await yanit.json();
  const metin = (veri.content ?? [])
    .filter((p: { type: string }) => p.type === "text")
    .map((p: { text: string }) => p.text)
    .join("\n");

  return NextResponse.json({ cevap: metin || "Boş yanıt döndü." });
}
"""

# ---------------------------------------------------------------- SQL
DOSYALAR["supabase/schema.sql"] = r"""
CREATE TABLE bolumler (
  bolum_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  bolum_adi VARCHAR(255) NOT NULL,
  derece_turu VARCHAR(50) NOT NULL CHECK (derece_turu IN ('onlisans', 'lisans'))
);

CREATE TABLE takip_edilecekler (
  mentor_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  isim_unvan VARCHAR(255) NOT NULL,
  platform VARCHAR(100) NOT NULL,
  profil_linki VARCHAR(512) NOT NULL,
  neden_takip_etmeli TEXT NOT NULL,
  sana_ne_katar TEXT
);

CREATE TABLE bolum_mentor_baglantisi (
  bolum_id UUID REFERENCES bolumler(bolum_id) ON DELETE CASCADE,
  mentor_id UUID REFERENCES takip_edilecekler(mentor_id) ON DELETE CASCADE,
  PRIMARY KEY (bolum_id, mentor_id)
);

CREATE TABLE yol_haritasi_adimlari (
  adim_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  bolum_id UUID REFERENCES bolumler(bolum_id) ON DELETE CASCADE,
  donem VARCHAR(100) NOT NULL,
  sira INT NOT NULL,
  aciklama TEXT NOT NULL
);

CREATE TABLE tamamlanan_adimlar (
  kullanici_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  adim_id UUID REFERENCES yol_haritasi_adimlari(adim_id) ON DELETE CASCADE,
  PRIMARY KEY (kullanici_id, adim_id)
);

ALTER TABLE bolumler ENABLE ROW LEVEL SECURITY;
ALTER TABLE takip_edilecekler ENABLE ROW LEVEL SECURITY;
ALTER TABLE bolum_mentor_baglantisi ENABLE ROW LEVEL SECURITY;
ALTER TABLE yol_haritasi_adimlari ENABLE ROW LEVEL SECURITY;
ALTER TABLE tamamlanan_adimlar ENABLE ROW LEVEL SECURITY;

CREATE POLICY "herkes okur" ON bolumler FOR SELECT USING (true);
CREATE POLICY "herkes okur" ON takip_edilecekler FOR SELECT USING (true);
CREATE POLICY "herkes okur" ON bolum_mentor_baglantisi FOR SELECT USING (true);
CREATE POLICY "herkes okur" ON yol_haritasi_adimlari FOR SELECT USING (true);

CREATE POLICY "kendi ilerlemem" ON tamamlanan_adimlar
  FOR ALL USING (auth.uid() = kullanici_id) WITH CHECK (auth.uid() = kullanici_id);
"""

DOSYALAR["supabase/seed.sql"] = r"""
WITH b AS (
  INSERT INTO bolumler (bolum_adi, derece_turu)
  VALUES ('Bilgisayar Programcılığı', 'onlisans')
  RETURNING bolum_id
)
INSERT INTO yol_haritasi_adimlari (bolum_id, donem, sira, aciklama)
SELECT b.bolum_id, v.donem, v.sira, v.aciklama
FROM b, (VALUES
  ('1. Sınıf Güz', 1, 'Temel Git/GitHub öğren ve ilk reposunu oluştur'),
  ('1. Sınıf Güz', 2, 'Bir programlama dilinde günlük küçük alıştırmalar yap'),
  ('1. Sınıf Bahar', 3, 'Bir yazılım topluluğuna (örn. GDG) üye ol ve etkinliklerine katıl'),
  ('1. Sınıf Bahar', 4, 'İlk küçük projeni GitHub üzerinde yayınla'),
  ('Yaz Dönemi', 5, 'En az 20 günlük zorunlu staj yeri bul'),
  ('Yaz Dönemi', 6, 'LinkedIn üzerinden 10 sektör profesyoneliyle bağlantı kur'),
  ('2. Sınıf Güz', 7, 'Veritabanı ve API temellerini bir projede uygula'),
  ('2. Sınıf Bahar', 8, 'CV ve LinkedIn profilini güncelle, dikey geçiş ve iş seçeneklerini karşılaştır')
) AS v(donem, sira, aciklama);
"""


def yaz():
    if not (KOK / "package.json").exists():
        print("HATA: Burada package.json yok.")
        print("Önce 'npx create-next-app@latest kariyer-asistani' çalıştır,")
        print("sonra bu dosyayı o klasörün içine koyup tekrar çalıştır.")
        sys.exit(1)

    for yol, icerik in DOSYALAR.items():
        hedef = KOK / yol
        hedef.parent.mkdir(parents=True, exist_ok=True)
        hedef.write_text(icerik.lstrip("\n"), encoding="utf-8")
        print("yazıldı:", yol)

    env_yerel = KOK / ".env.local"
    if not env_yerel.exists():
        env_yerel.write_text(DOSYALAR[".env.example"], encoding="utf-8")
        print("oluşturuldu: .env.local (gerçek anahtarlarını içine yaz)")

    print("\n@supabase/supabase-js kuruluyor...")
    try:
        subprocess.run(["npm", "install", "@supabase/supabase-js"], cwd=KOK, check=True, shell=(sys.platform == "win32"))
    except Exception as hata:
        print("npm kurulumu başarısız, elle çalıştır: npm install @supabase/supabase-js")
        print(hata)

    print("\nSıradaki adımlar:")
    print("1) Supabase SQL Editor'de supabase/schema.sql, sonra supabase/seed.sql dosyalarını çalıştır")
    print("2) .env.local içindeki anahtarları doldur")
    print("3) npm run dev  ->  http://localhost:3000")


if __name__ == "__main__":
    yaz()
