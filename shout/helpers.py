from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy import select
from flask_sqlalchemy import SQLAlchemy


class BlazeAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options['pool_size'] = 0
        return super(BlazeAlchemy, self).apply_driver_hacks(app, info, options)


def ping_connection(dbapi_connection, connection_record, connection_proxy):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except:
        # raise DisconnectionError - pool will try
        # connecting again up to three times before raising.
        raise exc.DisconnectionError()
    cursor.close()