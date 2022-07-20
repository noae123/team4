from flask import url_for

# todo delete after connection to db

all_videos = {0:{'audio': None,
                'img':None,
                'sender_name': None,
                'card_banner': None,
                'color': None,
                'shape': None,
                'dir': None,
                'title': None},
              1:{'audio': None,
                'img':None,
                'sender_name': 'noa',
                'card_banner': 'היי היי ביי לכחלךדחכקחכחקק׳חכךק׳חכלחק׳כחךק׳חכלךק׳חכך׳חכך׳חקכך׳חכקך׳כח׳קלךכחקך׳חכ׳ך',
                'color': 'white',
                'shape': 'heart',
                'dir': True,
                'title': 'try card'}}

def get_all_videos(id: int):
    video_dict = {}

    for video in all_videos:
        # this was needed to be generated from db
        video_info = all_videos[video]

        generate_default_pararms(video_info)

        # make this to some kind of string
        VIDEO_ID = 'p' + str(video)

        video_dict[VIDEO_ID] = video_info
    return video_dict

def generate_default_pararms(video: dict, default_text: bool = False):
    if video['audio'] == None:
        video['audio'] = url_for('audio_player.static', filename='media/music/happybday.mp3')

    if video['img'] == None:
        video['img'] = url_for('audio_player.static', filename='media/img/Black.png')

    if video['sender_name'] == None and default_text:
        video['sender_name'] = 'Sender Name'
    elif video['sender_name'] == None:
        video['sender_name'] = ''

    if video['card_banner'] == None and default_text:
        video['card_banner'] = 'Card Banner'
    elif video['card_banner'] == None:
        video['card_banner'] = ''

    if video['color'] == None:
        video['color'] = 'white'

    if video['shape'] == None:
        video['shape'] = 'circle'

    if video['dir'] == None:
        video['dir'] = False

    if video['title'] == None:
        video['title'] = ''

def get_video(video_id:int, user_id:int=None):
    if user_id == None:
        user_id = -1 #-1 is reserved for card 4 u

    # todo get video of user, by user id and video id
    if(video_id in all_videos):
        video_info = all_videos[video_id]
        generate_default_pararms(video_info, True)
        return True, video_info

    else:
        return False, None

def create_empty_video():
    empty = {'audio': None,
                'img':None,
                'sender_name': None,
                'card_banner':None,
                'color': None,
                'shape': None,
                'dir': None,
                'title': None}

    generate_default_pararms(empty, default_text=True)

    empty_id = -1

    return empty_id, empty