"""
Database migration utilities
"""
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.infrastructure.db.database import engine


def migrate_add_folder_column():
    """Add folder column to characters table if it doesn't exist"""
    with engine.connect() as conn:
        # Check if folder column exists
        result = conn.execute(
            text("PRAGMA table_info(characters)")
        ).fetchall()
        
        column_names = [row[1] for row in result]
        
        if 'folder' not in column_names:
            conn.execute(
                text("ALTER TABLE characters ADD COLUMN folder VARCHAR DEFAULT 'Sin carpeta'")
            )
            conn.commit()
            print("✅ Migration: Added 'folder' column to characters table")
        else:
            print("ℹ️  Migration: 'folder' column already exists")


def run_migrations():
    """Run all pending migrations"""
    migrate_add_folder_column()
