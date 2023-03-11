import React from "react";

interface IProp {
    isSender?: boolean;
}

enum Style {
    sender = 'flex-end',
    receiver = 'flex-start'


}

export function Message({isSender=false}:IProp) {
     

    return (
        <div className="Message" style={{
            'alignSelf': isSender? Style.sender: Style.receiver
        }
            
        }>
            <div className="Message-Content">contents test</div>

        </div>
    ) // add svg
} 