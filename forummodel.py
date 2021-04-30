    
class ForumModel:
    
    def __init__(self, posts):
        self.name = forum_name
        self.url = forum_url
        self.topic = topic
        self.posts = posts

class ForumSite:

    def __init__(self, forum_name, forum_url, topic_tag, posts_tag):
        self.name = forum_name
        self.url = forum_url
        self.topic_tag = topic_tag
        self.posts_tag = posts_tag

class ForumScraper:

    def scrape(forum_site):
        html = requests.get(forum_site.url)

        bs = BeautifulSoup(html.text,'html.parser')
        topic = get_topic(bs, forum_site.topic_tag)
        posts = get_posts(bs, forum_site.posts_tag)
    
    def get_topic(bs, topic_tag):
        topic = bs.select(topic_tag)
        if topic is not None and len(topic) > 0:
            return topic[0].get_text()
        return ''

    def get_posts(bs, posts_tag):
        posts_bs = bs.select(posts_tag)
        posts = []
        for post in posts:
            posts.append(post.get_text())
