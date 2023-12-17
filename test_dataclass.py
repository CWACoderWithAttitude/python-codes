import pytest
from .dataclass import StarTrekVesselDataClassNoDefaults, StarTrekVesselDataClassWithDefaults, StarTrekVesselWithDefaultsAndOptional

def test_init_dataclass_wo_properties():
    """Expect error because properties on default class have no default value.
    """
    with pytest.raises (TypeError) as excinfo:
        StarTrekVesselDataClassNoDefaults()
    assert str(excinfo.value) == "StarTrekVesselDataClassNoDefaults.__init__() missing 2 required positional arguments: 'name' and 'ship_type'"
    
def test_init_dataclass_with_all_properties():
    """No error because all properties have default values
    """
    StarTrekVesselDataClassNoDefaults(name='Enterprise', ship_type="Enterprise")

def test_dataclass_with_defaults():
    """No error because all properties have default values
    """
    StarTrekVesselDataClassWithDefaults()
    
def test_dc_without_optional():
    t = StarTrekVesselWithDefaultsAndOptional()
    assert 'USS-Enterprise' == t.name
    assert 'Galaxy-Class' == t.ship_type
    assert None == t.captain

def test_dc_with_optional():
    t = StarTrekVesselWithDefaultsAndOptional(captain='Jean-Luc Picard')
    assert 'USS-Enterprise' == t.name
    assert 'Galaxy-Class' == t.ship_type
    assert 'Jean-Luc Picard' == t.captain