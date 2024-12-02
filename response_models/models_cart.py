from datetime import datetime
from typing import Optional, Union

from pydantic import Field

#
# class Article(BaseConfigModel):
#     id_: int = Field(alias="id", strict=True)
#     dateCreated: datetime
#     preview: Optional[str] = None
#     body: str
#     customName: str
#     title: str
#     seoTitle: Optional[str] = None
#     pv: int
#     commenting: bool
#     comments: int
#     likes: list[Like]
#     content: int
#     type: int
#     keywords: Optional[str] = None
#
#
# FeedItem = Union[Article, Banner]
#
#
# class ArticleFeedResponse(BaseConfigModel):
#     content: list[Article]


# class ArticleFeedMoreResponse(BaseConfigModel):
#     articles: list[FeedItem]
#     next: int
#
#     def __init__(self, **data):
#         articles = data.get('articles', [])
#         validated_articles = []
#         for article in articles:
#             if article.get('content') == 5:
#                 validated_articles.append(Banner(**article))
#             else:
#                 validated_articles.append(Article(**article))
#         data['articles'] = validated_articles
#         super().__init__(**data)

