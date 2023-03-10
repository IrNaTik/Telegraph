import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';
import { Navigate } from 'react-router-dom';


const WS_URL = 'ws://localhost:8000/ws/chat';


function MediaChat() {
  let localConnection = new RTCPeerConnection()
  
  let sendChannel = localConnection.createDataChannel("sendChannel");
  sendChannel.onopen = handleSendChannelStatusChange;
  sendChannel.onclose = handleSendChannelStatusChange;
  
  function handleSendChannelStatusChange(event: any) {
    console.log('Status change')
    // if (sendChannel) {
    //   var state = sendChannel.readyState;
    
    //   if (state === "open") {
    //     messageInputBox.disabled = false;
    //     messageInputBox.focus();
    //     sendButton.disabled = false;
    //     disconnectButton.disabled = false;
    //     connectButton.disabled = true;
    //   } else {
    //     messageInputBox.disabled = true;
    //     sendButton.disabled = true;
    //     connectButton.disabled = false;
    //     disconnectButton.disabled = true;
    //   }
    // }
  }
  


  // const [video, setVideo] = useState<any>()
  // useEffect(() => {
  //   navigator.mediaDevices.getUserMedia({ audio: true, video: true })
  //   .then(function(stream) {
  //     const mediaSource = new MediaSource()
  //     setVideo(stream)
      
  //     console.log(stream.getVideoTracks())
  //   })
  //   .catch(function(err) {
  //     /* обработка ошибки */
  //   });
  // }, [])


    return (
      <>
        
      </>
    );
  }
  
  export default MediaChat;