"""Check the ECE 20875 Exam 1 page: every code solution passes its own tests, every starter still has blanks,
and the page scripts parse. Needs node on PATH. Run: python ece20875/exam1/check.py"""
import json, math, os, re, subprocess, sys

html = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), encoding="utf-8").read()
scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
data = next(s for s in scripts if "const P=[" in s)
dump = data + "\nconsole.log(JSON.stringify({P, W: Object.entries(LEARN).flatMap(([k, L]) => L.warm)}));"
out = subprocess.run(["node", "-"], input=dump, capture_output=True, text=True, encoding="utf-8")
assert out.returncode == 0, out.stderr
D = json.loads(out.stdout)
for s in scripts:  # syntax check every inline script
    r = subprocess.run(["node", "--check", "-"], input=s, capture_output=True, text=True, encoding="utf-8")
    assert r.returncode == 0, r.stderr

def run(pre, src, tests):
    ns = {"__name__": "__main__"}
    exec(pre or "", ns)
    exec(src, ns)
    bad = []
    for call, exp in tests:
        g, x = eval(call, ns), eval(exp, ns)
        if not (g == x or (isinstance(g, (int, float)) and isinstance(x, (int, float)) and math.isclose(g, x, rel_tol=1e-9))):
            bad.append(f"{call} -> {g!r}, expected {x!r}")
    return bad

parts = [(f"{q['s']}{q['n']} part {p['p']}", p) for q in D["P"] for p in q["parts"]] + [(f"warm-up {w['step']}", w) for w in D["W"]]
fails, n = [], 0
for name, p in parts:
    if p["kind"] == "num":
        assert len(p["ans"]) == len(p.get("lab", p["ans"])), name
    if p["kind"] == "mc":
        assert "ABCDEFG".index(p["a"]) < len(p["o"]), name
    if p["kind"] != "code":
        continue
    n += 1
    assert "____" in p["start"], f"{name}: starter has no blanks"
    bad = run(p.get("pre"), p["sol"], p["tests"])
    bad += [f"solution doesn't use {w}" for w in p.get("need", []) if w not in p["sol"]]
    if bad:
        fails.append((name, bad))
for name, bad in fails:
    print("FAIL", name, *bad, sep="\n  ")
print(f"{n} code parts, {len(parts)} parts total, {len(fails)} failing")
sys.exit(1 if fails else 0)
