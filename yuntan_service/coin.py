import json
from datetime import datetime

from .gateway import Gateway


class Coin(Gateway):
    secure = True

    def getScore(self, name):
        '''
        Get coin score
        @function Coin::getScore
        @async
        @param {String} name name
        @return {Number}
        '''

        pathname = '/api/coins/{}/score/'.format(name)
        return self.request(pathname)

    def getInfo(self, name):
        '''
        Get coin info
        @function Coin::getInfo
        @async
        @param {String} name name
        @return {Number} score
        @return {String} name
        @return {Object} info
        '''
        pathname = '/api/coins/{}/info/'.format(name)
        return self.request(pathname)


    def putInfo(self, name, json):
        '''
        Put coin info
        @function Coin::putInfo
        @async
        @param {String} name name
        @param {Object} info coin info
        '''

        pathname = '/api/coins/{}/info/'.format(name)
        return self.request(pathname, 'PUT', data = json, is_json = True)

    def dropCoin(self, name):
        '''
        Drop coin data
        @function Coin::dropCoin
        @async
        @param {String} name name
        '''
        pathname = '/api/coins/{}/drop/'.format(name)
        return self.request(pathname, 'POST')


    def getList(self, name, query = {}):
        '''
        Get coin list
        @function Coin::getList
        @async
        @param {String} name name
        @param {Object} [query] query string
        @param {Number} [query.from=0]
        @param {Number} [query.size=10]
        @param {String} [query.type]
        @return {Number} from
        @return {Number} size
        @return {Number} total
        @return {Coin[]} coins
        '''
        pathname = '/api/coins/{}/'.format(name)
        return self.request(pathname, query=query)


    def getListWithNameSpace(self, name, namespace, query = {}):
        '''
        Get coin list with namespace
        @function Coin::getList
        @async
        @param {String} name name
        @param {String} namespace namespace
        @param {Object} [query] query string
        @param {Number} [query.from=0]
        @param {Number} [query.size=10]
        @param {String} [query.type]
        @return {Number} from
        @return {Number} size
        @return {Number} total
        @return {Coin[]} coins
        '''
        pathname = '/api/coins/{}/namespace/{}/'.format(name, namespace)
        return self.request(pathname, query=query)


    def getHistories(self, query = {}):
        '''
        Get coin history list
        @function Coin::getHistories
        @async
        @param {Object} [query] query string
        @param {Number} [query.from=0]
        @param {Number} [query.size=10]
        @param {Number} [query.start_time=0]
        @param {Number} [query.end_time=now]
        @return {Number} from
        @return {Number} size
        @return {Number} total
        @return {Coin[]} coins
        '''
        pathname = '/api/histories/'
        return self.request(pathname, query=query)


    def getHistoriesByNameSpace(self, namespace, query = {}):
        '''
        Get coin history list by namespace
        @function Coin::getHistoriesByNameSpace
        @async
        @param {String} namespace spec namespace
        @param {Object} [query] query string
        @param {Number} [query.from=0]
        @param {Number} [query.size=10]
        @param {Number} [query.start_time=0]
        @param {Number} [query.end_time=now]
        @return {Number} from
        @return {Number} size
        @return {Number} total
        @return {Coin[]} coins
        '''
        pathname = '/api/histories/{}/'.format(namespace)
        return self.request(pathname, query)


    def save(self, name, **form):
        '''
        Save coin
        @function Coin::save
        @async
        @param {Coin} coin
        @param {String} coin.name coin name
        @param {String} coin.namespace spec namespace
        @param {Number} coin.score coin score
        @param {String} [coin.desc] coin description
        @param {String} coin.type One of Incr, Decr, incr, decr
        @return {Number} - current score
        '''
        pathname = '/api/coins/{}/'.format(name)
        return self.request(pathname, 'POST', data = form})


    def graphql(self, query):
        '''
        GraphQL api
          type Query {
            coin(name: String!): Coin
          }
          type Coin {
            history(from: Int, size: Int): [CoinHistory]
            total: Int
            score: Int
            info: CoinInfo
          }
          type CoinHistory {
            score: Int
            pre_score: Int
            type: String
            desc: String
            created_at: Int
          }
          type CoinInfo {

          }

        @function Coin::graphql
        @async
        @param {String} query graphql query language
        @return {Object}
        '''
        pathname = '/api/graphql/'
        return self.request(pathname, 'POST', data={ 'query' : query })


    def graphqlByName(self, name, query):
        '''
        GraphQL api by name

          type Query {
            history(from: Int, size: Int): [CoinHistory]
            total: Int
            score: Int
            info: CoinInfo
          }
          type CoinHistory {
            score: Int
            pre_score: Int
            type: String
            desc: String
            created_at: Int
          }
          type CoinInfo {

          }

        @function Coin::graphqlByName
        @async
        @param {String} name name
        @param {String} query graphql query language
        @return {Object}
        '''
        pathname = '/api/graphql/{}/'.format(name)
        return self.request(pathname, 'POST', data={ 'query' : query })
