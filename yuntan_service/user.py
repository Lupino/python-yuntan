import json
from .gateway import Gateway


class User(Gateway):
    secure = True

    # Create a new user
    # @function UserService::create
    # @async
    # @param {Object} user user data
    # @param {String} user.username UserName
    # @param {String} user.passwd Password
    # @return {User}
    def create(self, username, passwd):
        pathname = '/api/users/'
        return self.request(pathname,
                            'POST',
                            data={
                                'username': username,
                                'passwd': passwd
                            })

    # Get a user
    # @function UserService::get
    # @async
    # @param {String} uidOrName user_id or username
    # @return {User}
    def get(self, uidOrName):
        pathname = '/api/users/{}/'.format(uidOrName)
        return self.request(pathname)

    # Get user list
    # @function UserService::getList
    # @async
    # @param {Object} [query] query string
    # @param {Number} [query.from=0]
    # @param {Number} [query.size=10]
    # @return {Number} from
    # @return {Number} size
    # @return {Number} total
    # @return {User[]} users
    def get_list(self, from_=0, size=10):
        pathname = '/api/users/'
        return self.request(pathname,
                            query={
                                'from': from_,
                                'size': size,
                                'type': type
                            })

    # Remove a user
    # @function UserService::remove
    # @async
    # @param {String} uidOrName user_id or username
    # @return {String}
    def remove(self, uidOrName):
        pathname = '/api/users/{}/'.format(uidOrName)
        return self.request(pathname, 'DELETE')

    # Update user name
    # @function UserService::updateName
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} username New user name
    # @return {String}
    def update_name(self, uidOrName, username):
        pathname = '/api/users/{}/'.format(uidOrName)
        return self.request(pathname, 'POST', data={'username': username})

    # Update user passwd
    # @function UserService::updatePassword
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} passwd New password
    # @return {String}
    def update_password(self, uidOrName, passwd):
        pathname = '/api/users/{}/passwd'.format(uidOrName)
        return self.request(pathname, 'POST', data={'passwd': passwd})

    # Update user extra info
    # @function UserService::updateExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} extra User extra info
    # @return {String}
    def update_extra(self, uidOrName, extra):
        pathname = '/api/users/{}/extra'.format(uidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname, 'POST', data={'extra': extra})

    # Remove user extra info
    # @function UserService::removeExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} extra User extra info
    # @return {String}
    def remove_extra(self, uidOrName, extra):
        pathname = '/api/users/{}/extra'.format(uidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname, 'DELETE', data={'extra': extra})

    # Clear user extra info
    # @function UserService::clearExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} extra User extra info
    # @return {String}
    def clear_extra(self, uidOrName, extra):
        pathname = '/api/users/{}/extra/clear'.format(uidOrName)
        extra = json.dumps(extra)
        return self.request(pathname, 'POST')

    # Update user secure_extra info
    # @function UserService::updateSecureExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} extra User secure_extra info
    # @return {String}
    def update_secure_extra(self, uidOrName, extra):
        pathname = '/api/users/{}/secure_extra'.format(uidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname, 'POST', data={'extra': extra})

    # Remove user secure_extra info
    # @function UserService::removeSecureExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} extra User secure_extra info
    # @return {String}
    def remove_secure_extra(self, uidOrName, extra):
        pathname = '/api/users/{}/secure_extra'.format(uidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname, 'DELETE', data={'extra': extra})

    # Clear user secure_extra info
    # @function UserService::clearSecureExtra
    # @async
    # @param {String} uidOrName user_id or username
    # @return {String}
    def clear_secure_extra(self, uidOrName):
        pathname = '/api/users/{}/secure_extra/clear'.format(uidOrName)
        return self.request(pathname, 'POST')

    # Verify password
    # @function UserService::verifyPassword
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} passwd User password
    # @return {String}
    def verify_password(self, uidOrName, passwd):
        pathname = '/api/users/{}/verify'.format(uidOrName)
        return self.request(pathname, 'POST', data={'passwd': passwd})

    # Create bind
    # @function UserService::createBind
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Bind} bind
    # @param {String} bind.service Bind service
    # @param {String} bind.name    Bind name
    # @param {Object} bind.extra   Bind extra info
    # @return {Bind}
    def create_bind(self, uidOrName, service, name, extra={}):
        pathname = '/api/users/{}/binds'.format(uidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname,
                            'POST',
                            data={
                                'service': service,
                                'name': name,
                                'extra': extra
                            })

    # Get bind
    # @function UserService::getBind
    # @async
    # @param {String} name Bind name
    # @return {Bind}
    def get_bind(self, name):
        pathname = '/api/binds/'
        return self.request(pathname, query={'name': name})

    # Remove bind
    # @function UserService::removeBind
    # @async
    # @param {Number} bidOrName Bind ID or Bind name
    # @return {String}
    def remove_bind(self, bidOrName):
        pathname = '/api/binds/{}/'.format(bidOrName)
        return self.request(pathname, 'DELETE')

    # Update bind extra
    # @function UserService::updateBindExtra
    # @async
    # @param {Number} bidOrName Bind ID or Bind name
    # @param {Object} extra Bind extra value
    # @return {String}
    def update_bind_extra(self, bidOrName, extra):
        pathname = '/api/binds/{}/'.format(bidOrName)
        if not isinstance(extra, str):
            extra = json.dumps(extra)
        return self.request(pathname, 'POST', data={'extra': extra})

    # Get bind list by user
    # @function UserService::getBindListByUser
    # @async
    # @param {String} uidOrName user_id or username
    # @param {Object} [query] query string
    # @param {Number} [query.from=0]
    # @param {Number} [query.size=10]
    # @return {Number} from
    # @return {Number} size
    # @return {Number} total
    # @return {Bind[]} binds
    def get_bind_list_by_user(self, uidOrName, from_=0, size=10):
        pathname = '/api/users/{}/binds/'.format(uidOrName)
        return self.request(pathname, query={'from': from_, 'size': size})

    # Get bind list by service
    # @function UserService::getBindListByService
    # @async
    # @param {String} service bind service
    # @param {Object} [query] query string
    # @param {Number} [query.from=0]
    # @param {Number} [query.size=10]
    # @return {Number} from
    # @return {Number} size
    # @return {Number} total
    # @return {Bind[]} binds
    def get_bind_list_by_service(self, service, from_=0, size=10):
        pathname = '/api/service/{}/binds/'.format(service)
        return self.request(pathname, query={'from': from_, 'size': size})

    # Get bind list by user and service
    # @function UserService::getBindListByUserAndService
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} service bind service
    # @param {Object} [query] query string
    # @param {Number} [query.from=0]
    # @param {Number} [query.size=10]
    # @return {Number} from
    # @return {Number} size
    # @return {Number} total
    # @return {Bind[]} binds
    def get_bind_list_by_user_and_service(self,
                                          uidOrName,
                                          service,
                                          from_=0,
                                          size=10):
        pathname = '/api/users/{}/binds/{}/'.format(uidOrName, service)
        return self.request(pathname, query={'from': from_, 'size': size})

    # Get user list by group
    # @function UserService::getListByGroup
    # @async
    # @param {String} group group name
    # @param {Object} [query] query string
    # @param {Number} [query.from=0]
    # @param {Number} [query.size=10]
    # @return {Number} from
    # @return {Number} size
    # @return {Number} total
    # @return {User[]} users
    def get_list_by_group(self, group, from_=0, size=10):
        pathname = '/api/groups/{}/'.format(group)
        return self.request(pathname, query={'from': from_, 'size': size})

    # Create group
    # @function UserService::createGroup
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} group  group name
    # @return {String} ok
    def create_group(self, uidOrName, group):
        pathname = '/api/groups/{}/{}/'.format(group, uidOrName)
        return self.request(pathname, 'POST')

    # Remove group
    # @function UserService::removeGroup
    # @async
    # @param {String} uidOrName user_id or username
    # @param {String} group  group name
    # @return {String} ok
    def remove_group(self, uidOrName, group):
        pathname = '/api/groups/{}/{}/'.format(group, uidOrName)
        return self.request(pathname, 'DELETE')

    # GraphQL api
    #   type Query {
    #     user(name: String!): User
    #     user(name: Enum!): User
    #     user(id: Int!): User
    #     bind(name: String!): Bind
    #     bind(name: Enum!): Bind
    #     service(service: String!): Service
    #     service_binds(service: String!, from: Int, size: Int): [Bind]
    #     service_bind_count(service: String!)
    #     users(from: Int, size: Int): [User]
    #     user_count: Int
    #     group(group: String): Group
    #   }
    #   type Service {
    #     service: String
    #     binds(from: Int, size: Int): [Bind]
    #     bind_count: Int
    #   }
    #   type Group {
    #     group: String
    #     users(from: Int, size: Int): [User]
    #     user_count: Int
    #   }
    #   type User {
    #     id: Int
    #     name: String
    #     extra: Extra
    #     pick_extra(keys: [String]): Extra
    #     binds(from: Int, size: Int): [Bind]
    #     bind_count: Int
    #     groups: [String]
    #     service(service: String!): Service
    #     created_at: Int
    #   }
    #   type Bind {
    #     id: Int
    #     user_id: Int
    #     user: User
    #     name: String
    #     service: String
    #     extra: Extra
    #     pick_extra(keys: [String]): Extra
    #     created_at: Int
    #   }
    #   type Extra {
    #
    #   }
    # @function CoinService::graphql
    # @async
    # @param {String} query graphql query language
    # @return {Object}
    def graphql(self, query):
        pathname = '/api/graphql/'
        return self.request(pathname, 'POST', data={'query': query})
