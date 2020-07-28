import sqlite3
import aiosqlite

# Flariepoäng
conn = sqlite3.connect('Flarie.db')
c = conn.cursor()
tblFlaire = "info"
sql_create_table = """CREATE TABLE IF NOT EXISTS info
         (Name text NOT NULL, 
          MemberID integer PRIMARY KEY,
          SC integer,
          FT integer,
          AP integer,
          Level integer,
          Email text,
          Phonenumber text,
          Warnings integer)
        """
c.execute(sql_create_table)
conn.commit()


async def addMember(Name, MemberID):
    async with aiosqlite.connect('Flarie.db') as db:
        await db.execute(f'INSERT OR IGNORE INTO info VALUES ("{Name}", {MemberID}, 0, 0, 0, 0, "", "", 0)')
        await db.commit()


async def getWarnings(MemberID):
    async with aiosqlite.connect('Flarie.db') as db:
        cursor = await db.execute('SELECT Warnings FROM info WHERE MemberID = ?', (MemberID,))
        Tries = await cursor.fetchone()
        await db.commit()
        return Tries[0]


async def getInfo(MemberID):
    async with aiosqlite.connect('Flarie.db') as db:
        cursor = await db.execute('SELECT Email, Phonenumber FROM info WHERE MemberID = ?', (MemberID,))
        info = await cursor.fetchall()
        await db.commit()
        return info


async def getPoints(MemberID, type):
    async with aiosqlite.connect('Flarie.db') as db:
        cursor = await db.execute(f'SELECT {type.upper()} FROM info WHERE MemberID = ?', (MemberID,))
        Point = await cursor.fetchone()
        await db.commit()
        return Point[0]


async def getTop(type):
    async with aiosqlite.connect('Flarie.db') as db:
        cursor = await db.execute(f'SELECT Name, {type} FROM info ORDER BY {type} DESC')
        top = await cursor.fetchmany(10)
        await db.commit()
        return top


async def addPoints(MemberID, type, Point):
    async with aiosqlite.connect('Flarie.db') as db:
        await db.execute(f'SET {type.upper()} = {Point + getPoints(MemberID, type)} WHERE MemberID')
        await db.commit()


# AP

async def APadd(MemberID, AP):
    async with aiosqlite.connect('Flarie.db') as db:
        await db.execute('UPDATE info SET AP = ? WHERE MemberID = ?', (AP, MemberID,))
        await db.commit()


async def levelget(MemberID):
    async with aiosqlite.connect('Flarie.db') as db:
        cursor = await db.execute('SELECT Level from info WHERE MemberID = ?', (MemberID,))
        Level = await cursor.fetchone()
        await db.commit()
        return Level[0]


async def leveladd(Level, MemberID):
    async with aiosqlite.connect('Flarie.db') as db:
        await db.execute('UPDATE info SET Level = ? WHERE MemberID = ?', (Level, MemberID,))
        await db.commit()


# SC


# FT

async def FTchange(MemberID, FT):
    async with aiosqlite.connect('Flarie.db') as db:
        await db.execute('UPDATE info SET FT = ? WHERE MemberID = ?', (FT, MemberID,))
        await db.commit()
