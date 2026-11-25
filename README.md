# WiFi Drone for Home Assistant

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

[![PayPal](https://img.shields.io/static/v1?label=Support&message=PayPal&color=0070BA&logo=paypal&logoColor=white&style=for-the-badge)](https://paypal.me/seb5594) [![Buy Me a Coffee](https://img.shields.io/static/v1?label=Support&message=Buy%20Me%20a%20Coffee&color=FFDD00&logo=buy-me-a-coffee&logoColor=black&style=for-the-badge)](https://buymeacoffee.com/seb5594)
<!-- support:end -->

<!-- license:begin (generated from the license file) -->
## License

Released under the [MIT License](LICENSE).
<!-- license:end -->
