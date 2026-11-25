<!-- header:begin (generated from project metadata) -->
<h1 align="center">WiFi Drone</h1>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=seb5594&amp;repository=hass-wifi_drone-integration&amp;category=integration"><img src="https://img.shields.io/static/v1?label=HACS%20%C2%B7%20Marketplace&amp;message=Add%20integration&amp;color=41BDF5&amp;logo=homeassistantcommunitystore&amp;logoColor=white&amp;style=for-the-badge" alt="HACS · Marketplace" height="28"></a>
  <a href="https://github.com/seb5594/hass-wifi_drone-integration/actions/workflows/compat.yml"><img src="https://img.shields.io/static/v1?label=home%20assistant&amp;message=%E2%89%A5%202025.4.0&amp;color=1877A5&amp;style=for-the-badge" alt="home assistant" height="28"></a><br>
  <a href="https://github.com/seb5594/hass-wifi_drone-integration/releases"><img src="https://img.shields.io/static/v1?label=integration%20version&amp;message=0.1.0&amp;color=1877A5&amp;style=for-the-badge" alt="integration version" height="28"></a><br>
  <a href="https://github.com/seb5594/hass-wifi_drone-integration/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/seb5594/hass-wifi_drone-integration/ci.yml?branch=main&amp;label=checks&amp;style=flat" alt="checks" height="20"></a>
  <a href="https://github.com/seb5594/hass-wifi_drone-integration/issues"><img src="https://img.shields.io/github/issues/seb5594/hass-wifi_drone-integration?label=issues&amp;style=flat" alt="issues" height="20"></a><br>
  <a href="https://paypal.me/seb5594"><img src="https://img.shields.io/static/v1?label=Support&amp;message=PayPal&amp;color=0070BA&amp;logo=paypal&amp;logoColor=white&amp;style=for-the-badge" alt="PayPal" height="24"></a>
  <a href="https://buymeacoffee.com/seb5594"><img src="https://raw.githubusercontent.com/seb5594/Home-Assistant-Apps/473dc258f963096745aac327df54950eb9b59066/.github/assets/support-beer.svg" alt="Buy me a beer" height="24"></a><br>
  <a href="https://github.com/seb5594/hass-wifi_drone-integration#license"><img src="https://img.shields.io/github/license/seb5594/hass-wifi_drone-integration?label=license&amp;style=flat" alt="license" height="20"></a>
</p>
<!-- header:end -->

[Deutsch](README.de.md)

WiFi Drone connects Home Assistant to the local [WiFi Drone Bridge](https://github.com/seb5594/Home-Assistant-WiFi-Drone-App). It exposes a camera with live MJPEG and JPEG snapshots, a binary sensor for video connectivity and diagnostics with bridge and stream state.

## Installation

1. Start the bridge, configure the camera source and set its API token.
2. Add this GitHub repository to HACS as an **Integration** once a HACS ZIP release is available. To install from source, copy `custom_components/wifi_drone` into the Home Assistant configuration directory under `custom_components/`.
3. Restart Home Assistant. In **Settings → Devices & services**, add **WiFi Drone**.
4. Enter the bridge URL and API token. If installed directly from the app repository, use `http://c3b88628-wifi-drone:8099`. For other app catalogs use the hostname shown in the app's Info tab followed by port 8099.

Compatible with Home Assistant 2025.4 or later. Choose **Reconfigure** on the integration to edit the URL or enter a new token. A picture entity card using the camera with live view enabled can display the stream in a dashboard.

<!-- support:begin (generated, shared text) -->
## Say thanks

All my projects are built in my spare time, just for the fun of it. Still, they take a lot of time and care, and many of the smart home gadgets I buy end up here because I want to make them cloud-free and smart-home ready. Every bit of support means a lot to me.

If my work helped you or turned out to be useful, show your appreciation with a hot drink for my next sleepless night.

[![PayPal](https://img.shields.io/static/v1?label=Support&message=PayPal&color=0070BA&logo=paypal&logoColor=white&style=for-the-badge)](https://paypal.me/seb5594) [![Buy me a beer](https://raw.githubusercontent.com/seb5594/Home-Assistant-Apps/473dc258f963096745aac327df54950eb9b59066/.github/assets/support-beer.svg)](https://buymeacoffee.com/seb5594)
<!-- support:end -->

<!-- license:begin (generated from the license file) -->
## License

[![license](https://img.shields.io/static/v1?label=license&message=MIT&color=5B6770&style=flat)](LICENSE)

Published under the [MIT License](LICENSE).
<!-- license:end -->
