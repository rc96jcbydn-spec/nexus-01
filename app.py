import streamlit as st
from datetime import datetime
import pandas as pd

# 1. PAGE CONFIG & ELITE SAAS THEME
st.set_page_config(
    page_title="NEXUS-01 | Global Autonomous pSEO Infrastructure",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. MULTILINGUAL DICTIONARY (Top 10 Global Languages + Turkish)
TRANSLATIONS = {
    "Türkçe": {
        "lang_label": "🌐 Dil / Language",
        "hero_title": "⚛️ NEXUS-01 Çekirdek Mimarisi",
        "hero_subtitle": "Yüksek niyetli organik trafik kazanımı, topolojik nöro-evrim ve ölçeklenebilir ürünleştirilmiş monetizasyon için tasarlanmış otonom pSEO altyapısı.",
        "m1": "Mimari Motoru", "m1_sub": "Oto-Poetik DAG",
        "m2": "Aktif pSEO Sayfası", "m2_sub": "Optimize Edildi",
        "m3": "Konsensüs Güvenliği", "m3_sub": "BFT Korumalı",
        "m4": "Hedef Verim Modeli", "m4_sub": "Yüksek Niyet",
        "tab1": "🧬 1. Stratejik Matris",
        "tab2": "📝 2. pSEO Fabrikası",
        "tab3": "💳 3. Kurumsal Paketler",
        "tab4": "🛡️ 4. Sistem Denetim Günlüğü",
        "mat_title": "Hedef Mimari Parametreleri",
        "stack_label": "Altyapı Yığını:",
        "intent_label": "Dönüşüm Niyeti:",
        "mat_btn": "Uzun Kuyruklu Matris Üret",
        "mat_success": "Matris 4 ana semantik küme üzerinde başarıyla genişletildi.",
        "eco_title": "Ekonomik Metodoloji",
        "eco_desc": "* **Uzun Kuyruklu Hakimiyet:** Yüksek dönüşüm niyetine sahip, düşük rekabetli sorguları yakalar.\n* **Asimetrik Değer:** Yüzeysel metin özetleri yerine eksiksiz, üretime hazır şablonlar sunar.\n* **Oto-Poetik Ölçekleme:** Sentezlenen her sayfa içsel vektör bellek alanını genişletir.",
        "fac_title": "Otonom pSEO Sayfa Sentezi",
        "fac_desc": "Teknik alıcılar için özel olarak optimize edilmiş, yüksek sıralama potansiyeline sahip açılış sayfaları sentezleyin.",
        "kw_label": "Hedef Uzun Kuyruklu Anahtar Kelime:",
        "persona_label": "Birincil Persona:",
        "fac_btn": "Mimari Sayfasını Sentezle",
        "fac_success": "Başarıyla sentezlendi:",
        "reg_title": "Aktif Varlık Kaydı",
        "mon_title": "Ürünleştirilmiş Servis ve Lisanslama Katmanları",
        "mon_desc": "Sürtünmesiz kurumsal dönüşüm için tasarlanmış, şeffaf değer odaklı fiyatlandırma modelleri.",
        "tier1_title": "🥉 Standart Başlangıç Kiti",
        "tier1_price": "**39€** (Tek Seferlik)",
        "tier1_inc": "**İçerik:** Çekirdek Python/Streamlit pSEO şablonu, temel anahtar kelime matrisi üreteci ve kurulum kılavuzu.",
        "tier1_ideal": "**İdeal Kullanıcı:** Otonom trafik akışlarını test eden bireysel geliştiriciler.",
        "tier2_title": "🥇 Kurumsal Oto-Poetik Swarm",
        "tier2_price": "**99€** (Ömür Boyu Erişim)",
        "tier2_inc": "**İçerik:** Tam BFT konsensüs motoru, vektör DB senkronizasyonu, çoklu düğüm DAG morfing ve öncelikli güncellemeler.",
        "tier2_ideal": "**İdeal Kullanıcı:** Ölçeklenebilir, çok sektörlü dijital varlıklar inşa eden kurucular.",
        "checkout_btn": "Güvenli Ödeme (Stripe)",
        "audit_title": "BFT ve Vektör Senkronizasyon Denetim İzleme",
        "footer": "NEXUS-01 Oto-Poetik Çekirdek • Sürdürülebilir Otonom Büyüme İçin Tasarlanmıştır"
    },
    "English": {
        "lang_label": "🌐 Language / Dil",
        "hero_title": "⚛️ NEXUS-01 Core Architecture",
        "hero_subtitle": "Autonomous programmatic SEO infrastructure engineered for high-intent organic traffic acquisition, topological neuro-evolution, and scalable productized monetization.",
        "m1": "Architecture Engine", "m1_sub": "Autopoietic DAG",
        "m2": "Active pSEO Pages", "m2_sub": "Optimized",
        "m3": "Consensus Security", "m3_sub": "BFT Protected",
        "m4": "Target Yield Model", "m4_sub": "High Intent",
        "tab1": "🧬 1. Strategic Matrix",
        "tab2": "📝 2. pSEO Factory",
        "tab3": "💳 3. Enterprise Tiers",
        "tab4": "🛡️ 4. System Audit Log",
        "mat_title": "Target Architecture Parameters",
        "stack_label": "Infrastructure Stack:",
        "intent_label": "Conversion Intent:",
        "mat_btn": "Generate Long-Tail Matrix",
        "mat_success": "Matrix successfully expanded across 4 primary semantic clusters.",
        "eco_title": "Economic Methodology",
        "eco_desc": "* **Long-Tail Dominance:** Captures precise, low-competition queries with high conversion intent.\n* **Asymmetric Value:** Delivers complete, production-ready boilerplates instead of shallow text summaries.\n* **Autopoietic Scaling:** Every synthesized page expands the internal vector memory space.",
        "fac_title": "Autonomous pSEO Page Synthesis",
        "fac_desc": "Synthesize high-ranking, programmatically optimized landing pages tailored for technical buyers.",
        "kw_label": "Target Long-Tail Keyword:",
        "persona_label": "Primary Persona:",
        "fac_btn": "Synthesize Architecture Page",
        "fac_success": "Successfully synthesized:",
        "reg_title": "Active Asset Registry",
        "mon_title": "Productized Service & Licensing Tiers",
        "mon_desc": "Transparent, value-anchored pricing models designed for frictionless enterprise conversion.",
        "tier1_title": "🥉 Standard Starter Kit",
        "tier1_price": "**39€** (One-time)",
        "tier1_inc": "**Includes:** Core Python/Streamlit pSEO boilerplate, basic keyword matrix generator, and deployment guide.",
        "tier1_ideal": "**Ideal For:** Individual developers testing autonomous traffic streams.",
        "tier2_title": "🥇 Enterprise Autopoietic Swarm",
        "tier2_price": "**99€** (Lifetime Access)",
        "tier2_inc": "**Includes:** Full BFT consensus engine, vector DB synchronization, multi-node DAG morphing, and priority updates.",
        "tier2_ideal": "**Ideal For:** Founders building scalable, multi-sector digital assets.",
        "checkout_btn": "Secure Checkout (Stripe)",
        "audit_title": "BFT & Vector-Sync Audit Trail",
        "footer": "NEXUS-01 Autopoietic Core • Engineered for Sustainable Autonomous Growth"
    },
    "Español": {
        "lang_label": "🌐 Idioma",
        "hero_title": "⚛️ Arquitectura Núcleo NEXUS-01",
        "hero_subtitle": "Infraestructura autónoma de SEO programático diseñada para la adquisición de tráfico orgánico de alta intención, neuroevolución topológica y monetización escalable.",
        "m1": "Motor de Arquitectura", "m1_sub": "DAG Autopoiético",
        "m2": "Páginas pSEO Activas", "m2_sub": "Optimizado",
        "m3": "Seguridad de Consenso", "m3_sub": "Protegido BFT",
        "m4": "Modelo de Rendimiento", "m4_sub": "Alta Intención",
        "tab1": "🧬 1. Matriz Estratégica",
        "tab2": "📝 2. Fábrica pSEO",
        "tab3": "💳 3. Niveles Empresariales",
        "tab4": "🛡️ 4. Registro de Auditoría",
        "mat_title": "Parámetros de Arquitectura",
        "stack_label": "Pila de Infraestructura:",
        "intent_label": "Intención de Conversión:",
        "mat_btn": "Generar Matriz de Cola Larga",
        "mat_success": "Matriz ampliada con éxito en 4 grupos semánticos principales.",
        "eco_title": "Metodología Económica",
        "eco_desc": "* **Dominio de Cola Larga:** Captura consultas precisas de baja competencia.\n* **Valor Asimétrico:** Ofrece plantillas listas para producción.\n* **Escalado Autopoiético:** Cada página expande la memoria vectorial.",
        "fac_title": "Síntesis Autónoma de Páginas pSEO",
        "fac_desc": "Sintetize páginas de destino optimizadas para compradores técnicos.",
        "kw_label": "Palabra Clave Objetivo:",
        "persona_label": "Persona Principal:",
        "fac_btn": "Sintetizar Página de Arquitectura",
        "fac_success": "Sintetizado con éxito:",
        "reg_title": "Registro de Activos Activos",
        "mon_title": "Servicios Producto y Niveles de Licencia",
        "mon_desc": "Modelos de precios transparentes y anclados en el valor.",
        "tier1_title": "🥉 Kit de Inicio Estándar",
        "tier1_price": "**39€** (Pago único)",
        "tier1_inc": "**Incluye:** Plantilla base pSEO, generador de matriz y guía.",
        "tier1_ideal": "**Ideal para:** Desarrolladores individuales.",
        "tier2_title": "🥇 Enjambre Autopoiético Empresarial",
        "tier2_price": "**99€** (Acceso vitalicio)",
        "tier2_inc": "**Incluye:** Motor de consenso BFT completo, sincronización de BD vectorial.",
        "tier2_ideal": "**Ideal para:** Fundadores que construyen activos digitales.",
        "checkout_btn": "Pago Seguro (Stripe)",
        "audit_title": "Pista de Auditoría BFT y Sincronización Vectorial",
        "footer": "Núcleo Autopoiético NEXUS-01 • Diseñado para un Crecimiento Sostenible"
    },
    "Français": {
        "lang_label": "🌐 Langue",
        "hero_title": "⚛️ Architecture du Noyau NEXUS-01",
        "hero_subtitle": "Infrastructure SEO programmatique autonome conçue pour l'acquisition de trafic organique à haute intention et la monétisation évolutive.",
        "m1": "Moteur d'Architecture", "m1_sub": "DAG Autopoïétique",
        "m2": "Pages pSEO Actives", "m2_sub": "Optimisé",
        "m3": "Sécurité du Consensus", "m3_sub": "Protégé BFT",
        "m4": "Modèle Cible", "m4_sub": "Haute Intention",
        "tab1": "🧬 1. Matrice Stratégique",
        "tab2": "📝 2. Usine pSEO",
        "tab3": "💳 3. Niveaux Entreprise",
        "tab4": "🛡️ 4. Journal d'Audit",
        "mat_title": "Paramètres d'Architecture",
        "stack_label": "Pile d'Infrastructure:",
        "intent_label": "Intention de Conversion:",
        "mat_btn": "Générer la Matrice de Longue Traîne",
        "mat_success": "Matrice étendue avec succès sur 4 clusters sémantiques.",
        "eco_title": "Méthodologie Économique",
        "eco_desc": "* **Domination de Longue Traîne:** Capture des requêtes précises.\n* **Valeur Asymétrique:** Fournit des boilerplates prêts pour la production.\n* **Mise à l'échelle Autopoïétique:** Chaque page étend la mémoire vectorielle.",
        "fac_title": "Synthèse Autonome de Pages pSEO",
        "fac_desc": "Synthétisez des pages de destination optimisées pour les acheteurs techniques.",
        "kw_label": "Mot-clé Cible:",
        "persona_label": "Persona Principal:",
        "fac_btn": "Synthétiser la Page d'Architecture",
        "fac_success": "Synthétisé avec succès:",
        "reg_title": "Registre des Actifs Actifs",
        "mon_title": "Niveaux de Service et de Licence",
        "mon_desc": "Modèles de tarification transparents ancrés sur la valeur.",
        "tier1_title": "🥉 Kit de Démarrage Standard",
        "tier1_price": "**39€** (Paiement unique)",
        "tier1_inc": "**Comprend:** Boilerplate de base pSEO, générateur de matrice.",
        "tier1_ideal": "**Idéal pour:** Développeurs individuels.",
        "tier2_title": "🥇 Essaim Autopoïétique d'Entreprise",
        "tier2_price": "**99€** (Accès à vie)",
        "tier2_inc": "**Comprend:** Moteur de consensus BFT complet, synchronisation BD.",
        "tier2_ideal": "**Idéal pour:** Fondateurs d'actifs numériques.",
        "checkout_btn": "Paiement Sécurisé (Stripe)",
        "audit_title": "Piste d'Audit BFT et Synchro Vectorielle",
        "footer": "Noyau Autopoïétique NEXUS-01 • Conçu pour une Croissance Durable"
    },
    "Deutsch": {
        "lang_label": "🌐 Sprache",
        "hero_title": "⚛️ NEXUS-01 Kernarchitektur",
        "hero_subtitle": "Autonome programmatische SEO-Infrastruktur für hoch-intentierten organischen Datenverkehr und skalierbare Monetarisierung.",
        "m1": "Architektur-Engine", "m1_sub": "Autopoietischer DAG",
        "m2": "Aktive pSEO-Seiten", "m2_sub": "Optimiert",
        "m3": "Konsenssicherheit", "m3_sub": "BFT Geschützt",
        "m4": "Zielmodell", "m4_sub": "Hohe Intention",
        "tab1": "🧬 1. Strategische Matrix",
        "tab2": "📝 2. pSEO Fabrik",
        "tab3": "💳 3. Unternehmensstufen",
        "tab4": "🛡️ 4. System-Audit-Protokoll",
        "mat_title": "Zielarchitekturparameter",
        "stack_label": "Infrastruktur-Stack:",
        "intent_label": "Konversionsabsicht:",
        "mat_btn": "Long-Tail-Matrix Generieren",
        "mat_success": "Matrix erfolgreich über 4 semantische Cluster erweitert.",
        "eco_title": "Wirtschaftliche Methodik",
        "eco_desc": "* **Long-Tail-Dominanz:** Erfasst präzise, wettbewerbsarme Suchanfragen.\n* **Asymmetrischer Wert:** Bietet produktionsfertige Boilerplates.\n* **Autopoietische Skalierung:** Jede Seite erweitert den Vektorspeicher.",
        "fac_title": "Autonome pSEO-Seitensynthese",
        "fac_desc": "Synthetisieren Sie optimierte Landingpages für technische Käufer.",
        "kw_label": "Ziel-Keyword:",
        "persona_label": "Primäre Persona:",
        "fac_btn": "Architekturseite Synthetisieren",
        "fac_success": "Erfolgreich synthetisiert:",
        "reg_title": "Aktives Asset-Register",
        "mon_title": "Produktisierte Service- und Lizenzierungsstufen",
        "mon_desc": "Transparente, wertverankerte Preismodelle.",
        "tier1_title": "🥉 Standard Starter-Kit",
        "tier1_price": "**39€** (Einmalig)",
        "tier1_inc": "**Enthält:** Core pSEO-Boilerplate, Matrix-Generator und Leitfaden.",
        "tier1_ideal": "**Ideal für:** Einzelentwickler.",
        "tier2_title": "🥇 Enterprise Autopoietischer Schwarm",
        "tier2_price": "**99€** (Lebenszeit-Zugang)",
        "tier2_inc": "**Enthält:** Vollständige BFT-Konsens-Engine, Vektordatenbank-Sync.",
        "tier2_ideal": "**Ideal für:** Gründer skalierbarer digitaler Assets.",
        "checkout_btn": "Sicherer Checkout (Stripe)",
        "audit_title": "BFT & Vektor-Sync Audit-Trail",
        "footer": "NEXUS-01 Autopoietischer Kern • Für Nachhaltiges Wachsen Entwickelt"
    },
    "中文": {
        "lang_label": "🌐 语言",
        "hero_title": "⚛️ NEXUS-01 核心架构",
        "hero_subtitle": "专为高意图有机流量获取、拓扑神经演化和可扩展产品化变现而设计的自主编程SEO基础架构。",
        "m1": "架构引擎", "m1_sub": "自创生 DAG",
        "m2": "活动 pSEO 页面", "m2_sub": "已优化",
        "m3": "共识安全性", "m3_sub": "BFT 保护",
        "m4": "目标收益模型", "m4_sub": "高意图",
        "tab1": "🧬 1. 战略矩阵",
        "tab2": "📝 2. pSEO 工厂",
        "tab3": "💳 3. 企业阶梯",
        "tab4": "🛡️ 4. 系统审计日志",
        "mat_title": "目标架构参数",
        "stack_label": "基础架构栈:",
        "intent_label": "转化意图:",
        "mat_btn": "生成长尾矩阵",
        "mat_success": "矩阵已成功跨 4 个主要语义集群扩展。",
        "eco_title": "经济方法论",
        "eco_desc": "* **长尾主导:** 捕获具有高转化意图的精确、低竞争查询。\n* **非对称价值:** 提供完整的生产就绪样板。\n* **自创生扩展:** 每个合成页面都会扩展内部向量内存空间。",
        "fac_title": "自主 pSEO 页面合成",
        "fac_desc": "为技术买家定制合成高排名、程序优化的着陆页。",
        "kw_label": "目标长尾关键词:",
        "persona_label": "主要角色:",
        "fac_btn": "合成架构页面",
        "fac_success": "成功合成:",
        "reg_title": "活动资产注册表",
        "mon_title": "产品化服务与许可阶梯",
        "mon_desc": "透明的、基于价值锚定的定价模型。",
        "tier1_title": "🥉 标准入门套件",
        "tier1_price": "**39€** (一次性)",
        "tier1_inc": "**包含:** 核心 Python/Streamlit pSEO 样板、基础矩阵生成器和部署指南。",
        "tier1_ideal": "**适合人群:** 测试自主流量流的独立开发者。",
        "tier2_title": "🥇 企业自创生集群",
        "tier2_price": "**99€** (终身访问)",
        "tier2_inc": "**包含:** 完整 BFT 共识引擎、向量数据库同步、多节点 DAG 变形和优先更新。",
        "tier2_ideal": "**适合人群:** 构建可扩展多行业数字资产的创始人。",
        "checkout_btn": "安全结账 (Stripe)",
        "audit_title": "BFT 与向量同步审计跟踪",
        "footer": "NEXUS-01 自创生核心 • 专为可持续自主增长而设计"
    },
    "हिन्दी": {
        "lang_label": "🌐 भाषा",
        "hero_title": "⚛️ NEXUS-01 कोर आर्किटेक्चर",
        "hero_subtitle": "उच्च-इरादे वाले जैविक ट्रैफ़िक अधिग्रहण, टोपोलॉजिकल न्यूरो-इवोल्यूशन और स्केलेबल मुद्रीकरण के लिए इंजीनियर किया गया स्वायत्त pSEO बुनियादी ढांचा।",
        "m1": "आर्किटेक्चर इंजन", "m1_sub": "ऑटोपोएटिक DAG",
        "m2": "सक्रिय pSEO पेज", "m2_sub": "अनुकूलित",
        "m3": "सहमति सुरक्षा", "m3_sub": "BFT संरक्षित",
        "m4": "लक्ष्य उपज मॉडल", "m4_sub": "उच्च इरादा",
        "tab1": "🧬 1. रणनीतिक मैट्रिक्स",
        "tab2": "📝 2. pSEO फ़ैक्टरी",
        "tab3": "💳 3. एंटरप्राइज टीयर",
        "tab4": "🛡️ 4. सिस्टम ऑडिट लॉग",
        "mat_title": "लक्ष्य वास्तुकला पैरामीटर",
        "stack_label": "इन्फ्रास्ट्रक्चर स्टैक:",
        "intent_label": "परिवर्तन इरादा:",
        "mat_btn": "लॉन्ग-टेल मैट्रिक्स जनरेट करें",
        "mat_success": "मैट्रिक्स 4 प्राथमिक सिमेंटिक क्लस्टर में सफलतापूर्वक विस्तारित हुआ।",
        "eco_title": "आर्थिक पद्धति",
        "eco_desc": "* **लॉन्ग-टेल प्रभुत्व:** उच्च रूपांतरण इरादे के साथ सटीक, कम-प्रतिस्पर्धा प्रश्नों को कैप्चर करता है।\n* **असममित मूल्य:** उथले पाठ सारांश के बजाय पूर्ण, उत्पादन-तैयार बॉयलरप्लेट प्रदान करता है।\n* **ऑटोपोएटिक स्केलिंग:** प्रत्येक संश्लेषित पृष्ठ आंतरिक वेक्टर मेमोरी स्पेस का विस्तार करता है।",
        "fac_title": "स्वायत्त pSEO पेज संश्लेषण",
        "fac_desc": "तकनीकी खरीदारों के लिए सिलवाया गया लैंडिंग पेज बनाएं।",
        "kw_label": "लक्ष्य लॉन्ग-टेल कीवर्ड:",
        "persona_label": "प्राथमिक व्यक्ति:",
        "fac_btn": "आर्किटेक्चर पेज सिंथेटाइज करें",
        "fac_success": "सफलतापूर्वक संश्लेषित:",
        "reg_title": "सक्रिय संपत्ति रजिस्ट्री",
        "mon_title": "उत्पादित सेवा और लाइसेंसिंग टीयर",
        "mon_desc": "पारदर्शी, मूल्य-युक्त मूल्य निर्धारण मॉडल।",
        "tier1_title": "🥉 मानक स्टार्टर किट",
        "tier1_price": "**39€** (एक बार)",
        "tier1_inc": "**शामिल है:** कोर पायथन/स्ट्रीमलाइट pSEO बॉयलरप्लेट, बेसिक कीवर्ड मैट्रिक्स जेनरेटर।",
        "tier1_ideal": "**इसके लिए आदर्श:** व्यक्तिगत डेवलपर्स।",
        "tier2_title": "🥇 एंटरप्राइज़ ऑटोपोएटिक स्वार्म",
        "tier2_price": "**99€** (आजीवन पहुंच)",
        "tier2_inc": "**शामिल है:** पूर्ण BFT सर्वसम्मति इंजन, वेक्टर DB सिंक्रनाइज़ेशन।",
        "tier2_ideal": "**इसके लिए आदर्श:** डिजिटल संपत्ति बनाने वाले संस्थापक।",
        "checkout_btn": "सुरक्षित चेकआउट (Stripe)",
        "audit_title": "BFT और वेक्टर-सिंक ऑडिट ट्रेल",
        "footer": "NEXUS-01 ऑटोपोएटिक कोर • सतत विकास के लिए इंजीनियर"
    },
    "العربية": {
        "lang_label": "🌐 اللغة",
        "hero_title": "⚛️ هندسة نواة NEXUS-01",
        "hero_subtitle": "بنية تحتية مستقلة لتحسين محركات البحث المبرمجة مصممة خصيصًا لاكتساب حركة المرور العضوية عالية النية والتحول العصبي الطوبولوجي.",
        "m1": "محرك الهندسة", "m1_sub": "DAG ذاتي التكوين",
        "m2": "صفحات pSEO النشطة", "m2_sub": "متحسن",
        "m3": "أمان التوافق", "m3_sub": "محمي بـ BFT",
        "m4": "نموذج العائد المستهدف", "m4_sub": "نية عالية",
        "tab1": "🧬 1. المصفوفة الاستراتيجية",
        "tab2": "📝 2. مصنع pSEO",
        "tab3": "💳 3. المستويات المؤسسية",
        "tab4": "🛡️ 4. سجل تدقيق النظام",
        "mat_title": "معلمات الهندسة المستهدفة",
        "stack_label": "حزمة البنية التحتية:",
        "intent_label": "نية التحويل:",
        "mat_btn": "إنشاء مصفوفة الذيل الطويل",
        "mat_success": "تم توسيع المصفوفة بنجاح عبر 4 مجموعات دلالية أساسية.",
        "eco_title": "المنهجية الاقتصادية",
        "eco_desc": "* **هيمنة الذيل الطويل:** تلتقط استعلامات دقيقة منخفضة المنافسة.\n* **قيمة غير متناظرة:** تقدم نماذج جاهزة للإنتاج.\n* **التوسع الذاتي:** توسع كل صفحة مصممة ذاكرة المتجهات الداخلية.",
        "fac_title": "تخليق صفحة pSEO المستقلة",
        "fac_desc": "تخليق صفحات مقصودة مُحسينه خصيصًا للمشترين التقنيين.",
        "kw_label": "الكلمة المفتاحية المستهدفة:",
        "persona_label": "الشخصية الأساسية:",
        "fac_btn": "تخليق صفحة الهندسة",
        "fac_success": "تم التخليق بنجاح:",
        "reg_title": "سجل الأصول النشطة",
        "mon_title": "مستويات الخدمة والترخيص المنتجة",
        "mon_desc": "نماذج تسعير شفافة ومرتكزة على القيمة.",
        "tier1_title": "🥉 مجموعة البدء القياسية",
        "tier1_price": "**39€** (مرة واحدة)",
        "tier1_inc": "**تتضمن:** نموذج pSEO الأساسي، ومولد مصفوفة الكلمات الرئيسية.",
        "tier1_ideal": "**مثالي لـ:** المطورين الأفراد.",
        "tier2_title": "🥇 سرب المؤسسات ذاتي التكوين",
        "tier2_price": "**99€** (وصول مدى الحياة)",
        "tier2_inc": "**يتضمن:** محرك توافق BFT الكامل، ومزامنة قاعدة بيانات المتجهات.",
        "tier2_ideal": "**مثالي لـ:** المؤسسين الذين يبنون أصولًا رقمية قابلة للتوسع.",
        "checkout_btn": "الدفع الآمن (Stripe)",
        "audit_title": "مسار تدقيق BFT ومزامنة المتجهات",
        "footer": "نواة NEXUS-01 ذاتية التكوين • مصممة للنمو المستدام المستقل"
    },
    "Português": {
        "lang_label": "🌐 Idioma",
        "hero_title": "⚛️ Arquitetura do Núcleo NEXUS-01",
        "hero_subtitle": "Infraestrutura autônoma de SEO programático projetada para aquisição de tráfego orgânico de alta intenção e monetização escalável.",
        "m1": "Motor de Arquitetura", "m1_sub": "DAG Autopoiético",
        "m2": "Páginas pSEO Ativas", "m2_sub": "Otimizado",
        "m3": "Segurança de Consenso", "m3_sub": "Protegido BFT",
        "m4": "Modelo de Rendimento", "m4_sub": "Alta Intenção",
        "tab1": "🧬 1. Matriz Estratégica",
        "tab2": "📝 2. Fábrica pSEO",
        "tab3": "💳 3. Níveis Empresariais",
        "tab4": "🛡️ 4. Log de Auditoria",
        "mat_title": "Parâmetros de Arquitetura Alvo",
        "stack_label": "Pilha de Infraestrutura:",
        "intent_label": "Intenção de Conversão:",
        "mat_btn": "Gerar Matriz de Cauda Longa",
        "mat_success": "Matriz expandida com sucesso em 4 clusters semânticos.",
        "eco_title": "Metodologia Económica",
        "eco_desc": "* **Domínio de Cauda Longa:** Captura consultas precisas e de baixa concorrência.\n* **Valor Assimétrico:** Fornece boilerplates prontos para produção.\n* **Escalonamento Autopoiético:** Cada página sintetizada expande a memória vetorial.",
        "fac_title": "Síntese Autônoma de Páginas pSEO",
        "fac_desc": "Sintetize páginas de destino otimizadas para compradores técnicos.",
        "kw_label": "Palavra-chave Alvo:",
        "persona_label": "Persona Principal:",
        "fac_btn": "Sintetizar Página de Arquitetura",
        "fac_success": "Sintetizado com sucesso:",
        "reg_title": "Registro de Ativos Ativos",
        "mon_title": "Níveis de Serviço e Licenciamento",
        "mon_desc": "Modelos de preços transparentes ancorados no valor.",
        "tier1_title": "🥉 Kit Inicial Padrão",
        "tier1_price": "**39€** (Pagamento único)",
        "tier1_inc": "**Inclui:** Boilerplate pSEO, gerador de matriz e guia.",
        "tier1_ideal": "**Ideal para:** Desenvolvedores individuais.",
        "tier2_title": "🥇 Enxame Autopoiético Empresarial",
        "tier2_price": "**99€** (Acesso vitalicio)",
        "tier2_inc": "**Inclui:** Motor de consenso BFT completo, sincronização DB.",
        "tier2_ideal": "**Ideal para:** Fundadores construindo ativos digitais.",
        "checkout_btn": "Checkout Seguro (Stripe)",
        "audit_title": "Trilha de Auditoria BFT e Sincronização Vetorial",
        "footer": "Núcleo Autopoiético NEXUS-01 • Projetado para Crescimento Sustentável"
    },
    "Русский": {
        "lang_label": "🌐 Язык",
        "hero_title": "⚛️ Ядро архитектуры NEXUS-01",
        "hero_subtitle": "Автономная программная SEO-инфраструктура, разработанная для привлечения органического трафика с высокой степенью намерения и масштабируемой монетизации.",
        "m1": "Движок архитектуры", "m1_sub": "Автопоэтический DAG",
        "m2": "Активные pSEO страницы", "m2_sub": "Оптимизировано",
        "m3": "Безопасность консенсуса", "m3_sub": "BFT Защита",
        "m4": "Целевая модель", "m4_sub": "Высокое намерение",
        "tab1": "🧬 1. Стратегическая матрица",
        "tab2": "📝 2. pSEO Фабрика",
        "tab3": "💳 3. Корпоративные тарифы",
        "tab4": "🛡️ 4. Журнал аудита системы",
        "mat_title": "Параметры целевой архитектуры",
        "stack_label": "Инфраструктурный стек:",
        "intent_label": "Цель конверсии:",
        "mat_btn": "Сгенерировать длиннохвостую матрицу",
        "mat_success": "Матрица успешно расширена по 4 семантическим кластерам.",
        "eco_title": "Экономическая методология",
        "eco_desc": "* **Доминирование длинного хвоста:** Захватывает точные запросы с низкой конкуренцией.\n* **Асимметричная ценность:** Предоставляет готовые к продакшну шаблоны.\n* **Автопоэтическое масштабирование:** Каждая синтезированная страница расширяет векторную память.",
        "fac_title": "Автономный синтез pSEO страниц",
        "fac_desc": "Синтезируйте оптимизированные целевые страницы для технических покупателей.",
        "kw_label": "Целевое ключевое слово:",
        "persona_label": "Основной персонаж:",
        "fac_btn": "Синтезировать страницу архитектуры",
        "fac_success": "Успешно синтезировано:",
        "reg_title": "Реестр активных активов",
        "mon_title": "Продуктовые уровни и лицензирование",
        "mon_desc": "Прозрачные модели ценообразования, привязанные к ценности.",
        "tier1_title": "🥉 Стандартный стартовый набор",
        "tier1_price": "**39€** (Единоразово)",
        "tier1_inc": "**Включает:** Базовый шаблон pSEO, генератор матрицы и руководство.",
        "tier1_ideal": "**Идеально для:** Индивидуальных разработчиков.",
        "tier2_title": "🥇 Корпоративный автопоэтический рой",
        "tier2_price": "**99€** (Пожизненный доступ)",
        "tier2_inc": "**Включает:** Полный консенсусный движок BFT, синхронизацию векторной БД.",
        "tier2_ideal": "**Идеально для:** Основателей масштабируемых цифровых активов.",
        "checkout_btn": "Безопасная оплата (Stripe)",
        "audit_title": "Аудит консенсуса BFT и синхронизации векторов",
        "footer": "Автопоэтическое ядро NEXUS-01 • Разработано для устойчивого роста"
    }
}

if "lang" not in st.session_state:
    st.session_state.lang = "Türkçe"

# Sidebar language selector
selected_lang = st.sidebar.selectbox("🌐 Dil / Language / Idioma", list(TRANSLATIONS.keys()), index=list(TRANSLATIONS.keys()).index(st.session_state.lang))
if selected_lang != st.session_state.lang:
    st.session_state.lang = selected_lang
    st.rerun()

t = TRANSLATIONS[st.session_state.lang]

# 3. CUSTOM CSS FOR VERCEL/LINEAR-GRADE UI
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .hero-container {
        padding: 2.5rem 2rem;
        background: linear-gradient(135deg, rgba(17, 24, 39, 0.8) 0%, rgba(31, 41, 55, 0.4) 100%);
        border: 1px solid rgba(75, 85, 99, 0.3);
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.025em;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #9ca3af;
        line-height: 1.5;
    }
    div[data-testid="metric-container"] {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    .stButton>button {
        width: 100%;
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 6px;
        padding: 0.6rem 1rem;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        box-shadow: 0 0 12px rgba(59, 130, 246, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 4. SESSION STATE INITIALIZATION
if "pseo_registry" not in st.session_state:
    st.session_state.pseo_registry = [
        {"Keyword": "Best AI Workflow Template for n8n", "Category": "Automation Boilerplate", "Status": "Synthesized & Live"}
    ]

if "system_logs" not in st.session_state:
    st.session_state.system_logs = [f"[{datetime.now().strftime('%H:%M:%S')}] Core initialized with BFT Consensus Guard."]

# 5. HERO SECTION
st.markdown(f"""
    <div class="hero-container">
        <div class="hero-title">{t['hero_title']}</div>
        <div class="hero-subtitle">{t['hero_subtitle']}</div>
    </div>
""", unsafe_allow_html=True)

# 6. SYSTEM METRICS
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric(label=t['m1'], value="Autopoietic DAG", delta=t['m1_sub'])
with col_m2:
    st.metric(label=t['m2'], value=f"{len(st.session_state.pseo_registry)} Pages", delta=t['m2_sub'])
with col_m3:
    st.metric(label=t['m3'], value="99.8% BFT", delta=t['m3_sub'])
with col_m4:
    st.metric(label=t['m4'], value="700€ - 1000€/mo", delta="High Intent")

st.divider()

# 7. TABS
tab_engine, tab_factory, tab_monetize, tab_audit = st.tabs([
    t['tab1'], t['tab2'], t['tab3'], t['tab4']
])

# --- TAB 1 ---
with tab_engine:
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.subheader(t['mat_title'])
        tech_stack = st.selectbox(t['stack_label'], ["Streamlit & Python Boilerplate", "FastAPI & Tailwind Boilerplate", "Next.js & Markdown Boilerplate"])
        intent_type = st.selectbox(t['intent_label'], ["High-Intent Developer Tools", "B2B Solopreneur Automation", "E-commerce Scraper Kits"])
        
        if st.button(t['mat_btn']):
            st.success(t['mat_success'])
            st.code(f"1. best-{tech_stack.lower().replace(' ', '-')}-for-{intent_type.lower().replace(' ', '-')}\n2. open-source-{intent_type.lower().replace(' ', '-')}-template\n3. automated-{tech_stack.lower().replace(' ', '-')}-generator", language="bash")
            
    with col_e2:
        st.subheader(t['eco_title'])
        st.markdown(t['eco_desc'])

# --- TAB 2 ---
with tab_factory:
    st.subheader(t['fac_title'])
    st.markdown(t['fac_desc'])
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        custom_kw = st.text_input(t['kw_label'], "Production-ready Streamlit boilerplate for programmatic SEO")
        target_audience = st.text_input(t['persona_label'], "Solopreneurs & Technical Founders")
        
        if st.button(t['fac_btn']):
            page_title = custom_kw.title()
            st.session_state.pseo_registry.append({"Keyword": custom_kw, "Category": "Synthesized Asset", "Status": "Ready for Deploy"})
            st.success(f"{t['fac_success']} {page_title}")
            
    with col_f2:
        st.subheader(t['reg_title'])
        df_assets = pd.DataFrame(st.session_state.pseo_registry)
        st.dataframe(df_assets, use_container_width=True)

# --- TAB 3 ---
with tab_monetize:
    st.subheader(t['mon_title'])
    st.markdown(t['mon_desc'])
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"""
            ### {t['tier1_title']}
            * **{t['tier1_price']}**
            * {t['tier1_inc']}
            * {t['tier1_ideal']}
        """)
        st.markdown(f"[{t['checkout_btn']}](https://buy.stripe.com/test_placeholder)")
        
    with col_p2:
        st.markdown(f"""
            ### {t['tier2_title']}
            * **{t['tier2_price']}**
            * {t['tier2_inc']}
            * {t['tier2_ideal']}
        """)
        st.markdown(f"[{t['checkout_btn']}](https://buy.stripe.com/test_placeholder)")

# --- TAB 4 ---
with tab_audit:
    st.subheader(t['audit_title'])
    log_box = st.container(height=300)
    with log_box:
        for log in st.session_state.system_logs:
            st.text(log)

st.divider()
st.markdown(f"<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>{t['footer']}</p>", unsafe_allow_html=True)
