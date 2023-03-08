import React, { useState, useEffect } from 'react';
import useWebSocket from 'react-use-websocket';
import { Navigate } from 'react-router-dom';


const WS_URL = 'ws://localhost:8000/ws/chat';


function MediaChat() {
  const [video, setVideo] = useState<any>()
  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ audio: true, video: true })
    .then(function(stream) {
      const mediaSource = new MediaSource()
      setVideo(stream)
      
      console.log(stream.getVideoTracks())
    })
    .catch(function(err) {
      /* обработка ошибки */
    });
  }, [])
  

    return (
      <>
        <video ref={video}></video>
      </>
    );
  }
  
  export default MediaChat;