import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from controller import diagram
from controller import addClass, renameClass, deleteClass
from controller import addField, removeField, renameField
from controller import addMethod, removeMethod, renameMethod, addParameter, removeParameter, changeParameter
from controller import addRelationship, deleteRelationship

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")  #blue is my favorite colon -cn


class UMLApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #config window
        self.title("UML Diagram Application")
        self.geometry("1600x800")
        self.minsize(1600, 800)

        self.diagram = diagram  #now instead using the imported diagram from diagram.py. trying to adhere to aiden's format.

        #tracking pos for class frames
        self.classPos = {}
        self.classRects = {}
        self.relationshipLines = []  #next phase in sprint will be making different types of relationships
        self.createTBOX()
        self.createDrwArea()
        self.createStsBar()
        self.drawDiagram()


    def createTBOX(self):
        #da frame
        tboxFRAME = ctk.CTkFrame(self, width=150) #updated size a lil
        tboxFRAME.pack(side="left", fill="y", padx=5, pady=5)
        tboxLABEL = ctk.CTkLabel(tboxFRAME, text="Toolbox", font=ctk.CTkFont(size=16, weight="bold"))
        tboxLABEL.pack(pady=(10, 5))

        #add a class button
        addClassBTN = ctk.CTkButton(tboxFRAME, text="Add Class", command=self.addClass)
        addClassBTN.pack(padx=10, pady=5)

        #rename class button
        renameClassBTN = ctk.CTkButton(tboxFRAME, text="Rename Class", command=self.renameClass)
        renameClassBTN.pack(padx=10, pady=5)

        #list all classes button
        listClassesBTN = ctk.CTkButton(tboxFRAME, text="List Classes", command=self.listClasses)
        listClassesBTN.pack(padx=10, pady=5)

        #add relationship button
        addRelBTN = ctk.CTkButton(tboxFRAME, text="Add Relationship", command=self.addRelationship)
        addRelBTN.pack(padx=10, pady=5)

        #overall diagram button
        overallDiagramBTN = ctk.CTkButton(tboxFRAME, text="Overall Diagram", command=self.showOverallDiagram)
        overallDiagramBTN.pack(padx=10, pady=5)


    def createDrwArea(self):
        #create area frame
        self.drawFRAME = ctk.CTkFrame(master=self)
        self.drawFRAME.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.drawFRAME, bg="white")  #drawing to canvas
        self.canvas.pack(fill="both", expand=True)

        #binding clicking to giving options for the class instead of just deleting it like my previous vers
        self.canvas.bind("<Button-1>", self.onCanvasCLK)


    def createStsBar(self):
        statBAR = ctk.CTkFrame(self, height=30)  #I thought this would be a cool addition.
        statBAR.pack(side="bottom", fill="x")

        self.statLabel = ctk.CTkLabel(statBAR, text="Status: Ready", anchor="w")
        self.statLabel.pack(side="left", padx=10)


    def drawDiagram(self):
        self.canvas.delete("all")
        self.classPos.clear()
        self.classRects.clear()  #clear canvas of everything
        self.relationshipLines.clear()  #clear the old relationship lines

        #calculate the max width of all classes to determine spacing
        maxWidth = 150  #default min width
        for className, classData in self.diagram.items():
            width, bruh = self.calculateClassDimensions(className, classData)
            if width > maxWidth:
                maxWidth = width

        #adjust space based on the max width
        xOffST = 50
        yOffST = 50
        xSpacing = maxWidth + 50  #base it on the widest class
        ySpacing = 150
        maxRowWDTH = 3

        for idx, (className, classData) in enumerate(self.diagram.items()):#took too much effort but it looks amazing
            x = xOffST + (idx % maxRowWDTH) * xSpacing
            y = yOffST + (idx // maxRowWDTH) * ySpacing
            width, height = self.calculateClassDimensions(className, classData)
            self.classPos[className] = (x, y)
            self.drawClass(className, x, y, width, height)

        #now to actually draw the relationships
        for className, classData in self.diagram.items():
            if "relationships" in classData:
                connections = classData["relationships"].get("connections", [])
                for connectedClass in connections:
                    if connectedClass in self.classPos:
                        self.drawRelationship(className, connectedClass)


    def calculateClassDimensions(self, className, classData):
        width = 150  #minimum width
        height = 40 + len(classData.get("Fields", {})) * 15 + len(classData.get("Methods", {})) * 20

        #calculate width based on text length to prevent overflow
        classNameLength = len(className)

        fieldLen = [len(f"+{field_name}: {field_type}") for field_name, field_type in
                         classData.get("Fields", {}).items()]  #calc max length of each field line
        maxFieldLen = max(fieldLen, default=0)  #def 0 in case empty fields

        #calc max length of each method line
        methodLen = [  #calc max length of each method line
            len(f"+{methodName}({', '.join(params)})") #join em
            for methodName, methodDetails in classData.get("Methods", {}).items()
            for params in methodDetails
        ]
        maxMethodLen = max(methodLen, default=0)  #def 0 no methods

        #calc max text length among class name fields methods
        maxTxtLen = max(classNameLength, maxFieldLen, maxMethodLen)

        if maxTxtLen * 7 > width:
            width = maxTxtLen * 10

        return width, height


    def drawClass(self, className, x0, y0, width, height):
        x1 = x0 + width
        y1 = y0 + height  #class dims
        rectID = self.canvas.create_rectangle(x0, y0, x1, y0 + 20, fill="cyan", outline="black")  #header with class name
        self.canvas.create_rectangle(x0, y0 + 20, x1, y1, fill="white", outline="black")  #box for fields and methods

        self.classRects[rectID] = className  #id
        self.canvas.create_text((x0 + x1) // 2, y0 + 10, text=className, font=("Arial", 12, "bold"))  #the actual name of the class

        #display fields and methods
        classData = self.diagram[className]
        yText = y0 + 30
        if classData.get('Fields'):
            for fieldName, fieldType in classData['Fields'].items():
                self.canvas.create_text((x0 + x1) // 2, yText, text=f"+{fieldName}: {fieldType}", font=("Arial", 10))
                yText += 15

        if classData.get('Methods'):
            for methodName, methodDetails in classData['Methods'].items():
                for params in methodDetails:
                    paramStr = ', '.join(params)
                    self.canvas.create_text((x0 + x1) // 2, yText, text=f"+{methodName}({paramStr})", font=("Arial", 10, "italic"))
                    yText += 20

    def drawRelationship(self, className1, className2):
        x1, y1 = self.classPos[className1]
        x2, y2 = self.classPos[className2]
        width1, height1 = self.calculateClassDimensions(className1, self.diagram[className1])
        width2, height2 = self.calculateClassDimensions(className2, self.diagram[className2])

        x1 += width1 // 2
        y1 += height1 // 2
        x2 += width2 // 2
        y2 += height2 // 2

        lineID = self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
        self.relationshipLines.append(lineID)


    def addClass(self):
        className = self.promptClassNM()  #pop up like one of those scam popup's on tabloid sites

        if className:
            addClass(className)  #now uses the addclass function from classes.py
            self.drawDiagram()
            self.statLabel.configure(text=f"Status: Class '{className}' added")

    def renameClass(self):
        #first prompt
        dialog = ctk.CTkInputDialog(text="Enter the existing class name:", title="Rename Class")
        existingClassName = dialog.get_input()
        if existingClassName:
            #prompt once more
            dialog = ctk.CTkInputDialog(text="Enter the new class name:", title="Rename Class")
            newClassName = dialog.get_input()

            if newClassName:
                renameClass(existingClassName, newClassName)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Class '{existingClassName}' renamed to '{newClassName}'")

    def promptClassNM(self):
        dialog = ctk.CTkInputDialog(text="Enter new class name:", title="Add Class")
        return dialog.get_input()


    def onCanvasCLK(self, event):
        clickedItems = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)

        for item in clickedItems:
            if item in self.classRects:
                className = self.classRects[item]
                self.classOptions(className) #new handler instead of just prompting to delete.
                break

    def classOptions(self, className):
        option = messagebox.askquestion("Class Options", f"What do you want to do with class '{className}'?", icon='question', type='yesnocancel', detail='Yes: Edit, No: Delete, Cancel: Cancel')

        if option == 'yes':
            self.editClass(className)

        elif option == 'no':
            #to delete or not to delete that is the question. prompts to confirm delete.
            confirm = messagebox.askyesno("Delete Class", f"Do you want to delete class '{className}'? Pretty please?")

            if confirm:

                #remove all the relationships involving the class to be deleted. basically converting a relationship into a friendzone
                for otherClass, classData in self.diagram.items():
                    if className in classData.get("relationships", {}).get("connections", []):
                        classData["relationships"]["connections"].remove(className)

                deleteClass(className)  #outsourcing to classes.py for this operation.
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Class '{className}' deleted.")

    def editClass(self, className):
        editWin = tk.Toplevel(self)
        editWin.title(f"Edit Class '{className}'")
        editWin.geometry("500x1000")


        def addFieldHandler():
            fieldName = fieldEntry.get().strip()
            fieldType = fieldTypeEntry.get().strip()

            if fieldName and fieldType:
                addField(className, fieldName, fieldType)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Field '{fieldName}' added to class '{className}'")


        def removeFieldHandler():
            fieldName = fieldRemoveEntry.get().strip()
            if fieldName:
                removeField(className, fieldName)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Field '{fieldName}' removed from class '{className}'")


        def renameFieldHandler():
            oldFieldName = fieldRenameOldEntry.get().strip()
            newFieldName = fieldRenameNewEntry.get().strip()
            if oldFieldName and newFieldName:
                renameField(className, oldFieldName, newFieldName)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Field '{oldFieldName}' renamed to '{newFieldName}' in class '{className}'")


        def addMethodHandler():
            methodName = methodEntry.get().strip()
            paramEntryGet = paramEntry.get().strip()
            params = [param.strip() for param in paramEntryGet.split(',')] if paramEntryGet else []
            if methodName:
                addMethod(className, methodName, params)  #use addMethod from methods class
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Method '{methodName}' added to class '{className}'")


        def removeMethodHandler():
            methodName = methodRemoveEntry.get().strip()
            if methodName:
                removeMethod(className, methodName)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Method '{methodName}' removed from class '{className}'")

        def addParameterHandler():
            methodName = addParamMethodEntry.get().strip() #same old same old. get and strip
            paramName = addParamNameEntry.get().strip()
            paramType = addParamTypeENT.get().strip()

            if methodName and paramName and paramType:
                addParameter(className, methodName, paramName, paramType)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Parameter '{paramName}' added to method '{methodName}' in class '{className}'")

        def removeParameterHandler():
            methodName = removeParamMethodEntry.get().strip()
            paramName = removeParamNameEntry.get().strip()
            if methodName and paramName:
                removeParameter(className, methodName, paramName)
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Parameter '{paramName}' removed from method '{methodName}' in class '{className}'")

        #fields section
        tk.Label(editWin, text="Add Field: (name and type)").pack(pady=5)
        fieldEntry = tk.Entry(editWin)
        fieldEntry.pack(pady=5)
        fieldEntry.insert(0, "field_name") #inserting placeholder text so user knows which is which
        fieldTypeEntry = tk.Entry(editWin)
        fieldTypeEntry.pack(pady=5)
        fieldTypeEntry.insert(0, "field_type")
        addFieldBTN = tk.Button(editWin, text="Add Field", command=addFieldHandler)
        addFieldBTN.pack(pady=5)

        tk.Label(editWin, text="Remove Field: (name)").pack(pady=5)
        fieldRemoveEntry = tk.Entry(editWin)
        fieldRemoveEntry.pack(pady=5)
        fieldRemoveEntry.insert(0, "field_name")
        removeFieldBTN = tk.Button(editWin, text="Remove Field", command=removeFieldHandler)
        removeFieldBTN.pack(pady=5)

        tk.Label(editWin, text="Rename Field: (old name and new name)").pack(pady=5)
        fieldRenameOldEntry = tk.Entry(editWin)
        fieldRenameOldEntry.pack(pady=5)
        fieldRenameOldEntry.insert(0, "old_field_name")
        fieldRenameNewEntry = tk.Entry(editWin)
        fieldRenameNewEntry.pack(pady=5)
        fieldRenameNewEntry.insert(0, "new_field_name")
        renameFieldBTN = tk.Button(editWin, text="Rename Field", command=renameFieldHandler)
        renameFieldBTN.pack(pady=5)

        #methods sect
        tk.Label(editWin, text="Add Method: (name and parameters)").pack(pady=5)
        methodEntry = tk.Entry(editWin)
        methodEntry.pack(pady=5)
        methodEntry.insert(0, "method_name")
        paramEntry = tk.Entry(editWin)
        paramEntry.pack(pady=5)
        paramEntry.insert(0, "param1: type1, param2: type2") #worked hard on this
        addMethodBTN = tk.Button(editWin, text="Add Method", command=addMethodHandler)
        addMethodBTN.pack(pady=5)

        tk.Label(editWin, text="Remove Method: (name)").pack(pady=5)
        methodRemoveEntry = tk.Entry(editWin)
        methodRemoveEntry.pack(pady=5)
        methodRemoveEntry.insert(0, "method_name")
        removeMethodBTN = tk.Button(editWin, text="Remove Method", command=removeMethodHandler)
        removeMethodBTN.pack(pady=5)

        #parameters section...scuffed but will do
        tk.Label(editWin, text="Add Parameter to Method: (method, parameter name, type)").pack(pady=5)
        addParamMethodEntry = tk.Entry(editWin)
        addParamMethodEntry.pack(pady=5)
        addParamMethodEntry.insert(0, "method_name") #more placeholder text to autofill.
        addParamNameEntry = tk.Entry(editWin)
        addParamNameEntry.pack(pady=5)
        addParamNameEntry.insert(0, "param_name")
        addParamTypeENT = tk.Entry(editWin)
        addParamTypeENT.pack(pady=5)
        addParamTypeENT.insert(0, "param_type")
        addParamBTN = tk.Button(editWin, text="Add Parameter", command=addParameterHandler) #call my new handler
        addParamBTN.pack(pady=5)

        #new addition. actually being able to remove parameters
        tk.Label(editWin, text="Remove Parameter from Method: (method, parameter name)").pack(pady=5) #labels
        removeParamMethodEntry = tk.Entry(editWin)
        removeParamMethodEntry.pack(pady=5)
        removeParamMethodEntry.insert(0, "method_name")
        removeParamNameEntry = tk.Entry(editWin)
        removeParamNameEntry.pack(pady=5)
        removeParamNameEntry.insert(0, "param_name")
        removeParamBTN = tk.Button(editWin, text="Remove Parameter", command=removeParameterHandler)
        removeParamBTN.pack(pady=5)

    def listClasses(self):
        classListWin = tk.Toplevel(self)
        classListWin.title("List of Classes")
        classListWin.geometry("300x400")

        tk.Label(classListWin, text="Classes:", font=("Arial", 14, "bold")).pack(pady=10)

        for className, classDetails in self.diagram.items():
            tk.Label(classListWin, text=f"{className}", font=("Arial", 12)).pack(anchor="w", padx=10)

    def addRelationship(self):
        relWin = tk.Toplevel(self)
        relWin.title("Add Relationship")
        relWin.geometry("400x200")

        tk.Label(relWin, text="Enter Source Class:").pack(pady=5)
        sourceEntry = tk.Entry(relWin)
        sourceEntry.pack(pady=5)

        tk.Label(relWin, text="Enter Destination Class:").pack(pady=5)
        destEntry = tk.Entry(relWin)
        destEntry.pack(pady=5)

        def addRelHandler():
            source = sourceEntry.get().strip()
            dest = destEntry.get().strip()

            if source and dest:
                if source == dest:
                    messagebox.showerror("Error", "Cannot create a relationship with the same class. silly.")
                    return

                if source not in self.diagram or dest not in self.diagram:
                    messagebox.showerror("Error", "One or both classes do not exist.")
                    return

                addRelationship(source, dest)  #use addRelationship
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Relationship added between '{source}' and '{dest}.'") #congratulations to the couple <3

        addRelBTN = tk.Button(relWin, text="Add Relationship", command=addRelHandler)
        addRelBTN.pack(pady=10)

    def showOverallDiagram(self):
        diagramWin = tk.Toplevel(self)
        diagramWin.title("Overall Diagram")
        diagramWin.geometry("500x500")

        diagramText = tk.Text(diagramWin, wrap=tk.WORD)
        diagramText.pack(fill="both", expand=True)

        diagramText.insert(tk.END, f"{self.diagram}")
        diagramText.config(state=tk.DISABLED)


GUI = UMLApp()
GUI.mainloop()
