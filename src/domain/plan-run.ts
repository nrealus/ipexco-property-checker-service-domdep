import type {
	PropertyCheckerRequest,
	PropertyCheckRunStatus,
} from "./service_communication";

export interface PropertyCheckRun {
	request: PropertyCheckerRequest;
	status: PropertyCheckRunStatus;
	exp_path: string;
}
