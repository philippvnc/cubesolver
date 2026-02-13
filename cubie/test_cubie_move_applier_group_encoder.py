import unittest

from algorithm.group_encoder import GroupEncoder
from constants.move import Move
from cubie.cubie_move_applier import CubieMoveApplier
from cubie.test_cubie_util import TestCubieUtil


class TestCubieMoveApplierWithGroupEncoder(unittest.TestCase):


    def test_swapping_two_edge_pieces_in_a_group_does_not_change_group_encoding(self):
        possible_edges = [e for e in range(12)]  # whole cube
        slice_edges = [0, 1]  # UR and UF
        cubie = TestCubieUtil.solved_cubie()

        # initial encoding should be 0
        _, cubie_edges = cubie
        encoder = GroupEncoder(possible_edges, slice_edges)
        encoding = encoder.encode([e for e, _ in cubie_edges])
        self.assertEqual(encoding, 0)

        # move UR to UF pos
        cubie = CubieMoveApplier.apply(cubie, Move.U)
        # move UF to UR pos
        cubie = CubieMoveApplier.apply(cubie, Move.L_)
        cubie = CubieMoveApplier.apply(cubie, Move.B2)
        cubie = CubieMoveApplier.apply(cubie, Move.R_)

        # swapped edges inside slice should be 0 too
        _, cubie_edges = cubie
        encoder = GroupEncoder(possible_edges, slice_edges)
        encoding = encoder.encode([e for e, _ in cubie_edges])
        self.assertEqual(encoding, 0)

