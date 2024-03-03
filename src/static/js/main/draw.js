

function drawUserPanel(user, channel_name){
    const users_list_panel = document.getElementById('users_list_panel');

    html = 
    `
    <div class="hstack gap-2 p-2" style="background-color: rgba(0, 0, 0, 0.212); border-radius: 10px;" id="${channel_name}">
        <img src="${user.photo_profile}" style="width: 50px; height: 50px;border-radius: 10px;">
        <div class="vstack">

            <h5 class="text-h5-custom">${user.name}</h5>
            <h5 class="text-h5-custom">${user.type_user}</h5>

        </div>
    </div>
    `

    users_list_panel.innerHTML += html;
}