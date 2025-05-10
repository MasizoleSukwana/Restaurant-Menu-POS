from services import RoleService

class MockUser:
    def get_allowed_actions(self): return ["view", "edit"]

class MockUserRepo:
    def get_user(self, user_id): return MockUser()

def test_can_perform_action():
    service = RoleService(MockUserRepo())
    assert service.can_perform_action("user1", "view") is True
    assert service.can_perform_action("user1", "delete") is False
