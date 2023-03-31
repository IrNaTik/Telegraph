import React from "react";
import Logo from "src/components/common/logo/logo";
import { updateOpen } from "src/store/chat";
import { useAppDispatch } from "src/store/store";

export function Citem(props: any) {
    const dispatch = useAppDispatch();

    function handleClick(e: any) {
        dispatch(updateOpen());
    }

    return (
        <div className="Citem-Wrapper" onClick={(e) => handleClick(e)}>
            <Logo r={25} size={80}></Logo>
            <div className="Citem-TextBox">
                <div className="Citem-Title">
                    <div className="Citem-Name">Title</div>
                    <div className="Citem-LstMes">01.09</div>
                </div>
                <div className="Citem-Descr">Description</div>
            </div>
        </div>
    );
}
