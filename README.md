## Regensensor voor Home Assistant

Deze custom component voor Home Assistant biedt een regensensor die gebruikmaakt van gegevens van Buienradar. De sensor haalt regenverwachtingsgegevens op voor een opgegeven locatie en werkt de sensorstatus bij op basis van de aanwezigheid van regen in de komende intervallen.

### Kenmerken

- **Realtime Regengegevens**: Gebruikt de API van Buienradar om regengegevens op te halen voor een gegeven breedte- en lengtegraad.
- **Aanpasbaar**: Eenvoudig te configureren via de `configuration.yaml` van Home Assistant.
- **Eenvoudige Statusrapportage**: Rapporteert `true` als er regen wordt gedetecteerd in de komende intervallen, anders `false`.

### Installatie

1. Download of kloon deze repository.
2. Kopieer de `regensensor` map naar je `custom_components` map in je Home Assistant configuratiemap.
3. Voeg het volgende toe aan je `configuration.yaml`:

    ```yaml
    sensor:
      - platform: regensensor
        name: "Mijn Regensensor"
        latitude: "52.10473"
        longitude: "5.37501"
    ```

4. Herstart Home Assistant.

### Configuratie

- **name**: (Optioneel) De naam van de sensor. Standaard `Regensensor`.
- **latitude**: (Vereist) De breedtegraad van de locatie om te monitoren.
- **longitude**: (Vereist) De lengtegraad van de locatie om te monitoren.

### Voorbeeld Configuratie

```yaml
sensor:
  - platform: regensensor
    name: "Mijn Regensensor"
    latitude: "52.10473"
    longitude: "5.37501"
```
### Licentie
Dit project is gelicentieerd onder de MIT-licentie.
