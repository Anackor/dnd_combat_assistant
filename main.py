from app.infrastructure.db.database import init_db

def main():
    print("Starting D&D Assistant...")
    init_db()

if __name__ == "__main__":
    main()
