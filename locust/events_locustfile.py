from locust import HttpUser, task, constant

class EventsUser(HttpUser):

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user")
