from server import POINTS_FOR_A_PLACE


def test_login_logout(client, mock_clubs, mock_competitions):
    input_value_login = {'email': 'club1@test.com'}
    response = client.post('/showSummary', data=input_value_login)
    assert response.status_code == 200
    assert "Welcome" in response.data.decode()
    expected_club_value = 40 - (2 * POINTS_FOR_A_PLACE)
    expected_competition_value = 25 - 2
    input_value_purchase_places = {'club': 'Test Club 1',
                                   'competition': 'Test Competition 1',
                                   'places': 2
                                   }
    response = client.post('/purchasePlaces', data=input_value_purchase_places)
    assert response.status_code == 200
    assert "Great-booking complete!" in response.data.decode()
    assert f"Points available: {expected_club_value}"
    assert f"Number of Places: {expected_competition_value} Book Places"
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200