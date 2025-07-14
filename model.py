import datetime

class Todo:
    def __init__(self, id, task, category, date_added=None, date_completed=None, status=None, position=None):
        self.id = id
        self.task = task
        self.category = category
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()
        self.date_completed = date_completed if date_completed is not None else None
        # 0 for pending, 1 for completed
        self.status = status if status is not None else 0
        self.position = position if position is not None else None

    def __repr__(self):
        return (
            f"Todo(id={self.id}, task={self.task}, category={self.category}, "
            f"date_added={self.date_added}, date_completed={self.date_completed}, "
            f"status={self.status}, position={self.position})"
        )
        