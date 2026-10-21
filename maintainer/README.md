# English edition maintenance

Source curriculum: Russian agent-harness-workshop, commit 795fdd892fb8c1719d1f1fb28416fd69d31be01a. This edition adapts the explanations to natural English while preserving the curriculum, target functions and runtime contracts. Installation references were checked on 2026-10-22.

Run `python tools/check_course.py` and `python tools/check_english.py`. Rebuild downloads from the corresponding exercises after an edit. Current functions must remain unfinished, with preceding components prepared. Main-course checks do not contact a model or load GGUF weights.

English diagrams are generated with Pillow: `python tools/draw_course_flows.py --vault .`. Inspect keyframes, complete GIF decoding and static alternatives as well as checking dimensions. No independent live-model generation or OpenCode experiment is claimed merely because documentation checks pass.
