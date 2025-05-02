# config_manager.py

class POSConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(POSConfigManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance

    def set_config(self, key, value):
        self.config[key] = value

    def get_config(self, key):
        return self.config.get(key)
