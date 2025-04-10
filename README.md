# Heise Integration for Home Assistant 🏠

[![GitHub Release](https://img.shields.io/github/v/release/timniklas/hass-heiseonline?sort=semver&style=for-the-badge&color=green)](https://github.com/timniklas/hass-heiseonline/releases/)
[![GitHub Release Date](https://img.shields.io/github/release-date/timniklas/hass-heiseonline?style=for-the-badge&color=green)](https://github.com/timniklas/hass-heiseonline/releases/)
![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/timniklas/hass-heiseonline/latest/total?style=for-the-badge&label=Downloads%20latest%20Release)
![HA Analytics](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.heiseonline.total&style=for-the-badge&label=Active%20Installations&color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/timniklas/hass-heiseonline?style=for-the-badge)
[![hacs](https://img.shields.io/badge/HACS-Integration-blue.svg?style=for-the-badge)](https://github.com/hacs/integration)

## Overview

The Heise Home Assistant Custom Integration allows you to integrate the heiseonline news with your Home Assistant setup.

 ```
<h1><img src="https://www.heise.de/download/media/heise-online-app-fuer-android-78501/heise-online-news-logo_1-1-30.png"  height="26"> Heise Security</h1>
{%- for i in range(2) %}
{%- set title = states("sensor.heiseonline_security_alert_meldungen_"~ loop.index) %}
{%- set updated = state_attr("sensor.heiseonline_security_alert_meldungen_"~ loop.index, "updated") %}
{%- set link = state_attr("sensor.heiseonline_security_alert_meldungen_"~ loop.index, "link") %}
{%- set summary = state_attr("sensor.heiseonline_security_alert_meldungen_"~ loop.index, "summary") %}
<img src="https://www.heise.de/assets/heise/images/flammen.238.ltc.svg"  height="16"> <a href="{{link}}"><b>{{title}}</b></a><br>
{{updated|as_datetime|time_since}} ago
<br/>
{%- if not loop.last %}<br>{%- endif %}
{%- endfor %}
 ```

## Installation

### HACS (recommended)

This integration is available in HACS (Home Assistant Community Store).

1. Install HACS if you don't have it already
2. Open HACS in Home Assistant
3. Go to any of the sections (integrations, frontend, automation).
4. Click on the 3 dots in the top right corner.
5. Select "Custom repositories"
6. Add following URL to the repository `https://github.com/timniklas/hass-heiseonline`.
7. Select Integration as category.
8. Click the "ADD" button
9. Search for "Fitness Park"
10. Click the "Download" button

### Manual

To install this integration manually you have to download [_heiseonline.zip_](https://github.com/timniklas/hass-heiseonline/releases/latest/) and extract its contents to `config/custom_components/heiseonline` directory:

```bash
mkdir -p custom_components/heiseonline
cd custom_components/heiseonline
wget https://github.com/timniklas/hass-fitx/releases/latest/download/heiseonline.zip
unzip heiseonline.zip
rm heiseonline.zip
```

## Configuration

### Using UI

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=heiseonline)

From the Home Assistant front page go to `Configuration` and then select `Devices & Services` from the list.
Use the `Add Integration` button in the bottom right to add a new integration called `heiseonline`.

## Help and Contribution

If you find a problem, feel free to report it and I will do my best to help you.
If you have something to contribute, your help is greatly appreciated!
If you want to add a new feature, add a pull request first so we can discuss the details.

## Disclaimer

This custom integration is not officially endorsed or supported by heiseonline.
Use it at your own risk and ensure that you comply with all relevant terms of service and privacy policies.
