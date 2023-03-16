import React from "react";

interface IProp {
    isSender?: boolean;
    content: string | number
}

enum Style {
    sender = 'flex-end',
    receiver = 'flex-start'


}

export function Message({isSender=false, content}:IProp) {
     

    return (
        <div className="Message" style={{
            // 'alignSelf': isSender? Style.sender: Style.receiver
        }   
        }>
            <div className="Message-Content">{content}</div>
        </div>
    ) // add svg
} 