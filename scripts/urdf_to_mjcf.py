from xacrodoc import XacroDoc

doc = XacroDoc.from_file("../ur3_onrobot_rg2_model/ur3_onrobot_rg2.urdf.xacro")

# copy all the referenced assets to the directory `assets` before conversion
# name collisions between assets with the same filename are automatically
# resolved by appending numbers as needed
doc.localize_assets("../ur3_onrobot_rg2_model/meshes")
doc.to_mjcf_file("../ur3_onrobot_rg2_model/ur3_onrobot_rg2.xml", strippath="true", meshdir="../ur3_onrobot_rg2_model/meshes")