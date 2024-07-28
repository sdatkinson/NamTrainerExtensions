# File: tweak_cab_loss.py
# Created Date: Sunday July 28th 2024
# Author: Steven Atkinson (steven@atkinson.mn)

"""
Tweaks the cab loss to make it stronger.

This can be helpful if there are still some artifacts bugging you.
"""

from nam.train import core

# Change the loss weight for MRSTFT from 0.0002 to 0.002 (10x).
#
# WARNING: this accesses a private variable in the core module. This is risky
# and means that this extension could easily break! Do things like this at your
# own risk. (Better to open an Issue and ask to make this public so that there's
# a guarantee of stability.)
#
# I do a bit of cartwheels here to try and be "safe" about it:
name = "_CAB_MRSTFT_PRE_EMPH_WEIGHT"
if not hasattr(core, name):
    print(
        f"Failed to find MRSTFT loss weight as named attribute '{name}'. Something may "
        "have changed since this extension was written."
    )
else:
    _expected_previous = 2.0e-4  # As of v0.9.0
    _previous = core._CAB_MRSTFT_PRE_EMPH_WEIGHT
    _new = 2.0e-3
    core._CAB_MRSTFT_PRE_EMPH_WEIGHT = _new
    print(f"Change cab loss from {_previous} to {_new}.")
    if _previous != _expected_previous:
        print(
            f"WARNING: Previous was not as expected ({_expected_previous}). Something "
            "else touched this?"
        )
