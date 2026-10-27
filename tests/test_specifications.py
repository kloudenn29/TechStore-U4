import pytest
from decimal import Decimal
from app.specifications import MinimumAmountSpec, MinimumUnitsSpec, VIPCustomerSpec
from cargar_csv import load_fixture

def test_regla_10_porciento_vip():
    orders = load_fixture()
    order = orders["O001"] # Cumple: VIP, > 500, 4 unidades
    
    amount_spec = MinimumAmountSpec(Decimal("500"))
    units_spec = MinimumUnitsSpec(4)
    vip_spec = VIPCustomerSpec()
    
    # Combinación AND
    regla_10 = amount_spec & units_spec & vip_spec
    assert regla_10.is_satisfied_by(order) == True

def test_regla_rechazada_por_monto():
    orders = load_fixture()
    order = orders["O010"] # Total exacto 500, no es mayor a 500
    
    amount_spec = MinimumAmountSpec(Decimal("500"))
    assert amount_spec.is_satisfied_by(order) == False