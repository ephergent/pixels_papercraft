# Pixel's Papercraft - Game Development TODO

https://phaser.io/download/release/v3.90.0

## Game Overview
**Title:** Pixel's Papercraft  
**Engine:** Phaser 3.90.0
**Genre:** Platformer  
**Art Style:** 8-bit pixel art drawn on graph paper aesthetic  
**Story:** Pixel Paradox gets trapped in the Paper Dimension and must escape back to Prime Material

## Art & Visual Design

### Core Aesthetic
- [x] Create graph paper background texture template
- [x] Design pixel art sprites with visible graph paper grid underneath
- [x] Implement "sketched" line effect for all sprites
- [ ] Add paper texture overlay to entire game
- [ ] Create color palette: pencil gray, eraser pink, pen blue, highlighter yellow

### Character Design
- [ ] Design Pixel Paradox sprite (electric blue hair, neon green highlights)
  - [ ] red jacket,black cargo pants, black chunky boots
- [ ] Create A1 holographic projection sprites (minimal, geometric)
  - [ ] Sleek black metallic espresso machine
- [ ] Design Clive stapler sprite with personality animations
  - [ ] Orange office stapler
- [ ] Add "sketched on paper" effect to all character animations
- [ ] 3d look in 2d drawing

### Environmental Art
- [ ] 3d look in 2d drawing
- [ ] Paper terrain tiles (folded, crumpled, torn edges)
- [ ] Background layers with graph paper grid
- [ ] Interactive paper elements (fans, origami, paper planes)
- [ ] Lighting effects that look like desk lamp shadows

## Core Mechanics

### Paper World Physics
- [ ] **Paper Folding**: Create foldable platforms that change level geometry
- [ ] **Origami Bridges**: Fold paper into temporary bridges/platforms
- [ ] **Paper Airplane Rides**: Throwable paper planes for transportation
- [ ] **Crumple Zones**: Areas that compress when stepped on
- [ ] **Paper Tear Shortcuts**: Rip through certain walls to create new paths

### Character Abilities
- [ ] Basic platformer movement (jump, run, slide)
- [ ] **Reality Glitch Vision**: See hidden fold lines and tear points
- [ ] **A1 Scanner**: Holographic hints for paper manipulation points
- [ ] **Clive Staple**: Create temporary platforms by stapling paper together

### Interactive Elements
- [ ] Foldable platforms (click/touch to fold)
- [ ] Paper airplane launchers
- [ ] Origami puzzle switches
- [ ] Crumpled paper bounce pads
- [ ] Tape dispensers (repair torn paths)

## Level Design

### Level 1: "The Notebook Prison"
- [ ] Tutorial level in a spiral notebook
- [ ] Teach basic movement and paper folding mechanics
- [ ] Introduce A1's scanning ability
- [ ] Boss: Giant pencil eraser trying to erase Pixel
- [ ] soundtrack/01_Notebook_Prison_Blues.mp3

### Level 2: "Office Supply Chaos"
- [ ] Navigate through scattered desk supplies
- [ ] Introduce Clive's stapling ability
- [ ] Paper airplane transportation sections
- [ ] Boss: Sentient hole puncher creating dangerous gaps
- [ ] soundtrack/02_Office_Supply_Shuffle.mp3

### Level 3: "The Origami Garden"
- [ ] Complex folding puzzles with paper flowers/trees
- [ ] Moving platforms made of folding paper
- [ ] Wind mechanics affecting paper planes
- [ ] Boss: Origami dragon that unfolds/refolds during fight
- [ ] soundtrack/03_Origami_Garden_Waltz_Repris.mp3

### Level 4: "Corporate Memo Maze"
- [ ] Navigate through Corporate Corp paperwork
- [ ] References to DRM (Department of Reality Maintenance)
- [ ] Shredded paper obstacles and reconstruction puzzles
- [ ] Boss: Filing cabinet monster spitting out forms
- [ ] soundtrack/04_Corporate_Memo_Madness.mp3

### Level 5: "The Reality Rip Repair"
- [ ] Final escape sequence
- [ ] All mechanics combined in challenging platforming
- [ ] Repair the dimensional tear using paper manipulation
- [ ] Boss: The Paper Dimension itself trying to keep Pixel trapped
- [ ] soundtrack/05_Reality_Rip_Escape.mp3

## Programming Tasks

### Core Systems
- [x] Set up Phaser 2D project structure
- [x] Implement player controller with tight platformer feel
- [ ] Create paper folding system
- [ ] Build interaction system for paper manipulation
- [ ] Program camera follow with screen shake for paper effects

### Paper Mechanics Implementation
- [ ] Folding platform system (rotate/scale animations)
- [ ] Paper airplane physics and trajectory
- [ ] Origami animation system (complex folding sequences)
- [ ] Crumple physics (temporary deformation)
- [ ] Tear effect system (reveal hidden paths)

### UI/UX
- [ ] Design paper-themed UI elements
- [ ] Create graph paper menu backgrounds
- [ ] Implement "handwritten" font for text
- [ ] Add paper sound effects (rustling, tearing, folding)
- [ ] Create pause menu that looks like a notebook page


## Audio Design

### Sound Effects
- [ ] Paper rustling and folding sounds
- [ ] Pencil scratching and eraser rubbing
- [ ] Stapler clicking and paper tearing
- [ ] Ambient office/desk sounds
- [ ] A1's electronic beeps (filtered through paper)

### Music
- [ ] Chiptune soundtrack with "muffled by paper" effect
- [ ] Each level gets unique paper-themed instruments
- [ ] Boss battle music with increased intensity
- [ ] Victory theme for returning to Prime Material
- [ ] Player start screen music soundtrack/00_Stuck_Between_Pages.mp3
- [ ] Player end screen music soundtrack/06_Origami_Garden_Waltz-BONUS-01.mp3

## Story Integration

### Narrative Elements
- [ ] Opening cutscene: Reality rip pulls Pixel into paper dimension
- [ ] A1 dialogue boxes explaining paper physics
- [ ] Clive's staple-pattern messages throughout levels
- [ ] Environmental storytelling through Corporate Corp paperwork
- [ ] Ending sequence: Pixel escapes back to Prime Material

### Character Development
- [ ] Pixel's frustrated corporate worker personality in dialogue
- [ ] A1's protective British formality in hints/tutorials
- [ ] Clive's noir detective observations about the paper world
- [ ] References to their Corporate Corp origins

## Polish & Testing

### Visual Polish
- [ ] Particle effects for paper interactions
- [ ] Screen transitions that look like page turns
- [ ] Consistent graph paper grid overlay
- [ ] Paper texture aging effects over time

### Playtesting
- [ ] Test paper mechanic intuition and clarity
- [ ] Balance difficulty curve across 5 levels
- [ ] Ensure all interactions feel responsive
- [ ] Test story comprehension for new players

### Optimization
- [ ] Optimize paper folding animations
- [ ] Compress textures while maintaining pixel art clarity
- [ ] Ensure smooth performance on target platforms

## Release Preparation

### Build & Export
- [ ] Set up build pipeline for target platforms
- [ ] Create game icon with paper/pixel aesthetic
- [ ] Write game description referencing Ephergent Universe
- [ ] Package final build with proper credits

### Documentation
- [ ] Create simple control guide
- [ ] Write brief story context for players
- [ ] Document paper mechanics for players
- [ ] Include Ephergent Zine references as easter eggs

---

**Target Timeline:** 8-12 weeks for solo developer  
**Core Focus:** Tight platformer controls + unique paper manipulation mechanics  
**Theme Integration:** Corporate burnout meets interdimensional absurdity through papercraft lens
