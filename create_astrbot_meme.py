from astrbot.api.event import AstrMessageEvent
from astrbot.api import logger

async def erciyuan(event: AstrMessageEvent):
    logger.info(event.message_obj.raw_message)
    url = "https://api.lolimi.cn/API/preview/api.php?action=create_meme&qq=401693349&msg=%E5%97%A3/%E5%AB%A3%E7%84%B6%E9%83%A1%E4%B8%BB.%E8%90%A7%E7%AC%99%E7%AC%99.%E8%B4%B0.%E6%99%AF%E8%A1%8D%E7%8E%8B%E5%BA%9C.6300&type=4"
    return url