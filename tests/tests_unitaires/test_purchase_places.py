from server import POINTS_FOR_A_PLACE


def test_purchasePlaces_with_valid_data(client, mock_clubs, mock_competitions):
    valid_data = {'club': 'Test Club 1',
                  'competition': 'Test Competition 1',
                  'places': 12
                  }
    response = client.post('/purchasePlaces', data=valid_data)
    assert response.status_code == 200
    assert "Great-booking complete!" in response.data.decode()


def test_purchasePlaces_more_points_than_available(client, mock_clubs, mock_competitions):
    invalid_data = {'club': 'Test Club 2',
                    'competition': 'Test Competition 1',
                    'places': 14
                    }
    response = client.post('/purchasePlaces', data=invalid_data)
    assert response.status_code == 200
    assert "You cannot redeem more points than available!" in response.data.decode()
