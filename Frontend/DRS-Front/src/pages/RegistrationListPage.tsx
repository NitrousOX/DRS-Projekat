import {useEffect, useState} from "react"
import io, {Socket} from 'socket.io-client'

const socket: Socket = io('http://127.0.0.1:5000')


export default function RegistrationListPage(){
    const [message, setMessage] = useState<string>('');
    const [response, setResponse] = useState<string>('');

    useEffect(() => {
        // Socket.IO event listeners
        socket.on('connected', (data: { data: string }) => {
          console.log('Connected to server:', data.data);
        });
    
        socket.on('server_response', (data: { data: string }) => {
          setResponse(data.data);
        });
    
        // Cleanup on unmount
        return () => {
          socket.disconnect();
        };
      }, []);

      const sendMessage = () => {
        socket.emit('client_message', { message });
      };
      return (
        <div>
          <h1>Registration List Page</h1>
          <div>
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Enter a message"
            />
            <button onClick={sendMessage}>Send</button>
            <p>Server Response: {response}</p>
          </div>
        </div>
      );
};