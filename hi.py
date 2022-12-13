from vtkmodules.all import *

colors = vtkNamedColors()




reader = vtkDICOMImageReader()
reader.SetDirectoryName('3')
reader.Update()



iso_value = -100


surface = vtkMarchingCubes()
surface.SetInputData(reader.GetOutput())
surface.ComputeNormalsOn()
surface.SetValue(0, iso_value)


filter = vtkPolyDataConnectivityFilter()
filter.SetInputConnection(surface.GetOutputPort())
filter.SetExtractionModeToLargestRegion()

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(filter.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)

renderer = vtkRenderer()
renderer.AddActor(actor)

renwin = vtkRenderWindow()
renwin.AddRenderer(renderer)

interactor = vtkRenderWindowInteractor()

interactor.SetRenderWindow(renwin)
renwin.Render()
interactor.Initialize()
interactor.Start()