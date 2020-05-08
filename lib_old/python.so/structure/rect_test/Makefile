all: librect.so librect_c.so

librect.so: rect.cpp
	g++ -o librect.so -fPIC -shared rect.cpp

librect_c.so: rect.c
	gcc -o librect_c.so -fPIC -shared rect.c

clean:
	rm -rf librect.so librect_c.so *.o 

