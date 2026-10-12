# Setup Guide

## 1. Install GB Studio

Download the latest release from https://www.gbstudio.dev/ and install it for your OS.

Optional: Build the CLI from source if you want command-line ROM exports:

```bash
git clone https://github.com/chrismaltby/gb-studio.git
cd gb-studio
# Follow their README for Node version and yarn install
npm run make:cli
```

## 2. Install Chromatic CLI

```bash
npm install --global @modretro/chromatic-cli
chromatic-cli --version
chromatic-cli install-drivers   # run once; may need admin/sudo on some platforms
```

## 3. Activate Developer Mode (if you have a code)

DevDay Chromatic units came with an activation code. Regular units may not.

```bash
chromatic-cli activate YOUR_ACTIVATION_CODE
```

## 4. Verify Connection

```bash
chromatic-cli list-devices
chromatic-cli detect-cart
```

## Alternative Flashing (no official activation)

- **ChroMagic**: https://chromagic.org/ — custom firmware + desktop app that can flash homebrew to Chromatic carts.
- Community unlockers exist for the official MRUpdater; use at your own risk.

## Recommended Emulators for Testing

- BGB (excellent debugger)
- mGBA
- SameBoy
- GB Studio's built-in Play window / web export
