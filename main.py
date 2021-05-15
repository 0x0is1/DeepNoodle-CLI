from lib.deepnoodlelib import *
import uuid

def main():
    # checking ping
    print('[*] Checking ping...')
    status=check_ping()
    if status == 200:
        print('[+] Connection successful!')
    if status == 408:
        print('[-] Connection lost. Your country has banned our server. please use vpn to continue.')
        exit(0)

    # getting upload request token
    image_id = generate_random_token(TOKLEN_IMGID)
    session_id = generate_random_token(TOKLEN_SESSIONID)
    print('[*] Image id: {}'.format(image_id))
    print('[*] Session id: {}'.format(session_id))

    print('[+] Legalising upload token')
    print('[*] {}'.format(get_upload_perm(image_id, session_id)))
    
    # getting filename from user
    filename=input('Enter the Filename: ')
    # uploading image
    print('[+] Uploading image')
    status=upload_image(image_id, session_id, filename)
    if status == 200:
        print('[*] Uploading successful!')
    else:
        print('[-] Uploading Failed. Please check for internet connection.')
        exit(0)
    
    # getting result image
    print('[*] Generating image. It might take up to 20 seconds.')
    data = get_image(image_id, session_id)
    random_image_name=str(uuid.uuid1())

    if data[0] == 200:
        print('[+] Image Downloaded successfully.')
    else:
        print('[-] Image downloading failed. Please try again.')
    f=open(random_image_name+'.jpg', 'wb+')
    f.write(data[1])
    print('[+] Image saved successfully as {}.jpg'.format(random_image_name))
    f.close()

if __name__ == '__main__':
    main()
