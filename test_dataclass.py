import pytest
from .dataclass import StarTrekVesselDataClassNoDefaults, StarTrekVesselWithDefaults, StarTrekVesselWithDefaultsAndOptional, FrozenVessel

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
    """Dataclass has default values for properties.
    """
    v = StarTrekVesselWithDefaults()
    assert 'USS-Enterprise' == v.name
    assert 'Galaxy-Class' == v.ship_type

from dataclasses import FrozenInstanceError
def test_dc_without_optional():
    """Here the expected value for optional property is set None
    """
    t = StarTrekVesselWithDefaultsAndOptional()
    assert 'USS-Enterprise' == t.name
    assert 'Galaxy-Class' == t.ship_type
    assert None == t.captain

def test_dc_with_optional():
    """Here the expected value for given optional property is verified
    """
    t = StarTrekVesselWithDefaultsAndOptional(captain='Jean-Luc Picard')
    assert 'USS-Enterprise' == t.name
    assert 'Galaxy-Class' == t.ship_type
    assert 'Jean-Luc Picard' == t.captain

def test_dataclass_string_representation():
    """Dataclasses give us a useful default string representation
    """
    t = StarTrekVesselWithDefaultsAndOptional(captain='Jean-Luc Picard')
    assert "StarTrekVesselWithDefaultsAndOptional(captain='Jean-Luc Picard', name='USS-Enterprise', ship_type='Galaxy-Class')" == str(t)
    
def test_frozen_vessel():
    expected_error_msg = "cannot assign to field 'name'"
    t = FrozenVessel()
    assert 'USS-Enterprise' == t.name
    with pytest.raises (FrozenInstanceError) as excinfo:
        t.name = 'USS-Stargazer'
        assert 'USS-Stargazer' == t.name
    assert str(excinfo.value) == expected_error_msg
    
    