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

| File Name                       | Description                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `recreate_data/`                | Input scripts for QE                                                                                                          |
| `cubes/`                        | .cube files for the local density of states                                                                                   |
| `Be.pbe-n-rrkjus_psl.1.0.0.UPF` | Pseudopotential used for the QE calculation                                                                                   |
| `Be_snapshot0-3.out`                 | Output file of QE. calculation                                                                                                |
| `Be_snapshot0.dens.npy`                   | Electronic density numpy array.                                                                                               |
| `Be_snapshot0.dos.npy`                    | Density of states numpy array.                                                                                                |
| `Be_snapshot0-3.out.npy`                   | Local density of states numpy array.                                                                                          |
| `Be_snapshot0-3.in.npy`                   | Bispectrum descriptors numpy array.                                                                                          |

The `.npy` arrays have the following shapes:

```py
>>> np.load('Be2/Be_snapshot0.dos.npy').shape
(11,)
´>>> np.load('Be2/Be_snapshot0.dens.npy').shape
(18, 18, 27, 1)
>>> np.load('Be2/Be_snapshot1.in.npy').shape
(18, 18, 27, 94)
>>> np.load('Be2/Be_snapshot1.out.npy').shape
(18, 18, 27, 11)
```

## `workflow_test/`

Contains the saved parameters, network and input/output scaler for a run of
MALA example 01. With these the correct loading of a checkpoint in MALA can be
confirmed, i.e. the workflow can be checked.
