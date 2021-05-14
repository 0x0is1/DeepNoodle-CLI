from lib.deepnoodlelib import *

def main(filename, outputfile):
    # getting upload request token
    image_id = generate_random_token(TOKLEN_IMGID)
    session_id = generate_random_token(TOKLEN_SESSIONID)
    get_upload_perm(image_id, session_id)
    # uploading image
    upload_image(image_id, session_id, filename)
    # getting result image
    data = get_image(image_id, session_id)
    f=open(outputfile, 'wb+')
    f.write(data)
    f.close()
