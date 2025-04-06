#! /usr/bin/env python3

import sys
import os

import unified_planning.shortcuts as up
import unified_planning.model.htn as up_htn

from unified_planning.model.expression import ConstantExpression
from unified_planning.plans.hierarchical_plan import HierarchicalPlan

from parser import *
from model import *

if __name__ == "__main__":

    output_folder = os.path.abspath(".") # os.path.abspath(sys.path[0])
    output_upp_path = os.path.join(output_folder, "problem/problem.upp")
    output_plan_path = os.path.join(output_folder, "plan/plan.json")

    rust_binary_path = os.path.abspath(".") # os.path.abspath(sys.path[0])

    if sys.argv[1] == "check-properties":

        initial_state_filename = sys.argv[2] # './separated_jsons/test_instance_init_state.json'
        specifications_filename = sys.argv[3] # './separated_jsons/test_instance_specifications.json'
        plan_to_analyse_filename = sys.argv[4]
        test_pb_def = parse_problem_specs_and_init_state(initial_state_filename, specifications_filename)
        # print(test_pb_def)
        test_plan_def = parse_plan(plan_to_analyse_filename)
        assert test_plan_def is not None
        # print(test_plan_def)

        d = json.load(open(specifications_filename))
        properties = { entry['_id']: entry['definition'] for entry in d }

        satisfied_properties = check_plan_properties(
            properties,
            test_plan_def,
            { j.name: j.type for j in test_pb_def.jigs },
            { r.name: r.jigs for r in test_pb_def.racks },
            { r.name: r.size for r in test_pb_def.racks },
        )
        for prop_id in satisfied_properties:
            print(prop_id)

    else:
        print("UNKNOWN (OR NOT YET IMPLEMENTED) SUBCOMMAND {}".format(sys.argv[1]))
