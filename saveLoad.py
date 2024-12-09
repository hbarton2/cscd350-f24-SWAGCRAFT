'''Implements save and load functionality for the UML model'''

import json
from model import Model
from classes import Class
from relationship import Relationship
from methods import Method
from parameters import ParameterAbstraction, ParameterImplementation
from fields import FieldAbstraction, FieldImplementation
from factory_classes import FieldFactory, ParameterFactory
from resources import myModel

def save(filename, positions=None):
    """
    Saves the model to a JSON file.
    """
    try:
        model_dict = {
            "classList": {}
        }
        
        for class_name, class_obj in myModel.classList.items():
            class_dict = {
                "name": class_obj.name,
                "fields": [],
                "methods": [],
                "relationships": []
            }
            
            # Save fields
            for field in class_obj.field:
                field_dict = {
                    "name": field.getName(),
                    "fieldType": field.getType()
                }
                class_dict["fields"].append(field_dict)
            
            # Save methods and their parameters
            for method in class_obj.method:
                method_dict = {
                    "name": method.name,
                    "return_type": method.returnType,
                    "parameters": []
                }
                for param in method.parameters:
                    param_dict = {
                        "name": param.getName(),
                        "type": param.getType()
                    }
                    method_dict["parameters"].append(param_dict)
                    
                class_dict["methods"].append(method_dict)
            
            # Save relationships
            for rel in class_obj.relationship:
                rel_dict = {
                    "fromClass": rel.fromClass,
                    "toClass": rel.toClass,
                    "relationType": rel.relationType
                }
                class_dict["relationships"].append(rel_dict)
            
            model_dict["classList"][class_name] = class_dict

        if positions is not None:
            model_dict["positions"] = positions

        with open(filename, 'w') as f:
            json.dump(model_dict, f, indent=4)
        
        return True
        
    except Exception as e:
        print(f"Error saving model: {str(e)}")
        return False


def load(filename, return_positions=False):
    """
    Loads a model from a JSON file and updates the global model state.
    """
    try:
        with open(filename, 'r') as f:
            model_dict = json.load(f)
        
        myModel.classList.clear()
        
        for class_name, class_data in model_dict["classList"].items():
            myModel.addClass(class_name)
            class_obj = myModel.classList[class_name]
            
            # Reconstruct fields
            for field_data in class_data["fields"]:
                field = FieldFactory.create_field(field_data["name"], field_data["fieldType"])
                class_obj.field.append(field)
            
            # Reconstruct methods and their parameters
            for method_data in class_data["methods"]:
                parameters = [
                    ParameterFactory.create_parameter(param["name"], param["type"])
                    for param in method_data["parameters"]
                ]
                class_obj.addMethod(method_data["name"], method_data["return_type"], parameters)
            
            # Reconstruct relationships
            for rel_data in class_data["relationships"]:
                class_obj.addRelationship(
                    rel_data["fromClass"],
                    rel_data["toClass"],
                    rel_data["relationType"]
                )

        positions = model_dict.get("positions", {}) if return_positions else None

        if return_positions:
            return True, positions
        else:
            return True

    except Exception as e:
        print(f"Error loading model: {str(e)}")
        if return_positions:
            return False, {}
        else:
            return False
