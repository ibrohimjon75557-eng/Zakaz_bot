import aiosqlite

DB_NAME = "orders.db"

async def create_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            phone TEXT,
            kg REAL,
            box INTEGER
        )
        """)
        await db.commit()

async def save_order(user_id, phone, kg, box):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO orders (user_id, phone, kg, box) VALUES (?, ?, ?, ?)",
            (user_id, phone, kg, box)
        )
        await db.commit()
