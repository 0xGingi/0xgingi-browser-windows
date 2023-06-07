<div align="center">

  ![logo](https://github.com/0xGingi/0xgingi-browser/assets/104647854/cec41b3d-0279-4405-89f0-33d6682b681c)


# 0xGingi Browser
An experimental [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium-windows) fork that enhances privacy and security.

</div>

## Features
|--|Features of 0xGingi Browser|
|--|--|
|--|Removed Telemetry/All Google Services|
|--|Inox patchset|
|--|Bromite Patches|
|--|Debian Patches|
|--|Iridium Browser Patches|
|--|Chromium source based browser with regular security updates|
|--|Adequately maintained repository and software|

## Install
[Releases](https://github.com/0xgingi/0xgingi-browser/releases) page.

*Highly Reccomended To Install [Ublock Origin](https://github.com/gorhill/uBlock/releases/tag/1.49.2) Extension with setting reccomendations from [Arkenfox](https://github.com/arkenfox/user.js/wiki/4.1-Extensions)*

Alternativly, instead of manually installing add-ons, [follow this guide](https://avoidthehack.com/manually-install-extensions-ungoogled-chromium) to install the chromium web store.

Whitelist Sites for Cookies at chrome://settings/cookies (Always use cookies)

## 0xGingi SearxNG Instance

Make SearxNG/search.0xgingi.com your default search engine:

![Animation](https://github.com/0xGingi/0xgingi-browser/assets/104647854/6fe1132b-25ee-45e2-b215-2542e5860407)

## DoH DNS Proxy
0xGingi-Browser comes with a DNS-Over-HTTPS Built-in. It proxies DNS to Cloudflare, Quad9, and NextDNS then uses the fastest responce. Of course, I collect no logs.
Enable it in [chrome://settings/security](chrome://settings/security) -> Use Secure DNS -> With -> 0xGingi

To Use the DNS Proxy outside of the Browser:
 
DoH: https://dns-proxy.0xgingi.com/dns-query

DoT: dns-proxy.0xgingi.com

## Goals

- Enhance Default Browser Privacy + Security OOTB
- Modify some internal chromium components with better alternatives (e.g. Bromite Patches)
- Remove google telemetry/spyware

## TO-DO

- Install some Plugins (eg Ublock Origin) by default
- More Hardening
- Other Misc. Changes to Enchance Privacy
- Automatic Updates (Best option until automatic updates are working is to watch for releases on github so you get a email when a new release is added, I will try to have all chromium updates released within 24 hours)
