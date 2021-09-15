from lodat.database.database_manager import DatabaseManager


def test_init_database():
    dbm = DatabaseManager()
    success = dbm.close_database()
    assert success