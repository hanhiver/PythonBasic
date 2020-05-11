APP=test libtest.so

all: $(APP)

test: test.cpp Makefile
	g++ -o test test.cpp

libtest.so: test.cpp Makefile
	g++ -o libtest.so -shared -fPIC test.cpp

clean:
	rm -rf test libtest.so
