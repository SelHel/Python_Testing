def test_should_access_points_board(client):
    response = client.get('/displayPointsBoard')
    assert response.status_code == 200


def test_display_points_board(client, mock_clubs):
    clubs = mock_clubs
    response = client.get('/displayPointsBoard')
    assert response.status_code == 200
    for club in clubs:
        assert club['name'] in response.data.decode()
        assert str(club["points"]) in response.data.decode()
