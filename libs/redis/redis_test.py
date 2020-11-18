from redis import StrictRedis

import pysnooper 

#@pysnooper.snoop(normalize=False, thread_info=False, depth=1)
def main():
    # 远程连接redis服务，设置一个kv然后再获取。
    redis = StrictRedis(host='11.160.137.194', port=16379, db=0)
    redis.set('name', 'handong')
    print('直接连接: ', redis.get('name'))

    # 使用ConnectionPool来连接。
    from redis import ConnectionPool
    pool = ConnectionPool(host='11.160.137.194', port=16379, db=0)
    redis = StrictRedis(connection_pool=pool)
    print('ConnectionPool连接：', redis.get('name'))

    # 使用URL进行连接
    url = 'redis://11.160.137.194:16379/0'
    pool = ConnectionPool.from_url(url)
    redis = StrictRedis(connection_pool=pool)
    print('通过URL连接：', redis.get('name'))

    print('name是否存在：', redis.exists('name'))
    print('name健值的类型： ', redis.type('name'))
    print('随机选取一个健值： ', redis.randomkey())

if __name__ == '__main__':
    main()