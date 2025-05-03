class SyncService:
    def __init__(self, offline_order_repo, order_repository):
        self.offline_order_repo = offline_order_repo
        self.order_repository = order_repository

    def sync_orders(self):
        offline_orders = self.offline_order_repo.get_all_unsynced()
        for order in offline_orders:
            self.order_repository.save_order(order)
            order.synced = True
            self.offline_order_repo.mark_synced(order.id)
