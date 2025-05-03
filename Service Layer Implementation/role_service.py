class RoleService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def can_perform_action(self, user_id, action):
        user = self.user_repository.get_user(user_id)
        return action in user.get_allowed_actions()
