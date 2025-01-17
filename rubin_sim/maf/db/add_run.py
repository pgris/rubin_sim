#!/usr/bin/env python

import argparse
from . import addRunToDatabase


def addRun():

    parser = argparse.ArgumentParser(
        description="Add a MAF run to the tracking database."
    )
    parser.add_argument("mafDir", type=str, help="Directory containing MAF outputs.")
    parser.add_argument(
        "-c", "--mafComment", type=str, default=None, help="Comment on MAF analysis."
    )
    parser.add_argument("--group", type=str, default=None, help="Opsim Group name.")
    parser.add_argument("--opsimRun", type=str, default=None, help="Opsim Run Name.")
    parser.add_argument(
        "--opsimComment", type=str, default=None, help="Comment on OpSim run."
    )
    parser.add_argument(
        "--dbFile", type=str, default="None", help="Opsim Sqlite filename"
    )
    defaultdb = "trackingDb_sqlite.db"
    parser.add_argument(
        "-t",
        "--trackingDb",
        type=str,
        default=defaultdb,
        help="Tracking database filename. Default is %s, in the current directory."
        % (defaultdb),
    )
    args = parser.parse_args()

    addRunToDatabase(
        args.mafDir,
        args.trackingDb,
        args.group,
        args.opsimRun,
        args.opsimComment,
        args.mafComment,
        args.dbFile,
    )
