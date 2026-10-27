import pytest
from decimal import Decimal
from app.domain import Money, InvalidOrderData, InvalidOrderTransition, OrderItemLimitExceeded
from cargar_csv import load_fixture

def test_money_negativo():
    with pytest.raises(InvalidOrderData):
        Money(Decimal("-1"))

def test_pedido_0001_inicia_draft():
    orders = load_fixture()
    assert orders["O001"].status.value == "DRAFT"
    assert orders["O001"].units == 4
    assert orders["O001"].total.amount == Decimal("2100.00")

def test_limite_20_unidades():
    orders = load_fixture()
    order = orders["O009"] # Tiene 19 unidades
    
    with pytest.raises(OrderItemLimitExceeded):
        # Intentamos agregar 2 unidades más (supera el límite de 20)
        from app.domain import OrderItem, Money
        item = OrderItem(sku="SKU999", quantity=2, unit_price=Money(Decimal("100.00")))
        order.add_item(item)

def test_confirmacion_doble():
    orders = load_fixture()
    order = orders["O013"]
    order.confirm() # Primera vez (Éxito)
    
    with pytest.raises(InvalidOrderTransition):
        order.confirm() # Segunda vez debe fallar