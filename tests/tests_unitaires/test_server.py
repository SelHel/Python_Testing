def test_should_access_home(client):
    response = client.get('/')
    assert response.status_code == 200


def test_showSummary_with_known_email(client, mock_clubs):
    known_email = 'club3@test.com'
    response = client.post('/showSummary', data={'email': known_email})
    assert response.status_code == 200


def test_showSummary_with_unknown_email(client):
    unknown_email = 'wrong@email.co'
    response = client.post('/showSummary', data={'email': unknown_email})
    assert response.status_code == 302


def test_showSummary_with_empty_email(client):
    empty_email = ''
    response = client.post('/showSummary', data={'email': empty_email})
    assert response.status_code == 302






