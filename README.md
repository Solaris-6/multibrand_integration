# Multibrand Integration for Home Assistant

Integrazione per Home Assistant che supporta il rilevamento automatico di dispositivi di diverse marche:

- **Shelly** (49 prodotti)
- **Sonoff** (35 prodotti)  
- **Tuya** (38 prodotti)
- **Bticino** (13 prodotti)
- **Vimar** (15 prodotti)

## Installazione

### Con HACS

1. Apri HACS nel tuo Home Assistant
2. Vai su **Integrations**
3. Clicca su **+** → **Custom repositories**
4. Inserisci: `https://github.com/Solaris-6/multibrand_integration`
5. Seleziona **Integration** come tipo
6. Installa è pronto!

### Manualmente

1. Clona questo repository nella cartella `custom_components/` di Home Assistant:
   ```
   custom_components/multibrand_integration/
   ```

2. Riavvia Home Assistant

3. Vai su **Impostazioni** → **Dispositivi e servizi** → **Aggiungi integrazione** → **Multibrand**

## Configurazione

Modifica il file `__init__.py` per cambiare gli indirizzi IP di rete:
- Shelly: `http://192.168.1.1/rpc`
- Sonoff: `http://192.168.1.1:8080`
- Tuya: `http://192.168.1.1:6666`
- Bticino: `http://192.168.1.1/bticino`
- Vimar: `http://192.168.1.1/vimar`

## Supporto

Per segnalazioni, contributi o domande:
- GitHub: https://github.com/Solaris-6/multibrand_integration
- Home Assistant Community: https://community.home-assistant.io/

## License

MIT License
