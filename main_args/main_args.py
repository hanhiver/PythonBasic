import sys
import argparse

def main():
    global logger_manager
    global logger 
    global class_names
    global colors

    print('In main: ', *sys.argv)

    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--model', type = str, default = 'high_way_detector', 
                        help = 'Model name in the TF serving side. DEFAULT: high_way_detector')

    parser.add_argument('-u', '--url', type = str, default = 'localhost:8500', 
                        help = 'URL to the TF gRPC service address. DEFAULT: localhost:8500')

    parser.add_argument('-i', '--input', type = str, default = 'test.mp4', 
                        help = 'Input video. DEFAULT: test.mp4 ')

    parser.add_argument('-o', '--output', type = str, default = '', 
                        help = '[Optional] Output video. ')
    
    parser.add_argument('-l', '--loglevel', type = str, default = 'warning',
                        help = '[Optional] Log level. WARNING is default. ')

    parser.add_argument('-s', '--summary', type = str, default = '',
                        help = '[Optional] Log the fps information. ')

    parser.add_argument('-r', '--recordpath', type = str, default = '', 
                        help = '[Optional] Folder to save the record of incident. ')

    parser.add_argument('-mh', '--modelhost', type = str, default = '', 
                        help = '[Optional] Host of the model server. ')

    parser.add_argument('-mp', '--modelport', type = str, default = '', 
                        help = '[Optional] Port number of the model server. ')  

    parser.add_argument('-lv', '--localview', default = False, action="store_true",
                        help = '[Optional] If shows result to local view. ')    

    # Following two lines added by Mingliang
    parser.add_argument('-n', '--cnumber', type = str, default = '',
                        help = '[Optional] Camera ID (set by GUI). ')

    parser.add_argument('-p', '--port', type = str, default = '',
                        help = '[Optional] Port number to the GUI interface. ')

    parser.add_argument('-t', '--tag', type = str, default = '',
                        help = '[Optional] Tag to recognize the process. ')

    FLAGS = parser.parse_args()

    #logger_manager = loggerManager.LoggerManager(log_level = FLAGS.loglevel)
    #logger = logger_manager.get_logger('Mainfunc')

    #log_str = 'Camera {} Started. Connect to the model server: {}:{}.'.format(
    #            FLAGS.cnumber, FLAGS.modelhost, FLAGS.modelport)
    #logger.info(log_str)



    if 'input' in FLAGS:
        print('Input:   ', FLAGS.input)
        print('Output:  ', FLAGS.output)
        print('Summary: ', FLAGS.summary)
        print('Port:    ', FLAGS.port)
        print('CNumber: ', FLAGS.cnumber)
        print('Rpath:   ', FLAGS.recordpath)
        print('Mhost:   ', FLAGS.modelhost)
        print('Mport:   ', FLAGS.modelport)
        print('LView:   ', FLAGS.localview)

    else:
        print("See usage with --help.")

if __name__ == '__main__':
    print('In file: ', *sys.argv)
    main()  
