from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.corner_tetrad_encoder import CornerTetradEncoder
from cubie.encoder.edge_half_turn_permutation_encoder import EdgeHalfTurnPermutationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.corner_half_turn_permutation_encoder import CornerHalfTurnPermutationEncoder
from cubie.encoder.left_right_edge_slice_encoder import LeftRightEdgeSliceEncoder
from cubie.encoder.up_down_edge_slice_encoder import UpDownEdgeSliceEncoder
from thistlethwaite.offline.pruning_table_creator import PruningTableCreator
from thistlethwaite.offline.table_saver import TableSaver
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase3.phase3 import Phase3
from thistlethwaite.phase4.phase4 import Phase4

if __name__ == '__main__':
    eo_pruning = PruningTableCreator.create(2 ** 11, EdgeOrientationEncoder.from_cubie, Phase1.ALLOWED_MOVES)
    TableSaver.save_table(eo_pruning, "eo_pruning_table")

    co_pruning = PruningTableCreator.create(3 ** 7, CornerOrientationEncoder.from_cubie, Phase2.ALLOWED_MOVES)
    TableSaver.save_table(co_pruning, "co_pruning_table")

    ud_pruning = PruningTableCreator.create(495, UpDownEdgeSliceEncoder().encode_cubie, Phase2.ALLOWED_MOVES)
    TableSaver.save_table(ud_pruning, "ud_pruning_table")

    lr_pruning = PruningTableCreator.create(70, LeftRightEdgeSliceEncoder().encode_cubie, Phase3.ALLOWED_MOVES)
    TableSaver.save_table(lr_pruning, "lr_pruning_table")

    ct_pruning = PruningTableCreator.create(70, CornerTetradEncoder().encode_cubie, Phase3.ALLOWED_MOVES)
    TableSaver.save_table(ct_pruning, "ct_pruning_table")

    cp_pruning = PruningTableCreator.create(pow(24, 2), CornerHalfTurnPermutationEncoder().encode_cubie,
                                            Phase4.ALLOWED_MOVES)
    TableSaver.save_table(cp_pruning, "cp_pruning_table")

    ep_pruning = PruningTableCreator.create(pow(24, 3), EdgeHalfTurnPermutationEncoder().encode_cubie,
                                            Phase4.ALLOWED_MOVES)
    TableSaver.save_table(ep_pruning, "ep_pruning_table")
