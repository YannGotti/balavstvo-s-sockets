import json
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer

@database_sync_to_async
def get_user_async(user_id, user_name):
    from user.models import CustomUser
    from .serializers import CustomUserSerializer
    

    try:
        user = CustomUser.objects.get(id=user_id, name=user_name)
        return CustomUserSerializer(user).data
    
    except CustomUser.DoesNotExist:
        return None
    

@database_sync_to_async
def filter_user_async(user_id, user_name):
    from user.models import CustomUser
    from .serializers import CustomUserSerializer
    

    try:
        user = CustomUser.objects.filter(id=user_id, name=user_name)
        return CustomUserSerializer(user, many=True).data
    
    except CustomUser.DoesNotExist:
        return None
    

async def userConnected(self):

    initial_data = self.scope['query_string'].decode('utf-8')
    data = dict(q.split('=') for q in initial_data.split('&'))

    user = await get_user_async(data['user_id'], data['user_name'])

    await self.channel_layer.group_add(
        'players_group',
        self.channel_name
    )

    await self.channel_layer.group_send(
        'players_group',
        {
            'type': 'chat.message',
            'status' : 'connected',
            'channel_name': self.channel_name,
            'user' :  user
        }
    )

async def userDisconnected(self):
    await self.channel_layer.group_send(
        'players_group',
        {
            'type': 'chat.message',
            'status': 'disconnected',
            'channel_name': self.channel_name,
        }
    )
    
    await self.channel_layer.group_discard(
        'players_group',
        self.channel_name
    )



async def actionUser(self, data):

    try:
        status = data['status']
    except:
        return

    if (status == 'requestForInformation'):

        await self.channel_layer.group_send(
            'players_group',
            {
                'type': 'chat.message',
                'status': status,
                'channel_name': data['channel_name'],
            }
        )
       

    if (status == 'responceForInformation'):

        channel_layer = get_channel_layer()
        channel_name = str(data.get('channel_name'))

        try:
            user = await get_user_async(data['user']['user_id'], data['user']['user_name'])

            await channel_layer.send(
                channel_name,
                {
                    'type': 'chat.message',
                    'user': user,
                    'status': status
                }
            )
        except:
            return

        
    