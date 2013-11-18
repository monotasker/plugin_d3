import json
from pprint import pprint
if 0: from gluon import current

def example1():
    """
    Example of a controller function providing json data to a d3-based
    visualization.

    """
    # make sure d3.js dc.js and crossfire.js are loaded
    response.files.append(URL('static', 'plugin_d3/d3/d3.js'))
    response.files.append(URL('static', 'plugin_d3/dc/dc.js'))
    response.files.append(URL('static', 'plugin_d3/crossfilter/crossfilter.js'))
    response.files.append(URL('static', 'plugin_d3/dc/dc.css'))

    db = current.db
    group = 132
    rows = db((db.tag_progress.name == db.auth_membership.user_id) &
              (db.auth_membership.group_id == group)).select().as_list()
    pprint(rows)
    return {'data': rows}

