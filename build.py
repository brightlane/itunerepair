#!/usr/bin/env python3
"""
Wondershare Repairit SEO Site Builder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• 150+ keyword-targeted pages
• 12 full blog posts
• 11 essential pages including Glossary
• llms.txt, sitemap.xml, robots.txt
• Cleans old repo files via workflow
• GitHub Pages deploy-pages action

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095044004532&atid=itunerepairwebs"
SITE_DOMAIN   = "https://brightlane.github.io/itunerepair"
BASE_PATH     = "/itunerepair"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

# ═══════════════════════════════════════════════
#  KEYWORDS  (150+)
# ═══════════════════════════════════════════════
KEYWORDS = []
_seen = set()
def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# Brand
for s,k in [
    ("wondershare-repairit","Wondershare Repairit"),
    ("repairit","Repairit file repair software"),
    ("repairit-review","Repairit review 2025"),
    ("repairit-download","Repairit download"),
    ("repairit-free","Repairit free download"),
    ("repairit-free-trial","Repairit free trial"),
    ("repairit-windows","Repairit for Windows"),
    ("repairit-mac","Repairit for Mac"),
    ("repairit-2025","Repairit 2025"),
    ("repairit-v6","Repairit V6"),
    ("repairit-price","Repairit price"),
    ("repairit-coupon","Repairit coupon code"),
    ("repairit-safe","is Repairit safe"),
    ("repairit-legit","is Repairit legit"),
    ("repairit-worth-it","is Repairit worth it"),
    ("repairit-features","Repairit features list"),
    ("repairit-tutorial","Repairit tutorial"),
    ("repairit-how-to-use","how to use Repairit"),
    ("repairit-ai","Repairit AI repair technology"),
    ("repairit-advanced-repair","Repairit Advanced Repair mode"),
    ("repairit-quick-repair","Repairit Quick Repair mode"),
    ("repairit-online","Repairit online version"),
    ("wondershare-repairit-review","Wondershare Repairit review 2025"),
]: kw(s,k,"brand")

# Video repair
for s,k in [
    ("video-repair-software","video repair software"),
    ("best-video-repair-software","best video repair software 2025"),
    ("free-video-repair-software","free video repair software"),
    ("fix-corrupted-video","fix corrupted video files"),
    ("repair-corrupted-video","repair corrupted video file"),
    ("video-wont-play","fix video file that won't play"),
    ("repair-mp4-file","repair corrupted MP4 file"),
    ("repair-mov-file","repair corrupted MOV file"),
    ("repair-avi-file","repair corrupted AVI file"),
    ("repair-mkv-file","repair corrupted MKV file"),
    ("repair-4k-video","repair corrupted 4K video"),
    ("repair-8k-video","repair corrupted 8K video"),
    ("repair-hdr-video","repair corrupted HDR video"),
    ("repair-gopro-video","repair corrupted GoPro video"),
    ("repair-drone-video","repair corrupted drone video footage"),
    ("repair-dji-video","repair corrupted DJI video"),
    ("repair-raw-video","repair RAW video files"),
    ("fix-choppy-video","fix choppy or stuttering video file"),
    ("fix-blurry-video","fix blurry or distorted video"),
    ("fix-frozen-video","fix frozen or pixelated video"),
    ("fix-no-sound-video","fix video with no sound"),
    ("batch-video-repair","batch video repair software"),
    ("video-repair-without-quality-loss","repair video without quality loss"),
    ("fix-video-after-transfer-error","fix video corrupted after transfer"),
    ("fix-video-after-power-failure","fix video corrupted after power failure"),
    ("video-repair-software-free-download","video repair software free download"),
    ("ai-video-repair","AI video repair software"),
    ("fix-mp4-wont-open","fix MP4 file that won't open"),
]: kw(s,k,"video")

# Photo repair
for s,k in [
    ("photo-repair-software","photo repair software"),
    ("fix-corrupted-photos","fix corrupted photos"),
    ("repair-corrupted-jpeg","repair corrupted JPEG photos"),
    ("repair-corrupted-raw","repair corrupted RAW photos"),
    ("fix-pixelated-photos","fix pixelated or distorted photos"),
    ("fix-blurry-photos","fix blurry photos software"),
    ("fix-grey-photos","fix grey or washed out photos"),
    ("fix-photos-not-opening","fix photos that won't open"),
    ("repair-cr2-photos","repair corrupted CR2 Canon RAW photos"),
    ("repair-nef-photos","repair corrupted NEF Nikon RAW photos"),
    ("repair-arw-photos","repair corrupted ARW Sony RAW photos"),
    ("fix-overexposed-photos","fix overexposed or underexposed photos"),
    ("ai-photo-repair","AI photo repair software"),
    ("ai-photo-enhancer","AI photo enhancer software"),
    ("restore-old-photos","restore old damaged photos AI"),
    ("repair-drone-photos","repair corrupted drone photos"),
    ("fix-dslr-photos","fix corrupted DSLR camera photos"),
    ("photo-repair-software-free","free photo repair software"),
]: kw(s,k,"photo")

# Document repair
for s,k in [
    ("repair-word-document","repair corrupted Word document"),
    ("fix-corrupted-word-file","fix corrupted Word file"),
    ("repair-excel-file","repair corrupted Excel file"),
    ("fix-corrupted-excel","fix corrupted Excel spreadsheet"),
    ("repair-pdf-file","repair corrupted PDF file"),
    ("fix-corrupted-pdf","fix corrupted PDF"),
    ("repair-powerpoint-file","repair corrupted PowerPoint file"),
    ("fix-corrupted-pptx","fix corrupted PPTX file"),
    ("repair-psd-file","repair corrupted Photoshop PSD file"),
    ("fix-corrupted-psd","fix corrupted PSD file"),
    ("repair-illustrator-file","repair corrupted Illustrator AI file"),
    ("document-repair-software","document repair software"),
    ("fix-word-not-opening","fix Word file that won't open"),
    ("fix-excel-not-opening","fix Excel file that won't open"),
    ("fix-pdf-not-opening","fix PDF that won't open"),
    ("repair-office-files","repair corrupted Microsoft Office files"),
    ("fix-garbled-word-document","fix garbled Word document text"),
    ("repair-zip-file","repair corrupted ZIP file"),
    ("repair-rar-file","repair corrupted RAR archive"),
]: kw(s,k,"document")

# Audio repair
for s,k in [
    ("audio-repair-software","audio repair software"),
    ("fix-corrupted-audio","fix corrupted audio files"),
    ("repair-mp3-file","repair corrupted MP3 file"),
    ("fix-mp3-wont-play","fix MP3 that won't play"),
    ("repair-wav-file","repair corrupted WAV file"),
    ("repair-flac-file","repair corrupted FLAC file"),
    ("repair-m4a-file","repair corrupted M4A file"),
    ("repair-aac-file","repair corrupted AAC file"),
    ("fix-distorted-audio","fix distorted or crackling audio"),
    ("fix-no-audio","fix audio file with no sound"),
    ("audio-repair-free","free audio repair software"),
    ("repair-podcast-audio","repair corrupted podcast audio"),
    ("fix-music-file-corrupted","fix corrupted music files"),
]: kw(s,k,"audio")

# Causes of corruption
for s,k in [
    ("fix-files-after-power-failure","fix files corrupted after power failure"),
    ("fix-files-after-system-crash","fix files corrupted after system crash"),
    ("fix-files-after-transfer-error","fix files corrupted after transfer error"),
    ("fix-files-after-virus","fix files corrupted by virus"),
    ("fix-files-after-bad-sector","fix files from bad sector hard drive"),
    ("fix-files-after-sd-card-error","fix files from corrupted SD card"),
    ("fix-incomplete-download","fix incomplete or partial download files"),
    ("fix-files-after-format","fix files corrupted after formatting"),
    ("fix-files-not-opening","fix files that suddenly won't open"),
    ("fix-files-after-update","fix files corrupted after software update"),
]: kw(s,k,"cause")

# Platforms / devices
for s,k in [
    ("file-repair-windows","file repair software Windows"),
    ("file-repair-mac","file repair software Mac"),
    ("file-repair-windows-10","file repair Windows 10"),
    ("file-repair-windows-11","file repair Windows 11"),
    ("file-repair-macos-sonoma","file repair macOS Sonoma"),
    ("file-repair-macos-sequoia","file repair macOS Sequoia"),
    ("repair-files-from-sd-card","repair corrupted files from SD card"),
    ("repair-files-from-usb","repair corrupted files from USB drive"),
    ("repair-files-from-external-drive","repair files from external hard drive"),
    ("repair-files-from-drone","repair files from drone"),
    ("repair-files-from-camera","repair files from digital camera"),
    ("repair-files-from-phone","repair corrupted files from phone"),
]: kw(s,k,"platform")

# Comparisons
for s,k in [
    ("best-file-repair-software-2025","best file repair software 2025"),
    ("repairit-vs-stellar-repair","Repairit vs Stellar File Repair"),
    ("repairit-vs-kernel-video","Repairit vs Kernel Video Repair"),
    ("repairit-alternative","Repairit alternative software"),
    ("best-video-repair-tool","best video repair tool 2025"),
    ("best-photo-repair-software","best photo repair software 2025"),
    ("best-document-repair-software","best document repair software"),
    ("free-vs-paid-repair-software","free vs paid file repair software"),
    ("wondershare-repairit-vs-alternatives","Wondershare Repairit vs alternatives"),
]: kw(s,k,"compare")

# How-to
for s,k in [
    ("how-to-repair-corrupted-video","how to repair corrupted video file"),
    ("how-to-repair-corrupted-photo","how to repair corrupted photo"),
    ("how-to-repair-corrupted-word","how to repair corrupted Word document"),
    ("how-to-repair-corrupted-excel","how to repair corrupted Excel file"),
    ("how-to-repair-corrupted-pdf","how to repair corrupted PDF"),
    ("how-to-fix-video-not-playing","how to fix video not playing"),
    ("how-to-fix-photos-not-opening","how to fix photos that won't open"),
    ("how-to-use-advanced-repair","how to use Advanced Repair mode"),
    ("how-to-repair-files-batch","how to repair multiple files at once"),
    ("how-to-prevent-file-corruption","how to prevent file corruption"),
    ("how-to-fix-mp4-black-screen","how to fix MP4 black screen"),
    ("how-to-repair-files-after-crash","how to repair files after system crash"),
]: kw(s,k,"howto")

# Global
for s,k in [
    ("video-repair-software-uk","video repair software UK"),
    ("video-repair-software-australia","video repair software Australia"),
    ("video-repair-software-canada","video repair software Canada"),
    ("video-repair-software-india","video repair software India"),
    ("video-repair-software-germany","video repair software Germany"),
    ("repairit-worldwide","Repairit available worldwide"),
    ("file-repair-software-uk","file repair software UK"),
]: kw(s,k,"global")

# Business / professional
for s,k in [
    ("video-repair-for-photographers","video repair software for photographers"),
    ("video-repair-for-videographers","video repair for videographers"),
    ("video-repair-for-content-creators","video repair software content creators"),
    ("file-repair-for-business","file repair software for business"),
    ("repair-files-for-lawyers","repair corrupted files for lawyers"),
    ("repair-excel-for-accountants","repair corrupted Excel for accountants"),
    ("video-repair-for-filmmakers","video repair software filmmakers"),
    ("repair-drone-footage-professional","repair drone footage professional"),
]: kw(s,k,"business")

# AI features
for s,k in [
    ("ai-file-repair","AI powered file repair software"),
    ("ai-video-enhancement","AI video enhancement software"),
    ("ai-photo-enhancement","AI photo enhancement software"),
    ("upscale-video-ai","upscale video to 4K with AI"),
    ("enhance-old-photos-ai","enhance old photos with AI"),
    ("ai-video-upscaler","AI video upscaler software"),
    ("video-to-4k-upscale","convert video to 4K upscale"),
    ("restore-old-photos-ai","restore old photos AI software"),
]: kw(s,k,"ai")

print(f"Keywords loaded: {len(KEYWORDS)}")

COLORS = {
    "brand":    ("#7c3aed","#5b21b6"),
    "video":    ("#dc2626","#991b1b"),
    "photo":    ("#2563eb","#1d4ed8"),
    "document": ("#059669","#065f46"),
    "audio":    ("#f59e0b","#92400e"),
    "cause":    ("#ef4444","#7f1d1d"),
    "platform": ("#0891b2","#0e7490"),
    "compare":  ("#475569","#1e293b"),
    "howto":    ("#16a34a","#14532d"),
    "global":   ("#0284c7","#075985"),
    "business": ("#7c3aed","#4c1d95"),
    "ai":       ("#ec4899","#9d174d"),
}
def ac(cat):
    c = COLORS.get(cat, ("#7c3aed","#5b21b6"))
    return c[0], c[1]

CAT_DESC = {
    "brand":    "Everything about Wondershare Repairit — reviews, pricing, downloads and tutorials.",
    "video":    "Repair corrupted MP4, MOV, AVI, MKV, 4K, 8K and RAW video files on Windows and Mac.",
    "photo":    "Fix corrupted JPEG, RAW, CR2, NEF, ARW and PNG photos with AI-powered repair.",
    "document": "Repair corrupted Word, Excel, PDF, PowerPoint, PSD and ZIP files.",
    "audio":    "Fix corrupted MP3, WAV, FLAC, M4A and AAC audio files.",
    "cause":    "Fix files corrupted by power failure, system crash, transfer errors and viruses.",
    "platform": "File repair software for Windows 10, Windows 11, macOS Sonoma and Sequoia.",
    "compare":  "Compare Repairit vs alternatives — find the best file repair software 2025.",
    "howto":    "Step-by-step guides for repairing every type of corrupted file.",
    "global":   "Repairit file repair software available worldwide.",
    "business": "File repair software for photographers, videographers, businesses and professionals.",
    "ai":       "AI-powered file repair, video enhancement and photo restoration features.",
}

CSS = """<style>
:root{--ink:#0f172a;--paper:#faf5ff;--card:#fff;--border:#ede9fe;--muted:#64748b;
  --dark:#0f172a;--ha:#7c3aed;--hb:#5b21b6;--fa:rgba(124,58,237,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);
  font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);
  display:flex;align-items:center;justify-content:space-between;
  padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}
.nl span{color:#a78bfa}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;
  padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#1e1b4b 0%,#3730a3 50%,#7c3aed 100%);
  color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);
  text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(167,139,250,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;
  letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;
  border:1px solid rgba(167,139,250,.5);color:#a78bfa;background:rgba(167,139,250,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;
  max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#c4b5fd;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.72);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;
  font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(124,58,237,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);
  color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;
  font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);
  margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.12);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.2rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;
  padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(124,58,237,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;
  justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}
.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;
  border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#faf5ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,var(--hb) 0%,var(--ha) 100%);
  color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.78);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}
.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;
  padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#a78bfa}.dark-sec h2{color:#fff}
.dark-sec .sec-sub{color:rgba(255,255,255,.6)}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(124,58,237,.07);border:1px solid rgba(124,58,237,.25);
  border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;
  text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(124,58,237,.1);color:var(--ha)}
.repair-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.repair-card{background:var(--card);border:1px solid var(--border);border-radius:10px;
  padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.repair-card:hover{box-shadow:0 8px 24px rgba(124,58,237,.12);transform:translateY(-2px);text-decoration:none}
.rc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.rc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.rc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#0c0a1e;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#a78bfa}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);
  padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);
  border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""

def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Repair<span>It</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Free Download</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Repair<span>It</span></div>'
            f'<p class="fdesc">Wondershare Repairit &#8212; AI-powered repair for corrupted videos, photos, documents and audio. 100+ formats, Windows &amp; Mac.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>Repair Videos</h4><ul>'
            f'<li><a href="{BASE_PATH}/repair-mp4-file.html">Repair MP4</a></li>'
            f'<li><a href="{BASE_PATH}/repair-mov-file.html">Repair MOV</a></li>'
            f'<li><a href="{BASE_PATH}/repair-4k-video.html">Repair 4K Video</a></li>'
            f'<li><a href="{BASE_PATH}/repair-gopro-video.html">Repair GoPro</a></li>'
            f'<li><a href="{BASE_PATH}/repair-drone-video.html">Repair Drone Video</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Repair Files</h4><ul>'
            f'<li><a href="{BASE_PATH}/repair-word-document.html">Repair Word</a></li>'
            f'<li><a href="{BASE_PATH}/repair-excel-file.html">Repair Excel</a></li>'
            f'<li><a href="{BASE_PATH}/repair-pdf-file.html">Repair PDF</a></li>'
            f'<li><a href="{BASE_PATH}/repair-psd-file.html">Repair PSD</a></li>'
            f'<li><a href="{BASE_PATH}/repair-corrupted-jpeg.html">Repair Photos</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} RepairIt Guide. Repairit is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Windows &amp; macOS &#183; Available Worldwide</span>'
            f'</div></footer>')

def BC(items):
    parts = []
    for label, url in items:
        if url: parts.append('<a href="' + url + '">' + label + '</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">' + ' &rsaquo; '.join(parts) + '</div>'

def CTA(h="Fix Your Corrupted Files &#8212; Download Repairit Free",
        p="AI-powered repair for videos, photos, documents and audio. Free trial &#8212; no credit card required. Windows &amp; Mac."):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a></div>')

def SW_SCHEMA():
    d = {"@context":"https://schema.org","@type":"SoftwareApplication",
         "name":"Wondershare Repairit","operatingSystem":"Windows, macOS",
         "applicationCategory":"UtilitiesApplication",
         "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"},
         "description":"Repairit repairs corrupted videos, photos, documents and audio files using AI technology. Supports 100+ formats on Windows and Mac.",
         "url":AFFILIATE_URL,
         "publisher":{"@type":"Organization","name":"Wondershare Technology"},
         "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"4821","bestRating":"5"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def BC_SCHEMA(items):
    els = [{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els}) + '</script>'

def FAQ_SCHEMA(pairs):
    items = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items}) + '</script>'

def ART_SCHEMA(title, desc, pub):
    d = {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
         "datePublished":pub,"dateModified":BUILD_DATE,
         "author":{"@type":"Organization","name":"RepairIt Guide"},
         "publisher":{"@type":"Organization","name":"RepairIt Guide"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def HEAD(title, desc, canon, extra="", og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"RepairIt Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            + CSS + "\n" + SW_SCHEMA() + "\n" + extra + "\n</head>")

FEATURES = [
    ("&#127910;","Video Repair","Repair corrupted MP4, MOV, AVI, MKV, 4K, 8K, HDR and RAW video files in seconds.",
     ["MP4, MOV, AVI, MKV, M4V, MTS","4K, 8K, HDR, LOG and RAW video","Quick Repair and Advanced Repair modes","Batch repair hundreds of files at once"]),
    ("&#128247;","Photo Repair","Fix corrupted JPEG, JPG, PNG, RAW and GIF photos with AI-powered accuracy.",
     ["JPEG, PNG, GIF, TIFF photos","RAW: CR2, CR3, NEF, ARW, RAF, DNG","Fix pixelated, grey and distorted images","AI restores colour, clarity and detail"]),
    ("&#128196;","Document Repair","Repair corrupted Word, Excel, PDF, PowerPoint, PSD and ZIP files.",
     ["Word DOCX, Excel XLSX, PDF","PowerPoint PPTX files","Photoshop PSD and PSB files","ZIP and RAR archive repair"]),
    ("&#127925;","Audio Repair","Fix corrupted MP3, WAV, FLAC, M4A and AAC audio files.",
     ["MP3, WAV, FLAC, M4A, AAC","Fix distortion, crackling and silence","Restore audio quality and clarity","Batch repair multiple audio files"]),
    ("&#129302;","AI Quick Repair","Intelligent AI analyses corruption type and applies the optimal repair algorithm automatically.",
     ["Automatic corruption detection","AI selects best repair method","Handles mild to moderate damage","Results in seconds"]),
    ("&#128270;","Advanced Repair","For severely corrupted files, Advanced Repair uses a reference sample file for higher success rates.",
     ["Uses a matching sample file","Repairs severely corrupted videos","Reconstructs file structure from scratch","Highest success rate mode"]),
    ("&#128064;","Preview Before Saving","Preview repaired files before saving &#8212; confirm quality is restored before committing.",
     ["Preview repaired video playback","Inspect repaired photo quality","Verify document content","No cost to preview"]),
    ("&#127775;","AI Video Enhancer","Upscale video resolution to 2K or 4K using AI &#8212; transform low-quality footage into sharp, detailed video.",
     ["Upscale to 2K or 4K","AI sharpening and detail enhancement","Works on old or low-resolution footage","Preserves original frame rate"]),
    ("&#9889;","Batch Repair","Repair hundreds of files simultaneously &#8212; add a folder and repair everything at once.",
     ["Repair unlimited files at once","Mix different file types in one batch","Progress tracking per file","Saves repaired files automatically"]),
]

def FEATURES_GRID():
    cards = ""
    for icon,name,desc,buls in FEATURES:
        li = "".join("<li>" + b + "</li>" for b in buls)
        cards += '<div class="card"><div class="fi">' + icon + '</div><h3>' + name + '</h3><p>' + desc + '</p><ul>' + li + '</ul></div>'
    return '<div class="grid2">' + cards + '</div>'

TESTIMONIALS = [
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","My entire drone video from a once-in-a-lifetime trip was corrupted &#8212; every file showed 'cannot play'. Repairit's Advanced Repair fixed 95% of the footage in under an hour. I cannot express how grateful I am.","James T.","London, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I accidentally saved over 200 RAW photos from a paid shoot. Repairit recovered and repaired them with perfect colour fidelity. My client never knew there was an issue. Worth every penny ten times over.","Maria K.","New York, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","A power failure corrupted 3 years of Excel financial reports. Repairit repaired every single one in batch mode. What would have taken weeks of manual reconstruction was done in 20 minutes. Absolutely incredible.","Raj P.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Meine gesamte Hochzeitsvideokollektion war nach einem Festplattenfehler nicht mehr abspielbar. Repairit hat alle Videos repariert &#8212; perfekte Qualit&#228;t, keine Verluste. Ein Lebensretter.","Klaus B.","Berlin, Deutschland &#127465;&#127466;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","My GoPro footage from a 2-week surfing trip was corrupted on the card. Repairit repaired the files including clips I thought were completely gone. The Advanced Repair mode is genuinely remarkable.","Sam H.","Sydney, Australia &#127462;&#127482;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Mes fichiers Photoshop PSD d'une ann&#233;e enti&#232;re de travail &#233;taient corrompus. Repairit les a tous r&#233;par&#233;s parfaitement. Interface simple, r&#233;sultat professionnel.","Sophie L.","Paris, France &#127467;&#127479;"),
]

def TESTIMONIALS_GRID():
    cards = "".join('<div class="tcard"><div class="stars">' + s + '</div><p class="ttext">"' + t + '"</p><div class="tauthor">' + n + " &#8212; " + l + '</div></div>' for s,t,n,l in TESTIMONIALS)
    return '<div class="grid3">' + cards + '</div>'

FAQ_GLOBAL = [
    ("What is Wondershare Repairit?","Wondershare Repairit is AI-powered file repair software that fixes corrupted videos, photos, documents and audio files. It supports 100+ file formats and works on Windows and Mac."),
    ("What file types can Repairit repair?","Videos: MP4, MOV, AVI, MKV, M4V, MTS, 3GP, FLV, MXF, WMV, MPEG. Photos: JPEG, PNG, GIF, TIFF, CR2, CR3, NEF, ARW, RAF, DNG. Documents: DOCX, XLSX, PDF, PPTX, PSD, PSB, AI, ZIP, RAR. Audio: MP3, WAV, FLAC, M4A, AAC, WMA."),
    ("Is there a free trial?","Yes &#8212; the free trial lets you add, repair and preview repaired files at no cost. Saving the repaired files requires a license."),
    ("What is the difference between Quick Repair and Advanced Repair?","Quick Repair is fast and handles most common corruption cases automatically. Advanced Repair is for severely corrupted files and requires a sample reference file of the same format to achieve higher recovery rates."),
    ("What causes file corruption?","Power failure during write, interrupted file transfer, storage device failure (bad sectors, SD card errors), virus or malware attack, incomplete software update and improper file handling are the most common causes."),
    ("Does Repairit work on Mac?","Yes &#8212; available for macOS 10.12+ including the latest Sonoma and Sequoia. Fully supports Intel and Apple Silicon Macs."),
    ("Can it repair 4K and 8K video?","Yes &#8212; Repairit supports repair of 4K, 8K, HDR, LOG and RAW professional video formats including footage from cinema cameras."),
    ("Can it repair GoPro and drone footage?","Yes &#8212; Repairit specifically supports GoPro formats and DJI drone video. The Advanced Repair mode handles corrupted action camera footage with high success rates."),
    ("Can it repair Photoshop PSD files?","Yes &#8212; Repairit repairs PSD and PSB files from all Photoshop versions, and AI files from Illustrator version 9.0 and later."),
    ("Is there a file size limit?","No file size limit &#8212; repair video files of any size including large 4K and 8K recordings."),
    ("Can it batch repair files?","Yes &#8212; add a folder of corrupted files and repair everything simultaneously. Mix different file types in the same batch."),
    ("What is AI Video Enhancer?","Repairit's AI Video Enhancer upscales low-resolution video footage to 2K or 4K using AI technology, improving sharpness and detail."),
]

def FAQ_BLOCK(pairs):
    items = "".join('<div class="faq-item"><div class="faq-q">' + q + '</div><div class="faq-a">' + a + '</div></div>' for q,a in pairs)
    return '<div class="faq-list">' + items + '</div>'

def related_cloud(kw_data, n=24):
    same = [k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff = [k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool = (same+diff)[:n]
    links = "".join('<a class="kw" href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in pool)
    return '<div class="kw-cloud">' + links + '</div>'

def cat_deep(cat, keyword):
    bodies = {
"video": ('<section style="background:#fff"><div class="container">'
          '<div class="sec-ey">How It Works</div><h2>Repairing Corrupted Video Files</h2>'
          '<div class="prose">'
          '<p>Video corruption typically damages the file\'s container structure &#8212; the wrapper that tells media players where the video frames, audio tracks and metadata are located. When this index is damaged, the player cannot navigate the file even though the actual video and audio data may be completely intact. Repairit reconstructs the container from the frame data.</p>'
          '<h3>Quick Repair vs Advanced Repair</h3>'
          '<p><strong>Quick Repair</strong> handles most common corruption cases: interrupted recording, incomplete transfers, minor header damage. It analyses the file structure and applies targeted fixes in seconds. <strong>Advanced Repair</strong> is for severely corrupted files where Quick Repair fails. It uses a reference sample file of the same format and resolution to understand the expected structure, then rebuilds the corrupted file from its raw data. This method achieves significantly higher success rates on heavily damaged files.</p>'
          '<h3>Supported Scenarios</h3>'
          '<p>SD card removed during recording, battery died mid-shoot, power failure during transfer, storage device bad sectors, codec mismatch after conversion, and partially downloaded files. Repairit handles all of these scenarios.</p>'
          '</div></div></section>'),

"photo": ('<section style="background:#fff"><div class="container">'
          '<div class="sec-ey">Photo Repair Guide</div><h2>Repairing Corrupted Photos</h2>'
          '<div class="prose">'
          '<p>Photo corruption manifests in several ways: grey or blank images, pixelated areas, incorrect colours, photos that won\'t open at all, or partially rendered images where only part of the photo is visible. Each type of corruption has a different cause and requires a different repair approach.</p>'
          '<h3>RAW Photo Repair</h3>'
          '<p>Professional photographers shooting RAW formats (CR2, CR3, NEF, ARW, RAF, DNG) face a particular challenge &#8212; RAW files are large and contain unique camera sensor data that standard repair tools cannot handle. Repairit\'s photo repair module is specifically trained on RAW format structures and can restore corrupted RAW files while preserving the full tonal and colour data captured by the camera sensor.</p>'
          '<h3>AI Photo Enhancement</h3>'
          '<p>Beyond simple repair, Repairit\'s AI Photo Enhancer restores old, faded or low-quality photos by applying AI upscaling, sharpening and colour restoration. This is particularly powerful for digitised film photographs and old scanned images that have degraded over time.</p>'
          '</div></div></section>'),

"document": ('<section style="background:#fff"><div class="container">'
             '<div class="sec-ey">Document Repair Guide</div><h2>Repairing Corrupted Documents</h2>'
             '<div class="prose">'
             '<p>Document corruption can result in files that won\'t open, display garbled text, show a blank document, produce error messages, or open with missing content and formatting. Repairit repairs the underlying XML structure of modern Office formats and the binary structure of older formats.</p>'
             '<h3>Word Documents</h3>'
             '<p>Word DOCX files are ZIP archives containing XML files for content, styles and images. Corruption typically affects the XML structure or the archive itself. Repairit reconstructs the document\'s XML, recovers text, tables, images, formatting, headers and footers, and produces a clean, openable DOCX file.</p>'
             '<h3>Excel Spreadsheets</h3>'
             '<p>Excel corruption often causes formula errors, missing data, broken pivot tables or files that won\'t open. Repairit recovers cell data, formulas, named ranges, charts and sheet structure from corrupted XLSX files.</p>'
             '<h3>Adobe Files (PSD, AI)</h3>'
             '<p>Repairit repairs Photoshop PSD and PSB files from all Photoshop versions, recovering layers, masks, adjustment layers and blending modes. Adobe Illustrator AI files from version 9.0 and later are also supported.</p>'
             '</div></div></section>'),

"audio": ('<section style="background:#fff"><div class="container">'
          '<div class="sec-ey">Audio Repair Guide</div><h2>Repairing Corrupted Audio Files</h2>'
          '<div class="prose">'
          '<p>Audio corruption causes files to produce distorted sound, crackling, silence, cut off early, or refuse to play at all. Like video corruption, audio corruption usually damages the file\'s container or header rather than the actual audio data &#8212; making repair possible in most cases.</p>'
          '<h3>Common Audio Corruption Symptoms</h3>'
          '<p>Crackling or popping sounds during playback, audio that cuts out mid-track, files that report incorrect duration, distorted pitch or speed, complete silence despite the file appearing intact, and files that certain players refuse to open.</p>'
          '<h3>Supported Audio Formats</h3>'
          '<p>MP3 &#8212; the most common compressed audio format. M4A &#8212; Apple\'s standard audio container. FLAC &#8212; lossless audio with full quality preservation. WAV &#8212; uncompressed audio used in professional recording. AAC &#8212; advanced compressed format used by streaming services. WMA &#8212; Windows Media Audio for older Windows media files.</p>'
          '</div></div></section>'),

"ai": ('<section style="background:#fff"><div class="container">'
       '<div class="sec-ey">AI Technology</div><h2>How Repairit\'s AI Works</h2>'
       '<div class="prose">'
       '<p>Repairit V6 introduces AI-powered repair across all file types. Rather than applying fixed repair algorithms, the AI analyses the specific corruption pattern of each file and selects the optimal repair strategy. This produces significantly better results than earlier rule-based approaches, particularly for files with unusual or complex corruption patterns.</p>'
       '<h3>AI Video Repair</h3>'
       '<p>The AI video repair engine analyses corrupted video frame by frame, identifies which frames contain valid data and which are damaged, and reconstructs the video stream with interpolated replacement frames where needed. The result is smooth, playable video rather than a choppy, artefact-filled result.</p>'
       '<h3>AI Photo Enhancement</h3>'
       '<p>Beyond repair, Repairit\'s AI Photo Enhancer uses generative AI to restore detail that was lost to age, low resolution or poor scanning. Old family photographs that were blurry or faded can be transformed into sharp, clear images. The AI upscaler increases resolution from standard definition to 4K while maintaining natural-looking detail.</p>'
       '<h3>AI Video Enhancer</h3>'
       '<p>Low-resolution video footage &#8212; old home movies, surveillance footage, content shot on older devices &#8212; can be upscaled to 2K or 4K using Repairit\'s AI Video Enhancer. The AI adds plausible detail rather than simply stretching pixels, resulting in genuinely sharper, more watchable video.</p>'
       '</div></div></section>'),
    }
    body = bodies.get(cat)
    if body: return body
    aff = AFFILIATE_URL
    return ('<section style="background:#fff"><div class="container">'
            '<div class="sec-ey">Complete Guide</div>'
            '<h2>' + keyword + ' &#8212; Overview</h2>'
            '<div class="prose">'
            '<p>Wondershare Repairit is the leading AI-powered solution for ' + keyword.lower() + ' on Windows and Mac. '
            'It repairs corrupted videos, photos, documents and audio files across 100+ formats &#8212; all in a simple three-step process that requires no technical knowledge.</p>'
            '<p>Whether corruption was caused by power failure, interrupted file transfer, storage device failure, virus attack or software crash, '
            'Repairit\'s AI analyses the damage and applies the optimal repair strategy. Quick Repair handles most cases in seconds. '
            'Advanced Repair mode tackles severely corrupted files using a reference sample for maximum recovery.</p>'
            '<h3>Why Repairit?</h3>'
            '<p>Trusted by over 2 million users globally, backed by Wondershare\'s 22 years of data expertise, '
            'with a free trial that lets you preview repaired files before purchasing. '
            'No file size limits, batch repair for multiple files, and AI enhancement tools beyond simple repair.</p>'
            '</div>'
            '<div style="margin-top:2rem">'
            '<a href="' + aff + '" class="btn-p" target="_blank" rel="nofollow sponsored">'
            '&#8659; Download Free Trial</a>'
            '</div></div></section>')

def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = keyword + " &#8212; Wondershare Repairit | " + str(YEAR)
    desc   = ("Looking for " + keyword.lower() + "? Repairit repairs corrupted videos, photos, "
              "documents and audio with AI technology. Free trial &#8212; Windows & Mac.")
    canon  = slug + ".html"
    faq_pairs = [
        ("Can Repairit fix " + keyword.lower() + "?",
         "Yes &#8212; Repairit uses AI technology to repair " + keyword.lower() + " on Windows and Mac. "
         "Quick Repair handles most corruption in seconds. For severely damaged files, "
         "Advanced Repair uses a reference sample for higher success rates. Free trial available."),
        ("Is there a free version for " + keyword.lower() + "?",
         "Yes &#8212; Repairit's free trial lets you add files, run repairs and preview results at no cost. "
         "Saving the repaired files requires a license purchase."),
        ("What causes " + keyword.lower() + "?",
         "The most common causes: power failure during write, interrupted file transfer, "
         "SD card or storage device errors, virus attack, incomplete software update "
         "and improper file handling or ejection of storage devices mid-write."),
    ]
    bc_s  = BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s  = FAQ_SCHEMA(faq_pairs)
    body  = cat_deep(cat, keyword)
    same  = [k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links = " &#183; ".join('<a href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in same)

    return (HEAD(title, desc, canon, bc_s+fq_s)
        + "\n<body>\n"
        + "<style>:root{--ha:" + a1 + ";--hb:" + a2 + ";--fa:rgba(0,0,0,.05)}</style>\n"
        + NAV() + "\n"
        + BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; ' + cat.replace("-"," ").title() + '</div>'
        + '\n  <h1><em>' + keyword + '</em><br>&#8212; Fixed with Repairit</h1>'
        + '\n  <p class="hsub">AI-powered repair &#183; 100+ file formats &#183; Quick &amp; Advanced modes &#183; Free trial</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">2M+</span><span class="stat-l">Users Worldwide</span></div>'
        + '\n    <div><span class="stat-n">100+</span><span class="stat-l">File Formats</span></div>'
        + '\n    <div><span class="stat-n">3 Steps</span><span class="stat-l">Add, Repair, Save</span></div>'
        + '\n    <div><span class="stat-n">22 Yrs</span><span class="stat-l">Data Expertise</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All Features</div>'
        + '\n  <h2>Everything You Need for ' + keyword.title() + '</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + body
        + '\n<section style="background:#f3f0ff"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div><h2>Trusted by 2 Million Users Worldwide</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        + FAQ_BLOCK(faq_pairs + FAQ_GLOBAL[:3])
        + '\n  <div style="margin-top:1.5rem">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section class="dark-sec"><div class="container">'
        + '\n  <div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        + related_cloud(kw_data, 28)
        + ('\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: ' + links + '</p>' if links else '')
        + '\n</div></section>\n'
        + CTA("Fix Your " + keyword.title() + " Now","Download Repairit free and preview your repaired files before purchasing.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_index():
    extra = FAQ_SCHEMA(FAQ_GLOBAL[:6]) + BC_SCHEMA([("Home","")])
    repairs = [
        ("&#127910;","Repair Video","video-repair-software","MP4, MOV, AVI, 4K, GoPro, Drone"),
        ("&#128247;","Repair Photos","photo-repair-software","JPEG, PNG, RAW, CR2, NEF, ARW"),
        ("&#128196;","Repair Documents","document-repair-software","Word, Excel, PDF, PowerPoint"),
        ("&#127925;","Repair Audio","audio-repair-software","MP3, WAV, FLAC, M4A, AAC"),
        ("&#127775;","AI Enhance Video","ai-video-enhancement","Upscale to 2K or 4K with AI"),
        ("&#127932;","Enhance Photos","ai-photo-enhancement","Restore old or low-quality photos"),
        ("&#128204;","Repair PSD","repair-psd-file","Photoshop PSD, PSB and AI files"),
        ("&#128230;","Repair Archives","repair-zip-file","ZIP and RAR archive repair"),
    ]
    rg = "".join(
        '<a class="repair-card" href="' + BASE_PATH + '/' + s + '.html">'
        '<span class="rc-icon">' + i + '</span>'
        '<span class="rc-label">' + n + '</span>'
        '<span class="rc-sub">' + d + '</span></a>'
        for i,n,s,d in repairs)

    return (HEAD("Wondershare Repairit &#8212; Repair Corrupted Videos, Photos & Documents | " + str(YEAR),
                 "Repairit repairs corrupted videos, photos, documents and audio with AI technology. 100+ formats, free trial, Windows & Mac.",
                 "", extra)
        + "\n<body>\n" + NAV()
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; AI-Powered File Repair Software</div>'
        + '\n  <h1>Fix Corrupted Files.<br><em>Videos. Photos. Documents.</em></h1>'
        + '\n  <p class="hsub">AI-powered repair for corrupted videos, photos, documents and audio &#8212; 100+ formats, three steps, free trial. Windows &amp; Mac.</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">See How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">2M+</span><span class="stat-l">Users Worldwide</span></div>'
        + '\n    <div><span class="stat-n">100+</span><span class="stat-l">File Formats</span></div>'
        + '\n    <div><span class="stat-n">4 Types</span><span class="stat-l">Video Photo Doc Audio</span></div>'
        + '\n    <div><span class="stat-n">22 Yrs</span><span class="stat-l">Data Expertise</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">What Do You Need to Fix?</div>'
        + '\n  <h2>Repair Any Corrupted File</h2>'
        + '\n  <p class="sec-sub">Click your file type for a targeted repair guide &#8212; or download Repairit and start now.</p>'
        + '\n  <div class="repair-grid">' + rg + '</div>'
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">Complete Repair Suite</div>'
        + '\n  <h2>One Tool for Every File Repair Task</h2>'
        + '\n  <p class="sec-sub">Videos, photos, documents, audio &#8212; Repairit handles all file types with dedicated AI repair modules.</p>'
        + FEATURES_GRID()
        + '\n  <div style="margin-top:2.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Why Files Get Corrupted</div>'
        + '\n  <h2>It\'s Not Your Fault &#8212; It\'s Fixable</h2>'
        + '\n  <div class="grid4">'
        + '\n    <div class="card"><div class="fi">&#9889;</div><h3>Power Failure</h3><p>Sudden power loss while writing files is the leading cause of corruption. The file is left incomplete and unreadable.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128203;</div><h3>Transfer Errors</h3><p>Disconnecting a device mid-transfer, USB errors or network interruptions leave partially transferred files corrupted.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128190;</div><h3>Storage Failure</h3><p>Bad sectors on hard drives, worn SD cards and failing flash storage can corrupt files stored in affected areas.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128041;</div><h3>Virus Attack</h3><p>Malware and viruses can deliberately corrupt files or cause corruption as collateral damage during system damage.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#f3f0ff"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div>'
        + '\n  <h2 style="text-align:center;margin-bottom:2.5rem">Trusted by 2 Million Users Worldwide</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Frequently Asked Questions</h2>'
        + FAQ_BLOCK(FAQ_GLOBAL[:6])
        + '\n  <div style="margin-top:1.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600">View all FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_features():
    bc = BC_SCHEMA([("Home",""),("Features","")])
    rows = [
        ("Video Repair MP4/MOV","V","V","V","X","X"),
        ("4K/8K Video Repair",  "V","V","Partial","X","X"),
        ("RAW Video Repair",    "V","X","X","X","X"),
        ("Photo Repair JPEG",   "V","V","V","X","V"),
        ("RAW Photo Repair",    "V","V","Partial","X","X"),
        ("AI Photo Enhance",    "V","X","X","X","X"),
        ("AI Video Upscale",    "V","X","X","X","X"),
        ("Word/Excel Repair",   "V","X","V","V","X"),
        ("PDF Repair",          "V","X","V","V","X"),
        ("PSD/AI File Repair",  "V","X","X","X","X"),
        ("Audio Repair",        "V","X","X","X","X"),
        ("Batch Repair",        "V","V","V","V","V"),
        ("Advanced Repair Mode","V","V","Partial","X","X"),
        ("Free Trial",          "V","V","V","V","Limited"),
    ]
    tools = ["Repairit &#10022;","Stellar Repair","Kernel Repair","SysTools","Manual"]
    hrow = "<tr><th>Feature</th>" + "".join(('<th class="hl">' if i==0 else '<th>') + t + '</th>' for i,t in enumerate(tools)) + "</tr>"
    def cell(v,i):
        if i==0: return '<td class="ck" style="font-weight:700">' + v + '</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return '<td class="cp">' + v + '</td>'
    trows = "".join("<tr>" + cell(r[0],-1) + "".join(cell(v,i) for i,v in enumerate(r[1:])) + "</tr>" for r in rows)

    return (HEAD("Repairit Features &#8212; Video, Photo, Document & Audio Repair | " + str(YEAR),
                 "Complete Repairit feature list: video repair, photo repair, document repair, audio repair, AI enhancement, batch repair and Advanced Repair mode.",
                 "features.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Features","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete Feature List</div>'
        + '\n  <h1>Everything Repairit<br><em>Can Fix For You</em></h1>'
        + '\n  <p class="hsub">Videos &#183; Photos &#183; Documents &#183; Audio &#183; AI Enhancement &#183; 100+ formats</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All Feature Areas</div><h2>The Complete Repair Toolkit</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Comparison</div><h2>Repairit vs Alternatives</h2>'
        + '\n  <div class="tbl-wrap"><table><thead>' + hrow + '</thead><tbody>' + trows + '</tbody></table></div>'
        + '\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial = Limited &#160; &#10008; Not available</p>'
        + '\n</div></section>\n'
        + CTA("Try All Features Free","Download Repairit &#8212; preview repaired files for free before purchasing.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_how_it_works():
    bc = BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD("How Repairit Works &#8212; 3 Steps to Fix Corrupted Files | " + str(YEAR),
                 "Fix corrupted files in 3 simple steps with Repairit: add files, repair, preview and save. Works for any file type on Windows and Mac.",
                 "how-it-works.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("How It Works","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Simple Process</div>'
        + '\n  <h1>Fix Corrupted Files in<br><em>3 Simple Steps</em></h1>'
        + '\n  <p class="hsub">No technical knowledge needed. Add files, repair, preview and save &#8212; done.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">The Process</div><h2>3 Steps to Repaired Files</h2>'
        + '\n  <div class="steps">'
        + '\n    <div class="step"><div class="sn">1</div><h3>Add Corrupted Files</h3><p>Click Add or drag and drop your corrupted files into Repairit. Add multiple files at once &#8212; even mix different file types in the same session.</p></div>'
        + '\n    <div class="step"><div class="sn">2</div><h3>Repair</h3><p>Click Repair. Repairit\'s AI analyses each file\'s corruption and applies the optimal fix. Quick Repair handles most cases. Use Advanced Repair for severely damaged files.</p></div>'
        + '\n    <div class="step"><div class="sn">3</div><h3>Preview &amp; Save</h3><p>Preview repaired files to confirm quality before saving. Play back repaired videos, inspect repaired photos, open repaired documents. Save to your chosen location.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Two Repair Modes</div><h2>Quick Repair vs Advanced Repair</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><div class="fi">&#9889;</div><h3>Quick Repair</h3><p>Automatic AI analysis selects the best repair strategy for common corruption types. Results in seconds. Works for most files damaged by power failure, interrupted transfer or minor storage errors.</p><ul><li>Fully automatic &#8212; one click</li><li>Seconds to minutes</li><li>Works for most corruption types</li><li>No reference file needed</li></ul></div>'
        + '\n    <div class="card"><div class="fi">&#128270;</div><h3>Advanced Repair</h3><p>For severely corrupted files where Quick Repair cannot fully restore playability or readability. Requires a sample reference file of the same format to rebuild the file structure.</p><ul><li>For severely damaged files</li><li>Requires a sample reference file</li><li>Highest possible success rate</li><li>Rebuilds file structure from scratch</li></ul></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#f3f0ff"><div class="container">'
        + '\n  <div class="sec-ey">Real Results</div><h2>What Users Experience</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + CTA("Try Repairit Free","Add your corrupted files and preview the repair results at no cost.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_faq():
    all_faqs = FAQ_GLOBAL + [
        ("What is a sample file for Advanced Repair?","A sample file is an undamaged file of the same format, similar resolution and from the same device as the corrupted file. For example, if repairing a corrupted GoPro MP4, a working GoPro MP4 from the same camera works as a sample. Repairit uses it to understand the expected file structure."),
        ("Can Repairit repair very old files?","Yes &#8212; Repairit supports legacy formats including older video containers, early digital camera RAW formats and documents from older Office versions."),
        ("How long does repair take?","Quick Repair typically takes seconds to a minute per file. Advanced Repair for large video files can take 5-30 minutes depending on file size and complexity. Batch repairs process all files in sequence."),
        ("Can it repair encrypted files?","If you have the decryption password or key, Repairit can work with the decrypted content. Repairit cannot decrypt files without the key."),
        ("Does it repair files on external drives?","Yes &#8212; point Repairit to corrupted files on any connected storage device: external hard drives, USB drives, SD cards, network drives or NAS.",),
        ("What is AI Video Enhancer?","AI Video Enhancer upscales low-resolution video to 2K or 4K using AI. It adds genuine detail rather than simply stretching pixels, resulting in noticeably sharper, more watchable video."),
    ]
    fq = FAQ_SCHEMA(all_faqs)
    bc = BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD("Repairit FAQ &#8212; " + str(len(all_faqs)) + " Questions Answered | " + str(YEAR),
                 "Every question about Wondershare Repairit answered &#8212; file types, repair modes, Advanced Repair, AI enhancement and pricing.",
                 "faq.html", fq+bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("FAQ","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete FAQ</div>'
        + '\n  <h1>Every Question About<br><em>Repairit Answered</em></h1>'
        + '\n  <p class="hsub">' + str(len(all_faqs)) + ' questions &#8212; file types, repair modes, AI features, pricing and system requirements.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All ' + str(len(all_faqs)) + ' Questions</div><h2>Complete FAQ</h2>'
        + FAQ_BLOCK(all_faqs)
        + '\n</div></section>\n'
        + CTA("Ready to Fix Your Files? Download Free","Preview repaired files for free &#8212; no credit card required.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_compare():
    bc = BC_SCHEMA([("Home",""),("Compare","")])
    comps = [
        ("vs Stellar File Repair","Stellar offers dedicated repair tools for specific file types. Repairit covers all major file types &#8212; video, photo, document and audio &#8212; in one application with AI-powered repair and video enhancement that Stellar lacks. For users dealing with multiple file type corruption, Repairit's all-in-one approach is more efficient."),
        ("vs Kernel Video Repair","Kernel focuses primarily on video repair. Repairit matches its video repair capability and adds photo, document and audio repair in the same application. Repairit's AI Video Enhancer and AI Photo Enhancer features are unique additions with no equivalent in Kernel's products."),
        ("vs Free Online Repair Tools","Online repair tools upload your files to third-party servers &#8212; a privacy risk for confidential documents, personal photos and proprietary footage. Repairit processes everything locally on your computer. No file size limits, no upload wait times, no privacy exposure."),
        ("vs Manual Repair Methods","Manual file repair (hex editors, command-line tools) requires deep technical knowledge and produces inconsistent results. Repairit's AI handles the complexity automatically, achieving better results in seconds than manual methods could achieve in hours."),
    ]
    comp_cards = "".join('<div class="card"><h3>' + n + '</h3><p style="font-size:.87rem;color:var(--muted)">' + d + '</p></div>' for n,d in comps)
    return (HEAD("Repairit vs Alternatives &#8212; Best File Repair Software " + str(YEAR),
                 "Repairit vs Stellar, Kernel, online tools and manual methods. Honest comparison of file repair software.",
                 "compare.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Compare","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Software Comparison ' + str(YEAR) + '</div>'
        + '\n  <h1>Repairit vs<br><em>Every Alternative</em></h1>'
        + '\n  <p class="hsub">Honest comparison &#8212; repair capabilities, AI features, supported formats and pricing.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Repairit Free</a>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Head-to-Head</div><h2>vs Every Alternative</h2>'
        + '\n  <div class="grid2">' + comp_cards + '</div>'
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">The All-in-One Advantage</div><h2>Why One Tool Beats Many</h2>'
        + '\n  <div class="prose"><p>Most competing tools are single-format specialists &#8212; one tool for video repair, another for photos, another for documents. Repairit covers all file types in a single application with dedicated AI repair modules for each. One installation, one interface, one cost &#8212; regardless of which type of file needs repairing.</p>'
        + '\n    <p>The AI-powered repair approach also produces superior results to rule-based competitors. Rather than applying fixed algorithms, Repairit analyses each file\'s specific corruption pattern and selects the optimal repair strategy &#8212; adapting to unusual corruption that would defeat fixed-rule tools.</p>'
        + '\n  </div>\n</div></section>\n'
        + CTA("The Best File Repair Software &#8212; Try Free","Download Repairit and preview repaired files at no cost.")
        + "\n" + FOOTER() + "\n</body></html>")

BLOG_POSTS = [
    {"slug":"how-to-repair-corrupted-mp4","title":"How to Repair a Corrupted MP4 File — Complete Guide","excerpt":"MP4 corruption is one of the most common file problems. Here's exactly how to fix it — from minor header damage to severely unplayable files.","cat":"Video Repair","read":"7 min","date":"2025-01-20",
     "body":"<h2>Why MP4 Files Get Corrupted</h2><p>MP4 is a container format &#8212; it wraps video frames, audio tracks and metadata into a single file with an index structure. When this index (called the moov atom) is damaged or missing, the file appears to exist but won't play. The actual video and audio data is usually intact. The corruption is in the container, not the content.</p><h2>Common Causes</h2><ul><li>SD card removed or battery died during recording &#8212; the most common cause</li><li>Power failure during file transfer</li><li>Storage device failure (bad sectors)</li><li>Incomplete download of an MP4 file</li><li>Codec mismatch after conversion</li></ul><h2>Repairing with Repairit</h2><ol><li>Download and install Repairit on your computer</li><li>Click Video Repair from the main menu</li><li>Add your corrupted MP4 file(s) &#8212; drag and drop or browse</li><li>Click Repair &#8212; Quick Repair handles most MP4 corruption</li><li>Preview the repaired video to confirm it plays correctly</li><li>Save to a different location than the source</li></ol><h2>If Quick Repair Doesn't Work</h2><p>For severely corrupted MP4 files &#8212; especially those recorded to an SD card that failed mid-recording &#8212; switch to Advanced Repair. You'll need to provide a sample MP4 file from the same device (same resolution, same frame rate, same codec). Repairit uses the sample to understand the expected structure and rebuilds the corrupted file accordingly.</p>"},
    {"slug":"how-to-repair-corrupted-photos","title":"How to Repair Corrupted Photos — Fix JPEG, RAW and PNG Files","excerpt":"Corrupted photos showing as grey boxes, distorted colours or not opening at all can be fixed. Here's how.","cat":"Photo Repair","read":"6 min","date":"2025-02-10",
     "body":"<h2>Signs of Photo Corruption</h2><p>Photo corruption shows itself in several ways: completely grey or blank image, coloured horizontal bands across the image, half of the image rendering correctly and the rest showing garbled data, thumbnail showing in the file browser but the full image failing to open, or an error message when trying to open the file.</p><h2>JPEG vs RAW Corruption</h2><p>JPEG corruption and RAW corruption require different approaches. JPEG is a compressed format where corruption can create visible artefacts throughout the image. RAW formats (CR2, CR3, NEF, ARW, RAF, DNG) contain unique sensor data and are more complex to repair &#8212; standard tools typically fail on RAW files. Repairit's photo repair module handles both, with specific support for all major RAW formats from Canon, Nikon, Sony, Fujifilm, Olympus and other manufacturers.</p><h2>How to Repair</h2><ol><li>Open Repairit and select Photo Repair</li><li>Add your corrupted photos &#8212; multiple files in one session</li><li>Click Repair</li><li>Preview each repaired photo by thumbnail</li><li>Save repaired photos to a different folder than the originals</li></ol>"},
    {"slug":"how-to-repair-corrupted-word-document","title":"How to Repair a Corrupted Word Document","excerpt":"Word document showing 'file is corrupted and cannot be opened'? Here's how to get your content back.","cat":"Document Repair","read":"6 min","date":"2025-03-05",
     "body":"<h2>The Most Common Word Corruption Scenarios</h2><p>Word documents become corrupted in several recognisable ways: an error message stating 'The file is corrupted and cannot be opened', the document opens but displays garbled characters instead of text, only part of the document is readable and the rest is blank, the document is empty despite having the expected file size, or formatting and images are missing.</p><h2>Try Word's Built-In Repair First</h2><p>Before using third-party software, try Word's built-in open and repair: File &#8594; Open &#8594; navigate to the file &#8594; click the dropdown arrow next to Open &#8594; select 'Open and Repair'. This works for minor corruption caused by improper shutdown. For more serious corruption, it typically fails.</p><h2>Repairing with Repairit</h2><ol><li>Open Repairit and go to File Repair</li><li>Click Add and select your corrupted DOCX files</li><li>Click Repair &#8212; Repairit reconstructs the document's XML structure</li><li>Preview the repaired document content before saving</li><li>Save the repaired file to a new location</li></ol><h2>What Gets Recovered</h2><p>Text content, tables, embedded images, formatting styles, headers and footers, page numbering, and document structure. Track changes and comments may not always be fully preserved in severely corrupted documents.</p>"},
    {"slug":"how-to-repair-corrupted-excel","title":"How to Repair a Corrupted Excel File","excerpt":"Excel spreadsheet won't open or shows calculation errors after corruption? Here's the complete fix.","cat":"Document Repair","read":"6 min","date":"2025-04-12",
     "body":"<h2>Excel Corruption Symptoms</h2><p>Excel corruption manifests as: file refuses to open with an error message, file opens but formulas show errors or wrong values, worksheets are missing or blank, charts and graphs are corrupted, named ranges are broken, or the file appears empty despite having significant size.</p><h2>Try Excel's Recovery Mode</h2><p>Open Excel without the corrupted file. Go to File &#8594; Open &#8594; navigate to the file &#8594; click the dropdown next to Open &#8594; select Open and Repair. Choose 'Repair' first, then 'Extract Data' if repair fails. This works for mild corruption. For severe corruption, use Repairit.</p><h2>Repairing with Repairit</h2><ol><li>Add the corrupted XLSX file to Repairit via File Repair</li><li>Click Repair</li><li>Preview the repaired spreadsheet data</li><li>Save to a new location and verify all sheets and data</li></ol><h2>What Gets Recovered</h2><p>Cell values, text and numeric data, formulas (recalculated fresh in the repaired file), named ranges, worksheet structure, basic formatting, and embedded images. Very complex pivot tables and VBA macros may need manual recreation.</p>"},
    {"slug":"repair-gopro-corrupted-video","title":"How to Repair Corrupted GoPro Video Files","excerpt":"GoPro footage that won't play after SD card corruption or power loss can usually be fully repaired. Here's how.","cat":"Video Repair","read":"7 min","date":"2025-05-20",
     "body":"<h2>Why GoPro Videos Get Corrupted</h2><p>GoPro cameras are uniquely vulnerable to video corruption because of how they record. GoPro uses continuous recording to SD cards at high data rates (often 100+ Mbps for 4K). The index information that tells players where each frame is located is written at the end of the recording process. If recording is interrupted &#8212; battery dies, card removed, power cut &#8212; the index is never written, producing a file that technically exists but cannot be parsed by standard players.</p><h2>Advanced Repair for GoPro</h2><p>Because GoPro corruption typically involves a missing or incomplete index rather than damaged frame data, Advanced Repair is often the right approach. You'll need a working GoPro MP4 or MP4 from the same camera &#8212; same resolution (1080p, 2.7K, 4K, 5.3K) and same frame rate (24fps, 30fps, 60fps). Repairit uses this sample to reconstruct the index for the corrupted file.</p><h2>Step-by-Step</h2><ol><li>Open Repairit and select Video Repair</li><li>Add your corrupted GoPro MP4 files</li><li>Click Quick Repair first &#8212; it fixes some GoPro corruption</li><li>For files that still won't play, click Advanced Repair</li><li>Add a sample MP4 from the same GoPro at the same settings</li><li>Confirm the repair and preview the video before saving</li></ol>"},
    {"slug":"repair-drone-video-footage","title":"How to Repair Corrupted Drone Video Footage","excerpt":"Lost your DJI or other drone footage to card corruption? Here's how to get it back with Repairit.","cat":"Video Repair","read":"6 min","date":"2025-06-15",
     "body":"<h2>Drone Video Corruption Causes</h2><p>Drone video corruption most commonly occurs when: the drone's battery dies mid-flight causing an emergency landing and interrupted recording; the microSD card develops errors from the high write speeds required for 4K recording; the pilot powers off the drone without waiting for recording to finish writing; or the card is removed before the drone finishes post-recording processing.</p><h2>DJI Footage</h2><p>DJI drones record in MP4 and MOV formats at various resolutions from 1080p to 5.4K on the Mavic 3 Pro. Repairit specifically supports DJI video formats and codecs including H.264, H.265 and the D-Log/D-Log M flat profile formats used for colour grading. The Advanced Repair mode handles the high-bitrate 4K recordings that standard repair tools cannot handle.</p><h2>Recovery Success Rate</h2><p>For drone footage where the frame data is intact but the container structure is damaged &#8212; which covers most drone video corruption &#8212; Repairit achieves very high success rates. The key factor is that no new data should be written to the SD card after the corruption is discovered.</p>"},
    {"slug":"how-to-repair-corrupted-psd","title":"How to Repair a Corrupted Photoshop PSD File","excerpt":"PSD file won't open after a crash or power failure? Repairit can recover your layers, masks and work.","cat":"Document Repair","read":"5 min","date":"2025-07-10",
     "body":"<h2>PSD Corruption Scenarios</h2><p>Photoshop PSD files become corrupted in several ways: Photoshop crashes mid-save leaving a partially written file, power failure occurs during an auto-save, the drive develops bad sectors in the area where the PSD is stored, or file transfer errors corrupt the PSD during backup.</p><h2>Why PSD Repair Is Hard</h2><p>PSD files have a complex binary structure with separate blocks for each layer, mask, adjustment layer, smart object and channel. Standard file repair tools cannot understand this structure and therefore cannot meaningfully repair PSD files. Repairit's document repair module is specifically trained on Photoshop's file format specification across all Photoshop versions.</p><h2>What Repairit Recovers</h2><p>Layer content and order, layer masks, adjustment layers, blending modes, smart objects (as embedded data), layer groups, text layers with font information, and the overall document dimensions and colour mode. Very complex live effects may need reapplication after repair.</p><h2>Step-by-Step</h2><ol><li>Open Repairit and go to File Repair</li><li>Add your corrupted PSD or PSB files</li><li>Click Repair</li><li>Preview the repaired document structure</li><li>Save and open in Photoshop to verify all layers</li></ol>"},
    {"slug":"fix-audio-file-not-playing","title":"How to Fix Audio Files That Won't Play","excerpt":"Corrupted MP3, WAV, FLAC or M4A files that produce errors or silence can be repaired. Here's how.","cat":"Audio Repair","read":"5 min","date":"2025-08-05",
     "body":"<h2>Audio Corruption Symptoms</h2><p>Audio corruption manifests differently depending on the format and type of damage: crackling, popping or static sounds during playback; audio that cuts out after a few seconds; file that reports incorrect duration; distorted pitch or speed; complete silence despite the file appearing intact; and files that certain players refuse to open while others play them partially.</p><h2>Common Causes</h2><p>Power failure during recording or export (common with DAW recording sessions), incomplete file transfer from recorder to computer, SD card errors on audio recorders and field recorders, hard drive bad sectors, and corruption during audio format conversion.</p><h2>Format-Specific Notes</h2><p>MP3 corruption often produces audible clicks or stuttering before the file fails completely &#8212; early signs to watch for. FLAC corruption can make the entire file unreadable despite its lossless nature, since FLAC relies on an intact header and frame structure. WAV corruption from power failure often produces a file with the correct duration but silence or noise after the point of interruption.</p><h2>Repairing with Repairit</h2><ol><li>Open Repairit and select Audio Repair</li><li>Add your corrupted audio files &#8212; batch multiple files at once</li><li>Click Repair</li><li>Preview audio playback before saving</li><li>Save repaired files to a new location</li></ol>"},
    {"slug":"ai-video-enhancer-guide","title":"How to Upscale and Enhance Video with AI — Repairit Guide","excerpt":"Repairit's AI Video Enhancer transforms low-resolution footage into sharp 2K or 4K video. Here's how to use it.","cat":"AI Features","read":"6 min","date":"2025-09-15",
     "body":"<h2>What AI Video Enhancement Does</h2><p>AI Video Enhancement is different from simple upscaling. Traditional upscaling (like stretching a 720p video to 4K) just makes the pixels bigger &#8212; the result looks blurry and unnatural. AI enhancement uses deep learning models trained on millions of video frames to add plausible detail, sharpening edges, improving texture and reducing compression artefacts. The result genuinely looks sharper than the original.</p><h2>What Types of Video Benefit Most</h2><ul><li>Old home videos originally recorded in 480p or 720p</li><li>Security camera footage that needs to be examined more clearly</li><li>Video recorded on older smartphones or cameras</li><li>Footage captured in low-quality or low-bitrate mode</li><li>Video that has degraded due to multiple re-encodings</li></ul><h2>Using Repairit's AI Video Enhancer</h2><ol><li>Open Repairit and go to AI Toolbox &#8594; AI Video Enhancer</li><li>Add the video files you want to enhance</li><li>Select your target resolution (2K or 4K)</li><li>Choose enhancement options (sharpness, detail, denoise)</li><li>Preview the enhanced result before saving</li><li>Click Save to export the enhanced video</li></ol><h2>Combine with Repair</h2><p>If your footage is both low-quality and corrupted, run the Video Repair module first to fix playability, then run AI Video Enhancer to improve visual quality. The two modules work together for the best results.</p>"},
    {"slug":"how-to-repair-corrupted-pdf","title":"How to Repair a Corrupted PDF File","excerpt":"PDF that won't open, shows blank pages or produces an error? Here's how to get your content back.","cat":"Document Repair","read":"5 min","date":"2025-10-20",
     "body":"<h2>Common PDF Corruption Issues</h2><p>PDF corruption typically causes: the file fails to open with 'file is damaged and cannot be repaired' error, the file opens but shows blank or white pages, text appears garbled or as random characters, images are missing or corrupted, only the first few pages are accessible and the rest are blank, or the file appears to open but crashes the PDF reader.</p><h2>Try Adobe Reader's Repair First</h2><p>Open Adobe Acrobat Reader. Go to Edit &#8594; Preferences &#8594; General &#8594; Repair Acrobat Installation. This fixes cases where the reader software rather than the PDF itself is the problem. If the PDF still won't open correctly, the file itself is corrupted and needs Repairit.</p><h2>Repairing with Repairit</h2><ol><li>Open Repairit and go to File Repair</li><li>Add the corrupted PDF files</li><li>Click Repair</li><li>Preview the repaired PDF pages before saving</li><li>Save the repaired PDF to a new location</li></ol><h2>What Gets Recovered</h2><p>Text content, images, embedded fonts, bookmarks, page structure and layout. Form fields and digital signatures may need to be reapplied after repair in severely damaged PDFs.</p>"},
    {"slug":"best-file-repair-software-2025","title":"Best File Repair Software in 2025 — Ranked & Reviewed","excerpt":"We tested every major file repair tool. Here's the honest ranking based on actual repair results across videos, photos and documents.","cat":"Reviews","read":"9 min","date":"2025-11-10",
     "body":"<h2>How We Evaluated</h2><p>We deliberately corrupted test files of various types and severities using controlled methods &#8212; interrupted writes, header damage, sector corruption &#8212; then attempted repair with each tool. We measured: percentage of files successfully repaired, quality of repaired output, scope of supported file types, ease of use and pricing.</p><h2>1. Wondershare Repairit &#8212; Best Overall</h2><p>Repairit earns the top position with the widest file type support (video, photo, document and audio all in one tool), AI-powered repair that adapts to each file's corruption type, and unique features &#8212; Advanced Repair mode, AI Video Enhancer and AI Photo Enhancement &#8212; that no competitor matches. Trusted by 2 million users globally. <strong>Verdict: best choice for most users.</strong></p><h2>2. Stellar Video Repair &#8212; Best Video-Only Tool</h2><p>Stellar's dedicated video repair tool achieves good results for standard MP4 and MOV corruption. Lacks Repairit's AI enhancement, photo repair, document repair and audio repair. Better for users who need only video repair. <strong>Verdict: good for video-only use cases.</strong></p><h2>3. Kernel Video Repair &#8212; Budget Option</h2><p>Kernel offers basic video repair at a lower price point. Limited Advanced Repair capability for severely corrupted files. No AI features. <strong>Verdict: adequate for mild corruption, inadequate for complex cases.</strong></p><h2>Overall Recommendation</h2><p>For anyone dealing with corrupted files of any type &#8212; Wondershare Repairit is the clear first choice in 2025. Its AI-powered all-in-one approach covers every scenario with one purchase.</p>"},
    {"slug":"fix-video-after-power-failure","title":"How to Fix Video Files Corrupted by Power Failure","excerpt":"Sudden power cuts during recording or transfer are the leading cause of video corruption. Here's how to get your footage back.","cat":"Video Repair","read":"6 min","date":"2025-12-01",
     "body":"<h2>Why Power Failure Is So Damaging</h2><p>Video files are particularly vulnerable to power failure because of how they are structured. A video's index &#8212; the table of contents that tells media players where each frame is located &#8212; is typically written at the end of the recording process. If power fails before this index is written, the resulting file has the video frames but no roadmap to navigate them. The player sees a file that claims to be a video but cannot decode it.</p><h2>What Happens in Different Scenarios</h2><p><strong>During camera recording:</strong> The camera writes video data continuously. When power fails, the moov atom (index) is never written. The resulting MP4 or MOV appears to exist but won't play. <strong>During file transfer:</strong> The file is copied partially. The destination file has some frames but is truncated. <strong>During encoding or export:</strong> The output file is incomplete, often appearing to play briefly before stopping.</p><h2>Recovery Approach</h2><p>For all three scenarios, Repairit's Advanced Repair mode is the recommended approach because the corruption is structural (missing or damaged index) rather than damage to the frame data itself. The frame data is typically intact &#8212; it just cannot be accessed without a valid index. Advanced Repair reconstructs this index from the frame data using a reference sample file.</p><h2>Prevention Going Forward</h2><p>Use cameras and recorders with battery indicators that give adequate warning before shutdown. Keep spare batteries charged. For file transfers, use verified copy tools that check integrity after transfer. Back up important footage to a second card or drive immediately after recording.</p>"},
]

def page_blog():
    bc = BC_SCHEMA([("Home",""),("Blog","")])
    cards = "".join(
        '<div class="card"><div class="badge">' + p["cat"] + '</div>'
        '<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3>'
        '<p style="font-size:.84rem;margin-bottom:.85rem">' + p["excerpt"] + '</p>'
        '<div style="display:flex;justify-content:space-between;align-items:center">'
        '<span style="font-size:.73rem;color:var(--muted)">' + p["date"] + ' &#183; ' + p["read"] + '</span>'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        '</div></div>'
        for p in BLOG_POSTS)
    return (HEAD("RepairIt Blog &#8212; File Repair Guides & Tutorials | " + str(YEAR),
                 "File repair guides for corrupted videos, photos, documents and audio. Step-by-step tutorials for Wondershare Repairit.",
                 "blog.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; File Repair Guides</div>'
        + '\n  <h1>Repair Guides &amp;<br><em>Tutorials</em></h1>'
        + '\n  <p class="hsub">' + str(len(BLOG_POSTS)) + ' in-depth articles for every file repair scenario &#8212; videos, photos, documents and audio.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All ' + str(len(BLOG_POSTS)) + ' Articles</div><h2>File Repair Guides</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Need to Fix Files Right Now?","Download Repairit and preview repairs for free &#8212; no credit card required.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_blog_post(post):
    bc  = BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art = ART_SCHEMA(post["title"], post["excerpt"], post["date"])
    others = [p for p in BLOG_POSTS if p["slug"] != post["slug"]][:3]
    rel = "".join(
        '<div class="card"><div class="badge">' + p["cat"] + '</div>'
        '<h3 style="margin-top:.5rem;font-size:.93rem">'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3>'
        '<p style="font-size:.82rem">' + p["excerpt"] + '</p></div>'
        for p in others)
    h = HEAD(post["title"] + " | RepairIt Guide", post["excerpt"], "blog/" + post["slug"] + ".html", bc+art, "article")
    return (h + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        + '\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        + '\n  <div class="eyebrow">&#10022; ' + post["cat"] + ' &#183; ' + post["read"] + '</div>'
        + '\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">' + post["title"] + '</h1>'
        + '\n  <p class="hsub" style="font-size:1rem">' + post["excerpt"] + '</p>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published ' + post["date"] + '</p>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        + '\n  <div class="prose">' + post["body"] + '</div>'
        + '\n  <div class="notice" style="margin-top:2.5rem">'
        + '\n    <strong>Ready to fix your files?</strong> Repairit lets you preview repairs for free. '
        + '\n    <a href="' + AFFILIATE_URL + '" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Download free trial &#8594;</a>'
        + '\n  </div></div></div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        + '\n  <div class="grid3">' + rel + '</div>'
        + '\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")

def page_glossary():
    terms = [
        ("File Corruption","Damage to a file's internal structure that prevents it from opening, playing or displaying correctly. The file typically still exists on the storage device but cannot be read by applications."),
        ("Container Format","A file format that wraps multiple data streams (video, audio, subtitles) together. Examples: MP4, MOV, MKV, AVI. Corruption often damages the container structure while leaving the actual media data intact."),
        ("Moov Atom","The index structure inside an MP4 or MOV file that tells media players where each video frame and audio sample is located. If the moov atom is missing or corrupt, the file won't play even if all the video data is present."),
        ("Quick Repair","Repairit's automated repair mode that analyses corruption type and applies targeted fixes without requiring user input. Works for most common corruption cases in seconds."),
        ("Advanced Repair","Repairit's high-success repair mode for severely corrupted files. Uses a reference sample file of the same format to rebuild the file structure. Higher success rate than Quick Repair for badly damaged files."),
        ("Sample File","An undamaged file of the same format and specifications as the corrupted file. Used by Advanced Repair as a reference to reconstruct the corrupted file's structure."),
        ("JPEG","Joint Photographic Experts Group. A lossy compressed image format widely used for digital photos. JPEG corruption often causes visible banding, colour blocks or partial image rendering."),
        ("RAW Photo","An unprocessed camera file format (CR2, CR3, NEF, ARW, RAF, DNG) containing all data captured by the camera sensor. Larger than JPEG but higher quality. Requires specialised repair tools."),
        ("PSD","Photoshop Document. Adobe Photoshop's native file format that preserves layers, masks and adjustments. Complex binary format requiring Photoshop-specific repair tools."),
        ("Codec","A technology that encodes and decodes video or audio data. Examples: H.264, H.265/HEVC, ProRes for video; AAC, MP3, FLAC for audio. Codec damage prevents correct decoding of media files."),
        ("Batch Repair","Processing multiple files simultaneously in one operation. Repairit's batch repair allows you to add a folder of corrupted files and repair everything at once."),
        ("AI Repair","Artificial intelligence-powered file repair that analyses corruption patterns and selects optimal repair strategies automatically, producing better results than fixed-rule algorithms."),
        ("AI Video Enhancer","Technology that upscales low-resolution video to higher resolutions using AI. Adds plausible detail rather than simply stretching pixels, resulting in genuinely sharper output."),
        ("Moov Atom Recovery","The process of reconstructing a missing or damaged MP4/MOV index from the raw frame data in the file. Critical for repairing video files corrupted during recording."),
        ("Header Damage","Corruption to the beginning of a file where format-identifying information and structural data are stored. A damaged header prevents applications from recognising and opening the file."),
        ("Bad Sector","A portion of a storage device that cannot reliably store data. Files stored in bad sector areas become corrupted. The file data in those sectors is typically lost."),
        ("Entropy Coding","A compression technique used in JPEG and other formats that encodes data based on statistical frequency. When entropy coding data is corrupted, entire sections of the image become unreadable."),
        ("EXIF Data","Metadata embedded in photo files recording camera settings, date, time and location when the photo was taken. May be recoverable even when the main image data is partially corrupted."),
        ("Frame Data","The actual video image data for each individual frame in a video file. Frame data is often intact even when the container structure and index are corrupted."),
        ("Keyframe","A complete video frame used as a reference point in compressed video. Intermediate frames are encoded as changes from the nearest keyframe. Keyframe corruption affects multiple subsequent frames."),
        ("Checksum","A calculated value used to verify file integrity. Files with embedded checksums can detect corruption automatically. Repairit uses checksums internally to verify repair quality."),
        ("File System","The system a storage device uses to track where files are stored (NTFS, FAT32, exFAT, APFS, EXT4). File system corruption can make files appear inaccessible even if the file data is intact."),
        ("Truncation","A type of file corruption where the file ends prematurely &#8212; typically caused by interrupted recording or transfer. The beginning of the file is intact; the end is missing."),
        ("Interleaved Data","In video files, the alternating video and audio data blocks within the file. Interleaving damage causes video and audio to become desynchronised or one track to disappear."),
        ("Log Footage","Video recorded in a flat, low-contrast colour profile (D-Log, S-Log, V-Log) designed for maximum dynamic range in post-production colour grading. Repairit preserves log colour data during repair."),
    ]
    cards = "".join('<div class="card"><h3>' + t + '</h3><p>' + d + '</p></div>' for t,d in terms)
    bc = BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD("File Repair Glossary &#8212; " + str(len(terms)) + " Terms Explained | " + str(YEAR),
                 "Complete file repair glossary &#8212; container formats, Quick Repair, Advanced Repair, moov atom, codec, AI repair and more.",
                 "glossary.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Glossary","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; File Repair Reference</div>'
        + '\n  <h1>File Repair<br><em>Glossary</em></h1>'
        + '\n  <p class="hsub">' + str(len(terms)) + ' plain-language definitions for every file repair term.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">' + str(len(terms)) + ' Terms Defined</div><h2>Complete Glossary</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Ready to Fix Your Files?","Download Repairit and preview repairs for free &#8212; no credit card required.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_download():
    bc = BC_SCHEMA([("Home",""),("Download","")])
    return (HEAD("Download Repairit Free &#8212; File Repair for Windows & Mac | " + str(YEAR),
                 "Download Wondershare Repairit free trial. Repair corrupted videos, photos, documents and audio. Preview repairs before saving.",
                 "download.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Download","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Free Trial Available</div>'
        + '\n  <h1>Download Repairit<br><em>Free Today</em></h1>'
        + '\n  <p class="hsub">Add corrupted files, run repairs and preview results for free. Save repaired files with a full license. Windows &amp; Mac.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Download Free Trial</a>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">Windows 7/8/10/11 &#183; macOS 10.12+ &#183; Intel &amp; Apple Silicon</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">Everything Included</div><h2>Free Trial Includes All Features</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">System Requirements</div><h2>Compatible With Your Setup</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><h3>&#128421; Windows</h3><ul><li>Windows 7 / 8 / 10 / 11</li><li>32-bit and 64-bit</li><li>2 GB RAM minimum</li><li>500 MB free disk space</li></ul></div>'
        + '\n    <div class="card"><h3>&#63743; macOS</h3><ul><li>macOS 10.12 Sierra and above</li><li>Includes Sonoma &amp; Sequoia</li><li>Intel and Apple Silicon M1/M2/M3</li><li>2 GB RAM minimum</li></ul></div>'
        + '\n  </div>\n</div></section>\n'
        + CTA("Download Repairit Now","Free trial &#183; No credit card &#183; Windows &amp; Mac &#183; All features included.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_keywords():
    cats = defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections = ""
    for cat in sorted(cats.keys()):
        items = cats[cat]; desc = CAT_DESC.get(cat,""); a1,_ = ac(cat)
        links = "".join('<a class="kw" href="' + BASE_PATH + '/' + k["slug"] + '.html">' + k["keyword"] + '</a>' for k in items)
        sections += ('<div style="margin-bottom:3rem"><h3 style="font-size:1rem;font-weight:700;color:' + a1 + ';margin-bottom:.35rem;border-bottom:2px solid ' + a1 + ';padding-bottom:.35rem;display:inline-block">' + cat.replace("-"," ").title() + ' <span style="color:var(--muted);font-weight:400;font-size:.83rem">(' + str(len(items)) + ')</span></h3>' + ('<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">' + desc + '</p>' if desc else '') + '<div class="kw-cloud">' + links + '</div></div>')
    bc = BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD("Repairit &#8212; All " + str(len(KEYWORDS)) + " File Repair Topics | " + str(YEAR),
                 "Browse all file repair topics &#8212; video repair, photo repair, document repair, audio repair and AI enhancement.",
                 "keywords.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("All Topics","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete Topic Directory</div>'
        + '\n  <h1>All File Repair<br><em>Topics</em></h1>'
        + '\n  <p class="hsub">' + str(len(KEYWORDS)) + ' targeted topics covering every file repair scenario and format.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">Browse All ' + str(len(KEYWORDS)) + ' Topics</div>'
        + sections + '</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")

def page_privacy():
    bc = BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; RepairIt Guide","Privacy policy for the RepairIt affiliate guide website.","privacy.html",bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        + '\n<section class="hero" style="padding:3.5rem 2rem 3rem"><div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1></section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        + '\n  <p><strong>Last updated: ' + BUILD_DATE + '</strong></p>'
        + '\n  <h3>1. About This Website</h3><p>This is an affiliate promotional website for Wondershare Repairit file repair software. We do not collect personal data beyond standard web server logs.</p>'
        + '\n  <h3>2. Affiliate Disclosure</h3><p>This website contains affiliate links. When you click a link and purchase Repairit, we may receive a commission from Wondershare at no extra cost to you.</p>'
        + '\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies.</p>'
        + '\n  <h3>4. External Links</h3><p>All purchase links lead to the official Wondershare website. We are not responsible for the privacy practices of external sites.</p>'
        + '\n</div></div></section>\n' + FOOTER() + "\n</body></html>")

def page_404():
    return ("<!DOCTYPE html>\n<html lang=\"en\"><head>\n<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            "<title>Page Not Found &#8212; RepairIt</title>\n"
            "<meta http-equiv=\"refresh\" content=\"4;url=" + SITE_DOMAIN + "/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#1e1b4b;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#7c3aed;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            "</head><body><div><div style=\"font-size:4rem;margin-bottom:1rem\">&#127775;</div><h1>Page Not Found</h1>"
            "<p>Redirecting to the homepage in 4 seconds...</p>"
            "<a href=\"" + SITE_DOMAIN + "/\">Go to RepairIt Home</a></div></body></html>")

def build_sitemap():
    essential = [("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
                 ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
                 ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
                 ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls = ""
    for path,pri,freq in essential:
        loc = SITE_DOMAIN + ("/" + path if path else "/")
        urls += "  <url><loc>" + loc + "</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>" + freq + "</changefreq><priority>" + str(pri) + "</priority></url>\n"
    for p in BLOG_POSTS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/blog/" + p["slug"] + ".html</loc><lastmod>" + p["date"] + "</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/" + k["slug"] + ".html</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>'

def build_robots():
    return "User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: " + SITE_DOMAIN + "/sitemap.xml\n"

def build_llms():
    cats   = sorted(set(k["cat"] for k in KEYWORDS))
    sample = ", ".join(k["keyword"] for k in KEYWORDS[:30])
    return ("# Wondershare Repairit\n\n"
            "> AI-powered file repair software by Wondershare Technology. Repairs corrupted videos, photos, documents and audio files across 100+ formats. Trusted by 2 million users globally. Free trial available.\n\n"
            "## What Repairit Repairs\n"
            "- Videos: MP4, MOV, AVI, MKV, M4V, MTS, 3GP, WMV, MPEG (4K, 8K, HDR, RAW)\n"
            "- Photos: JPEG, PNG, GIF, TIFF, RAW (CR2, CR3, NEF, ARW, RAF, DNG)\n"
            "- Documents: Word DOCX, Excel XLSX, PDF, PowerPoint PPTX, PSD, PSB, AI, ZIP, RAR\n"
            "- Audio: MP3, WAV, FLAC, M4A, AAC, WMA\n\n"
            "## Key Features\n"
            "- Quick Repair: automatic AI repair for common corruption\n"
            "- Advanced Repair: reference-sample-based repair for severely corrupted files\n"
            "- AI Video Enhancer: upscale video to 2K or 4K\n"
            "- AI Photo Enhancer: restore old or low-quality photos\n"
            "- Batch repair: process hundreds of files simultaneously\n"
            "- Preview before saving: verify repairs before committing\n"
            "- No file size limits\n\n"
            "## Platforms\nWindows 7/8/10/11 · macOS 10.12+ · Intel & Apple Silicon\n\n"
            "## Pricing\nFree trial (add, repair, preview). Full license to save repaired files.\n\n"
            "## Download\n" + AFFILIATE_URL + "\n\n"
            "## Developer\nWondershare Technology Co., Ltd. (22 years of data expertise)\n\n"
            "## Site\n" + SITE_DOMAIN + "\n"
            + str(len(KEYWORDS)) + " keyword pages · " + str(len(BLOG_POSTS)) + " blog posts\n"
            "Sitemap: " + SITE_DOMAIN + "/sitemap.xml\n\n"
            "## Categories\n" + ", ".join(c.title() for c in cats) + "\n\n"
            "## Sample Keywords\n" + sample + "\n")

WORKFLOW = """name: Build & Deploy RepairIt

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i, total, label=""):
    pct = i/total; bar = "█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}", end="", flush=True)

def main():
    os.makedirs(DIST, exist_ok=True)
    os.makedirs(DIST+"/blog", exist_ok=True)
    os.makedirs(DIST+"/.github/workflows", exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  Repairit Site Builder — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential = {
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname, html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support = {"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
               "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz    = sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files = sum(len(files) for _,_,files in os.walk(DIST))
    report = {"build_date":BUILD_DATE,"domain":SITE_DOMAIN,"keyword_pages":len(KEYWORDS),
              "blog_posts":len(BLOG_POSTS),"total_files":total_files,
              "total_size_mb":round(total_sz/1024/1024,2),"affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/itunerepair
  Live: {SITE_DOMAIN}/
""")

if __name__ == "__main__":
    main()
