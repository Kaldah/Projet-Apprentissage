# WorldEdit Helper

A quick reference guide for common WorldEdit commands and usage.

---

## Selection Tools

- `//wand`  
  Give yourself the wooden axe tool for selections.
- `//pos1` / `//pos2`  
  Manually set selection corners to your current location.
- `//sel <type>`  
  Change selection shape (`cuboid`, `ellipsoid`, `polygon`).

---

## Basic Editing

- `//set <block>`  
  Fill the entire selection with the specified block.
- `//replace <from> <to>`  
  Replace all blocks of type `<from>` in the selection with `<to>`.
- `//outline <block>`  
  Create a hollow shell of the selection using `<block>`.
- `//walls <block>`  
  Build walls around the perimeter of your selection.

---

## Clipboard Operations

- `//copy`  
  Copy the selected region into the clipboard.
- `//cut`  
  Copy and then clear the selected region.
- `//paste [–a]`  
  Paste the clipboard content at your current position. Use `-a` to paste without air.
- `//rotate <angle>`  
  Rotate the clipboard content by `<angle>` degrees.
- `//flip <direction>`  
  Flip the clipboard content (`north`, `east`, `south`, `west`, `up`, `down`).
- `//stack <times>`  
  Repeat the clipboard content `<times>` times in the direction you’re facing.
- `//move <distance>`  
  Move the clipboard content `<distance>` blocks in the direction you’re facing.

---

## Shapes & Structures

- `//sphere <block> <radius>`  
  Create a solid sphere.
- `//hsphere <block> <radius>`  
  Create a hollow sphere.
- `//cyl <block> <radius> <height>`  
  Create a solid cylinder.
- `//hcyl <block> <radius> <height>`  
  Create a hollow cylinder.
- `//pyramid <block> <radius> <height>`  
  Build a pyramid shape.
- `//forest <type> <count> [<radius>]`  
  Randomly place `<count>` trees of `<type>` within optional `<radius>`.

---

## Schematic Management

- `//schem save <name> [–a]`  
  Save clipboard to `/plugins/WorldEdit/schematics/<name>.schem`.
- `//schem load <name> [–a]`  
  Load schematic from file into clipboard.
- `//schem list`  
  List all saved schematics.

---

## Utilities & Analysis

- `//count <block>`  
  Count how many blocks of type `<block>` are in your selection.
- `//distr`  
  Display a distribution of block types in the selection.
- `//floor <block>`  
  Flatten the selection bottom to `<block>`.
- `//smooth`  
  Smooth the terrain in your selection.

---

## Undo / Redo

- `//undo`  
  Undo the last WorldEdit action.
- `//redo`  
  Redo an undone action.

---

## Tips & Best Practices

- **Run headless**:  
  ```bash
  cd minecraft-server\
  java -Xms1G -Xmx2G -jar .\paper-1.19.4-550.jar nogui
  ```
- **Detach process** on Linux:
  ```bash
  nohup java -Xms1G -Xmx2G -jar ./paper-1.19.4-550.jar nogui &
  ```
- Use a **permissions plugin** (e.g., LuckPerms) to control access to WorldEdit commands.
- Always **undo** (`//undo`) if a command doesn’t do what you expected.
- Combine `//stack`, `//rotate`, and `//move` for complex patterns.
