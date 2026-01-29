from locust import HttpUser, task, constant_pacing

class MyEventsUser(HttpUser):
    wait_time = constant_pacing(0)

    @task
    def view_my_events(self):
        self.client.get("/my-events?user=locust_user")
