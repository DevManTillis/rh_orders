
# Subscribes to controller
# - JSON maps to parent trader
# - Need crud parent trader mapping so that user can edit who they subscribe to
# - must break up app so that service doesn't lock up when switching between subscriber trader / parent trader
# - Push or pull?

class CopyCat:
    def __init__(self, JSON: dict):
        if JSON['parent_id'] == CONFIG.parent_id:
            print(f"Check if service is subscribed to parent_id {}")
        elif JSON['parent_id'] != CONFIG.parent_id:
            return "do something"