""" SQL template for Users CRUD
"""

__all__ = [
    "INS_USER_SINGLE_ROW",
    "UPD_USER_SINGLE_ROW",
    "CHECK_DUPLICATE_USER",
    "CHECK_USER_EXISTS",
    "QUERY_NAME",
    "UPDATE_NAME",
]

__DATABASE = "website"
__USER_TABLE = "member"

INS_USER_SINGLE_ROW = (
    f"INSERT INTO {__DATABASE}.{__USER_TABLE} (username, name, password) VALUES("
    "%s, %s, %s"
    ");"
)

UPD_USER_SINGLE_ROW = (
    f"UPDATE {__DATABASE}.{__USER_TABLE} SET %s=%s "
)
CHECK_DUPLICATE_USER = (
    f"SELECT count(*) FROM {__DATABASE}.{__USER_TABLE} "
    "WHERE username=%s"
)

CHECK_USER_EXISTS = (
    f"SELECT id,name FROM {__DATABASE}.{__USER_TABLE} "
    "WHERE 1=1 "
    "AND username=%s "
    "AND password=%s "
)
QUERY_NAME = (
    f"SELECT id,name,username FROM {__DATABASE}.{__USER_TABLE} "
    "WHERE 1=1 "
    "AND username=%s "
)

UPDATE_NAME = (
    f"UPDATE {__DATABASE}.{__USER_TABLE} "
    "SET name=%s "
    "WHERE 1=1 "
    "AND id=%s "
)