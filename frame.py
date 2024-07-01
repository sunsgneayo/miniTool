#!/usr/bin/env python

import os
import ffmpeg


# 遍历目录下的mp4文件，提取第一帧为png
def process_mp4_files_in_dir(directory):
    print(f'Processing MP4 files in directory: {directory}')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                input_file = os.path.join(root, file)
                # 输出文件名（添加后缀或改变扩展名）
                base, ext = os.path.splitext(file)
                output_file = os.path.join(root, f"{base}.png")

                # 使用ffmpeg提取第一帧
                (
                    ffmpeg
                    .input(input_file, ss=0, vframes=1)  # ss=0表示从视频开始处提取，vframes=1表示只提取一帧
                    .output(output_file, vcodec='png')  # 指定输出格式为png
                    .run()
                )
                print(f"Processed {input_file} to {output_file}")


if __name__ == '__main__':
    input_path = input("输入视频文件路径:")
    print(input_path)

    # 确保输入的路径存在
    if os.path.exists(input_path):
        process_mp4_files_in_dir(input_path)
    else:
        print("输入的路径不存在，请检查路径是否正确。")

    input("按Enter键关闭窗口...")