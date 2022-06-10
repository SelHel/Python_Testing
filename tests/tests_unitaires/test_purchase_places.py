from server import POINTS_FOR_A_PLACE

"""
Bug :
Quand un secrétaire échange plus de points qu'il en a à sa disposition,
ce qui le laisserait dans le négatif, il reçoit un message de confirmation.

Attendu :
Il ne devrait pas pouvoir échanger plus de points que disponibles.
Les points échangés doivent être correctement déduits du total du club.
"""


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


def test_purchasePlaces_update_club_points(client, mock_clubs, mock_competitions):
    places_required = 12
    club = mock_clubs[0]
    competition = mock_competitions[0]
    club_points_before_booking = int(club["points"])
    club_points_after_booking = club_points_before_booking - (places_required * POINTS_FOR_A_PLACE)
    data = {'club': club['name'],
            'competition': competition['name'],
            'places': places_required
            }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert int(club['points']) == club_points_after_booking
    assert "Great-booking complete!" in response.data.decode()