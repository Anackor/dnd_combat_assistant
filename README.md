# dnd_combat_assistant
This is a local desktop application built with Python for helping Game Masters run Dungeons &amp; Dragons 4e encounters. The application allows users to configure and visualize party members or enemies with attributes like health points, defenses, and active effects.

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

    ```sh Create PJ with CLI
    python -m app.cli create-character --name "Torm" --max-hp 50 --current-hp 50 --ca-def 20 --ref-def 18 --fort-def 19 --vol-def 17
    ```
    ```sh List Characters
    python -m app.cli list-characters
    ```
