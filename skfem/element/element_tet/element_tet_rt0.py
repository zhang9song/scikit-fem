import numpy as np

from ..element_hdiv import ElementHdiv
from ...mesh.mesh3d import MeshTet


class ElementTetRT0(ElementHdiv):
    facet_dofs = 1
    dim = 3
    maxdeg = 1
    dofnames = ['u^n']
    doflocs = np.array([[.5, .5, .0],
                        [.5, .0, .5],
                        [.0, .5, .5],
                        [.5, .5, .5]])
    mesh_type = MeshTet

    def lbasis(self, X, i):
        x, y, z = X

        if i == 0:
            phi = np.array([x, y, z - 1.])
            dphi = 3. + 0. * x
        elif i == 1:
            phi = np.array([x, y - 1., z])
            dphi = 3. + 0. * x
        elif i == 2:
            phi = np.array([x - 1., y, z])
            dphi = 3. + 0. * x
        elif i == 3:
            phi = np.array([x, y, z])
            dphi = 3. + 0. * x
        else:
            self._index_error()

        return phi, dphi
