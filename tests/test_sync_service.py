from services import SyncService

class MockOfflineRepo:
    def get_all_unsynced(self):
        return [type("Order", (), {"id": "1", "synced": False})()]
    def mark_synced(self, order_id): self.synced = order_id

class MockOrderRepo:
    def save_order(self, order): pass

def test_sync_orders_marks_synced():
    offline = MockOfflineRepo()
    service = SyncService(offline, MockOrderRepo())
    service.sync_orders()
    assert offline.synced == "1"
