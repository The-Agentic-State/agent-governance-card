#!/usr/bin/env python3
"""Generate the worked-example page section for the AGC site from the v0.3 NYC fill."""
import json, html, re, sys, yaml, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent

schema = yaml.safe_load((REPO / "schema/agent-governance-card.schema.yaml").read_text())
fill = json.loads((REPO / "examples/nyc-mycity.card.json").read_text())
verdict = json.loads((REPO / "examples/nyc-mycity.verdict.json").read_text())

meta = {}
for key in ("core_fields", "extended_fields"):
    for f in schema.get(key, []):
        meta[f["id"]] = {**f, "part": "Core" if key == "core_fields" else "Extended"}

GROUPS = [
    ("identity",           "Identity"),
    ("what_it_does",       "What it does"),
    ("what_it_touches",    "What it touches"),
    ("autonomy_control",   "Autonomy &amp; control"),
    ("accountability",     "Accountability"),
    ("placement",          "Placement"),
    ("risk",               "Risk"),
    ("identity_delegation","Identity &amp; delegation"),
    ("automation_detail",  "Automation detail"),
    ("oversight",          "Oversight"),
    ("redress",            "Redress"),
    ("cost_lockin",        "Cost &amp; lock-in"),
]
SOURCES = {
    "S1": "Dossier S1 — System overview",
    "S2": "Dossier S2 — Register / official record (NYC Local Law 35)",
    "S3": "Dossier S3 — Technical architecture",
    "S4": "Dossier S4 — Governance, oversight &amp; procurement",
    "S5": "Dossier S5 — Impact &amp; incidents",
    "S6": "Dossier S6 — Sources",
}
STATUS_LABEL = {
    "answered": "answered",
    "unknown": "unknown",
    "not_in_place": "not in place",
    "not_applicable": "n/a",
}


def esc(s):
    return html.escape(str(s), quote=True)


def render_value(fid, f):
    st = f.get("status")
    if st == "answered":
        v = f.get("value")
        if isinstance(v, bool):
            out = "Yes" if v else "No"
        elif isinstance(v, list):
            out = ", ".join(str(x) for x in v)
        else:
            out = str(v)
        detail = f.get("detail")
        if detail and not isinstance(f.get("value"), str):
            out += " — " + detail
        return out
    if st == "not_in_place":
        return f.get("reason") or "Not in place."
    if st == "unknown":
        return f.get("reason") or f.get("detail") or "Not determinable from the public record."
    if st == "not_applicable":
        return f.get("reason") or "Not applicable."
    return "—"


rows_by_group = {g: [] for g, _ in GROUPS}
for fid, f in fill["fields"].items():
    m = meta.get(fid, {})
    g = m.get("group", "risk")
    ev = f.get("evidence") or {}
    st = f.get("status", "answered")
    diff = f.get("difficulty")

    why = []
    if ev.get("justification"):
        why.append('<p class="just">%s</p>' % esc(ev["justification"]))
    if ev.get("quote"):
        why.append('<blockquote>%s</blockquote>' % esc(ev["quote"]))
    if ev.get("source"):
        tag = SOURCES.get(ev["source"], esc(ev["source"]))
        basis = ev.get("basis")
        src = tag + (' · recorded as <b>%s</b>' % esc(basis) if basis else "")
        why.append('<p class="src">%s</p>' % src)
    if f.get("link"):
        why.append('<p class="src"><a href="%s">%s</a></p>' % (esc(f["link"]), esc(f["link"])))
    if f.get("note"):
        why.append('<p class="fnote"><b>Filler’s note.</b> %s</p>' % esc(f["note"]))

    why_html = ""
    if why:
        why_html = (
            '<details class="why"><summary>Why this answer</summary>%s</details>' % "".join(why)
        )

    chips = '<span class="st st-%s">%s</span>' % (st.replace("_", "-"), STATUS_LABEL.get(st, st))
    if diff:
        chips += '<span class="diff d%d" title="Difficulty for the person filling it in: %d of 5">%d/5</span>' % (
            diff, diff, diff)

    rows_by_group[g].append(
        '<div class="fld" id="f-%s">'
        '<div class="fhead"><code class="fid">%s</code>'
        '<div class="fq"><b>%s</b><span>%s</span></div>'
        '<div class="fchips">%s</div></div>'
        '<div class="fval">%s</div>%s</div>'
        % (fid, fid, esc(m.get("label", fid)), esc(m.get("question", "")),
           chips, esc(render_value(fid, f)), why_html)
    )

ledger = []
for g, title in GROUPS:
    if not rows_by_group.get(g):
        continue
    part = next((v["part"] for v in meta.values() if v.get("group") == g), "")
    ledger.append(
        '<section class="grp"><h3>%s <span class="gpart">%s</span></h3>%s</section>'
        % (title, part, "".join(rows_by_group[g]))
    )

inputs = verdict["inputs"]
inputs_html = "".join(
    '<tr><td><code>%s</code></td><td>%s</td><td>%s</td></tr>'
    % (k, esc(meta.get(k, {}).get("label", k)), esc(v))
    for k, v in inputs.items()
)

answered = sum(1 for f in fill["fields"].values() if f.get("status") == "answered")
gaps = sum(1 for f in fill["fields"].values() if f.get("status") in ("not_in_place", "unknown"))
diffs = [f["difficulty"] for f in fill["fields"].values() if f.get("difficulty")]
mean_diff = sum(diffs) / len(diffs)
mins = fill["meta"]["minutes_part1"] + fill["meta"]["minutes_part2"]

page = f"""
  <!-- ==================== PAGE 3 · WORKED EXAMPLE ==================== -->
  <!-- AGC:EXAMPLE:START — generated by scripts/gen_example.py from
       fills_v0_3/nyc-mycity__P1.json. Do not hand-edit; regenerate instead. -->
  <section class="page" id="page-example">
    <p class="facenote"><b>A worked example — NYC MyCity chatbot.</b> One real, public deployment,
    filled against card v0.3. This is what a completed card looks like, and what it surfaces.</p>

    <div class="provenance">
      <b>Read this first.</b> This card was filled by us from the <b>public record only</b> — the
      city's Local Law 35 register entries, the Comptroller's audit, the launch materials, and press
      reporting. <b>New York City did not participate and has not reviewed it.</b> A real card would
      be filled by the product team, who would know the answers we had to infer. We publish it
      because the case is fully documented in public, not because it is authoritative.
    </div>

    <div class="schemahead">
      <div class="stat"><b>{answered}<span class="of">/45</span></b><span>fields answered</span></div>
      <div class="stat"><b>{gaps}</b><span>unknown / not in place</span></div>
      <div class="stat"><b>{mins}′</b><span>to fill</span></div>
      <div class="stat"><b>{mean_diff:.1f}</b><span>mean difficulty / 5</span></div>
    </div>

    <div class="derivation">
      <div class="dlead">The Impact Level is computed, not chosen. Two independent legs; the higher wins.</div>
      <div class="legs">
        <div class="leg fired">
          <span class="lno">Leg 1 · OMB high-impact test</span>
          <b>{verdict['omb_high_impact_status'].replace('_',' ')}</b>
          <p>From C7 alone. The chatbot gave official-sounding guidance on housing, employment and
          consumer-protection rules that users could reasonably treat as a principal basis for
          decisions with legal effects.</p>
        </div>
        <div class="leg">
          <span class="lno">Leg 2 · Operational tier</span>
          <b>{verdict['operational_tier']}</b>
          <p>From C8/C10/C11/C11a/C12. It only informs — no tools, no actions, no personal data of
          record, no red-line trifecta. On its own this would have been a Low.</p>
        </div>
        <div class="leg result">
          <span class="lno">Final</span>
          <b class="lvl {verdict['impact_level']}">{verdict['impact_level']}</b>
          <p>The higher of the two. Part 2 (Extended) is required, plus the full OMB minimum-practice
          set for high-impact systems.</p>
        </div>
      </div>
      <table class="inputs">
        <thead><tr><th>Input</th><th>Field</th><th>Answer</th></tr></thead>
        <tbody>{inputs_html}</tbody>
      </table>
      <p class="honest"><b>Where this is contestable.</b> Our pre-registered expert label for this
      case was <b>Moderate</b>, not High — so the card over-called it, conservatively. C7 is also the
      single hardest field to answer in our testing (mean difficulty 3.5/5 across all fills). If you
      think the card gets this wrong, that is exactly the feedback we want: does citizen-facing legal
      <i>guidance</i> count as a &ldquo;principal basis&rdquo; for a decision?</p>
    </div>

    <h2 class="exh">What filling the card surfaced</h2>
    <p class="exsub">None of these are hidden facts — each traces to a public document. What the card
    does is make their absence <i>a required field</i> rather than something nobody thought to ask.
    Note that most of them are recorded as an ordinary <b>No</b>, not as a blank: only two fields
    here are &ldquo;not in place.&rdquo; A card that looks complete can still be telling you the
    safeguards are missing — which is why the level is computed from the answers rather than from
    how full the form looks.</p>
    <div class="findings">
      <div class="finding"><code>C7a</code><b>No determination record</b><p>Nobody wrote down who
        judged this system's risk, in what role, or on what basis. The most consequential judgement
        about the system was never recorded.</p></div>
      <div class="finding"><code>E13</code><b>No appeal route</b><p>A user harmed by relying on a
        wrong answer had nowhere to go. The only channel was a feedback form.</p></div>
      <div class="finding"><code>E9</code><b>No live monitoring</b><p>No documented monitoring of
        answer quality in production — the errors were found by journalists, not by the city.</p></div>
      <div class="finding"><code>C20</code><b>No assessable pre-deployment testing</b><p>OTI claimed
        red-teaming and 95–99% accuracy; the only artifact was a one-page summary the Comptroller's
        auditors found too thin to assess.</p></div>
      <div class="finding"><code>E18</code><b>No exit plan</b><p>No documented plan for shutdown,
        data portability, or continuity — for a system that ran for over two years.</p></div>
      <div class="finding"><code>C22 · E15</code><b>Disclaimers as the only safeguard</b><p>Fully
        automated legal guidance, protected by a disclaimer the bot itself contradicted when it told
        a user it could be relied on for professional advice.</p></div>
      <div class="finding"><code>E5</code><b>No named accountable human</b><p>Accountability sat at
        office level. No individual output could be traced to a responsible person.</p></div>
    </div>

    <h2 class="exh">The filled card</h2>
    <p class="exsub">All 45 fields as answered. Open <b>Why this answer</b> on any field to see the
    reasoning and the verbatim public source it rests on.</p>
    <div class="evnote"><b>Note the card has no evidence field.</b> The sources below are our
    working record, not part of the schema — the card asks <i>what</i> is true, not <i>how you know</i>.
    Whether it should ask for the basis of each answer is one of the questions we are putting to you.
    <br><br>The machine-readable card and its computed verdict are in the repo:
    <a href="examples/nyc-mycity.card.json"><code>examples/nyc-mycity.card.json</code></a> ·
    <a href="examples/nyc-mycity.verdict.json"><code>examples/nyc-mycity.verdict.json</code></a>.
    This page is generated from them by <code>tools/gen_example.py</code>.</div>

    {"".join(ledger)}

    <p class="adoption"><b>Retired.</b> The chatbot was shut down around February 2026, described by
    the incoming mayor as &ldquo;functionally unusable&rdquo; at a cost of roughly half a million
    dollars a year. C18 records that; the card is designed to outlive the system it describes.</p>
  </section>
  <!-- AGC:EXAMPLE:END -->
"""

out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("example_section.html")
out.write_text(page)
print("wrote", out, len(page), "bytes;", answered, "answered,", gaps, "gaps, mean diff", round(mean_diff, 2))
