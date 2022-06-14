"""
Quand un secrétaire se connecte à l'application il devrait pouvoir voir la liste des clubs
et leurs soldes de points actuels.
"""


def test_should_access_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_showSummary_with_known_email(client, mock_clubs):
    known_email = 'club3@test.com'
    response = client.post('/showSummary', data={'email': known_email})
    assert response.status_code == 200
    assert "Welcome" in response.data.decode()


def test_showSummary_with_unknown_email(client, mock_clubs):
    unknown_email = 'wrong@email.co'
    response = client.post('/showSummary', data={'email': unknown_email})
    assert response.status_code == 200
    assert "Sorry, that email wasn&#39;t found." in response.data.decode()


def test_showSummary_with_empty_email(client, mock_clubs):
    empty_email = ''
    response = client.post('/showSummary', data={'email': empty_email})
    assert response.status_code == 200
    assert "Sorry, that email wasn&#39;t found." in response.data.decode()






