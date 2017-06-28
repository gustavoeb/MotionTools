# ICEFlowCreateInstanceArrayPlugin
# Initial code generated by Softimage SDK Wizard
# Executed Mon Nov 21 23:23:05 UTC-0200 2011 by Gustavo
# 
# Tip: To add a command to this plug-in, right-click in the 
# script editor and choose Tools > Add Command.
import win32com.client
from win32com.client import constants
from siutils import siut

null = None
false = 0
true = 1
xsi = Application
log = Application.LogMessage

def XSILoadPlugin( in_reg ):
	in_reg.Author = "Gustavo E Boehs"
	in_reg.Name = "MotionTools_ICEFlow"
	in_reg.Major = 1
	in_reg.Minor = 01

	in_reg.RegisterMenu(constants.siMenuTbICEParticlesCreateID,"mTools_ICEFlow_Menu",false,false)
	in_reg.RegisterCommand("mTools_PickAndGroup","mTools_PickAndGroup")
	in_reg.RegisterCommand("mTools_CreateInstanceArray","mTools_CreateInstanceArray")
	in_reg.RegisterCommand("mTools_CreatePolyIslandControl","mTools_CreatePolyIslandControl")
	in_reg.RegisterCommand("mTools_CreateSimulationFramework","mTools_CreateSimulationFramework")
	in_reg.RegisterCommand("mTools_ApplyModifier","mTools_ApplyModifier")
	in_reg.RegisterCommand("mTools_AddControlersToInstancer","mTools_AddControlersToInstancer")
	#RegistrationInsertionPoint - do not remove this line

	return true

def XSIUnloadPlugin( in_reg ):
	strPluginName = in_reg.Name
	log(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
	return true

#Register commands
def mTools_PickAndGroup_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "If supportsGrouping is true it picks as many objects as selected and groups them together"
	oCmd.Tooltip = "If supportsGrouping is true it picks as many objects as selected and groups them together"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("pickMessage",constants.siArgumentInput)
	oArgs.Add("groupName",constants.siArgumentInput)
	oArgs.Add("supportsGrouping",constants.siArgumentInput)
	return true
	
def mTools_CreateInstanceArray_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Creates an ICEtree wich instances objects along an array of points. Point distribution is controlled by Type"
	oCmd.Tooltip = "Creates an ICEtree wich instances objects along an array of points. Point distribution is controlled by Type"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("Type",constants.siArgumentInput)
	return true

def mTools_CreatePolyIslandControl_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Inits polygon island data at a given object and creates a pointcloud to control those polygon islands"
	oCmd.Tooltip = "Inits polygon island data at a given object and creates a pointcloud to control those polygon islands"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("Mode",constants.siArgumentInput)
	return true

def mTools_CreateSimulationFramework_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Creates a simulated ICEtree at a given pointcloud"
	oCmd.Tooltip = "Creates a simulated ICEtree at a given pointcloud"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("Mode",constants.siArgumentInput)
	return true
	
def mTools_ApplyModifier_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Applies a modifier to a Instancer Root node"
	oCmd.Tooltip = "Applies a modifier to a Instancer Root node"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("newModifier",constants.siArgumentInput)
	return true
	
def mTools_AddControlersToInstancer_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Creates nulls to control the instance array node"
	oCmd.Tooltip = "Creates nulls to control the instance array node"
	oCmd.ReturnValue = true

	oArgs = oCmd.Arguments
	oArgs.Add("Object",constants.siArgumentInput)
	oArgs.Add("Node",constants.siArgumentInput)
	return true

#Register main menu
def mTools_ICEFlow_Menu_Init( in_ctxt ):
	oMenu = in_ctxt.Source
	oMenu.Name = "Motion Tools"
	oHeader = oMenu.AddItem( oMenu.Name, 4)
	oHeader.SetBackgroundColor(214,206,137)
	oSub1 = oMenu.AddSubMenu("Create Instance Array");
	oSub2 = oMenu.AddSubMenu("Create Instance Array on Geom.");
	oSub3 = oMenu.AddSubMenu("Create Instances from Islands");
	oSub4 = oMenu.AddSubMenu("Modify");
	oSub5 = oMenu.AddSubMenu("Simulate");
	oSub1.AddCallbackItem("Linear", "ICEFlow_CreateInstanceArray_Callback")
	oSub1.AddCallbackItem("Grid","ICEFlow_CreateInstanceArray_Callback")
	oSub1.AddCallbackItem("Radial","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At Vertices","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At Edges","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At Polygons","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At Surface (randomly)","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At Surface (by Texture Projection) *CAUTION*","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At volume (randomly)","ICEFlow_CreateInstanceArray_Callback")
	oSub2.AddCallbackItem("At volume (voxel grid)","ICEFlow_CreateInstanceArray_Callback")
	oSub3.AddCallbackItem("Use existing Polygon Islands", "ICEFlow_CreateInstanceArray_Callback")
	oSub3.AddCallbackItem("Slice Polygons into Polygon Islands", "ICEFlow_CreateInstanceArray_Callback")
	oSub4.AddCallbackItem("Modify Transform", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Modify Color", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Modify by Linear Steps", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Modify by Harmonic Steps", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Modify with Object", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Modify over Time", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Point At", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Randomize", "ICEFlow_AddModifiers_Callback")
	oSub4.AddCallbackItem("Get Animation from Clip", "ICEFlow_AddModifiers_Callback")
	oSub5.AddCallbackItem("Simulate Always", "ICEFlow_CreateSimulation_Callback")
	oSub5.AddCallbackItem("Simulate when Triggered", "ICEFlow_CreateSimulation_Callback")
	return True

#Menu callbacks
def ICEFlow_CreateInstanceArray_Callback(in_ctxt):
	oTmp = in_ctxt.source.name
	if oTmp == "Linear": xsi.mTools_CreateInstanceArray(0)
	elif oTmp == "Grid": xsi.mTools_CreateInstanceArray(1)
	elif oTmp == "Radial": xsi.mTools_CreateInstanceArray(2)
	elif oTmp == "At Vertices": xsi.mTools_CreateInstanceArray(3)
	elif oTmp == "At Edges": xsi.mTools_CreateInstanceArray(4)
	elif oTmp == "At Polygons": xsi.mTools_CreateInstanceArray(5)
	elif oTmp == "At Surface (randomly)": xsi.mTools_CreateInstanceArray(6)
	elif oTmp == "At Surface (by Texture Projection) *CAUTION*": xsi.mTools_CreateInstanceArray(7)
	elif oTmp == "At volume (randomly)": xsi.mTools_CreateInstanceArray(8)
	elif oTmp == "At volume (voxel grid)": xsi.mTools_CreateInstanceArray(9)
	elif oTmp == "Use existing Polygon Islands": xsi.mTools_CreatePolyIslandControl(0)
	elif oTmp == "Slice Polygons into Polygon Islands": xsi.mTools_CreatePolyIslandControl(1)

def ICEFlow_AddModifiers_Callback(in_ctxt):
	oTmp = in_ctxt.source.name
	xsi.mTools_ApplyModifier(oTmp)

def ICEFlow_CreateSimulation_Callback(in_ctxt):
	oTmp = in_ctxt.source.name
	if oTmp == "Simulate Always": xsi.mTools_CreateSimulationFramework(0)
	elif oTmp == "Simulate when Triggered": xsi.mTools_CreateSimulationFramework(1)

def ICEFlow_CreateInstanceArray_Init( in_ctxt ):
	oCmd = in_ctxt.Source
	oCmd.Description = "Creates a MotionTools' Instance array "
	oCmd.Tooltip = "Creates a MotionTools' Instance array "
	oCmd.ReturnValue = true
	return true


#Command executions
def mTools_PickAndGroup_Execute(pickMessage, groupName, supportsGrouping):
	#Picks either one object, one group, or groups many objects together
	#It returns only one value, either the single object or the groups name
	#If nothing is selected it returns False
	oType = "polymsh"
	oObj = ""
	oList = []
	Loop = True
	xsi.DeselectAll()
	while oType == "polymsh" and Loop == True and oObj != None:
		rtn = xsi.PickElement("", pickMessage, pickMessage)
		oObj = rtn.Value("PickedElement")
		if supportsGrouping == False: Loop = False
		if oObj != None:
			oType = oObj.Type
			if oType != "#Group" and supportsGrouping == True:
				oList.append(str(oObj))				
	if oObj == None and len(oList) == 0: return False
	elif oType != "#Group" and len(oList) > 1:
		for i in range(len(oList)):
			xsi.AddToSelection(oList[i], "", True)
		oObj = xsi.CreateGroup(groupName, "", "")
	elif oType != "#Group" and len(oList) == 1:
		return oList[0]
	elif oType == "#Group" and supportsGrouping == False:
		log("This function does not support Groups as input.", 4)
		return False
	return oObj
	
def mTools_CreateInstanceArray_Execute( Type ):
	#Pick and Group objects for this operation
	if Type > 2:
		oCurrentSel = str(xsi.GetValue("SelectionList")).rsplit(",")
		if oCurrentSel[0] != "":
			oInputGeo = xsi.Dictionary.GetObject(oCurrentSel[0])
		else:
			log("Pick object to instance ON", 8)
			oInputGeo = xsi.mTools_PickAndGroup("Pick object to instance ON","InputGeometry", False)
			if oInputGeo == False: return False
	log("Pick objects or group to instance", 8)
	oInstanced = xsi.mTools_PickAndGroup("Pick objects or group to instance","InstancedObjects", True)
	#Creates the PointCloud and the basic nodes that are shared by any type
	oPointCloud = xsi.GetPrim("pointcloud", "InstancerObject", "", "")	
	oICEtree = str(xsi.ApplyOp("ICEtree", oPointCloud, "siNode", "", "", 0))
	xsi.AddICECompoundNode("Instancer Root", oICEtree)
	xsi.ConnectICENodes(oICEtree + ".port1", oICEtree + ".Instancer_Root.execute")
	xsi.AddICECompoundNode("Set Initial Shape and Color", oICEtree)
	xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Initial_Values", oICEtree + ".Set_Initial_Shape_and_Color.Execute")
	#Connects nodes depending on the selecet type
	if Type <= 2:
		oInstanceGenerator = xsi.AddICECompoundNode("Create Point  Array", oICEtree)
		xsi.SetValue(oICEtree + ".Create_Point__Array.Mode", Type, "")	
		xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Create_Points", oICEtree + ".Create_Point__Array.Execute")	
	elif Type == 7:
		oTriangGeom = xsi.Clone(oInputGeo, "", 1, 1, 0, 0, 1, 0, 1, "", "", "", "", "", "", "", "", "", "")
		xsi.CopyPaste(oTriangGeom, "", oInputGeo, 1)
		oInputGeo = oTriangGeom
		xsi.ToggleVisibility(oInputGeo, "", "")
		xsi.ApplyTopoOp("TriangulatePolygons", oInputGeo, "siUnspecified", "siPersistentOperation", "")
		oInstanceGenerator = xsi.AddICECompoundNode("Create Points from Texture Projection", oICEtree)
		xsi.SetValue(oICEtree + ".Create_Points_from_Texture_Projection.Reference1", str(oInputGeo), "")
		xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Create_Points", oICEtree + ".Create_Points_from_Texture_Projection.Execute")
		
	else:
		oInstanceGenerator = xsi.AddICECompoundNode("Create Point Array on Geometry", oICEtree)
		xsi.SetValue(oICEtree + ".Create_Point_Array_on_Geometry.Mode", (Type-3), "")
		xsi.SetValue(oICEtree + ".Create_Point_Array_on_Geometry.Reference", str(oInputGeo), "")
		xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Create_Points", oICEtree + ".Create_Point_Array_on_Geometry.Execute")	
	xsi.InspectObj(oInstanceGenerator)
	#If there is an instance shape, assign it
	if oInstanced != False:
		xsi.SetValue(oICEtree + ".Set_Initial_Shape_and_Color.Enabled", True, "")
		xsi.SetValue(oICEtree + ".Set_Initial_Shape_and_Color.Reference", str(oInstanced), "")

def mTools_CreatePolyIslandControl_Execute( Mode ):
	#Selecting and initing. data on geometry
	oCurrentSel = str(xsi.GetValue("SelectionList")).rsplit(",")
	if oCurrentSel[0] != "":
		oInputGeo = xsi.Dictionary.GetObject(oCurrentSel[0])
	else:
		log("Pick object", 8)
		oInputGeo = xsi.mTools_PickAndGroup("Pick object","InputGeometry", False)
		if oInputGeo == False: return False
	oGeo_ICEtree = str(xsi.ApplyOp("ICEtree", oInputGeo, "siNode", "", "", 0))
	oInitPolyIslandCompound = str(xsi.AddICECompoundNode("Initialize PolyIsland Data", oGeo_ICEtree))
	xsi.ConnectICENodes(oGeo_ICEtree + ".port1", oInitPolyIslandCompound + ".Execute")
	xsi.SetValue(oInitPolyIslandCompound + ".Mode", Mode, "")
	xsi.SetValue(oGeo_ICEtree + ".Name", "init_PolyIsland", "")
	#Creating Point Cloud and its ICEtree
	oPointCloud = str(xsi.GetPrim("pointcloud", "PolyIsland_Control", "", ""))	
	oICEtree = str(xsi.ApplyOp("ICEtree", oPointCloud, "siNode", "", "", 0))
	oPointGenerator = str(xsi.AddICECompoundNode("Create Points from Polygon Islands", oICEtree))
	oConstraint = str(xsi.AddICECompoundNode("Constraint PolyIslands to PointCloud", oICEtree))
	xsi.AddICECompoundNode("Instancer Root", oICEtree)
	xsi.ConnectICENodes(oICEtree + ".port1", oICEtree + ".Instancer_Root.execute")
	xsi.AddICECompoundNode("Set Initial Shape and Color", oICEtree)
	xsi.SetValue(oICEtree + ".Set_Initial_Shape_and_Color.Shape", 5, "")
	xsi.SetValue(oPointCloud + ".particledisplay.displaytype", 1, "")
	xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Initial_Values", oICEtree + ".Set_Initial_Shape_and_Color.Execute")
	xsi.SetValue(oPointGenerator + ".Reference", str(oInputGeo), "")
	xsi.ConnectICENodes(oICEtree + ".Instancer_Root.Create_Points", oPointGenerator + ".Execute")
	xsi.AddPortToICENode(oICEtree + ".port1", "siNodePortDataInsertionLocationAfter")
	xsi.ConnectICENodes(oICEtree + ".port2", oConstraint + ".Execute")
	xsi.SetValue(oConstraint + ".Reference", str(oInputGeo), "")

def mTools_CreateSimulationFramework_Execute( Mode ):
	oCurrentSel = str(xsi.GetValue("SelectionList")).rsplit(",")
	if len(oCurrentSel) > 1:
		log("Select only 1 point cloud at a time")
		return False
	if oCurrentSel[0] != "":
		oCurrentSel = xsi.Dictionary.GetObject(oCurrentSel[0])
		if oCurrentSel.Type != "pointcloud":
			log("Only point clouds are supported")
			return False
		else:
			oInputGeo = oCurrentSel
	else:
		oInputGeo = str(xsi.mTools_PickAndGroup("Pick point cloud to be simulated","InputGeometry", False))
	oCollisionGeo = xsi.mTools_PickAndGroup("Pick collide objects or group","Colliders", True)
	oICEtree = str(xsi.CreateSimulatedICETree(oInputGeo, "siNode", ""))
	Application.AddICECompoundNode("Simulation Root", oICEtree)
	#If particles constraint polygon islands of a certain object move the constraint to post-sim region
	oPorts = xsi.Dictionary.GetObject(str(oInputGeo) + ".pointcloud.ICEtree")
	oPorts = oPorts.InputPorts
	islandConstraint = None
	for i in oPorts:
		if i.IsConnected == True and "Constraint_PolyIslands_to_PointCloud" in str(i.ConnectedNodes[0]): islandConstraint = str(i.ConnectedNodes[0])
	if islandConstraint != None:
		islandConstraintValue = xsi.GetValue(islandConstraint + ".Reference")
		Application.DeleteObj(islandConstraint)
		xsi.AddICECompoundNode("Constraint PolyIslands to PointCloud", oICEtree)
		xsi.SetValue(oICEtree + ".Constraint_PolyIslands_to_PointCloud.Reference", islandConstraintValue, "")
		xsi.ConnectICENodes(oICEtree + ".Simulation_Root.PostSimExecute1", oICEtree + ".Constraint_PolyIslands_to_PointCloud.Execute")
	#Follow
	xsi.ConnectICENodes(oICEtree + ".port1", oICEtree + ".Simulation_Root.Execute")
	xsi.AddICECompoundNode("Add Forces", oICEtree)
	xsi.AddICECompoundNode("Gravity Force", oICEtree)
	xsi.AddICENode("$XSI_DSPRESETS\\ICENodes\\SimulateBulletRigidBodiesNode.Preset", oICEtree)
	xsi.SetValue(oICEtree + ".Gravity_Force.Gravity_Strength_and_Direction_y", -98, "")
	xsi.ConnectICENodes(oICEtree + ".Add_Forces.Force1", oICEtree + ".Gravity_Force.Force")
	if oCollisionGeo != False:
		oCollidersNode = str(xsi.AddICENode("$XSI_DSPRESETS\\ICENodes\\GetDataNode.Preset", oICEtree))
		xsi.SetValue(oCollidersNode + ".reference", str(oCollisionGeo), "")
		xsi.ConnectICENodes(oICEtree + ".SimulateBulletRigidBodiesNode.geometry1", oCollidersNode + ".value")
	if Mode == 0:
		xsi.ConnectICENodes(oICEtree + ".Simulation_Root.Forces", oICEtree + ".Add_Forces.Execute")
		xsi.ConnectICENodes(oICEtree + ".Simulation_Root.Simulate", oICEtree + ".SimulateBulletRigidBodiesNode.simulate")
	elif Mode == 1:
		xsi.AddICECompoundNode("Simple State", oICEtree)
		xsi.AddICECompoundNode("Apply Modifiers Inside Simulation", oICEtree)
		xsi.ConnectICENodes(oICEtree + ".Simulation_Root.State1", oICEtree + ".Simple_State.Execute_State")
		xsi.SetValue(oICEtree + ".Simulation_Root.Use_State_Machine", True, "")
		xsi.ConnectICENodes(oICEtree + ".Simple_State.Simulate", oICEtree + ".SimulateBulletRigidBodiesNode.simulate")
		xsi.ConnectICENodes(oICEtree + ".Simple_State.Forces", oICEtree + ".Add_Forces.Execute")
		xsi.ConnectICENodes(oICEtree + ".Simulation_Root.Execute1", oICEtree + ".Apply_Modifiers_Inside_Simulation.Execute")
		xsi.SetValue(oICEtree + ".Simple_State.State_ID", 1, "")
	xsi.InspectObj(oICEtree + ".SimulateBulletRigidBodiesNode")
	
def mTools_ApplyModifier_Execute(newModifier):
	oObj = str(xsi.GetValue("SelectionList")).rsplit(",")
	if len(oObj) >= 2:
		log("Only one object at a time.", 2)
		return False
	oObj = xsi.Dictionary.GetObject(oObj[0])
	xsi.DeselectAll()
	oICEtree = xsi.SelectObj(str(oObj) + ".pointcloud.ICEtree*")
	oICEtree = str(xsi.GetValue("SelectionList")).rsplit(",")
	oICEtree = xsi.Dictionary.GetObject(oICEtree[len(oICEtree)-1])
	Application.DeselectAll()
	oNode = xsi.SelectObj(str(oICEtree) + ".Instancer_Root*")
	oNode = str(xsi.GetValue("SelectionList")).rsplit(",")
	oNode = xsi.Dictionary.GetObject(oNode[len(oNode)-1])
	xsi.DeselectAll()
	xsi.SelectObj(oObj, "", True)
	oPorts = oNode.InputPorts
	oPorts = oPorts.Filter("","","Mod*")
	oModifier = Application.AddICECompoundNode(newModifier, oICEtree)
	xsi.InspectObj(oModifier)
	for i in reversed(range(0,oPorts.Count)):
		if i+1 == oPorts.Count and oPorts[i].IsConnected == True:
			oPort = xsi.AddPortToICENode(oPorts[i], "siNodePortDataInsertionLocationAfter")
			xsi.ConnectICENodes(oPort, str(oModifier) + ".Execute")
			return
		elif oPorts[i].IsConnected == True:
			oPort = oPorts[i+1]
			xsi.ConnectICENodes(oPort, str(oModifier) + ".Execute")
			return
		elif i == 0:
			oPort = oPorts[i]
			xsi.ConnectICENodes(oPort, str(oModifier) + ".Execute")
			return

def mTools_AddControlersToInstancer_Execute( Object, Node ):
	#sets up the nulls
	STnull = Application.GetPrim("Null", "STPoint", Object, "")
	EDNull = Application.GetPrim("Null", "EDPoint", Object, "")
	xsi.SetValue(str(STnull) + ".null.primary_icon", 2, "")
	xsi.SetValue(str(EDNull) + ".null.primary_icon", 2, "")
	xsi.MakeLocal(str(STnull) + ".display", "siDefaultPropagation")
	xsi.SetValue(str(STnull) + ".display.wirecolorg", 1, "")
	xsi.MakeLocal(str(EDNull) + ".display", "siDefaultPropagation")
	xsi.SetValue(str(EDNull) + ".display.wirecolorr", 1, "")
	#position nulls in place
	STnull.Kinematics.Global.Parameters("posx").value = xsi.GetValue(str(Node) + ".Starting_Point_x")
	STnull.Kinematics.Global.Parameters("posy").value = xsi.GetValue(str(Node) + ".Starting_Point_y")
	STnull.Kinematics.Global.Parameters("posz").value = xsi.GetValue(str(Node) + ".Starting_Point_z")
	EDNull.Kinematics.Global.Parameters("posx").value = xsi.GetValue(str(Node) + ".End_Point_x")
	EDNull.Kinematics.Global.Parameters("posy").value = xsi.GetValue(str(Node) + ".End_Point_y")
	EDNull.Kinematics.Global.Parameters("posz").value = xsi.GetValue(str(Node) + ".End_Point_z")
	#connects nulls in the ICEtree
	STnode = xsi.AddICENode("GetDataNode", "InstancerObject.pointcloud.ICEtree")
	xsi.SetValue(str(STnode) + ".reference", str(STnull), "")
	EDnode = xsi.AddICENode("GetDataNode", "InstancerObject.pointcloud.ICEtree")
	xsi.SetValue(str(EDnode) + ".reference", str(EDNull), "")
	xsi.ConnectICENodes(str(Node) + ".SP_Control_Object", str(STnode) + ".outname")
	xsi.ConnectICENodes(str(Node) + ".EP_Control_Object", str(EDnode) + ".outname")
