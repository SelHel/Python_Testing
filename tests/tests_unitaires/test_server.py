
def test_showSummary_with_unknown_email(client):
    unknown_email = 'wrong@email.co'
    response = client.post('/showSummary', data={'email': unknown_email})
    assert response.status_code == 302


def test_showSummary_with_known_email(client):
    known_email = 'john@simplylift.co'
    response = client.post('/showSummary', data={'email': known_email})
    assert response.status_code == 200


def test_club_should_not_be_able_to_use_more_than_their_points_allowed():
    pass


def test_points_should_be_deducted_from_the_clubs_total():
    pass




