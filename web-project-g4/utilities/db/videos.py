import os
from flask import url_for
from app import app
from utilities.db.db_manager import dbManager
from uuid import uuid4

########## FETCH  -  SELECT ##########
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
        if video['audio'] == None or video['audio'] == '' or video['audio'] == 'None':
            video['audio'] = url_for('audio_player.static', filename='media/music/happybday.mp3')
        else:
            path = 'media_users/music/' + video['audio']
            video['audio'] = url_for('static', filename=path)

        if video['img'] == None or video['img'] == '' or video['img'] == 'None':
            video['img'] = url_for('audio_player.static', filename='media/img/Black.png')
        else:
            path = 'media_users/img/' + video['img']
            video['img'] = url_for('static', filename=path)
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

    if video['color'] == None or video['color'] == '' or video['color'] == 'None':
        video['color'] = 'white'

    if video['shape'] == None or video['shape'] == '' or video['shape'] == 'None':
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
    if video_list == []:
        return (None, False)

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
    return (res, True)

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

########## COMMIT  -  INSERT, UPDATE, DELETE ##########

# create a new video
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp3', 'wav'}
AUDIO_FILE = ['mp3', 'wav']

def saveFile(file):
    folder = 'img'
    filename = file.filename
    ext = filename.split('.')[-1]
    if ext in AUDIO_FILE:
        folder = 'music'
    filename = str(uuid4()) + '.' + ext
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], folder, filename))
    return filename

def create_a_new_vid(requestForm, user_id:int):
    # fill all important info:
    # assign correct direction
    if 'textDir' in requestForm.form and requestForm.form['textDir'] == 'on':
        dir = 1
    else:
        dir = 0

    # handling the files
    if 'image' in requestForm.files and requestForm.files['image'].filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        imgFilePath = saveFile(requestForm.files['image'])
    else:
        imgFilePath = ''

    if 'audio' in requestForm.files and requestForm.files['audio'].filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        audioFilePath = saveFile(requestForm.files['audio'])
    else:
        audioFilePath = ''

    # only user id is important, it does not come from the video
    query = "INSERT INTO videos(user_id, audio, image, sender_name, card_banner, color, shape, dir)  VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s' , %s);" %(user_id, audioFilePath, imgFilePath, requestForm.form['Audio_Name'], requestForm.form['Choose_Categories'], requestForm.form['playerColorStr'], requestForm.form['shape'], dir)
    last_row_effected = dbManager.commit(query)

    return last_row_effected

# update a video
def update_video(requestForm, user_id:int, id_video:int):
    # update audio:
    if 'audio' in requestForm.files and requestForm.files['audio'].filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        audioFilePath = saveFile(requestForm.files['audio'])
        query = "UPDATE videos SET audio='%s' where user_id=%s and id_video=%s;" % (audioFilePath, user_id, id_video)
        dbManager.commit(query)

    # update image
    if 'image' in requestForm.files and requestForm.files['image'].filename.split('.')[-1] in ALLOWED_EXTENSIONS:
        imgFilePath = saveFile(requestForm.files['image'])
        query = "UPDATE videos SET image='%s' where user_id=%s and id_video=%s;" % (imgFilePath, user_id, id_video)
        dbManager.commit(query)

    # update dir
    dir = 0
    if 'textDir' in requestForm.form:
        dir = 1
    query = "UPDATE videos SET dir=%s where user_id=%s and id_video=%s;" % (dir, user_id, id_video)
    dbManager.commit(query)

    # update sender_name, card_banner, color, shape
    if 'Audio_Name' in requestForm.form and requestForm.form['Audio_Name'] != '' and requestForm.form['Audio_Name'] != 'None':
        query = "UPDATE videos SET sender_name='%s' where user_id=%s and id_video='%s';" % (requestForm.form['Audio_Name'], user_id, id_video)
        dbManager.commit(query)

    if 'Choose_Categories' in requestForm.form and requestForm.form['Choose_Categories'] != '' and requestForm.form['Choose_Categories'] != 'None':
        query = "UPDATE videos SET card_banner='%s' where user_id=%s and id_video='%s';" % (requestForm.form['Choose_Categories'], user_id, id_video)
        dbManager.commit(query)

    if 'playerColorStr' in requestForm.form and requestForm.form['playerColorStr'] != '' and requestForm.form['playerColorStr'] != 'None':
        query = "UPDATE videos SET color='%s' where user_id=%s and id_video='%s';" % (requestForm.form['playerColorStr'], user_id, id_video)
        dbManager.commit(query)

    if 'shape' in requestForm.form and requestForm.form['shape'] != '' and requestForm.form['shape'] != 'None':
        query = "UPDATE videos SET shape='%s' where user_id=%s and id_video='%s';" % (requestForm.form['shape'], user_id, id_video)
        dbManager.commit(query)


# delete a video
def delete_video(id):
    query="DELETE  FROM videos WHERE id_video='%s';" % id
    dbManager.commit(query)