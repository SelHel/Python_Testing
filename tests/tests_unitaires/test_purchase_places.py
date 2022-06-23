from server import POINTS_FOR_A_PLACE, MAX_PLACES_PER_COMPETITION
"""
Bug :
Quand un secrétaire essaie de réserver plus de 12 places dans une compétition,
il reçoit un message de confirmation.

Attendu :
Il ne devrait pas pouvoir réserver plus de 12 places par compétition.
L'UI doit l'empêcher de réserver plus de 12 places.
Les places doivent être correctement déduites de la compétition.
"""


def test_purchasePlaces_more_than_twelve_places_in_competition(client, mock_clubs, mock_competitions):
    data = {'club': 'Test Club 2',
            'competition': 'Test Competition 1',
            'places': 13
            }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert f"You cannot book more than {MAX_PLACES_PER_COMPETITION} places per competition!" in response.data.decode()


def test_purchasePlaces_more_places_than_available_in_competition(client, mock_clubs, mock_competitions):
    data = {'club': 'Test Club 2',
                    'competition': 'Test Competition 3',
                    'places': 6
                    }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert "You cannot reserve more places than are available in the competition!" in response.data.decode()


def test_purchasePlaces_update_competition_places(client, mock_clubs, mock_competitions):
    places_required = 12
    club = mock_clubs[0]
    competition = mock_competitions[0]
    competition_places_before_booking = int(competition['numberOfPlaces'])
    competition_places_after_booking = competition_places_before_booking - places_required
    data = {'club': club['name'],
            'competition': competition['name'],
            'places': places_required
            }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert int(competition['numberOfPlaces']) == competition_places_after_booking
    assert "Great-booking complete!" in response.data.decode()




