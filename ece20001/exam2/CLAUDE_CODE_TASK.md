# Task: build the ECE 20001 Exam 2 lab (`ece20001/exam2/`)

Read the repo `README.md` first and follow its conventions: one static `index.html` per exam, shared `site.css`, MathJax 3 from cdnjs, Google Fonts, progress in localStorage, no build step. Use `ma261/exam1/index.html` as the structural model (Start here / Practice / Mock exam / Topics & formulas tabs). Then add a card for this exam to the root `index.html` under a new **ECE 20001 · Electrical Engineering Fundamentals I** course section, with `data-k="ece20001e2"`.

Everything you need is already in this folder. Do not fetch anything from Brightspace or Boilerexams.

## What is here

| Path | What it is | Published? |
| --- | --- | --- |
| `data/problems.json` | 323 problems with answers, topics, provenance and figure paths | yes (inline it into the page, or fetch it) |
| `figs/exams/` | One crop per past-exam question (some questions span two crops) | yes |
| `figs/cop/` | One crop per Collection of Problems item (stem + figure; options are text in the JSON) | yes |
| `figs/hw/` | Circuit images from the Brightspace HW 5–9 quizzes, named as referenced in `figs` | yes |
| `figs/boilerexams/` | Figures for the Boilerexams Spring 2023 Exam 2 items | yes |
| `_source/` | Original PDFs, saved HW attempt pages, raw Boilerexams data, my answer-reading notes | **no**: gitignored, reference only |

`_source/` must stay out of git. Confirm `ece20001/exam2/_source/` is in `.gitignore` before any commit.

## Exam facts (from Brightspace and Piazza)

- Thursday Nov 5, 2026, 8–9 PM. 60 minutes. One double-sided formula sheet, 1- or 2-line scientific calculator.
- Format on the last two years' exams: 10 questions × 10 pts. Questions 1–7 are multiple choice (often split into (a)/(b) parts, 6–8 options, last option "None of the above"). Questions 8–10 are work-out problems graded with partial credit.
- **Scope (instructor answer on Piazza):** maximum power transfer from Ch. 4, plus Ch. 5 through 8.10, which includes resonance and frequency response. No Ch. 9.

## `problems.json` schema

```json
{
  "topics": { "<key>": "<label>" },
  "problems": [{
    "id": "E2_S25-Q4",
    "set": "past_exam | homework | cop | boilerexams",
    "source": "Spring 2025 Exam 2 (Version A)",
    "number": 4, "part": null,
    "topics": ["first"],
    "scope": "core | ch4-review",
    "stem": "text with \\( LaTeX \\), or null when the stem lives only in the crop",
    "options": ["..."] | {"1": "..."} | null,
    "answer": {"kind": "mc | free", "index": [0, 8] | 4 | null, "letter": "C" | null, "text": "..."},
    "answer_basis": "where the answer came from",
    "figs": ["exams/e2_s25_q4.png", "exams/e2_s25_q4_p2.png"],
    "notes": "anything you must handle" | null
  }]
}
```

Index conventions: **homework** `answer.index` is 0-based into `options` (a list, sometimes 2 correct answers). **cop** `answer.index` is the 1-based option number used in the book, and `options` is an object keyed "1".."9". **boilerexams** `answer.index` is a 0-based list. **past_exam** has no `options` (they are in the crop) and carries `answer.letter` for multiple choice, plus `answer.text` with the value.

## Answer provenance: show it, never upgrade it

Every problem says where its answer came from. Surface this as a small label next to each solution, and keep the wording honest:

| `answer_basis` starts with | Count | Show as |
| --- | --- | --- |
| `official COP answer key` / `official TA solution` | 148 | Official key |
| `official key` | 57 | Official key |
| `official key, mapped to a letter by me…` (Fall 2025 Exam 3) | 13 | Official key (letter matched from the worked answer) |
| `graded attempt…` (HW 5–9) | 84 | Confirmed by a full-credit Brightspace attempt |
| `Boilerexams answer data` | 11 | Boilerexams (student site, not official) |
| `self-derived` (Fall 2024 P5, P7–P10) | 6 | Worked out, no official key |
| `no official answer found` (COP 6.40–6.43) | 4 | No answer yet. Solve each one yourself and label it "Worked out", or drop it |

Do not present a self-derived or Boilerexams answer as official.

## Things to fix while building

1. **Past-exam stems and options are only in the crops.** Transcribe each past-exam question into MathJax text (stem + options) by reading its crop, so the page can render options as buttons like the MA 261 lab. Keep the crop for the circuit figure; crop it down to just the figure if that is cleaner. Check every transcription against the crop.
2. **Spring 2024 crops (`exams/e2_s24_*_page.png`) are scanned solution pages with the worked solution written on them.** Do not show these as the question. Crop out only the printed circuit/graph, or redraw the circuit in SVG, and use the handwritten work only as the source for the worked solution.
3. **Fall 2025 Exam 2 and Exam 3 crops come from solution copies with the colored ink removed.** A few option strings the solver highlighted are damaged. For F25 Q7 the options are already in the JSON. For anything else unreadable, render `_source/pdf/ece2k1_E2_F25_sol.pdf` or `ece2k1_E3_F25_sol.pdf` at that page and read it there.
4. **COP free-response keys** with `⟨…⟩` in `answer.text` were pulled from a PDF where superscripts landed on separate lines. Rebuild those expressions from `_source/pdf/ece2k1_COP_key_ch5-8.pdf`.
5. **HW stems** were converted from Brightspace MathML to LaTeX automatically. Skim each for broken math and fix it against the matching image.
6. **COP crops include the printed stem text.** Either show the crop only, or show the JSON stem plus a figure-only crop. Don't show the stem twice.
7. **Flagged answers to double-check before publishing:**
   - `E3_F25-Q10` part (iii): the official key says L = ∞. The reasoning is unusual; keep the key's answer but say so.
   - `E3_F25-Q1.2`: the key ticks two options. F, 4 sin(ωt + 130°), is the correct one.
   - `E2_F24-Q8`: self-derived τ = 26 s depends on the dependent-source polarity in the crop; re-derive it.
   - `E2_S25-Q5` and `E2_F24-Q4.2`: the key left the bubble empty but the worked value matches one option. The letter is recorded.
   - `E2_F25-Q6`: the key notes that Version B asks for the other capacitor (60 A).
8. Fall 2025 Exam 3 is a later exam, but every problem on it is Ch. 7–8, so it is in scope. Label it "Fall 2025 Exam 3" so nobody thinks it is an Exam 2.

## Page structure

- **Start here:** one card per topic key in `topics` (skip `ch4` or fold it into max power). Per the README: an "On the exam" line built from the real past-exam questions for that topic, one warm-up per skill those questions need, and a last warm-up shaped like a real question with new numbers. Define every symbol where it first appears. Phasor sign conventions, conjugate matching (Z_L = Z_th*), RMS vs peak in P = |V|²/(2R) vs V_rms²/R, and capacitor-open/inductor-short at DC are the traps the keys show most.
- **Practice:** filters for Set (Past exams / Homework / Collection of Problems / Boilerexams), Source exam, Topic, and "Unanswered only"; a toggle to hide `ch4-review`. Multiple choice is clickable and shows right/wrong; free response gets a "Show answer" and a self-grade (Got it / Missed it). Every solution shows its provenance label.
- **Mock exam:** 60-minute timer, 7 multiple-choice + 3 work-out, drawn from past-exam and COP questions and covering the topic mix of the real exams (first-order transients, L/C basics, phasors/impedance, AC power, max power, one resonance item). Work-out problems are self-graded against the key.
- **Topics & formulas:** a formula sheet per topic, plus the common traps. This should look like something worth copying onto the allowed one-page formula sheet.

## Done when

- `ece20001/exam2/index.html` loads with no console errors, MathJax renders, all 323 problems appear under Practice, and every figure path resolves (write a quick check that every `figs` entry exists).
- The root `index.html` has the new course card.
- `_source/` is untracked (`git status` shows nothing under it).
- The README's exam list has an **ECE 20001 Exam 2** entry in the same style as the others, including the provenance breakdown above.
