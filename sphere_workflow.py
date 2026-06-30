from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseAnalyzer import (
    analyze_assembly_base_dataset,
    write_parameter_table,
)
from SystemDesigner.AssemblyBaseDesigner.AssemblyBasePlot import (
    plot_parameter_distributions,
)
from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseTemplates import (
    write_monodisperse_spherical_nanoparticle_base,
)
from SystemDesigner.AssemblyBaseMagnetizer.AssemblyBaseMagnetizer import (
    write_spherical_magnetization_data,
)
from SystemDesigner.AssemblyBaseMagnetizer.MagnetizationBaseTemplates import (
    spherical_vortex_magnetization_base,
)



OUTPUT_DIR = "AssemblyExample1"

# Generate a dilute ensemble of spherical nanoparticles with a monodisperse
# distribution of radii.
summary = write_monodisperse_spherical_nanoparticle_base(
    R=10.0,
    a=1.0,
    atomtype="Fe",
    n_objects=500,
    output_dir=OUTPUT_DIR,
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

# Materialize a local spherical vortex magnetization field on the generated
# local objects. The resulting files are written without headers and with
# space-separated columns:
#
#     RealSpaceData/LocalMagData/Object_1/m_1.csv
#     RealSpaceData/LocalMagData/Object_2/m_1.csv
#     ...
mag_summary = write_spherical_magnetization_data(
    assembly_dir=OUTPUT_DIR,
    magnetization_base_data=spherical_vortex_magnetization_base(
        kappa=1.0,
        profile_type="linear",
        xi_type="cylindrical_xi",
        turns=1.0,
    ),
    output_file="m_1.csv",
)
