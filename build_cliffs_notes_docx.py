import os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUTPUT_FILE = r"c:\Users\callen\OneDrive - Reisource\Desktop\The Route\Cliffs_Notes_The_Route.docx"

def add_heading(doc, text, level):
    h = doc.add_heading(text, level=level)
    if level == 1:
        h.alignment = WD_ALIGN_PARAGRAPH.CENTER

def main():
    doc = Document()

    # Set page size (4.25 x 6.87) and margins (1 inch)
    for section in doc.sections:
        section.page_width = Inches(4.25)
        section.page_height = Inches(6.87)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Blank first page for cover art
    if os.path.exists("cover_art.png"):
        doc.add_picture("cover_art.png", width=Inches(3.5))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_page_break()

    # Title
    doc.add_paragraph() # Spacing
    title = doc.add_paragraph("🥷 Notes (Ninja Notes): The Route")
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title.runs[0]
    title_run.font.size = Pt(20)
    title_run.bold = True
    
    author = doc.add_paragraph("Author: Black P. Pull")
    author.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    # Overall Summary
    add_heading(doc, "Overall Summary", 1)
    summary_text = (
        "The Route follows the lifelong journey of the narrator, Cairo, and his close friend Ash "
        "as they navigate a mysterious \"path\" that serves as both a physical trail and a profound teacher. "
        "Starting as young boys learning to survive and discern the intentions of those they meet, "
        "they encounter different philosophies of knowledge and memory. These are represented by "
        "Keepers (who braid maps and history into their hair) and Archivists (who preserve history on paper). "
        "They also face the dark side of survival through the \"Valley Feeders,\" a corrupted society that uses "
        "deception and false promises to lead travelers off cliffs to scavenge their resources.\n\n"
        "Along the way, Cairo and Ash rescue and befriend Lulu, a Keeper who joins them before temporarily "
        "parting ways to travel with her own people. After an accidental return to Cairo's childhood home, "
        "the duo decides it is time to stop wandering and plant their own roots. They soon reunite with Lulu "
        "and establish a permanent settlement in a fertile valley, which they call the Promised Land. "
        "There, they raise families and pass their hard-earned lessons to the next generation.\n\n"
        "Tragedy strikes when Ash's wife falls ill and dies from a delayed sickness, a consequence of her "
        "unknowing childhood consumption of human flesh in a distant, desperate feeder region. As their children "
        "eventually come of age and leave to walk the path themselves, the pull of the road calls the aging "
        "friends back. Ash leaves the valley first. Years later, Cairo also feels the call, leaving Lulu to "
        "tend the valley she considers her true home. In the poignant final chapter, the two old friends reunite "
        "on the road, continuing their endless journey of observation, connection, and discovery."
    )
    doc.add_paragraph(summary_text)

    # Character Guide
    doc.add_page_break()
    add_heading(doc, "Character Guide", 1)
    
    add_heading(doc, "Main Characters", 2)
    p = doc.add_paragraph()
    p.add_run("Cairo\n").bold = True
    p.add_run("Origin/Literal Meaning: Arabic (Al-Qāhirah) — The Victorious / The Conqueror.\nStory Significance: Symbolizes curiosity, exploration, and the thirst for knowledge. Conquers the unknown not with force, but with observation, patience, and compassion. Evolves from a young seeker into a keeper of memory, walking the world and leaving a legacy.\nThematic Role: Embers of curiosity; connection to wind and movement through life’s cycles.")
    
    p = doc.add_paragraph()
    p.add_run("Ash\n").bold = True
    p.add_run("Origin/Literal Meaning: Inspired by Asha (Sanskrit for \"hope/life\"); also Old English \"ash tree\" (strength/support) or \"ash from fire\" (memory/survival/renewal).\nStory Significance: Represents resilience, memory, and moral grounding. Experiences grief, loss, and the passage of time, but continues walking. Acts as a living link between generations, guiding and observing younger travelers.\nThematic Role: Current and Ashes & Rain; memory and endurance; moral compass alongside curiosity.")
    
    p = doc.add_paragraph()
    p.add_run("Lulu\n").bold = True
    p.add_run("Origin/Literal Meaning: Short for Tululuh — “Pearl of patience” / “Hidden gem nurtured over time”.\nStory Significance: Embodies nurture, patience, stability, and home. Remains at the settlement, content in routine and the world she cultivates. Offers emotional anchor and understanding, allowing Cairo and Ash to pursue their paths without conflict.\nThematic Role: Ashes & Rain; embodiment of roots and calm; contrast to movement and exploration.")
    
    add_heading(doc, "Supporting Characters", 2)
    
    p = doc.add_paragraph()
    p.add_run("The Archivist\n").bold = True
    p.add_run("Origin/Literal Meaning: Human embodiment of record-keeping and observation. Archives = memory, record, continuity.\nStory Significance: Observes Cairo and Ash without directly intervening. Ensures that stories, experiences, and knowledge are passed along accurately. Serves as a meta-guide for morality and understanding, correcting miscommunications.\nThematic Role: Memory, continuity, ethical guidance; acts as a bridge between past and future generations.")
    
    p = doc.add_paragraph()
    p.add_run("The Keepers\n").bold = True
    p.add_run("Origin/Literal Meaning: Guardians of the land, moral and environmental balance. Keeper = protector, observer, steward.\nStory Significance: Enforce balance without oppression. Challenge Cairo and Ash to learn observation, patience, and moral discernment. Act as cautionary examples of what happens when rules are broken or misunderstood.\nThematic Role: Embodiment of responsibility, consequence, and societal ethics.")
    
    p = doc.add_paragraph()
    p.add_run("The Valley Feeders\n").bold = True
    p.add_run("Origin/Literal Meaning: Corrupt system that evolved from population control into unethical exploitation. \"Feeders\" = providing sustenance or taking life.\nStory Significance: Deceptive leaders lure people to death under the guise of providing. Demonstrate the dangers of blind obedience and ethical compromise. Their eventual reform and atonement show that wrongdoing arises from flawed systems, not inherently monstrous individuals.\nThematic Role: Ethical ambiguity, societal reflection, the cost of ignorance, accountability.")
    
    p = doc.add_paragraph()
    p.add_run("Ash’s Wife\n").bold = True
    p.add_run("Origin/Literal Meaning: From the Valley Feeders region. Represents the personal cost of systemic corruption.\nStory Significance: Her marriage and family with Ash humanize the impact of the Valley Feeders’ actions. Her death triggers Ash’s return to walking.\nThematic Role: Catalyst for adult grief, reflection, and continuation of the journey.")
    
    p = doc.add_paragraph()
    p.add_run("Cairo’s Parents\n").bold = True
    p.add_run("Origin/Literal Meaning: Local origin, part of Cairo’s initial home environment. Represent roots, home, and the cyclical nature of life.\nStory Significance: Their accidental reunion emphasizes life cycles, reflection, and the importance of leaving a legacy. Reactions of fear and wonder show human discomfort with the unfamiliar and the unknown.\nThematic Role: Home, roots, cycles, and intergenerational legacy.")
    
    p = doc.add_paragraph()
    p.add_run("Lulu’s / Ash’s Children\n").bold = True
    p.add_run("Origin/Literal Meaning: The next generation of walkers. Embody continuity, inheritance of knowledge.\nStory Significance: Demonstrate that lessons passed down are absorbed differently by each generation. Their walking represents new cycles of discovery and growth.\nThematic Role: Legacy, renewal, and the enduring rhythm of life.")
    
    p = doc.add_paragraph()
    p.add_run("Minor Mentors, Locals, and Travelers\n").bold = True
    p.add_run("Origin/Literal Meaning: People encountered along the road. Each is a facet of the world’s lessons.\nStory Significance: Offer moments of reflection, challenge, or friendship. Reinforce the idea that not all lessons are comfortable, and not all guidance is trustworthy.\nThematic Role: Mirrors, ethical dilemmas, and learning opportunities.")

    # Chapter-by-Chapter
    doc.add_page_break()
    add_heading(doc, "Chapter-by-Chapter Summary", 1)

    chapters = [
        ("Chapter 1 – Embers: The First Steps", "Cairo, as a young boy, begins his solitary walk on the path, recalling the warmth and teachings of his parents. He learns to observe his surroundings, understanding that the path is alive and full of both danger and instruction."),
        ("Chapter 2 – Embers: First Encounters", "Cairo continues his journey, observing traces of others. He encounters a boy around his age (Ash) at a ravine. Without words, Ash offers a gesture of connection, giving Cairo a small wrapped object."),
        ("Chapter 3 – Embers: Learning the Way", "Cairo learns to read the signs of the path: stone markers, old fires, and the presence of adult travelers. He reunites briefly with Ash by a stream, where they communicate through gestures and shared observation."),
        ("Chapter 4 – Embers: Crossing Shadows", "Cairo navigates the physical challenges of the path. He encounters Ash again at a campfire. They sit together in silence, establishing a deeper, unspoken trust and a mutual understanding of how to learn from observation."),
        ("Chapter 5 – Current: Moving Together", "Cairo and Ash begin traveling as a pair. They learn to move in sync, crossing streams and rough terrain. They discover signs of Keepers (twisted hair left as markers) and realize the path is filled with hidden knowledge."),
        ("Chapter 6 – Current: Shadows in the Flow", "The duo encounters another young traveler who tests their observation. Through a harrowing ridge crossing, they learn that trust must be earned through action and alignment with the path, not just words."),
        ("Chapter 7 – Current: Knots in the Flow", "Cairo and Ash meet an adult female Keeper. She teaches them the basics of her silent language: patterns and maps braided into hair and etched in the dirt, emphasizing observation and patience."),
        ("Chapter 8 – Current: Ink and Memory", "The boys encounter an Archivist who records the path using ink and paper. They learn that while Keepers carry living memory, Archivists preserve permanent records, offering a different form of knowledge."),
        ("Chapter 9 – Current: Shadows and Intent", "The pair runs into a group of erratic travelers whose intentions feel deceptive. Trusting his instincts, Cairo leads Ash away from a dangerous cliff-edge path suggested by the group, learning to discern masked intent."),
        ("Chapter 10 – Current: Knots and Paths", "They observe a Keeper braiding a young boy's hair, a living map of paths taken and avoided. The lesson reinforces that the path is shaped by those who walk it and that not all knots speak the truth."),
        ("Chapter 11 – Current: Lines of Truth", "Cairo and Ash witness a silent intersection of methods as a Keeper and an Archivist work near each other. They realize that different perspectives and methods can capture the same truths about the path."),
        ("Chapter 12 – Current: Shadows Among Knots", "While observing a Keeper, a dangerous stranger approaches. The boys learn that deception can easily hide behind courtesy and that not all guides can be trusted. The shadow of the Valley Feeders begins to loom."),
        ("Chapter 13 – Current: The Edge of the Path", "A charismatic stranger tries to lure them down a steep, treacherous trail. Guided by their instincts and past lessons, Cairo and Ash avoid the trap, recognizing the subtle menace of the Valley Feeders."),
        ("Chapter 14 – Current: False Promises", "They encounter a group recruiting workers for a \"farm.\" Sensing the imbalance and the scent of iron, Cairo and Ash realize it is a trap meant to lead travelers to their deaths."),
        ("Chapter 15 – Current: The Hollowed Farm", "Investigating the farm structure, they confirm it is a gruesome trap set by the Valley Feeders. They subtly help a wide-eyed child avoid the workers' attention before slipping away safely."),
        ("Chapter 16 – Current: Echoes of the Valley", "Bearing the heavy knowledge of the hollowed farm, they encounter Keepers who acknowledge their shared understanding. The path requires constant vigilance against the systemic deception of the Feeders."),
        ("Chapter 17 – Current: The Edge of Trust", "Another encounter with seemingly friendly guides tests their resolve. They veer away from the edge, relying purely on their own observation, solidifying their trust in each other over strangers."),
        ("Chapter 18 – Current: The Keeper and the Knots", "They find a Keeper tending a fire. Cairo feels a deep sense of familiarity with her language of gestures. She shows them how knots serve as warnings and guides against the false paths of the Feeders."),
        ("Chapter 19 – Current: Learning the Knots", "Spending the day with the Keeper, Cairo and Ash learn to mimic and understand the basic language of her knots. They realize the twists in hair are a living history of survival."),
        ("Chapter 20 – Current: The Archivist", "They meet another Archivist deep in their work. The boys learn to appreciate the permanence and layered complexity of written records, contrasting with the fluid, living memory of the Keepers."),
        ("Chapter 21 – Current: False Paths", "An older traveler with unfamiliar knots tries to guide them down a dangerous trail. Relying on the true patterns they've learned, they ignore the false guide, realizing deception is an ever-present part of the journey."),
        ("Chapter 22 – Current: The Valley Feeders", "Descending into a dark valley, they spot Valley Feeders actively directing people toward cliff edges. They cautiously navigate the shadows and free a bound female Keeper named Lulu just before she is sacrificed."),
        ("Chapter 23 – Current: Shadows and Lessons", "Traveling with Lulu, they join a fire with other Keepers. Lulu acts as a guide, helping them distinguish between genuine travelers and deceptive ones, solidifying their understanding of discernment."),
        ("Chapter 24 – Current: The Archivist", "The trio visits an elaborate structure maintained by an Archivist. They learn that even preserved stories can be incomplete or manipulated, emphasizing that truth requires personal experience."),
        ("Chapter 25 – Current: Choices in the Shadows", "A seemingly weary traveler tries to redirect them. Using the combined instincts of their varied experiences, Cairo prevents a misstep, proving their mastery over spotting false guidance."),
        ("Chapter 26 – Current: Shadows of Leadership", "They reach a plain controlled by Valley Feeders where villagers obey out of fear. Appalled by the corruption of survival into cruelty, they leave the plain. Lulu safely departs with a group of Keepers, her path diverging from theirs."),
        ("Chapter 27 – The Accidental Return", "Cairo and Ash accidentally loop back to Cairo's childhood valley. Cairo reunites with his aging parents, sharing his stories. Through this stillness, they both realize it is time to stop wandering and plant roots."),
        ("Chapter 28 – Leaving the Valley", "Leaving Cairo's parents behind, the duo sets out to find their own place to settle. The valley has taught them the value of home, but they know they must forge their own future."),
        ("Chapter 29 – The Reunion", "While walking, they cross paths with Lulu once again. The serendipitous reunion confirms the cyclical nature of the road and brings the three companions back together for the next phase of life."),
        ("Chapter 30 – The Promised Land", "They discover a beautiful, unclaimed valley and decide to settle there, calling it the Promised Land. Ash marries, Cairo and Lulu marry, and they begin cultivating the land, turning their life of motion into one of growth."),
        ("Chapter 31 – New Steps", "Generations begin. Cairo, Lulu, and Ash raise children, teaching them the lessons of observation, patience, and the path, letting them explore the valley while knowing the road will eventually call them."),
        ("Chapter 32 – A Shadow from the Past", "Ash's wife grows inexplicably ill and dies. It is revealed she unknowingly consumed human flesh as a child in a feeder region, carrying a delayed, fatal sickness. Ash grieves but stays to raise his children."),
        ("Chapter 33 – When Children Walk", "Ash's children come of age and feel the pull of the road. Ash supports their decision to leave, knowing the world will teach them what the valley cannot. With his children gone, his final tether to the valley is released."),
        ("Chapter 34 – The Road Calls Again", "Feeling the familiar call of the path, Ash decides to leave the settlement. He bids a quiet farewell to Cairo and Lulu, returning to the endless road he has always belonged to."),
        ("Chapter 35 – Roots and Horizons", "Cairo and Lulu age gracefully in the thriving valley. Lulu expresses her deep connection to the land, her \"road\" being the cultivation of the valley. Cairo, however, continues to feel the pull of the distant horizon."),
        ("Chapter 36 – The Hardest Step", "Acknowledging that their true paths now differ, Cairo decides to leave the valley. Lulu supports his choice, staying behind to tend to the settlement. They part with deep mutual respect and love."),
        ("Chapter 37 – Keepers of the Road", "Years later, as an old man walking the path, Cairo unexpectedly encounters Ash. The two old friends reunite seamlessly, falling back into their shared rhythm as they continue their endless journey along the road.")
    ]

    for title_text, desc_text in chapters:
        p = doc.add_paragraph()
        run = p.add_run(title_text)
        run.bold = True
        doc.add_paragraph(desc_text)

    # Save
    doc.save(OUTPUT_FILE)
    print(f"Generated formatted DOCX at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
