# Talenta Clockin/Out Automation

> Because devs are already stressed out with tickets, why not make their life easier with this automation?

## Installation

```sh
pip install -r requirements.txt
playwrignt install
```

## Usage
```sh
python main.py clockin your@email.com somePassword --coord="-6.023,102.323" --desc="Optional description"
python main.py clockout your@email.com somePassword --coord="-6.023,102.323" --desc="Optional description"
```
> Note: `--coord` while looks optional, it is required, I did this because this is the best way to escape negative sign.

## About
This is a simple automation script to clockin/out to Talenta. It uses Playwright to automate the browser. It is not a headless browser, so you can see the browser in action. It just uses Playwright to get the PHPSESSID because Talenta set the ttl of their cookies very short. The rest is handled by simple POST request to attendance endpoint. You can use your own scheduling solution to automate this script. Github actions might work, or just use cron on some vacant server.

This script is not intended to be used for malicious purposes. It is just a simple automation script to make life easier for devs.
 