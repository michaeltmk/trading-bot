from pydantic import BaseModel
import yaml
from typing import List, Any
from strategies import get_strategies_config_model
class strategy_config_model(BaseModel):
    name: str
    enabled: bool
    type: str
    config: Any

    @model_validator(mode='before')
    def ingest_config(cls, v):
        try:
            v['config'] = get_strategies_config_model(v['type'])(**v['config'])
        except ValueError:
            raise ValueError(f"Unknown strategy type: {v['type']}")



class strategies_config_model(BaseModel):
    strategies: List[strategy_config_model]


def load_strategies_config(config_file) -> strategies_config_model:
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return strategies_config_model(**config)