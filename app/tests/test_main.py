from app.main import Dashboard

dashboard = Dashboard()

class TestMain:

    def test_title(self):
        dashboard.title()
        assert(True)
