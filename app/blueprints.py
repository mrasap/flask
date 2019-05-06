"""
All Flask blueprints for the entire application.
All blueprints for all views go here. They shall be imported by the views themselves and by
application.py. Blueprint URL paths are defined here as well.
"""

from flask import Blueprint


def _factory(name, url_prefix):
    """
    Generates blueprint objects for view modules.

    :param name -- string representing a view module without the absolute path
    (e.g. 'index' for app.views.index).
    :param url_prefix -- URL prefix passed to the blueprint.

    :return: Blueprint instance for a view module.
    """
    return Blueprint(
        name=name,
        import_name='app.views.{}'.format(name),
        template_folder='templates',
        url_prefix=url_prefix
    )


index = _factory('index', '/')
increase = _factory('increase', '/increase')

all_blueprints = (index, increase, )
