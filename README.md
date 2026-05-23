# SystemDesigner

SystemDesigner is an early-stage Python toolkit for building atomistic crystal
objects, materializing local object bases, and preparing higher-level assembly
workflows. The current design separates local crystal generation from later
global organization and from optional derived fields such as magnetization or
nuclear scattering length density.

The core idea is hierarchical:

```text
CrystalDesigner
    builds local atomistic crystal objects

AssemblyBaseDesigner
    samples crystal-template parameters
    materializes local objects to disk
    analyzes realized parameter distributions

AssemblyBaseStructurizer
    planned: place local objects in global space

AssemblyBaseMagnetizer
    planned: attach local magnetic vector fields

AssemblyBaseNucleizer
    planned: attach local nuclear SLD fields
```

## Current Status

Implemented:

- Create one- or multi-atom crystal bases as structured dictionaries.
- Repeat crystal bases in simple lattice directions.
- Apply coordinate operators such as centering and implicit cuts.
- Define crystal templates, currently including spherical simple-cubic
  nanoparticles.
- Define assembly-base parameter distributions:
  - constant
  - uniform
  - normal
  - lognormal
- Materialize sampled local objects to:

```text
RealSpaceData/
    Local_Objects/
        Object_1/
            pos.csv
            meta.csv
            atomtype.csv
        Object_2/
            ...
```

- Analyze realized template parameters from `meta.csv`.
- Plot realized parameter histograms with expected density overlays when
  distribution metadata is available.

Planned:

- `AssemblyBaseStructurizer`: generate `StructData.csv` with global object
  centers and, later, object rotations.
- `AssemblyBaseMagnetizer`: generate `MagData/Object_i/m_k.csv` with local
  `x, y, z, mx, my, mz` data.
- `AssemblyBaseNucleizer`: generate local nuclear SLD data without modifying
  the original object geometry.
- Export or simulation-builder layer that combines local object data,
  `StructData.csv`, and optional magnetic/nuclear data.

## Project Layout

```text
SystemDesigner/
    CrystalDesigner/
        CrystalBase.py
        CrystalRepeater.py
        CrystalOperator.py
        CrystalTemplates.py
        CrystalPlot.py
        Example1.py

    AssemblyBaseDesigner/
        AssemblyBase.py
        AssemblyBaseTemplates.py
        AssemblyBaseWriter.py
        AssemblyBaseAnalyzer.py
        AssemblyBasePlot.py
        Example1.py

    AssemblyBaseStructurizer/
    AssemblyBaseMagnetizer/
    AssemblyBaseNucleizer/
```

## Requirements

The code currently expects a Python environment with at least:

- `numpy`
- `matplotlib`

The project does not yet include its own `pixi.toml` or `pyproject.toml`.
During development, tests were run with an external Pixi Python environment.

## Quick Start

Run the AssemblyBaseDesigner example:

```bash
python SystemDesigner/AssemblyBaseDesigner/Example1.py
```

This generates a dilute local object base of spherical Fe nanoparticles with a
Gaussian radius distribution:

```text
AssemblyExample1/
    RealSpaceData/
        Local_Objects/
        parameter_table.csv
        parameter_distributions.png
```

The example uses:

```python
write_gaussian_spherical_nanoparticle_base(
    R_mean=10.0,
    R_std=3.0,
    a=1.0,
    atomtype="Fe",
    n_objects=500,
    output_dir="AssemblyExample1",
    seed=123,
)
```

## CrystalDesigner Example

The crystal example builds a simple-cubic Fe sphere and plots it:

```bash
python SystemDesigner/CrystalDesigner/Example1.py
```

This example opens a Matplotlib window via `plt.show()`.

## Data Model

### Local Crystal Object

Local objects are stored before any global arrangement is applied.

`pos.csv`:

```text
x,y,z
...
```

`atomtype.csv`:

```text
atom_index,atomtype
0,Fe
...
```

`meta.csv`:

```text
key,value
object_id,1
template_name,sc_sphere_crystal
n_atoms,1419
template_param.R,7.03
template_param_distribution.R.distribution,normal
template_param_distribution.R.mean,10.0
template_param_distribution.R.sigma,3.0
```

### Future Global Assembly

The planned `AssemblyBaseStructurizer` should create a separate
`StructData.csv`, for example with object centers and rotations. This keeps
local object geometry independent from global organization.

## Design Principles

- Local crystal construction and global assembly organization are separate.
- Assembly bases store sampled template parameters and materialized local
  objects, not global positions.
- Magnetic and nuclear derived data should be added in orthogonal branches
  without mutating the base geometry.
- Templates hide lower-level crystal-template details from examples and user
  scripts.

## Development Notes

- The codebase is still experimental and API names may change.
- `AssemblyBaseAnalyzer` can read both the new
  `RealSpaceData/Local_Objects` layout and legacy `RealSpaceData/Objects`
  datasets.
- `gen_structure.py` is retained as a reference script and is not part of the
  current cleaned SystemDesigner API.
