import pytest

# Pytest will scan the directory for conftests
# This is the place where all the fixtures belong
# Possible values for scope are: function, class, module, package or session
# https://docs.pytest.org/en/latest/fixture.html#


@pytest.fixture(scope='module')
def test_client():
    exec(open("app/setup.py").read())
    flask_app = create_app('flask_test.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
