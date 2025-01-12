def test_invalid_competition_date(client, mock_clubs, mock_competitions):
    club = mock_clubs[0]['name']
    competition = mock_competitions[3]['name']
    response = client.get(f"/book/{competition}/{club}")
    assert response.status_code == 200
    assert "You cannot book places in past competition" in response.data.decode()


def test_valid_competition_date(client, mock_clubs, mock_competitions):
    club = mock_clubs[0]['name']
    competition = mock_competitions[0]['name']
    response = client.get(f"/book/{competition}/{club}")
    assert response.status_code == 200


def test_no_existing_competition(client, mock_clubs, mock_competitions):
    club = 'no existing'
    competition = 'no existing'
    response = client.get(f"/book/{competition}/{club}")
    assert response.status_code == 200
    assert "Something went wrong-please try again" in response.data.decode()
