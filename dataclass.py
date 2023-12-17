from dataclasses import dataclass
from typing import Optional

@dataclass
class StarTrekVesselDataClassNoDefaults:
    name: str
    ship_type: str
    
@dataclass
class StarTrekVesselWithDefaults:
    name: str = 'USS-Enterprise'
    ship_type: str = 'Galaxy-Class'

@dataclass
class StarTrekVesselWithDefaultsAndOptional:
    captain: Optional[str] = None
    name: str = 'USS-Enterprise'
    ship_type: str = 'Galaxy-Class'
    