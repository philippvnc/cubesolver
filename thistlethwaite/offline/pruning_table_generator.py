from cubie.encoder.corner_orientation_encoder import CornerOrientationEncoder
from cubie.encoder.edge_orientation_encoder import EdgeOrientationEncoder
from cubie.encoder.phase_2_1_encoder import Phase21Encoder
from cubie.encoder.phase_2_2_encoder import Phase22Encoder
from cubie.encoder.phase_3_encoder import Phase3Encoder
from cubie.encoder.phase_4_1_encoder import Phase41Encoder
from cubie.encoder.phase_4_2_encoder import Phase42Encoder
from cubie.encoder.phase_4_3_encoder import Phase43Encoder
from cubie.encoder.phase_4_4_encoder import Phase44Encoder
from cubie.encoder.phase_4_5_encoder import Phase45Encoder
from thistlethwaite.offline.pruning_table_creator import PruningTableCreator
from thistlethwaite.offline.table_saver import TableSaver
from thistlethwaite.phase1.phase1 import Phase1
from thistlethwaite.phase2.phase2 import Phase2
from thistlethwaite.phase3.phase3 import Phase3
from thistlethwaite.phase4.phase4 import Phase4


def main():
    eo_pruning = PruningTableCreator.create(2 ** 11, EdgeOrientationEncoder.from_cubie, Phase1().allowed_moves)
    TableSaver.save_table(eo_pruning, "eo_pruning_table")

    co_pruning = PruningTableCreator.create(3 ** 7, CornerOrientationEncoder.from_cubie, Phase2().allowed_moves)
    TableSaver.save_table(co_pruning, "co_pruning_table")

    phase_2_1_pruning = PruningTableCreator.create(13365, Phase21Encoder().encode, Phase2().allowed_moves)
    TableSaver.save_table(phase_2_1_pruning, "phase_2_1_pruning")

    phase_2_2_pruning = PruningTableCreator.create(13365, Phase22Encoder().encode, Phase2().allowed_moves)
    TableSaver.save_table(phase_2_2_pruning, "phase_2_2_pruning")

    phase_3_pruning = PruningTableCreator.create(19600, Phase3Encoder().encode_cubie, Phase3().allowed_moves)
    TableSaver.save_table(phase_3_pruning, "phase_3_pruning_table")

    phase_4_1_pruning = PruningTableCreator.create(pow(24, 3), Phase41Encoder().encode_cubie,
                                            Phase4().allowed_moves)
    TableSaver.save_table(phase_4_1_pruning, "phase_4_1_pruning_table")

    phase_4_2_pruning = PruningTableCreator.create(pow(24, 3), Phase42Encoder().encode_cubie,
                                            Phase4().allowed_moves)
    TableSaver.save_table(phase_4_2_pruning, "phase_4_2_pruning_table")

    phase_4_3_pruning = PruningTableCreator.create(pow(24, 3), Phase43Encoder().encode_cubie,
                                            Phase4().allowed_moves)
    TableSaver.save_table(phase_4_3_pruning, "phase_4_3_pruning_table")

    phase_4_4_pruning = PruningTableCreator.create(pow(24, 3), Phase44Encoder().encode_cubie,
                                            Phase4().allowed_moves)
    TableSaver.save_table(phase_4_4_pruning, "phase_4_4_pruning_table")

    phase_4_5_pruning = PruningTableCreator.create(pow(24, 3), Phase45Encoder().encode_cubie,
                                            Phase4().allowed_moves)
    TableSaver.save_table(phase_4_5_pruning, "phase_4_5_pruning_table")

if __name__ == "__main__":
    main()