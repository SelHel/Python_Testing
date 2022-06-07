import pytest

import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    return client


@pytest.fixture
def mock_clubs(mocker):
    clubs = [
        {
            "name": "Test Club 1",
            "email": "club1@test.com",
            "points": "13"
        },
        {
            "name": "Test Club 2",
            "email": "club2@test.com",
            "points": "4"
        },
        {
            "name": "Test Club 3",
            "email": "club3@test.com",
            "points": "12"
        },
    ]
    mocker.patch.object(server, 'clubs', clubs)