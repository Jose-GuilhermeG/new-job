export default function Logo({className} : {className? : string}) {
    return (
        <div className={`p-3 bg-blue-700 w-fit h-fit rounded-[5px] ${className}`}>
            <h1 className="text-2xl text-white font-bold">
                NJ
            </h1>
        </div>
    )
}