"""Support for wildcard import."""

from skfem.mesh import *
from skfem.assembly import *
from skfem.mapping import *
from skfem.element import *
from skfem.utils import *
from skfem.version import __version__


__all__ = ['Mesh',
           'Mesh2D',
           'Mesh3D',
           'MeshHex',
           'MeshLine',
           'MeshQuad',
           'MeshTet',
           'MeshTri',
           'FacetBasis',
           'Basis',
           'InteriorBasis',
           'MortarBasis',
           'asm',
           'Mapping',
           'MappingAffine',
           'MappingIsoparametric',
           'MortarPair',
           'adaptive_theta',
           'bilinear_form',
           'BilinearForm',
           'build_pc_ilu',
           'build_pc_diag',
           'condense',
           'derivative',
           'L2_projection',
           'linear_form',
           'LinearForm',
           'functional',
           'Functional',
           'rcm',
           'solve',
           'solver_direct_scipy',
           'solver_iter_pcg',
           'solver_iter_krylov',
           'Element',
           'ElementTriArgyris',
           'ElementH1',
           'ElementH2',
           'ElementHcurl',
           'ElementHdiv',
           'ElementHex1',
           'ElementTriMorley',
           'ElementTriMini',
           'ElementQuad0',
           'ElementQuad1',
           'ElementQuad2',
           'ElementQuadS2',
           'ElementQuadDG',
           'ElementQuadP',
           'ElementTetN0',
           'ElementTetP0',
           'ElementTetP1',
           'ElementTetP2',
           'ElementTetRT0',
           'ElementTriDG',
           'ElementTriP0',
           'ElementTriP1',
           'ElementTriP2',
           'ElementTriRT0',
           'ElementVectorH1',
           'ElementLineP1',
           'ElementLineP2',
           'ElementLinePp']
