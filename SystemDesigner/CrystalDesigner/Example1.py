import sys
from pathlib import Path


PACKAGE_PARENT = Path(__file__).resolve().parents[2]
if str(PACKAGE_PARENT) not in sys.path:
    sys.path.insert(0, str(PACKAGE_PARENT))

from SystemDesigner.CrystalDesigner.CrystalPlot import scatter_plot_crystal
from SystemDesigner.CrystalDesigner.CrystalTemplates import sc_sphere_crystal


crystal = sc_sphere_crystal(a=0.8, R=10.0, atomtype="Fe")

scatter_plot_crystal(crystal, "Simple Cubic Fe Lattice with Spherical Cut")
