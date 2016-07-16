from couchbase.bucket import Bucket
from couchbase.exceptions import CouchbaseError

def get_bucket():
    buc = Bucket('couchbase://localhost:8091/default')
    return buc


def get_doc(bucket, key):
    try:
        val = bucket.get(key)
        return val.value
    except CouchbaseError as e:
        print e


def update_doc(bucket, key, doc):
    try:
        bucket.upsert(key, doc)

    except CouchbaseError as e:
        print e

def map_point(data_id, date, category, latitude, longitude):
    return {
        date: date,
        category: category,
        latitude: latitude,
        longitude: longitude
    }


def blog_post(blog_id, date, title, body, latitude, longitude, location):
    return {
        date: date,
        title: title,
        body: body,
        latitude: latitude,
        longitude: longitude,
        location: location
    }

