from csv_app import db


def full_refresh_batch_insert(table_class, data, batch_size):
    try:
        db.session.query(table_class).delete()
        db.session.commit()
    except:                                     # noqa: E722
        # Ignore the UndefinedTable error
        # The table has not been created yet,
        # so the operation cannot be performed
        pass

    for index in range(0, len(data), batch_size):
        batch = data[index:index+batch_size]
        db.session.execute(table_class.__table__.insert(), batch)
        db.session.commit()
