import Footer from "@/layout/Footer"
import Header from "@/layout/Header"
import type { IconLink } from "@/types/gerelaTypes"
import { User , BriefcaseBusiness } from "lucide-react"

export default function Home() {
  const links : Array<IconLink> = [
    {icon : <BriefcaseBusiness/> , link : ""},
    {icon : <User/> , link : ""},
  ]
  return (
    <main className="h-screen bg-background-neutral">
      <Header links={links}/>
        <section className="min-h-[100vh]">
          
        </section>
      <Footer/>
    </main>
  )
}
