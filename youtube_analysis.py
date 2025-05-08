import pandas as pd

from googleapiclient.discovery import build

API_KEY = 'Your API Key'



def get_trending_videos(api_key, max_results=200):

    # build the youtube service

    youtube = build('youtube', 'v3', developerKey=api_key)

=E2=80=8B

    # initialize the list to hold video details

    videos = []

    # fetch the most popular videos

    request = youtube.videos().list(

        part='snippet,contentDetails,statistics'</span>,

        chart='mostPopular',

        regionCode='US',  

        maxResults=50</span>

    )

    # paginate through the results if max_results > 50

    while request and len(videos) < max_results:

        response = request.execute()

        for item in response['items']:

                'video_id': item['id'],

                'title': item['snippet']['title'],

                'description': item['snippet']['description'],

                'published_at': item['snippet']['publishedAt'],

                'channel_title': item['snippet']['channelTitle'],

                'category_id': item['snippet']['categoryId'],

                'tags': item['snippet'].get('tags', []),

                'duration': item['contentDetails']['duration'],

<span role="presentation" style="padding-right: 0.1px;">                'definition': item['contentDetails']['definition'],

                'caption': item['contentDetails'].get('caption', 'false'),

                'view_count': item['statistics'].get('viewCount', 0),

                'like_count': item['statistics'].get('likeCount', 0),

                'dislike_count': item['statistics'].get('dislikeCount', 0),

                'favorite_count': item['statistics'].get('favoriteCount', 0),

                'comment_count'</span>: item['statistics'].get('commentCount', 0)

            }

            videos.append(video_details)



        # get the next page token

        request = youtube.videos().list_next(request, response)

    return videos[:max_results]

def save_to_csv(data, filename):

    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

def main():

    trending_videos = get_trending_videos(API_KEY)

    filename = 'trending_videos.csv'

    save_to_csv(trending_videos, filename)

    print(f'Trending videos saved to {filename}')

<span class="cm-keyword">if __name__ == '__main__':

    main()

import pandas as pd

trending_videos = pd.read_csv('trending_videos.csv')</span>

      video_id                                     title  \0  22tVWwmTie8   Eminem - Houdini [Official Music Video]   1  Kf86x8F9M90  College Football 25 | Gameplay Deep Dive   2  mfz-Ztki88s                 ILLEGAL builds in LEGO...   3  VGnOpZhsPk4          ATEEZ(=EC=97=90=EC=9D=B4=ED=8B=B0=EC=A6=88) - 'WORK' Official MV   4  m-4ZM3jxhdE              State of Play | May 30, 2024                                            description          published_at  \0  Eminem - Houdini\nListen: https://eminem.lnk.t...  2024-05-31T04:00:02Z   1  Bring Glory Home. Pre-order EA SPORTS College ...  2024-05-31T14:55:06Z   2  50+ secret ways to build in Lego you probably ...  2024-05-31T15:30:38Z   3  [GOLDEN HOUR : Part.1]\nRelease Date: 2024. 5....  2024-05-31T04:00:01Z   4  State of Play is back! Tune in live for update...  2024-05-30T22:00:12Z                    channel_id      channel_title  category_id  \0  UC20vb-R_px4CguHzzBPhoyQ         EminemVEVO           10   1  UCT4wAMwETXqDf-U_DVuqabA  EA SPORTS College           20   2  UCUU3GdGuQshZFRGnxAPBf_w          TD BRICKS           24   3  UCQdq-lqPEq_yZ_wP_kuVB9Q   KQ ENTERTAINMENT           10   4  UC-2Y8dQb0S6DtpxNgAKoJKA        PlayStation           20                                                   tags  duration definition  \0  ['Eminem', 'Houdini', 'Hip', 'Hop', '=E3=82=A8=E3=83=9F=E3=83=8D=E3=83=A0', '=EC=97=90...   PT4M57S         hd   1  ['college football', 'college football 25', 'c...   PT4M52S         hd   2  ['lego', 'lego set', 'lego sets', 'lego movie'...    PT9M7S         hd   3                                      ['KQ', '=EC=BC=80=EC=9D=B4=ED=81=90']   PT3M15S         hd   4  ['PlayStation', 'PS5', 'video games', 'next ge...  PT35M32S         hd      caption  view_count  like_count  dislike_count  favorite_count  \0     True    14736971     1306831              0               0   1    False     1079642       50259              0               0   2     True     1064281       24723              0               0   3     True    11742765      338559              0               0   4     True     1672973       52456              0               0      comment_count  0         105793  1           6936  2           2690  3          28919  4           8292  

# check for missing values

missing_values = trending_videos.isnull().sum()

# display data types

missing_values, data_types

(video_id          0 title             0 description       4 published_at      0 channel_id        0 channel_title     0 category_id       0 tags              0 duration          0 definition        0 caption           0 view_count        0 like_count        0 dislike_count     0 favorite_count    0 comment_count     0 dtype: int64, video_id          object title             object description       object published_at      object channel_id        object channel_title     object category_id        int64 tags              object duration          object definition        object caption             bool view_count         int64 like_count         int64 dislike_count      int64 favorite_count     int64 comment_count      int64 dtype: object)

# fill missing descriptions with "No description"

trending_videos['description'].fillna('No description', inplace=True)

# convert `published_at` to datetime

trending_videos['published_at'] =</span> pd.to_datetime(trending_videos['published_at'])

# convert tags from string representation of list to actual list

trending_videos['tags'] = trending_videos['tags'].apply(lambda x: eval(x) if isinstance(x, str) else x)

# descriptive statistics

descriptive_stats = trending_videos[['view_count', 'like_count', 'dislike_count', 'comment_count']].describe()

<span class="cm-variable">descriptive_stats

import matplotlib.pyplot <span class="cm-keyword">as plt</span>

sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 3, figsize=</span>(18, 5))

# view count distribution

sns.histplot(<span class="cm-variable">trending_videos['view_count'], bins=30, kde=True, ax=axes[0], color='blue')

axes[<span class="cm-number">0].set_xlabel('View Count')

axes[0].set_ylabel('Frequency')

<span cm-text="">

<span class="cm-comment"># like count distribution

sns.histplot(trending_videos['like_count'], bins=30, kde=True, ax=axes[1], color='green')

axes[1].set_title('Like Count Distribution')

axes[1].set_xlabel('Like Count')

axes[1].set_ylabel('Frequency')

# comment count distribution

sns.histplot(trending_videos['comment_count'], bins=30, kde=True, ax=axes[2], color='red')</span>

axes[2].set_ylabel('Frequency')

plt.tight_layout()

plt.show()

# correlation matrix

correlation_matrix = trending_videos[['view_count', 'like_count', 'comment_count']].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, linecolor='black')

from googleapiclient.discovery import build



youtube = build('youtube', <span class="cm-string">'v3', developerKey=API_KEY)

    request</span> = youtube.videoCategories().list(

        part=</span>'snippet',

        regionCode='US'</pre>

    response = request.execute()

    category_mapping = {}

    for item in response['items']:

        category_id = int(item['id'])

        category_name = item['snippet']['title']

        category_mapping[category_id] = category_name

    return category_mapping

<span role="presentation" style="padding-right: 0.1px;">

<span role="presentation" style="padding-right: 0.1px;"># get the category mapping

category_mapping = get_category_mapping()

print(category_mapping)

{1: 'Film & Animation', 2: 'Autos & Vehicles', 10: 'Music', 15: 'Pets & Animals', 17: 'Sports', 18: 'Short Movies', 19: 'Travel & Events', 20: 'Gaming', 21: 'Videoblogging', 22: 'People & Blogs', 23: 'Comedy', 24: 'Entertainment', 25: 'News & Politics', 26: 'Howto & Style', 27: 'Education', 28: 'Science & Technology', 29: 'Nonprofits & Activism', 30: 'Movies', 31: 'Anime/Animation', 32: 'Action/Adventure', 33: 'Classics', 34: 'Comedy', 35: 'Documentary', 36: 'Drama', 37: 'Family', 38: 'Foreign', 39: 'Horror', 40: 'Sci-Fi/Fantasy', 41: 'Thriller', 42: 'Shorts', 43: 'Shows', 44: 'Trailers'}

trending_videos['category_name'] = trending_videos['category_id'].map(category_mapping)

# Bar chart for category counts

plt.figure(figsize=(12, 8))

sns.countplot(y=trending_videos['category_name'], order=trending_videos['category_name'].value_counts().index, palette='viridis')

plt.title('Number of Trending Videos by Category')

plt.xlabel('Number of Videos')

plt.ylabel('Category')

# average engagement metrics by category

category_engagement = trending_videos.groupby('category_name')[['view_count', 'like_count', 'comment_count']].mean().sort_values(by=</span>'view_count', ascending=False)

fig, axes = plt.subplots(1, 3, figsize=(18, 10))

# view count by category

sns.barplot(y=category_engagement.index, x=category_engagement['view_count'], ax=axes[0], palette='viridis')

axes[0].set_title('Average View Count by Category')

axes[0].set_xlabel(<span class="cm-string">'Average View Count')

axes[0].set_ylabel('Category')

<span class="cm-comment"># like count by category

sns.barplot(y=category_engagement.index, x=category_engagement['like_count'], ax=axes[1], palette='viridis')

axes[1].set_title('Average Like Count by Category')

axes[1].set_xlabel('Average Like Count')

axes[1].set_ylabel('')

<span role="presentation" style="padding-right: 0.1px;"># comment count by category

sns.barplot(y=category_engagement.index, x=category_engagement['comment_count'], ax=axes[2], palette='viridis')

axes[2].set_title('Average Comment Count by Category')

axes[2].set_xlabel('Average Comment Count')

axes[2].set_ylabel('')

<span role="presentation" style="padding-right: 0.1px;">plt.tight_layout()

!pip install isodate

import isodate

# convert ISO 8601 duration to seconds

trending_videos['duration_seconds'] = trending_videos['duration'].apply</span>(lambda x: isodate.parse_duration(x).total_seconds())

trending_videos['duration_range'] = pd.cut(trending_videos['duration_seconds'], bins=[0, 300, 600, 1200, 3600, 7200], labels=['0-5 min', '5-10 min', '10-20 min', '20-60 min', <span class="cm-string">'60-120 min'])

# scatter plot for video length vs view count

plt.figure(figsize=(10, 6))</span>

plt.title('Video Length vs View Count')

plt.xlabel('Video Length (seconds)')

plt.ylabel('View Count')

# bar chart for engagement metrics by duration range

length_engagement = trending_videos.groupby('duration_range')[['view_count', 'like_count'</span>, 'comment_count']].mean()

fig, axes = plt.subplots(1, 3, figsize</span>=(18, 8))

# view count by duration range

axes[0].set_title('Average View Count by Duration Range')

axes[0].set_ylabel('Duration Range')

# like count by duration range</span>

sns.barplot(y=length_engagement.index, x=length_engagement['like_count'], ax=axes[1], palette='magma')

axes[1].set_xlabel('Average Like Count')

# comment count by duration range

sns</span>.barplot(y=length_engagement.index, x=length_engagement['comment_count'], ax=axes[2], palette='magma')

axes[2].set_ylabel('')

plt.tight_layout()

plt.show()

# calculate the number of tags for each video

trending_videos['tag_count'] = trending_videos['tags'].apply(len)

# scatter plot for number of tags vs view count

plt.figure(figsize=(10, 6))

plt.title('Number of Tags vs View Count')

plt.xlabel('Number of Tags')

# extract hour of publication

trending_videos['publish_hour'] = trending_videos['published_at'].dt.hour

# bar chart for publish hour distribution

plt.figure(figsize=(12, 6))

sns.countplot(x='publish_hour', data=trending_videos, palette=</span>'coolwarm')

plt.title('Distribution of Videos by Publish Hour')

plt.xlabel('Publish Hour')

plt.ylabel('Number of Videos')

# scatter plot for publish hour vs view count

plt.figure(figsize=(10, 6))

sns.scatterplot(x='publish_hour', y='view_count', data=trending_videos, alpha=0.6, color='teal')

plt.title('Publish Hour vs View Count')</pre>

plt.xlabel('Publish Hour')