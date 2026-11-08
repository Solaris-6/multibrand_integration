# Multibrand Integration for Home Assistant ⚡

Integrazione **moderna** per Home Assistant che supporta il rilevamento automatico e la configurazione tramite interfaccia di diversi brand:

## 🎯 Brand Supportati

- **Shelly** (49 prodotti)
- **Sonoff** (35 prodotti)
- **Tuya** (38 prodotti)
- **Bticino** (13 prodotti)
- **Vimar** (15 prodotti)

---

## ✨ Caratteristiche Principali

✅ Setup moderno con ConfigEntry (compatibile Home Assistant 2024.11+)  
✅ Configurazione tramite interfaccia utente  
✅ Supporto per sensori, switch e device tracker  
✅ Product catalog completo per tutti i brand  
✅ Traduzioni in italiano ed inglese  

---

## 📦 Installazione

### Opzione A: Tramite HACS (Consigliato)

1. Apri **HACS** nel tuo Home Assistant
2. Vai su **Integrations** → **+** → **Custom repositories**
3. Inserisci URL repository: `https://github.com/Solaris-6/multibrand_integration`
4. Seleziona **Integration** come tipo di repository
5. Installa e riavvia Home Assistant

### Opzione B: Installazione Manuale

```bash
# Crea directory nel config di Home Assistant
mkdir -p /config/custom_components/multibrand_integration

# Clona il repository (opzionale)
git clone https://github.com/Solaris-6/multibrand_integration.git /config/custom_components/multibrand_integration
```

3. Riavvia Home Assistant

4. Vai su **Impostazioni** → **Dispositivi e servizi** → **Aggiungi integrazione** → **Multibrand**

---

## ⚙️ Configurazione

### Primo Uso

1. Aggiungi l'integrazione Multibrand
2. Il sistema esegue automaticamente il discovery dei dispositivi
3. Configura gli indirizzi IP dei vari brand (opzionale)

### Dispositivi Supportati

L'integrazione supporta automaticamente:

- **Switch/Plug**: Shelly Plug, Sonoff, Tuya plugs
- **Sensori**: Temperatura, umidità, energia
- **Luce**: Smart lights RGBW, dimmer
- **Tracker**: Motion detection, temperature

---

## 🌐 Protocolli di Comunicazione

### Shelly
```
Endpoint: /rpc
Porta: 80 (o quella configurata nel device)
API: REST RPC
```

### Sonoff
```
Endpoint: /
Porta: 80/443 (o eWeLink API su porta specifica)
```

### Tuya
```
Endpoint: /sm o /data
Porta: 80/443
API: Smart Life/Tuya Cloud
```

---

## 📋 Struttura Repository

```
multibrand_integration/
├── custom_components/
│   └── multibrand/
│       ├── __init__.py        # Setup entry + discovery
│       ├── config_flow.py     # Configurazione UI
│       ├── const.py           # Costanti
│       ├── manifest.json      # Metadata
│       ├── hacs.json          # HACS metadata
│       ├── sensor.py          # Piattaforma sensori
│       ├── switch.py          # Piattaforma switch
│       ├── device_tracker.py  # Piattaforma tracker
│       └── translations/       # File traduzioni (opzionale)
├── README.md
└── LICENSE
```

---

## 🐛 Debug e Log

### Abilitare log dettagliati

Modifica `configuration.yaml`:
```yaml
logger:
  default: debug
  logs:
    homeassistant.components.multibrand: debug
```

Riavvia Home Assistant per applicare.

---

## ⚠️ Note Importanti

### Compatibilità Home Assistant

- **Minima**: Home Assistant 2024.11.0 o superiore
- **Consigliata**: Home Assistant 2025.x o versioni successive
- **Piattaforma**: Linux, Docker, Supervised, OSM

### Requisiti Sistemistici

- Python 3.11+ (per requisiti di Home Assistant)
- Accesso alla rete locale per discovery
- Portata Wi-Fi/Ethernet sufficiente

---

## 🔄 Aggiornamenti e Manutenzione

### Aggiornamento HACS

1. Apri HACS → Integrations
2. Seleziona **Multibrand** dall'elenco
3. Clicca su **Update** se disponibile

### Aggiornamento Manuale

```bash
# Nel repository GitHub
cd /config/custom_components/multibrand_integration
git pull origin main

# Riavvia Home Assistant
```

---

## 📊 Supporto e Risorse

### GitHub Repository
- **Main**: https://github.com/Solaris-6/multibrand_integration
- **Issues**: https://github.com/Solaris-6/multibrand_integration/issues
- **Wiki**: Documentazione completa disponibile su GitHub

### Home Assistant Community
- Forum ufficiale: https://community.home-assistant.io/
- Discussione HACS: https://community.home-assistant.io/t/hacs-discussion-multibrand-integration/
- Discord: https://discord.gg/home-assistant

---

## 📜 Licenza

Questo progetto è distribuito con licenza MIT. Vedi file `LICENSE` per dettagli.

```
MIT License

Copyright (c) 2024-2025 Solaris-6

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contatti e Contributi

Vuoi contribuire? Apri una Issue su GitHub o crea un Pull Request!

**Autore**: Solaris-6  
**Data Ultima Revisione**: 2025-11-06  
**Versione**: 2.0.0 (Corretto)

---

## 🎉 Grazie per l'uso!

Buon automazione con Home Assistant! 🏠⚡