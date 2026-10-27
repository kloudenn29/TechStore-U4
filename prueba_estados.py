from cargar_csv import load_fixture
from app.domain import InvalidOrderTransition

orders = load_fixture()
order = list(orders.values())[0]

print(f"Estado Inicial: {order.status.value}")
order.confirm()
print(f"Tras primer confirm(): {order.status.value} - Eventos: {[e.name for e in order.events]}")

try:
    order.confirm()
except InvalidOrderTransition as e:
    print(f"Error al intentar confirmar de nuevo: {e}")