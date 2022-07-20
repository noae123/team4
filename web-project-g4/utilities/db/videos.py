from flask import url_for
from utilities.db.db_manager import dbManager

def get_all_videos(user_id: int):
    query = "select * from videos where user_id='%s';" % user_id
    video_list = dbManager.fetch(query)

    #check if something was returend
    bool_ans = True
    if video_list == []:
        bool_ans = False

    res = {}
    for video in video_list:
        new_video ={'audio': video.audio,
         'img': video.image,
         'sender_name': video.sender_name,
         'card_banner': video.card_banner,
         'color': video.color,
         'shape': video.shape,
         'dir': video.dir,
         'title': video.video_name}

        generate_default_pararms(new_video)

        res['p' + str(video.id_video)] = new_video
    return (res, bool_ans)

def generate_default_pararms(video: dict, default_text: bool = False):
    try:
        if video['audio'] == None:
            video['audio'] = url_for('audio_player.static', filename='media/music/happybday.mp3')

        if video['img'] == None:
            video['img'] = url_for('audio_player.static', filename='media/img/Black.png')
    except:
        print('need to be run from app.py to see this changes')

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
        user_id = 0  # 0 is reserved for card 4 u

    query = "select * from videos where user_id=%s and id_video=%s;" % (user_id, video_id)
    video_list = dbManager.fetch(query)

    #check if something was returend
    bool_ans = True
    if video_list == []:
        bool_ans = False

    video = video_list[0]
    res ={'audio': video.audio,
     'img': video.image,
     'sender_name': video.sender_name,
     'card_banner': video.card_banner,
     'color': video.color,
     'shape': video.shape,
     'dir': video.dir,
     'title': video.video_name}

    generate_default_pararms(res, True)

    res['p' + str(video.id_video)] = res
    return (res, bool_ans)

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
