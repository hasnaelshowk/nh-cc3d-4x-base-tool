from cc3d import CompuCellSetup

from cellsort_2D_variable_motilitySteppables import cellsort_2D_variable_motilitySteppable

CompuCellSetup.register_steppable(steppable=cellsort_2D_variable_motilitySteppable(frequency=1))

CompuCellSetup.run()