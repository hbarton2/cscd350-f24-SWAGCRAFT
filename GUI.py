import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image
from controller import *
import io



class UMLApp(ctk.CTk):
    def __init__(self, exportMode=False):
        super().__init__()
        self.exportMode = exportMode
        if not self.exportMode:
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("blue")  #blue is my favorite color -cn

            #config window
            self.title("UML Diagram Application")
            self.geometry("1600x800")
            self.minsize(1600, 800)

            self.mainFRAME = ctk.CTkFrame(self)
            self.mainFRAME.pack(side="top", fill="both", expand=True)

            self.createTBOX()
            self.createDrwArea()
            self.createStsBar()
        else:
            self.canvas = tk.Canvas(self, bg="white")
            self.canvas.pack(fill="both", expand=True)


        self.diagram = controllerCopyData() #now instead using the imported diagram from diagram.py. trying to adhere to aiden's format.

        #tracking pos for class frames
        self.classPos = {}
        self.classPosManual = {}
        self.classRects = {}
        self.relationshipLines = {} #changed overall
        self.draggingClass = None
        self.draggingData = None
        self.autoOrientation = True


        if not self.exportMode:
            self.drawDiagram()


    def createTBOX(self):
        #da frame
        tboxFRAME = ctk.CTkFrame(self.mainFRAME, width=150) #updated size a lil
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

        #delete relationship button
        deleteRelationshipBTN = ctk.CTkButton(tboxFRAME, text="Delete Relationship", command=self.deleteRelationship)
        deleteRelationshipBTN.pack(padx=10, pady=5)

        #overall diagram button
        overallDiagramBTN = ctk.CTkButton(tboxFRAME, text="Overall Diagram", command=self.showOverallDiagram)
        overallDiagramBTN.pack(padx=10, pady=5)

        #undo button waiting for momento creation
        undoBTN = ctk.CTkButton(tboxFRAME, text="Undo", command=self.undo)
        undoBTN.pack(padx=10, pady=5)

        #redo button
        redoBTN = ctk.CTkButton(tboxFRAME, text="Redo", command=self.redo)
        redoBTN.pack(padx=10, pady=5)

        saveLoadBTN = ctk.CTkButton(tboxFRAME, text="Save/Load", command=self.saveLoad)  #no longer a placeholder ;)
        saveLoadBTN.pack(padx=10, pady=5)

        printScreenBTN = ctk.CTkButton(tboxFRAME, text="Print Screen", command=self.exportCanvas)
        printScreenBTN.pack(padx=10, pady=5)

    def undo(self):
        if controllerUndo():
            self.diagram = controllerCopyData()
            self.drawDiagram()
            self.statLabel.configure(text="Status: Undo operation successful")
        else:
            self.statLabel.configure(text="Status: Nothing to undo")

    def redo(self):
        if controllerRedo():
            self.diagram = controllerCopyData()
            self.drawDiagram()
            self.statLabel.configure(text="Status: Redo operation successful")
        else:
            self.statLabel.configure(text="Status: Nothing to redo")

    def deleteRelationship(self):
        """Function to call the controller to have it delete a relationship"""
        dialogue = ctk.CTkInputDialog(text="Enter the source class name:", title="Delete Relationship")
        source = dialogue.get_input().strip()

        if(source):
            dialogue = ctk.CTkInputDialog(text="Enter the destination class name:", title="Delete Relationship")
            destination = dialogue.get_input().strip()

            if(destination):
                dialogue = ctk.CTkInputDialog(text="Enter the relationship type (aggregation, composition, generalization, realization, dependency, association):", title="Delete Relationship")
                relationshipType = dialogue.get_input().strip().lower()

                validTypes = ["aggregation", "composition", "generalization", "realization", "dependency", "association"]
                if relationshipType not in validTypes:
                    self.statLabel.configure(text="Status: Invalid relationship type given")
                    return

                success = controllerDeleteRelationship(source, destination, relationshipType)  # Use controller to delete the relationship
                if(success):
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text = f"Status: Relationship between {source} and {destination} deleted")

                else:
                    self.statLabel.configure(text = f"Status: Relationship between {source} and {destination} not found")

            else:
                self.statLabel.configure(text = "Status: Destination class name is required")

        else:
            self.statLabel.configure(text = "Status: Source class name is required")

    def createDrwArea(self):
        #create area frame
        self.drawFRAME = ctk.CTkFrame(master=self.mainFRAME)
        self.drawFRAME.pack(side="right", fill="both", expand=True)

        self.canvas = tk.Canvas(self.drawFRAME, bg="white")  #drawing to canvas

        #create horizontal and vertical scrollbars
        hScroll = tk.Scrollbar(self.drawFRAME, orient="horizontal", command=self.canvas.xview)
        vScroll = tk.Scrollbar(self.drawFRAME, orient="vertical", command=self.canvas.yview)

        #config the canvas to use scroll
        self.canvas.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)

        #layout the canvas and scroll
        self.canvas.grid(row=0, column=0, sticky="nsew")
        hScroll.grid(row=1, column=0, sticky="ew")
        vScroll.grid(row=0, column=1, sticky="ns")

        #configure the grid weights to make canvas expand wooo
        self.drawFRAME.rowconfigure(0, weight=1)
        self.drawFRAME.columnconfigure(0, weight=1)

        #binding clicking to giving options for the class instead of just deleting it like my previous vers
        self.canvas.bind("<Button-1>", self.onCanvasCLK)


        self.toggleButton = ctk.CTkButton(self.drawFRAME, text="Auto Orientation: ON", command=self.toggleAutoOrientation)
        self.toggleButton.place(relx=0.0, rely=0.0, anchor='nw')


    def toggleAutoOrientation(self):
        self.autoOrientation = not self.autoOrientation #toggle
        if self.autoOrientation:
            self.toggleButton.configure(text="Auto Orientation: ON")
        else:
            self.toggleButton.configure(text="Auto Orientation: OFF")
        self.drawDiagram()


    def createStsBar(self):
        statBAR = ctk.CTkFrame(self, height=30)  #I thought this would be a cool addition.
        statBAR.pack(side="bottom", fill="x")

        self.statLabel = ctk.CTkLabel(statBAR, text="Status: Ready", anchor="w")
        self.statLabel.pack(side="left", padx=10)


    def drawDiagram(self):
        self.canvas.delete("all")
        self.classRects.clear()  #clear canvas of everything
        self.relationshipLines.clear()  #clear the old relationship lines

        if self.autoOrientation:
            #overwrite self.classPos with new positions
            self.classPosManual = self.classPos.copy()
            self.classPos.clear()

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
            maxRowWDTH = 4 #rechange for now

            for idx, (className, classData) in enumerate(self.diagram.items()):#took too much effort but it looks amazing
                x = xOffST + (idx % maxRowWDTH) * xSpacing
                y = yOffST + (idx // maxRowWDTH) * ySpacing
                width, height = self.calculateClassDimensions(className, classData)
                self.classPos[className] = (x, y)
                self.drawClass(className, x, y, width, height)

        else:
            for className in self.diagram.keys():
                if className not in self.classPosManual:
                    self.classPosManual[className] = (50 + len(self.classPosManual) * 200, 50)
            self.classPos = self.classPosManual.copy()

            for className, classData in self.diagram.items(): #positions in self.classPos
                x, y = self.classPos[className]
                width, height = self.calculateClassDimensions(className, classData)
                self.drawClass(className, x, y, width, height)

        #now to actually draw the relationships
        for className, classData in self.diagram.items():
            if "Relationships" in classData:
                for relationship in classData["Relationships"]:
                    fromClass = relationship.get("fromClass")
                    toClass = relationship.get("toClass")
                    relationType = relationship.get("relationType")
                    if fromClass and toClass and relationType:
                        if toClass in self.classPos and fromClass in self.classPos:
                            self.drawRelationship(fromClass, toClass, relationType)

        #draw color code reference in bottom right corner
        self.drawRelationshipLegend()
        #update the scroll region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def calculateClassDimensions(self, className, classData):
        width = 150  #minimum width
        methodCount = sum(len(overloads) for overloads in classData.get("Methods", {}).values()) #killed me
        height = 40 + len(classData.get("Fields", {})) * 15 + methodCount * 20

        #calculate width based on text length to prevent overflow
        classNameLength = len(className)

        fieldLen = [len(f"+{fieldNM}: {fieldTYP}") for fieldNM, fieldTYP in classData.get("Fields", {}).items()]  #calc max length of each field line
        maxFieldLen = max(fieldLen, default=0)  #def 0 in case empty fields

        #calc max length of each method line
        methodLen = [  #calc max length of each method line
            len(f"+{methodName}({', '.join(params['parameters'])}): {params.get('return_type', '')}") #join em
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
        classTag = f"class_{className}"
        rectIDHead = self.canvas.create_rectangle(x0, y0, x1, y0 + 20, fill="cyan", outline="black", tags=(classTag,))  #header with class name
        rectIDBdy = self.canvas.create_rectangle(x0, y0 + 20, x1, y1, fill="white", outline="black", tags=(classTag,))  #box for fields and methods


        self.classRects[className] = [rectIDHead, rectIDBdy] #map classTag to a list of all item IDs for class

        textIDHead = self.canvas.create_text((x0 + x1) // 2, y0 + 10, text=className, font=("Arial", 12, "bold"), tags=(classTag,))  #the actual name of the class
        self.classRects[className].append(textIDHead)

        #display fields and methods
        classData = self.diagram[className]
        yText = y0 + 30
        if classData.get('Fields'):
            for fieldName, fieldType in classData['Fields'].items():
                textIDField = self.canvas.create_text((x0 + x1) // 2, yText, text=f"+{fieldName}: {fieldType}", font=("Arial", 10), tags=(classTag,))
                self.classRects[className].append(textIDField)
                yText += 15

        if classData.get('Methods'):
            for methodName, methodDetails in classData['Methods'].items():
                for params in methodDetails:
                    paramStr = ', '.join(params["parameters"])
                    returnType = params.get("return_type", "void") #default void now
                    textIDMeth = self.canvas.create_text((x0 + x1) // 2, yText, text=f"+{methodName}({paramStr}): {returnType}", font=("Arial", 10, "italic"), tags=(classTag,)) #now adding tags for easier use
                    self.classRects[className].append(textIDMeth)
                    yText += 20


        if not self.autoOrientation: #bind events for dragging when toggle false
            self.canvas.tag_bind(classTag, "<ButtonPress-1>", self.onClassPress)
            self.canvas.tag_bind(classTag, "<B1-Motion>", self.onClassMotion)
            self.canvas.tag_bind(classTag, "<ButtonRelease-1>", self.onClassRelease)
        else:
            self.canvas.tag_unbind(classTag, "<ButtonPress-1>")
            self.canvas.tag_unbind(classTag, "<B1-Motion>")
            self.canvas.tag_unbind(classTag, "<ButtonRelease-1>")

    def drawRelationship(self, className1, className2, relType):
        relKey = (className1, className2, relType)

        #remove existing relationship lines only for this rel
        if relKey in self.relationshipLines:
            for lineID in self.relationshipLines[relKey]:
                self.canvas.delete(lineID)
            del self.relationshipLines[relKey]

        #time for some math
        x1, y1 = self.classPos[className1]
        x2, y2 = self.classPos[className2]
        width1, height1 = self.calculateClassDimensions(className1, self.diagram[className1])
        width2, height2 = self.calculateClassDimensions(className2, self.diagram[className2])


        classARect = (x1, y1, x1 + width1, y1 + height1)
        classBRect = (x2, y2, x2 + width2, y2 + height2)

        overlap = not (classARect[2] <= classBRect[0] or classARect[0] >= classBRect[2] or classARect[3] <= classBRect[1] or classARect[1] >= classBRect[3])

        if overlap:
            return

        centerX1 = x1 + width1 / 2
        centerY1 = y1 + height1 / 2
        centerX2 = x2 + width2 / 2
        centerY2 = y2 + height2 / 2

        deltaX = centerX2 - centerX1
        deltaY = centerY2 - centerY1

        if abs(deltaX) > abs(deltaY):
            if deltaX > 0:
                startPoint = (x1 + width1, centerY1)
                endPoint = (x2, centerY2)
                primaryDirection = 'horizontal'
                direction = 1
            else:
                startPoint = (x1, centerY1)
                endPoint = (x2 + width2, centerY2)
                primaryDirection = 'horizontal'
                direction = -1
        else:
            if deltaY > 0:
                startPoint = (centerX1, y1 + height1)
                endPoint = (centerX2, y2)
                primaryDirection = 'vertical'
                direction = 1
            else:
                startPoint = (centerX1, y1)
                endPoint = (centerX2, y2 + height2)
                primaryDirection = 'vertical'
                direction = -1

        currX, currY = startPoint
        endX, endY = endPoint


        lineColor = {
            "aggregation": "blue",
            "composition": "green",
            "generalization": "red",
            "realization": "orange",
            "dependency": "purple",
            "association": "pink"
        }.get(relType, "black")  #adding this to default to black in case something errors out (soft error)


        linePoints = [(currX, currY)]
        edgeOffST = 20


        if primaryDirection == 'horizontal':
            currX += direction * edgeOffST
        else:
            currY += direction * edgeOffST
        linePoints.append((currX, currY))


        if primaryDirection == 'horizontal':
            preEndX = endX - direction * edgeOffST
            preEndY = currY
        else:
            preEndX = currX
            preEndY = endY - direction * edgeOffST


        collision = False
        for otherClass in self.diagram:
            if otherClass in (className1, className2):
                continue
            otherX, otherY = self.classPos[otherClass]
            otherWidth, otherHeight = self.calculateClassDimensions(otherClass, self.diagram[otherClass])

            otherLeft = otherX
            otherRight = otherX + otherWidth
            otherTop = otherY
            otherBottom = otherY + otherHeight


            if primaryDirection == 'horizontal':

                minX = min(currX, preEndX)
                maxX = max(currX, preEndX)
                if otherTop <= currY <= otherBottom and not (otherRight < minX or otherLeft > maxX):
                    collision = True
                    break
            else:

                minY = min(currY, preEndY)
                maxY = max(currY, preEndY)
                if otherLeft <= currX <= otherRight and not (otherBottom < minY or otherTop > maxY):
                    collision = True
                    break

        if collision:

            if primaryDirection == 'horizontal':
                adjustY = -50 if currY > centerY2 else 50
                currY += adjustY
                linePoints.append((currX, currY))
            else:
                adjustX = -50 if currX > centerX2 else 50
                currX += adjustX
                linePoints.append((currX, currY))

        if primaryDirection == 'horizontal':
            currX = preEndX
            linePoints.append((currX, currY))
            if currY != endY:
                currY = endY
                linePoints.append((currX, currY))
        else:
            currY = preEndY
            linePoints.append((currX, currY))
            if currX != endX:
                currX = endX
                linePoints.append((currX, currY))

        linePoints.append((endX, endY))

        lineCoords = [coord for point in linePoints for coord in point]

        #time to draw
        lineID = self.canvas.create_line(lineCoords, fill=lineColor, width=2, arrow=tk.LAST)
        self.relationshipLines[relKey] = [lineID]

    def updateRelationships(self):
        #going to ref, delete lines
        for lineIDs in self.relationshipLines.values():
            for lineID in lineIDs:
                self.canvas.delete(lineID)


        self.relationshipLines.clear()

        for className, classData in self.diagram.items():
            if "Relationships" in classData:
                for relationship in classData["Relationships"]:
                    fromClass = relationship.get("fromClass")
                    toClass = relationship.get("toClass")
                    relationType = relationship.get("relationType")
                    if fromClass and toClass and relationType:
                        if fromClass in self.classPos and toClass in self.classPos:
                            self.drawRelationship(fromClass, toClass, relationType)

    def drawRelationshipLegend(self):
        self.update_idletasks()#added to make it load after canvas render

        #draw legend in bottom right corner
        legendRelColor = {
            "Aggregation": "blue",
            "Composition": "green",
            "Generalization": "red",
            "Realization": "orange",
            "Dependency": "purple",
            "Association": "pink"
        }

        x0 = self.canvas.winfo_width() - 250
        y0 = self.canvas.winfo_height() - 100
        y = y0  #da start y position

        for text, color in legendRelColor.items():
            self.canvas.create_line(x0, y, x0 + 20, y, fill=color, width=2, arrow=tk.LAST)
            self.canvas.create_text(x0 + 30, y, anchor="w", text=text, font=("Arial", 10))
            y += 20  #spacing next item

    def addClass(self):
        className = self.promptClassNM()  #pop up like one of those scam popup's on tabloid sites

        if className:
            success = controllerAddClass(className)

            if success:
                if not self.autoOrientation:
                    self.classPosManual[className] = (50 + len(self.classPosManual) * 200, 50)
                else:
                    pass
                self.diagram = controllerCopyData()
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Class '{className}' added")
            else:
                self.statLabel.configure(text=f"Status: Class '{className}' already exists")

    def exportCanvas(self, fileName=None):
        fileTypes = [('PNG Image', '*.png'), ('JPEG Image', '*.jpg'), ('Bitmap Image', '*.bmp')] #borrowed stuff from stackoverflow but it works. you would not believe the amount of cursing I did figuring this out:D
        if fileName is None:
            fileName = filedialog.asksaveasfilename(defaultextension='.png', filetypes=fileTypes)
        if fileName:
            self.canvas.update()
            bbox = self.canvas.bbox('all') #important: get the canvas's scroll region
            if bbox:
                x0, y0, x1, y1 = bbox
                width = x1 - x0
                height = y1 - y0
            else:
                x0 = 0
                y0 = 0
                width = self.canvas.winfo_width()
                height = self.canvas.winfo_height()

            psStuff = self.canvas.postscript(colormode='color', x=x0, y=y0, width=width, height=height)
            renderedIMG = Image.open(io.BytesIO(psStuff.encode('utf-8')))
            renderedIMG.save(fileName)
            if not self.exportMode:
                self.statLabel.configure(text=f"Status: Canvas exported to '{fileName}'")

    def renameClass(self):
        #first prompt
        dialog = ctk.CTkInputDialog(text="Enter the existing class name:", title="Rename Class")
        existingClassName = dialog.get_input()
        if existingClassName:
            #prompt once more
            dialog = ctk.CTkInputDialog(text="Enter the new class name:", title="Rename Class")
            newClassName = dialog.get_input()

            if newClassName:
                success = mainRenameClass(existingClassName, newClassName)  # Use controller to rename the class
                if success:
                    #update positions
                    if existingClassName in self.classPos:
                        self.classPos[newClassName] = self.classPos.pop(existingClassName)
                    if existingClassName in self.classPosManual:
                        self.classPosManual[newClassName] = self.classPosManual.pop(existingClassName)
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Class '{existingClassName}' renamed to '{newClassName}'")
                else:
                    self.statLabel.configure(text=f"Status: Failed to rename class '{existingClassName}'")

    def promptClassNM(self):
        dialog = ctk.CTkInputDialog(text="Enter new class name:", title="Add Class")
        return dialog.get_input()


    def onCanvasCLK(self, event): #reimplementing to fit drag implementation
        if not self.autoOrientation: #dragging is handled elsewhere
            return

        #get item under cursor
        item = self.canvas.find_withtag("current")
        if item:
            tags = self.canvas.gettags(item[0])
            for tag in tags:
                if tag.startswith("class_"):
                    className = tag[6:]
                    self.classOptions(className) #new handler instead of just prompting to delete.
                    break

    def onClassPress(self, event): #looked this up
        if not self.autoOrientation:
            item = self.canvas.find_withtag("current") #item under cursor
            if item:
                tags = self.canvas.gettags(item[0])
                for tag in tags:
                    if tag.startswith("class_"):
                        className = tag[6:]
                        break
                else:
                    className = None

                if className and className in self.classPos:
                    self.draggingClass = className
                    #record the offst between the mouse position and the item's position
                    x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
                    itemX, itemY = self.classPos[className]
                    self.draggingData = (x - itemX, y - itemY)
                    #bring item to front
                    classTag = f"class_{className}"
                    self.canvas.tag_raise(classTag)
                else:
                    self.draggingClass = None
                    self.draggingData = None
        else:
            self.draggingClass = None
            self.draggingData = None

    def onClassMotion(self, event):
        if not self.autoOrientation and self.draggingClass: #handle mouse motion event for dragging a class
            x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            if self.draggingData:
                newOffsetX, newOffsetY = self.draggingData
                #calc new pos for the class
                newx = x - newOffsetX
                newY = y - newOffsetY
                changeX = newx - self.classPos[self.draggingClass][0] #change in position for dragged class
                changeY = newY - self.classPos[self.draggingClass][1]

                className = self.draggingClass #move class items
                classTag = f"class_{className}"
                self.canvas.move(classTag, changeX, changeY)
                #update the pos in self.classPos
                self.classPos[className] = (newx, newY)
                self.classPosManual[className] = (newx, newY)

                self.updateRelationships() #refresh
        else:
            self.draggingClass = None
            self.draggingData = None

    def onClassRelease(self, event):
        #mouse release event after dragging a class rect
        self.draggingClass = None
        self.draggingData = None

    def classOptions(self, className):
        def handleOption(option):
            optionWin.destroy()
            if option == "edit":
                self.editClass(className)
            elif option == "delete":
                #to delete or not to delete that is the question. prompts to confirm delete.
                confirm = messagebox.askyesno("Delete Class", f"Do you want to delete class '{className}'?")
                if confirm:
                    success = controllerDeleteClass(className)
                    if success:
                        if className in self.classPos:
                            del self.classPos[className]
                        if className in self.classPosManual:
                            del self.classPosManual[className]
                        self.diagram = controllerCopyData()
                        self.drawDiagram()
                        self.statLabel.configure(text=f"Status: Class '{className}' deleted.")
                    else:
                        self.statLabel.configure(text=f"Status: Failed to delete class '{className}'.")

            elif option == "cancel":
                return

        #revision made to popup window. No longer a question box.
        optionWin = ctk.CTkToplevel(self)
        optionWin.title(f"Options for {className}")
        optionWin.geometry("300x170")
        label = ctk.CTkLabel(optionWin, text=f"What would you like to do with '{className}'?")
        label.pack(pady=10)

        editButton = ctk.CTkButton(optionWin, text="Edit", command=lambda: handleOption("edit"))
        editButton.pack(pady=5)
        deleteButton = ctk.CTkButton(optionWin, text="Delete", command=lambda: handleOption("delete"))
        deleteButton.pack(pady=5)
        cancelButton = ctk.CTkButton(optionWin, text="Cancel", command=lambda: handleOption("cancel"))
        cancelButton.pack(pady=5)

    def editClass(self, className): #now using CTK as I should have from the start


        def addFieldHandler():
            fieldName = fieldEntry.get().strip()
            fieldType = fieldTypeEntry.get().strip()

            if fieldName and fieldType:
                success = controllerAddField(className, fieldName, fieldType)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Field '{fieldName}' added to class '{className}'")
                else:
                    self.statLabel.configure(text=f"Status: Failed to add field '{fieldName}' to class '{className}'")


        def removeFieldHandler():
            fieldName = fieldRemoveEntry.get().strip()
            if fieldName:
                success = controllerRemoveField(className, fieldName)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Field '{fieldName}' removed from class '{className}'")
                else:
                    self.statLabel.configure(
                        text=f"Status: Failed to remove field '{fieldName}' from class '{className}'")


        def renameFieldHandler():
            oldFieldName = fieldRenameOldEntry.get().strip()
            newFieldName = fieldRenameNewEntry.get().strip()
            if oldFieldName and newFieldName:
                success = controllerRenameField(className, oldFieldName, newFieldName)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(
                        text=f"Status: Field '{oldFieldName}' renamed to '{newFieldName}' in class '{className}'")
                else:
                    self.statLabel.configure(text=f"Status: Failed to rename field '{oldFieldName}' in class '{className}'")


        def addMethodHandler():
            methodName = methodEntry.get().strip()
            paramEntryGet = paramEntry.get().strip()
            params = []
            returnType = returnTypeEntry.get().strip() or "void"

            if paramEntryGet:
                paramList = [param.strip() for param in paramEntryGet.split(',')]
                for param in paramList:
                    if ':' in param:
                        paramName, paramType = param.split(':')
                        paramName = paramName.strip()
                        paramType = paramType.strip()
                        params.append(Parameter(paramName, paramType))
                    else:
                        paramName = param.strip()
                        paramType = "void"
                        params.append(Parameter(paramName, paramType))

            if methodName:
                success = controllerAddMethod(className, methodName, returnType, params)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Method '{methodName}' added to class '{className}'")
                else:
                    self.statLabel.configure(
                        text=f"Status: Method '{methodName}' already exists in class '{className}'")
            else:
                self.statLabel.configure(text="Status: Please provide a method name.")

        def removeMethodHandler():
            methodName = methodRemoveEntry.get().strip()
            if methodName:
                success = controllerRemoveMethod(className, methodName)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Method '{methodName}' removed from class '{className}'")
                else:
                    self.statLabel.configure(
                        text=f"Status: Failed to remove method '{methodName}' from class '{className}'")

        def addParameterHandler():
            methodName = addParamMethodEntry.get().strip() #same old same old. get and strip
            paramName = addParamNameEntry.get().strip()
            paramType = addParamTypeENT.get().strip()

            if methodName and paramName and paramType:
                success = controllerAddParameter(className, methodName, paramType, paramName)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(
                        text=f"Status: Parameter '{paramName}' added to method '{methodName}' in class '{className}'")
                else:
                    self.statLabel.configure(
                        text=f"Status: Failed to add parameter '{paramName}' to method '{methodName}' in class '{className}'")
            else:
                self.statLabel.configure(text="Status: Please provide method name, parameter name, and parameter type.")

        def removeParameterHandler():
            methodName = removeParamMethodEntry.get().strip()
            paramName = removeParamNameEntry.get().strip()
            if methodName and paramName:
                success = controllerRemoveParameter(className, methodName, paramName)
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(
                        text=f"Status: Parameter '{paramName}' removed from method '{methodName}' in class '{className}'")
                else:
                    self.statLabel.configure(
                        text=f"Status: Failed to remove parameter '{paramName}' from method '{methodName}' in class '{className}'")
            else:
                self.statLabel.configure(text="Status: Please provide method name and parameter name.")

        editWin = ctk.CTkToplevel(self)
        editWin.title(f"Edit Class '{className}'")
        editWin.geometry("500x700")

        self.sectionStates = {
            "Add": True,
            "Remove": False,
            "Rename": False
        } #state track

        def toggleSection(sectionName): #logic is per toggle one collapsable should be seen at a time
            for key in self.sectionStates.keys():
                self.sectionStates[key] = False
            self.sectionStates[sectionName] = True
            updateSections()

        def updateSections():
            addFrame.pack_forget()
            removeFrame.pack_forget()
            renameFrame.pack_forget()

            if self.sectionStates["Add"]:
                addFrame.pack(fill="x", padx=10, pady=5)
                addButton.configure(text="▼ Add")
            else:
                addButton.configure(text="► Add")

            if self.sectionStates["Remove"]:
                removeFrame.pack(fill="x", padx=10, pady=5)
                removeButton.configure(text="▼ Remove")
            else:
                removeButton.configure(text="► Remove")

            if self.sectionStates["Rename"]:
                renameFrame.pack(fill="x", padx=10, pady=5)
                renameButton.configure(text="▼ Rename")
            else:
                renameButton.configure(text="► Rename")

        #full on revision time
        addButton = ctk.CTkButton(editWin, text="▼ Add", width=200, command=lambda: toggleSection("Add"))
        addButton.pack(fill="x")

        addFrame = ctk.CTkFrame(editWin)

        removeButton = ctk.CTkButton(editWin, text="► Remove", width=200, command=lambda: toggleSection("Remove"))
        removeButton.pack(fill="x")

        removeFrame = ctk.CTkFrame(editWin)

        renameButton = ctk.CTkButton(editWin, text="► Rename", width=200, command=lambda: toggleSection("Rename"))
        renameButton.pack(fill="x")

        renameFrame = ctk.CTkFrame(editWin)


        updateSections()

        #add options section
        addFieldLabel = ctk.CTkLabel(addFrame, text="Add Field: (name and type)")
        addFieldLabel.pack(pady=5)
        fieldEntry = ctk.CTkEntry(addFrame)
        fieldEntry.pack(pady=5)
        fieldEntry.insert(0, "field_name")
        fieldTypeEntry = ctk.CTkEntry(addFrame)
        fieldTypeEntry.pack(pady=5)
        fieldTypeEntry.insert(0, "field_type")
        addFieldBTN = ctk.CTkButton(addFrame, text="Add Field", command=addFieldHandler)
        addFieldBTN.pack(pady=5)

        addMethodLabel = ctk.CTkLabel(addFrame, text="Add Method: (name and parameters)")
        addMethodLabel.pack(pady=5)
        methodEntry = ctk.CTkEntry(addFrame)
        methodEntry.pack(pady=5)
        methodEntry.insert(0, "method_name")
        paramEntry = ctk.CTkEntry(addFrame)
        paramEntry.pack(pady=5)
        paramEntry.insert(0, "param1: type1, param2: type2")
        returnTypeEntry = ctk.CTkEntry(addFrame)
        returnTypeEntry.pack(pady=5)
        returnTypeEntry.insert(0, "void")
        addMethodBTN = ctk.CTkButton(addFrame, text="Add Method", command=addMethodHandler)
        addMethodBTN.pack(pady=5)

        addParamLabel = ctk.CTkLabel(addFrame, text="Add Parameter to Method: (method, parameter name, type)")
        addParamLabel.pack(pady=5)
        addParamMethodEntry = ctk.CTkEntry(addFrame)
        addParamMethodEntry.pack(pady=5)
        addParamMethodEntry.insert(0, "method_name")
        addParamNameEntry = ctk.CTkEntry(addFrame)
        addParamNameEntry.pack(pady=5)
        addParamNameEntry.insert(0, "param_name")
        addParamTypeENT = ctk.CTkEntry(addFrame)
        addParamTypeENT.pack(pady=5)
        addParamTypeENT.insert(0, "param_type")
        addParamBTN = ctk.CTkButton(addFrame, text="Add Parameter", command=addParameterHandler)
        addParamBTN.pack(pady=5)

        #remove section
        removeFieldLabel = ctk.CTkLabel(removeFrame, text="Remove Field: (name)")
        removeFieldLabel.pack(pady=5)
        fieldRemoveEntry = ctk.CTkEntry(removeFrame)
        fieldRemoveEntry.pack(pady=5)
        fieldRemoveEntry.insert(0, "field_name")
        removeFieldBTN = ctk.CTkButton(removeFrame, text="Remove Field", command=removeFieldHandler)
        removeFieldBTN.pack(pady=5)


        removeMethodLabel = ctk.CTkLabel(removeFrame, text="Remove Method: (name)")
        removeMethodLabel.pack(pady=5)
        methodRemoveEntry = ctk.CTkEntry(removeFrame)
        methodRemoveEntry.pack(pady=5)
        methodRemoveEntry.insert(0, "method_name")
        removeMethodBTN = ctk.CTkButton(removeFrame, text="Remove Method", command=removeMethodHandler)
        removeMethodBTN.pack(pady=5)

        removeParamLabel = ctk.CTkLabel(removeFrame, text="Remove Parameter from Method: (method, parameter name)")
        removeParamLabel.pack(pady=5)
        removeParamMethodEntry = ctk.CTkEntry(removeFrame)
        removeParamMethodEntry.pack(pady=5)
        removeParamMethodEntry.insert(0, "method_name")
        removeParamNameEntry = ctk.CTkEntry(removeFrame)
        removeParamNameEntry.pack(pady=5)
        removeParamNameEntry.insert(0, "param_name")
        removeParamBTN = ctk.CTkButton(removeFrame, text="Remove Parameter", command=removeParameterHandler)
        removeParamBTN.pack(pady=5)

        #rename section
        renameFieldLabel = ctk.CTkLabel(renameFrame, text="Rename Field: (old name and new name)")
        renameFieldLabel.pack(pady=5)
        fieldRenameOldEntry = ctk.CTkEntry(renameFrame)
        fieldRenameOldEntry.pack(pady=5)
        fieldRenameOldEntry.insert(0, "old_field_name")
        fieldRenameNewEntry = ctk.CTkEntry(renameFrame)
        fieldRenameNewEntry.pack(pady=5)
        fieldRenameNewEntry.insert(0, "new_field_name")
        renameFieldBTN = ctk.CTkButton(renameFrame, text="Rename Field", command=renameFieldHandler)
        renameFieldBTN.pack(pady=5)

    def listClasses(self):
        classListWin = tk.Toplevel(self)
        classListWin.title("List of Classes")
        classListWin.geometry("300x400")

        tk.Label(classListWin, text="Classes:", font=("Arial", 14, "bold")).pack(pady=10)

        for className, classDetails in self.diagram.items():
            tk.Label(classListWin, text=f"{className}", font=("Arial", 12)).pack(anchor="w", padx=10)

    def addRelationship(self):
        relWin = ctk.CTkToplevel(self)
        relWin.title("Add Relationship")
        relWin.geometry("200x500")

        ctk.CTkLabel(relWin, text="Enter Source Class:").pack(pady=5)
        sourceEntry = ctk.CTkEntry(relWin)
        sourceEntry.pack(pady=5)

        ctk.CTkLabel(relWin, text="Enter Destination Class:").pack(pady=5)
        destEntry = ctk.CTkEntry(relWin)
        destEntry.pack(pady=5)

        ctk.CTkLabel(relWin, text="Select Relationship Type:").pack(pady=10)

        def addRelHandler(relationType):
            source = sourceEntry.get().strip()
            dest = destEntry.get().strip()
            relationType = relationType.strip().lower()

            if source and dest:
                if source == dest:
                    self.statLabel.configure(text = "Error: Cannot create a relationship with the same class. silly.")
                    return

                if source not in self.diagram or dest not in self.diagram:
                    self.statLabel.configure(text = "Error: One or both classes do not exist.")
                    return

                success = controllerAddRelationship(source, dest, relationType)  # Use controller to add relationship
                if success:
                    self.diagram = controllerCopyData()
                    self.drawDiagram()
                    self.statLabel.configure(text=f"Status: Relationship '{relationType}' added between '{source}' and '{dest}'.") #I made a small change in how it is said, as saying it out loud it felt improper
                    relWin.destroy()
                else:
                    self.statLabel.configure(text=f"Status: Failed to add relationship between '{source}' and '{dest}'.")
            else:
                self.statLabel.configure(text="Status: Please enter both source and destination classes.")


        buttonFrame = ctk.CTkFrame(relWin)
        buttonFrame.pack(pady=10)

        aggregationButton = ctk.CTkButton(buttonFrame, text="Aggregation", command=lambda: addRelHandler("aggregation"))
        aggregationButton.pack(pady=5)

        compositionButton = ctk.CTkButton(buttonFrame, text="Composition", command=lambda: addRelHandler("composition"))
        compositionButton.pack(pady=5)

        generalizationButton = ctk.CTkButton(buttonFrame, text="Generalization", command=lambda: addRelHandler("generalization"))
        generalizationButton.pack(pady=5)

        realizationButton = ctk.CTkButton(buttonFrame, text="Realization", command=lambda: addRelHandler("realization"))
        realizationButton.pack(pady=5)
        realizationButton = ctk.CTkButton(buttonFrame, text="Dependency", command=lambda: addRelHandler("dependency"))
        realizationButton.pack(pady=5)
        realizationButton = ctk.CTkButton(buttonFrame, text="Association", command=lambda: addRelHandler("association"))
        realizationButton.pack(pady=5)



        cancelButton = ctk.CTkButton(relWin, text="Cancel", command=relWin.destroy)
        cancelButton.pack(pady=10)

    def showOverallDiagram(self):
        diagramWin = tk.Toplevel(self)
        diagramWin.title("Overall Diagram")
        diagramWin.geometry("500x500")

        diagramText = tk.Text(diagramWin, wrap=tk.WORD)
        diagramText.pack(fill="both", expand=True)

        diagramText.insert(tk.END, f"{self.diagram}")
        diagramText.config(state=tk.DISABLED)

    def saveLoad(self):
        #create a new dialog for save/load actions
        dialogWin = tk.Toplevel(self)
        dialogWin.title("Save or Load Diagram")
        dialogWin.geometry("400x280")

        #entry field for the file name. All this drive to use customtkinter and I've been neglecting to use it for parts
        fileLbl = ctk.CTkLabel(dialogWin, text="Enter file name (optional):", text_color="black")
        fileLbl.pack(pady=5)

        fileEntry = ctk.CTkEntry(dialogWin)
        fileEntry.pack(pady=5)

        #checkbox to decide whether to save positions
        savePositionsVar = tk.BooleanVar(value=False)
        savePositionsCheckbox = ctk.CTkCheckBox(dialogWin, text="Save Positions", variable=savePositionsVar, text_color="black")
        savePositionsCheckbox.pack(pady=5)
        loadPositionsVar = tk.BooleanVar(value=False)
        loadPositionsCheckbox = ctk.CTkCheckBox(dialogWin, text="Load Positions", variable=loadPositionsVar, text_color="black")
        loadPositionsCheckbox.pack(pady=5)

        #handler for save action
        def saveHandler():
            fileName = fileEntry.get().strip() or "data.json"  #default to data.json if empty
            savePositions = savePositionsVar.get()
            positions = self.classPosManual if savePositions else None
            if controllerSave(fileName, positions):  #call save function
                self.statLabel.configure(text=f"Status: The diagram was saved as '{fileName}'")
            else:
                self.statLabel.configure(text="Status: Error when saving diagram")
            dialogWin.destroy()  #close the dialog

        #handler for load action
        def loadHandler():
            fileName = fileEntry.get().strip() or "data.json"  #default to data.json if empty
            loadPositions = loadPositionsVar.get()
            if loadPositions:
                success, positions = controllerLoad(fileName, return_positions=True)
            else:
                success = controllerLoad(fileName)
                positions = None

            if success: #call load function
                self.diagram = controllerCopyData()
                if loadPositions and positions: #update GUI with loaded data
                    self.classPosManual = positions
                    self.autoOrientation = False  #switch to manual mode to reflect loaded positions
                    self.toggleButton.configure(text="Auto Orientation: OFF")
                self.drawDiagram()
                self.statLabel.configure(text=f"Status: Diagram loaded from '{fileName}'")
            else:
                self.statLabel.configure(text="Status: Error loading diagram")
            dialogWin.destroy()  #close the dialog. I am become death. Destroyer of worlds

        #buttons for save load and cancel
        saveBtn = ctk.CTkButton(dialogWin, text="Save", command=saveHandler)
        saveBtn.pack(pady=5)

        loadBtn = ctk.CTkButton(dialogWin, text="Load", command=loadHandler)
        loadBtn.pack(pady=5)

        cancelBtn = ctk.CTkButton(dialogWin, text="Cancel", command=dialogWin.destroy)
        cancelBtn.pack(pady=5)


def startGUI():
    GUI = UMLApp()
    GUI.mainloop()


def exportDiagramImage(filename=None):
    app = UMLApp(exportMode=True)
    app.withdraw()
    app.update()
    app.drawDiagram()
    app.exportCanvas(filename=filename)
    app.destroy()
