
class WebServer{

    constructor(user_id, user_name) {
        this.user = 
        {
            'user_id' : user_id,
            'user_name' : user_name,
            'channel_name' : ''
        }

        this.socket = null;
    }

    connect() {
        this.socket = new WebSocket('ws://127.0.0.1:8001/ws/some_path/?user_id='+ this.user.user_id +'&user_name='+ this.user.user_name);

        this.socket.addEventListener('open', this.onOpen.bind(this));
        this.socket.addEventListener('message', this.onMessage.bind(this));
        this.socket.addEventListener('close', this.onClose.bind(this));
        this.socket.addEventListener('error', this.onError.bind(this));
    }


    onOpen(event) {
        console.log('Удачное соединение');
    }

    onMessage(event) {
        const data = JSON.parse(event.data);
        actionUser(this, data);
    }

    onClose(event) {
        console.log('WebSocket connection closed:', event);
    }

    onError(error) {
        console.error('WebSocket error:', error);
    }

    sendMessage(message) {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(JSON.stringify({ message }));
        } else {
            console.error('WebSocket connection is not open.');
        }
    }

}