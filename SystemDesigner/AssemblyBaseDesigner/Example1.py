from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseAnalyzer import (
    analyze_assembly_base_dataset,
    write_parameter_table,
)
from SystemDesigner.AssemblyBaseDesigner.AssemblyBasePlot import (
    plot_parameter_distributions,
)
from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseTemplates import (
    write_gaussian_spherical_nanoparticle_base,
)


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

# Generate a dilute ensemble of spherical nanoparticles with a Gaussian
# distribution of radii.
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

# Analyze the generated output.
analysis = analyze_assembly_base_dataset(OUTPUT_DIR)

parameter_table_path = write_parameter_table(
    analysis,
    f"{OUTPUT_DIR}/RealSpaceData/parameter_table.csv",
)

# Plot histograms of analyzer output.
plot_path = f"{OUTPUT_DIR}/RealSpaceData/parameter_distributions.png"
plot_parameter_distributions(
    analysis,
    output_path=plot_path,
    bins=20,
)

print(f"Wrote {summary['n_objects']} local objects to {summary['output_dir']}")
print(f"Wrote parameter table to {parameter_table_path}")
print(f"Wrote parameter plot to {plot_path}")
