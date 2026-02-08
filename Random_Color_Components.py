# NX 2412
# Journal created by NADOSI on Sun Feb  8 20:53:52 2026 SE Asia Standard Time
#
import math
import random
import sys
import NXOpen
import NXOpen.Assemblies
def _collect_components(component):
    components = []
    if component is None:
        return components
    for child in component.GetChildren():
        components.append(child)
        components.extend(_collect_components(child))
    return components


def _component_from_object(obj, work_part):
    if isinstance(obj, NXOpen.Assemblies.Component):
        return obj
    if hasattr(obj, "OwningComponent") and obj.OwningComponent is not None:
        return obj.OwningComponent
    if hasattr(obj, "OwningPart") and obj.OwningPart is not None:
        root = work_part.ComponentAssembly.RootComponent
        for component in _collect_components(root):
            if component.Prototype == obj.OwningPart:
                return component
    return None


def main(args):
    the_session = NXOpen.Session.GetSession()
    work_part = the_session.Parts.Work
    ui = NXOpen.UI.GetUI()

    selection_manager = ui.SelectionManager
    selected_objects = []
    for index in range(selection_manager.GetNumSelectedObjects()):
        selected_objects.append(selection_manager.GetSelectedObject(index))

    root_component = work_part.ComponentAssembly.RootComponent
    if selected_objects:
        components = []
        for obj in selected_objects:
            component = _component_from_object(obj, work_part)
            if component is not None:
                components.append(component)
    else:
        components = _collect_components(root_component)

    if not components:
        return

    color_by_part = {}
    random.seed()
    for component in components:
        prototype = component.Prototype
        key = prototype.Tag if prototype is not None else component.Tag
        if key not in color_by_part:
            color_by_part[key] = random.randint(1, 216)

    mark_id = the_session.SetUndoMark(
        NXOpen.Session.MarkVisibility.Visible,
        "Random Color Components",
    )
    display_modification = the_session.DisplayManager.NewDisplayModification()
    display_modification.ApplyToAllFaces = True
    display_modification.ApplyToOwningParts = False
    display_modification.EndPointDisplayState = False

    for component in components:
        prototype = component.Prototype
        key = prototype.Tag if prototype is not None else component.Tag
        display_modification.NewColor = color_by_part[key]
        display_modification.Apply([component])

    the_session.UpdateManager.DoUpdate(mark_id)
    display_modification.Dispose()
    the_session.CleanUpFacetedFacesAndEdges()


if __name__ == '__main__':
    main(sys.argv[1:])
