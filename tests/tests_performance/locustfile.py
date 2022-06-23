from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    """
    Utilisez Locust pour vous assurer que le temps de chargement ne dépasse jamais 5 secondes,
    et que les mises à jour ne prennent pas plus de 2 secondes.
    Le nombre d'utilisateurs par défaut pour les tests de performance est de 6.
    """
    @task
    def index(self):
        with self.client.get('/', catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure('The request took too long')

    @task
    def show_summary(self):
        data = {'email': 'john@simplylift.co'}
        with self.client.post('/showSummary', data=data, catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure('The request took too long')

    @task
    def purchase_places(self):
        data = {'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1}
        with self.client.post('/purchasePlaces', data=data, catch_response=True) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure('The request took too long')

    @task
    def book(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    @task
    def display_points_board(self):
        with self.client.get('/displayPointsBoard', catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure('The request took too long')

    @task
    def logout(self):
        with self.client.get('/logout', catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure('The request took too long')
