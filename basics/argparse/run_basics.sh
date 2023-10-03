#!/bin/bash

cmd0="python3 basics/argparse/basics.py -h"
cmd1="python3 basics/argparse/basics.py must -m must_hyphen"
cmd2="python3 basics/argparse/basics.py must -m must_hyphen
                                        --opt_arg opt
                                        -t t
                                        --int_arg 5
                                        --flag
                                        --choice choice2
                                        --list0 0 1 2 3 4
                                        --list1 255
                                        --list2 -1 -2"


echo $cmd0;eval $cmd0
echo $cmd1;eval $cmd1
echo $cmd2;eval $cmd2