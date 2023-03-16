import React from "react";

interface IProp {
    r?: number,
    size?: number
}

// default 80 
export default function Logo({ r=80, size=160}: IProp) {

    const center = size / 2;

    return(
        <svg className="Logo-SVG" viewBox={`0 0 ${size} ${size}`} style={{"width":size}}>
            <circle id="MyLogo" cx={center} cy={center} r={r} ></circle>
        </svg>
    )
}