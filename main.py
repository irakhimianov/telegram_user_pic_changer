import time
from config import TG_API_ID, TG_API_HASH
from telethon import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from utils import get_image


client = TelegramClient(session='my_session', api_id=TG_API_ID, api_hash=TG_API_HASH)
client.start()


async def main():
    while True:
        image = get_image()
        current_photo_id = await client.get_profile_photos('me')
        if current_photo_id:
            await client(DeletePhotosRequest(current_photo_id))
        file = await client.upload_file(image)
        await client(UploadProfilePhotoRequest(file))
        time.sleep(59)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())