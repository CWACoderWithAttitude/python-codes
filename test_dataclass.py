import pytest
from .dataclass import StarTrekVesselDataClassNoDefaults, StarTrekVesselDataClassWithDefaults

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