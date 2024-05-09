import requests
import os


def download_video(url, save_path):
    # 发送GET请求获取视频内容
    url = "https://" + url
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 写入视频内容到本地文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"视频 {url} 下载成功！")
    else:
        print(f"视频 {url} 下载失败！")


# 多个视频URL列表
video_urls = [
    "maixiaomeng.oss-cn-hangzhou.aliyuncs.com/material/ovideo/svg/20231120/555247a2-dbb3-488d-8fc1-2fb051cae98b.mp4?type=aliyun",
    "maixiaomeng.oss-cn-hangzhou.aliyuncs.com/material/ovideo/svg/20231120/555247a2-dbb3-488d-8fc1-2fb051cae98b.mp4?type=aliyun",
    "maixiaomeng.oss-cn-hangzhou.aliyuncs.com/material/ovideo/svg/20231120/e2b1454f-bcdc-4ca1-8364-36e18c7c956a.mp4?type=aliyun",

]


# 循环下载每个视频
def main():


    for index, url in enumerate(video_urls):
        # 指定保存路径，以视频在列表中的索引作为文件名
        save_path = f"video_{index + 1}.mp4"
        # 下载视频
        download_video(url, save_path)

if __name__ == "__main__":
    main()
