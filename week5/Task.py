class Task:
    def __init__(self, task_id, priority, arrival_time, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task({self.task_id}, {self.priority})"
