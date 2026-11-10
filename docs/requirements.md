# Requirements and deadlines

Sources: [Project topic selection](https://people.cs.umass.edu/~brun/class/2026Fall/CS520/project/ProjectTopicSelection.pdf),
[Project plan](https://people.cs.umass.edu/~brun/class/2026Fall/CS520/project/ProjectPlan.pdf),
[Mid-date report](https://people.cs.umass.edu/~brun/class/2026Fall/CS520/project/midProjectReport.pdf),
[MSR 2027 Mining Challenge](https://2027.msrconf.org/track/msr-2027-mining-challenge).

## CS 520 deadlines

| Milestone | Due | Status |
|---|---|---|
| Team + project selected (Canvas group name ends in `MSR`) | Thu Sep 24, 2026, 9:00 AM EDT | |
| Project plan (1-page PDF on Canvas) | Thu Oct 8, 2026, 9:00 AM EDT | |
| Mid-point check-in: 7-min talk at a TA group meeting (book a slot with our TA) | **Thu Nov 12 – Tue Nov 17, 2026**; be ready by Thu Nov 12, 9:00 AM EST | |
| Final project | **Tue Dec 15, 2026, 11:55 PM EST** | |

Teams have 3–4 students and submit one project. Canvas: https://umamherst.instructure.com/courses/41134

## Project plan contents (1 page)

1. Datasets and code repositories used. The challenge offers GitSkills and SpecMine, and we can use either or both.
2. Research questions.
3. Experiments to answer each RQ.
4. Anticipated risks and mitigations.

## Mid-point check-in contents (7 min, strict, bring slides)

All team members attend. By now we should have the data and code and have started running experiments.
If the plan changed since Oct 8, say what changed and why. Then a few minutes of TA questions.

1. **Problem** (1 slide, ≤2 min): dataset (GitSkills) and RQs, with a one-sentence summary on the slide.
2. **Design** (≤2 min): data extraction and analysis pipeline; what we collect, how we process it, what we measure.
3. **Evaluation** (≤2 min): how we know we succeeded, sanity checks, statistical tests. Show preliminary results.
4. **Plan** (quick): timeline, each member's responsibilities, which planned risks came up and how we're handling them.

## MSR 2027 Mining Challenge (optional external submission)

| Milestone | Due (AoE) |
|---|---|
| Abstract | Dec 18, 2026 |
| Paper | Dec 23, 2026 |
| Notification | Jan 19, 2027 |
| Camera-ready | Jan 26, 2027 |

- Submit via HotCRP: https://msr2027-challenge.hotcrp.com/
- 4 pages plus 1 page of references, strictly. IEEE conference template: `\documentclass[10pt,conference]{IEEEtran}`.
  Do not change spacing or font size.
- Double-anonymous: no author names, and cite our own prior work in the third person.
- Needs an **ethics section before the conclusion**.
- State the dataset snapshot or version used.

## Datasets

- **GitSkills**: agent `SKILL.md` files on GitHub. See the [README](../README.md#dataset).
- **SpecMine**: spec-driven development artifacts.
  Zenodo https://doi.org/10.5281/zenodo.22102779, HF https://huggingface.co/datasets/ShyAgarwal/specmine,
  GitHub http://github.com/shyamagarwal13/specmine-official
