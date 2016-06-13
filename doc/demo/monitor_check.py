#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #########################################################################
# Copyright (c) 2015, UChicago Argonne, LLC. All rights reserved.         #
#                                                                         #
# Copyright 2015. UChicago Argonne, LLC. This software was produced       #
# under U.S. Government contract DE-AC02-06CH11357 for Argonne National   #
# Laboratory (ANL), which is operated by UChicago Argonne, LLC for the    #
# U.S. Department of Energy. The U.S. Government has rights to use,       #
# reproduce, and distribute this software.  NEITHER THE GOVERNMENT NOR    #
# UChicago Argonne, LLC MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR        #
# ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE.  If software is     #
# modified to produce derivative works, such modified software should     #
# be clearly marked, so as not to confuse it with the version available   #
# from ANL.                                                               #
#                                                                         #
# Additionally, redistribution and use in source and binary forms, with   #
# or without modification, are permitted provided that the following      #
# conditions are met:                                                     #
#                                                                         #
#     * Redistributions of source code must retain the above copyright    #
#       notice, this list of conditions and the following disclaimer.     #
#                                                                         #
#     * Redistributions in binary form must reproduce the above copyright #
#       notice, this list of conditions and the following disclaimer in   #
#       the documentation and/or other materials provided with the        #
#       distribution.                                                     #
#                                                                         #
#     * Neither the name of UChicago Argonne, LLC, Argonne National       #
#       Laboratory, ANL, the U.S. Government, nor the names of its        #
#       contributors may be used to endorse or promote products derived   #
#       from this software without specific prior written permission.     #
#                                                                         #
# THIS SOFTWARE IS PROVIDED BY UChicago Argonne, LLC AND CONTRIBUTORS     #
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT       #
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS       #
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL UChicago     #
# Argonne, LLC OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,        #
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,    #
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;        #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT      #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN       #
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE         #
# POSSIBILITY OF SUCH DAMAGE.                                             #
# #########################################################################
"""
Please make sure the installation :ref:`pre-requisite-reference-label` are met.

This example shows how to verify newly created or modified files in a monitored folder. This test
will be used if the data of the same type (i.e. "data" or "data_dark" or "data_white) is collected
in multiple files.

This example takes four mandatory and one optional command line arguments:
conf: a string defining the configuration file. If only path is defined, the name 'dqconfig_test.ini'
will be added as default
folder: the folder to monitor
type: a string defining data type being processed; i.e. 'data_dark', 'data_white' or 'data'.
num_files: an integer value specifying how many files will be processed
report_by_files: a boolean value defining how the bad indexes should be reported. If True,
the bad indexes will be sorted by files the image belongs to, and the indexes will be relative
to the files. If False, the bad indexes are reported as a list of all indexes in sequence that
did not pass quality checks.

The configuration file will have the following definitions:
'limits' - file name including path that contains dictionary of limit values that will be applied to verify quality check calculations.
           Example of limits file: doc/source/config/dqschemas/limits.json
'log_file' - defines log file. If not configured, the software will create default.log file in the working directory.
'extensions' - list of file extensions that the script will monitor for.

This test can be done at during data collection to confirm data quality
values are within acceptable range.

"""
import sys
import dquality.monitor as monitor
import argparse
import json


def main(arg):

    parser = argparse.ArgumentParser()
    parser.add_argument("cfname", help="configuration file name")
    parser.add_argument("fname", help="folder name to monitor for files")
    parser.add_argument("type", help="data type to be verified (i.e. data_dark, data_white, or data)")
    parser.add_argument("numfiles", help="number of files to monitor for")
    parser.add_argument("repbyfile", help="boolean value defining how the bad indexes should be reported.")

    args = parser.parse_args()

    conf = args.cfname
    fname = args.fname
    dtype = args.type
    num_files = args.numfiles
    report_by_file = args.repbyfile

    bad_indexes = monitor.verify(conf, fname, dtype, int(num_files), report_by_file)
    print json.dumps(bad_indexes)
    return bad_indexes


if __name__ == "__main__":
    main(sys.argv[1:])

