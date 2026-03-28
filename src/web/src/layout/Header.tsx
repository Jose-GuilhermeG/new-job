import Logo from "@/components/Logo";
import IconInput from "@/components/ui/IconInput";
import type { IconLink } from "@/types/gerelaTypes";
import { Search } from "lucide-react";

import { Link } from "react-router-dom";

interface HeaderProps{
    links : Array<IconLink>
}

export default function Header({links} : HeaderProps){

    return (
        <header className="w-full h-[8vh] sticky top-0 bg-background">
            <nav className="grid grid-cols-3 w-4/5 m-auto h-full">
                <Link to="/" className="m-auto">
                    <Logo/>
                </Link>
                <div className="m-auto w-full relative">
                    <IconInput inputType="search" icon={<Search/>}/>
                </div>
                <ul className="m-auto flex w-full h-full justify-center items-center px-5 [&_li]:mx-10">
                    {links.map(element=>(
                        <li>
                            <Link to={element.link}>
                                {element.icon}
                            </Link>
                        </li>
                    ))}
                </ul>
            </nav>
        </header>
    )
}