function userConnected(user, channel_name){
    drawUserPanel(user, channel_name);
}


function userDisconnected(channel_name){
    const userPanel = document.getElementById(channel_name);
    userPanel.remove();
}


function actionUser(self, data){

    const received_data = 
        {
            'status' : data.status,
            'channel_name' : data.channel_name
        }

    if (data.status === 'connected'){
        console.log(data.status, data.user.name);

        if (self.user.channel_name != data.channel_name){
            userConnected(data.user, data.channel_name);
        }

        if (self.user.channel_name == ''){
            self.user.channel_name = data.channel_name
        }


        if (self.user.channel_name == data.channel_name){
            received_data['status'] = 'requestForInformation';
        }
        
    }

    

    if (data.status == 'requestForInformation'){

        if (self.user.channel_name == data.channel_name){
            return;
        }

        received_data['user'] = self.user;
        received_data['status'] = 'responceForInformation'
        received_data['channel_name'] = data.channel_name
    }

    

    if (data.status == 'responceForInformation'){


        drawUserPanel(data.user, data.channel_name);
    }

    if (data.status == 'disconnected'){
        if (self.user.channel_name == data.channel_name){
            return;
        }

        userDisconnected(data.channel_name);
    }


    self.sendMessage(received_data);

}
