#!/usr/bin/env python3
"""Set or clear the shared demo key used by the site's live interview.

    python3 tools/set_demo_key.py sk-or-v1-...   # set
    python3 tools/set_demo_key.py --clear        # clear
    python3 tools/set_demo_key.py --show         # report whether one is set

The key is base64-encoded into demo-key.js. That is obfuscation, not security:
the site is static, so anyone can decode it from the browser. It exists to keep
the key out of the plain `sk-or-` pattern that bots scrape public repos for.
The credit limit set on the key in OpenRouter is the actual control.
"""
import base64
import pathlib
import re
import sys

KEYFILE = pathlib.Path(__file__).resolve().parent.parent / "demo-key.js"
ASSIGN = re.compile(r"^window\.__AGC_DEMO = '.*';$", re.M)


def write(encoded: str) -> None:
    text = KEYFILE.read_text()
    new, n = ASSIGN.subn("window.__AGC_DEMO = '%s';" % encoded, text)
    if n != 1:
        sys.exit("could not find the assignment line in demo-key.js — fix it by hand")
    KEYFILE.write_text(new)


def current() -> str:
    m = re.search(r"window\.__AGC_DEMO = '(.*)';", KEYFILE.read_text())
    return m.group(1) if m else ""


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    arg = sys.argv[1]

    if arg == "--show":
        enc = current()
        if not enc:
            print("no demo key set")
            return 0
        try:
            dec = base64.b64decode(enc).decode()
        except Exception:
            print("a value is set, but it does not decode — check demo-key.js")
            return 1
        print("demo key set: %s…%s (%d chars)" % (dec[:8], dec[-4:], len(dec)))
        return 0

    if arg == "--clear":
        write("")
        print("cleared. Now revoke the key in the OpenRouter dashboard too — "
              "clearing the file does not disable the key.")
        return 0

    key = arg.strip()
    if not key.startswith("sk-or-"):
        sys.exit("that does not look like an OpenRouter key (expected sk-or-…)")
    write(base64.b64encode(key.encode()).decode())
    print("set: %s…%s" % (key[:8], key[-4:]))
    print("\nBefore you push, confirm in OpenRouter that this key has a credit limit.")
    print("The page is public — the limit is the only thing bounding spend.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
