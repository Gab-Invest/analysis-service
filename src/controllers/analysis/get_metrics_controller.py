class GetMetrics():
    def __init__(self, metrics_repository, scrapper) -> None:
        self.metrics_repository = metrics_repository
        self.scrapper = scrapper
    
    def handle(self):
        return self.scrapper.execute()
