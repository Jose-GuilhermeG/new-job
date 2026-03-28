import type React from "react";
import { useRef } from "react";

interface IconInputProps{
    className? : string;
    icon : React.ReactElement;
    inputType? : React.HTMLInputTypeAttribute;
    name? : string;
    id? : string;
}

export default function IconInput({className , icon , inputType , name , id} : IconInputProps){
    const inputRef = useRef<HTMLInputElement>(null);

    const handlerClick = ()=>inputRef.current?.focus()

    return (
        <div className={`p-2 border border-sidebar-foreground rounded-2xl h-fit flex ${className} text-sidebar-foreground`} onClick={handlerClick}>
            {icon}
            <input type={inputType} name={name} id={id} className="outline-none w-[90%] mx-2" ref={inputRef}/>
        </div>
    )
}