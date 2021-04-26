
class Registrar:
    def __init__(self):
        # connect to database
        pass


    def add_slave_to_master(master_id: str, slave_id: str) -> bool:
        # Check if slave is in master list
        # if slave is not in master list, add to master list
        try:
            return True
        except Exception as e:
            print(e)
            return False

    def remove_slave_from_master(master_id: str, slave_id: str) -> bool:
        try:
            return True
        except Exception as e:
            print(e)
            return False

    def is_slave_in_master_list(master_id: str, slave_id: str) -> bool:
        try:
            return True
        except Exception as e:
            print(e)
            return False