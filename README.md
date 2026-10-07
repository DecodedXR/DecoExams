# DecoExams

Exam prep labs for Purdue courses. `index.html` is the picker: choose a course, then an exam.

- **MA 261 Exam 1** (`ma261/exam1/`): a "Start here" refresher with warm-ups for each topic, all 72 questions from six past exams (Fall 2022 through Spring 2025) with worked solutions, a topic breakdown, a formula sheet, and a timed 12-question mock exam. Fall 2022 had no official key; those answers were worked out by hand. All others match the official keys.
- **ECE 20875 Exam 1** (`ece20875/exam1/`): refreshers, interactive figures and warm-ups for 10 topics; both official Fall 2026 mock exams (1a, 1b) with their keys, plus 12 extra problems built from lecture examples; code questions that run real Python in the browser (Pyodide, in a Web Worker with a 6 s limit); a printable notes sheet; and a timed 6-question mock you self-grade.

One folder per exam (`<course>/<exam>/index.html`); add a card for each new exam to the root `index.html`. Build each topic's Start here warm-ups backwards from the real exam questions: an "On the exam" line saying what gets asked, one warm-up per skill those questions need, and a last warm-up shaped like a real question with new numbers. Write for the reader who knows the least: define every term and symbol where it first appears, and walk through each step with real numbers instead of shorthand. Better they skip what they know than get lost in jargon. Static files, no build step. `site.css` is shared. Math uses MathJax 3 from cdnjs; fonts from Google Fonts. Progress is saved in each visitor's browser (localStorage).

`python ece20875/exam1/check.py` (needs node) runs every ECE code solution against its tests and checks the page scripts parse.

## Publish on GitHub Pages

In the repo's Settings > Pages, set Source to "Deploy from a branch", branch `main`, folder `/ (root)`.
