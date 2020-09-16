from time import time
import json
from .gateway import Gateway

class Article(Gateway):


    def create(self, title, summary='', content='',
            created_at=str(int(time()))):
        pathname = '/api/articles/'
        body = {
            'title': title,
            'created_at': created_at
        }
        if summary:
            body['summary'] = summary
        if content:
            body['content'] = content

        return self.request(pathname, 'POST', data = body)


    def update(self, art_id, title='', summary='', content=''):
        pathname = '/api/articles/{}/'.format(art_id)
        body = {}
        changed = False
        if title:
            changed = True
            body['title'] = title
        if summary:
            changed = True
            body['summary'] = summary
        if content:
            changed = True
            body['content'] = content

        if not changed:
            return False
        return self.request(pathname, 'POST', data = body)


    def update_extra(self, art_id, extra):
        pathname = '/api/articles/{}/extra'.format(art_id)
        return self.request(pathname, 'POST', data = {'extra': json.dumps(extra)})


    def get_extra(self, art_id, extra_keys=[]):
        pathname = '/api/articles/{}/extra'.format(art_id)
        return self.request(pathname, query = {'extra_keys': ','.join(extra_keys)})


    def remove_extra(self, art_id, extra):
        pathname = '/api/articles/${artId}/extra'.format(art_id);
        return self.request(pathname, 'DELETE', data = { 'extra': json.dumps(extra) })


    def update_cover(self, art_id, file_id):
        pathname = '/api/articles/{}/cover'.format(art_id)
        body = { 'file_id': file_id }
        return self.request(pathname, 'POST', data = body)


    def remove_cover(self, art_id):
        pathname = '/api/articles/{}/cover'.format(art_id)
        return self.request(pathname, 'DELETE')


    # Get article by id
    # @private
    # @async
    # @function ArticleService::get
    # @param {String} artId article id
    # @param {Object} options options
    # @param {[]String} [options.extra_keys=[]] pickup extra by extra_keys
    # @param {[]String} [options.content_keys=[]] pickup content by content_keys
    # @param {String} [options.content_json] decode content with json
    # @param {String} [options.jl] Functional sed for JSON see https://github.com/chrisdone/jl
    # @return {json}
    def get(self, art_id, extra_keys=[], content_json=False, content_keys=[], jl=''):
        pathname = '/api/articles/{}/'.format(art_id)
        return self.request(pathname, query = {
            'extra_keys': ','.join(extra_keys),
            'content_json': content_json,
            'jl': jl,
            'content_keys': ','.join(content_keys)
        })


    def remove(self, art_id):
        pathname = '/api/articles/{}/'.format(art_id)
        return self.request(pathname, 'DELETE')


    def create_tag(self, tag):
        pathname = '/api/tags/'
        return self.request(pathname, 'POST', data={'tag': tag})


    def get_tag(self, tag_id):
        pathname = '/api/tags/{}/'.format(tag_id)
        return self.request(pathname)


    def get_tag_by_name(self, tag):
        pathname = '/api/tags/'
        return self.request(pathname, query={'tag': tag})


    async def add_article_tag(self, art_id, tag):
        pathname = '/api/articles/{}/tags/'.format(art_id)
        await self.create_tag(tag)
        return await self.request(pathname, 'POST', data={'tag': tag})


    # Get article list
    # @private
    # @async
    # @function ArticleService::getList
    # @param {Object} options options
    # @param {Number} [options.from=0]
    # @param {Number} [options.size=10]
    # @param {[]String} [options.extra_keys=[]] pickup extra by extra_keys
    # @param {[]String} [options.content_keys=[]] pickup content by content_keys
    # @param {String} [options.content_json] decode content with json
    # @param {String} [options.jl] Functional sed for JSON see https://github.com/chrisdone/jl
    # @return {json}
    def get_list(self, from_=0, size=10, extra_keys=[], content_json=False, content_keys=[], jl=''):
        pathname = '/api/articles/'
        return self.request(pathname, query={
            'from': from_,
            'size': size,
            'extra_keys': ','.join(extra_keys),
            'content_json': content_json,
            'jl': jl,
            'content_keys': ','.join(content_keys)
        })


    def save_file(self, key, bucket='upload', extra={}):
        pathname = '/api/file/{}'.format(key)
        return self.request(pathname, 'POST', data={
            'bucket': bucket,
            'extra': json.dumps(extra)
        })


    def get_file(self, key):
        pathname = '/api/file/{}'.format(key)
        return self.request(pathname)


    def create_timeline(self, timeline, art_id):
        pathname = '/api/timeline/{}/'.format(timeline)
        return self.request(pathname, 'POST', data={ 'art_id': art_id })


    # Get timeline list
    # @private
    # @async
    # @function ArticleService::getTimelineList
    # @param {String} timeline timeline name
    # @param {Object} options options
    # @param {Number} [options.from=0]
    # @param {Number} [options.size=10]
    # @param {[]String} [options.extra_keys=[]] pickup extra by extra_keys
    # @param {[]String} [options.content_keys=[]] pickup content by content_keys
    # @param {String} [options.content_json] decode content with json
    # @param {String} [options.jl] Functional sed for JSON see https://github.com/chrisdone/jl
    # @return {json}
    def get_timeline(self, timeline, from_=0, size=10, extra_keys=[], content_json=False, content_keys=[], jl=''):
        pathname = '/api/timeline/{}/'.format(timeline)
        return self.request(pathname, query={
            'from': from_,
            'size': size,
            'extra_keys': ','.join(extra_keys),
            'content_json': content_json,
            'jl': jl,
            'content_keys': ','.join(content_keys)
        })


    def clear_extra(self, art_id):
        pathname = '/api/articles/{}/extra/clear'.format(art_id)
        return self.request(pathname, 'POST')


    def remove_article_tag(self, art_id, tag):
        pathname = '/api/articles/{}/tags/'.format(art_id)
        return self.request(pathname, 'DELETE', data={'tag': tag})


    def update_tag(self, tag_id, tag):
        pathname = '/api/tags/{}/'.format(art_id)
        return self.request(pathname, 'POST', data={'tag': tag})


    def remove_timeline(self, timeline, art_id):
        pathname = '/api/timeline/{}/{}/'.format(timeline, art_id)
        return self.request(pathname, 'DELETE')


    def save_timeline_meta(self, timeline, title='', summary=''):
        pathname = '/api/timeline/{}/meta'.format(timeline)
        return self.request(pathname, 'POST', data={'title': title, 'summary': summary})


    def get_timeline_meta(self, timeline):
        pathname = '/api/timeline/{}/meta'.format(timeline)
        return self.request(pathname)


    def remove_timeline_meta(self, timeline):
        pathname = '/api/timeline/{}/meta'
        pathname = '/api/timeline/{}/meta'.format(timeline)
        return self.request(pathname, 'DELETE')


    def graphql(self, query, file_extra={}, article_extra = {}):
        pathname = '/api/graphql'
        return self.request(pathname, 'POST', data = {
            'query': query,
            'file_extra': json.dumps(file_extra),
            'article_extra': json.dumps(article_extra)
        })

    def check_alias(self, alias):
        pathname = '/api/alias/{}'.format(alias)
        return self.request(pathname)

    def remove_alias(self, alias):
        pathname = '/api/alias/{}'.format(alias)
        return self.request(pathname, 'DELETE')

    def save_alias(self, art_id, alias):
        pathname = '/api/articles/{}/alias'.format(art_id)
        return self.request(pathname, 'POST', data = {'alias': alias})
