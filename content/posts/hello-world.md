+++
title = "Hello World"
date = "2026-11-20T16:46:27-06:00"
#dateFormat = "2006-01-02" # This value can be configured for per-post date formatting
author = ""
authorTwitter = "" #do not include @
cover = ""
tags = ["", ""]
keywords = ["", ""]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

# Nature of the beast

Oof. Are we doing this again? Restarting my blog so I have somewhere to ramble. Using Hugo this time. The theme is the 'Black & White' variant of [terminal](https://themes.gohugo.io/themes/hugo-theme-terminal) with a modified color scheme to match [dracula](https://draculatheme.com). I love Dracula.

```bash

#!/usr/bin/env bash

set -x

CURL_BIN="$(which curl)"
[ -z "$CURL_BIN" ] && echo "cURL must be installed for use!" && exit 255

[ -z "$1" ] && echo "A HTTP Method is Required to call" && exit 1
METHOD="-X $1"

[ -z "$2" ] && echo "A URL is required to use" && exit 2
URL="$2"

if [ -z "$3" ]; then
  $CURL_BIN -qi -o - -H "Content-Type: application/json" -H "Accept: application/json" $JC_EXTRA_HEADERS $METHOD $URL
else
  DATA="-d @${3}"
  $CURL_BIN -qi -o - -H "Content-Type: application/json" -H "Accept: application/json" $JC_EXTRA_HEADERS $METHOD $DATA $URL
fi
```
