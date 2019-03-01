all: libtest.so main

libtest.so: test.c 
	gcc -o libtest.so -fPIC -shared test.c

main: test.c
	gcc -o main test.c -L . -I . -ltest

clean:
	rm -rf libtest.so *.o main 

