# Logos Notebook

An offline Bible with a voice-enabled notebook. It is a Progressive Web App: one app that installs on
Windows, macOS, Linux, Android and iPhone/iPad, and keeps working with no internet connection.

## What is in this version

| Feature | Status |
| --- | --- |
| Bible reader: book/chapter picker, swipe or arrow keys, search, parallel view, compare, highlights, bookmarks | Done |
| KJV and ASV (public domain) | Built in, work offline immediately |
| The other 18 translations | Import slots (see "Translations"); the copyrighted text is not included |
| Audio Bible: play/pause, skip, speed, sleep timer, verse highlight, auto-continue, lock-screen controls | Done, uses on-device voices |
| Notebook: notebooks, tags, search, verse links, backlinks, Markdown export, backup/restore | Done |
| Dictation (speech to text) with spoken references ("John three sixteen" becomes John 3:16) and voice commands | Done, offline where the browser supports it |
| Read a note aloud (text to speech), including the text of verses it mentions | Done |
| Works offline (app, Bible text, notes, audio voices) | Done |
| Phone and desktop layouts | Done |

## Install and run

An installable web app must be served over **HTTPS** (or from `localhost`).

**On this computer (quickest):**

1. Install Python 3 if you do not have it.
2. In this folder run `python3 serve.py` (Windows: `py serve.py`).
3. Open http://localhost:8080 in Chrome or Edge and click **Install app** (top bar, or the install icon in the address bar).

**For phones and everyone else:** upload this whole folder to any static HTTPS host
(GitHub Pages, Netlify, Cloudflare Pages, your church or school web server). Nothing runs on a server;
it is only files. Then open the address on the phone:

- **Android (Chrome):** menu, Install app.
- **iPhone/iPad (Safari):** Share, Add to Home Screen.
- **Mac (Safari 17+):** File, Add to Dock. **Windows/Linux/Mac (Chrome or Edge):** the install icon in the address bar.

After the first visit the app and the Bible text are stored on the device. Turn off Wi-Fi to confirm: it still opens.
**More, This app** shows whether the offline files are ready.

## Translations and copyright

Only the King James Version and American Standard Version (1901) are public domain, so only they are included.
The other 18 requested versions (RSV, AMP, TLB, NASB, GNT, NIV, NKJV, NRSV, CEV, NLT, ESV, MSG, CJB, ISV,
NABRE, CEB, CSB, LSB) are copyrighted. This app does not contain or download their text, and I did not
build in any way to fetch it from unlicensed sources.

If you hold a license (or a publisher or Bible-licensing service supplies a module for your app),
open **More, Translations, Import** and choose the file. It is validated, stored on the device, and works
offline like the built-in versions. Imported text is kept on the device and never uploaded.
The rights holders shown in the app are from general knowledge; confirm them with each publisher.

### Module file format

A JSON file with the 66 books in order, each a list of chapters, each a list of verse strings:

```json
{
  "abbr": "ESV",
  "name": "English Standard Version",
  "copyright": "Scripture quotations are from the ESV Bible ... (the publisher's required notice)",
  "books": [
    [ ["Genesis 1:1 text", "Genesis 1:2 text"], ["Genesis 2:1 text"] ],
    "... 65 more books ..."
  ]
}
```

A bare array of the 66 books is also accepted. The `copyright` line is shown under each chapter and attached
to every verse copied or saved into a note. Publishers usually require this.

## Audio and dictation: what to expect

- **Audio Bible** uses the voices installed on the device, so it works offline in every translation.
  Quality depends on the device. On Android and iPhone, install a high-quality offline voice in system settings.
  Recorded human narration is a separate license and is not included.
- **Dictation** uses the browser's speech recognition. In Chrome and Edge the app checks whether an on-device
  language pack is available and offers to download it (More, Dictation). Without a pack, Chrome sends audio to
  an online speech service and dictation needs a connection. Turn on **On-device only** to forbid that.
  Safari on iPhone and Mac can dictate on-device when offline dictation is enabled in system settings.
  Firefox has no speech recognition; typing and everything else still work.
- **Dictation commands:** "new paragraph", "new line", "bullet", "insert verse Psalm 23 1", "stop dictation".
- Browsers may stop long dictation sessions; the app restarts listening automatically.

## Your data

Notes, highlights, bookmarks and settings are stored in the browser's local database on your device.
Nothing is sent anywhere. Use **More, Your data** to export a backup (JSON) or all notes as Markdown, and to ask
the browser to protect storage from automatic cleanup. Installing the app also makes cleanup much less likely.
There is no account and no cloud sync in this version.

## Known limits

- No cloud sync between devices yet. Use backup export/import to move notes.
- No recorded narration, cross-reference or footnote data (those come with licensed content).
- Browser-based dictation accuracy and offline support vary by browser and device.
- The Bible text and offline cache add roughly 10 MB to storage.

## Files

```
index.html, styles.css, manifest.webmanifest, sw.js   app shell and offline cache
js/app.js        interface and logic        js/books.js    reference parsing (typed and spoken)
js/speech.js     audio player, dictation    js/store.js    local database and settings
js/catalog.js    the 20 translations        data/          KJV and ASV text
icons/           app icons                  serve.py       local test server
```

To publish a new version, change `VERSION` in `sw.js` (for example `logos-v1.0.1`). Installed apps update on
their next online launch and show a "Reload" prompt.

Bible text for KJV and ASV was converted from the public-domain files at github.com/bibleapi/bibleapi-bibles-json.
