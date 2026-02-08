# -*- coding: utf-8 -*-
import NXOpen
import NXOpen.Assemblies

def main():
    session = NXOpen.Session.GetSession()
    ui = NXOpen.UI.GetUI()
    lw = session.ListingWindow
    lw.Open()

    sel = ui.SelectionManager
    count = sel.GetNumSelectedObjects()

    if count == 0:
        ui.NXMessageBox.Show(
            "Clear Component Color",
            NXOpen.NXMessageBox.DialogType.Warning,
            "No component selected"
        )
        return

    disp_mod = session.DisplayManager.NewDisplayModification()

    # ⭐ ĐÚNG TÊN THUỘC TÍNH TRONG NX 2206
    disp_mod.RemoveOverrides = True
    disp_mod.ApplyToAllFaces = True
    disp_mod.ApplyToOwningParts = True

    cleared = 0

    for i in range(count):
        obj = sel.GetSelectedObject(i)

        if isinstance(obj, NXOpen.Assemblies.Component):
            disp_mod.Apply([obj])
            lw.WriteLine("Reset color override: " + obj.Name)
            cleared += 1

    disp_mod.Dispose()

    ui.NXMessageBox.Show(
        "Clear Component Color",
        NXOpen.NXMessageBox.DialogType.Information,
        "Reset color for {} component(s).".format(cleared)
    )

if __name__ == "__main__":
    main()
