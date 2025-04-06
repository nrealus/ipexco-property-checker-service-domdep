import fs from "node:fs";
import { type PlanningModel } from "../domain/model";
import type { PlanProperty } from "../domain/plan_property";
import type { Action } from "../domain/action";

export function setupRunEnvironment(
	model: PlanningModel,
	properties: PlanProperty[],
	plan_actions: Action[],
	expFolder: string,
) {
	fs.mkdirSync(expFolder);

    const problem_init_state_path = expFolder + '/problem_init_state.json'
    fs.writeFileSync(problem_init_state_path, JSON.stringify(model))

	const problem_specifications_path = expFolder + '/problem_specifications.json'
    fs.writeFileSync(problem_specifications_path, JSON.stringify(properties))

	const plan_path = expFolder + '/plan.json'
    fs.writeFileSync(plan_path, JSON.stringify(plan_actions))

}

export function cleanUpRunEnvironment(expFolder: string) {
	fs.rmSync(expFolder, { recursive: true, force: true });
}
