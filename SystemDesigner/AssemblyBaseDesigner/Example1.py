import sys
from pathlib import Path


PACKAGE_PARENT = Path(__file__).resolve().parents[2]
if str(PACKAGE_PARENT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_PARENT))

from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseAnalyzer import analyze_assembly_base_dataset, write_parameter_table
from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseTemplates import write_gaussian_spherical_nanoparticle_base
from SystemDesigner.AssemblyBaseDesigner.AssemblyBasePlot import plot_parameter_distributions

# Example 1:
# Generate a dilute object set made from spherical Fe nanoparticle templates.
#
# This example only creates the local object geometries:
#
#     RealSpaceData/Local_Objects/Object_1/pos.csv
#     RealSpaceData/Local_Objects/Object_1/meta.csv
#     ...
#
# It does not yet define object-center positions or rotations. That later
# organization step belongs to AssemblyBaseOrganizer and can write StructData.csv.
# After generation, the realized template-parameter distributions are extracted
# from the Object_i/meta.csv files and plotted.

N_OBJECTS = 500
R_MEAN = 10.0
R_STD = 3.0
LATTICE_CONSTANT = 1.0
ATOMTYPE = "Fe"
SEED = 123
OUTPUT_DIR = "AssemblyExample1"

# generates a dilute ensemble of spherical nanoparticles with 
# a gaussian distribution of radii
summary = write_gaussian_spherical_nanoparticle_base(
    R_mean=R_MEAN,
    R_std=R_STD,
    a=LATTICE_CONSTANT,
    atomtype=ATOMTYPE,
    n_objects=N_OBJECTS,
    output_dir=OUTPUT_DIR,
    seed=SEED,
    name="dilute spherical Fe nanoparticles",
)

# analyze the generated output 
analysis = analyze_assembly_base_dataset(OUTPUT_DIR)


parameter_table_path = write_parameter_table(
    analysis,
    f"{OUTPUT_DIR}/RealSpaceData/parameter_table.csv",
)
 
# plot histograms of analyzer output
plot_path = f"{OUTPUT_DIR}/RealSpaceData/parameter_distributions.png"
plot_parameter_distributions(
    analysis,
    output_path=plot_path,
    bins=20,
)
 
