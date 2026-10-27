from fastapi import FastAPI, HTTPException
from cargar_csv import load_fixture
from app.domain import InvalidOrderTransition, InvalidOrderData

app = FastAPI(title="TechStore U4")
orders = load_fixture()

@app.post("/orders/{order_id}/confirm")
def confirm_order(order_id: str):
    # Buscamos el pedido limpiando cualquier espacio invisible de ambos lados
    order = next((o for key, o in orders.items() if str(key).strip() == str(order_id).strip()), None)
    
    if order is None:
        raise HTTPException(status_code=404, detail="No existe")
    
    try:
        order.confirm()
    except InvalidOrderTransition as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    except InvalidOrderData as exc:
        raise HTTPException(status_code=422, detail=str(exc))
        
    return {"id": order.id, "status": order.status.value}