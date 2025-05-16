import os

import mala

"""
Small preprocessing script for multiple elements and (L)DOS splitting. 
"""


def preprocess(folder):
    params = mala.Parameters()

    # These are dictated by the LDOS sampling files.
    params.targets.target_type = "LDOS"
    params.targets.ldos_gridsize = [9, 10, 11, 26]
    params.targets.ldos_gridspacing_ev = [0.5, 0.5, 0.5, 0.5]
    params.targets.ldos_gridoffset_ev = [-19, -9, -4.5, 4.5]

    # This is a very minimal bispectrum descriptor setup. It should be enough
    # for testing.
    params.descriptors.descriptor_type = "Bispectrum"
    params.descriptors.bispectrum_twojmax = 6
    params.descriptors.bispectrum_cutoff = 4.0
    params.descriptors.bispectrum_element_weights = [1.0, 1.0]

    data_converter = mala.DataConverter(params)
    for i in range(0, 1):
        data_converter.add_snapshot(
            descriptor_input_type="espresso-out",
            descriptor_input_path=os.path.join(
                folder, "snapshot" + str(i), "BaO_snapshot" + str(i) + ".out"
            ),
            target_input_type=".cube",
            target_input_path=[
                os.path.join(
                    folder,
                    "snapshot" + str(i),
                    "tmp.pp00*BaO_ldos_0.cube",
                ),
                os.path.join(
                    folder,
                    "snapshot" + str(i),
                    "tmp.pp0*BaO_ldos_1.cube",
                ),
                os.path.join(
                    folder,
                    "snapshot" + str(i),
                    "tmp.pp0*BaO_ldos_2.cube",
                ),
                os.path.join(
                    folder,
                    "snapshot" + str(i),
                    "tmp.pp0*BaO_ldos_3.cube",
                ),
            ],
            target_units="1/(Ry*Bohr^3)",
            simulation_output_type="espresso-out",
            simulation_output_path=os.path.join(
                folder, "snapshot" + str(i), "BaO_snapshot" + str(i) + ".out"
            ),
        )
    data_converter.convert_snapshots(".", naming_scheme="BaO_snapshot*")


preprocess(...)
