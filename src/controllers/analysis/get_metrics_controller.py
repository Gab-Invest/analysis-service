class GetMetrics():
    def __init__(self, metrics_repository) -> None:
        self.metrics_repository = metrics_repository
    
    def handle(self):
        return self.metrics_repository.find() 