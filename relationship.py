'''Define inter-class relations'''

#This imports the global dictionary from main
from diagram import diagram

def addRelationship(className1, className2):
    # Check if both class names exist in the diagram
    if className1 in diagram and className2 in diagram:
        
        # For className1
        if "relationships" in diagram[className1]:
            diagram[className1]['relationships']['connections'].append(className2)
        else:
            diagram[className1]['relationships'] = {'connections': [className2]}
        
        # For className2
        if "relationships" in diagram[className2]:
            diagram[className2]['relationships']['connections'].append(className1)
        else:
            diagram[className2]['relationships'] = {'connections': [className1]}
    
    else:
        if className1 not in diagram:
            print(f"'{className1}' is not in the diagram.")
        if className2 not in diagram:
            print(f"'{className2}' is not in the diagram.")

def deleteRelationship(className1, className2):
    # Check if both classes exist in the diagram
    if className1 in diagram and className2 in diagram:
        
        # Check if relationships exist
        if "relationships" in diagram[className1] and className2 in diagram[className1]['relationships']['connections']:
            diagram[className1]['relationships']['connections'].remove(className2)
        
        if "relationships" in diagram[className2] and className1 in diagram[className2]['relationships']['connections']:
            diagram[className2]['relationships']['connections'].remove(className1)
    
    else:
        if className1 not in diagram:
            print(f"'{className1}' is not in the diagram.")
        if className2 not in diagram:
            print(f"'{className2}' is not in the diagram.")

