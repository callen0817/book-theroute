# The Route
**Author:** Black P. Pull  
**Genre:** Literary Fiction / Allegorical Novel / Philosophical Bildungsroman  
**Repository:** [https://github.com/callen0817/book-theroute](https://github.com/callen0817/book-theroute)

---

## About the Novel

*The Route* is an allegorical epic following the lifelong journey of **Cairo** and his companion **Ash** as they navigate a mysterious path that serves as both a physical trail and an existential teacher. 

The title holds a deliberate double entendre and homonym:
* **The Route:** The physical, winding overland trail representing wandering, survival, personal trials, and the restless human hunger to seek the horizon.
* **The Root:** The grounded anchor representing domestic cultivation, family, generational memory, and the soil where we bury our dead and raise our children.

Structured in four elemental movements:
1. **Part 1 — Embers (Chapters 1–4):** The spark of life, childhood curiosity, and the unspoken bond of brotherhood.
2. **Part 2 — Current (Chapters 5–26):** The flow of youth, learning navigation from Keepers (whose braided hair charts elevation and topography) vs. Archivists (who preserve textual memory), and evading the predatory Valley Feeders.
3. **Part 3 — Ashes & Rain (Chapters 27–36):** Adulthood, domestic roots in the Promised Land, the gentle grace and tragic loss of Amara, generational renewal, and the painful necessity of parting.
4. **Part 4 — Wind (Chapter 37):** Elder silver wisdom, circular return, and the eternal continuity of the road.

---

## Repository Structure

```
├── chapters/                       # Individual text files for Chapters 1-37 & Front Matter
├── audiobook/                      # Master generated audiobook files (Chapter 1 sample)
├── docs/
│   └── antigravity-history/        # Complete Antigravity conversation transcript & plans
│       ├── README.md               # Index of exported Antigravity docs
│       ├── architectural_decisions_and_plans.md
│       ├── conversation_transcript.md
│       ├── cliffs_notes_the_route_comprehensive.md
│       └── the_route_marketing_and_audiobook_blueprint.md
├── The Route.txt                   # Complete compiled manuscript
├── The_Route_Final.docx            # Formatted Word manuscript
├── Cliffs_Notes_The_Route.docx     # Complete classroom study guide (Word edition)
├── Cliffs_Notes_The_Route.md       # Complete classroom study guide (Markdown edition)
├── Character Name Guide.docx       # Character etymology and symbolic profiles
├── Marketing_and_Audiobook_Blueprint.md # Marketing kit, Instagram copy & audio blueprint
├── The_Route_Final_Shells_Beads_Cover.jpg # Official Leonardo da Vinci cover art
├── The_Route_Final_Shells_Beads_IG_Post.jpg # 1:1 Social media graphic
├── The_Route_Final_Shells_Beads_IG_Story.jpg # 9:16 Social media vertical story
├── generate_audiobook.py           # GPU-accelerated local voice-cloning synthesis engine
├── clean_audio.py                  # Audio mastering, de-essing, and anti-echo DSP tool
├── run_audiobook_generator.bat     # Windows production launcher menu
├── setup_environment.bat          # Automated local Python & PyTorch CUDA setup script
├── requirements.txt               # Python package dependencies
├── EXCLUSIONS.md                   # Explicit guide to Git exclusions & local rebuild
└── .gitignore                     # Git exclusion rules
```

---

## Local Audiobook Production Suite

This repository includes a 100% free, local AI voice-cloning audiobook production engine powered by **F5-TTS** and accelerated by NVIDIA GPUs.

### Quick Start
1. **Setup Environment:** Run `setup_environment.bat` to configure Python, PyTorch with CUDA 12.4, and audio DSP dependencies.
2. **Generate Audio:** Run `run_audiobook_generator.bat` to launch the interactive synthesis menu.
3. **Exclusions & Rebuild Guide:** Consult [EXCLUSIONS.md](EXCLUSIONS.md) for details on excluded machine learning models, virtual environments, and local rebuild instructions.

---

## Antigravity Collaborative History

The full collaborative development history, prompts, architectural decisions, and diagnostic transcripts conducted in Google Antigravity are preserved in [`docs/antigravity-history/`](docs/antigravity-history/).
