import darkPool

PORT = '18501'

if __name__ == '__main__':
    #main()
    darkPool.startServer(port = PORT, model_pool_size = 2)
