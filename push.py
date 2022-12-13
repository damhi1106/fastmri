from vtkmodules.all import *

def transformPolyData(actor):
    transform = vtkTransform()
    transform.SetMatrix(actor.GetMatrix())

    fil = vtkTransformPolyDataFilter()
    fil.SetTransform(transform)
    fil.SetInputDataObject(actor.GetMapper().GetInput())
    fil.Update()

    return fil.GetOutput()

def right(obj, ev):
    print(iren.GetKeySym())
    if iren.GetKeySym() == 'Right' :
        actor.AddPosition(10, 0, 0)
        print(assembly.GetMatrix())
        renWin.Render()

def right1(obj, ev):
    print(iren.GetKeySym())
    if iren.GetKeySym() == '2' :
        sphere_actor.AddPosition(10, 0, 0)
        print(assembly.GetMatrix())
        renWin.Render()

def left(obj, ev):
    print(iren.GetKeySym())
    if iren.GetKeySym() == 'Left' :
        actor.AddPosition(-10, 0, 0)
        print(assembly.GetMatrix())
        renWin.Render()

def left1(obj, ev):
    print(iren.GetKeySym())
    if iren.GetKeySym() == '1' :
        sphere_actor.AddPosition(-10, 0, 0)
        print(assembly.GetMatrix())
        renWin.Render()

def space(obj,ev):
    if iren.GetKeySym() == 'space':
        filter=vtkBooleanOperationPolyDataFilter()
        filter.SetOperationToUnion
        filter.SetInputData(0,transformPolyData(actor))
        filter.SetInputData(1, transformPolyData(sphere_actor))
        booleanOperationMapper=vtkPolyDataMapper()
        booleanOperationMapper.SetInputConnection(filter.GetOutputPort())
        
        result_actor=vtkActor()
        result_actor.SetMapper(booleanOperationMapper)
        
        ren.AddActor(result_actor)

reader = vtkSTLReader()
reader.SetFileName("C:/Users/damhI/Downloads/vertebra.stl")
reader.Update()

polydata = reader.GetOutput()
 
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)

sphere_source = vtkSphereSource()
sphere_source.SetRadius(20)
sphere_source.SetCenter(100, 0, 0)
sphere_source.SetPhiResolution(20) 
sphere_source.Update()

sphere_mapper = vtkPolyDataMapper()
sphere_mapper.SetInputConnection(sphere_source.GetOutputPort())

sphere_actor = vtkActor()
sphere_actor.SetMapper(sphere_mapper)

ren = vtkRenderer()

renWin = vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

axis = vtkAxesActor()
axis.SetTotalLength(30, 30, 30)

axis2 = vtkAxesActor()
axis2.SetTotalLength(30, 30, 30) 

assembly = vtkAssembly()
assembly.AddPart(actor)
assembly.AddPart(axis2)

ren.AddActor(assembly)
ren.AddActor(axis)
ren.AddActor(sphere_actor)

iren.Initialize()
iren.AddObserver("KeyPressEvent", space)
iren.AddObserver("KeyPressEvent", left)
iren.AddObserver("KeyPressEvent", right)
iren.AddObserver("KeyPressEvent", left1)
iren.AddObserver("KeyPressEvent", right1)
renWin.Render()

iren.Start()