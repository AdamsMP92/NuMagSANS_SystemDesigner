try:
    from .AssemblyBase import assembly_base, constant, normal
    from .AssemblyBaseWriter import write_assembly_base_objects
except ImportError:
    try:
        from SystemDesigner.AssemblyBaseDesigner.AssemblyBase import assembly_base, constant, normal
        from SystemDesigner.AssemblyBaseDesigner.AssemblyBaseWriter import write_assembly_base_objects
    except ImportError:
        from AssemblyBase import assembly_base, constant, normal
        from AssemblyBaseWriter import write_assembly_base_objects


SC_SPHERE_CRYSTAL_TEMPLATE = "sc_sphere_crystal"


def gaussian_spherical_nanoparticle_base(
    R_mean,
    R_std,
    a,
    atomtype,
    name="Gaussian spherical nanoparticle base",
):
    """Create an assembly base for spherical nanoparticles with Gaussian radii.

    This template defines only the object-level crystal-template parameters. It
    does not generate object centers, rotations, or a StructData.csv file.

    Parameters
    ----------
    R_mean : float
        Mean particle radius.
    R_std : float
        Standard deviation of the particle radius.
    a : float
        Lattice constant passed to the spherical crystal template.
    atomtype : object
        Free-form atom label, for example ``"Fe"``.
    name : str, optional
        Human-readable name stored in the assembly base.

    Returns
    -------
    dict
        Assembly base dictionary for the ``sc_sphere_crystal`` template.
    """
    return assembly_base(
        ct_temps=SC_SPHERE_CRYSTAL_TEMPLATE,
        ct_temps_params=["a", "R", "atomtype"],
        param_dist_props={
            "a": constant(a),
            "R": normal(mean=R_mean, sigma=R_std),
            "atomtype": constant(atomtype),
        },
        name=name,
    )


def write_gaussian_spherical_nanoparticle_base(
    R_mean,
    R_std,
    a,
    atomtype,
    n_objects,
    output_dir,
    seed=None,
    name="Gaussian spherical nanoparticle base",
):
    """Generate and store a Gaussian spherical nanoparticle object base.

    This is the high-level template entry point. It hides the underlying
    ``sc_sphere_crystal`` template name from examples and user scripts.
    """
    return write_assembly_base_objects(
        assembly_base_data=gaussian_spherical_nanoparticle_base(
            R_mean=R_mean,
            R_std=R_std,
            a=a,
            atomtype=atomtype,
            name=name,
        ),
        template_name=SC_SPHERE_CRYSTAL_TEMPLATE,
        n_objects=n_objects,
        output_dir=output_dir,
        seed=seed,
    )
