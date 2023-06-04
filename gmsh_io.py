import h5py
from meshio import read

def gmsh2mat(gmshfile: str, matfile: str):
    # Load mesh data from GMSH file
    mesh = read(gmshfile)

    # Extract node and element data
    nodes = mesh.points
    elements = mesh.cells

    # Write data to MAT file
    with h5py.File(matfile, 'w') as matfile:
        matfile.create_dataset('p', data=nodes.T)
        matfile.create_dataset('e', data=elements.T)
