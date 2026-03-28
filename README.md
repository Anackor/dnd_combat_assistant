# dnd_combat_assistant
This is a local desktop application built with Python for helping Game Masters run Dungeons &amp; Dragons 4e encounters. The application allows users to configure and visualize party members or enemies with attributes like health points, defenses, and active effects.

## New Features 🎉
- **Character Folders**: Organize your characters into folders for easy access
- **Multiple Combat Characters**: Select and manage multiple characters simultaneously in combat overlay
- **Duplicate Characters**: Create copies of existing characters quickly to represent multiple instances of the same enemy type

## Project Structure
    ```sh
    dnd_assistant/
    ├── app/
    │   ├── config/            # Configuration loading and saving
    │   ├── core/              # Business logic / use cases
    │   ├── domain/            # Domain entities (Character, Effect, Defense...)
    │   ├── infrastructure/
    │   │   └── db/            # SQLite access and models
    │   └── ui/                # GUI windows and components (PySide6 / Qt)
    ├── tests/                 # Unit and integration tests
    ├── scripts/               # Scripts (optional)
    ├── main.py                # Entry point for launching the app
    ├── requirements.txt       # Python dependencies
    └── README.md
    ```

## Installer
    ```sh
    pip install -r requirements.txt
    ```
    ```sh
    .venv\Scripts\Activate.ps1
    ```
    ```sh Required Launch Tests
    pip install pytest
    ```
    ```sh Launch Tests
    pytest
    ```
    ```sh Launch App
    python main.py
    ```

## GUI Usage

### Creating Characters
1. Click **Create Character** button
2. Fill in character details (name, HP, defenses, type)
3. Select or type a **Folder** name to organize your character
4. Click **Create**

### Managing Characters 
- Characters are organized in a **folder tree view** for easy navigation
- Select multiple characters to start combat with several combatants at once
- Use **Edit Character** to modify existing characters and their folder assignment
- Click **New Folder** to create a new folder and immediately add the first character to it

### Creating Character Folders
**Method 1 - Using "New Folder" button (Recommended):**
1. Click **New Folder**
2. Enter folder name (e.g., "Goblins", "Party Members")
3. Fill in character details
4. Character is created in the new folder

**Method 2 - Manual during character creation:**
1. Click **Create Character**
2. In the **Folder** field, type a new folder name (the dropdown is editable)
3. Fill in other details and create
4. Folder is automatically created

### Duplicating Characters
- Open **Edit Character** and select the character you want to duplicate
- Click **Duplicar** (Duplicate) to create a copy with "(Copy)" suffix
- Perfect for representing multiple instances of the same enemy type with the same stats

### Adding Multiple Copies to Combat
1. Select ONE character from the tree view
2. Click **Add Copies to Combat**
3. Enter how many copies you want (e.g., 5 for 5 goblins)
4. The copies will be added to your combat selection
5. Click **Iniciar Combate** to start combat with all instances

### Starting Combat
1. Select one or more characters from the tree view
2. Click **Iniciar Combate** (Start Combat)
3. The overlay will show all selected characters with their HP, defenses, and effects

## CLI Commands

### Create Character
```sh
python -m app.cli create-character \
  --name "Torm" \
  --max-hp 50 \
  --current-hp 50 \
  --ca-def 20 \
  --ref-def 18 \
  --fort-def 19 \
  --vol-def 17 \
  --char-type "PJ" \
  --folder "Party Members"
```

### List Characters
```sh
python -m app.cli list-characters
```
Output is grouped by folder for easy organization.

### Move Character to Different Folder
```sh
python -m app.cli move-character --char-id 1 --folder "Enemies"
```

### List All Folders
```sh
python -m app.cli list-folders
```

### Duplicate a Character
```sh
python -m app.cli duplicate-character --char-id 1
```
This creates a copy of the character with "(Copy)" suffix, useful for quickly creating multiple instances of the same enemy type.
