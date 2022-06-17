from server import POINTS_FOR_A_PLACE
"""
Bug :
Quand un secrétaire échange des points contre une place dans une compétition le nombre de points du club reste le même.

Attendu :
Le nombre de points utilisés doit être déduit du solde du club.
"""


def test_purchasePlaces_update_club_points(client, mock_clubs, mock_competitions):
    places_required = 10
    club = mock_clubs[0]
    competition = mock_competitions[0]
    club_points_before_booking = int(club["points"])  # Mock with 13 points
    club_points_after_booking = club_points_before_booking - (places_required * POINTS_FOR_A_PLACE)  # expected result 3
    data = {'club': club['name'],
            'competition': competition['name'],
            'places': places_required
            }
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert int(club['points']) == club_points_after_booking
    assert "Points available: 3" in response.data.decode()


def test_







