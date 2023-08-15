from fastapi import APIRouter 
from src.controllers.analysis.get_metrics_controller import GetMetrics
from src.repositories.metrics import MetricsRespository
from src.services.reddit_scrapper import RedditScrapper
from src.adapters.http_client import HttpClient

router = APIRouter(prefix='/api')

metrics_repository = MetricsRespository()

reddit_http_client = HttpClient('https://www.reddit.com')
reddit_scrapper = RedditScrapper(reddit_http_client)

get_metrics_controller = GetMetrics(metrics_repository, reddit_scrapper)

@router.get("/metrics")
async def root():
    return get_metrics_controller.handle()

