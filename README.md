# Syntax-Based Belief Merging with Unknown Reliability

In this repository, you can find all the code for the operators of the literature and the operators that use the reliability. You can find the code to generate datasets and run the tests on the operators. The code is in Python3. 

The code to generate the datasets is in v4/generation/gen_bel_synt.py and run the tests is in v4/generation/read_xp.py. 

The code to evaluate the reliability of the agents and the confidence of formulae is in v4/graph and v4/vote. 

The formulae and profiles used for the experiments are in v4/generation/xp/res710xp0bia.csv

The main to test a specific method is in v4/main/main_bm.py

The code of the operators that use the reliability is in v4/belms/sf*.py (with *=leximax/sum).

The code of the operators from (Konieczny, 2000) is in v4/belms/*.py with (*=mcsymm/mcintersect/mcdrastic).

The example used in Table 1 is in v4/examples/bms/exintro.txt.
