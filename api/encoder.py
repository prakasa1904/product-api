# Encoder Class
# Code di bawah ini untuk melihat file info dari upload member
'''
ffprobe -v quiet -show_format -show_streams -print_format json kecil.mp3
'''
# Format data :
'''
{
    "streams": [
        {
            "index": 0,
            "codec_name": "mp3",
            "codec_long_name": "MP3 (MPEG audio layer 3)",
            "codec_type": "audio",
            "codec_time_base": "1/44100",
            "codec_tag_string": "[0][0][0][0]",
            "codec_tag": "0x0000",
            "sample_fmt": "s16p",
            "sample_rate": "44100",
            "channels": 2,
            "channel_layout": "stereo",
            "bits_per_sample": 0,
            "r_frame_rate": "0/0",
            "avg_frame_rate": "0/0",
            "time_base": "1/14112000",
            "start_pts": 353600,
            "start_time": "0.025057",
            "duration_ts": 193536000,
            "duration": "13.714286",
            "bit_rate": "128000",
            "disposition": {
                "default": 0,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0
            },
            "tags": {
                "encoder": "Lavc56.13"
            }
        }
    ],
    "format": {
        "filename": "kecil.mp3",
        "nb_streams": 1,
        "nb_programs": 0,
        "format_name": "mp3",
        "format_long_name": "MP2/3 (MPEG audio layer 2/3)",
        "start_time": "0.025057",
        "duration": "13.714286",
        "size": "219778",
        "bit_rate": "128203",
        "probe_score": 51,
        "tags": {
            "major_brand": "mp42",
            "minor_version": "1",
            "compatible_brands": "mp41mp42isom",
            "encoder": "Lavf56.15.102"
        }
    }
}
'''
# Show format :
'''
ffprobe -v quiet -show_format -print_format json kecil.mp3
'''
# Format Data
'''
{
    "format": {
        "filename": "kecil.mp3",
        "nb_streams": 1,
        "nb_programs": 0,
        "format_name": "mp3",
        "format_long_name": "MP2/3 (MPEG audio layer 2/3)",
        "start_time": "0.025057",
        "duration": "13.714286",
        "size": "219778",
        "bit_rate": "128203",
        "probe_score": 51,
        "tags": {
            "major_brand": "mp42",
            "minor_version": "1",
            "compatible_brands": "mp41mp42isom",
            "encoder": "Lavf56.15.102"
        }
    }
}
'''
