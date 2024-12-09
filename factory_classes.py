from methods import Method
from parameters import ParameterImplementation, ParameterAbstraction
from fields import FieldAbstraction, FieldImplementation
from relationship import Relationship

class MethodFactory:
    @staticmethod
    def create_method(name, return_type, parameters):
        return Method(name, return_type, parameters)

class ParameterFactory:
    @staticmethod
    def create_parameter(param_name, param_type):
        param_impl = ParameterImplementation(param_name, param_type)
        return ParameterAbstraction(param_impl)

class FieldFactory:
    @staticmethod
    def create_field(field_name, field_type):
        field_impl = FieldImplementation(field_name, field_type)
        return FieldAbstraction(field_impl)

class RelationshipFactory:
    @staticmethod
    def create_relationship(fromClass, toClass, relationType):
        return Relationship(fromClass, toClass, relationType)