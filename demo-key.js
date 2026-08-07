/* Shared demo key for the live interview on the "Try the skill" tab.
 *
 * EMPTY BY DEFAULT. Set it with:   python3 tools/set_demo_key.py sk-or-...
 * Clear it with:                   python3 tools/set_demo_key.py --clear
 *
 * READ THIS BEFORE SETTING A KEY
 * ------------------------------
 * This site is a static page on GitHub Pages. There is no server, so any key the
 * page can use is a key a visitor can read out of devtools. The base64 below is
 * OBFUSCATION, NOT SECURITY: it keeps the key out of the plain-text `sk-or-`
 * pattern that automated scrapers crawl public repos for, which is the threat
 * that actually empties keys in practice. It stops a bot. It does not stop a
 * person.
 *
 * The real control is the CREDIT LIMIT SET ON THE KEY ITSELF in the OpenRouter
 * dashboard (Keys -> credit limit). That is what bounds the damage. Set it low.
 *
 * Operationally: set the key shortly before the session, revoke it in OpenRouter
 * right after, and run --clear. Never reuse this key anywhere else.
 */
window.__AGC_DEMO = '';
