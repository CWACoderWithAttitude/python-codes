from dataclasses import dataclass

@dataclass
class StarTrekVesselDataClassNoDefaults:
    name: str
    ship_type: str
    
@dataclass
class StarTrekVesselDataClassWithDefaults:
    name: str = 'USS-Enterprise'
    ship_type: str = 'Galaxy-Class'
    