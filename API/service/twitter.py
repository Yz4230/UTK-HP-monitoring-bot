import copy

import tweepy

from API.common import APIBase
from crawlers.common import News
from renderers import render_twitter_text


class TwitterAPI(APIBase):
    DEBUG_NAME = __name__
    KEY_NAME = "twitter"

    def broadcast_prod(self, news: News, school_name: str) -> None:
        twitter_tokens = self.get_tokens(school_name)
        if not twitter_tokens:
            return
        auth = tweepy.OAuthHandler(
            twitter_tokens.consumer_key,
            twitter_tokens.consumer_secret
        )
        auth.set_access_token(
            twitter_tokens.access_token,
            twitter_tokens.access_token_secret
        )

        twitter_api = tweepy.API(auth)
        rendered_text = render_twitter_text(copy.copy(news), school_name)
        twitter_api.update_status(rendered_text)
