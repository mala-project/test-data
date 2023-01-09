# Test data for MALA


This repository contains data to test, develop and debug
[MALA](https://github.com/mala-project/mala) and MALA based runscripts. If you
plan to do machine-learning tests ("Does this network implementation work? Is
this new data loading strategy working?"), you can use either Al36 or Be2 data.
If you plan to actually calculate physical quantities (total energy, band
energy, forces, etc.), please use Be2, since only for Be2 a full simulation
cell is captured (see below). The Al36 data is smaller (x4), making it better
suited for small tests.

## Array shapes

For all arrays with dimension > 1, such as SNAP descriptor arrays like

```py
>>> np.load('Al36/Al_debug_2k_nr0.in.npy').shape
(100, 20, 1, 94)
```

the first 3 dimensions represent a grid within the (super)cell. In the last
dimension of length 94, the first 3 entries are the grid coordinates / indices
(an artifact of the SNAP vector generation). **The actual features
are `snap_array[..., 3:]`**.


## `Al36/`

Contains DFT calculation output from a
[QuantumEspresso](https://www.quantum-espresso.org/) calculation for an
aluminium cell with 36 atoms, along with input scripts and pseudopotential to
replicate this calculation. Please note that the LDOS and SNAP descriptors for
this example DO NOT cover the full simulation cell. To provide a minimal data
for debugging, each .in/out.npy contains 2000 data points carved from a cell
containing ~1 million points. Therefore no meaningful physical results can be
taken from this data. The 200x10x1 chunks of data were carved out one after
another from the 108x108x100 full cell, starting at position (0,0,0), leading
to 5 reduced "snapshots" (number 0 to 4). The energy grid for the LDOS is 250
entries long, starting at -10 eV with a spacing of 0.1 eV. In detail, the
following data files can be found:

| File Name                       | Description                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `recreate_data/`                | Input scripts for QE                                                                                                          |
| `Al.pbe-n-rrkjus_psl.1.0.0.UPF` | Pseudopotential used for the QE calculation                                                                                   |
| `Al.pw.scf.out`                 | Output file of QE. calculation                                                                                                |
| `Al_debug_2k_nr[0-4].in.npy`    | Reduced SNAP descriptor numpy arrays for this atomic configuration. Each file contains SNAP descriptors for 2000 grid points. |
| `Al_debug_2k_nr[0-4].out.npy`   | Reduced LDOS numpy arrays for this atomic configuration. Each file contains the LDOS for 2000 grid points.                    |
| `Al_dens.npy`                   | Electronic density numpy array.                                                                                               |
| `Al_dos.npy`                    | Density of states numpy array.                                                                                                |

The `.npy` arrays have the following shapes:

```py
>>> np.load('Al36/Al_dos.npy').shape
(250,)
>>> np.load('Al36/Al_dens.npy').shape
(108, 108, 100)
>>> np.load('Al36/Al_debug_2k_nr0.in.npy').shape
(100, 20, 1, 94)
>>> np.load('Al36/Al_debug_2k_nr0.out.npy').shape
(100, 20, 1, 250)
```

with SNAP descriptor (length 94) grids in each `Al_debug_2k_nr[0-4]*` file of
100 x 20 x 1 (1-dimensional slices).

## `Be2`

Contains DFT calculation output from a
[QuantumEspresso](https://www.quantum-espresso.org/) calculation for a
beryllium cell with 2 atoms, along with input scripts and pseudopotential to
replicate this calculation. In comparison to Al36, which is larger in size and
allows for more physically correct tests, this is a very minimal example. LDOS
files are usually large, therefore this reduced example samples the LDOS
somewhat inaccurately, in order to reduce storage size. The energy grid for the
LDOS is 11 entries long, starting at -5 eV with a spacing of 2.5 eV. In detail,
the following data files can be found:

| File Name                       | Description                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `recreate_data/`                | Input scripts for QE                                                                                                          |
| `cubes/`                        | .cube files for the local density of states                                                                                   |
| `training_data/`                | Additional, reduced training data to train networks on Beryllium. Slightly larger then the reduced Al data, so debugging might be slower, but the LDOS are complete and can be integrated correctly.|
| `Be.pbe-n-rrkjus_psl.1.0.0.UPF` | Pseudopotential used for the QE calculation                                                                                   |
| `Be.pw.scf.out`                 | Output file of QE. calculation                                                                                                |
| `Be_dens.npy`                   | Electronic density numpy array.                                                                                               |
| `Be_dos.npy`                    | Density of states numpy array.                                                                                                |
| `Be_ldos.npy`                   | Local density of states numpy array.                                                                                          |

The `.npy` arrays have the following shapes:

```py
>>> np.load('Be2/Be_dos.npy').shape
(11,)
>>> np.load('Be2/Be_ldos.npy').shape
(18, 18, 27, 11)
>>> np.load('Be2/Be_dens.npy').shape
(18, 18, 27)
>>> np.load('Be2/training_data/Be_snapshot1.in.npy').shape
(18, 18, 27, 94)
>>> np.load('Be2/training_data/Be_snapshot1.out.npy').shape
(18, 18, 27, 11)
```

with a SNAP descriptor (length 94) grid of `18 x 18 x 27`.

### Density data for GP tests

Reduced inputs with 2 features (5 minus first 3 lammps grid index)

```py
>>> np.load("Be2/densities_gp/inputs_snap/snapshot0.in.npy").shape
(18, 18, 27, 5)
```

Inputs with "optimized" set of SNAP features (55)

```py
>>> np.load("Be2/densities_gp/inputs_snap/optimized_snapshot0.in.npy").shape
(18, 18, 27, 58)
```

We can also use the non-reduced normal 91 feature SNAPs from
`Be2/training_data/Be_snapshot*.in.npy`, where numbers map to each other, e.g.
`Be2/training_data/Be_snapshot1.in.npy` -- `Be2/densities_gp/outputs_density/snapshot1.out.npy`.

The density arrays have an extra 4th dimension of length 1, compared to
`Be2/Be_dens.npy`.

```py
>>> np.load("Be2/densities_gp/outputs_density/snapshot0.out.npy").shape
(18, 18, 27, 1)
```


## `workflow_test/`

Contains the saved parameters, network and input/output scaler for a run of
MALA example 05. With these the correct loading of a checkpoint in MALA can be
confirmed, i.e. the workflow can be checked.
