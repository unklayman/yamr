class Status:
    ok = 200
    not_found = 404
    error = 500
    already_exists = 409

    @staticmethod
    def description(stat):
        if stat == Status.ok:
            return "Ok"
        elif stat == Status.not_found:
            return "Item not found"
        elif stat == Status.error:
            return "Internal error"
        else:
            return "Item already exists"


class MapStatus:
    accepted = 201  # task has been started
    chunk_loaded = 202  # data chunk has been loaded

    chunk_not_found = 404

    error = 500
    already_exists = 501 # task already exists

    finished = 600


class TaskStatus:
    accepted = 200
    mapping = 210
    mapping_done = 220
    reducing = 230
    task_done = 240