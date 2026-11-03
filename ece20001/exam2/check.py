"""Sanity check for the ECE 20001 Exam 2 lab: every figure exists, every MC answer points at a real option."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "data", "problems.json"), encoding="utf-8"))
P = d["problems"]
optimgs = lambda p: re.findall(r'src="figs/([^"]+)"', " ".join((p["opts"] or []) + [p["key"]]))
missing = [(p["id"], f) for p in P for f in p["figs"] + p.get("ctxfigs", []) + optimgs(p)
           if not os.path.isfile(os.path.join(HERE, "figs", f))]
html = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
wfig = re.findall(r'"(\w+?\d)"', re.search(r"const WFIG = \[(.*?)\]", html).group(1))
missing += [("warm-up", f"w_{w}.svg") for w in wfig if not os.path.isfile(os.path.join(HERE, "figs", f"w_{w}.svg"))]
assert not missing, f"missing figures: {missing}"
for p in P:
    assert p["key"] and p["prov"], p["id"]
    if p["answer"]["kind"] == "mc":
        n = len(p["opts"]) if p["opts"] else p["nopt"]
        assert n and p["ans"] and all(0 <= k < n for k in p["ans"]), p["id"]
    if p["set"] == "past_exam":
        assert p["sol"], p["id"]
assert len({p["id"] for p in P}) == len(P), "duplicate ids"
print(f"ok: {len(P)} problems, {sum(len(p['figs']) for p in P)} figure references, all present")
