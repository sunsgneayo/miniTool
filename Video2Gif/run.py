import os
import subprocess
import json
import ffmpeg

# 设置要遍历的文件夹路径和输出文件夹路径
input_folder = './ovideo'  # 替换为你的视频文件所在的文件夹路径
output_folder = './nvideo'  # 替换为你想要保存压缩后视频的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历 input_folder 中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):  # 确保处理的是 mp4 文件
        # 设置输入和输出文件的完整路径
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # 使用 ffprobe 获取视频的元数据
        ffprobe_command = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_streams',
            '-show_format',
            input_path
        ]

        # 执行 ffprobe 命令并获取输出
        try:
            probe_result = subprocess.run(ffprobe_command, check=True, stdout=subprocess.PIPE, text=True)
            # 解析输出结果获取宽度和高度
            stream_info = json.loads(probe_result.stdout)
            print(f'视频数据： {stream_info} ')
            width = stream_info['streams'][1]['width']
            height = stream_info['streams'][1]['height']
        except subprocess.CalledProcessError as e:
            print(f'无法获取 {filename} 的元数据: {e}')
            continue
        # 调用 FFmpeg 进行压缩，使用获取到的分辨率
        command = [
            'ffmpeg',
            '-i', input_path,
            '-movflags', 'faststart',  # 修正了之前的参数错误，-r 和 -s 不是连在一起的
            '-r', '25',  # 帧率
            '-s', f'{width}x{height}',  # 使用获取的分辨率
            output_path  # 输出文件
        ]

        # 执行 FFmpeg 命令
        subprocess.run(command, check=True)

        print(f'压缩完成: {filename}')