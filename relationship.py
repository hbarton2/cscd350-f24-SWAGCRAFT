from diagram import diagram

def addRelationship(className1, className2, relationType):
    """
    Use this function to add a new relationship between two classes.

    Parameters:
    className1 (str): The name of the first class.
    className2 (str): The name of the second class.
    relationType (str, optional): The type of the relationship (defaults to 'Aggregation').

    Returns:
    bool: True if the relationship was added successfully, False otherwise.
    """
    # Check if both class names exist in the diagram
    if className1 in diagram and className2 in diagram:
        # For className1
        if "relationships" in diagram[className1]:
            diagram[className1]['relationships']['connections'].append((className2, relationType))
        else:
            diagram[className1]['relationships'] = {'connections': [(className2, relationType)]}
        
        # For className2
        if "relationships" in diagram[className2]:
            diagram[className2]['relationships']['connections'].append((className1, relationType))
        else:
            diagram[className2]['relationships'] = {'connections': [(className1, relationType)]}
        
        return True
    else:
        return False


def deleteRelationship(className1, className2):
    """
    Use this function to remove an existing relationship between two classes.

    Parameters:
    className1 (str): The name of the first class.
    className2 (str): The name of the second class.

    Returns:
    bool: True if the relationship was removed successfully, False otherwise.
    """
    # Check if both classes exist in the diagram
    if className1 in diagram and className2 in diagram:
        # Check if relationships exist
        if "relationships" in diagram[className1]:
            for i, (related_class, _) in enumerate(diagram[className1]['relationships']['connections']):
                if related_class == className2:
                    del diagram[className1]['relationships']['connections'][i]
                    break
        
        if "relationships" in diagram[className2]:
            for i, (related_class, _) in enumerate(diagram[className2]['relationships']['connections']):
                if related_class == className1:
                    del diagram[className2]['relationships']['connections'][i]
                    break
        
        return True
    else:
        return False


def changeRelationType(className1, className2, newRelationType):
    """
    Use this function to change the type of an existing relationship between two classes.

    Parameters:
    className1 (str): The name of the first class.
    className2 (str): The name of the second class.
    newRelationType (str): The new type for the relationship.

    Returns:
    bool: True if the relationship type was changed successfully, False otherwise.
    """
    # Check if both classes exist in the diagram
    if className1 in diagram and className2 in diagram:
        # Check if relationships exist
        if "relationships" in diagram[className1]:
            for i, (related_class, relationType) in enumerate(diagram[className1]['relationships']['connections']):
                if related_class == className2:
                    diagram[className1]['relationships']['connections'][i] = (related_class, newRelationType)
                    break
        
        if "relationships" in diagram[className2]:
            for i, (related_class, relationType) in enumerate(diagram[className2]['relationships']['connections']):
                if related_class == className1:
                    diagram[className2]['relationships']['connections'][i] = (related_class, newRelationType)
                    break
        
        return True
    else:
        return False