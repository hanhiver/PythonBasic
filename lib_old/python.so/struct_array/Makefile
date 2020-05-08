all: libtest.so main

libtest.so: test.c 
	gcc -o libtest.so -fPIC -shared test.c

main: libtest.so main.c
	gcc -o main main.c -L . -I . -ltest

#cpptest.so: cpptest.cpp
#	g++ -o cpptest.so -shared -fPIC cpptest.cpp

clean:
	rm -rf libtest.so *.o main cpptest.so

