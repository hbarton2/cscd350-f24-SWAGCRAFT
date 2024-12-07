from methods import Method
from parameters import Parameter
from fields import Field
from relationship import Relationship

class MethodFactory:
    @staticmethod
    def create_method(name, return_type, parameters):
        return Method(name, return_type, parameters)

class ParameterFactory:
    @staticmethod
    def create_parameter(name, param_type):
        return Parameter(name, param_type)

class FieldFactory:
    @staticmethod
    def create_field(name, field_type):
        return Field(name, field_type)

class RelationshipFactory:
    @staticmethod
    def create_relationship(fromClass, toClass, relationType):
        return Relationship(fromClass, toClass, relationType)