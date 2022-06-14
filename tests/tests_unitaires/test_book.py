from server import POINTS_FOR_A_PLACE, MAX_PLACES_PER_COMPETITION
"""
Bug :
Quand un secrétaire essaie de réserver un certain nombre de places dans une compétition déjà passée,
il reçoit un message de confirmation.

Attendu :
Il ne devrait pas pouvoir réserver de places dans une compétition déjà passée.
Mais les concours passés doivent être visibles.
La page booking.html doit être affichée pour une compétition valide.
Un message d'erreur doit s'afficher lorsqu'une compétition n'est pas valide.
Un message de confirmation doit s'afficher lorsqu'une compétition est valide.
"""


def test_invalid_competition_date(client, mock_clubs, mock_competitions):
    club = mock_clubs[0]['name']
    competition = mock_competitions[0]['name']
    response = client.get(f"/book/{competition}/{club}")
    assert response.status_code == 200
    assert "You cannot book places in past competition" in response.data.decode()


def test_valid_competition_date(client, mock_clubs, mock_competitions):
    club = mock_clubs[0]['name']
    competition = mock_competitions[1]['name']
    response = client.get(f"/book/{competition}/{club}")
    assert response.status_code == 200







