# NX 2412
# Journal created by NADOSI on Sun Feb  8 20:53:52 2026 SE Asia Standard Time
#
import math
import NXOpen
import NXOpen.Assemblies
def main(args) : 

    theSession  = NXOpen.Session.GetSession() #type: NXOpen.Session
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Object Color Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Object Color
    # ----------------------------------------------
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Object Color")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Object Color")
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = True
    
    displayModification1.ApplyToOwningParts = False
    
    displayModification1.NewColor = 186
    
    displayModification1.EndPointDisplayState = False
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT SAN PHAM 1")
    objects1[0] = component1
    displayModification1.Apply(objects1)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    displayModification1.Dispose()
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    displayModification2 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification2.ApplyToAllFaces = True
    
    displayModification2.ApplyToOwningParts = False
    
    displayModification2.EndPointDisplayState = False
    
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    objects2[0] = component1
    displayModification2.Apply(objects2)
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId5)
    
    theSession.DeleteUndoMark(markId5, "Edit Object Display")
    
    displayModification2.Dispose()
    theSession.CleanUpFacetedFacesAndEdges()
    
    # ----------------------------------------------
    #   Menu: Tools->Automation->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main(sys.argv[1:])