all:
	gcc -o libtest.so -fPIC -shared test.c
	gcc -o main main.c -L . -I . -ltest 

clean:
	rm -rf libtest.so *.o main
