from vtkmodules.all import *
#Source
reader = vtkSTLReader()
reader.SetFileName("C:/Users/damhI/Downloads/vertebra.stl")
reader.Update()

#Mapper 
poly_mapper = vtkPolyDataMapper()
poly_mapper.SetInputConnection(reader.GetOutputPort())

#Actor
actor = vtkActor()
actor.SetMapper(poly_mapper)
actor.GetProperty().SetRepresentationToWireframe() 

#Renderer
renderer = vtkRenderer()
renderer.AddActor(actor)

#Render Window
renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(renderer)

#Interactor
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Initialize()

renderWindow.Render()

iren.Start()