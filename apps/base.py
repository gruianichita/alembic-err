from humps import camelize
from pydantic import BaseModel


def to_camel(string):
    """
    Func to create an alias from snake case variables
    """
    return camelize(string)


class CamelModel(BaseModel):
    """
    Base model to auto create a camelCase alias. 
    Also allows population of Pydantic model via alias
    """

    class Config:
        """Config"""

        alias_generator = to_camel
        allow_population_by_field_name = True
