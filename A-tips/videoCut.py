from moviepy.editor import VideoFileClip, concatenate_videoclips

video_1 = VideoFileClip("/Users/edy/Downloads/zhibo01.mp4")
video_2 = VideoFileClip("/Users/edy/Downloads/zhibo02.mp4")

final_video = concatenate_videoclips([video_1, video_2])

final_video.write_videofile("/Users/edy/Downloads/zhibo8G.mp4")