import os
import subprocess
import json
import asyncio

async  def videoReduce(folder):
    # 遍历 folder 中的所有文件
    for filename in os.listdir(folder):
        if filename.endswith('.mp4'):  # 确保处理的是 mp4 文件
            # 设置输入和输出文件的完整路径
            input_path = os.path.join(folder, filename)
            output_path = os.path.join(folder, f"{filename}_reduce.mp4")

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

                if 'streams' in stream_info and len(stream_info['streams']) >= 2:
                    # 检查第一个流是否有 'width' 键
                    if 'width' in stream_info['streams'][0]:
                        width = stream_info['streams'][0]['width']
                    else:
                        # 如果第一个流没有 'width' 键，检查第二个流
                        width = stream_info['streams'][1].get('width', None)

                    # 检查第一个流是否有 'height' 键
                    if 'height' in stream_info['streams'][0]:
                        height = stream_info['streams'][0]['height']
                    else:
                        # 如果第一个流没有 'width' 键，检查第二个流
                        height = stream_info['streams'][1].get('height', None)
                else:
                    # 如果 'streams' 不存在或列表中的元素不足两个，设置默认值或进行其他处理
                    width = None
                    height = None

                print(f'with width: {width} and height: {height}')
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


if '__main__' == __name__:
    input_path = input("输入视频文件目录:")
    if not os.path.exists(input_path):
        print(f' {input_path} <- 文件目录不存在')
        # 结束运行
    else:
        print(f' {input_path} <- 正在打开目录...')
        asyncio.run(videoReduce(input_path))
        # videoReduce(input_path)
        input("Tip: 回车！ 关闭窗口")