export type JobType = "full_time" | "part_time" | "internship";

export type JobLocation = "on_site" | "remote" | "hybrid";

export interface JobCardProtocol{
    id : number;
    enterpriseImage? : string;
    enterpriseName : string;
    title : string;
    location : JobLocation;
}