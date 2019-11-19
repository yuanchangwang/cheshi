#coding=utf8
from models.base import metadata, mysql_db
from models.model_user import MUser
from models.model_award_pool import MAwardPool
from models.model_round_record import MRoundRecord

def create_table(table_names):
    need_tables = []
    for table in metadata.sorted_tables:
        if table.name in table_names:
            need_tables.append(table)

    metadata.create_all(mysql_db, need_tables)

if __name__ == "__main__":
    # create_table("ibb_user")
    create_table("ibb_awardpool")
    create_table("ibb_roundrecord")