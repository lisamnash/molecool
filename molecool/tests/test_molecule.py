"""
Unit and regression test for the molecule module.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np


def test_build_bond_list():

    coordinates = np.array(
        [
            [1, 1, 1],
            [2.4, 1, 1],
            [-0.4, 1, 1],
            [1, 1, 2.4],
            [1, 1, -0.4],
        ]
    )

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4
