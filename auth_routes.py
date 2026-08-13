from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autentication():
    """
    Rota principal e padrão de autenticação
    """
    return {"mensagem": "User requisita autenticação", "status": False}