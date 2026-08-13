from fastapi import APIRouter

order_router = APIRouter(prefix="/order",tags=["Orders"])

@order_router.get("/")
async def pedidos():
    """
    Rota padrão e principal dos pedidos
    """
    return {"mensagem": "Estes são os pedidos"}