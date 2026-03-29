import JobsGalery from "@/features/jobs/JobsGalery"
import Footer from "@/layout/Footer"
import Header from "@/layout/Header"
import type { IconLink } from "@/types/gerelaTypes"
import type { JobCardProtocol } from "@/types/jobTypes"
import { User , BriefcaseBusiness, ArrowDown, Check } from "lucide-react"

export default function Home() {
  const links : Array<IconLink> = [
    {icon : <BriefcaseBusiness/> , link : ""},
    {icon : <User/> , link : ""},
  ]

  const jobs : Array<JobCardProtocol> = [
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
    {id : 1 , title : "teste de vaga" , location : "on_site" , enterpriseName : "Google"},
  ]

  return (
    <main className="min-h-screen bg-background-neutral">
      <Header links={links}/>
        <section className="min-h-[80vh] my-10 w-3/4 m-auto grid grid-cols-2 gap-5">
        <div className="bg-background">

        </div>
        <div className="flex flex-col w-full h-full justify-between">
          <div className="bg-background h-1/6 p-5 shadow shadow-2xl">
            <h1 className="flex text-2xl font-semibold items-center rounded-[5px]">
              <BriefcaseBusiness className="w-10 h-10 mx-2"/>Vagas para Você
            </h1>
            <p className="m-2 font-light capitalize flex">
              Vagas que melhor se encaixam para voce <Check className="mx-2"/>
            </p>
          </div>
          <JobsGalery jobs={jobs} className="col-start-2 h-4/5 row-start-2 bg-background rounded-[5px] shadow-2xl"/>
        </div>
        </section>
      <Footer/>
    </main>
  )
}
