import { Separator } from "@/components/ui/separator";
import type { JobCardProtocol } from "@/types/jobTypes";
import { Building2 } from "lucide-react";


export default function JobsCard({title , enterpriseName , enterpriseImage , location} : JobCardProtocol){
    return (
        <div>
            <div className="flex px-5 py-2 m-2 cursor-pointer group">
                <div className="bg-background-neutral aspect-square w-20 flex items-center justify-center text-card-foreground rounded-[5px] mx-2">
                    {enterpriseImage ? 
                        <img src={enterpriseImage} className="w-full h-full object-cover"/> : 
                        <Building2 className="w-15 h-15 group-hover:scale-105 transition-transform"/> 
                    }
                </div>
                <div>
                    <h1 className="text-2xl font-semibold text-blue-600 hover:text-blue-800">
                        {title}
                    </h1>
                    <p>
                        {enterpriseName} - ({location})
                    </p>
                </div>
            </div>
            <Separator/>
        </div>
    )
}