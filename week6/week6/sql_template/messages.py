""" SQL temmplate for MESSAGE CRUD
"""

__all__ = [
    "SHOW_MESSAGE_ALL_ROWS",
    "INS_MESSAGE_SINGLE_ROW",
    "DEL_MESSAGE_SINGLE_ROW",
]

__DATABASE = "website"
__USER_TABLE = "member"
__MESSAGE_TABLE = "message"

SHOW_MESSAGE_ALL_ROWS = (
    f"SELECT member_id, name, content, {__MESSAGE_TABLE}.id FROM {__DATABASE}.{__MESSAGE_TABLE} " 
    f"JOIN {__DATABASE}.{__USER_TABLE} ON {__MESSAGE_TABLE}.member_id={__USER_TABLE}.id "
    f"ORDER BY {__MESSAGE_TABLE}.time DESC"
    ";"
)

INS_MESSAGE_SINGLE_ROW = (
    f"INSERT INTO {__DATABASE}.{__MESSAGE_TABLE} (member_id, content) VALUES("
    "%s, %s"
    ");"
)

DEL_MESSAGE_SINGLE_ROW = (
    f"DELETE FROM {__DATABASE}.{__MESSAGE_TABLE} "
    "WHERE 1=1 "
    "AND id=%s "
    "AND member_id=%s "
)