# Test data for MALA

This repository contains data to test, develop and debug [MALA](https://github.com/mala-project/mala) and MALA based runscripts.

## `Al36/`

Contains DFT calculation output from a [QuantumEspresso](https://www.quantum-espresso.org/) calculation for an aluminium cell with 36 atoms, along with input scripts and pseudopotential to replicate this calculation. In detail, the following data files can be found:

| File Name                       | Description                                                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `recreate_data/`                | Input scripts for QE                                                                                                          |
| `Al.pbe-n-rrkjus_psl.1.0.0.UPF` | Pseudopotential used for the QE calculation                                                                                   |
| `Al.pw.scf.out`                 | Output file of QE calculation                                                                                                 |
| `Al_debug_2k_nr[0-4].in.npy`    | Reduced SNAP descriptor numpy arrays for this atomic configuration. Each file contains SNAP descriptors for 2000 grid points. |
| `Al_debug_2k_nr[0-4].out.npy`   | Reduced LDOS numpy arrays for this atomic configuration. Each file contains the LDOS for 2000 grid points.                    |
| `Al_dens.npy`                   | Electronic density numpy array.                                                                                               |
| `Al_dos.npy`                    | Density of states numpy array.                                                                                                |

## `example05_data/`

Contains the saved parameters, network and input/output scaler for a run of MALA example 05. With these the correct loading of a checkpoint in MALA can be confirmed.
