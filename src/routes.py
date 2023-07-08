from fastapi import APIRouter 
from src.controllers.analysis.get_metrics_controller import GetMetrics
from src.repositories.metrics import MetricsRespository

router = APIRouter(prefix='/api')

metrics_repository = MetricsRespository()
get_metrics_controller = GetMetrics(metrics_repository)

@router.get("/metrics")
async def root():
    return get_metrics_controller.handle()

