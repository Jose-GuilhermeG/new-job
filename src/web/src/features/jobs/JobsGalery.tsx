import type { JobCardProtocol } from "@/types/jobTypes";
import JobsCard from "./JobCard";
import { Empty, EmptyHeader, EmptyMedia, EmptyTitle } from "@/components/ui/empty";
import { AlertCircle } from "lucide-react";

interface JobsGaleryProps{
    className? : string
    emptyMessage? : string;
    jobs : Array<JobCardProtocol>;
}

export default function JobsGalery({className ,jobs , emptyMessage = "Nenhuma Vaga encontrada"} : JobsGaleryProps){

    if(!jobs.length) return (
        <div className={`py-20 ${className}`}>
            <Empty>
                <EmptyHeader>
                    <EmptyMedia>
                        <AlertCircle className="w-10 h-10"/>
                    </EmptyMedia>
                    <EmptyTitle className="text-2xl font-semibold">
                        {emptyMessage}
                    </EmptyTitle>
                </EmptyHeader>
            </Empty>
        </div>
    )

    return (
        <div className={`flex flex-col max-h-[80vh] overflow-x-hidden overflow-y-scroll scrollbar ${className}`}>
            {jobs.map(element=>(
                <JobsCard key={element.id} {...element}/>
            ))}
        </div>
    )
}