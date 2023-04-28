import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL
from AnonX import app


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def gen_thumb(videoid, user_id):
    if os.path.isfile(f"cache/{videoid}_{user_id}.png"):
        return f"cache/{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

            youtube = Image.open(f"cache/thumb{videoid}.jpg")
            image1 = changeImageSize(1280, 720, youtube)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(30))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            image2 = background
                                                                                            
            circle = Image.open(f"AnonX/assets/anonx.png")

            # changing circle color
            im = circle
            im = im.convert('RGBA')
            color = make_col()

            data = np.array(im)
            red, green, blue, alpha = data.T

            white_areas = (red == 255) & (blue == 255) & (green == 255)
            data[..., :-1][white_areas.T] = color

            im2 = Image.fromarray(data)
            circle = im2
            # done

            image3 = image1.crop((280,0,1000,720))
            lum_img = Image.new('L', [720,720] , 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
            img_arr = np.array(image3)
            lum_img_arr = np.array(lum_img)
            final_img_arr = np.dstack((img_arr,lum_img_arr))
            image3 = Image.fromarray(final_img_arr)
            image3 = image3.resize((600,600))
            

            image2.paste(image3, (50,70), mask = image3)
            image2.paste(circle, (0,0), mask = circle)

            # fonts
            font1 = ImageFont.truetype("AnonX/assets/font.ttf', 30)
            font2 = ImageFont.truetype("AnonX/assets/font.ttf', 70)
            font3 = ImageFont.truetype("AnonX/assets/font.ttf', 40)
            font4 = ImageFont.truetype("AnonX/assets/font.ttf', 35)

            image4 = ImageDraw.Draw(image2)
            image4.text((10, 10), "VENOM x MUSIC", fill="white", font = font1, align ="left") 
            image4.text((670, 150), "NOW PLAYING", fill="white", font = font2, stroke_width=2, stroke_fill="white", align ="left") 

            # title
            title1 = truncate(title)
            image4.text((670, 300), text=title1[0], fill="white", stroke_width=1, stroke_fill="white",font = font3, align ="left") 
            image4.text((670, 350), text=title1[1], fill="white", stroke_width=1, stroke_fill="white", font = font3, align ="left") 

            # description
            views = f"Views : {views}"
            duration = f"Duration : {duration} Mins"
            channel = f"Channel : {channel}"

            image4.text((670, 450), text=views, fill="white", font = font4, align ="left") 
            image4.text((670, 500), text=duration, fill="white", font = font4, align ="left") 
            image4.text((670, 550), text=channel, fill="white", font = font4, align ="left")
            
            image2 = ImageOps.expand(image2,border=20,fill=make_col())
            image2 = image2.convert('RGB')
            image2.save(f"cache/{videoid}.jpg")
            file = f"cache/{videoid}.jpg"
            return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


async def gen_qthumb(videoid, user_id):
    if os.path.isfile(f"cache/que{videoid}_{user_id}.png"):
        return f"cache/que{videoid}_{user_id}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

            youtube = Image.open(f"cache/thumb{videoid}.jpg")
            image1 = changeImageSize(1280, 720, youtube)
            image2 = image1.convert("RGBA")
            background = image2.filter(filter=ImageFilter.BoxBlur(30))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            image2 = background
                                                                                            
            circle = Image.open(f"AnonX/assets/anonx.png")

            # changing circle color
            im = circle
            im = im.convert('RGBA')
            color = make_col()

            data = np.array(im)
            red, green, blue, alpha = data.T

            white_areas = (red == 255) & (blue == 255) & (green == 255)
            data[..., :-1][white_areas.T] = color

            im2 = Image.fromarray(data)
            circle = im2
            # done

            image3 = image1.crop((280,0,1000,720))
            lum_img = Image.new('L', [720,720] , 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
            img_arr = np.array(image3)
            lum_img_arr = np.array(lum_img)
            final_img_arr = np.dstack((img_arr,lum_img_arr))
            image3 = Image.fromarray(final_img_arr)
            image3 = image3.resize((600,600))
            

            image2.paste(image3, (50,70), mask = image3)
            image2.paste(circle, (0,0), mask = circle)

            # fonts
            font1 = ImageFont.truetype("AnonX/assets/font.ttf', 30)
            font2 = ImageFont.truetype("AnonX/assets/font.ttf', 70)
            font3 = ImageFont.truetype("AnonX/assets/font.ttf', 40)
            font4 = ImageFont.truetype("AnonX/assets/font.ttf', 35)

            image4 = ImageDraw.Draw(image2)
            image4.text((10, 10), "VENOM x MUSIC", fill="white", font = font1, align ="left") 
            image4.text((670, 150), "NOW PLAYING", fill="white", font = font2, stroke_width=2, stroke_fill="white", align ="left") 

            # title
            title1 = truncate(title)
            image4.text((670, 300), text=title1[0], fill="white", stroke_width=1, stroke_fill="white",font = font3, align ="left") 
            image4.text((670, 350), text=title1[1], fill="white", stroke_width=1, stroke_fill="white", font = font3, align ="left") 

            # description
            views = f"Views : {views}"
            duration = f"Duration : {duration} Mins"
            channel = f"Channel : {channel}"

            image4.text((670, 450), text=views, fill="white", font = font4, align ="left") 
            image4.text((670, 500), text=duration, fill="white", font = font4, align ="left") 
            image4.text((670, 550), text=channel, fill="white", font = font4, align ="left")
            
            image2 = ImageOps.expand(image2,border=20,fill=make_col())
            image2 = image2.convert('RGB')
            image2.save(f"cache/{videoid}.jpg")
            file = f"cache/{videoid}.jpg"
            return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
