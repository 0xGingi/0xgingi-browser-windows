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

Alternativly, instead of manually installing add-ons, install the chromium web store. See Below For Instructions.

Whitelist Sites for Cookies at chrome://settings/cookies (Always use cookies)

## 0xGingi SearxNG Instance

Make my SearxNG Instance https://search.0xgingi.com your default search engine 

No logs are collected, this includes Queries and IP Addresses:

![Animation](https://github.com/0xGingi/0xgingi-browser/assets/104647854/6fe1132b-25ee-45e2-b215-2542e5860407)

## DoH DNS Proxy
0xGingi-Browser comes with a DNS-Over-HTTPS Proxy Built-in. It proxies DNS to Cloudflare, Quad9, and NextDNS then uses the fastest responce. 

No logs are collected, this includes Queries and IP Addresses.

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

## Install Chromium Web Store
The Chromium Web Store Exension allows you to install extensions from the chrome web store

Change The Flag chrome://flags/#extension-mime-request-handling to Always prompt for install

Download the latest .crx from [https://github.com/NeverDecaf/chromium-web-store/releases](https://github.com/NeverDecaf/chromium-web-store/releases)

Upon Downloading, the browser should prompt for you to install the extension. 

## Building

### Setting up the build environment

#### Setting up Visual Studio

[Follow the "Visual Studio" section of the official Windows build instructions](https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/windows_build_instructions.md#visual-studio).

* Make sure to read through the entire section and install/configure all the required components.
* If your Visual Studio is installed in a directory other than the default, you'll need to set a few environment variables to point the toolchains to your installation path. (Copied from [instructions for Electron](https://electronjs.org/docs/development/build-instructions-windows))
	* `vs2022_install = DRIVE:\path\to\Microsoft Visual Studio\2022\Community` (replace `2022` and `Community` with your installed versions)
	* `WINDOWSSDKDIR = DRIVE:\path\to\Windows Kits\10`
	* `GYP_MSVS_VERSION = 2022` (replace 2022 with your installed version's year)


#### Other build requirements

**IMPORTANT**: Currently, the `MAX_PATH` path length restriction (which is 260 characters by default) must be lifted in for our Python build scripts. This can be lifted in Windows 10 (v1607 or newer) with the official installer for Python 3.6 or newer (you will see a button at the end of installation to do this). See [Issue #345](https://github.com/Eloston/ungoogled-chromium/issues/345) for other methods for other Windows versions.

1. Setup the following:

    * 7-zip
    * Python 3.6 - 3.9 or 3.10.2+ (for build and packaging scripts used below)
        * At the end of the Python installer, click the button to lift the `MAX_PATH` length restriction.
        * Check that your `PATH` does not contain the `python3` wrapper shipped by Windows, as it will only promt you to install Python from the Microsoft Store and exit. See [this question on stackoverflow.com](https://stackoverflow.com/questions/57485491/python-python3-executes-in-command-prompt-but-does-not-run-correctly)
    * Git
        * During setup, make sure "Git from the command line and also from 3rd-party software" is selected. This is usually the recommended option.

### Building

NOTE: The commands below assume the `py` command was installed by Python 3 into `PATH`. If this is not the case, then substitute it with `python3`.

Run in `cmd.exe` (as administrator):

```cmd
git clone https://github.com/0xGingi/0xgingi-browser
py build.py
cp -r modified-files/* ./
py rebrand/config.py
py rebrand/script.py
py build2.py
py package.py
```

A zip archive and an installer will be created under `build`.

**NOTE**: If the build fails, you must take additional steps before re-running the build:

* If the build fails while downloading the Chromium source code (which is during `build.py`), it can be fixed by removing `build\download_cache` and re-running the build instructions.
* If the build fails at any other point during `build.py`, it can be fixed by removing everything under `build` other than `build\download_cache` and re-running the build instructions. This will clear out all the code used by the build, and any files generated by the build.

An efficient way to delete large amounts of files is using `Remove-Item PATH -Recurse -Force`. Be careful however, files deleted by that command will be permanently lost.

