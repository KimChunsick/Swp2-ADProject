#-*- coding: utf-8 -*-
# PlayList.text파일 불러오기 테스트
def test_playlist_text():
    sample_data = """
    MINO(송민호) - ‘아낙네 (FIANCÉ)’ M/V','NY8VGNft-Zc\r\n
    Red Velvet 레드벨벳 'RBB (Really Bad Boy)' MV','IWJUPY-2EIM\r\n
    TWICE(트와이스) "YES or YES" M/V','mAKsZ26SabQ\r\n
    [M/V] 술탄 오브 더 디스코 - 통배권 (feat. 뱃사공)','r_SI6s9XhPA\r\n
    [M/V] 술탄 오브 더 디스코 - 사라지는 꿈','7fsavq0mU2k\r\n
    Jazzyfact - Smoking Dreams','vJL0KjrK5BA
    """
    sample_data = sample_data.split('\r\n')

    processed_data = list()
    for data in sample_data:
        result = data.lstrip().split("','")
        processed_data.append((result[0], result[1],))

    assert len(processed_data) != 0

    video_dict = dict()
    for key, value in processed_data:
        video_dict[key] = value

    assert len(video_dict) != 0

    print(video_dict)

# 샘플 데이터 파싱 테스트
def test_parse_youtube_search_result():
    import json

    sample_data = \
    r"""
{
    "kind": "youtube#searchListResponse",
    "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/NDakHe6CzTDbhzwxWIMmGKCmCyk\"",
    "nextPageToken": "CAMQAA",
    "regionCode": "KR",
    "pageInfo": {
        "totalResults": 1000000,
        "resultsPerPage": 3
    },
    "items": [
        {
            "kind": "youtube#searchResult",
            "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/im5UsCiOaglsH3W8P1S3Z8T50yY\"",
            "id": {
                "kind": "youtube#video",
                "videoId": "rsvJOrI2GfE"
            },
            "snippet": {
                "publishedAt": "2018-08-03T09:00:00.000Z",
                "channelId": "UCviI9lzTe2pkxJ9M2ArA7WQ",
                "title": "[MV] 기리보이, Kid Milli, NO:EL, 스윙스 - flex (Prod.By 기리보이) [Official Video] (GIRIBOY, 키드밀리, 노엘, Swings)",
                "description": "이번 여름을 책임질 #flex 멜론에서 바로 듣기: https://melon.do/a7TO8qHnO 벅스로 바로 듣기 : https://music.bugs.co.kr/track/31171147 지니로 바로 듣기: ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/rsvJOrI2GfE/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/rsvJOrI2GfE/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/rsvJOrI2GfE/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "dingo freestyle",
                "liveBroadcastContent": "none"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/6cz-y_kt5Bl25q1eAHvgrvAaKUU\"",
            "id": {
                "kind": "youtube#video",
                "videoId": "qq_3yt7RANM"
            },
            "snippet": {
                "publishedAt": "2018-07-31T09:00:53.000Z",
                "channelId": "UCviI9lzTe2pkxJ9M2ArA7WQ",
                "title": "[DF LIVE]기리보이, Kid milli, NO:EL, 스윙스 - flex (Prod.By 기리보이)",
                "description": "이번 여름을 책임질 #flex 멜론에서 바로 듣기: https://melon.do/a7TO8qHnO 벅스로 바로 듣기 : https://music.bugs.co.kr/track/31171147 지니로 바로 듣기: ...",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/qq_3yt7RANM/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/qq_3yt7RANM/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/qq_3yt7RANM/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "dingo freestyle",
                "liveBroadcastContent": "none"
            }
        },
        {
            "kind": "youtube#searchResult",
            "etag": "\"XI7nbFXulYBIpL0ayR_gDh3eu1k/7cjhgkh3C-5SAsezdZdkwsbwoNQ\"",
            "id": {
                "kind": "youtube#video",
                "videoId": "k94UG4eA2AU"
            },
            "snippet": {
                "publishedAt": "2018-08-12T12:50:35.000Z",
                "channelId": "UCgvOZhLzN7znK2fZ9qnMVZQ",
                "title": "flex(Prod.By 기리보이)-기리보이,Kid Milli,NO:EL,스윙스(Swings)가사",
                "description": "flex(Prod.By 기리보이)-기리보이,Kid Milli,NO:EL,스윙스(Swings)가사.",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/k94UG4eA2AU/default.jpg",
                        "width": 120,
                        "height": 90
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/k94UG4eA2AU/mqdefault.jpg",
                        "width": 320,
                        "height": 180
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/k94UG4eA2AU/hqdefault.jpg",
                        "width": 480,
                        "height": 360
                    }
                },
                "channelTitle": "가사가 없어서내가만들었어",
                "liveBroadcastContent": "none"
            }
        }
    ]
}
    """

    json_result = json.loads(sample_data)
    assert len(json_result) != 0
    for temp in json_result['items']:
        title = temp['snippet']['title']
        videoId = temp['id']['videoId']
        assert title != '' and videoId != ''
        print('title: {0}, videoId: {1}'.format(title, videoId))
