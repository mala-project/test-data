# Test data for MALA

This repository contains data to test, develop and debug
[MALA](https://github.com/mala-project/mala) and MALA based runscripts. If you
plan to do machine-learning tests ("Does this network implementation work? Is
this new data loading strategy working?"), this is the right data to test with.
It is NOT production level data!

## `Be2`

Contains DFT calculation output from a
[QuantumEspresso](https://www.quantum-espresso.org/) calculation for a
beryllium cell with 2 atoms, along with input scripts and pseudopotential to
replicate this calculation. LDOS files are usually large, therefore this
reduced example samples the LDOS somewhat inaccurately, in order to reduce
storage size. The energy grid for the LDOS is 11 entries long, starting at
-5 eV with a spacing of 2.5 eV. For LDOS and descriptors, 4 snapshots are
contained. In detail, the following data files can be found:

File Name                       | Description
-|-
`recreate_data/`                | Input scripts for QE
`cubes/`                        | `.cube` files for the local density of states
`Be.pbe-n-rrkjus_psl.1.0.0.UPF` | Pseudopotential used for the QE calculation
`Be_snapshot0.dens.npy`         | Electronic density numpy array (snapshot 0)
`Be_snapshot.dens.h5`           | Electronic density (HDF5 format, see details below)
`Be_snapshot0.dos.npy`          | Density of states numpy array (snapshot 0)
`Be_snapshot0-3.out`            | Output file of QE. calculation
`Be_snapshot0-3.in.npy`         | Bispectrum descriptors numpy array
`Be_snapshot0-3.out.npy`        | Local density of states numpy array
`Be_snapshot0-3.in.h5`          | Bispectrum descriptors (HDF5 format)
`Be_snapshot0-3.out.h5`         | Local density of states (HDF5 format)
`Be_model.zip`                  | MALA trained model archive for examples and tests

### `numpy` format files

SNAP bispectrum descriptors of length 91 on `18 x 18 x 27` real space grid.

> [!NOTE]
> In the last dimension of length 94, the first 3 entries are the grid coordinates / indices (an artifact of the SNAP vector generation). **The actual features are `snap_array[..., 3:]`**.

```py
>>> np.load('Be2/Be_snapshot1.in.npy').shape
(18, 18, 27, 94)
```

LDOS (11 points) on `18 x 18 x 27` real space grid.

```py
>>> np.load('Be2/Be_snapshot1.out.npy').shape
(18, 18, 27, 11)
```

Density of states (only provided for snapshot 0):

```py
>>> np.load('Be2/Be_snapshot0.dos.npy').shape
(11,)
```

Density for snapshot 0 on a `18 x 18 x 27` real space grid. The extra dimension
can be ignored, i.e. use `d=np.load(...); d[..., -1]` to squeeze the shape to
`(18, 18, 27)`.

```py
>>> np.load('Be2/Be_snapshot0.dens.npy').shape
(18, 18, 27, 1)
```

### openPMD-based files

MALA [supports the openPMD
format](https://mala-project.github.io/mala/advanced_usage/openpmd.html), so we
also provide data in that format here.

```sh
$ h5ls -r Be_snapshot0.in.h5 | grep Dataset | sort -V
/data/0/meshes/Bispectrum/0  Dataset {18, 18, 27}
/data/0/meshes/Bispectrum/1  Dataset {18, 18, 27}
...
/data/0/meshes/Bispectrum/93 Dataset {18, 18, 27}

$ h5ls -r Be_snapshot0.out.h5 | grep Dataset | sort -V
/data/0/meshes/LDOS/0     Dataset {18, 18, 27}
/data/0/meshes/LDOS/1     Dataset {18, 18, 27}
...
/data/0/meshes/LDOS/10    Dataset {18, 18, 27}
```

For the density, the snapshot number 0 is encoded in the name
`/data/0`.

```sh
$ h5ls -r Be_snapshot.dens.h5 | grep Dataset
/data/0/meshes/Density/0 Dataset {18, 18, 27}
```

To understand the naming scheme, we can use openPMD's introspection tool:

```sh
$ openpmd-ls Be_snapshot.dens.h5
openPMD series: Be_snapshot.dens
openPMD standard: 1.1.0
openPMD extensions: 0

data author: ...
data created: 2023-05-23 15:37:18 +0200
data backend: HDF5
generating machine: unknown
generating software: MALA (version: 1.1.0)
generating software dependencies: unknown

number of iterations: 1 (groupBased)
  all iterations: 0

number of meshes: 1
  all meshes:
    Density

number of particle species: 0
```

So `/data/0/` is the openPMD iteration counter, which we use to name snapshots.
`Density/0` is one grid / array / Dataset (in hdf terms) / mesh (in openPMD
terms) of shape `18 x 18 x 27`. Multiple snapshots in one file would be called

```sh
/data/0/meshes/Density/0     Dataset {18, 18, 27}
/data/1/meshes/Density/0     Dataset {18, 18, 27}
/data/2/meshes/Density/0     Dataset {18, 18, 27}
...
```
