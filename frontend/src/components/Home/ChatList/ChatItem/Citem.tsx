import React from "react";
import Logo from 'src/common/logo/logo';

export function Citem(props: any) {
    return(
        <div className="Citem-Wrapper">
            <Logo r={20} size={80}></Logo>
            <div className="Citem-TextBox">
                <div className="Citem-Name">Title</div>
                <div className="Citem-Descr">Description</div>
            </div>
            <div className="Citem-LstMes">01.09</div>
        </div>
    ) 
}