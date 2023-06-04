from solver.gmsh_io import gmsh2mat
from solver.geometry_conversion import class_node
from solver.derivatives import LRB2D

class ShallowWaterSolver:
    def __init__(self, gmshfile, matfile, N_D, c):
        self.gmshfile = gmshfile
        self.matfile = matfile
        self.N_D = N_D
        self.c = c
        self.Point = None
        self.WW_X = None
        self.WW_XX = None
        self.WW_Y = None
        self.WW_YY = None

    def import_geometries(self):
        gmsh2mat(self.gmshfile, self.matfile)

    def convert_geometries(self):
        with h5py.File(self.matfile, 'r') as matfile:
            p = matfile['p'][:]
            e = matfile['e'][:]

        self.IN, self.OUT, self.Point = class_node(p, e)

    def calculate_derivative_matrices(self):
        lrb2d = LRB2D(self.Point, self.IN, self.OUT, self.N_D, self.c)
        self.WW_X, self.WW_XX, self.WW_Y, self.WW_YY = lrb2d.main()

    def solve_shallow_water_equations(self):
        self.import_geometries()
        self.convert_geometries()
        self.calculate_derivative_matrices()

class ShallowWater2D:
    def __init__(self, domain_size, num_elements, time_step, final_time):
        self.domain_size = domain_size
        self.num_elements = num_elements
        self.time_step = time_step
        self.final_time = final_time
        self.gravity = None
        self.bed_slope = None
        self.viscosity = None
        self.element_size = None
        self.delta_t = None

    def define_parameters(self):
        self.gravity = 9.81
        self.bed_slope = 0.0
        self.viscosity = 0.0
        # Add any other parameters specific to your problem

    def calculate_element_size(self):
        self.element_size = self.domain_size / self.num_elements

    def calculate_time_step(self):
        self.delta_t = self.time_step

    def solve(self):
        self.define_parameters()
        self.calculate_element_size()
        self.calculate_time_step()
